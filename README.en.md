# Curated Skills

[简体中文](README.md) · English

#### AI skills selected, refined, and used in real projects.

Each skill has been tried on a concrete task before being adapted into instructions others can understand and use. This repository is **Private** and continues to be curated.

## 📋 Contents

| Name | In one sentence | Guide |
|---|---|---|
| [github-project-showcase（GitHub 项目展示同步）](skills/github-project-showcase) | After a project is finished, align its description, links, and screenshots across its GitHub repo, profile, and portfolio. | — |
| [github-readme-maintainer（GitHub README 维护）](skills/github-readme-maintainer) | Write clear project and setup docs for GitHub, add real product screenshots, and prepare Android packages and bilingual release notes. | — |
| [nextjs-github-pages-deploy（Next.js 部署 GitHub Pages）](skills/nextjs-github-pages-deploy) | Publish a Next.js website on GitHub Pages; keep its Vercel version too and fix blank pages or broken assets. | — |

## 📦 Install

In an agent that supports `SKILL.md`, ask it to install the skill and provide the matching folder URL. For example:

```text
Please read and install this skill:
https://github.com/wanghoufan/alw-003-curated-skill-open-source/tree/main/skills/github-readme-maintainer
```

Replace the final folder name with the skill you want. Because this repository is private, the GitHub identity used by the agent must have read access. You can also clone the repository and install the skill folder according to your agent's instructions.

## ✨ Skills

### 🧭 github-project-showcase（GitHub 项目展示同步）

> When a project is ready, its repository and portfolio descriptions should be in sync too.

This skill prepares **one named project** for presentation. It checks repository facts, links, and screenshots, then updates only the GitHub repository, profile, or portfolio destinations you specify. It does not invent features or put a private project on a public page.

**Best for**: Wrapping up one project, checking its presentation, or verifying portfolio links and screenshots. It is not an account-wide portfolio audit.

**How to trigger it**

```text
This project is wrapping up. Sync its repository description and portfolio entry.
Check whether this GitHub repository's description, links, and screenshots are accurate.
Add this project to my GitHub profile README, checking for duplicates first.
```

→ [Open skill](skills/github-project-showcase/SKILL.en.md)

### 📝 github-readme-maintainer（GitHub README 维护）

> Help a first-time visitor understand the project, run it, and see what changed in every release.

It uses repository code and observed behavior to maintain the README, About metadata, and Release notes. A product with a UI gets genuine screenshots near the top: major mobile tabs in one row, or a website home page plus only a few key views. For a formal Android release, it checks for a correctly signed APK and bilingual release notes.

**Best for**: Creating or updating a README, reviewing GitHub About, preparing product screenshots, or publishing an Android APK with bilingual release notes. Do not use it to invent a project description from its name alone.

**How to trigger it**

```text
Update the Chinese and English READMEs from the current code, with genuine screenshots near the top.
Check whether this repository's GitHub About Website should prefer GitHub Pages.
Prepare a GitHub Release for this Android version, attach the signed APK, and write bilingual notes.
```

→ [Open skill](skills/github-readme-maintainer/SKILL.en.md)

### 🚀 nextjs-github-pages-deploy（Next.js 部署 GitHub Pages）

> The tricky parts of publishing a Next.js project site are its subpath and static-export limits.

It checks whether the app can be statically exported, then handles `basePath`, asset paths, dynamic routes, and the Actions workflow. If Vercel stays in place, it separates the two build configurations and verifies both live targets.

**Best for**: Deploying a Next.js project site to GitHub Pages, adding Pages as a mirror for Vercel, or diagnosing blank pages and missing assets. Features that require a server cannot be preserved by static export alone.

**How to trigger it**

```text
Deploy this Next.js project to GitHub Pages.
I want to keep Vercel and add a GitHub Pages version; check what needs to change.
The Pages site is blank. Check basePath, routes, and asset paths.
```

→ [Open skill](skills/nextjs-github-pages-deploy/SKILL.en.md)

## About

This is a personally maintained collection. The repository is private and has no license yet. Before any public release, each skill will be reviewed for scope, privacy, and redistribution rights.
