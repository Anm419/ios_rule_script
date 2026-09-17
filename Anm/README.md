# Anm 规则集

规则链接均指向 `Anm419/ios_rule_script` 仓库 `master` 分支下的 `Anm` 目录。

Loon 使用 `policy=` 指定策略或策略组；Surge 使用每行末尾的 `YouTube`、`OpenAI`、`Google` 指定策略或策略组。请按你的配置修改。同一分类的普通版和 `_Resolve` 版选择其中一种使用即可。

## Loon

以下条目按 Loon 格式编写：`policy=Available` 指定策略或策略组，请替换为你配置中实际存在的名称；`tag` 用于标识规则集，`enabled=true` 表示启用。

### 普通版

```ini
# > YouTube 视频
https://raw.githubusercontent.com/Anm419/ios_rule_script/master/Anm/Loon/YouTube/YouTube.list, policy=Available, tag=YouTube, enabled=true

# > OpenAI 服务
https://raw.githubusercontent.com/Anm419/ios_rule_script/master/Anm/Loon/OpenAI/OpenAI.list, policy=Available, tag=OpenAI, enabled=true

# > 谷歌服务
https://raw.githubusercontent.com/Anm419/ios_rule_script/master/Anm/Loon/Google/Google.list, policy=Available, tag=Google, enabled=true
```

### _Resolve 版（可选替代）

```ini
# > YouTube 视频
https://raw.githubusercontent.com/Anm419/ios_rule_script/master/Anm/Loon/YouTube/YouTube_Resolve.list, policy=Available, tag=YouTube, enabled=true

# > OpenAI 服务
https://raw.githubusercontent.com/Anm419/ios_rule_script/master/Anm/Loon/OpenAI/OpenAI_Resolve.list, policy=Available, tag=OpenAI, enabled=true

# > 谷歌服务
https://raw.githubusercontent.com/Anm419/ios_rule_script/master/Anm/Loon/Google/Google_Resolve.list, policy=Available, tag=Google, enabled=true
```

## Surge

### 普通版

```ini
# > YouTube 视频
RULE-SET,https://raw.githubusercontent.com/Anm419/ios_rule_script/master/Anm/Surge/YouTube/YouTube.list,YouTube

# > OpenAI 服务
RULE-SET,https://raw.githubusercontent.com/Anm419/ios_rule_script/master/Anm/Surge/OpenAI/OpenAI.list,OpenAI

# > 谷歌服务
RULE-SET,https://raw.githubusercontent.com/Anm419/ios_rule_script/master/Anm/Surge/Google/Google.list,Google
```

### _Resolve 版（可选替代）

```ini
# > YouTube 视频
RULE-SET,https://raw.githubusercontent.com/Anm419/ios_rule_script/master/Anm/Surge/YouTube/YouTube_Resolve.list,YouTube

# > OpenAI 服务
RULE-SET,https://raw.githubusercontent.com/Anm419/ios_rule_script/master/Anm/Surge/OpenAI/OpenAI_Resolve.list,OpenAI

# > 谷歌服务
RULE-SET,https://raw.githubusercontent.com/Anm419/ios_rule_script/master/Anm/Surge/Google/Google_Resolve.list,Google
```
