# 部署指南

## 快速开始 (Windows)

确保你已经下载并安装了 [Git](https://git-scm.com/) 和 [Python](https://www.python.org/).

为了压缩仓库大小，本项目不再内置 go-cqhttp，请自行下载 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp/releases)

现在，在你想要安装 NoDice 的目录打开 `Git bash`，逐条执行以下命令。

```shell
git clone git@github.com:thereisnodice/nodice2.git
cd nodice2/nodice/
poetry install
```

接着，在 nodice2 目录创建 `go-cqhttp` 文件夹（当然你也可以把 go-cqhttp 文件夹放到其他地方，只是放在一起更方便管理）并将之前下载好的 go-cqhttp 复制到该目录下。

### 配置 go-cqhttp

运行一次 go-cqhttp ，此时目录下会出现 `config.yml` 文件，按如下修改配置。

```yml
# go-cqhttp 默认配置文件

account: # 账号相关
  uin: 0 # QQ账号
  password: "" # 密码为空时使用扫码登录
  encrypt: false  # 是否开启密码加密
  status: 0      # 在线状态 请参考 https://github.com/Mrs4s/go-cqhttp/blob/dev/docs/config.md#在线状态
  relogin: # 重连设置
    disabled: true
    delay: 3      # 重连延迟, 单位秒
    interval: 0   # 重连间隔
    max-times: 0  # 最大重连次数, 0为无限制

  # 是否使用服务器下发的新地址进行重连
  # 注意, 此设置可能导致在海外服务器上连接情况更差
  use-sso-address: true

heartbeat:
  disabled: true # 是否开启心跳事件上报
  # 心跳频率, 单位秒
  # -1 为关闭心跳
  interval: 5

message:
  # 上报数据类型
  # 可选: string,array
  post-format: array
  # 是否忽略无效的CQ码, 如果为假将原样发送
  ignore-invalid-cqcode: false
  # 是否强制分片发送消息
  # 分片发送将会带来更快的速度
  # 但是兼容性会有些问题
  force-fragment: false
  # 是否将url分片发送
  fix-url: false
  # 下载图片等请求网络代理
  proxy-rewrite: ''
  # 是否上报自身消息
  report-self-message: true
  # 移除服务端的Reply附带的At
  remove-reply-at: false
  # 为Reply附加更多信息
  extra-reply-data: false

output:
  # 日志等级 trace,debug,info,warn,error
  log-level: info
  # 是否启用 DEBUG
  debug: false # 开启调试模式

# 默认中间件锚点
default-middlewares: &default
  # 访问密钥, 强烈推荐在公网的服务器设置
  access-token: ''
  # 事件过滤器文件目录
  filter: ''
  # API限速设置
  # 该设置为全局生效
  # 原 cqhttp 虽然启用了 rate_limit 后缀, 但是基本没插件适配
  # 目前该限速设置为令牌桶算法, 请参考:
  # https://baike.baidu.com/item/%E4%BB%A4%E7%89%8C%E6%A1%B6%E7%AE%97%E6%B3%95/6597000?fr=aladdin
  rate-limit:
    enabled: false # 是否启用限速
    frequency: 1  # 令牌回复频率, 单位秒
    bucket: 1     # 令牌桶大小

servers:
  # HTTP 通信设置
  - http:
      # 是否关闭正向HTTP服务器
      disabled: true
      # 服务端监听地址
      host: 127.0.0.1
      # 服务端监听端口
      port: 5700
      # 反向HTTP超时时间, 单位秒
      # 最小值为5，小于5将会忽略本项设置
      timeout: 5
      middlewares:
        <<: *default # 引用默认中间件
      # 反向HTTP POST地址列表
      post:
      #- url: '' # 地址
      #  secret: ''           # 密钥
      #- url: 127.0.0.1:5701 # 地址
      #  secret: ''          # 密钥

  # 正向WS设置
  - ws:
      # 是否禁用正向WS服务器
      disabled: true
      # 正向WS服务器监听地址
      host: 127.0.0.1
      # 正向WS服务器监听端口
      port: 6700
      middlewares:
        <<: *default # 引用默认中间件

  - ws-reverse:
      # 是否禁用当前反向WS服务
      disabled: false
      # 反向WS Universal 地址
      # 注意 设置了此项地址后下面两项将会被忽略
      universal: ws://127.0.0.1:4000/cqhttp/ws/
      # 反向WS API 地址
      api: 
      # 反向WS Event 地址
      event: 
      # 重连间隔 单位毫秒
      reconnect-interval: 3000
      middlewares:
        <<: *default # 引用默认中间件
  # pprof 性能分析服务器, 一般情况下不需要启用.
  # 如果遇到性能问题请上传报告给开发者处理
  # 注意: pprof服务不支持中间件、不支持鉴权. 请不要开放到公网
  - pprof:
      # 是否禁用pprof性能分析服务器
      disabled: true
      # pprof服务器监听地址
      host: 127.0.0.1
      # pprof服务器监听端口
      port: 7700

  # 可添加更多
  #- ws-reverse:
  #- ws:
  #- http:
  #- pprof:

database: # 数据库相关设置
  leveldb:
    # 是否启用内置leveldb数据库
    # 启用将会增加10-20MB的内存占用和一定的磁盘空间
    # 关闭将无法使用 撤回 回复 get_msg 等上下文相关功能
    enable: true
```

再次运行 go-cqhttp

### 配置 nonebot2

```shell
nb run
```

## 快速开始（Linux）

**目前由于诸多原因，不推荐使用 Docker 部署。如需 Docker 部署请自行尝试，恕不提供技术支持。**