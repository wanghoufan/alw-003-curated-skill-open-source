---
name: nextjs-github-pages-deploy
description: Use when deploying a Next.js site to GitHub Pages project sites, migrating a compatible site from Vercel, or maintaining a Vercel and GitHub Pages dual deployment.
metadata:
  version: "1.0.0"
  language: zh-CN
  display_name: "Next.js 部署 GitHub Pages"
---

# Next.js 部署 GitHub Pages

把 Next.js 网站部署到 GitHub Pages 项目页，重点处理项目子路径、静态导出和两种部署环境的差异。

## 适用范围

- Next.js App Router 项目部署到 `https://<owner>.github.io/<repo>/`。
- 同一项目保留 Vercel 动态站，并额外发布 GitHub Pages 静态版。
- 排查 Pages 白屏、路由错误、图片或静态资源 404。

纯静态 HTML 无需本 Skill。GitHub 用户页（`<owner>.github.io` 根路径）不需要项目子路径配置。静态导出不支持依赖服务器运行时的功能；若项目必须依赖这些能力，应保留服务器部署，不能强行迁移。

## 执行流程

1. 读取 `package.json`、锁文件、Next.js 配置、路由、API、图片引用、Actions workflow 和 Git 状态；确认项目页还是用户页、仓库名、应用路由和现有线上部署。
2. 盘点静态导出阻塞：服务器端请求信息（cookies/headers）、动态 API、middleware、动态路由参数、图片优化、运行时环境变量、服务端动作及外部数据请求。
3. 先做最小改造。保留 Vercel 行为时，用环境变量只为 Pages 构建打开 `output: "export"`、`basePath`、`trailingSlash` 和必要的 `images.unoptimized`；不要让 Pages 配置改变 Vercel URL 或功能。
4. 统一业务逻辑。把可复用的计算、格式化和纯业务规则放在浏览器与服务端都能使用的模块；把需要后端的功能明确降级、隐藏或接入已有 API，不伪造成功结果。
5. 处理资源路径：Next.js `<Link>` 与 `_next` 由 `basePath` 处理；原生 `<img>`、`<a>` 和数据里的站内绝对路径需要单独加项目子路径。外站 URL、`mailto:`、`data:` URL 不得加前缀。
6. 检查动态路由是否能在构建时列出所有路径。必要时为 `'use client'` 页面拆出服务端壳与客户端组件，避免在不支持的位置导出 `generateStaticParams`。
7. 配置 GitHub Actions 构建并发布导出目录。确认 `permissions: contents: read`，Pages 部署权限按官方 workflow 所需最小化；项目页开启正确的 Pages 来源。留意 `_next` 目录、`.nojekyll`、构建缓存和工作流触发分支。
8. 本地验证生产构建和子路径预览：检查首页、深层路由、刷新、图片、字体、下载文件、外链及浏览器控制台；然后核验 Actions 与线上 Pages 页面。双线项目还要分别验证 Vercel 和 Pages。

## 配置要点

项目页一般需要 `basePath: "/<repo>"`。双线部署可以通过显式环境变量区分构建目标，例如：

```ts
const isPages = process.env.DEPLOY_TARGET === "github-pages";
const basePath = isPages ? process.env.BASE_PATH ?? "" : "";

const nextConfig = {
  ...(isPages ? { output: "export" as const, trailingSlash: true } : {}),
  ...(basePath ? { basePath } : {}),
  images: { unoptimized: isPages },
};
```

示例中的仓库值必须按目标仓库配置；不要把别的项目名复制进来。若当前 Next.js 版本或框架规则与示例不兼容，先查项目安装版本对应的官方文档，再调整。

## 常见症状

| 症状 | 先检查 |
|---|---|
| 首页白屏或刷新 404 | 项目页子路径、路由输出结构、Pages 部署目录和 basePath |
| 图片、字体、下载文件 404 | 是否有未加前缀的站内绝对路径；外部地址有没有误加前缀 |
| 构建通过但页面缺数据 | 是否依赖服务器 API、运行时变量或数据库；静态版是否有明确降级 |
| Vercel URL 行为变化 | Pages 专用配置是否错误地影响 Vercel 构建 |
| Actions 成功但页面仍旧 | Pages 部署来源、artifact 内容、缓存与发布目标是否匹配 |

## 安全与边界

- 先检查工作区改动，不覆盖用户文件；不擅自删掉服务器功能或生产数据。
- 不把秘密写进前端、仓库或 Actions 日志；使用平台提供的 secrets，并区分构建时公开变量与服务端秘密。
- 不更改仓库可见性、域名、生产数据或线上架构，除非用户明确授权。
- 推送或部署仅按用户指示执行；完成后核对线上实际页面，而不只报告构建成功。
