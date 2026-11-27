# 控制面导航与交接

＜?...!＞
首次接手读完本页。后续按[每轮必读](../AGENTS.md#每轮必读)开工，需要定位控制面、领域面或交接说明时查下方目录。 [重新接手原话](../ORIGINAL-INTENT.md#u131) · [README 与 AGENTS 分工原话](../ORIGINAL-INTENT.md#u191)

<a id="control-plane"></a>
## 控制面

控制面确定项目目标、已有取舍，以及怎样探讨问题和组织产出。 [控制面职能原话](../ORIGINAL-INTENT.md#u129) · [依赖倒置原话](../ORIGINAL-INTENT.md#u213)

| 想知道什么 | 打开哪里 |
|---|---|
| 产出与问题探讨遵循什么 | [交流内核](communication-core.md) |
| 当前目标是什么 | [项目目标](../OBJECTIVE.md) |
| 对控制面和问题域的当前理解 | [当前理解](../UNDERSTANDING.md) |
| 用户原话、来源与优先级 | [原话文档](../ORIGINAL-INTENT.md#intent-purpose) · [原话与来源标记](关于内容维护.md#source-markers) |
| 已定且难以逆转的取舍 | [项目决策索引](../ADR.md) |
| 内容维护、新文件 | [关于内容维护](关于内容维护.md#maintain-content) · [关于新内容](关于新文件.md) |

追溯需求时，查[原话文档](../ORIGINAL-INTENT.md#intent-purpose)。核对规则依据时，沿负责文档内的锚点找到对应原话。 [In-file reference 规则](关于内容维护.md#inner-reference)

控制面的[工作流程](control-plane/workflow.md)。
<a id="problem-domain"></a>
## 领域面

领域面按具体问题组织术语、解释所需的前提与结论，以及研究判断和依据。 [领域面职能原话](../ORIGINAL-INTENT.md#u129) · [问题域语义中心原话](../ORIGINAL-INTENT.md#u172)

| 想知道什么 | 打开哪里 |
|---|---|
| 术语定义与具体用例 | [问题域词汇表](../domain/GLOSSARY.md) |
| 按问题组织的研究判断和证据 | [领域查找](#domain-lookup) |
| 已定决定的理由和适用范围 | [项目决策索引](../ADR.md)，按条目打开正文 |

<a id="domain-lookup"></a>
### 领域查找

- **找研究判断和实际证据**。从[当前目标与证据](../OBJECTIVE.md#证据与方法)进入相关[问题域正文](../domain/README.md)。
- **词义、对象关系或适用范围影响判断**。查[问题域词汇表](../domain/GLOSSARY.md)。需要澄清时查[domain-modeling 原文](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md#discuss-concrete-scenarios)，形成术语后按[术语入表原话](关于内容维护.md#maintenance-principles)维护。
- **已有取舍影响本轮做法**。从[项目决策索引](../ADR.md)定位决定正文。

<a id="collaboration"></a>
## 协作方式

| 想知道什么 | 打开哪里 |
|---|---|
| 和用户、其他 AI、AI 自己怎么同步知识 | [知识同步](communication-core.md#knowledge-sync) |
| 每轮工作流程 | [控制面和领域面工作流程](control-plane/workflow.md#workflow) |
| 痛点登记、综合与归档 | [痛点文档](../痛点文档.md#更新规则) |
| 搁置讨论登记、续谈与归档 | [搁置讨论清单](../搁置讨论清单.md) |
| 向其他 AI 交付本轮原话、理解和待办 | [交接](#交接) |

需要回顾这段协作怎样形成，见[控制面协作收获](协作收获.md)。

## 交接

### 接手者能读取仓库

向接手者交付仓库位置和本轮任务，让它从[每轮必读](../AGENTS.md#每轮必读)开工。用[知识同步入口](communication-core.md#knowledge-sync)交接与本轮相关的原话、理解和待办。验收时让接手者自行找到必要依据，并凭实际结果判断是否完成。

### 接手者需要附件

向它上传交流约定、当前目标、相关用户原话、需要的领域定义，以及本轮相关材料和研究结果。保留相对目录，或者在交接消息中注明每个附件的用途。若只提供本机路径，对方得不到文件内容；此时将实际文件打包或作为附件提供。

<a id="repository-handoff"></a>
### 换设备或从 Git 恢复

换设备或拿到仓库副本时，按[控制面目录](#control-plane)核对六类入口，再按[每轮必读](../AGENTS.md#每轮必读)开工。从[问题域正文](../domain/README.md)找项目资料。需要复跑或查原始输出时，随任务交付对应批次的实际文件，并在接收方用的副本里确认可读。历史答复中的本机路径原样留存，换设备后按仓库里的对应文件位置查阅。见[原话](../ORIGINAL-INTENT.md#u132)。

保存需要交付的项目版本时，核对本次同步的文件范围，把版本同步到 GitHub，确认能打开后把版本链接交给你。见[交付方式原话](../ORIGINAL-INTENT.md#u133)。

### 受限任务的交接

负责项目统筹的 AI 使用上述项目上下文。参加受限任务的 AI 按专用资料包的任务、skill 和材料工作。准备者依据该任务的信息范围选取内容，保存资料包版本和原始输出。

旧的冻结资料包保留当时内容。新一轮采用新的资料包和版本，按该轮明确的输入规则运行。
＜/?...!＞
