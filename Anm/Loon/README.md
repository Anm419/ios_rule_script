## Advertising

- 将 `https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/reject.txt` 内容复制到 `Anm/Loon/rule/Advertising/reject.list`。

## Lan

- 将 `rule/Loon/Lan/Lan.list` 内容复制到 `Anm/Loon/rule/Inner/Lan/Lan.list`。

## China

- 将 `rule/Loon/China/China_Domain.list` 转换后写入 `Anm/Loon/rule/Inner/China/China_All.list`（以 `.` 开头的域名去掉首个点并添加 `DOMAIN-SUFFIX,`，其余域名添加 `DOMAIN,`）。
- 将 `rule/Loon/China/China_Resolve.list` 内容合并到 `Anm/Loon/rule/Inner/China/China_All.list`。
- 将 `rule/Loon/ChinaMedia/ChinaMedia.list` 内容合并到 `Anm/Loon/rule/Inner/China/China_All.list`（该来源较 Surge 少 6 条 `PROCESS-NAME` 规则）。

## Tencent

- 将 `rule/Loon/Tencent/Tencent_Domain.list` 按“以 `.` 开头的域名去掉首个点并添加 `DOMAIN-SUFFIX,`，其余域名添加 `DOMAIN,`”转换后写入 `Anm/Loon/rule/Inner/Tencent/Tencent_All.list`。
- 将 `rule/Loon/Tencent/Tencent_Resolve.list` 内容合并到 `Anm/Loon/rule/Inner/Tencent/Tencent_All.list`。

- 按用户要求，为 `Anm/Loon/rule/Inner/Tencent/Tencent_All.list` 中所有 IP 规则补充 `no-resolve`，避免主动触发 DNS 解析。

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

- 将 `rule/Loon/Apple/Apple_Domain.list` 转换后写入 `Anm/Loon/rule/Out/Apple/Apple_All.list`（以 `.` 开头的域名去掉首个点并添加 `DOMAIN-SUFFIX,`，其余域名添加 `DOMAIN,`；较 Surge 缺少 13 条进程名规则，无法等价转换，按其他规则继续分流）。
- 将 `rule/Loon/Apple/Apple_Resolve.list` 内容合并到 `Anm/Loon/rule/Out/Apple/Apple_All.list`。

## Disney

- 将 `rule/Loon/Disney/Disney.list` 内容复制到 `Anm/Loon/rule/Out/Disney/Disney.list`（较 Surge 缺少 2 条进程名规则，无法等价转换，按其他规则继续分流）。

## Global

- 将 `rule/Loon/Global/Global_Domain.list` 按“以 `.` 开头的域名去掉首个点并添加 `DOMAIN-SUFFIX,`，其余域名添加 `DOMAIN,`”转换后写入 `Anm/Loon/rule/Out/Global/Global_All.list`。
- 将 `rule/Loon/Global/Global_Resolve.list` 内容合并到 `Anm/Loon/rule/Out/Global/Global_All.list`（较 Surge 缺少 `PROCESS-NAME,LookupViewService`，Loon 不支持进程匹配，无法等价转换，按其他规则继续分流）。

- 将 `rule/Loon/GlobalMedia/GlobalMedia_Domain.list` 按“以 `.` 开头的域名去掉首个点并添加 `DOMAIN-SUFFIX,`，其余域名添加 `DOMAIN,`”转换后，与 `Anm/Loon/rule/Out/Global/Global_All.list`（先导入 Global 来源，排除 `rule/Loon/GlobalMedia/` 来源的规则组）对比，将未覆盖的规则合并到 `Anm/Loon/rule/Out/Global/Global_All.list`。
- 将 `rule/Loon/GlobalMedia/GlobalMedia_Resolve.list` 与 `Anm/Loon/rule/Out/Global/Global_All.list`（先导入 Global 来源，排除 `rule/Loon/GlobalMedia/` 来源的规则组）对比，将未覆盖的规则合并到 `Anm/Loon/rule/Out/Global/Global_All.list`（较 Surge 缺少 `com.viu.pad`、`com.viu.phone`、`com.vuclip.viu` 三条进程规则，无法等价转换，按其他规则继续分流）。

## Google

- 将 `rule/Loon/Google/Google.list` 内容复制到 `Anm/Loon/rule/Out/Google/Google.list`（较 Surge 缺少 5 条进程名规则，无法等价转换，按其他规则继续分流）。

## Microsoft

