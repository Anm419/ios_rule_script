# `China_All.list `和 `ChinaMedia.list`规则

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
