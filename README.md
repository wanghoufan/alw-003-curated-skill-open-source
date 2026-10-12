# 精选 Skill

中文 · [English](README.en.md)

#### 我从真实项目里挑出、整理并实际用过的 AI Skill。

每项都先在具体工作中验证，再整理成别人看得懂、能照着用的指令。仓库目前为 **Private**，正在持续筛选和完善。

---

## 📋 目录

| 名称 | 一句话 |
|---|---|
| [github-project-showcase（GitHub 项目展示同步）](skills/github-project-showcase/SKILL.md) | 项目收尾时，同步 GitHub 仓库、个人主页和作品集中的项目介绍、链接与截图。 |
| [github-readme-maintainer（GitHub README 维护）](skills/github-readme-maintainer/SKILL.md) | 维护 README、产品截图和 Release；Android 发版时整理 APK 与中英文更新说明。 |
| [nextjs-github-pages-deploy（Next.js 部署 GitHub Pages）](skills/nextjs-github-pages-deploy/SKILL.md) | 部署 Next.js 到 GitHub Pages，处理子路径和静态资源，需要时兼顾 Vercel。 |

---

## 📦 怎么安装

在支持 `SKILL.md` 的智能体中，告诉它要安装哪项，并提供仓库里的对应目录链接。例如：

```text
帮我读取并安装这个 Skill：
https://github.com/wanghoufan/alw-003-curated-skill-open-source/tree/main/skills/github-readme-maintainer
```

把链接末尾换成上面对应的 Skill 文件夹名称。因为仓库是私有的，智能体使用的 GitHub 身份必须有读取权限。也可以先克隆仓库，再按对应客户端的说明安装该 Skill 目录。

---

## ✨ Skills

### 🧭 github-project-showcase（GitHub 项目展示同步）

> 一个项目做完了，仓库和作品集上的介绍也要跟着对齐。

它针对**一个指定项目**，依据仓库里的实际情况核对项目介绍、网站链接和截图，再更新你指定的 GitHub 仓库、个人主页或作品集位置。不会编造功能，也不会把私有项目放到公开页面。

**适合**：项目收尾、校对项目介绍、核验作品集链接和截图。全账号作品盘点不属于这项 Skill。

**怎么触发**

```text
这个项目准备收尾了，帮我把仓库介绍和作品集条目对齐。
检查这个 GitHub 仓库的介绍、主页链接和截图是否准确。
把这个项目加到我的 GitHub 个人主页 README，先检查有没有重复。
```

[查看完整 Skill](skills/github-project-showcase/SKILL.md)

---

### 📝 github-readme-maintainer（GitHub README 维护）

> 让第一次打开仓库的人看得懂、跑得起来，也能看清每次更新了什么。

它根据项目代码和实际运行信息维护 README、GitHub About 和 Release。带界面的产品会在 README 顶部展示真实截图：手机 App 的主要 Tab 并排放图；网页放首页和少量关键页面。Android 正式发布时核对签名 APK，并准备中英文更新说明。

**适合**：新建或更新 README、检查 GitHub About、整理产品截图、发布 Android APK 和双语 Release Notes。

**怎么触发**

```text
根据当前代码整理中英文 README，顶部放真实产品截图。
帮我检查 GitHub About 的 Website 是否应该优先用 GitHub Pages。
准备这个 Android 版本的 GitHub Release，上传签名 APK 并写中英文更新说明。
```

[查看完整 Skill](skills/github-readme-maintainer/SKILL.md)

---

### 🚀 nextjs-github-pages-deploy（Next.js 部署 GitHub Pages）

> 同一个 Next.js 项目发布到 GitHub Pages 时，最容易踩的是项目子路径和静态导出的限制。

它先检查项目能否静态导出，再处理 `basePath`、资源路径、动态路由和 Actions 发布。如果同时保留 Vercel，会区分两种部署配置，并分别核对线上结果。

**适合**：把 Next.js 项目发布到 GitHub Pages、给 Vercel 站点增加 Pages 版本、排查白屏和资源 404。依赖服务器运行时的功能不能只靠静态导出保留。

**怎么触发**

```text
帮我把这个 Next.js 项目部署到 GitHub Pages。
我想同时保留 Vercel，再加一个 GitHub Pages 版本，先检查需要改什么。
Pages 上白屏了，帮我检查 basePath、路由和资源路径。
```

[查看完整 Skill](skills/nextjs-github-pages-deploy/SKILL.md)

---

## 关于

这是一个个人维护的精选集。当前仓库为私有，许可证尚未确定；公开前会继续核对每项内容的适用范围、隐私和再分发条件。