- 将 `rule/Loon/Microsoft/Microsoft.list` 内容复制到 `Anm/Loon/rule/Out/Microsoft/Microsoft.list`（较 Surge 缺少 2 条进程名规则，无法等价转换，按其他规则继续分流）。

## Netflix

- 将 `rule/Loon/Netflix/Netflix.list` 内容复制到 `Anm/Loon/rule/Out/Netflix/Netflix.list`（较 Surge 缺少 1 条进程名规则，无法等价转换，按其他规则继续分流）。

## Claude

- 将 `rule/Loon/Claude/Claude.list` 内容复制到 `Anm/Loon/rule/Out/Claude/Claude.list`。

- 将用户自定义的以下规则添加到 `Anm/Loon/rule/Out/Claude/Claude.list`。

```text
DOMAIN-SUFFIX,claude.com
DOMAIN-SUFFIX,clau.de
DOMAIN-SUFFIX,claudeusercontent.com
DOMAIN-SUFFIX,datadoghq.com
IP-CIDR,160.79.104.0/23,no-resolve
IP-CIDR6,2607:6bc0::/48,no-resolve
```

## OpenAI

- 将 `rule/Loon/OpenAI/OpenAI.list` 内容复制到 `Anm/Loon/rule/Out/OpenAI/OpenAI.list`。

- 将用户自定义的以下规则添加到 `Anm/Loon/rule/Out/OpenAI/OpenAI.list`。

```text
IP-CIDR,108.160.166.62/32,no-resolve
```

## Telegram

- 将 `rule/Loon/Telegram/Telegram.list` 内容复制到 `Anm/Loon/rule/Out/Telegram/Telegram.list`（较 Surge 缺少 5 条进程名规则，无法等价转换，按其他规则继续分流；Surge 的 OR 所列 5 个 ASN 已由本来源同选项的独立 IP-ASN 规则等价覆盖）。

## YouTube

- 将 `rule/Loon/YouTube/YouTube.list` 内容复制到 `Anm/Loon/rule/Out/YouTube/YouTube.list`。

## Bank

- 将 `rule/Loon/CCB/CCB.list` 内容合并到 `Anm/Loon/rule/Inner/Bank/Bank.list`。
- 将 `rule/Loon/CMB/CMB.list` 内容合并到 `Anm/Loon/rule/Inner/Bank/Bank.list`。
- 将 `rule/Loon/ABC/ABC.list` 内容合并到 `Anm/Loon/rule/Inner/Bank/Bank.list`。
- 将 `rule/Loon/BOC/BOC.list` 内容合并到 `Anm/Loon/rule/Inner/Bank/Bank.list`。
- 将 `rule/Loon/BOCOM/BOCOM.list` 内容合并到 `Anm/Loon/rule/Inner/Bank/Bank.list`。
- 将 `rule/Loon/CGB/CGB.list` 内容合并到 `Anm/Loon/rule/Inner/Bank/Bank.list`。
- 将 `rule/Loon/UnionPay/UnionPay.list` 内容合并到 `Anm/Loon/rule/Inner/Bank/Bank.list`。
- 将 `rule/Loon/ICBC/ICBC.list` 内容合并到 `Anm/Loon/rule/Inner/Bank/Bank.list`。

## Synthesis_Out

- 将 `rule/Loon/GitHub/GitHub.list` 内容复制到 `Anm/Loon/rule/Out/Synthesis/Synthesis_Out.list`。

## Extra_Out

- 将用户自定义的以下规则添加到 `Anm/Loon/rule/Out/Extra/Extra_Out.list`。

```text
DOMAIN-SUFFIX,context7.com
DOMAIN-SUFFIX,jetbrains.com
DOMAIN-SUFFIX,npmjs.org
DOMAIN-SUFFIX,zeroturnaround.com
```

## USA

- 将用户自定义的以下规则添加到 `Anm/Loon/rule/Out/USA/USA.list`。

```text
DOMAIN-SUFFIX,ping0.cc
```

## Extra_Inner

- 将用户自定义的以下规则添加到 `Anm/Loon/rule/Inner/Extra/Extra_Inner.list`。

```text
DOMAIN-SUFFIX,aiguoai.com
DOMAIN-SUFFIX,aiguoerp.com
DOMAIN-SUFFIX,xtkj99.com
DOMAIN-SUFFIX,synergypeak.org,DIRECT
DOMAIN-SUFFIX,speedtest.cn
DOMAIN-SUFFIX,api-flowercloud.com
```

