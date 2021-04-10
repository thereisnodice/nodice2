<div align="center">
	<img width="128" src="docs/nodice.png" alt="logo"></br>

# NoDice2

*基于 [nonebot2](https://github.com/nonebot/nonebot2)，兼容 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 和 [mirai-api-http](https://github.com/project-mirai/mirai-api-http) 的QQ跑团掷骰机器人*

Demo：[Dr.Sink](https://wpa.qq.com/msgrd?v=3&uin=1351483470&site=qq&menu=yes)

[![License](https://img.shields.io/github/license/thereisnodice/nodice2)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.7.+-blue.svg)
![NoneBot Version](https://img.shields.io/badge/nonebot-2.0.0a11+-red.svg)

</div>

### Commands

**完美移植的功能：**

- [x] 人物作成 `.coc/dnd`
- [ ] 拓展牌堆 `.draw`
- [ ] COC 成长检定 `.en`
- [x] 帮助文档 `.help`
- [x] 今日人品 `.jrrp`
- [ ] 随机姓名 `.name`
- [ ] 设置昵称 `.nn(n)`
- [ ] 旁观模式 `.ob`
- [ ] 角色卡记录 `.pc`
- [x] 标准掷骰 `.r`
- [ ] COC 检定 `.ra/rc`
- [ ] DND 先攻 `.ri` 
- [x] 规则速查 `.rules`
- [ ] COC 理智检定 `.sc`
- [ ] 设置默认骰 `.set`
- [ ] COC 房规 `.setcoc`
- [ ] 属性记录 `.st`
- [ ] 疯狂症状 `.ti/li`
- [ ] WOD 骰池 `.w(w)`

**已整合的功能**

- [ ] 分群牌堆 `.deck` ：整合至拓展牌堆 `.draw` 下，具体形式未定。
- [ ] 先攻列表 `.init` ：整合至 DND 先攻 `.ri` 下，具体形式未定。

**用其他插件实现的功能**

- [x] 退群指令 `.dismiss` ：计划中，目前仍在项目内
- [x] 骰子开关 `.bot on/off`：[nonebot_plugin_manager](https://github.com/Jigsaw111/nonebot_plugin_manager)
- [x] 跑团记录 `.log` ：[TRPGLogger](https://github.com/thereisnodice/TRPGLogger)

**低优先级的功能**

- [ ] 第三人称动作 `.me `
- [ ] 发送消息 `.send`
- [ ] 欢迎词 `.welcome`

**永远不会移植的功能**

- [ ] 集成群管 `.group`
- [ ] 授权许可 `!authorize`

[为什么不移植这些功能](./docs/DEVELOPER.md#某些功能不会移植的原因)

### Developer

[开发文档](./docs/DEVELOPER.md)

### Mannal

[部署指南](./docs/MANNAL.md)

### License

[AGPL-3.0 License](LICENSE)

### Thanks

- [w4123](https://github.com/w4123) aka 溯洄，Dice! 的主要开发者与 Dice3 的开发者。
- [mystringEmpty](https://github.com/mystringEmpty) Dice! 的另一名主要开发者。