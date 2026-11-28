# 控制面导航与交接

＜?...!＞
首次接手读完本页。后续按[每轮必读](../AGENTS.md#每轮必读)开工，需要定位控制面、领域面或交接说明时查下方目录。 [重新接手原话](../ORIGINAL-INTENT.md#u131) · [README 与 AGENTS 分工原话](../ORIGINAL-INTENT.md#u191)

<a id="control-plane"></a>
## 控制面

控制面确定项目目标、已有取舍，以及怎样探讨问题和组织产出。 [控制面职能原话](../ORIGINAL-INTENT.md#u129) · [依赖倒置原话](../ORIGINAL-INTENT.md#u213)

控制面按五块组织，顺序即依赖顺序：方法 → 流程 → 入口 → 来源 → 目标、理解与决定。开工读[每轮必读](../AGENTS.md#每轮必读)，需要定位时按下表。

| 块 | 管什么 | 落在哪 |
|---|---|---|
| 大脑必备知识 | 交流内核【1】【2】【3】、产出与问题探讨、主导职责 | [交流内核](communication-core.md#方法原文) |
| 大脑工作流程 | 同步原话 → 交流内核找断裂处 → 走本轮入口 → 对齐目标并交接主导 | [控制面和领域面工作流程](control-plane/workflow.md#workflow) |
| 产出（本轮入口） | 新内容 / 内容维护 / 知识同步 / 代码工程 / 其它产出走关于所有产出五选一 | [关于本轮入口](关于所有的产出.md#output-entrances) |
| 来源 | 用户原话、原话与来源标记、in-file reference | [原话文档](../ORIGINAL-INTENT.md#intent-purpose) · [原话与来源标记](关于内容维护.md#source-markers) · [In-file reference](关于内容维护.md#inner-reference) |
| 目标、理解与决定 | 当前目标、当前理解、已定决定、词汇表索引 | [项目目标](../OBJECTIVE.md) · [当前理解](../UNDERSTANDING.md) · [项目决策索引](../ADR.md) · [词汇表索引](../GLOSSARY-MAP.md) |

其中，大脑必备知识，工作流程，产出块不对AI修改开放，需要经过审核或者到协作收获中登记待审。

反馈按需读，不常驻：[痛点文档](../痛点文档.md#更新规则) · [搁置讨论清单](../搁置讨论清单.md)。
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

本轮任务走哪个入口，从[关于所有的产出](关于所有的产出.md#output-entrances)选。

＜/?...!＞