## Synthesis_Inner

- 将 `rule/Loon/AliPay/AliPay.list` 与 `Anm/Loon/rule/Inner/China/China_All.list` 对比，将未覆盖的规则合并到 `Anm/Loon/rule/Inner/Synthesis/Synthesis_Inner.list`。

```text
DOMAIN-SUFFIX,luohanacademy.com
```

- 将 `rule/Loon/DouYin/DouYin.list` 与 `Anm/Loon/rule/Inner/China/China_All.list` 对比，将未覆盖的规则合并到 `Anm/Loon/rule/Inner/Synthesis/Synthesis_Inner.list`。

```text
DOMAIN-SUFFIX,idouyinvod.com
```

- 将 `rule/Loon/Alibaba/Alibaba_Domain.list` 按“以 `.` 开头的域名去掉首个点并添加 `DOMAIN-SUFFIX,`，其余域名添加 `DOMAIN,`”转换后，与 `Anm/Loon/rule/Inner/China/China_All.list` 和 `Anm/Loon/rule/Inner/Synthesis/Synthesis_Inner.list`（排除 `rule/Loon/Alibaba/` 来源的规则组）联合对比，将未覆盖的规则合并到 `Anm/Loon/rule/Inner/Synthesis/Synthesis_Inner.list`。

- 将 `rule/Loon/Alibaba/Alibaba_Resolve.list` 与 `Anm/Loon/rule/Inner/China/China_All.list` 和 `Anm/Loon/rule/Inner/Synthesis/Synthesis_Inner.list`（排除 `rule/Loon/Alibaba/` 来源的规则组）联合对比，将未覆盖的规则合并到 `Anm/Loon/rule/Inner/Synthesis/Synthesis_Inner.list`（较 Surge 缺少 `PROCESS-NAME,com.taobao.taobao`，无等价转换，其他请求按现有规则分流）。

- 将 `rule/Loon/Download/Download.list` 与 `Anm/Loon/rule/Inner/China/China_All.list` 对比，将未覆盖的规则合并到 `Anm/Loon/rule/Inner/Synthesis/Synthesis_Inner.list`（较 Surge 缺少 13 条进程规则，无等价转换，其他请求按现有规则分流；HTTPS URL 匹配需 MITM）。

```text
DOMAIN-SUFFIX,qbittorrent.org
DOMAIN-KEYWORD,aria2
DOMAIN-KEYWORD,thunder
DOMAIN-KEYWORD,xlliveud
DOMAIN-KEYWORD,xunlei
DOMAIN-KEYWORD,yunpan
URL-REGEX,assets\d+\.xboxlive\.(com|cn)
```

- 将 `rule/Loon/JingDong/JingDong.list` 与 `Anm/Loon/rule/Inner/China/China_All.list` 对比，将未覆盖的规则合并到 `Anm/Loon/rule/Inner/Synthesis/Synthesis_Inner.list`。

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

- 将 `rule/Loon/WeChat/WeChat.list` 与 `rule/Loon/China/China_Domain.list` 和 `rule/Loon/China/China_Resolve.list` 联合对比，将未覆盖的规则合并到 `Anm/Loon/rule/Inner/Synthesis/Synthesis_Inner.list`。

```text
DOMAIN,slife.xy-asia.com
DOMAIN-SUFFIX,iot-tencent.com
DOMAIN-SUFFIX,wechatlegal.net
DOMAIN-SUFFIX,wechatos.net
DOMAIN-SUFFIX,wechatpay.com
DOMAIN-SUFFIX,weixin.com
DOMAIN-SUFFIX,weixinsxy.com
IP-ASN,132203,no-resolve
```

- 将 `rule/Surge/WeChat/WeChat.list` 中 `rule/Loon/WeChat/WeChat.list` 未提供的 `DOMAIN-KEYWORD`、`IP-CIDR` 和 `IP-CIDR6` 规则与 `rule/Loon/China/China_Domain.list` 和 `rule/Loon/China/China_Resolve.list` 联合对比，将未覆盖的规则合并到 `Anm/Loon/rule/Inner/Synthesis/Synthesis_Inner.list`（沿用 Loon 支持的原语法，保留数字关键词及 IP 规则的 `no-resolve`）。

- 将 `rule/Loon/XianYu/XianYu.list` 内容合并到 `Anm/Loon/rule/Inner/Synthesis/Synthesis_Inner.list`。
