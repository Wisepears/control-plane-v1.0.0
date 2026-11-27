# 控制面 v1.0.1

这个仓库提供一个 Codex 技能，把控制面和领域面的骨架装进新项目。

## 仓库里的文件会放到哪里

仓库中需要看的文件都在 [skills/control-plane/](skills/control-plane) 下。表里的「新项目」就是你说「初始化当前项目」时打开的那个项目。

| 仓库里的位置 | 用途 | 初始化后的位置 |
|---|---|---|
| [SKILL.md](skills/control-plane/SKILL.md) | Codex 接到「用控制面初始化」时读的入口 | 它随技能安装 |
| [assets/project/](skills/control-plane/assets/project) | 可直接浏览的项目模板 | 按原目录放到新项目根目录。例如 AGENTS.md 放到项目根目录，foundation/communication-core.md 放到项目的 foundation/ 目录 |
| [scripts/initialize.py](skills/control-plane/scripts/initialize.py) | 把项目模板放到目标项目 | 它随技能安装 |

在 GitHub 上可以直接从[模板的 AGENTS.md](skills/control-plane/assets/project/AGENTS.md) 点进去。初始化完成后，从新项目的 AGENTS.md 开始读。 想知道去哪里找规则和领域知识，再打开它指向的 foundation/README.md。

## 在新项目初始化

本机安装技能后，在目标项目打开 Codex，发送：

> 用 $control-plane 初始化当前项目的控制面和领域面。

初始化后的项目携带固定版本的共用规则。[初始化说明](skills/control-plane/references/initialize.md)

## 在另一台机器使用

从 [v1.0.1](https://github.com/Wisepears/control-plane-v1.0.0/tree/v1.0.1) 获取仓库，把 skills/control-plane 整个目录复制到用户主目录下的 .agents/skills 目录。用 Codex 打开目标项目调用该技能。也可以直接从仓库用 Python 3.9 或更新版本运行：

~~~text
python skills/control-plane/scripts/initialize.py --target "<项目根目录>" --dry-run
python skills/control-plane/scripts/initialize.py --target "<项目根目录>"
~~~

## 内容归属

共用交流内核、每轮工作流程、产出、内容维护、领域建模与协作记录随版本发布。项目自己的原话、目标、领域事实、取舍和记录保存在各项目。Matt Pocock 方法原文及许可见[随附许可](skills/control-plane/assets/project/foundation/skills/mattpocock/LICENSE)。
