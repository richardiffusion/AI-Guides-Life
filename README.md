# AI-Guides-Life

用 AI 辅助生活规划、执行与复盘的通用方法论库。

本仓库面向任何希望改善生活组织方式的人。它提供框架、操作步骤、提示词和空白模板；读者在仓库之外的独立私有空间完成个性化配置。

> **最高优先级：仓库仅保存可公开复用的方法论，不得包含任何人的个人信息。此规则在仓库为 private 时同样生效。**

## 从这里开始

1. 阅读[仓库边界与隐私规则](docs/privacy.md)。
2. 按[快速开始](docs/quick-start.md)，只选择一个生活领域和一个可执行动作。
3. 从下方领域指南选取方法，将[个人配置空白模板](templates/personal-setup.md)复制到仓库之外的私有空间填写。
4. 使用[通用提示词](prompts/core.md)生成备选方案，确认后执行。
5. 在私有空间使用[周复盘模板](templates/weekly-review.md)，将真正可复用的改进抽象后再考虑贡献到本仓库。

## 九大生活领域

| 领域 | 主要问题 | 方法论入口 |
| --- | --- | --- |
| 日常作息 | 如何安排一天，并在变化时调整 | [作息指南](domains/01-daily-routine/README.md) |
| 睡眠 | 如何建立睡前、夜间与起床流程 | [睡眠指南](domains/02-sleep/README.md) |
| 饮食 | 如何组织菜单、采购与备餐 | [饮食指南](domains/03-nutrition/README.md) |
| 喝水 | 如何建立合适、低打扰的饮水流程 | [喝水指南](domains/04-hydration/README.md) |
| 健身 | 如何安排训练、恢复与执行 | [健身指南](domains/05-fitness/README.md) |
| 通勤 | 如何比较路线、处理延误与出发准备 | [通勤指南](domains/06-commute/README.md) |
| 读书 | 如何选择、理解、回忆与运用 | [读书指南](domains/07-reading/README.md) |
| 出行、旅游 | 如何规划行程、核实信息与准备备选 | [出行指南](domains/08-travel/README.md) |
| 交友见面 | 如何发出邀约、协调安排与尊重边界 | [见面指南](domains/09-social/README.md) |

## 共用方法

- [系统方法](docs/methodology.md)：目标、约束、最小动作、反馈与调整。
- [跨领域协调](docs/cross-domain.md)：处理睡眠、饮食、训练、通勤和社交之间的冲突。
- [自动化分级](docs/automation.md)：确定 AI 可以建议、草拟、提醒和执行的边界。
- [信息核实](docs/evidence.md)：区分已知事实、用户输入、假设和待核实项。
- [实施路线](docs/roadmap.md)：明确已交付内容与尚未实现的功能。

## 提示词与模板

- 提示词：[通用工作流](prompts/core.md)、[跨领域规划](prompts/planning.md)、[复盘与方案评审](prompts/review.md)。
- 空白模板：[个性化配置](templates/personal-setup.md)、[日计划](templates/daily-plan.md)、[周复盘](templates/weekly-review.md)、[单变量尝试](templates/experiment.md)、[自动化约定](templates/automation-contract.md)、[信息核实表](templates/source-check.md)。
- [纯虚构流程演示](examples/fictional-walkthrough.md)：展示如何组合这些材料。

## 仓库结构

```text
docs/        通用原则、隐私、协调、自动化与建设路线
domains/     九个领域的操作指南
prompts/     可复制到不同 AI 工具的提示词
templates/   仅含占位符的空白模板
examples/    明确标记的纯虚构方法演示
scripts/     文档结构、链接与常见敏感信息检查
.github/     自动检查配置
```

## 维护与检查

使用 Python 3.10 或更新版本，无需第三方依赖：

```sh
python3 scripts/check_repository.py
```

检查涵盖结构、站内链接、文件边界及若干常见敏感信息模式，不能替代人工隐私审查。详细规则见[贡献指南](CONTRIBUTING.md)。后续如转为 public，需另行审查完整 Git 历史；当前框架不代表已经连接日历、健康设备或任何个人账号。

本项目未指定开源许可证。未来是否公开、采用何种许可证，由维护者另行决定；仓库可访问性与内容再分发授权应分别处理。
