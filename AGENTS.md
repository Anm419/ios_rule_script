# 背景
借助[开源仓库-ios_rule_script](https://github.com/blackmatrix7/ios_rule_script/tree/master)开源仓库打造自己的`Surge`和`Loon`的分流规则

# 项目结构
1. `rule/Surge`原有项目的`Surge`分流规则
2. `rule/Loon`原有项目的`Loon`分流规则
3. `Anm/Surge`的规则是从`rule/Surge`下整理的`Surge`分流规则
4. `Anm/Loon`的规则是从`rule/Loon`下整理的`Loon`分流规则

# 注意事项
1. 未经允许的情况下只允许更新`Anm/Surge/Surge.conf`下的[Rule]模块和`Anm/Loon/Loon.lcf`下的[Remote Rule]
2. 在做`Anm/Surge`下操作的同时需要同步`Anm/Loon`,同理做`Anm/Loon`下操作也需要同步`Anm/Surge`
