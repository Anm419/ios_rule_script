## Process

- 将用户自定义的以下规则添加到 `Anm/Surge/rule/Process/Process.list`（仅 Surge Mac 支持，iOS 忽略；Loon 不支持进程匹配，无法等价转换，沿用其他规则分流）。

```text
PROCESS-NAME,OpenVPN Connect
PROCESS-NAME,v2ray
PROCESS-NAME,xray
PROCESS-NAME,clash
PROCESS-NAME,naive
PROCESS-NAME,trojan
PROCESS-NAME,trojan-go
PROCESS-NAME,ss-local
PROCESS-NAME,privoxy
PROCESS-NAME,leaf
PROCESS-NAME,Thunder
PROCESS-NAME,DownloadService
PROCESS-NAME,qBittorrent
PROCESS-NAME,Transmission
PROCESS-NAME,fdm
PROCESS-NAME,aria2c
PROCESS-NAME,Folx
PROCESS-NAME,NetTransport
PROCESS-NAME,uTorrent
PROCESS-NAME,WebTorrent
```

## Advertising

- 将 `https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/reject.txt` 内容复制到 `Anm/Surge/rule/Advertising/reject.list`。

## Lan

- 将 `rule/Surge/Lan/Lan.list` 内容复制到 `Anm/Surge/rule/Inner/Lan/Lan.list`。

## China

- 将 `rule/Surge/China/China_All.list` 内容复制到 `Anm/Surge/rule/Inner/China/China_All.list`。
- 将 `rule/Surge/ChinaMedia/ChinaMedia.list` 内容合并到 `Anm/Surge/rule/Inner/China/China_All.list`。

## Tencent

- 将 `rule/Surge/Tencent/Tencent_All.list` 内容复制到 `Anm/Surge/rule/Inner/Tencent/Tencent_All.list`。

- 按用户要求，为 `Anm/Surge/rule/Inner/Tencent/Tencent_All.list` 中所有 IP 规则补充 `no-resolve`，避免主动触发 DNS 解析。

```diff
-IP-CIDR,101.32.104.4/32
+IP-CIDR,101.32.104.4/32,no-resolve
-IP-CIDR,101.32.104.41/32
+IP-CIDR,101.32.104.41/32,no-resolve
-IP-CIDR,101.32.104.56/32
+IP-CIDR,101.32.104.56/32,no-resolve
-IP-CIDR,101.32.118.25/32
+IP-CIDR,101.32.118.25/32,no-resolve
-IP-CIDR,101.32.133.16/32
+IP-CIDR,101.32.133.16/32,no-resolve
-IP-CIDR,101.32.133.209/32
+IP-CIDR,101.32.133.209/32,no-resolve
-IP-CIDR,101.32.133.53/32
+IP-CIDR,101.32.133.53/32,no-resolve
-IP-CIDR,103.238.16.0/23
+IP-CIDR,103.238.16.0/23,no-resolve
-IP-CIDR,103.7.28.0/22
+IP-CIDR,103.7.28.0/22,no-resolve
-IP-CIDR,119.147.8.78/32
+IP-CIDR,119.147.8.78/32,no-resolve
-IP-CIDR,120.41.44.0/32
+IP-CIDR,120.41.44.0/32,no-resolve
-IP-CIDR,122.5.0.129/32
+IP-CIDR,122.5.0.129/32,no-resolve
-IP-CIDR,129.226.107.244/32
+IP-CIDR,129.226.107.244/32,no-resolve
-IP-CIDR,129.226.3.47/32
+IP-CIDR,129.226.3.47/32,no-resolve
-IP-CIDR,140.249.239.0/32
+IP-CIDR,140.249.239.0/32,no-resolve
-IP-CIDR,140.249.28.0/32
+IP-CIDR,140.249.28.0/32,no-resolve
-IP-CIDR,150.138.137.0/32
+IP-CIDR,150.138.137.0/32,no-resolve
-IP-CIDR,150.139.143.0/32
+IP-CIDR,150.139.143.0/32,no-resolve
-IP-CIDR,27.159.95.0/32
+IP-CIDR,27.159.95.0/32,no-resolve
-IP-CIDR,58.58.81.129/32
+IP-CIDR,58.58.81.129/32,no-resolve
```

## Apple

- 将 `rule/Surge/Apple/Apple_All.list` 内容复制到 `Anm/Surge/rule/Out/Apple/Apple_All.list`。

## Disney

- 将 `rule/Surge/Disney/Disney.list` 内容复制到 `Anm/Surge/rule/Out/Disney/Disney.list`。

## Global

- 将 `rule/Surge/Global/Global_All.list` 内容复制到 `Anm/Surge/rule/Out/Global/Global_All.list`。

