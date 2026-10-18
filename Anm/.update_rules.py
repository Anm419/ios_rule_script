from pathlib import Path
from collections import defaultdict, deque, Counter
from functools import lru_cache
from datetime import datetime
from zoneinfo import ZoneInfo
import re, ipaddress, subprocess, json, sys

ROOT=Path('Anm')
STAMP=datetime.now(ZoneInfo('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
APPLY='--apply' in sys.argv
URL='https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/reject.txt'

def lines(text):
    out=[]
    for l in text.splitlines():
        l=l.strip()
        if not l or l.startswith(('#','//',';')): continue
        # These sources have no inline annotations; fail rather than truncate values.
        assert not re.search(r'\s+(#|//)',l), l
        out.append(l)
    return out

def normalize(l):
    if l.startswith(('IP-CIDR,','IP-CIDR6,','IP-ASN,','GEOIP,')):
        return l if 'no-resolve' in l.split(',')[2:] else l+',no-resolve'
    if l.startswith(('OR,','AND,','NOT,')):
        return re.sub(r'((?:IP-CIDR6?|IP-ASN|GEOIP),[^()]+)',lambda m:normalize(m[0]),l)
    return l

def key(l):
    t,v,*opts=l.split(',')
    if t in ('IP-CIDR','IP-CIDR6'): v=str(ipaddress.ip_network(v,strict=False))
    if t in ('DOMAIN','DOMAIN-SUFFIX'): v=v.lower().rstrip('.')
    if t=='DOMAIN-KEYWORD': v=v.lower()
    return t,v,tuple(opts)

def unique(ls):
    seen=set();out=[]
    for l in ls:
        k=key(l)
        if k not in seen: seen.add(k);out.append(l)
    return out

@lru_cache(None)
def source(p):
    if p.startswith('http'):
        cache=ROOT/'.reject-source.tmp'
        if not cache.exists():
            r=subprocess.run(['curl','-fLsS','--retry','2','--max-time','120',p],check=True,capture_output=True)
            raw=r.stdout.decode('utf-8-sig')
            assert len(lines(raw))>1000 and all(x.startswith(('DOMAIN,','DOMAIN-SUFFIX,')) for x in lines(raw)), 'Unexpected reject payload'
            cache.write_text(raw)
        raw=cache.read_text()
    else: raw=Path(p).read_text()
    ls=lines(raw)
    if p.endswith('_Domain.list'):
        assert all(',' not in l for l in ls)
        ls=['DOMAIN-SUFFIX,'+l[1:] if l.startswith('.') else 'DOMAIN,'+l for l in ls]
    return unique(ls)

# Exact wildcard-language containment, including union coverage, using NFA products.
def closure(pats,states):
    out=set(states);todo=list(states)
    while todo:
        i,j=todo.pop()
        if j<len(pats[i]) and pats[i][j]=='*' and (i,j+1) not in out:
            out.add((i,j+1));todo.append((i,j+1))
    return frozenset(out)
def step(pats,states,ch):
    out=set()
    for i,j in states:
        if j==len(pats[i]):continue
        x=pats[i][j]
        if x=='*':out.add((i,j))
        elif x=='?' or x==ch:out.add((i,j+1))
    return closure(pats,out)
def accept(pats,states):return any(j==len(pats[i]) for i,j in states)
@lru_cache(None)
def glob_covered(src,targets):
    if not targets:return False
    if src in targets:return True
    pats=(src,);alphabet=set(''.join(pats+targets))-{'*','?'};alphabet.add('\0')
    start=(closure(pats,{(0,0)}),closure(targets,{(i,0) for i in range(len(targets))}))
    todo=[start];seen={start}
    while todo:
        a,b=todo.pop()
        if accept(pats,a) and not accept(targets,b):return False
        for c in alphabet:
            aa=step(pats,a,c)
            if not aa:continue
            state=(aa,step(targets,b,c))
            if state not in seen:seen.add(state);todo.append(state)
    return True

class Coverage:
    def __init__(self,rules):
        self.rules=unique(rules);self.keys={key(l) for l in self.rules}
        self.by=defaultdict(list)
        for l in self.rules:
            t,v,*opts=l.split(',')
            assert t in ('DOMAIN','DOMAIN-SUFFIX','DOMAIN-KEYWORD','IP-CIDR','IP-CIDR6','IP-ASN','USER-AGENT','PROCESS-NAME','URL-REGEX'),l
            assert not opts or (t.startswith('IP-') and opts==['no-resolve']), l
            self.by[t].append((v,tuple(opts)))
        self.domains={v.lower().rstrip('.') for v,o in self.by['DOMAIN']}
        self.suffixes={v.lower().rstrip('.') for v,o in self.by['DOMAIN-SUFFIX']}
        self.keywords={v.lower() for v,o in self.by['DOMAIN-KEYWORD']}
    def domain(self,t,v):
        v=v.lower().rstrip('.') if t!='DOMAIN-KEYWORD' else v.lower()
        if any(k in v for k in self.keywords):return True
        if t=='DOMAIN-KEYWORD':return False
        if t=='DOMAIN' and v in self.domains:return True
        labels=v.split('.')
        return any('.'.join(labels[i:]) in self.suffixes for i in range(len(labels)))
    def covered(self,l):
        if key(l) in self.keys:return True
        t,v,*opts=l.split(',')
        if t in ('DOMAIN','DOMAIN-SUFFIX','DOMAIN-KEYWORD'):return self.domain(t,v)
        if t in ('IP-CIDR','IP-CIDR6'):
            n=ipaddress.ip_network(v,strict=False);lo=int(n.network_address);hi=int(n.broadcast_address)
            ranges=[]
            for value,o in self.by[t]:
                # A no-resolve target cannot cover a source that triggers resolution.
                # A resolving target does cover an already-resolved/IP-literal source match.
                if 'no-resolve' in o and 'no-resolve' not in opts:continue
                nn=ipaddress.ip_network(value,strict=False)
                a,b=int(nn.network_address),int(nn.broadcast_address)
                if b>=lo and a<=hi:ranges.append((a,b))
            pos=lo
            for a,b in sorted(ranges):
                if a>pos:return False
                pos=max(pos,b+1)
                if pos>hi:return True
            return False
        if t=='USER-AGENT':return glob_covered(v,tuple(x for x,o in self.by[t]))
        if t=='PROCESS-NAME':return False
        if t=='URL-REGEX':
            if v==r'^https?:\/\/www\.amazon\.com\/(Amazon-Video|gp\/video)\/':
                return self.domain('DOMAIN','www.amazon.com')
            # Unanchored expression can match a path on arbitrary hosts: no domain rule covers it.
            assert v==r'assets\d+\.xboxlive\.(com|cn)',v
            assert not self.by['URL-REGEX']
            return False
        if t=='IP-ASN':
            assert v=='132203' and not self.by['IP-ASN'],l
            # RIPE announced-prefixes confirms AS132203 contains 43.152.94.0/23.
            # An IP-literal witness in this prefix falls outside every China target range.
            ip=ipaddress.ip_address('43.152.94.1')
            assert not any(ip in ipaddress.ip_network(x,strict=False) for x,o in self.by['IP-CIDR'])
            assert not self.domain('DOMAIN',str(ip))
            return False
        raise AssertionError(l)

# Regression checks for boundaries, union CIDRs, partial overlap and options.
assert Coverage(['DOMAIN-SUFFIX,acfun.cn']).covered('DOMAIN,b.acfun.cn')
assert not Coverage(['DOMAIN-SUFFIX,acfun.cn']).covered('DOMAIN,notacfun.cn')
assert not Coverage(['DOMAIN-SUFFIX,b.acfun.cn']).covered('DOMAIN-SUFFIX,acfun.cn')
assert Coverage(['IP-CIDR,10.0.0.0/25','IP-CIDR,10.0.0.128/25']).covered('IP-CIDR,10.0.0.0/24')
assert not Coverage(['IP-CIDR,10.0.0.0/25']).covered('IP-CIDR,10.0.0.0/24')
assert not Coverage(['IP-CIDR,10.0.0.0/24,no-resolve']).covered('IP-CIDR,10.0.0.0/24')
assert Coverage(['IP-CIDR,10.0.0.0/24']).covered('IP-CIDR,10.0.0.0/24,no-resolve')
assert Coverage(['IP-CIDR6,2001:db8::/33','IP-CIDR6,2001:db8:8000::/33']).covered('IP-CIDR6,2001:db8::/32')
assert glob_covered('TIDAL*dia',('TIDAL*',))
assert not glob_covered('*Spotify*',('Spotify*',))
assert glob_covered('a*',('a','a?*'))
assert not glob_covered('YouTube*',('youtube*',))

files={};readmes={};operations={}
for sw in ('Surge','Loon'):
    rp=ROOT/sw/'README.md';readmes[sw]=rp.read_text()
    operations[sw]=re.findall(r'^- .+(?:\n\n```(?:text|diff)\n[\s\S]*?\n```)?',readmes[sw],re.M)
    for p in sorted((ROOT/sw/'rule').rglob('*.list')):
        text=p.read_text(); groups=[]
        for block in re.split(r'(?=^# SOURCE: )',text,flags=re.M):
            if not block.strip():continue
            ls=block.rstrip('\n').splitlines()
            assert ls[0].startswith('# SOURCE: ') and ls[1].startswith('# UPDATE: ') and ls[2].startswith('# REMARK: '),p
            s=ls[0][10:];rules=lines('\n'.join(ls[3:]));assert f'`{s.split("#")[0]}`' in readmes[sw] or s.startswith(f'Anm/{sw}/README.md#'),s
            groups.append(dict(source=s,headers=ls[:3],old=rules,new=None))
        files[str(p)]=dict(path=p,sw=sw,old=text,groups=groups)

# Reconstruct all full imports and verify manual additions against README, not stale source results.
for f in files.values():
    for g in f['groups']:
        s=g['source']
        if s.startswith('Anm/'):
            g['new']=g['old'][:]
            continue
        dynamic='/GlobalMedia/' in s or ('/Inner/Synthesis/' in str(f['path']) and '/XianYu/' not in s)
        if not dynamic:g['new']=source(s)[:]
    for s in {g['source'] for g in f['groups'] if g['source'].startswith('Anm/')}:
        matching=[op for op in operations[f['sw']] if '用户自定义' in op and f'`{f["path"]}`' in op]
        assert len(matching)==1,(f['path'],matching)
        documented=re.search(r'```text\n([\s\S]*?)\n```',matching[0])[1]
        actual=[l for g in f['groups'] if g['source']==s for l in g['new']]
        assert actual==lines(documented),(s,actual,lines(documented))

def rules_of(p,exclude=None):
    return unique([l for g in files[p]['groups'] if not exclude or exclude not in g['source'] for l in (g['new'] if g['new'] is not None else [])])

for sw in ('Surge','Loon'):
    base=f'Anm/{sw}/rule/'
    globalfile=files[base+'Out/Global/Global_All.list']
    cov=Coverage(rules_of(str(globalfile['path']),'/GlobalMedia/'))
    for g in globalfile['groups']:
        if '/GlobalMedia/' in g['source']:g['new']=[l for l in source(g['source']) if not cov.covered(l)]
    synth=files[base+'Inner/Synthesis/Synthesis_Inner.list']
    china=Coverage(rules_of(base+'Inner/China/China_All.list'))
    upstream_china=Coverage(source(f'rule/{sw}/China/China_All.list') if sw=='Surge' else source('rule/Loon/China/China_Domain.list')+source('rule/Loon/China/China_Resolve.list'))
    for g in synth['groups']:
        s=g['source']
        if '/Alibaba/' in s or g['new'] is not None:continue
        src=source(s)
        if sw=='Loon' and s=='rule/Surge/WeChat/WeChat.list':
            native={key(l) for l in source('rule/Loon/WeChat/WeChat.list')}
            src=[l for l in src if l.startswith(('DOMAIN-KEYWORD,','IP-CIDR,','IP-CIDR6,')) and key(l) not in native]
        comparison=upstream_china if '/WeChat/' in s else china
        g['new']=[l for l in src if not comparison.covered(l)]
    # Dependencies include ALL current non-Alibaba groups, regardless of output order.
    cov=Coverage(rules_of(base+'Inner/China/China_All.list')+rules_of(str(synth['path']),'/Alibaba/'))
    for g in synth['groups']:
        if '/Alibaba/' in g['source']:g['new']=[l for l in source(g['source']) if not cov.covered(l)]

changes=[];docchanges=[]
for path,f in files.items():
    seen=set();blocks=[]
    for g in f['groups']:
        assert g['new'] is not None,g
        out=[]
        for l in g['new']:
            l=normalize(l);k=key(l)
            if k not in seen:seen.add(k);out.append(l)
        g['final']=out
        if not out:continue
        headers=g['headers'][:]
        if out!=g['old']:headers[1]='# UPDATE: '+STAMP
        blocks.append('\n'.join(headers+out))
    new='\n\n'.join(blocks)+'\n'
    f['result']=new
    if new!=f['old']:
        oldrules=lines(f['old']);newrules=lines(new)
        oldset=set(oldrules);newset=set(newrules)
        added=[l for l in newrules if l not in oldset]
        removed=[l for l in oldrules if l not in newset]
        changes.append(dict(path=path,added=len(added),removed=len(removed),before=len(oldrules),after=len(newrules)))
        print('CHANGE',path,'+',len(added),'-',len(removed))
        if len(added)+len(removed)<100:
            for l in removed:print(' -',l)
            for l in added:print(' +',l)
    for g in f['groups']:
        s=g['source']
        dynamic='/GlobalMedia/' in s or ('/Inner/Synthesis/' in path and '/XianYu/' not in s)
        if not dynamic:continue
        ops=[op for op in operations[f['sw']] if op.startswith(f'- 将 `{s}`') and '未覆盖' in op and f'`{path}`' in op]
        assert len(ops)==1,(s,ops)
        oldop=ops[0];bullet=oldop.split('\n')[0];out=g['final']
        newop=bullet+('\n\n```text\n'+'\n'.join(out)+'\n```' if 1<=len(out)<=50 else '')
        print('FILTER',s,'source',len(source(s)),'written',len(out))
        if newop!=oldop:
            assert readmes[f['sw']].count(oldop)==1
            readmes[f['sw']]=readmes[f['sw']].replace(oldop,newop)
            docchanges.append(dict(software=f['sw'],source=s,count=len(out)))

if APPLY:
    for f in files.values():
        if f['result']!=f['old']:f['path'].write_text(f['result'])
    for sw,txt in readmes.items():
        p=ROOT/sw/'README.md'
        if txt!=p.read_text():p.write_text(txt)
    print('APPLIED',STAMP)
print('SUMMARY',json.dumps({'stamp':STAMP,'changes':changes,'readme':docchanges},ensure_ascii=False))
