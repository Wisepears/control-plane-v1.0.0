# 初始化

＜?...!＞
1. 定位用户指定的目标项目根目录。用 Python 3.9 或更新版本从本技能目录执行，将路径换成实际路径。

   ~~~text
   python scripts/initialize.py --target "<项目根目录>" --dry-run
   python scripts/initialize.py --target "<项目根目录>"
   ~~~

2. 根据预检输出处理已有文件。已有 AGENTS.md 时，保留其正文并追加项目入口。其他已有控制面文件发生冲突时，先查它们的职责和调用者，再制定迁移方案。
3. 用户已说明项目需求时，把相关原话写入项目 ORIGINAL-INTENT.md，再据此填入 OBJECTIVE.md 和 UNDERSTANDING.md。缺少项目资料时照常初始化。
4. 从目标 AGENTS.md 走一遍[项目工作流程](../assets/project/foundation/control-plane/workflow.md)的读取入口。核对项目入口、固定的版本号和词汇表去处。
＜/?...!＞
