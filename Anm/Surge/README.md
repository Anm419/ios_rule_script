## China

- 将 `rule/Surge/China/China_All.list` 内容复制到 `Anm/Surge/rule/Inner/China/China_All.list`。
- 将 `rule/Surge/ChinaMedia/ChinaMedia.list` 内容合并到 `Anm/Surge/rule/Inner/China/China_All.list`。

## Apple

- 将 `rule/Surge/Apple/Apple_All.list` 内容复制到 `Anm/Surge/rule/Out/Apple/Apple_All.list`。

## Disney

- 将 `rule/Surge/Disney/Disney.list` 内容复制到 `Anm/Surge/rule/Out/Disney/Disney.list`。

## GitHub

- 将 `rule/Surge/GitHub/GitHub.list` 内容复制到 `Anm/Surge/rule/Out/GitHub/GitHub.list`。

## GlobalMedia

- 将 `rule/Surge/GlobalMedia/GlobalMedia_All.list` 内容复制到 `Anm/Surge/rule/Out/GlobalMedia/GlobalMedia_All.list`。

## Google

- 将 `rule/Surge/Google/Google.list` 内容复制到 `Anm/Surge/rule/Out/Google/Google.list`。

## Microsoft

- 将 `rule/Surge/Microsoft/Microsoft.list` 内容复制到 `Anm/Surge/rule/Out/Microsoft/Microsoft.list`。

## Netflix

- 将 `rule/Surge/Netflix/Netflix.list` 内容复制到 `Anm/Surge/rule/Out/Netflix/Netflix.list`。

## OpenAI

- 将 `rule/Surge/OpenAI/OpenAI.list` 内容复制到 `Anm/Surge/rule/Out/OpenAI/OpenAI.list`。

## Proxy

- 将 `rule/Surge/Proxy/Proxy_All.list` 内容复制到 `Anm/Surge/rule/Out/Proxy/Proxy_All.list`。

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

## Synthesis

- 将 `rule/Surge/AliPay/AliPay.list` 与 `Anm/Surge/rule/Inner/China/China_All.list` 对比，将未覆盖的规则合并到 `Anm/Surge/rule/Inner/Synthesis/Synthesis.list`。

```text
DOMAIN-SUFFIX,luohanacademy.com
```

- 将 `rule/Surge/DouYin/DouYin.list` 与 `Anm/Surge/rule/Inner/China/China_All.list` 对比，将未覆盖的规则合并到 `Anm/Surge/rule/Inner/Synthesis/Synthesis.list`。

```text
DOMAIN-SUFFIX,idouyinvod.com
```

- 将 `rule/Surge/iQIYI/iQIYI.list` 与 `Anm/Surge/rule/Inner/China/China_All.list` 对比，将未覆盖的规则合并到 `Anm/Surge/rule/Inner/Synthesis/Synthesis.list`（进程规则仅 Surge Mac 支持，iOS 忽略；Loon 对应来源无此规则，未找到等价转换，沿用现有规则）。

```text
PROCESS-NAME,com.qiyi.video
```
