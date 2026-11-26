# 控制面 v1.0.1

把控制面和领域面的协作方式用在多个项目。共用规则放在 [control-plane 技能](skills/control-plane/SKILL.md)，项目从 [AGENTS.md](skills/control-plane/assets/project/AGENTS.md) 进入自己的目标、原话、理解、词汇表和决定。

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

共用交流内核、每轮工作流程、产出、内容维护、领域建模与协作记录随版本发布。项目自己的原话、目标、领域事实、取舍和记录保存在各项目。Matt Pocock 方法原文及许可见[随附许可](skills/control-plane/references/runtime/skills/mattpocock/LICENSE)。