- 将 `rule/Surge/GlobalMedia/GlobalMedia_All.list` 与 `Anm/Surge/rule/Out/Global/Global_All.list`（先导入 Global 来源，排除 `rule/Surge/GlobalMedia/` 来源的规则组）对比，将未覆盖的规则合并到 `Anm/Surge/rule/Out/Global/Global_All.list`。

## Google

- 将 `rule/Surge/Google/Google.list` 内容复制到 `Anm/Surge/rule/Out/Google/Google.list`。

## Microsoft

- 将 `rule/Surge/Microsoft/Microsoft.list` 内容复制到 `Anm/Surge/rule/Out/Microsoft/Microsoft.list`。

## Netflix

- 将 `rule/Surge/Netflix/Netflix.list` 内容复制到 `Anm/Surge/rule/Out/Netflix/Netflix.list`。

## Claude

- 将 `rule/Surge/Claude/Claude.list` 内容复制到 `Anm/Surge/rule/Out/Claude/Claude.list`。

- 将用户自定义的以下规则添加到 `Anm/Surge/rule/Out/Claude/Claude.list`。

```text
DOMAIN-SUFFIX,claude.com
DOMAIN-SUFFIX,clau.de
DOMAIN-SUFFIX,claudeusercontent.com
DOMAIN-SUFFIX,datadoghq.com
IP-CIDR,160.79.104.0/23,no-resolve
IP-CIDR6,2607:6bc0::/48,no-resolve
```

## OpenAI

- 将 `rule/Surge/OpenAI/OpenAI.list` 内容复制到 `Anm/Surge/rule/Out/OpenAI/OpenAI.list`。

- 将用户自定义的以下规则添加到 `Anm/Surge/rule/Out/OpenAI/OpenAI.list`。

```text
IP-CIDR,108.160.166.62/32,no-resolve
```

## Telegram

- 将 `rule/Surge/Telegram/Telegram.list` 内容复制到 `Anm/Surge/rule/Out/Telegram/Telegram.list`。

## YouTube

- 将 `rule/Surge/YouTube/YouTube.list` 内容复制到 `Anm/Surge/rule/Out/YouTube/YouTube.list`。

## Bank

- 将 `rule/Surge/CCB/CCB.list` 内容合并到 `Anm/Surge/rule/Inner/Bank/Bank.list`。
- 将 `rule/Surge/CMB/CMB.list` 内容合并到 `Anm/Surge/rule/Inner/Bank/Bank.list`。
- 将 `rule/Surge/ABC/ABC.list` 内容合并到 `Anm/Surge/rule/Inner/Bank/Bank.list`。
- 将 `rule/Surge/BOC/BOC.list` 内容合并到 `Anm/Surge/rule/Inner/Bank/Bank.list`。
- 将 `rule/Surge/BOCOM/BOCOM.list` 内容合并到 `Anm/Surge/rule/Inner/Bank/Bank.list`。
- 将 `rule/Surge/CGB/CGB.list` 内容合并到 `Anm/Surge/rule/Inner/Bank/Bank.list`。
- 将 `rule/Surge/UnionPay/UnionPay.list` 内容合并到 `Anm/Surge/rule/Inner/Bank/Bank.list`。
- 将 `rule/Surge/ICBC/ICBC.list` 内容合并到 `Anm/Surge/rule/Inner/Bank/Bank.list`。

## Synthesis_Out

- 将 `rule/Surge/GitHub/GitHub.list` 内容复制到 `Anm/Surge/rule/Out/Synthesis/Synthesis_Out.list`。

## Extra_Out

- 将用户自定义的以下规则添加到 `Anm/Surge/rule/Out/Extra/Extra_Out.list`。

```text
DOMAIN-SUFFIX,context7.com
DOMAIN-SUFFIX,jetbrains.com
DOMAIN-SUFFIX,npmjs.org
DOMAIN-SUFFIX,zeroturnaround.com
```

## USA

- 将用户自定义的以下规则添加到 `Anm/Surge/rule/Out/USA/USA.list`。

```text
DOMAIN-SUFFIX,ping0.cc
```

## Extra_Inner

- 将用户自定义的以下规则添加到 `Anm/Surge/rule/Inner/Extra/Extra_Inner.list`。

```text
DOMAIN-SUFFIX,aiguoai.com
DOMAIN-SUFFIX,aiguoerp.com
DOMAIN-SUFFIX,xtkj99.com
DOMAIN-SUFFIX,synergypeak.org,DIRECT
DOMAIN-SUFFIX,speedtest.cn
DOMAIN-SUFFIX,api-flowercloud.com
```

## Synthesis_Inner

