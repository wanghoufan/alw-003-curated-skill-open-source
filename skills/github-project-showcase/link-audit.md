# 链接核验

把链接放到公开 README 或作品集前，按本说明逐项核验。

## 仓库信息

使用已认证的 GitHub CLI 查询指定仓库：

```bash
gh api repos/OWNER/REPOSITORY --jq '[.full_name,.visibility,.fork,.default_branch,.pushed_at,.homepage]|@tsv'
```

确认仓库名称是否为当前名称、是否 fork、是否公开。私有仓库不得放入公开展示列表。

## Release 与网站

- 确认 Release 标签存在，且包含预期资产，再放下载链接。
- `/releases/latest` 可能不指向预发布版；必要时使用具体标签页链接。
- 打开线上项目并确认它确属该项目。仅有部署配置不能证明网站已上线。
- 网络超时或代理错误不等于 HTTP 404。宣布死链前应换一种允许的方式复测。
- 条件允许时优先使用仓库内的图片，少用第三方图床。

## 报告证据

每个链接记录完整 URL 和核验结果，例如 HTTP 状态码、页面标题、Release 标签或资产名称。无法完成的检查要标为未验证。
