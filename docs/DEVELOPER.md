### TO DO List

- `.admin update` `.admin reload`
- `.bot on/off` `.dismiss`

### 简单的架构说明

TO DO

### 各模块功能说明

*以下说明已不可靠，请直接看源码或者等待更新。*

#### calculator.py

计算/掷骰核心,由可以进行标准掷骰的基类 `BaseCalculator`  继承出 `CocCalculator` `FateCalculaotr` `WodCalculator` 等派生类,是所有掷骰相关功能的核心。 

**相关功能:**

- [ ] 标准掷骰 `.r(h) 4#3d6k2+5 reason`
- [ ] 设置默认骰 `.set`
- [ ] COC 检定 `.ra(h)`
- [ ] COC 房规 `.setcoc`
- [ ] DND 先攻 `.ri` 
- [ ] 先攻列表 `.init`
- [ ] FATE 掷骰 `.rf`
- [ ] WOD 骰池 `.w(w)`
- [ ] COC 理智检定 `.sc`
- [ ] COC 成长检定 `.en`
- [ ] COC 奖惩骰 `.rb/p`

#### deck.py

牌堆核心,将重构为Deck类,负责读取 `decks` 目录下的所有json文件和yml文件，并存入内存当中。（在nodice1时期每抽取一次牌堆都会读取一次所有牌堆，这对于效率是一个很大的问题。本版本将修复此问题，作为代价每次加了新牌堆都必须手动更新。）

**相关功能:**

- [ ] 拓展牌堆 `.draw` 
- [ ] 分群牌堆 `.deck`
- [ ] 疯狂抽取 `.ti/li`
- [ ] 随机姓名 `.name`

#### character.py

负责管理角色卡与人物作成，顺便把人物做成和人物卡设置对接到一起以便自动生成可调用的人物卡。

- [ ] 人物作成 `.coc/dnd`
- [ ] 角色卡 `.pc`
- [ ] 角色卡设置 `.st`
- [ ] 设置昵称 `.nn(n)`

#### group.py

群管模块，开关、欢迎词、群管操作，跟QQ群有较大关系的功能都会丢到这里。

- [ ] 骰子开关 `.bot on/off`
- [ ] 退群指令  `.dismiss`
- [ ] 欢迎词 `.welcome`
- [ ] 群管理操作 `.group `
- [ ] 旁观者模式 `.ob`

#### admin.py

骰主管理模式，要注意的是Nonebot自身有一个SUPERUSER权限，但它的权限在这里是没有用处的，你必须手动认主才能使骰娘正常工作。

*nodice1的bot_control也被合并到了该模块。*

- [ ] 骰主绑定 `.master`
- [ ] 全局管理 `.admin`

#### logger.py

本属于TRPGlogger的功能，被我也整合进了nodice里，同时支持自动格式处理以适配[ auto_video ](https://github.com/jigsaw111/auto_video)。

- [ ] 跑团记录 `.log`

#### help.py

帮助功能信息，基本都是写死的字符串。

- [ ] 帮助文档 `.help`
- [ ] 自定义帮助词条 `.helpdoc`
- [ ] 自定义回执文本 `.str`

#### others.py

不知道该往哪分类的神奇功能，就都丢到这个模块了。后面两个功能可以选择本地或者调用溯洄的API（默认使用本地服务）。

- [ ] 第三人称动作 `.me`
- [ ] 发送消息 `.send`
- [ ] 今日人品 `.jrrp`
- [ ] 规则速查 `.rules`

#### sqlite.py  

链接sqlite3数据库，所有需要数据库的操作都通过此模块进行。

#### utils.py  

工具模块，负责给__init__.py提供接口以便调用其他函数。

#### nb.py

适配 nonebot

#### nb2.py

适配 nonebot2

#### constant.py

储存第一次运行时需要释放的数据

### Bug

- 突然发现自己写 format_message 的时候留下了一个致命的 bug ：只要在带原因的指令中将原因写成 {reason} ，nodice 就会在这一步无限递归，锁死 nb 。

### Note

*已修复的 Bug 会被丢到这来。*

1. 写 [TRPGLogger](https://github.com/thereisnodice/TRPGLogger) 的时候发现我一直以来都把数据储存在插件文件夹里，这对于使用 `git clone` 来下载插件的人没有什么问题，但是一旦有人使用 pypi 来下载插件，数据便会被存储到 python 的 site-package 里，导致挂载在同一台计算机上的 bot 共享数据。

2. 不知道为什么会把 `[` 转义成奇怪的编码，经低调佬指点得知是 get_message 的问题，需要再 extract_plain_text 才行。