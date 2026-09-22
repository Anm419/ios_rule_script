# `China_All.list `和 `ChinaMedia.list`规则

## 包含了那些规则

- 包含了`AliPay.list`
- 包含了`DouYin.list`
- 包含了`Pinduoduo.list`
- 包含了`Youku.list`
- 包含了`115.list`
- 包含了`BiliBili.list`
- 包含了 `iQIYI.list`
- 包含了 `TencentVideo.list`

## 对比规则缺失

- `AliPay.list`对比`China_All.list`和`ChinaMedia.list`将`DOMAIN-SUFFIX,luohanacademy.com`合并到`China_All.list`
- `DouYin.list`对比`China_All.list`和`ChinaMedia.list`将`DOMAIN-SUFFIX,idouyinvod.com`合并到`China_All.list`
- `iQIYI.list`对比`China_All.list`和`ChinaMedia.list`将`PROCESS-NAME,com.qiyi.video`合并到`ChinaMedia.list`
- `DingTalk.list`对比`Alibaba_All.list`、`China_All.list`和`ChinaMedia.list`将`DOMAIN-SUFFIX,realapp.xin`合并到`Alibaba_All.list`

# 规则合并

- `CCB.list`合并到了`Bank.list`中
- `CMB.list`合并到了`Bank.list`中
- `ABC.list`合并到了`Bank.list`中
- `BOC.list`合并到了`Bank.list`中
- `BOCOM.list`合并到了`Bank.list`中
- `CGB.list`合并到了`Bank.list`中
- `UnionPay.list`合并到了`Bank.list`中
- `ICBC.list`合并到了`Bank.list`中

# 个人规则补充

- `DOMAIN-SUFFIX,openai.azure.com`合并到了`OpenAI.list`中
- `DOMAIN-SUFFIX,oai.azure.com`合并到了`OpenAI.list`中
- 从 [Unbreak.list](https://api-huacloud.dev/getruleset?type=1&url=UHJvZmlsZXMvU3VyZ2UvUnVsZXNldC9VbmJyZWFrLmxpc3Q) 补充以下 6 条未覆盖规则到 Loon 和 Surge 的 `China_All.list` 开头，并标注来源：

```text
DOMAIN,app.adjust.com
DOMAIN,app.appsflyer.com
DOMAIN,safebrowsing.googleapis.com
DOMAIN,safebrowsing.googleapis-cn.com
DOMAIN,safebrowsing.clients.google.com
DOMAIN,safebrowsing-cache.google.com
```
- 将 `IP-CIDR6,fd00::/8,no-resolve` 合并到 `Lan.list`

- 从 [花云.list](https://api-huacloud.dev/getruleset?type=1&url=UHJvZmlsZXMvU3VyZ2UvUnVsZXNldC9DaGluYS5saXN0) 补充以下 7 条未覆盖规则到 Loon 和 Surge 的 `China_All.list` 开头，并标注来源：

```text
DOMAIN-SUFFIX,netspeedtestmaster.com
DOMAIN,speedtest.macpaw.com
DOMAIN-SUFFIX,acg.rip
DOMAIN-SUFFIX,chdbits.co
DOMAIN-SUFFIX,comicat.org
DOMAIN-SUFFIX,hdsky.me
GEOIP,CN,no-resolve
```
