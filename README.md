# 精选 Skill

中文 · [English](README.en.md)

#### 把真实项目里反复验证过的 AI 工作方法，整理成别人也看得懂、用得上的 Skill。

这里不是把 Skill 攒在一起就算完成。每个入选项都要有明确用途、真实项目经验、可以照着走的步骤和清楚的安全边界。当前先以私有仓库整理与检查，许可证和公开范围确认后再开放。

本仓库里的 Skill 采用 `SKILL.md` 结构，可供支持 Agent Skills 的工具读取；每个工具的具体安装方法取决于使用的智能体和它是否有权访问本私有仓库。

---

## 📋 目录

| 名称 | 一句话 | 说明 |
|---|---|---|
| [github-project-showcase](skills/github-project-showcase/SKILL.md)（GitHub 项目展示同步） | 帮你把一个项目的 GitHub 仓库、个人主页或作品集介绍整理准确、链接验通、截图过隐私检查 | [使用说明](skills/github-project-showcase/SKILL.md) |

---

## 📦 安装与使用

本仓库目前是 **Private**。只有拥有仓库读取权限、且能访问 GitHub 的智能体，才能从这里读取 Skill。

在支持读取 GitHub Skill 的智能体中，可以这样提出安装请求：

```text
请读取并安装这个 Skill：
https://github.com/wanghoufan/alw-003-curated-skill-open-source/tree/main/skills/github-project-showcase
```

也可以先克隆仓库，再按照所用智能体的 Skill 安装说明，将 `skills/github-project-showcase/` 整个目录安装到对应位置。目录中的参考文件需和 `SKILL.md` 放在一起。

如果智能体无法访问私有仓库，先为它配置 GitHub 读取权限；不要把整个仓库或访问令牌贴进对话。仓库未来公开后，会补充各客户端实际验证过的安装命令。

---

## ✨ Skills

### 🧭 github-project-showcase（GitHub 项目展示同步）

> 一个项目做完了，仓库、个人主页和作品集上的介绍也应该跟着对齐。

它帮助你把**一个指定项目**整理到对外展示的位置。先查看真实项目和 GitHub 当前状态，再核对介绍有没有事实依据、链接能不能打开、截图是否泄露隐私；之后只改你点名的展示位置，并回读或打开页面验证结果。

#### 它能帮你做什么

- 整理项目仓库 README、About 简介和相关链接。
- 将项目加入 GitHub 个人主页 README，或修正已有条目。
- 更新作品集网站中的项目介绍、链接和截图。
- 检查 GitHub Pages、Vercel、Release 与图片链接是否真实可用。
- 检查截图和文案中的个人信息、设备标识、密钥及第三方素材授权。

个人主页和作品集是**可选目标**；只更新用户指定的位置，不会猜测账号、网站仓库或内容文件在哪里。它不做全账号盘点，也不接管项目管理。

#### 什么时候用

```text
这个项目准备收尾了，帮我把仓库介绍和作品集条目对齐。
检查这个 GitHub 仓库的 README、主页链接和截图是否适合展示。
把这个项目加到我的 GitHub 个人主页 README，先检查有没有重复。
```

#### 使用前提与边界

- 需要检查 GitHub 时使用已登录的 GitHub CLI `gh`；个人主页或作品集目标必须由使用者提供或明确指定。
- 不把私有项目列入公开页面；不把第三方、fork 或模板作品说成原创。
- 远端编辑、提交、推送、发版或部署只在用户明确要求时执行。
- 没有真实且安全的产品截图时宁可不放，不用 Logo、概念图或装饰图代替。

#### 文件

- [SKILL.md](skills/github-project-showcase/SKILL.md)：主流程和行为边界
- [sync-flows.md](skills/github-project-showcase/sync-flows.md)：不同展示位置的同步步骤
- [cover-rules.md](skills/github-project-showcase/cover-rules.md)：截图选择与隐私检查
- [link-audit.md](skills/github-project-showcase/link-audit.md)：仓库、网站与 Release 链接核验
- [checklist.md](skills/github-project-showcase/checklist.md)：交付前验收清单

---

## 🌱 收录原则

优先收录在真实项目中反复用过、能解决具体问题、又不依赖作者私人环境的 Skill。每项会标清用途、前置条件、限制和来源；第三方内容先确认许可证与署名要求。个人账号信息、机器路径、内部管理流程和私密项目数据不会进入可公开版本。

## 关于与许可

这是一个个人维护的精选集，目前处于私有整理阶段。许可证尚未确定；在许可证和再分发范围明确前，请勿复制或转发其中的 Skill。欢迎先在私有仓库中检查内容和使用方式。
