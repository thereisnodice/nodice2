# 开发文档

~~本项目暂时以 Dice! 2.5.0 作为移植的蓝本，在完成 80% 以上的基本功能移植之前不会增加新的功能。~~

本项目以 Dice! 2.4 作为指令参照，如有雷同不是巧合。

## 移植计划

### 为何没有 XX 功能

> 如无必要，勿增实体。

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

## Bug

- [ ] 在带原因的指令中将原因写成`{reason}`会造成死锁