- 将 `rule/Surge/AliPay/AliPay.list` 与 `Anm/Surge/rule/Inner/China/China_All.list` 对比，将未覆盖的规则合并到 `Anm/Surge/rule/Inner/Synthesis/Synthesis_Inner.list`。

```text
DOMAIN-SUFFIX,luohanacademy.com
```

- 将 `rule/Surge/DouYin/DouYin.list` 与 `Anm/Surge/rule/Inner/China/China_All.list` 对比，将未覆盖的规则合并到 `Anm/Surge/rule/Inner/Synthesis/Synthesis_Inner.list`。

```text
DOMAIN-SUFFIX,idouyinvod.com
```

- 将 `rule/Surge/iQIYI/iQIYI.list` 与 `Anm/Surge/rule/Inner/China/China_All.list` 对比，将未覆盖的规则合并到 `Anm/Surge/rule/Inner/Synthesis/Synthesis_Inner.list`（进程规则仅 Surge Mac 支持，iOS 忽略；Loon 对应来源无此规则，未找到等价转换，沿用现有规则）。

```text
PROCESS-NAME,com.qiyi.video
```

- 将 `rule/Surge/Alibaba/Alibaba_All.list` 与 `Anm/Surge/rule/Inner/China/China_All.list` 和 `Anm/Surge/rule/Inner/Synthesis/Synthesis_Inner.list`（排除 `rule/Surge/Alibaba/` 来源的规则组）联合对比，将未覆盖的规则合并到 `Anm/Surge/rule/Inner/Synthesis/Synthesis_Inner.list`（进程规则仅 Surge Mac 支持，iOS 忽略；Loon 对应来源无此规则且无等价转换，其他请求按现有规则分流）。

- 将 `rule/Surge/Download/Download.list` 与 `Anm/Surge/rule/Inner/China/China_All.list` 对比，将未覆盖的规则合并到 `Anm/Surge/rule/Inner/Synthesis/Synthesis_Inner.list`（进程规则仅 Surge Mac 支持，iOS 忽略；Loon 对应来源缺少 13 条进程规则，无等价转换，其他请求按现有规则分流；HTTPS URL 匹配需 MITM）。

```text
DOMAIN-SUFFIX,qbittorrent.org
DOMAIN-KEYWORD,aria2
DOMAIN-KEYWORD,thunder
DOMAIN-KEYWORD,xlliveud
DOMAIN-KEYWORD,xunlei
DOMAIN-KEYWORD,yunpan
URL-REGEX,assets\d+\.xboxlive\.(com|cn)
PROCESS-NAME,BitComet
PROCESS-NAME,DownloadService
PROCESS-NAME,Folx
PROCESS-NAME,NetTransport
PROCESS-NAME,Thunder
PROCESS-NAME,Transmission
PROCESS-NAME,WebTorrent
PROCESS-NAME,WebTorrentHelper
PROCESS-NAME,Weiyun
PROCESS-NAME,aria2c
PROCESS-NAME,fdm
PROCESS-NAME,qbittorrent
PROCESS-NAME,uTorrent
```

- 将 `rule/Surge/JingDong/JingDong.list` 与 `Anm/Surge/rule/Inner/China/China_All.list` 对比，将未覆盖的规则合并到 `Anm/Surge/rule/Inner/Synthesis/Synthesis_Inner.list`。

```text
DOMAIN-SUFFIX,buyjingxi.com
DOMAIN-SUFFIX,ibaitiao.com
DOMAIN-SUFFIX,info-insur.com
DOMAIN-SUFFIX,jcloudwaf.com
DOMAIN-SUFFIX,jcloudwaftest.com
DOMAIN-SUFFIX,jcloudwaftest.net
DOMAIN-SUFFIX,jdcontent.com
DOMAIN-SUFFIX,jdd-global.com
DOMAIN-SUFFIX,jddtv.com
DOMAIN-SUFFIX,jdfeijing.com
DOMAIN-SUFFIX,jdfinance.com
DOMAIN-SUFFIX,jdfmgt.com
DOMAIN-SUFFIX,jdsmartkf.com
DOMAIN-SUFFIX,jdworldwide.com
DOMAIN-SUFFIX,shlsyb.com
DOMAIN-SUFFIX,wanggou.com
DOMAIN-SUFFIX,yihaomall.com
DOMAIN-SUFFIX,yixun.com
```

- 将 `rule/Surge/WeChat/WeChat.list` 与 `rule/Surge/China/China_All.list` 对比，将未覆盖的规则合并到 `Anm/Surge/rule/Inner/Synthesis/Synthesis_Inner.list`。

- 将 `rule/Surge/XianYu/XianYu.list` 内容合并到 `Anm/Surge/rule/Inner/Synthesis/Synthesis_Inner.list`。
