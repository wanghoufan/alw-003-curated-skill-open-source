---
name: vercel-deploy-triage
description: Use when a Vercel deployment is blocked or skipped, a deployment reports success but the live site is stale, or Git integration rejects a commit author.
metadata:
  version: "1.0.0"
  language: zh-CN
  display_name: "Vercel 部署故障诊断"
---

# Vercel 部署故障诊断

先找出部署卡在哪里，再选择影响最小的修复方式。状态名相似不代表原因相同，不能靠重复部署碰运气。

## 适用场景

- 部署显示 `BLOCKED`、`UNKNOWN`、`SKIPPED` 或未生成构建。
- 命令显示成功，但线上仍是旧版本。
- Git 集成提示提交作者无法关联到 GitHub/Git provider 账号。

## 诊断流程

1. 收集项目、团队、Git 仓库、分支、commit SHA、部署 ID、状态、错误原文、创建时间和生产域名。优先使用 Vercel CLI、部署详情/API 和 Git 状态做只读检查。
2. 判断部署触发来源：Git 集成、CLI、外部 API 或手动操作。对照预期生产分支、commit SHA 与实际部署记录，避免把预览部署当生产部署。
3. 读取完整错误和跳转到的官方说明；区分 Git 作者/协作权限、构建失败、项目关联、额度、队列、缓存、域名和平台故障。不要仅凭 `UNKNOWN` 猜根因。
4. 若提示作者无法关联，核验 commit author email 是否属于已连接的 Git 账号，检查 Git 集成权限、团队成员资格和项目关联。不要公开仓库来绕过权限检查。
5. 若构建成功但线上旧，确认 production deployment 指向的 commit、域名别名、缓存和项目是否一致；重新部署前先确认是否会重复运行有副作用的构建步骤。
6. 先提出最小、可逆的修复方案。修改 Git 身份、团队权限、计费、项目关联、仓库可见性或生产域名之前，说明影响并等待授权。
7. 修复后用新的部署记录和线上页面验证：部署状态为 Ready、生产域名指向正确部署、页面内容或版本标识与预期 commit 一致。保留错误原文与修复证据。

## 只读检查示例

```bash
vercel project ls
vercel ls
vercel inspect <deployment-url>
git status --short
git log -1 --format='%H%n%an <%ae>'
git remote -v
```

命令选项随 Vercel CLI 版本变化；先用 `vercel --help` 或 CLI 官方文档确认当前语法。不要把 Token 放进命令历史、输出或报告。

## 处理原则

- 初始诊断只读；只在已确认根因后提出修复。
- 不把仓库公开、升级付费套餐、改写提交历史或改变团队权限当成默认解法。
- 若使用无 Git 元数据的临时目录、重置缓存或重跑构建，先确认不会遗漏必要文件或造成副作用。
- 不通过删除遮罩、修改服务端响应或伪造状态来绕过平台限制。
- 不确定时保留错误与证据，说明需要补查的项目；不宣称“已修复”。

## 完成标准

报告根因（或仍待确认的假设）、证据、采取的变更、部署 ID/commit、线上验证结果和剩余风险。构建成功本身不等于生产站点已更新。
