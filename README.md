# AI-Guides-Life

用 AI 辅助长期了解、综合建议、周期规划、执行与复盘的通用方法论库。

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
| 日常作息 | 如何统筹月、周、日与全部领域，并按实际反馈调整 | [作息指南](domains/01-daily-routine/README.md) |
| 睡眠 | 如何结合持续设备记录与体验，形成阶段总结和建议 | [睡眠指南](domains/02-sleep/README.md) |
| 饮食 | 如何从粗略记录估计摄入、识别结构缺项并持续复盘 | [饮食指南](domains/03-nutrition/README.md) |
| 喝水 | 如何记录每日大致饮用量并降低习惯执行的阻力 | [喝水指南](domains/04-hydration/README.md) |
| 健身 | 如何结合情况、训练与设备记录，给出分类型建议和安排 | [健身指南](domains/05-fitness/README.md) |
| 通勤 | 如何了解实际成本、优化方式与时长，并选择合适的时间用途 | [通勤指南](domains/06-commute/README.md) |
| 读书 | 如何结合历史与目标，建议书籍、阅读时长和方法 | [读书指南](domains/07-reading/README.md) |
| 出行、旅游 | 如何评估是否参加、优化行程与时间使用并复盘 | [出行指南](domains/08-travel/README.md) |
| 交友见面 | 如何评估活动、控制负担、协调安排与选择合意记录 | [见面指南](domains/09-social/README.md) |

日常作息是统筹层，连接月、周、日及其他八个领域；各领域在私有空间积累必要记录后形成阶段建议。出行旅游与见面按事件触发，先评估是否参加和如何调整，再安排与复盘。所有真实记录和设备数据仍在仓库之外。

## 共用方法

- [系统方法](docs/methodology.md)：目标、约束、最小动作、反馈与调整。
- [长期了解与阶段建议](docs/longitudinal.md)：观察范围、记录质量、设备估计和综合总结。
- [跨领域协调](docs/cross-domain.md)：处理睡眠、饮食、训练、通勤和社交之间的冲突。
- [活动取舍与复盘](docs/activity-evaluation.md)：时间全成本、多种价值、参加或放弃及可选合意记录。
- [自动化分级](docs/automation.md)：确定 AI 可以建议、草拟、提醒和执行的边界。
- [信息核实](docs/evidence.md)：区分已知事实、用户输入、假设和待核实项。
- [健康、设备与记录方法来源](docs/health-sources.md)：穿戴估计、饮食误差、补充剂与录音参考的适用边界。
- [实施路线](docs/roadmap.md)：明确已交付内容与尚未实现的功能。

## 提示词与模板

- 提示词：[通用工作流](prompts/core.md)、[跨领域规划](prompts/planning.md)、[复盘与方案评审](prompts/review.md)。
- 空白模板：[个性化配置](templates/personal-setup.md)、[日计划](templates/daily-plan.md)、[周复盘](templates/weekly-review.md)、[单变量尝试](templates/experiment.md)、[自动化约定](templates/automation-contract.md)、[信息核实表](templates/source-check.md)。
- 周期与综合模板：[月计划](templates/monthly-plan.md)、[周计划](templates/weekly-plan.md)、[阶段总结](templates/period-review.md)、[活动评估](templates/activity-review.md)。
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
