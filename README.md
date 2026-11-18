# MyDalamudRepo — 汉化插件聚合源

这里收录 lllluqu 维护的 Dalamud 汉化 / 中文插件，所有插件共用一个仓库地址，添加一次即可。
仓库本身只存放插件源清单 [`pluginmaster.json`](pluginmaster.json)，插件本体从各自源码仓库的 Release 下载。

## 安装

1. 游戏内输入 `/xlsettings` 打开 Dalamud 设置。
2. 切到 **实验性功能 / Experimental** 标签页。
3. 在 **自定义插件仓库 / Custom Plugin Repositories** 里粘贴下面的地址，点 `+` 并勾选启用：

   ```
   https://raw.githubusercontent.com/lllluqu/MyDalamudRepo/main/pluginmaster.json
   ```

4. **保存并关闭**，然后在 `/xlplugins` 里刷新插件列表，搜索插件名安装。

> 如果 `raw.githubusercontent.com` 访问困难，可以把地址换成镜像前缀 + 原地址，或把 `pluginmaster.json` 与 Release 里的 zip 放到自己的静态服务器。

## 收录插件

| 插件 | 内部名 | 下载量 | 说明 | 源码 / 文档 |
| --- | --- | --- | --- | --- |
| **AetherBags CN** | `AetherBagsCN` | [![下载](https://img.shields.io/github/downloads/lllluqu/AetherBags/total?label=%E4%B8%8B%E8%BD%BD&color=blue)](https://github.com/lllluqu/AetherBags/releases) | 用原生 UI 按分类整理背包，支持自定义分类、规则筛选、排序、货币显示等 | [lllluqu/AetherBags](https://github.com/lllluqu/AetherBags) |
| **Avarice CN** | `AvariceCN` | [![下载](https://img.shields.io/github/downloads/lllluqu/AvariceCN/total?label=%E4%B8%8B%E8%BD%BD&color=blue)](https://github.com/lllluqu/AvariceCN/releases) | 像素级精确的身位判定反馈：背/侧身预读扇形、射程圈、场中心点、命中/未命中反馈等 | [lllluqu/AvariceCN](https://github.com/lllluqu/AvariceCN) |
| **Mouseover Action CN** | `MOActionCN` | [![下载](https://img.shields.io/github/downloads/lllluqu/MOActionPluginCN/total?label=%E4%B8%8B%E8%BD%BD&color=blue)](https://github.com/lllluqu/MOActionPluginCN/releases) | 不用宏也能对悬停目标释放技能，支持按职业配置动作堆栈与修饰键 | [lllluqu/MOActionPluginCN](https://github.com/lllluqu/MOActionPluginCN) |
| **JobBars CN** | `JobBarsCN` | [![下载](https://img.shields.io/github/downloads/lllluqu/JobBarsCN/total?label=%E4%B8%8B%E8%BD%BD&color=blue)](https://github.com/lllluqu/JobBarsCN/releases) | 额外职业量谱、队友增益计时、减伤监控、图标替换与光标提示 | [lllluqu/JobBarsCN](https://github.com/lllluqu/JobBarsCN) |

下载量徽章由 [shields.io](https://shields.io) 实时渲染（数据来自 GitHub Releases 资产下载数，约 5 分钟缓存；GitHub 按 24 小时内同一请求方最多计一次，所以近似"独立安装/更新次数"）。若 shields.io 访问困难，可把徽章域名换成国内镜像（如 `img.shields.icu`）。同时 [`.github/workflows/download-stats.yml`](.github/workflows/download-stats.yml) 每 15 分钟把这些数字同步进 `pluginmaster.json` 的 `DownloadCount` 字段（脚本：[`tools/sync_stats.py`](tools/sync_stats.py)）。

每个插件的安装、语言设置、版本号规则等详细说明，见各自源码仓库的 README（如 AetherBags 的[中文说明](https://github.com/lllluqu/AetherBags#%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E6%B1%89%E5%8C%96%E7%89%88--chinese-localization)）。

## 说明

- 插件之间保持各自独立的 `InternalName`，可与对应的英文原版同时安装。
- 每个插件遵循其源码仓库的许可证（AetherBags、JobBars 为 AGPL-3.0，Avarice 为 BSD-3-Clause）。
- 插件源格式参考 [Dalamud 官方文档](https://dalamud.dev/plugin-publishing/custom-repositories/)。
