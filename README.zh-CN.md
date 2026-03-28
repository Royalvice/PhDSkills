# PhDSkills

[![Stars](https://img.shields.io/github/stars/Royalvice/PhDSkills?style=for-the-badge&logo=github)](https://github.com/Royalvice/PhDSkills/stargazers)
[![Visitors](https://komarev.com/ghpvc/?username=Royalvice&repo=PhDSkills&style=for-the-badge)](https://github.com/Royalvice/PhDSkills)
[![Skills](https://img.shields.io/badge/skills-growing-0ea5e9?style=for-the-badge&logo=bookstack&logoColor=white)](#技能目录)
[![Status](https://img.shields.io/badge/status-active-22c55e?style=for-the-badge&logo=vercel&logoColor=white)](#)

> 面向博士研究工作流的 Codex skills 仓库，覆盖写作、发布、文献处理、研究协作与学术生产效率。

[English](./README.md) | 简体中文

## 仓库定位

`PhDSkills` 是一个为研究密集型场景设计的 Codex skills 库。
它服务于博士生、导师、研究助理以及需要标准化学术流程的研究团队，目标不是堆砌提示词，而是沉淀可复用、可维护、可自动化的技能工作流。

这个仓库从一开始就按“未来会持续增长”的方式设计，方便后续逐步扩展为覆盖完整学术生命周期的 skills 集合。

## 提供什么

- `写作工作流`：学术 Markdown、论文草稿、学位论文、开题、中期、报告与修订流程
- `发布工作流`：DOCX、PDF、HTML、Quarto、Pandoc、模板、参考文献与结构校验
- `研究运维`：环境检查、项目初始化、可复现流程与自动化任务
- `知识管理`：引文、参考文献、资料整理、笔记流与阅读支持
- `扩展结构`：为未来新增大量技能保留统一规范，不需要反复重构仓库

## 仓库结构

```text
PhDSkills/
├─ AGENTS.md
├─ README.md
├─ README.zh-CN.md
├─ .gitignore
├─ ai-research-landscape/
│  ├─ SKILL.md
│  ├─ scripts/
│  ├─ assets/
│  ├─ references/
│  └─ agents/
├─ draft-ai-phd-reports/
│  ├─ SKILL.md
│  ├─ scripts/
│  ├─ assets/
│  ├─ references/
│  └─ agents/
├─ frontend-slides/
│  ├─ SKILL.md
│  ├─ scripts/
│  ├─ assets/
│  ├─ references/
│  └─ agents/
├─ md2all/
│  ├─ SKILL.md
│  ├─ scripts/
│  ├─ assets/
│  ├─ references/
│  └─ agents/
├─ agent-project-system/
│  ├─ SKILL.md
│  ├─ scripts/
│  ├─ assets/
│  ├─ references/
│  └─ agents/
├─ report-image-integrator/
│  ├─ SKILL.md
│  ├─ scripts/
│  ├─ assets/
│  ├─ references/
│  └─ agents/
├─ report-to-flowchart-prompt/
│  ├─ SKILL.md
│  ├─ scripts/
│  ├─ assets/
│  ├─ references/
│  └─ agents/
├─ report-to-talk-slides/
│  ├─ SKILL.md
│  ├─ scripts/
│  ├─ assets/
│  ├─ references/
│  └─ agents/
└─ <future-skill>/
   ├─ SKILL.md
   ├─ scripts/
   ├─ assets/
   ├─ references/
   └─ agents/
```

## 技能目录

这个部分刻意保留为可增长结构。

| 技能 | 状态 | 关注点 |
| --- | --- | --- |
| `ai-research-landscape` | 已提供 | 已验证的 AI 文献脉络综述与参考文献整理 |
| `agent-project-system` | 已提供 | 面向 AI 自主推进的项目状态文档、恢复契约与证据化治理 |
| `draft-ai-phd-reports` | 已提供 | AI 博士报告撰写、重写与引文感知润色 |
| `frontend-slides` | 已提供 | HTML 幻灯片创建与 PPT 转网页演示工作流 |
| `md2all` | 已提供 | Markdown 与 Quarto 发布工作流 |
| `report-image-integrator` | 已提供 | 面向 Markdown 报告的图像内容筛选、插入、重命名与交叉引用 |
| `report-to-flowchart-prompt` | 已提供 | 从报告、研究计划和提案生成研究总览流程图图像提示词 |
| `report-to-talk-slides` | 已提供 | 从报告和技术文稿生成演讲幻灯片蓝图 |
| `future-skill` | 预留 | 随着仓库扩展在此新增技能 |

## 设计原则

- `确定性优先`：优先脚本、资源和显式工作流，而不是模糊行为
- `默认保守`：避免无必要改写和隐式修改
- `可组合`：每个 skill 都应可独立使用，也能与其他 skill 协同
- `可迁移`：工作流应尽量适用于不同机器和环境
- `可维护`：仓库元数据与技能清单必须和实际目录保持同步

## 新增技能约定

每个 skill 都应位于仓库根目录下的独立文件夹，并以 `SKILL.md` 作为入口。

推荐结构：

```text
new-skill/
├─ SKILL.md
├─ scripts/
├─ assets/
├─ references/
└─ agents/
```

新增 skill 时应同时完成：

1. 创建 skill 目录与 `SKILL.md`
2. 根据需要补齐 `scripts`、`assets`、`references`、`agents`
3. 更新 `README.md` 中的 `Skill Catalog`
4. 更新 `README.zh-CN.md` 中对应的技能目录
5. 保持 `AGENTS.md` 中的规则与当前仓库状态一致

## 适用场景

- 为博士研究工作建立长期可维护的个人 Codex 技能库
- 在实验室或课题组内共享可复用的学术工作流
- 标准化文档转换与发布流程
- 为论文、学位论文、综述、数据处理与学术行政任务预留后续技能位置

## 贡献

贡献前请先遵守 [`AGENTS.md`](./AGENTS.md) 中的仓库协作规则。
如果新增了 skill，没有同步 README 文档，变更就不算完整。

## 路线图

- 从发布场景继续扩展到更完整的博士研究工作流
- 增加更多可复用模板与面向具体场景的工具能力
- 提升技能发现、验证和上手体验

## 许可证

在对外广泛分享前，请补充与你预期共享方式一致的许可证。
