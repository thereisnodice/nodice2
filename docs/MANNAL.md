# 部署指南

**poetry 导致的 nonebot2 版本问题**

如果你是使用 poerty 管理机器人的话（如果你是按照部署指南来部署的话那就肯定是），请自行进入虚拟环境使 nonebot2 与 nonebot-adapter-cqhttp 处于较为稳定的版本搭配。

以下是两种较为稳定的版本搭配：

```
nonebot2==2.0.0a11
nonebot-adapter-cqhttp==2.0.0a11.post2
```

或

```
nonebot2==2.0.0a13.post1
nonebot-adapter-cqhttp==2.0.0a12
```

### 快速开始 (Windows)

确保你已经下载并安装了 [Git](https://git-scm.com/) 和 [Python](https://www.python.org/).

为了压缩仓库大小，本项目不再内置 go-cqhttp，请自行下载 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp/releases)

现在，在你想要安装 NoDice 的目录打开 `Git bash`，逐条执行以下命令。

```
git clone git@github.com:thereisnodice/nodice2.git
cd nodice2/nodice/
poetry install
```

接着，在 nodice2 目录创建 `go-cqhttp` 文件夹（当然你也可以把 go-cqhttp 文件夹放到其他地方，只是放在一起更方便管理）并将之前下载好的 go-cqhttp 复制到该目录下。

#### 配置go-cqhttp

运行一次 go-cqhttp ，此时目录下会出现 `config.hjson` 文件，按如下修改配置。

```json
{
    // QQ号
    uin: 0
    // QQ密码
    password: ""
    // 是否启用密码加密
    encrypt_password: false
    // 加密后的密码, 如未启用密码加密将为空, 请勿随意修改.
    password_encrypted: ""
    // 是否启用内置数据库
    // 启用将会增加10-20MB的内存占用和一定的磁盘空间
    // 关闭将无法使用 撤回 回复 get_msg 等上下文相关功能
    enable_db: false
    // 访问密钥, 强烈推荐在公网的服务器设置
    access_token: ""
    // 重连设置
    relogin: {
        // 是否启用自动重连
        // 如不启用掉线后将不会自动重连
        enabled: true
        // 重连延迟, 单位秒
        relogin_delay: 3
        // 最大重连次数, 0为无限制
        max_relogin_times: 0
    }
    // API限速设置
    // 该设置为全局生效
    // 原 cqhttp 虽然启用了 rate_limit 后缀, 但是基本没插件适配
    // 目前该限速设置为令牌桶算法, 请参考: 
    // https://baike.baidu.com/item/%E4%BB%A4%E7%89%8C%E6%A1%B6%E7%AE%97%E6%B3%95/6597000?fr=aladdin
    _rate_limit: {
        // 是否启用限速
        enabled: false
        // 令牌回复频率, 单位秒
        frequency: 1
        // 令牌桶大小
        bucket_size: 1
    }
    // 是否忽略无效的CQ码
    // 如果为假将原样发送
    ignore_invalid_cqcode: false
    // 是否强制分片发送消息
    // 分片发送将会带来更快的速度
    // 但是兼容性会有些问题
    force_fragmented: false
    // 心跳频率, 单位秒
    // -1 为关闭心跳
    heartbeat_interval: 0
    // HTTP设置
    http_config: {
        // 是否启用正向HTTP服务器
        enabled: false
        // 服务端监听地址
        host: 0.0.0.0
        // 服务端监听端口
        port: 5700
        // 反向HTTP超时时间, 单位秒
        // 最小值为5，小于5将会忽略本项设置
        timeout: 0
        // 反向HTTP POST地址列表
        // 格式: 
        // {
        //    地址: secret
        // }
        post_urls: {}
    }
    // 正向WS设置
    ws_config: {
        // 是否启用正向WS服务器
        enabled: false
        // 正向WS服务器监听地址
        host: 0.0.0.0
        // 正向WS服务器监听端口
        port: 6700
    }
    // 反向WS设置
    ws_reverse_servers: [
        // 可以添加多个反向WS推送
        {
            // 是否启用该推送
            enabled: true
            // 反向WS Universal 地址
            // 注意 设置了此项地址后下面两项将会被忽略
            // 留空请使用 ""
            reverse_url: ws://127.0.0.1:4000/cqhttp/ws/
            // 反向WS API 地址
            reverse_api_url:
            // 反向WS Event 地址
            reverse_event_url:
            // 重连间隔 单位毫秒
            reverse_reconnect_interval: 3000
        }
    ]
    // 上报数据类型
    // 可选: string array
    post_message_format: array
    // 是否使用服务器下发的新地址进行重连
    // 注意, 此设置可能导致在海外服务器上连接情况更差
    use_sso_address: false
    // 是否启用 DEBUG
    debug: false
    // 日志等级 trace,debug,info,warn,error
    log_level: "info"
    // WebUi 设置
    web_ui: {
        // 是否启用 WebUi
        enabled: false
        // 监听地址
        host: 127.0.0.1
        // 监听端口
        web_ui_port: 9999
        // 是否接收来自web的输入
        web_input: false
    }
}
```

再次运行 go-cqhttp

#### 配置 nonebot2

```
nb run
```

### 快速开始（Linux）

**目前由于诸多原因，不推荐使用 Docker 部署。如需 Docker 部署请自行尝试，恕不提供技术支持。**