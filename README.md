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

| 插件 | 内部名 | 说明 | 源码 / 文档 |
| --- | --- | --- | --- |
| **AetherBags 汉化版** | `AetherBagsCN` | 用原生 UI 按分类整理背包，支持自定义分类、规则筛选、排序、货币显示等 | [lllluqu/AetherBags](https://github.com/lllluqu/AetherBags) |

每个插件的安装、语言设置、版本号规则等详细说明，见各自源码仓库的 README（如 AetherBags 的[中文说明](https://github.com/lllluqu/AetherBags#%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E6%B1%89%E5%8C%96%E7%89%88--chinese-localization)）。

## 维护者：新增一个插件

1. 在插件源码仓库里构建并发布 Release，资产名带版本号（如 `AetherBagsCN-1.0.0.51.zip`），避免 GitHub 下载缓存命中旧文件。
2. 把新条目保存成 `entry.json`（模板如下）：

```json
{
    "Author": "作者 / 汉化者",
    "Name": "插件显示名",
    "Description": "插件简介（中文）",
    "InternalName": "PluginInternalName",
    "AssemblyVersion": "1.0.0.1",
    "RepoUrl": "https://github.com/lllluqu/插件源码仓库",
    "ApplicableVersion": "any",
    "Tags": ["ui"],
    "CategoryTags": ["ui"],
    "DalamudApiLevel": 15,
    "Punchline": "一句话简介",
    "IconUrl": "https://raw.githubusercontent.com/lllluqu/插件源码仓库/master/Images/icon.png",
    "DownloadLinkInstall": "https://github.com/lllluqu/插件源码仓库/releases/download/v1.0.0.1/Plugin-1.0.0.1.zip",
    "DownloadLinkUpdate": "https://github.com/lllluqu/插件源码仓库/releases/download/v1.0.0.1/Plugin-1.0.0.1.zip",
    "DownloadLinkTesting": "https://github.com/lllluqu/插件源码仓库/releases/download/v1.0.0.1/Plugin-1.0.0.1.zip",
    "IsHide": false,
    "IsTestingExclusive": false,
    "DownloadCount": 0,
    "LastUpdated": 0
}
```

3. 合并进清单（按 `InternalName` 去重，同名的旧条目会被替换）：

   ```powershell
   python tools/merge_pluginmaster.py --master pluginmaster.json --entry entry.json
   ```

4. 提交 `pluginmaster.json`，玩家刷新列表后就能看到新插件。

> 不要直接用 PowerShell 的 `ConvertTo-Json` 往数组里加对象：PS 5.1 会把嵌套数组写成 `{"value": [...], "Count": n}`，Dalamud 会解析失败。上面的脚本会按标准扁平数组写出。

## 说明

- 插件之间保持各自独立的 `InternalName`，可与对应的英文原版同时安装。
- 每个插件遵循其源码仓库的许可证（AetherBags 为 AGPL-3.0）。
- 插件源格式参考 [Dalamud 官方文档](https://dalamud.dev/plugin-publishing/custom-repositories/)。
