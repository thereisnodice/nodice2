### 某些功能不会移植的原因

TO DO

### 简单的结构说明

TO DO

### 各模块功能说明

TO DO

### Bug

- 突然发现自己写 format_message 的时候留下了一个致命的 bug ：只要在带原因的指令中将原因写成 {reason} ，nodice 就会在这一步无限递归，锁死 nb 。

### Bug(fix)

*已修复的 Bug 会被丢到这来。*

1. 写 [TRPGLogger](https://github.com/thereisnodice/TRPGLogger) 的时候发现我一直以来都把数据储存在插件文件夹里，这对于使用 `git clone` 来下载插件的人没有什么问题，但是一旦有人使用 pypi 来下载插件，数据便会被存储到 python 的 site-package 里，导致挂载在同一台计算机上的 bot 共享数据。

2. 不知道为什么会把 `[` 转义成奇怪的编码，经低调佬指点得知是 get_message 的问题，需要再 extract_plain_text 才行。

### Changelog

TO DO

### Nothing useful

本项目旨在用 python 移植 CQ原生插件 Dice! ~~（虽然本项目的架构更像是 Dice3）~~。

之所以取名 NoDice ，是因为一开始只是想要把 Dice的感叹号移到前面来，也就是 NotDice ，刚好可以把组织名取作 `this is not dice` 来玩双关。接着因为本项目基于 nonebot 框架，就想取个相近的名字，而 not 和 none 就只有 no 这两个字相同了，组织名刚好也能玩双关，只是意思从“这不是骰子”变成了“这里没有骰子”~~（当然我更喜欢翻译为无骰骑士异闻录）~~。