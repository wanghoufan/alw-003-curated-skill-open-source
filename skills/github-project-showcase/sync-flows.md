# 展示位置同步流程

只执行用户指定目标对应的小节。运行命令前确认仓库所有者与仓库名准确。

## 项目仓库

读取当前 README 和 GitHub About 值。对照项目文件和线上站点核实 README 中的链接。如果任务包含 Android Release 资产，遵循项目发布规范并核对应用标识、版本、签名和更新说明；否则不要创建 Release。

## GitHub 个人主页 README

个人主页 README 位于与 GitHub 用户名同名的仓库中。编辑前确认用户名和仓库名，不要根据本机账号名称猜测。

1. 读取当前 `README.md` 并记录文件 SHA。
2. 搜索目标项目的仓库名。已有条目时只改该条；不存在时，只在用户确认的分类中新增。
3. 文件中有项目总数时，仅在新条目确实新增且数字能核实时修改总数。
4. 通过 GitHub Contents API 写入并带上第 1 步读取的 SHA；写后重新读取，比较修改文字。

### 双语个人主页 README

如果个人主页仓库同时有 `README.md` 和 `README.en.md`，将其作为同一份项目清单的两个语言视图。分别通过 Contents API 读取两份文件；`readme` 端点只返回 GitHub 默认展示的文件。记录两份各自的 SHA，并在写入前分别查找目标项目。

- 两份文件的项目集合、目标链接、分类数量与顺序、分类小计和总数必须一致。可以翻译说明文字，但不得增删项目。
- 每份文件都使用各自最新 SHA 写入，随后重新读取验证；如果 SHA 变化，先重新读取并合并并发修改，不能覆盖。
- 修改任意一份后都运行只读校验：

  ```bash
  python3 <skill-directory>/scripts/parity_check.py --owner <github-login>
  # 有本地副本时可离线检查：
  python3 <skill-directory>/scripts/parity_check.py --owner <github-login> --readme <workspace>/README.md --readme-en <workspace>/README.en.md
  ```

- 若输出 `PARITY-DRIFT`，在本次任务范围内修复并重跑到 `PARITY-OK`。无关条目已有漂移时单独报告，不顺手重写。
- 如果没有 `README.en.md`，除非用户要求创建英文主页，否则不要新建；此时校验脚本不适用。

## 作品集网站

从用户或仓库说明定位站点内容源。优先改源数据，不改生成页面。依照既有字段填写 slug、标题、简介、状态、仓库链接、线上链接、Release 链接和截图路径；逐项按当前事实核对。遵循已有排序规则；若规则不明确，保留原顺序并询问。修改后运行站点文档规定的检查。

## 提交与部署

暂存前检查 `git status`、当前分支、remote 和 diff。只暂存本次任务涉及的文件，禁止强制推送。只有用户明确要求时才提交、推送或部署；执行后核实远端 HEAD 和部署状态。推送成功本身不代表托管网站已完成部署。
