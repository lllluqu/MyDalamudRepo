# AetherBags 汉化版 — Dalamud 插件源

这是 [AetherBags](https://github.com/Zeffuro/AetherBags)（FF14 背包分类插件）的简体中文汉化版插件源，汉化由 [lllluqu](https://github.com/lllluqu) 维护。

- 汉化源码：[lllluqu/AetherBags](https://github.com/lllluqu/AetherBags)
- 本仓库只存放 Dalamud 插件源清单 `pluginmaster.json`，插件本体从源码仓库的 Release 下载。

## 安装

1. 在游戏内输入 `/xlplugins` 打开插件安装器。
2. 点击底部的 **设置 / Settings**，切到 **实验性功能 / Experimental** 标签页。
3. 在 **自定义插件仓库 / Custom Plugin Repositories** 里粘贴下面的地址，点击 `+`，勾选启用：

   ```
   https://raw.githubusercontent.com/lllluqu/AetherBags-Repo/main/pluginmaster.json
   ```

4. 点击 **保存并关闭**，插件列表会刷新，搜索 **AetherBags 汉化版** 并安装。

> 如果 `raw.githubusercontent.com` 访问困难，可改用加速镜像（把上面的地址替换成镜像前缀 + 原地址），或直接把 `pluginmaster.json` 与 Release 里的 zip 放到自己的静态服务器上。

## 语言说明

- 默认 **跟随客户端语言**：国服 / 中文客户端自动显示简体中文，其他语言客户端显示英文。
- 也可以在插件设置 → 常规 → **语言 / Language** 中手动切换「自动（跟随客户端）」「简体中文」「English」。
- 切换语言后需要关闭并重新打开插件窗口才会生效。

## 与英文原版的区别

| 项目 | 原版 | 汉化版 |
| --- | --- | --- |
| 插件内部名 | `AetherBags` | `AetherBagsCN` |
| 显示名称 | AetherBags | AetherBags 汉化版 |
| 配置目录 | `PluginConfigs/AetherBags` | `PluginConfigs/AetherBagsCN` |
| 游戏内 addon 名 | `AetherBags_*` | `AetherBagsCN_*` |
| IPC 前缀 | `AetherBags.` | `AetherBagsCN.` |

因为内部名不同，**汉化版可以与英文原版同时安装**，互不冲突；但两边的设置、分类配置彼此独立，不会自动迁移。

## 功能概览

- 用游戏原生 UI 替换/增强背包显示，按分类展示物品。
- 自定义分类：名称、描述、颜色、优先级、固定、启用开关。
- 规则筛选：物品 ID、名称正则、界面分类、等级 / 物品品级 / 商店价格区间、稀有度、可交易 / 可染色 / 可分解 / 精炼度等状态。
- 支持游戏分类、自定义分类、Allagan Tools 筛选、BisBuddy 毕业装备、水晶、重要物品等来源。
- 分类显示顺序、物品排序规则、紧凑排布、窗口尺寸、快捷键、服务器信息栏（DTR）格式、最近拾取等设置项。
- 配置导入 / 导出（含 SortaKinda 分类导入）。

## 更新日志

插件自带的更新日志窗口（设置窗口右上角问号按钮）里可以看到每个版本的改动；仓库里的 [changelog](https://github.com/lllluqu/AetherBags/blob/master/AetherBags/changelog.md) 同步维护。

## 自行构建

```powershell
git clone --recurse-submodules https://github.com/lllluqu/AetherBags.git
cd AetherBags
dotnet build -c Release
```

需要 .NET 10 SDK，以及 Dalamud 开发库（`%AppData%\XIVLauncher\addon\Hooks\dev`，可从 <https://goatcorp.github.io/dalamud-distrib/latest.zip> 获取）。

打包产物位于 `AetherBags/bin/x64/Release/AetherBagsCN/latest.zip`。

发布新版本时，把 `AetherBags.csproj` 里的 `<Version>` 提升并推送 `v*` 标签，GitHub Actions 会自动构建并创建 Release（见 `.github/workflows/release.yml`）。

## 致谢与许可

- 原插件作者：Zeffuro、Pie Lover（[Zeffuro/AetherBags](https://github.com/Zeffuro/AetherBags)）
- UI 框架：[KamiToolKit](https://github.com/MidoriKami/KamiToolKit)（MidoriKami）
- 本项目遵循原仓库的 **AGPL-3.0** 许可，源码同样公开。
