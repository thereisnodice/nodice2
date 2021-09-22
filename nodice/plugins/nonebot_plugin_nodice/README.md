# Nonebot Plugin NoDice

*基于 [nonebot2](https://github.com/nonebot/nonebot2) 和 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的 QQ 跑团掷骰插件*

[![License](https://img.shields.io/github/license/thereisnodice/nodice2)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.7.3+-blue.svg)
![NoneBot Version](https://img.shields.io/badge/nonebot-2.0.0a11+-red.svg)
![Pypi Version](https://img.shields.io/pypi/v/nonebot-plugin-nodice.svg)

## Commands

### 核心功能

- [x] 掷骰`.roll` `.r`
  - [ ] 设置默认骰`.set`
- [ ] 角色卡`.char` `.pc`
  - [ ] 设置昵称`.nn(n)`
  - [ ] 属性记录`.st`
  - [ ] 人物作成`.coc` `.dnd`
- [ ] 拓展牌堆`.draw` `.deck`
  - [ ] 随机姓名`.name`

### COC 拓展

- [ ] COC 检定`.ra` `.rc`
  - [ ] COC 房规`.setcoc`
  - [ ] COC 理智检定`.sc`
  - [ ] COC 成长检定`.en`
- [x] 疯狂症状`.ti` `.li`
- [ ] 旁观模式`.ob`

### 依赖于溯洄公开服务的功能

- [x] 今日人品`.jrrp`
- [x] 规则速查`.rules`
- [x] 跑团记录`.log` [TRPGLogger](https://github.com/thereisnodice/TRPGLogger)

### 暂不实现的功能

- [ ] 骰子开关`.bot` **REPLACE** [nonebot_plugin_manager](https://github.com/Jigsaw111/nonebot_plugin_manager)
- [ ] WOD 骰池`.w(w)` **TODO**
- [ ] DND 先攻`.ri` **TODO**
- [ ] 先攻列表`.init` **TODO**
- [ ] 发送消息`.send` **MAYBE**
- [ ] 集成群管`.group` **MAYBE**
- [ ] 欢迎词`.welcome` **MAYBE**
- [ ] 退群指令`.dismiss` **MAYBE**
- [ ] 第三人称动作`.me` **NEVER**
- [ ] 授权许可`!authorize` **NEVER**

## License

[AGPL-3.0 License](LICENSE)

## Thanks

- [w4123](https://github.com/w4123) aka 溯洄，Dice! 的主要开发者与 Dice3 的开发者。
- [mystringEmpty](https://github.com/mystringEmpty) Dice! 的另一名主要开发者。