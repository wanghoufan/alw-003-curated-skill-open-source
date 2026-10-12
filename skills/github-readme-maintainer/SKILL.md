---
name: github-readme-maintainer
description: Use when writing, reviewing, or updating a software project's GitHub README, repository About metadata, product screenshots, or GitHub Release notes. Verify claims against the repository and keep requested languages aligned.
metadata:
  version: "1.0.0"
  language: zh-CN
  display_name: "GitHub 项目文档维护"
---

# GitHub 项目文档维护

让第一次访问仓库的人快速理解项目、看到真实产品、按说明运行，并能从清楚的版本记录中了解每次发布。

## 适用任务

- 新建、重写或维护 `README.md` 及对应的其他语言版本。
- 更新 GitHub About 的 Description、Website、Topics。
- 为有界面的产品整理真实截图。
- 发布或维护 GitHub Release，尤其是 Android APK 与双语更新说明。

## 工作顺序

1. **确认目标与当前状态**：读取仓库文件、分支、工作区改动、近期提交、版本配置、构建与发布流程。确认本次只处理哪些文档或发布内容。
2. **建立事实依据**：从代码、配置、实际运行结果、用户提供且可核验的信息中整理名称、用途、功能、平台、安装步骤、限制和版本变化。无法证实的内容标成待确认，不要补猜。
3. **规划读者路径**：README 开头先讲产品是什么、解决什么问题、如何开始；细节按需放入 `docs/`。只新增读者确实需要的文档。
4. **整理截图**：GUI / Web 产品的 README 顶部须有真实产品界面图。手机 App 展示每个主要底部 Tab 的一张图，横向并排、等比例缩小；常见显示宽度约 140–220px，不拉伸成全宽。网页通常放首页，必要时加 1–2 张关键页面；总数控制在 1–3 张。可使用与当前实现一致的无数据演示界面。没有真实界面图时列为发布阻断项，不能用 Logo、概念图或虚构画面替代。无界面的 CLI、库、API 不强制配图。
5. **维护语言版本**：若项目采用中英文 README，中文和英文都更新。两者的功能、版本、命令、限制、链接和图片顺序保持一致；英文自然表达，不额外添加未经证实的能力。
6. **检查链接和隐私**：逐个验证仓库、在线站点、文档、下载和图片链接。GitHub About 的 Website 优先选择已实际发布且可访问的 GitHub Pages，其次 Vercel，再次其他真实在线站点；不能只凭配置推断已上线。检查截图、文档和提交内容，排除密钥、令牌、个人数据和未经许可的素材。
7. **回读与交付**：检查 Markdown 渲染、相对链接、双语一致性、拼写、命令可复制性和变更范围。报告完成项及未验证项。

## README 编写规则

- 标题使用仓库中能证实的正式项目名；紧接一句普通读者能懂的用途说明。
- 有界面时，标题和简介之后尽早放真实产品截图；不要让徽章、目录树、技术栈挡住产品介绍。
- 按项目类型提供必要的安装、配置、启动和最小使用步骤。示例命令必须来自真实项目。
- 功能介绍讲用户能完成什么；技术栈、架构和完整参数放在后续章节或独立文档。
- 环境变量文档只写变量名、用途和安全的示例格式，不能写真实值。
- GitHub About 的 Description、Website、Topics 以仓库事实为准，不虚构功能或站点。

## Android APK 与 GitHub Release

当任务包含 Android APK 的正式发布或换机备份分发时：

1. 确认仓库版本、应用版本、构建来源和目标架构；构建或取得与该版本对应的**可安装、正确签名** APK。不得上传 debug 包冒充正式版。
2. 仓库公开或私有都应把用户要求保留的最新 APK 附在 GitHub Release，确保用户在有权限的设备上可下载。仓库可见性只影响谁能访问，不改变“保存安装包”的要求。
3. 给 Release 写中文和英文更新说明。按用户、开发者都能读懂的内容归纳：新增功能、改进、修复、已知限制、兼容要求；只写有代码、提交或验证证据的变化。没有变化的类别可省略。
4. Release 标题和 tag 对应实际版本；附件文件名、包版本与说明一致。上传前检查 APK 大小、签名、SHA-256 和附件是否为正确文件。
5. 发布后打开 Release 页面，核对标题、双语说明和 APK 附件，并用下载或 API 元数据确认附件可取。下载后可复核 SHA-256。

推荐的双语 Release 说明结构：

```markdown
## 简体中文
### 本次更新
- 新增：……
- 优化：……
- 修复：……
### 安装与兼容
- Android：……
- 安装包：`<filename>.apk`（SHA-256：`<hash>`）

## English
### What’s new
- Added: …
- Improved: …
- Fixed: …
### Install and compatibility
- Android: …
- Package: `<filename>.apk` (SHA-256: `<hash>`)
```

不要为了套模板虚构更新项；不适用的条目删掉。Release 不是 README，避免粘贴整份技术文档。

## Git 与发布边界

- 默认先审阅工作区改动，不覆盖用户已有更改。
- 只有用户明确要求提交、推送、创建 Release 或部署时才执行对应远端操作。
- 用户已明确授权发布时，先完成本地文档与产物检查，再提交和推送；最后用系统默认浏览器打开最新 GitHub 页面供检查，并亲自核对线上结果。
- 仓库公开、修改可见性、覆盖既有 Release、替换已发布附件等高影响操作须获得明确授权。

## 触发示例

```text
帮我根据当前代码整理中英文 README，顶部要有真实产品截图。
为这个 Android 版本准备 GitHub Release，上传签名 APK，并写中英文更新说明。
检查 GitHub About 的 Website 是否应使用 GitHub Pages。
```
