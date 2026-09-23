## China

- 将 `rule/Loon/China/China_Domain.list` 转换后写入 `Anm/Loon/rule/Inner/China/China_All.list`（以 `.` 开头的域名去掉首个点并添加 `DOMAIN-SUFFIX,`，其余域名添加 `DOMAIN,`）。
- 将 `rule/Loon/China/China_Resolve.list` 内容合并到 `Anm/Loon/rule/Inner/China/China_All.list`。

## ChinaMedia

- 将 `rule/Loon/ChinaMedia/ChinaMedia.list` 内容复制到 `Anm/Loon/rule/Inner/ChinaMedia/ChinaMedia.list`（该来源较 Surge 少 6 条 `PROCESS-NAME` 规则）。

## Apple

- 将 `rule/Loon/Apple/Apple_Domain.list` 转换后写入 `Anm/Loon/rule/Out/Apple/Apple_All.list`（以 `.` 开头的域名去掉首个点并添加 `DOMAIN-SUFFIX,`，其余域名添加 `DOMAIN,`；较 Surge 缺少 13 条进程名规则，无法等价转换，按其他规则继续分流）。
- 将 `rule/Loon/Apple/Apple_Resolve.list` 内容合并到 `Anm/Loon/rule/Out/Apple/Apple_All.list`。

## Disney

- 将 `rule/Loon/Disney/Disney.list` 内容复制到 `Anm/Loon/rule/Out/Disney/Disney.list`（较 Surge 缺少 2 条进程名规则，无法等价转换，按其他规则继续分流）。

## GitHub

- 将 `rule/Loon/GitHub/GitHub.list` 内容复制到 `Anm/Loon/rule/Out/GitHub/GitHub.list`。

## GlobalMedia

- 将 `rule/Loon/GlobalMedia/GlobalMedia_Domain.list` 转换后写入 `Anm/Loon/rule/Out/GlobalMedia/GlobalMedia_All.list`（以 `.` 开头的域名去掉首个点并添加 `DOMAIN-SUFFIX,`，其余域名添加 `DOMAIN,`；较 Surge 缺少 3 条进程名规则，无法等价转换，按其他规则继续分流）。
- 将 `rule/Loon/GlobalMedia/GlobalMedia_Resolve.list` 内容合并到 `Anm/Loon/rule/Out/GlobalMedia/GlobalMedia_All.list`。

## Google

- 将 `rule/Loon/Google/Google.list` 内容复制到 `Anm/Loon/rule/Out/Google/Google.list`（较 Surge 缺少 5 条进程名规则，无法等价转换，按其他规则继续分流）。

## Microsoft

- 将 `rule/Loon/Microsoft/Microsoft.list` 内容复制到 `Anm/Loon/rule/Out/Microsoft/Microsoft.list`（较 Surge 缺少 2 条进程名规则，无法等价转换，按其他规则继续分流）。

## Netflix

- 将 `rule/Loon/Netflix/Netflix.list` 内容复制到 `Anm/Loon/rule/Out/Netflix/Netflix.list`（较 Surge 缺少 1 条进程名规则，无法等价转换，按其他规则继续分流）。

## OpenAI

- 将 `rule/Loon/OpenAI/OpenAI.list` 内容复制到 `Anm/Loon/rule/Out/OpenAI/OpenAI.list`。

## Proxy

- 将 `rule/Loon/Proxy/Proxy_Domain.list` 转换后写入 `Anm/Loon/rule/Out/Proxy/Proxy_All.list`（以 `.` 开头的域名去掉首个点并添加 `DOMAIN-SUFFIX,`，其余域名添加 `DOMAIN,`）。
- 将 `rule/Loon/Proxy/Proxy_Resolve.list` 内容合并到 `Anm/Loon/rule/Out/Proxy/Proxy_All.list`。

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

## Synthesis

- 将 `rule/Loon/AliPay/AliPay.list` 与 `Anm/Loon/rule/Inner/China/China_All.list` 和 `Anm/Loon/rule/Inner/ChinaMedia/ChinaMedia.list` 联合对比，将未覆盖的规则合并到 `Anm/Loon/rule/Inner/Synthesis/Synthesis.list`。

```text
DOMAIN-SUFFIX,luohanacademy.com
```

- 将 `rule/Loon/DouYin/DouYin.list` 与 `Anm/Loon/rule/Inner/China/China_All.list` 和 `Anm/Loon/rule/Inner/ChinaMedia/ChinaMedia.list` 联合对比，将未覆盖的规则合并到 `Anm/Loon/rule/Inner/Synthesis/Synthesis.list`。

```text
DOMAIN-SUFFIX,idouyinvod.com
```
