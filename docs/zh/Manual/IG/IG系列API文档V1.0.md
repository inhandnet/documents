# IG系列API文档V1.0

## API使用说明

- IG系列产品提供了一套HTTP API可以进行网络管理和系统管理，用户可以使用curl、Postman等工具或使用代码构建发送HTTP请求管理设备
- API使用了HTTPS协议，因为使用了自签名证书，客户端不需要校验证书，不校验证书的方法如下：
  - curl命令加上`-k`参数
  - Postman需要关闭`SSL certificate verification`

![1742178463272-bac06fda-8921-4a71-ae8f-8f1f0bd8dab5.png](./img/tBKzVoMxyovpxRsO/1742178463272-bac06fda-8921-4a71-ae8f-8f1f0bd8dab5-366639.webp)

```
- HTTP API端口固定为443，使用时URL需要带上前缀：https://<IP>或https://<IP>:443
- 在Linux系统下，你可以使用curl命令来调用API，有关更多curl命令的使用方法：[https://curl.se/docs/](https://curl.se/docs/)
- 在Windows系统下，你可以使用Postman软件来调用API，Postman使用文档：
```

<https://learning.postman.com/docs/introduction/overview/>

## 获取鉴权

调用HTTP相关的API接口需要获取Authorization token，获取的方法是对用户名密码以username:password的形式进行base64编码，获取初始的token，然后用这个token调用登录接口获取最终的Authorization token.

```http
POST /v1/user/login
```

**请求示例**

令牌YWRtOjEyMzQ1Ng==是对默认用户名密码以adm:123456格式进行base64编码获得的.

```json
Authorization: Basic YWRtOjEyMzQ1Ng==
```

**返回信息**

```json
{
    "results": {
        "name": "adm",
        "priv": 15,
        "from": "10.5.30.215",
        "web_session": "HryznYzqVlLkOerl0RXeeoAh0vmcPPpn",
        "first_login": 0
    }
}
```

**参数说明**

| \*\*            参数名称\*\* | \*\*            参数描述\*\* | \*\*            参数类型\*\* | \*\*              取值范围\*\* |
| --- | --- | --- | --- |
| web\_session |  | 字符串 | |

**返回示例**

```json
{
    "results": {
        "name": "adm",
        "priv": 15,
        "from": "10.5.30.215",
        "web_session": "9vh4d7NVeYxEm318VMleC6PHIvNQNCZL",
        "first_login": 0
    }
}
```

## 网络接口

### 蜂窝网

#### 更新配置

接口

```http
PUT v1/cellular/config?autosave=1
```

负载

```json
{
    "enable": 1,
    "enable_dual_sim": 0,
    "main_sim": 1,
    "max_dial_times": 3,
    "min_dial_times": 0,
    "backup_sim_timeout": 0,
    "network_type": 0,
    "sim1_profile": 1,
    "sim2_profile": 0,
    "sim1_roaming": 1,
    "sim2_roaming": 1,
    "sim1_pincode": "",
    "sim2_pincode": "",
    "sim1_csq_threshold": 0,
    "sim2_csq_threshold": 0,
    "sim1_csq_detect_interval": 0,
    "sim2_csq_detect_interval": 0,
    "sim1_csq_detect_retries": 0,
    "sim2_csq_detect_retries": 0,
    "static_ip": 0,
    "ip_addr": "",
    "peer_addr": "",
    "connect_mode": 0,
    "trig_data": 1,
    "trig_sms": 0,
    "max_idle_time": 60,
    "radial_interval": 10,
    "init_command": "",
    "rssi_poll_interval": 120,
    "dial_timeout": 120,
    "mtu": 1500,
    "mru": 1500,
    "use_default_asyncmap": 0,
    "use_peer_dns": 1,
    "lcp_interval": 55,
    "lcp_max_retries": 5,
    "infinitely_dial_retry": 0,
    "debug": 0,
    "expert_options": "",
    "dial_time_on_sim2": 0,
    "pdp_type": 2,
    "sms": {
        "enable": 0,
        "mode": 1,
        "enable_reply": 0,
        "interval": 30,
        "phone_num_white_lists": [

        ]
    },
    "profile": [
        {
            "index": "default",
            "network_type": 1,
            "apn": "",
            "access_number": "",
            "auth_method": 0,
            "username": "",
            "password": ""
        },
        {
            "index": 1,
            "network_type": 1,
            "apn": "3gnet",
            "access_number": "*99***1#",
            "auth_method": 2,
            "username": "gprs",
            "password": "gprs"
        }
    ]
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | 拨号使能开关，0关闭，1开启 |
| enable\_dual\_sim | integer | \[0, 1] | 双卡使能开关，0关闭，1开启 |
| main\_sim | integer | \[1, 2] | 主sim卡，1表示sim1，2表示sim2 |
| max\_dial\_times | integer | \[1, 10] | 在某张sim卡拨号失败达到设置的次数后，切换sim卡 |
| min\_dial\_times | integer | 0 | 历史遗留字段，固定为0 |
| backup\_sim\_timeout | integer | \[0, 8640000]s | 工作在备卡上的时间，当时间到达后切回主卡，单位秒。 |
| network\_type | integer | \[0, 7] | 0：自动<br/>1：2G<br/>2：3G<br/>3：4G<br/>6：5G<br/>7：4G5G<br/>不同的型号的设置支持的网络制式存在差异 |
| sim1\_profile | integer | \[0, 10] | sim1卡的拨号参数及。0表示默认的拨号参数集<br/>1~10对应profile数组中的index值 |
| sim2\_profile | integer | \[0, 10] | sim2卡的拨号参数及。0表示默认的拨号参数集<br/>1~10对应profile数组中的index值 |
| sim1\_roaming | integer | \[0, 1] | sim1卡是否开启漫游，0关闭，1开启 |
| sim2\_roaming | integer | \[0, 1] | sim2卡是否开启漫游，0关闭，1开启 |
| sim1\_pincode | string | \[1, 6]字符 | sim1卡的pincode |
| sim2\_pincode | string | \[1, 6]字符 | sim2卡的pincode |
| sim1\_csq\_threshold | integer | 0 | 历史遗留字段，固定为0 |
| sim2\_csq\_threshold | integer | 0 | 历史遗留字段，固定为0 |
| sim1\_csq\_detect\_interval | integer | 0 | 历史遗留字段，固定为0 |
| sim2\_csq\_detect\_interval | integer | 0 | 历史遗留字段，固定为0 |
| sim1\_csq\_detect\_retries | integer | 0 | 历史遗留字段，固定为0 |
| sim2\_csq\_detect\_retries | integer | 0 | 历史遗留字段，固定为0 |
| static\_ip | integer | \[0, 1] | 是否启用静态ip，0关闭，1启用，只有ppp拨号的模组才支持这个配置 |
| ip\_addr | string | \[1, 16]字符 | 启用静态ip时本端ip地址 |
| peer\_addr | string | \[1, 16]字符 | 启用静态ip时对端ip地址 |
| connect\_mode | integer | 0 | 历史遗留字段，固定为0 |
| trig\_data | integer | 1 | 历史遗留字段，固定为1 |
| trig\_sms | integer | 0 | 历史遗留字段，固定为0 |
| max\_idle\_time | integer | 60 | 历史遗留字段，固定为60 |
| radial\_interval | integer | \[1, 3600]s | 拨号失败后会重新拨号，但重拨之前会等待一段时间，这里设置的是等待时间。 |
| init\_command | string | \[1, 32]字符 | 初始化命令 |
| rssi\_poll\_interval | integer | \[1, 3600]s | 信号检测间隔 |
| dial\_timeout | integer | \[10, 3600]s | 拨号超时时间 |
| mtu | integer | \[128, 1500] | 拨号接口的MTU值 |
| mru | integer | \[128, 1500] | 拨号接口的MRU值 |
| use\_default\_asyncmap | integer | 0 | 历史遗留字段，固定为0 |
| use\_peer\_dns | integer | \[0, 1] | 是否使用拨号分配的DNS，0不使用，1使用 |
| infinitely\_dial\_retry | integer | \[0, 1] | 是否开启无限重拨，开启后，无论拨号失败多少次，系统都不会重启；关闭后，当拨号失败达到一定次数后，会自动重启系统。 |
| debug | integer | \[0, 1] | 是否开启调试日志，0关闭，1开启 |
| expert\_options | string | \[1, 32]字符 | 专家选项 |
| pdp\_type | integer | \[0, 2] | 0: IPV4<br/>1: IPV6<br/>2: IPV4V6 |
| sms.enable | integer | \[0, 1] | 是否开启短信功能，0关闭，1开启 |
| sms.mode | integer | 1 | 短信模式，固定为1，表示text格式的短信 |
| sms.enable\_reply | integer | \[0, 1] | 通过短信配置网关后，是否通过短信回复配置结果，0不回复，1回复。 |
| sms.interval | integer |  | 处理短信的周期 |
| sms.phone\_num\_white\_lists | array | 最多10个成员 | 手机号白名单，只有在白名单中的手机号发送的短信，程序才会处理。 |
|  |  |  |  |

#### 查询配置

接口

```http
GET v1/cellular/config
```

响应

```json
{
    "results": {
        "enable": 0,
        "enable_dual_sim": 1,
        "main_sim": 1,
        "max_dial_times": 2,
        "min_dial_times": 300,
        "backup_sim_timeout": 0,
        "dial_time_on_sim2": 0,
        "network_type": 0,
        "pdp_type": 0,
        "sim1_profile": 0,
        "sim1_roaming": 1,
        "sim1_pincode": "",
        "sim2_profile": 0,
        "sim2_roaming": 1,
        "sim2_pincode": "",
        "sim1_csq_threshold": 0,
        "sim2_csq_threshold": 0,
        "sim1_csq_detect_interval": 0,
        "sim2_csq_detect_interval": 0,
        "sim1_csq_detect_retries": 0,
        "sim2_csq_detect_retries": 0,
        "static_ip": 0,
        "connect_mode": 0,
        "radial_interval": 10,
        "sms": {
            "enable": 0,
            "mode": 1,
            "enable_reply": 0,
            "interval": 30,
            "phone_num_white_lists": []
        },
        "profile": [
            {
                "index": 1,
                "network_type": 1,
                "apn": "3gnet",
                "access_number": "*99***1#",
                "auth_method": 0,
                "username": "gprs",
                "password": "gprs"
            }
        ],
        "init_command": "",
        "rssi_poll_interval": 120,
        "dial_timeout": 120,
        "mtu": 1500,
        "mru": 1500,
        "use_default_asyncmap": 0,
        "use_peer_dns": 1,
        "lcp_interval": 55,
        "lcp_max_retries": 5,
        "infinitely_dial_retry": 0,
        "debug": 0,
        "expert_options": ""
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | 拨号使能开关，0关闭，1开启 |
| enable\_dual\_sim | integer | \[0, 1] | 双卡使能开关，0关闭，1开启 |
| main\_sim | integer | \[1, 2] | 主sim卡，1表示sim1，2表示sim2 |
| max\_dial\_times | integer | \[1, 10] | 在某张sim卡拨号失败达到设置的次数后，切换sim卡 |
| min\_dial\_times | integer | 0 | 历史遗留字段，固定为0 |
| backup\_sim\_timeout | integer | \[0, 8640000]s | 工作在备卡上的时间，当时间到达后切回主卡，单位秒。 |
| network\_type | integer | \[0, 7] | 0：自动<br/>1：2G<br/>2：3G<br/>3：4G<br/>6：5G<br/>7：4G5G<br/>不同的型号的设置支持的网络制式存在差异 |
| sim1\_profile | integer | \[0, 10] | sim1卡的拨号参数及。0表示默认的拨号参数集<br/>1~10对应profile数组中的index值 |
| sim2\_profile | integer | \[0, 10] | sim2卡的拨号参数及。0表示默认的拨号参数集<br/>1~10对应profile数组中的index值 |
| sim1\_roaming | integer | \[0, 1] | sim1卡是否开启漫游，0关闭，1开启 |
| sim2\_roaming | integer | \[0, 1] | sim2卡是否开启漫游，0关闭，1开启 |
| sim1\_pincode | string | \[1, 6]字符 | sim1卡的pincode |
| sim2\_pincode | string | \[1, 6]字符 | sim2卡的pincode |
| sim1\_csq\_threshold | integer | 0 | 历史遗留字段，固定为0 |
| sim2\_csq\_threshold | integer | 0 | 历史遗留字段，固定为0 |
| sim1\_csq\_detect\_interval | integer | 0 | 历史遗留字段，固定为0 |
| sim2\_csq\_detect\_interval | integer | 0 | 历史遗留字段，固定为0 |
| sim1\_csq\_detect\_retries | integer | 0 | 历史遗留字段，固定为0 |
| sim2\_csq\_detect\_retries | integer | 0 | 历史遗留字段，固定为0 |
| static\_ip | integer | \[0, 1] | 是否启用静态ip，0关闭，1启用，只有ppp拨号的模组才支持这个配置 |
| ip\_addr | string | \[1, 16]字符 | 启用静态ip时本端ip地址 |
| peer\_addr | string | \[1, 16]字符 | 启用静态ip时对端ip地址 |
| connect\_mode | integer | 0 | 历史遗留字段，固定为0 |
| trig\_data | integer | 1 | 历史遗留字段，固定为1 |
| trig\_sms | integer | 0 | 历史遗留字段，固定为0 |
| max\_idle\_time | integer | 60 | 历史遗留字段，固定为60 |
| radial\_interval | integer | \[1, 3600]s | 拨号失败后会重新拨号，但重拨之前会等待一段时间，这里设置的是等待时间。 |
| init\_command | string | \[1, 32]字符 | 初始化命令 |
| rssi\_poll\_interval | integer | \[1, 3600]s | 信号检测间隔 |
| dial\_timeout | integer | \[10, 3600]s | 拨号超时时间 |
| mtu | integer | \[128, 1500] | 拨号接口的MTU值 |
| mru | integer | \[128, 1500] | 拨号接口的MRU值 |
| use\_default\_asyncmap | integer | 0 | 历史遗留字段，固定为0 |
| use\_peer\_dns | integer | \[0, 1] | 是否使用拨号分配的DNS，0不使用，1使用 |
| infinitely\_dial\_retry | integer | \[0, 1] | 是否开启无限重拨，开启后，无论拨号失败多少次，系统都不会重启；关闭后，当拨号失败达到一定次数后，会自动重启系统。 |
| debug | integer | \[0, 1] | 是否开启调试日志，0关闭，1开启 |
| expert\_options | string | \[1, 32]字符 | 专家选项 |
| pdp\_type | integer | \[0, 2] | 0: IPV4<br/>1: IPV6<br/>2: IPV4V6 |
| sms.enable | integer | \[0, 1] | 是否开启短信功能，0关闭，1开启 |
| sms.mode | integer | 1 | 短信模式，固定为1，表示text格式的短信 |
| sms.enable\_reply | integer | \[0, 1] | 通过短信配置网关后，是否通过短信回复配置结果，0不回复，1回复。 |
| sms.interval | integer |  | 处理短信的周期 |
| sms.phone\_num\_white\_lists | array | 最多10个成员 | 手机号白名单，只有在白名单中的手机号发送的短信，程序才会处理。 |
|  |  |  |  |

#### 查询状态

##### 模组状态

接口

```http
GET v1/cellular/modem/status
```

响应

```json
{
    "results": {
        "active_sim": "SIM 1",
        "imei_code": "865847055239576",
        "imsi_code": "460026001115905",
        "iccid_code": "898600F0221109E25905",
        "phone_number": "",
        "signal_level": 17,
        "dbm": 79,
        "rerp": 0,
        "rerq": 0,
        "register_status": 1,
        "operator": "China Mobile",
        "mcc_mnc": 46000,
        "apns": "",
        "network_type": "4G",
        "lac": "8005",
        "cell_id": "8006700",
        "arfcn": 0,
        "sinr": "",
        "pci": 0,
        "network_submode": "LTE",
        "model_temp": 0
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| active\_sim | string | \[1, 16]字符 | 当前使用的sim卡 |
| imei\_code | string | \[1, 16]字符 | 蜂窝模组的IEMI信息 |
| imsi\_code | string | \[1, 16]字符 | SIM卡的IMSI信息 |
| iccid\_code | string | \[1, 32]字符 | SIM卡的ICCID信息 |
| phone\_number | string | \[1, 16]字符 | 手机号 |
| signal\_level | integer | \[0, 31] | 信号质量 |
| rerp | integer |  | RERP |
| rerq | integer |  | RERQ |
| register\_status | integer | \[0, 7] | 连接状态：<br/>0： 正在注册到网络  <br/>1： 注册网络成功<br/>2： 正在注册到网络  <br/>3： 注册网络被拒绝<br/>4： 注册网络失败，原因未知  <br/>5： 注册网络失败，原因未知  <br/>6： 尚未注册到网络 <br/>7： 关闭拨号，此时不显示注册状态      |
| operator | string | \[1, 16]字符 | 运营商 |
| mcc\_mnc | integer |  | PLMN |
| apns | string | \[1, 16]字符 | APN信息 |
| network\_type | string | \[1, 16]字符 | 网络类型 |
| lac | string | \[1, 16]字符 | 位置区码 |
| cell\_id | string | \[1, 16]字符 | 小区ID |

##### 连接状态

接口

```http
GET v1/cellular/network/status
```

响应

```json
{
    "results": [
        {
            "status": 1,
            "ip_addr": "10.148.48.144",
            "netmask": "255.255.255.255",
            "gateway": "10.148.48.145",
            "dns": "223.87.253.100 223.87.253.253",
            "mtu": 1500,
            "connect_time": 2
        }
    ]
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| status | integer | \[0, 1] | 0：未连接；1：已连接 |
| ip\_addr | string | \[1, 16]字符 | 蜂窝接口IP地址 |
| netmask | string | \[1, 16]字符 | 蜂窝接口子网掩码 |
| gateway | string | \[1, 16]字符 | 网关 |
| mtu | integer | \[68, 1500] | 接口MTU值 |
| dns | string | \[1, 32] | dns信息 |
| connect\_time | integer |  | 蜂窝接口连接时长 |

### WAN口

#### 更新配置

接口

```http
PUT v1/eth/config?autosave=1
```

负载

```json
{
    "iface_name": "fastethernet 0/1",
    "internet": 0,
    "primary_ip": "10.5.30.213",
    "netmask": "255.255.255.0",
    "mtu": 1500,
    "speed_duplex": 0,
    "track_l2_state": 1,
    "shutdown": 0,
    "description": "",
    "multi_ip": [
        {
            "secondary_ip": "192.168.6.2",
            "netmask": "255.255.255.0"
        }
    ]
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| iface\_name | string | \[1, 16]字符 | 接口名称 |
| internet | integer | \[0, 1] | 0：接口配置为静态IP<br/>1：接口配置为DHCP获取地址 |
| primary\_ip | string | \[1, 16]字符 | 接口IP地址 |
| netmask | string | \[1, 16]字符 | 接口子网掩码 |
| mtu | integer | \[68, 1500] | 接口MTU值 |
| track\_l2\_state | integer | \[0, 1] | 二层状态联动开关；0关闭，1开启 |
| shutdown | integer | \[0, 1] | 接口状态开关；0开启，1关闭 |
| description | string | \[0, 32]字符 | 接口描述信息 |
| multi\_ip | object | | 接口从IP信息 |

#### 查询配置

接口

```http
GET v1/eth/config?iface=eth1
```

响应

```json
{
    "results": {
        "iface_name": "fastethernet 0/1",
        "internet": 0,
        "primary_ip": "10.5.30.213",
        "netmask": "255.255.255.0",
        "mtu": 1500,
        "speed_duplex": 0,
        "track_l2_state": 1,
        "shutdown": 0,
        "description": "test",
        "multi_ip": []
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| iface\_name | string | \[1, 16]字符 | 接口名称 |
| internet | integer | \[0, 1] | 0：接口配置为静态IP<br/>1：接口配置为DHCP获取地址 |
| primary\_ip | string | \[1, 16]字符 | 接口IP地址 |
| netmask | string | \[1, 16]字符 | 接口子网掩码 |
| mtu | integer | \[68, 1500] | 接口MTU值 |
| track\_l2\_state | integer | \[0, 1] | 二层状态联动开关；0关闭，1开启 |
| shutdown | integer | \[0, 1] | 接口状态开关；0开启，1关闭 |
| description | string | \[0, 32]字符 | 接口描述信息 |
| multi\_ip | object | | 接口从IP信息 |

#### 查询状态

接口

```http
GET v1/eth/status?iface=eth1
```

响应

```json
{
    "results": {
        "iface_name": "fastethernet 0/1",
        "connect_type": 0,
        "ip_addr": "10.5.30.213",
        "netmask": "255.255.255.0",
        "gateway": "0.0.0.0",
        "dns": "0.0.0.0 ",
        "mtu": 1500,
        "status": 1,
        "connect_time": 70629,
        "remaining_lease": 0,
        "description": "test"
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| iface\_name | string | \[1, 16]字符 | 接口名称 |
| connect\_type | integer | \[0, 1] | 0：接口配置为静态IP<br/>1：接口配置为DHCP获取地址 |
| ip\_addr | string | \[1, 16]字符 | 接口IP地址 |
| netmask | string | \[1, 16]字符 | 接口子网掩码 |
| mtu | integer | \[68, 1500] | 接口MTU值 |
| gateway | string | \[1, 16]字符 | 网关的IP地址 |
| status | integer | \[0, 1] | 接口状态；0表示接口down，1表示接口up |
| dns | string | \[0, 32]字符 | dns信息 |
| connect\_time | integer | \[1, n] | 接口up的时长 |
| remaining\_lease | integer | \[0, 10080] | 接口通过DHCP获取地址时的剩余租期，单位是分钟。 |

### LAN口

#### 更新配置

接口

```http
PUT v1/bridge/config?autosave=1&brid=1
```

负载

```json
{
    "iface_name": "bridge 1",
    "primary_ip": "192.168.2.1",
    "netmask": "255.255.255.0",
    "shutdown": false,
    "description": "lan_interface",
    "bridge_ifaces": [
        "fastethernet 0/2"
    ],
    "multi_ip": [
        {
            "secondary_ip": "192.168.7.100",
            "netmask": "255.255.255.0"
        }
    ]
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| iface\_name | string | \[1, 16]字符 | 接口名称 |
| primary\_ip | string | \[1, 16]字符 | 接口IP地址 |
| netmask | string | \[1, 16]字符 | 接口子网掩码 |
| shutdown | bool | true/false | 接口状态开关；false开启，true关闭 |
| bridge\_interfaces | array |  | LAN是一个桥接口，这里列出桥接口包含了哪些物理接口。 |
| description | string | \[0, 32]字符 | 接口描述信息 |
| multi\_ip | object | | 接口从IP信息 |

#### 查询配置

接口

```http
GET v1/bridge/config?brid=1
```

响应

```json
{
    "results": {
        "iface_name": "bridge 1",
        "primary_ip": "192.168.2.1",
        "netmask": "255.255.255.0",
        "shutdown": 0,
        "description": "lan_interface",
        "bridge_ifaces": [
            "fastethernet 0/2"
        ],
        "multi_ip": [
            {
                "secondary_ip": "192.168.7.100",
                "netmask": "255.255.255.0"
            }
        ]
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| iface\_name | string | \[1, 16]字符 | 接口名称 |
| primary\_ip | string | \[1, 16]字符 | 接口IP地址 |
| netmask | string | \[1, 16]字符 | 接口子网掩码 |
| shutdown | bool | true/false | 接口状态开关；false开启，true关闭 |
| bridge\_interfaces | array |  | LAN是一个桥接口，这里列出桥接口包含了哪些物理接口。 |
| description | string | \[0, 32]字符 | 接口描述信息 |
| multi\_ip | object | | 接口从IP信息 |

#### 查询状态

接口

```http
v1/bridge/status?brid=1
```

响应

```json
{
    "results": {
        "iface_name": "bridge 1",
        "connect_type": 0,
        "ip_addr": "192.168.2.1",
        "netmask": "255.255.255.0",
        "gateway": "0.0.0.0",
        "dns": "0.0.0.0 ",
        "mtu": 1500,
        "status": 1,
        "connect_time": 338203,
        "remaining_lease": 0,
        "description": "lan_interface"
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| iface\_name | string | \[1, 16]字符 | 接口名称 |
| connect\_type | integer | \[0, 1] | 0：接口配置为静态IP<br/>1：接口配置为DHCP获取地址 |
| ip\_addr | string | \[1, 16]字符 | 接口IP地址 |
| netmask | string | \[1, 16]字符 | 接口子网掩码 |
| mtu | integer | \[68, 1500] | 接口MTU值 |
| gateway | string | \[1, 16]字符 | 网关的IP地址 |
| dns | string | \[0, 32]字符 | dns信息 |
| connect\_time | integer | \[1, n] | 接口up的时长 |
| description | string | \[0, 32]字符 | 接口描述信息 |
| status | integer | \[0, 1] | 接口状态；0表示接口down，1表示接口up |
| remaining\_lease | integer | \[0, 10080] | 接口通过DHCP获取地址时的剩余租期，单位是分钟。 |

### WLAN

#### 更新Station配置

接口

```http
PUT v1/dot11radio/config?autosave=1
```

负载

```json
{
    "enable": 1,
    "iface": "dot11radio1",
    "station_role": 1,
    "ap_ssid_broadcast": 1,
    "ap_ssid": "InEdgeGateway",
    "auth_method": 0,
    "wpa_psk_key": "",
    "ap_max_associations": 0,
    "ap_wpa_group_rekey": 3600,
    "ap_isolate": 0,
    "ap_band": 0,
    "ap_radio_type": 7,
    "ap_channel": 11,
    "encrypt_mode": 0,
    "wep_key": "",
    "ap_radius_ip": "",
    "ap_radius_port": 1812,
    "ap_radius_key": "",
    "ap_radius_srcif": "",
    "ap_bandwidth": 0,
    "sta_default_route": 1,
    "sta_ssid": "0x696E68616E642D76697369746F72",
    "sta_auth_method": 5,
    "sta_encrypt_mode": 4,
    "sta_wpa_psk_key": "inhand@visitor",
    "sta_wep_key": "",
    "sta_auth_mode": 0,
    "sta_inner_auth": 0,
    "sta_username": "",
    "sta_password": "",
    "sta_dhcp": 1,
    "ip_addr": "",
    "netmask": ""，
    "sta_auth_mode": 1,
    "sta_inner_auth": 1,
    "sta_username": "hello",
    "sta_password": "abcd123456",
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | WLAN开关，0关闭，1开启 |
| station\_role   | integer | \[0, 1] | Wi-Fi工作模式<br/>0：AP<br/>1：Station |
| ap\_ssid | string | \[1, 32]字符 | AP模式时的ssid名称 |
| ap\_ssid\_broadcast | integer | \[0, 1] | SSID广播开关，0为关闭，1为开启 |
| auth\_method | integer | \[0, 8] | 认证方式<br/>0：无认证<br/>1：共享认证<br/>2：保留字段<br/>3：WPA-PSK  <br/>4： WPA <br/>5： WPA2-PSK  <br/>6： WPA2 <br/>7： WPA/WPA2 <br/>8： WPAPSK/WPA2PSK   |
| wpa\_psk\_key | string | \[8, 63]字符 |  WPA/WPA2 PSK 密钥， 认证方式为 WPA-PSK，WPA2-PSK，WPAPSK/WPA2PSK 时，该选项才有效  |
| ap\_max\_associations | integer | \[1, 128] | 客户端的最大数量 |
| ap\_wpa\_group\_rekey | integer | \[600, 86400] | 组密码协商时间 |
| ap\_isolate | integer | \[0, 1] | AP隔离开关，0关闭，1开启 |
| ap\_band | integer | \[0, 1] | 无线频段，0为2.4G，1为5G |
| ap\_radio\_type | integer | 0: 802.11b/g, <br/>1: 802.11b, <br/>2: 802.11a, <br/>4: 802.11g, <br/>6: 802.11n, <br/>7: 802.11g/n, <br/>8: 802.11an/ac,<br/>9: 802.11b/g/n , <br/>11: 802.11na   |  无线频段为 2.4G 时，该下拉选项有：0, 1, 4, 6, 7, 9；无线频段为 5G 时，该下拉选项有：2, 8, 11    |
|  ap\_channel | integer | \[1, 11] | 信道 |
| encrypt\_mode | integer | \[0, 4] | 加密方式<br/>0：不加密<br/>1： WEP40 <br/>2： WEP104  <br/>3： TKIP <br/>4:    AES |
| wep\_key | string | \[0, 16]字符 | 网络密钥 |
| ap\_radius\_ip | string | \[1, 16]字符 | radius服务器的IP地址 |
| ap\_radius\_port | integer | \[1, 65535] | radius服务器的端口号 |
| ap\_radius\_key | string | \[1, 32]字符 | radius服务器的共享密钥 |
| ap\_radius\_srcif | string | \[1, 16]字符 | 与radius服务器连接的接口名称 |
| ap\_bandwidth | integer | 0，1，3 | 无线频宽<br/>0：20MHZ<br/>1：40MHz<br/>3：80MHz |
| sta\_default\_route | integer | \[0, 1] | 模式为station的时候时候添加基于WLAN的默认路由，0不添加，1添加 |
| sta\_ssid | string | \[1, 64]字符 | 模式为station时要连接的ssid名称 |
| sta\_auth\_method | integer | \[0, 6] | 认证方式<br/>0: 无认证<br/>1: 共享式认证<br/>2: 保留未使用<br/>3: WPA-PSK认证<br/>4: WPA认证<br/>5: WPA2-PSK认证<br/>6: WPA2认证 |
| sta\_auth\_mode | integer | 1 | 认证模式(WPA/WPA2模式时需要配置)<br/>1: EAP-PEAP |
| sta\_inner\_auth | integer | \[1, 2] | 内部身份验证(WPA/WPA2模式时需要配置)<br/>1: mschapv2<br/>2: md5 |
| sta\_username | string |  | 用户名(WPA/WPA2模式时需要配置) |
| sta\_password | string |  | 密码(WPA/WPA2模式时需要配置) |
| sta\_dhcp | integer | \[0, 1] | 是否启用静态IP：<br/>0：使用静态IP<br/>1：不使用静态IP，使用DHCP获取IP地址 |
| ip\_addr | string | \[0, 16]字符 | 启用静态ip时，设置的静态IP地址 |
| netmask | string | \[0, 16]字符 | 启用静态ip时，设置的子网掩码 |

#### 查询Station配置

接口

```http
GET v1/dot11radio/config?iface=dot11radio1
```

响应

```json
{
    "results": {
        "enable": 1,
        "iface": "dot11radio1",
        "station_role": 1,
        "ap_ssid_broadcast": 1,
        "ap_ssid": "InEdgeGateway",
        "auth_method": 0,
        "wpa_psk_key": "",
        "ap_max_associations": 0,
        "ap_wpa_group_rekey": 3600,
        "ap_isolate": 0,
        "ap_band": 0,
        "ap_radio_type": 7,
        "ap_channel": 11,
        "encrypt_mode": 0,
        "wep_key": "",
        "ap_radius_ip": "",
        "ap_radius_port": 1812,
        "ap_radius_key": "",
        "ap_radius_srcif": "",
        "ap_bandwidth": 0,
        "sta_default_route": 1,
        "sta_ssid": "0x696E68616E642D76697369746F72",
        "sta_auth_method": 5,
        "sta_encrypt_mode": 4,
        "sta_wpa_psk_key": "inhand@visitor",
        "sta_wep_key": "",
        "sta_auth_mode": 0,
        "sta_inner_auth": 0,
        "sta_username": "",
        "sta_password": "",
        "sta_dhcp": 1,
        "ip_addr": "0.0.0.0",
        "netmask": "0.0.0.0"
    }
}
```

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | WLAN开关，0关闭，1开启 |
| station\_role   | integer | \[0, 1] | Wi-Fi工作模式<br/>0：AP<br/>1：Station |
| ap\_ssid | string | \[1, 32]字符 | AP模式时的ssid名称 |
| ap\_ssid\_broadcast | integer | \[0, 1] | SSID广播开关，0为关闭，1为开启 |
| auth\_method | integer | \[0, 8] | 认证方式<br/>0：无认证<br/>1：共享认证<br/>2：保留字段<br/>3：WPA-PSK  <br/>4： WPA <br/>5： WPA2-PSK  <br/>6： WPA2 <br/>7： WPA/WPA2 <br/>8： WPAPSK/WPA2PSK   |
| wpa\_psk\_key | string | \[8, 63]字符 |  WPA/WPA2 PSK 密钥， 认证方式为 WPA-PSK，WPA2-PSK，WPAPSK/WPA2PSK 时，该选项才有效  |
| ap\_max\_associations | integer | \[1, 128] | 客户端的最大数量 |
| ap\_wpa\_group\_rekey | integer | \[600, 86400] | 组密码协商时间 |
| ap\_isolate | integer | \[0, 1] | AP隔离开关，0关闭，1开启 |
| ap\_band | integer | \[0, 1] | 无线频段，0为2.4G，1为5G |
| ap\_radio\_type | integer | 0: 802.11b/g, <br/>1: 802.11b, <br/>2: 802.11a, <br/>4: 802.11g, <br/>6: 802.11n, <br/>7: 802.11g/n, <br/>8: 802.11an/ac,<br/>9: 802.11b/g/n , <br/>11: 802.11na   |  无线频段为 2.4G 时，该下拉选项有：0, 1, 4, 6, 7, 9；无线频段为 5G 时，该下拉选项有：2, 8, 11    |
|  ap\_channel | integer | \[1, 11] | 信道 |
| encrypt\_mode | integer | \[0, 4] | 加密方式<br/>0：不加密<br/>1： WEP40 <br/>2： WEP104  <br/>3： TKIP <br/>4:    AES |
| wep\_key | string | \[0, 16]字符 | 网络密钥 |
| ap\_radius\_ip | string | \[1, 16]字符 | radius服务器的IP地址 |
| ap\_radius\_port | integer | \[1, 65535] | radius服务器的端口号 |
| ap\_radius\_key | string | \[1, 32]字符 | radius服务器的共享密钥 |
| ap\_radius\_srcif | string | \[1, 16]字符 | 与radius服务器连接的接口名称 |
| ap\_bandwidth | integer | 0，1，3 | 无线频宽<br/>0：20MHZ<br/>1：40MHz<br/>3：80MHz |
| sta\_default\_route | integer | \[0, 1] | 模式为station的时候时候添加基于WLAN的默认路由，0不添加，1添加 |
| sta\_ssid | string | \[1, 64]字符 | 模式为station时要连接的ssid名称 |
| sta\_auth\_method | integer | \[0, 6] | 认证方式<br/>0: 无认证<br/>1: 共享式认证<br/>2: 保留未使用<br/>3: WPA-PSK认证<br/>4: WPA认证<br/>5: WPA2-PSK认证<br/>6: WPA2认证 |
| sta\_auth\_mode | integer | 1 | 认证模式(WPA/WPA2模式时需要配置)<br/>1: EAP-PEAP |
| sta\_inner\_auth | integer | \[1, 2] | 内部身份验证(WPA/WPA2模式时需要配置)<br/>1: mschapv2<br/>2: md5 |
| sta\_username | string |  | 用户名(WPA/WPA2模式时需要配置) |
| sta\_password | string |  | 密码(WPA/WPA2模式时需要配置) |
| sta\_dhcp | integer | \[0, 1] | 是否启用静态IP：<br/>0：使用静态IP<br/>1：不使用静态IP，使用DHCP获取IP地址 |
| ip\_addr | string | \[0, 16]字符 | 启用静态ip时，设置的静态IP地址 |
| netmask | string | \[0, 16]字符 | 启用静态ip时，设置的子网掩码 |

#### 查询Station状态

接口

```http
GET v1/dot11radio/status?iface=dot11radio1
```

响应

```json
{
    "results": {
        "station_role": 1,
        "status": 1,
        "mac_addr": "f4:3c:3b:36:18:2d",
        "ap_ssid": "InEdgeGateway",
        "auth_method": 0,
        "ap_channel": 11,
        "encrypt_method": 0,
        "sta_ssid": "0x696E68616E642D76697369746F72",
        "sta_connection": 1,
        "sta_auth_method": 5,
        "sta_encrypt_method": 4,
        "sta_gateway": "10.5.60.254",
        "sta_dns": "61.139.2.69 183.221.253.100",
        "sta_connect_time": 218,
        "ip_addr": "10.5.60.111",
        "netmask": "255.255.255.0"
    }
}
```

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| station\_role | string | \[0,1] | Wi-Fi模式<br/>0: AP<br/>1: Station |
| status | integer | \[0, 1] | Wi-Fi状态<br/>0：关闭<br/>1：开启 |
| mac\_addr | string | 17字符 | Wi-Fi接口的MAC地址 |
| encrypt\_method | integer | \[0, 4] | 加密方式<br/>0：不加密<br/>1： WEP40 <br/>2： WEP104  <br/>3： TKIP <br/>4:    AES |
| sta\_ssid | integer | \[1, 32] | 连接的SSID名称 |
| sta\_connection | integer | \[0, 1] | 连接状态：<br/>0： 未连接<br/>1： 已连接 |
| sta\_auth\_method | integer | \[0, 6] | 认证方式<br/>0: 无认证<br/>1: 共享式认证<br/>2: 保留未使用<br/>3: WPA-PSK认证<br/>4: WPA认证<br/>5: WPA2-PSK认证<br/>6: WPA2认证 |
| sta\_gateway | string | \[1, 16]字符 | Wi-Fi 接口的网关地址，即AP的IP地址。 |
| sta\_dns | string | \[1, 16]字符 | Wi-Fi接口获取的dns地址 |
| sta\_connect\_time | integer | \[0, 4294967296] | Wi-Fi连接时长 |
| ip\_addr | string | \[1, 16]字符 | Wi-Fi接口的IP地址 |
| netmask | string | \[1, 16]字符 | Wi-Fi接口的子网掩码 |

#### 更新AP配置

接口

```http
PUT v1/dot11radio/config?autosave=1
```

负载

```json
{
    "enable": 1,
    "iface": "dot11radio1",
    "station_role": 0,
    "ap_ssid_broadcast": 1,
    "ap_ssid": "0x496E4564676547617465776179",
    "auth_method": 0,
    "wpa_psk_key": "",
    "ap_max_associations": 10,
    "ap_wpa_group_rekey": 3600,
    "ap_isolate": 0,
    "ap_band": 0,
    "ap_radio_type": 7,
    "ap_channel": 11,
    "encrypt_mode": 0,
    "wep_key": "",
    "ap_radius_ip": "",
    "ap_radius_port": 1812,
    "ap_radius_key": "",
    "ap_radius_srcif": "",
    "ap_bandwidth": 0,
    "sta_default_route": 0,
    "sta_ssid": "",
    "sta_auth_method": 0,
    "sta_encrypt_mode": 0,
    "sta_wpa_psk_key": "",
    "sta_wep_key": "",
    "sta_auth_mode": 0,
    "sta_inner_auth": 0,
    "sta_username": "",
    "sta_password": "",
    "sta_dhcp": 0,
    "ip_addr": "",
    "netmask": ""
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | WLAN开关，0关闭，1开启 |
| station\_role   | integer | \[0, 1] | Wi-Fi工作模式<br/>0：AP<br/>1：Station |
| ap\_ssid | string | \[1, 32]字符 | AP模式时的ssid名称 |
| ap\_ssid\_broadcast | integer | \[0, 1] | SSID广播开关，0为关闭，1为开启 |
| auth\_method | integer | \[0, 8] | 认证方式<br/>0：无认证<br/>1：共享认证<br/>2：保留字段<br/>3：WPA-PSK  <br/>4： WPA <br/>5： WPA2-PSK  <br/>6： WPA2 <br/>7： WPA/WPA2 <br/>8： WPAPSK/WPA2PSK   |
| wpa\_psk\_key | string | \[8, 63]字符 |  WPA/WPA2 PSK 密钥， 认证方式为 WPA-PSK，WPA2-PSK，WPAPSK/WPA2PSK 时，该选项才有效  |
| ap\_max\_associations | integer | \[1, 128] | 客户端的最大数量 |
| ap\_wpa\_group\_rekey | integer | \[600, 86400] | 组密码协商时间 |
| ap\_isolate | integer | \[0, 1] | AP隔离开关，0关闭，1开启 |
| ap\_band | integer | \[0, 1] | 无线频段，0为2.4G，1为5G |
| ap\_radio\_type | integer | 0: 802.11b/g, <br/>1: 802.11b, <br/>2: 802.11a, <br/>4: 802.11g, <br/>6: 802.11n, <br/>7: 802.11g/n, <br/>8: 802.11an/ac,<br/>9: 802.11b/g/n , <br/>11: 802.11na   |  无线频段为 2.4G 时，该下拉选项有：0, 1, 4, 6, 7, 9；无线频段为 5G 时，该下拉选项有：2, 8, 11    |
|  ap\_channel | integer | \[1, 11] | 信道 |
| encrypt\_mode | integer | \[0, 4] | 加密方式<br/>0：不加密<br/>1： WEP40 <br/>2： WEP104  <br/>3： TKIP <br/>4:    AES |
| wep\_key | string | \[0, 16]字符 | 网络密钥 |
| ap\_radius\_ip | string | \[1, 16]字符 | radius服务器的IP地址 |
| ap\_radius\_port | integer | \[1, 65535] | radius服务器的端口号 |
| ap\_radius\_key | string | \[1, 32]字符 | radius服务器的共享密钥 |
| ap\_radius\_srcif | string | \[1, 16]字符 | 与radius服务器连接的接口名称 |
| ap\_bandwidth | integer | 0，1，3 | 无线频宽<br/>0：20MHZ<br/>1：40MHz<br/>3：80MHz |
| sta\_default\_route | integer | \[0, 1] | 模式为station的时候时候添加基于WLAN的默认路由，0不添加，1添加 |
| sta\_ssid | string | \[1, 64]字符 | 模式为station时要连接的ssid名称 |
| sta\_auth\_method | integer | \[0, 6] | 认证方式<br/>0: 无认证<br/>1: 共享式认证<br/>2: 保留未使用<br/>3: WPA-PSK认证<br/>4: WPA认证<br/>5: WPA2-PSK认证<br/>6: WPA2认证 |
| sta\_auth\_mode | integer | 1 | 认证模式(WPA/WPA2模式时需要配置)<br/>1: EAP-PEAP |
| sta\_inner\_auth | integer | \[1, 2] | 内部身份验证(WPA/WPA2模式时需要配置)<br/>1: mschapv2<br/>2: md5 |
| sta\_username | string |  | 用户名(WPA/WPA2模式时需要配置) |
| sta\_password | string |  | 密码(WPA/WPA2模式时需要配置) |
| sta\_dhcp | integer | \[0, 1] | 是否启用静态IP：<br/>0：使用静态IP<br/>1：不使用静态IP，使用DHCP获取IP地址 |
| ip\_addr | string | \[0, 16]字符 | 启用静态ip时，设置的静态IP地址 |
| netmask | string | \[0, 16]字符 | 启用静态ip时，设置的子网掩码 |

#### 查询AP配置

接口

```http
GET v1/dot11radio/config?iface=dot11radio1
```

响应

```json
{
    "results": {
        "enable": 1,
        "iface": "dot11radio1",
        "station_role": 0,
        "ap_ssid_broadcast": 1,
        "ap_ssid": "0x496E4564676547617465776179",
        "auth_method": 0,
        "wpa_psk_key": "",
        "ap_max_associations": 10,
        "ap_wpa_group_rekey": 3600,
        "ap_isolate": 0,
        "ap_band": 0,
        "ap_radio_type": 7,
        "ap_channel": 11,
        "encrypt_mode": 0,
        "wep_key": "",
        "ap_radius_ip": "",
        "ap_radius_port": 1812,
        "ap_radius_key": "",
        "ap_radius_srcif": "",
        "ap_bandwidth": 0,
        "sta_default_route": 0,
        "sta_ssid": "",
        "sta_auth_method": 0,
        "sta_encrypt_mode": 0,
        "sta_wpa_psk_key": "",
        "sta_wep_key": "",
        "sta_auth_mode": 0,
        "sta_inner_auth": 0,
        "sta_username": "",
        "sta_password": "",
        "sta_dhcp": 0,
        "ip_addr": "0.0.0.0",
        "netmask": "0.0.0.0"
    }
}
```

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | WLAN开关，0关闭，1开启 |
| station\_role   | integer | \[0, 1] | Wi-Fi工作模式<br/>0：AP<br/>1：Station |
| ap\_ssid | string | \[1, 32]字符 | AP模式时的ssid名称 |
| ap\_ssid\_broadcast | integer | \[0, 1] | SSID广播开关，0为关闭，1为开启 |
| auth\_method | integer | \[0, 8] | 认证方式<br/>0：无认证<br/>1：共享认证<br/>2：保留字段<br/>3：WPA-PSK  <br/>4： WPA <br/>5： WPA2-PSK  <br/>6： WPA2 <br/>7： WPA/WPA2 <br/>8： WPAPSK/WPA2PSK   |
| wpa\_psk\_key | string | \[8, 63]字符 |  WPA/WPA2 PSK 密钥， 认证方式为 WPA-PSK，WPA2-PSK，WPAPSK/WPA2PSK 时，该选项才有效  |
| ap\_max\_associations | integer | \[1, 128] | 客户端的最大数量 |
| ap\_wpa\_group\_rekey | integer | \[600, 86400] | 组密码协商时间 |
| ap\_isolate | integer | \[0, 1] | AP隔离开关，0关闭，1开启 |
| ap\_band | integer | \[0, 1] | 无线频段，0为2.4G，1为5G |
| ap\_radio\_type | integer | 0: 802.11b/g, <br/>1: 802.11b, <br/>2: 802.11a, <br/>4: 802.11g, <br/>6: 802.11n, <br/>7: 802.11g/n, <br/>8: 802.11an/ac,<br/>9: 802.11b/g/n , <br/>11: 802.11na   |  无线频段为 2.4G 时，该下拉选项有：0, 1, 4, 6, 7, 9；无线频段为 5G 时，该下拉选项有：2, 8, 11    |
|  ap\_channel | integer | \[1, 11] | 信道 |
| encrypt\_mode | integer | \[0, 4] | 加密方式<br/>0：不加密<br/>1： WEP40 <br/>2： WEP104  <br/>3： TKIP <br/>4:    AES |
| wep\_key | string | \[0, 16]字符 | 网络密钥 |
| ap\_radius\_ip | string | \[1, 16]字符 | radius服务器的IP地址 |
| ap\_radius\_port | integer | \[1, 65535] | radius服务器的端口号 |
| ap\_radius\_key | string | \[1, 32]字符 | radius服务器的共享密钥 |
| ap\_radius\_srcif | string | \[1, 16]字符 | 与radius服务器连接的接口名称 |
| ap\_bandwidth | integer | 0，1，3 | 无线频宽<br/>0：20MHZ<br/>1：40MHz<br/>3：80MHz |
| sta\_default\_route | integer | \[0, 1] | 模式为station的时候时候添加基于WLAN的默认路由，0不添加，1添加 |
| sta\_ssid | string | \[1, 64]字符 | 模式为station时要连接的ssid名称 |
| sta\_auth\_method | integer | \[0, 6] | 认证方式<br/>0: 无认证<br/>1: 共享式认证<br/>2: 保留未使用<br/>3: WPA-PSK认证<br/>4: WPA认证<br/>5: WPA2-PSK认证<br/>6: WPA2认证 |
| sta\_auth\_mode | integer | 1 | 认证模式(WPA/WPA2模式时需要配置)<br/>1: EAP-PEAP |
| sta\_inner\_auth | integer | \[1, 2] | 内部身份验证(WPA/WPA2模式时需要配置)<br/>1: mschapv2<br/>2: md5 |
| sta\_username | string |  | 用户名(WPA/WPA2模式时需要配置) |
| sta\_password | string |  | 密码(WPA/WPA2模式时需要配置) |
| sta\_dhcp | integer | \[0, 1] | 是否启用静态IP：<br/>0：使用静态IP<br/>1：不使用静态IP，使用DHCP获取IP地址 |
| ip\_addr | string | \[0, 16]字符 | 启用静态ip时，设置的静态IP地址 |
| netmask | string | \[0, 16]字符 | 启用静态ip时，设置的子网掩码 |

#### 查询AP状态

接口

```http
GET v1/dot11radio/status?iface=dot11radio1
```

响应

```json
{
    "results": {
        "station_role": 0,
        "status": 1,
        "mac_addr": "f4:3c:3b:36:18:2d",
        "ap_ssid": "0x496E4564676547617465776179",
        "ap_channel": 11,
    }
}
```

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| station\_role | string | \[0,1] | Wi-Fi模式<br/>0: AP<br/>1: Station |
| status | integer | \[0, 1] | Wi-Fi状态<br/>0：关闭<br/>1：开启 |
| mac\_addr | string | 17字符 | Wi-Fi接口的MAC地址 |
| ap\_ssid | string | \[1,32]字符 | AP SSID的名称 |
| ap\_channel | integer | \[1, 11] | 信道 |

### Loopback

#### 更新配置

接口

```http
PUT v1/loopback/config?autosave=1
```

负载

```json
{
    "ip_addr": "127.0.0.1",
    "netmask": "255.0.0.0",
    "multi_ip": [
        {
            "ip_addr": "127.0.0.2",
            "netmask": "255.255.255.0"
        }
    ],
    "description": ""
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| ip\_addr | string | \[1, 16]字符 | 环回口IP地址 |
| netmask | string | \[1, 16]字符 | 接口子网掩码 |
| description | string | \[0, 32]字符 | 接口描述信息 |
| multi\_ip | object | | 唤回口从IP信息 |

#### 查询配置

接口

```http
GET v1/loopback/config
```

响应

```json
{
    "results": {
        "ip_addr": "127.0.0.1",
        "netmask": "255.0.0.0",
        "multi_ip": [
            {
                "ip_addr": "127.0.0.2",
                "netmask": "255.255.255.0"
            }
        ],
        "description": ""
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| ip\_addr | string | \[1, 16]字符 | 环回口IP地址 |
| netmask | string | \[1, 16]字符 | 接口子网掩码 |
| description | string | \[0, 32]字符 | 接口描述信息 |
| multi\_ip | object | | 唤回口从IP信息 |

## 网络服务

### DHCP服务器

#### 更新配置

接口

```http
PUT v1/dhcp/services/config?autosave=1
```

负载

```json
{
    "dhcp_services": [
        {
            "enable": 1,
            "interface": "bridge 1",
            "start_addr": "192.168.2.2",
            "end_addr": "192.168.2.100",
            "lease": 1440
        }
    ],
    "windows_name_server": "192.168.2.200",
    "macip_bind_config": [
        {
            "mac_addr": "00:18:06:21:EA:EA",
            "ip_addr": "192.168.2.100"
        }
    ],
    "dhcp_relay_enable": 0,
    "isChecked": 1
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| dhcp\_services | object |  | DHCP Server的配置 |
| enable | integer | \[0, 1] | DHCP Server开关，0关闭，1开启 |
| start\_addr | string | \[1, 16]字符 | DHCP地址池的起始地址 |
| end\_addr | string | \[1, 16]字符 | DHCP地址池的结束地址 |
| lease | integer | \[30, 10080]分钟 | 租期时长 |
| windows\_name\_server | string | \[1, 16]字符 | Windows名称服务器 |
| macip\_bind\_config | object |  | MAC和IP绑定的配置 |
| mac\_addr | string | \[1, 18]字符 | 需要绑定的MAC地址 |
| ip\_addr | string | \[1, 16]字符 | 需要绑定的IP地址 |
| dhcp\_relay\_enable | integer | \[0, 1] | 是否开启DHCP中继，0关闭，1开启 |
| isChecked | interger | \[0, 1] | 是否开启IP地址冲突检测，固定为1 |

#### 查询配置

接口

```http
GET v1/dhcp/services/config
```

响应

```http
{
    "results": {
        "dhcp_relay_enable": 0,
        "dhcp_services": [
            {
                "enable": 1,
                "interface": "bridge 1",
                "start_addr": "192.168.2.2",
                "end_addr": "192.168.2.100",
                "lease": 1440
            }
        ],
        "windows_name_server": "",
        "macip_bind_config": [

        ]
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| dhcp\_services | object |  | DHCP Server的配置 |
| enable | integer | \[0, 1] | DHCP Server开关，0关闭，1开启 |
| start\_addr | string | \[1, 16]字符 | DHCP地址池的起始地址 |
| end\_addr | string | \[1, 16]字符 | DHCP地址池的结束地址 |
| lease | integer | \[30, 10080]分钟 | 租期时长 |
| windows\_name\_server | string | \[1, 16]字符 | Windows名称服务器 |
| macip\_bind\_config | object |  | MAC和IP绑定的配置 |
| mac\_addr | string | \[1, 18]字符 | 需要绑定的MAC地址 |
| ip\_addr | string | \[1, 16]字符 | 需要绑定的IP地址 |
| dhcp\_relay\_enable | integer | \[0, 1] | 是否开启DHCP中继，0关闭，1开启 |

### DNS服务

DNS服务页面分为域名服务和中继服务。

#### 域名服务

##### 更新配置

接口

```http
v1/dns/server/config?autosave=1
```

负载

```json
{
    "primary_dns": "8.8.8.8",
    "secondary_dns": "114.114.114.114"
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| primary\_dns | string | \[1, 16]字符 | 首选域名服务器 |
| secondary\_dns | string | \[1, 16]字符 | 备选域名服务器 |

##### 查询配置

接口

```http
GET v1/dns/server/config
```

响应

```json
{
    "results": {
        "primary_dns": "8.8.8.8",
        "secondary_dns": "114.114.114.114"
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| primary\_dns | string | \[1, 16]字符 | 首选域名服务器 |
| secondary\_dns | string | \[1, 16]字符 | 备选域名服务器 |

#### 中继服务

##### 更新配置

接口

```http
PUT v1/dns/relay/config?autosave=1
```

负载

```json
{
    "enable": 1,
    "dhcp_enable": 1,
    "host_ip_relation": [
        {
            "host": "www.google.com",
            "ip_addr1": "1.2.3.4",
            "ip_addr2": "4.3.2.1"
        }
    ]
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | DNS中继服务开关，0关闭，1开启 |
| dhcp\_enable | integer | \[0, 1] | DHCP Server开关，0关闭，1开启，调用该接口前，先查询DHCP Server的状态，此处传值保持一致。 |
| host\_ip\_relation | object |  | 域名和IP映射 |
| host | string | \[1, 64]字符 |  |
| ip\_addr1 | string | \[1, 16]字符 | 域名对应的第一个IP地址 |
| ip\_addr2 | string | \[1, 16]字符 | 域名对应的第二个IP地址 |

##### 查询配置

接口

```http
GET v1/dns/relay/config
```

响应

```json
{
    "results": {
        "enable": 1,
        "dhcp_enable": 0,
        "host_ip_relation": [
            {
                "host": "www.google.com",
                "ip_addr1": "1.2.3.4",
                "ip_addr2": "4.3.2.1"
            }
        ]
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | DNS中继服务开关，0关闭，1开启 |
| dhcp\_enable | integer | \[0, 1] | DHCP Server开关，0关闭，1开启，调用该接口前，先查询DHCP Server的状态，此处传值保持一致。 |
| host\_ip\_relation | object |  | 域名和IP映射 |
| host | string | \[1, 64]字符 |  |
| ip\_addr1 | string | \[1, 16]字符 | 域名对应的第一个IP地址 |
| ip\_addr2 | string | \[1, 16]字符 | 域名对应的第二个IP地址 |

## 主机列表

#### 查询状态

接口

```http
v1/dhcp/services/status
```

响应

```json
{
    "results": [
        {
            "interface": "fastethernet 0/1",
            "mac_addr": "e4:54:e8:d2:1a:be",
            "ip_addr": "10.5.30.215",
            "host_addr": "",
            "lease": 0
        },
        {
            "interface": "fastethernet 0/1",
            "mac_addr": "08:00:27:6b:a1:eb",
            "ip_addr": "10.5.30.31",
            "host_addr": "",
            "lease": 0
        },
        {
            "interface": "bridge 1",
            "mac_addr": "88:a4:c2:95:71:35",
            "ip_addr": "192.168.2.99",
            "host_addr": "",
            "lease": 0
        },
        {
            "interface": "fastethernet 0/1",
            "mac_addr": "78:17:be:ca:0d:76",
            "ip_addr": "10.5.30.254",
            "host_addr": "",
            "lease": 0
        }
    ]
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| interface | string | \[1, 32]字符 | 和主机相连的接口的名称 |
| mac\_addr | string | \[1, 18]字符 | 主机mac地址 |
| ip\_addr | string | \[1, 16]字符  | 主机ip地址 |
| host\_addr | string | \[1, 64]字符 | 主机名称 |
| lease | string | \[0, 10080]字符 | 主机通过DHCP获取地址时的租期时长 |

## 路由

路由菜单下分为路由状态和静态路由配置

#### 路由状态

##### 查询状态

```http
GET v1/route/status
```

响应

```json
{
    "results": [
        {
            "type": "static",
            "destination": "0.0.0.0",
            "netmask": "0.0.0.0",
            "gateway": "10.5.30.254",
            "interface": "fastethernet 0/1",
            "distance_metric": "255/0",
            "time": ""
        },
        {
            "type": "connected",
            "destination": "10.5.30.0",
            "netmask": "255.255.255.0",
            "gateway": "",
            "interface": "fastethernet 0/1",
            "distance_metric": "0/0",
            "time": ""
        },
        {
            "type": "connected",
            "destination": "127.0.0.0",
            "netmask": "255.0.0.0",
            "gateway": "",
            "interface": "loopback 1",
            "distance_metric": "0/0",
            "time": ""
        },
        {
            "type": "connected",
            "destination": "192.168.2.0",
            "netmask": "255.255.255.0",
            "gateway": "",
            "interface": "bridge 1",
            "distance_metric": "0/0",
            "time": ""
        }
    ]
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| type | string | \[1, 16]字符 | static：静态路由<br/>connected：直连路由 |
| interface | string | \[1, 16]字符 | 路由对应的接口名称 |
| destination | string | \[1, 16]字符 | 路由的目标地址 |
| netmask | string | \[1, 16]字符  | 路由的目标地址的子网掩码 |
| distance\_metric | string | \[1, 16]字符 | 路由的距离和度量信息 |
| gateway | string | \[1, 16]字符 | 路由下一跳的IP地址 |
| time | string | \[0, 32]字符 |  |

#### 静态路由

##### 更新配置

接口

```http
v1/route/static/config?autosave=1
```

负载

```json
[
    {
        "destination": "0.0.0.0",
        "netmask": "0.0.0.0",
        "interface": "cellular 1",
        "gateway": "",
        "distance": 253,
        "track": 0
    },
    {
        "destination": "0.0.0.0",
        "netmask": "0.0.0.0",
        "interface": "fastethernet 0/1",
        "gateway": "10.5.30.254",
        "distance": 254,
        "track": 0
    }
]
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| destination | string | \[1, 16]字符 | 路由的目标地址 |
| netmask | string | \[1, 16]字符  | 路由的目标地址的子网掩码 |
| interface | string | \[1, 16]字符 | 路由对应的接口信息 |
| gateway | string | \[1, 16]字符 | 路由下一跳的IP地址 |
| distance | integer | \[2, 255] | 路由的距离信息 |
| track | integer | \[1, 10] | 路由的track标识 |

##### 查询配置

接口

```http
GET v1/route/static/config
```

响应

```json
{
    "results": [
        {
            "destination": "0.0.0.0",
            "netmask": "0.0.0.0",
            "interface": "cellular 1",
            "gateway": "",
            "distance": 253,
            "track": 0
        },
        {
            "destination": "0.0.0.0",
            "netmask": "0.0.0.0",
            "interface": "fastethernet 0/1",
            "gateway": "10.5.30.254",
            "distance": 254,
            "track": 0
        }
    ]
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| destination | string | \[1, 16]字符 | 路由的目标地址 |
| netmask | string | \[1, 16]字符  | 路由的目标地址的子网掩码 |
| interface | string | \[1, 16]字符 | 路由对应的接口信息 |
| gateway | string | \[1, 16]字符 | 路由下一跳的IP地址 |
| distance | integer | \[2, 255] | 路由的距离信息 |
| track | integer | \[1, 10] | 路由的track标识 |

## 防火墙

防火墙包含访问控制列表和网络地址转换两个子功能

#### 访问控制列表

##### 更新配置

接口

```http
PUT v1/firewall/acl/config?autosave=1
```

负载

```json
{
    "access_control_list": [
        {
            "id": 100,
            "sequence_number": 10,
            "action": 0,
            "protocol": 0,
            "acl_source": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "any",
                "port1": 0,
                "port2": 0
            },
            "acl_destination": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "any",
                "port1": 0,
                "port2": 0
            },
            "icmp_type": 0,
            "icmp_describe_value": "all",
            "icmp_type_value": 0,
            "icmp_code_value": 0,
            "established": 0,
            "fragments": 0,
            "log": 0,
            "description": ""
        },
        {
            "id": 101,
            "sequence_number": 10,
            "action": 0,
            "protocol": 0,
            "acl_source": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "any",
                "port1": 0,
                "port2": 0
            },
            "acl_destination": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "any",
                "port1": 0,
                "port2": 0
            },
            "icmp_type": 0,
            "icmp_describe_value": "all",
            "icmp_type_value": 0,
            "icmp_code_value": 0,
            "established": 0,
            "fragments": 0,
            "log": 0,
            "description": ""
        },
        {
            "id": 102,
            "sequence_number": 20,
            "action": 0,
            "protocol": 0,
            "acl_source": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "any",
                "port1": 0,
                "port2": 0
            },
            "acl_destination": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "any",
                "port1": 0,
                "port2": 0
            },
            "icmp_type": 0,
            "icmp_describe_value": "all",
            "icmp_type_value": 0,
            "icmp_code_value": 0,
            "established": 0,
            "fragments": 0,
            "log": "",
            "description": ""
        },
        {
            "id": 192,
            "sequence_number": 10,
            "action": 0,
            "protocol": 6,
            "acl_source": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "any",
                "port1": 0,
                "port2": 0
            },
            "acl_destination": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "eq",
                "port1": 443,
                "port2": 0
            },
            "icmp_type": 0,
            "icmp_describe_value": "all",
            "icmp_type_value": 0,
            "icmp_code_value": 0,
            "established": 0,
            "fragments": 0,
            "log": 1,
            "description": ""
        },
        {
            "id": 192,
            "sequence_number": 20,
            "action": 1,
            "protocol": 6,
            "acl_source": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "any",
                "port1": 0,
                "port2": 0
            },
            "acl_destination": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "eq",
                "port1": 80,
                "port2": 0
            },
            "icmp_type": 0,
            "icmp_describe_value": "all",
            "icmp_type_value": 0,
            "icmp_code_value": 0,
            "established": 0,
            "fragments": 0,
            "log": 0,
            "description": ""
        },
        {
            "id": 192,
            "sequence_number": 30,
            "action": 1,
            "protocol": 6,
            "acl_source": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "any",
                "port1": 0,
                "port2": 0
            },
            "acl_destination": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "eq",
                "port1": 23,
                "port2": 0
            },
            "icmp_type": 0,
            "icmp_describe_value": "all",
            "icmp_type_value": 0,
            "icmp_code_value": 0,
            "established": 0,
            "fragments": 0,
            "log": 0,
            "description": ""
        },
        {
            "id": 192,
            "sequence_number": 40,
            "action": 1,
            "protocol": 6,
            "acl_source": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "any",
                "port1": 0,
                "port2": 0
            },
            "acl_destination": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "eq",
                "port1": 22,
                "port2": 0
            },
            "icmp_type": 0,
            "icmp_describe_value": "all",
            "icmp_type_value": 0,
            "icmp_code_value": 0,
            "established": 0,
            "fragments": 0,
            "log": 0,
            "description": ""
        },
        {
            "id": 192,
            "sequence_number": 50,
            "action": 1,
            "protocol": 6,
            "acl_source": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "any",
                "port1": 0,
                "port2": 0
            },
            "acl_destination": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "eq",
                "port1": 53,
                "port2": 0
            },
            "icmp_type": 0,
            "icmp_describe_value": "all",
            "icmp_type_value": 0,
            "icmp_code_value": 0,
            "established": 0,
            "fragments": 0,
            "log": 0,
            "description": ""
        },
        {
            "id": 192,
            "sequence_number": 60,
            "action": 1,
            "protocol": 17,
            "acl_source": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "any",
                "port1": 0,
                "port2": 0
            },
            "acl_destination": {
                "ip": "any",
                "wildcard_mask": "",
                "port_rule": "eq",
                "port1": 53,
                "port2": 0
            },
            "icmp_type": 0,
            "icmp_describe_value": "all",
            "icmp_type_value": 0,
            "icmp_code_value": 0,
            "established": 0,
            "fragments": 0,
            "log": 0,
            "description": ""
        }
    ],
    "default_policy": 0,
    "interface_list": [
        {
            "interface": "cellular 1",
            "inbound_acl": 0,
            "outbound_acl": 0,
            "admin_acl": 192
        }
    ]
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| destination | string | \[1, 16]字符 | 路由的目标地址 |
| netmask | string | \[1, 16]字符  | 路由的目标地址的子网掩码 |
| interface | string | \[1, 16]字符 | 路由对应的接口信息 |
| gateway | string | \[1, 16]字符 | 路由下一跳的IP地址 |
| distance | integer | \[2, 255] | 路由的距离信息 |
| track | integer | \[1, 10] | 路由的track标识 |

##### 查询配置

接口

```http
GET v1/firewall/acl/config
```

响应

```json
{
    "results": {
        "default_policy": 0,
        "access_control_list": [
            {
                "id": 100,
                "sequence_number": 10,
                "action": 0,
                "protocol": 0,
                "acl_source": {
                    "ip": "any",
                    "wildcard_mask": ""
                },
                "acl_destination": {
                    "ip": "any",
                    "wildcard_mask": ""
                },
                "fragments": 0,
                "log": 0,
                "description": ""
            },
            {
                "id": 101,
                "sequence_number": 10,
                "action": 0,
                "protocol": 0,
                "acl_source": {
                    "ip": "any",
                    "wildcard_mask": ""
                },
                "acl_destination": {
                    "ip": "any",
                    "wildcard_mask": ""
                },
                "fragments": 0,
                "log": 0,
                "description": ""
            },
            {
                "id": 102,
                "sequence_number": 20,
                "action": 0,
                "protocol": 0,
                "acl_source": {
                    "ip": "any",
                    "wildcard_mask": ""
                },
                "acl_destination": {
                    "ip": "any",
                    "wildcard_mask": ""
                },
                "fragments": 0,
                "log": 0,
                "description": ""
            },
            {
                "id": 192,
                "sequence_number": 10,
                "action": 0,
                "protocol": 6,
                "acl_source": {
                    "ip": "any",
                    "wildcard_mask": "",
                    "port_rule": "any"
                },
                "acl_destination": {
                    "ip": "any",
                    "wildcard_mask": "",
                    "port_rule": "eq",
                    "port1": 443
                },
                "established": 0,
                "log": 1,
                "description": ""
            },
            {
                "id": 192,
                "sequence_number": 20,
                "action": 1,
                "protocol": 6,
                "acl_source": {
                    "ip": "any",
                    "wildcard_mask": "",
                    "port_rule": "any"
                },
                "acl_destination": {
                    "ip": "any",
                    "wildcard_mask": "",
                    "port_rule": "eq",
                    "port1": 80
                },
                "established": 0,
                "log": 0,
                "description": ""
            },
            {
                "id": 192,
                "sequence_number": 30,
                "action": 1,
                "protocol": 6,
                "acl_source": {
                    "ip": "any",
                    "wildcard_mask": "",
                    "port_rule": "any"
                },
                "acl_destination": {
                    "ip": "any",
                    "wildcard_mask": "",
                    "port_rule": "eq",
                    "port1": 23
                },
                "established": 0,
                "log": 0,
                "description": ""
            },
            {
                "id": 192,
                "sequence_number": 40,
                "action": 1,
                "protocol": 6,
                "acl_source": {
                    "ip": "any",
                    "wildcard_mask": "",
                    "port_rule": "any"
                },
                "acl_destination": {
                    "ip": "any",
                    "wildcard_mask": "",
                    "port_rule": "eq",
                    "port1": 22
                },
                "established": 0,
                "log": 0,
                "description": ""
            },
            {
                "id": 192,
                "sequence_number": 50,
                "action": 1,
                "protocol": 6,
                "acl_source": {
                    "ip": "any",
                    "wildcard_mask": "",
                    "port_rule": "any"
                },
                "acl_destination": {
                    "ip": "any",
                    "wildcard_mask": "",
                    "port_rule": "eq",
                    "port1": 53
                },
                "established": 0,
                "log": 0,
                "description": ""
            },
            {
                "id": 192,
                "sequence_number": 60,
                "action": 1,
                "protocol": 17,
                "acl_source": {
                    "ip": "any",
                    "wildcard_mask": "",
                    "port_rule": "any"
                },
                "acl_destination": {
                    "ip": "any",
                    "wildcard_mask": "",
                    "port_rule": "eq",
                    "port1": 53
                },
                "log": 0,
                "description": ""
            }
        ],
        "interface_list": [
            {
                "interface": "cellular 1",
                "inbound_acl": 0,
                "outbound_acl": 0,
                "admin_acl": 192
            }
        ]
    }
}
```

#### 网络地址转换

##### 更新配置

接口

```http
PUT v1/firewall/nat/config?autosave=1
```

负载

```json
{
    "nat_rule_list": [
        {
            "action": 0,
            "source_network": 0,
            "translation_type": 5,
            "transmit_protocol": 0,
            "transmit_source": {
                "ip_addr": "0.0.0.0",
                "port": 0,
                "acl_num": 101,
                "interface": "",
                "end_port": 0
            },
            "transmit_dest": {
                "ip_addr": "0.0.0.0",
                "port": 0,
                "acl_num": 0,
                "interface": "fastethernet 0/1",
                "end_port": 0
            },
            "source_range": {
                "ip_addr": "0.0.0.0",
                "netmask": "0.0.0.0"
            },
            "description": "",
            "log": 0
        },
        {
            "action": 0,
            "source_network": 0,
            "translation_type": 5,
            "transmit_protocol": 0,
            "transmit_source": {
                "ip_addr": "0.0.0.0",
                "port": 0,
                "acl_num": 100,
                "interface": "",
                "end_port": 0
            },
            "transmit_dest": {
                "ip_addr": "0.0.0.0",
                "port": 0,
                "acl_num": 0,
                "interface": "cellular 1",
                "end_port": 0
            },
            "source_range": {
                "ip_addr": "0.0.0.0",
                "netmask": "0.0.0.0"
            },
            "description": "",
            "log": 0
        },
        {
            "action": 0,
            "source_network": 0,
            "translation_type": 0,
            "transmit_protocol": 1,
            "transmit_source": {
                "ip_addr": "1.1.1.1",
                "port": 0,
                "acl_num": 100,
                "end_port": 0,
                "interface": ""
            },
            "transmit_dest": {
                "ip_addr": "2.2.2.2",
                "port": 0,
                "acl_num": 0,
                "end_port": 0,
                "interface": ""
            },
            "source_range": {
                "ip_addr": "0.0.0.0",
                "mask": "0.0.0.0"
            },
            "description": "",
            "log": 0
        }
    ],
    "network_interface": [
        {
            "type": 2,
            "interface": "cellular 1"
        },
        {
            "type": 1,
            "interface": "bridge 1"
        },
        {
            "type": 2,
            "interface": "fastethernet 0/1"
        }
    ]
}
```

##### 查询配置

接口

```http
GET v1/firewall/nat/config
```

响应

```json
{
    "nat_rule_list": [
        {
            "action": 0,
            "source_network": 0,
            "translation_type": 5,
            "transmit_protocol": 0,
            "transmit_source": {
                "ip_addr": "0.0.0.0",
                "port": 0,
                "acl_num": 101,
                "interface": "",
                "end_port": 0
            },
            "transmit_dest": {
                "ip_addr": "0.0.0.0",
                "port": 0,
                "acl_num": 0,
                "interface": "fastethernet 0/1",
                "end_port": 0
            },
            "source_range": {
                "ip_addr": "0.0.0.0",
                "netmask": "0.0.0.0"
            },
            "description": "",
            "log": 0
        },
        {
            "action": 0,
            "source_network": 0,
            "translation_type": 5,
            "transmit_protocol": 0,
            "transmit_source": {
                "ip_addr": "0.0.0.0",
                "port": 0,
                "acl_num": 100,
                "interface": "",
                "end_port": 0
            },
            "transmit_dest": {
                "ip_addr": "0.0.0.0",
                "port": 0,
                "acl_num": 0,
                "interface": "cellular 1",
                "end_port": 0
            },
            "source_range": {
                "ip_addr": "0.0.0.0",
                "netmask": "0.0.0.0"
            },
            "description": "",
            "log": 0
        },
        {
            "action": 0,
            "source_network": 0,
            "translation_type": 0,
            "transmit_protocol": 1,
            "transmit_source": {
                "ip_addr": "1.1.1.1",
                "port": 0,
                "acl_num": 100,
                "end_port": 0,
                "interface": ""
            },
            "transmit_dest": {
                "ip_addr": "2.2.2.2",
                "port": 0,
                "acl_num": 0,
                "end_port": 0,
                "interface": ""
            },
            "source_range": {
                "ip_addr": "0.0.0.0",
                "mask": "0.0.0.0"
            },
            "description": "",
            "log": 0
        }
    ],
    "network_interface": [
        {
            "type": 2,
            "interface": "cellular 1"
        },
        {
            "type": 1,
            "interface": "bridge 1"
        },
        {
            "type": 2,
            "interface": "fastethernet 0/1"
        }
    ]
}
```

## 边缘计算

### Python APP

#### 安装Python APP

由于Python APP安装包可能会比较大，安装的过程需要对APP安装包进行分块传输；这个过程中需要调用3类接口：

1. 分块传输开始接口

```http
GET /v1/files/before/app/import?md5=02c22f0493471e0bc3d25cbdf3893481&name=device_supervisor-V3.1.5.tar.gz
```

**参数说明**

| \*\*            参数名称\*\* | \*\*            参数描述\*\* | \*\*            参数类型\*\* | \*\*              取值范围\*\* |
| --- | --- | --- | --- |
| name | app安装包的名称 | 字符串 | |
| md5 | app安装包的md5值 | 字符串 | |

1. 分块传输接口

建议将app安装包安装5 \* 1024 \* 1024字节大小进行分块.

```http
POST /v1/files/app/import?type=app&sub_type=app&fileName=device_supervisor-V3.1.5.tar.gz&chunks=27&chunk=17&size=82408268&md5=02c22f0493471e0bc3d25
```

| \*\*            参数名称\*\* | \*\*            参数描述\*\* | \*\*            参数类型\*\* | \*\*              取值范围\*\* |
| --- | --- | --- | --- |
| type | 导入文件的类型，安装python app的时候取值为app |  | |
| sub\_type | 导入文件的子类型，安装python app的时候取值为app |  | |
| fileName | app安装包的名称 |  | |
| chunks | 总的分块数量 |  | |
| chunk | 当前包是第几个分块 |  | |
| size | app安装包的总大小，单位是字节 |  | |
| md5 | app安装包的md5值 |  | |

1. 将分块合并为app整包接口

```http
POST /v1/files/merge/app/import
```

**请求示例**

```json
{
    "data": {
        "name": "device_supervisor-V3.1.5.tar.gz",
        "total": 82408268
    }
}
```

参数说明

|             参数名称 |             参数描述 |             参数类型 |               取值范围 |
| --- | --- | --- | --- |
| name | app安装包的名称 |  | |
| total | app安装包的大小，单位是字节 |  | |

#### 删除Python APP

```http
POST /v1/python/agent/uninstall/app?autosave=1&app_name=device_supervisor
```

**参数说明**

|             参数名称 |             参数描述 |             参数类型 |               取值范围 |
| --- | --- | --- | --- |
| app\_name | 需要删除的app名称 | 字符串 | |

#### 获取Python APP的配置

```http
GET /v1/python/agent/app/config
```

**返回示例**

```json
{
    "results": {
        "python_engine": 1,
        "app_configuration": [
            {
                "enable": 0,
                "app_name": "device_supervisor",
                "app_version": "3.1.5",
                "sdk_version": "1.4.5",
                "start_args": "",
                "log_size": 1,
                "microfrontend_app": 1,
                "log_file_num": 2
            }
        ]
    }
}
```

**参数说明**

|        参数名称 |           参数描述 |            参数类型 |             取值范围 |
| --- | --- | --- | --- |
| python\_engine | 配置python engine的开启/关闭状态 | 数值 | \[0, 1]；0表示关闭python engine；1表示开启python engine. |
| enable | python app的开启/关闭状态 | 数值 | \[0, 1]；0表示关闭python app，1表示开启python app. |
| app\_name | python app的名称；app安装后程序会自动设置； | 字符串 |  |
| app\_version | python app的版本；app安装后程序会自动设置 | 字符串 | |
| sdk\_version | python app依赖的python sdk版本；app安装后程序会自动设置 | 字符串 | |
| start\_args | python app的启动参数；app安装后默认为空 | 字符串 | |
| log\_size | python app的日志大小；app安装后默认为1M | 数值 | \[1, 100]，单位是M. |
| microfrontend\_app | python app是否为微前端程序，app安装后固定为1； | 数值 | 固定为1 |
| log\_file\_num | python app的日志数量；app安装后固定为2 | 数值 | \[1, 2] |

#### 更新Python APP的配置

```http
v1/python/agent/app/config?autosave=1
```

**请求示例**

```json
{
    "python_engine": 1,
    "app_configuration": [
        {
            "enable": 1,
            "app_name": "device_supervisor",
            "app_version": "3.1.5",
            "sdk_version": "1.4.5",
            "start_args": "",
            "log_size": 1,
            "microfrontend_app": 1,
            "log_file_num": 2
        }
    ]
}
```

***

**参数说明**

|        参数名称 |           参数描述 |            参数类型 |             取值范围 |
| --- | --- | --- | --- |
| python\_engine | 配置python engine的开启/关闭；由于python app的运行依赖python engine，此配置项需要配置为1表示开启python engine. | 数值 | \[0, 1]；0表示关闭python engine；1表示开启python engine. |
| enable | python app的开启/关闭； | 数值 | \[0, 1]；0表示关闭python app，1表示开启python app. |
| app\_name | 配置python app的名称； | 字符串 | 这个信息是app安装后程序生成的，需要从获取配置的接口中获取这个信息；不能配置成其他值； |
| app\_version | 配置python app的版本； | 字符串 | 这个信息是app安装后程序生成的，需要从获取配置的接口中获取这个信息；不能配置成其他值； |
| sdk\_version | 配置python app依赖的python sdk版本； | 字符串 | 这个信息是app安装后程序生成的，需要从获取配置的接口中获取这个信息；不能配置成其他值； |
| start\_args | python app启动参数 | 字符串 | |
| log\_size | python app日志大小 | 数值 | \[1, 100]，单位是M. |
| microfrontend\_app | 标志是否为微前端；配置的时候，此参数的取值需要固定为1 | 数值 | 固定为1 |
| log\_file\_num | 日志文件数量，固定为2 | 数值 | 固定为2 |

***

**响应示例**

```json
{
    "results": {
        "python_engine": 1,
        "app_configuration": [
            {
                "enable": 0,
                "app_name": "device_supervisor",
                "app_version": "3.1.5",
                "sdk_version": "1.4.5",
                "start_args": "",
                "log_size": 1,
                "microfrontend_app": 1,
                "log_file_num": 2
            }
        ]
    }
}
```

```http
```

```http
```

#### 启动/停止Python APP

```http
PUT /v1/python/agent/app/management?app_name=device_supervisor&action=start
```

**参数说明**

|        参数名称 |           参数描述 |            参数类型 |             取值范围 |
| --- | --- | --- | --- |
| app\_name | 需要启动的app名称 | 字符串 |  |
| action | python app的开启/关闭； | 字符串 | start表示启动app；stop表示关闭app |

#### 查询Python APP运行状态

```http
GET /v1/python/agent/app/status
```

***

**响应示例**

```json
{
    "results": [
        {
            "app_name": "device_supervisor",
            "app_version": "3.1.5",
            "sdk_version": "1.4.5",
            "state": "STOPPED",
            "start": "2024-05-11T06:06:02+0000",
            "stop": "2024-05-11T06:16:39+0000",
            "exit_code": 0,
            "uptime": "May 11 02:16 PM"
        }
    ]
}
```

**参数说明**

|        参数名称 |           参数描述 |            参数类型 |             取值范围 |
| --- | --- | --- | --- |
| state | python app的运行状态 | 字符串 |  |

## 系统管理

### 系统时间

#### 设置时区

接口

```http
PUT v1/system/timezone?autosave=1
```

负载

```json
{
    "timezone": "UTC-8"
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| timezone | string | \[1, 32]字符 | 时区编码 |

#### 查询时区

接口

```http
GET v1/system/timeinfo
```

> 这个接口除了返回时区信息外，还会返回设备时间信息

响应

```json
{
    "results": {
        "device_time": "2024-08-02 15:58:14",
        "timezone": "UTC-8"
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| timezone | string | \[1, 32]字符 | 时区编码 |
| device\_time | string | \[1, 32]字符 | 设备时间 |

#### 设置时间

接口

```http
PUT v1/system/settime
```

负载

```json
{
    "device_time": "2024-08-01 16:00:17"
}
```

#### SNTP客户端

##### 更新配置

接口

```http
PUT v1/sntp/client/config?autosave=1
```

负载

```json
{
    "enable": 1,
    "update_interval": 600,
    "source_ip": "",
    "sntp_servers_list": [
        {
            "server_addr": "0.pool.ntp.org",
            "port": 123
        },
        {
            "server_addr": "1.pool.ntp.org",
            "port": 123
        },
        {
            "server_addr": "2.pool.ntp.org",
            "port": 123
        },
        {
            "server_addr": "3.pool.ntp.org",
            "port": 123
        }
    ]
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | SNTP开关，0关闭，1开启 |
| update\_interval | integer | \[60, 2592000]秒 | SNTP客户端和服务器同步时间的周期，单位s |
| source\_ip | string | \[1, 16]字符 | 请求报文的源IP地址，置空即可，由系统自动选择。 |
| server\_addr | string | \[1, 64]字符 | sntp服务器的地址 |
| port | port | \[1, 65535] | sntp服务器的端口 |

##### 查询配置

接口

```http
GET v1/sntp/client/config
```

响应

```json
{
    "results": {
        "enable": 1,
        "update_interval": 600,
        "source_ip": "",
        "sntp_servers_list": [
            {
                "server_addr": "0.pool.ntp.org",
                "port": 123
            },
            {
                "server_addr": "1.pool.ntp.org",
                "port": 123
            },
            {
                "server_addr": "2.pool.ntp.org",
                "port": 123
            },
            {
                "server_addr": "3.pool.ntp.org",
                "port": 123
            }
        ]
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | SNTP开关，0关闭，1开启 |
| update\_interval | integer | \[60, 2592000]秒 | SNTP客户端和服务器同步时间的周期，单位s |
| source\_ip | string | \[1, 16]字符 | 请求报文的源IP地址，置空即可，由系统自动选择。 |
| server\_addr | string | \[1, 64]字符 | sntp服务器的地址 |
| port | port | \[1, 65535] | sntp服务器的端口 |

#### NTP 服务器

##### 更新配置

接口

```http
PUT v1/ntp/server/config?autosave=1
```

负载

```json
{
    "enable": 1,
    "master": 2,
    "source_interface": "fastethernet 0/1",
    "source_ip": "",
    "ntp_servers_list": [
        {
            "server_addr": "0.pool.ntp.org",
            "prefer_ntp_server": 1
        },
        {
            "server_addr": "1.pool.ntp.org",
            "prefer_ntp_server": 0
        },
        {
            "server_addr": "2.pool.ntp.org",
            "prefer_ntp_server": 0
        },
        {
            "server_addr": "3.pool.ntp.org",
            "prefer_ntp_server": 0
        }
    ]
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | NTP服务器开关，0关闭，1开启 |
| master | integer | \[2， 15] | NTP服务器层级 |
| source\_interface | string | \[1, 16]字符 | NTP服务器源监听的接口，和source\_ip二选一，配置了一个，另外一个需要为空。 |
| source\_ip | string | \[1, 16]字符 | NTP服务器监听的IP地址，和source\_interface二选一，配置了一个，另外一个需要为空 |
| server\_addr | string | \[1, 64]字符 | NTP服务器地址 |
| prefer\_ntp\_server | integer | \[0， 1] | 是否为主服务器，0否，1是 |

##### 查询配置

接口

```http
GET v1/ntp/server/config
```

响应

```json
{
    "results": {
        "enable": 1,
        "master": 2,
        "source_interface": "fastethernet 0/1",
        "source_ip": "",
        "ntp_servers_list": [
            {
                "server_addr": "0.pool.ntp.org",
                "prefer_ntp_server": 1
            },
            {
                "server_addr": "1.pool.ntp.org",
                "prefer_ntp_server": 0
            },
            {
                "server_addr": "2.pool.ntp.org",
                "prefer_ntp_server": 0
            },
            {
                "server_addr": "3.pool.ntp.org",
                "prefer_ntp_server": 0
            }
        ]
    }
}
```

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | NTP服务器开关，0关闭，1开启 |
| master | integer | \[2， 15] | NTP服务器层级 |
| source\_interface | string | \[1, 16]字符 | NTP服务器源监听的接口，和source\_ip二选一，配置了一个，另外一个需要为空。 |
| source\_ip | string | \[1, 16]字符 | NTP服务器监听的IP地址，和source\_interface二选一，配置了一个，另外一个需要为空 |
| server\_addr | string | \[1, 64]字符 | NTP服务器地址 |
| prefer\_ntp\_server | integer | \[0， 1] | 是否为主服务器，0否，1是 |

### 系统日志

#### 查询日志

接口

```http
GET v1/syslog/view?lines=20
```

> lines=20表示返回最新的20条日志；如果返回全部日志，则传参lines=all

响应

```json
{
    "results": [
        [
            6,
            "Aug  1 18:26:12",
            " ntpd[3063]: 45.76.221.157 local addr 10.5.30.213 -> <null>"
        ],
        [
            6,
            "Aug  1 18:26:12",
            " ntpd[3063]: 202.112.31.197 local addr 10.5.30.213 -> <null>"
        ],
        [
            6,
            "Aug  1 18:26:12",
            " agent[1609]: start ntp server service"
        ],
        [
            5,
            "Aug  1 18:26:12",
            " ntpd[15503]: ntpd 4.2.8p12@1.3728-o Tue Jul 30 03:04:58 UTC 2024 (1): Starting"
        ],
        [
            6,
            "Aug  1 18:26:12",
            " ntpd[15503]: Command line: ntpd -n -c /etc/ntp.conf"
        ],
        [
            6,
            "Aug  1 18:26:12",
            " ntpd[15503]: proto: precision = 3.334 usec (-18)"
        ],
        [
            6,
            "Aug  1 18:26:12",
            " ntpd[15503]: Listen and drop on 0 v6wildcard [::]:123"
        ],
        [
            6,
            "Aug  1 18:26:12",
            " ntpd[15503]: Listen and drop on 1 v4wildcard 0.0.0.0:123"
        ],
        [
            6,
            "Aug  1 18:26:12",
            " ntpd[15503]: Listen normally on 2 lo 127.0.0.1:123"
        ],
        [
            6,
            "Aug  1 18:26:12",
            " ntpd[15503]: Listen normally on 3 eth1 10.5.30.213:123"
        ],
        [
            6,
            "Aug  1 18:26:12",
            " ntpd[15503]: Listen normally on 4 lo [::1]:123"
        ],
        [
            6,
            "Aug  1 18:26:12",
            " ntpd[15503]: Listening on routing socket on fd #21 for interface updates"
        ],
        [
            7,
            "Aug  1 18:37:45",
            " kernel: [10581.266736] rtc-ds1307 0-006f: write secs=46, mins=37, hours=10, mday=1, mon=7, year=124, wday=4"
        ],
        [
            7,
            "Aug  1 18:37:45",
            " kernel: [10581.266757] rtc-ds1307 0-006f: write: c6 37 10 0d 01 08 24"
        ],
        [
            7,
            "Aug  1 18:37:45",
            " kernel: [10581.267396] rtc-ds1307 0-006f: read: c6 37 10 2d 01 28 24"
        ],
        [
            7,
            "Aug  1 18:37:45",
            " kernel: [10581.267416] rtc-ds1307 0-006f: read secs=46, mins=37, hours=10, mday=1, mon=7, year=124, wday=4"
        ],
        [
            7,
            "Aug  1 18:49:23",
            " kernel: [11279.271306] rtc-ds1307 0-006f: write secs=24, mins=49, hours=10, mday=1, mon=7, year=124, wday=4"
        ],
        [
            7,
            "Aug  1 18:49:23",
            " kernel: [11279.271330] rtc-ds1307 0-006f: write: a4 49 10 0d 01 08 24"
        ],
        [
            7,
            "Aug  1 18:49:23",
            " kernel: [11279.271963] rtc-ds1307 0-006f: read: a4 49 10 2d 01 28 24"
        ],
        [
            7,
            "Aug  1 18:49:23",
            " kernel: [11279.271982] rtc-ds1307 0-006f: read secs=24, mins=49, hours=10, mday=1, mon=7, year=124, wday=4"
        ]
    ]
}
```

> 每个数组成员包含三个元素，第一个是日志等级，第二个是日志产生的时间，第三个是具体的日志内容。

#### 更新配置

接口

```http
PUT v1/syslog/config?autosave=1
```

负载

```json
{
    "log_to_remote_enable": 1,
    "history_log_size": 512,
    "history_log_severity": 5,
    "remote_server": [
        {
            "server_addr": "192.168.2.100",
            "server_port": 514
        }
    ],
    "log_to_console": 0
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| log\_to\_remote\_enable | integer | \[0, 1] | 发送到远程日志服务器开关，0关闭，1开启 |
| history\_log\_size | integer | \[64，2048]KB | 历史日志大小 |
| history\_log\_severity | integer | \[0, 7] | 历史日志等级<br/>0：紧急<br/>1：警报<br/>2：严重<br/>3：错误<br/>4：警告<br/>5：通知<br/>6：信息<br/>7：调试 |
| server\_addr | string | \[1, 16]字符 | 远程日志服务器的IP地址 |
| server\_port | integer | \[1, 65535] | 远程日志服务器的端口号 |
| log\_to\_console | integer | \[0，1] | 固定为0 |

### 系统升级

#### 导入固件

接口

```http
POST v1/import/firmware
```

示例

```shell
curl -k -X POST -H "Authorization: Bearer 6nwWSPQ6AEe18L4zi4sbr9SM0xJLI2nE" -F "file=@/home/nowlan/Temp/IG502.bin" https://10.5.30.206/v1/import/firmware
```

响应

```json
{
    "results": "ok"
}
```

#### 设备重启

固件升级到设备上后，需要重启设备才能切换版本。设备重启的api见`重启`-> `手动重启`章节。

### 配置管理

##### 配置自动保存

接口

```http
PUT v1/system/autosave?autosave=1
```

负载

```json
{
    "auto_save": 1
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| auto\_save | integer | \[0, 1] | 自动保存开关，0关闭，1开启 |

##### 配置加密密码

接口

```http
PUT v1/system/encrypt/password?autosave=1
```

负载

```json
{
    "encrypt_passwd": 1
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| encrypt\_passwd | integer | \[0, 1] | 加密明文密码开关，0关闭，1开启 |

##### 查询系统配置

接口

```http
GET v1/system/sysinfo
```

响应

```json
{
    "results": {
        "language": "Chinese",
        "hostname": "EdgeGateway",
        "model_name": "IG502L",
        "oem_name": "inhand",
        "serial_number": "GL5022221013911",
        "feature": "",
        "mac_addr1": "00:18:05:20:ea:ea",
        "mac_addr2": "00:18:05:20:ea:1e",
        "firmware_version": "V2.1.25",
        "bootloader_version": "2017.01.r14382",
        "product_number": "LFA3-D485-IO-W-G",
        "description": "www.inhand.com.cn",
        "auto_save": 1,
        "encrypt_passwd": 0
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| auto\_save | integer | \[0, 1] | 自动保存开关，0关闭，1开启 |
| encrypt\_passwd | integer | \[0, 1] | 加密明文密码开关，0关闭，1开启 |

##### 恢复出厂设置

接口

```http
PUT /v1/system/restore/config
```

负载

```json
{
    "restore_all_data": 1
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| restore\_all\_data | integer | \[0, 1] | 是否清除个人数据，安装的app；0保留，1清除 |

### 设备云平台

#### Inhand Inconect Service

##### 更新配置

接口

```http
PUT v1/inconnect/config?autosave=1
```

负载

```json
{
    "enable": 1,
    "server_addr": "ics.inhandiot.com",
    "tls": 1,
    "register_account": "test@qq.com",
    "https_proxy": "",
    "http_proxy": "",
    "site_name": "",
    "asset_number": "",
    "location_type": 1,
    "lbs_upload_interval": 120,
    "channel_keepalive": 60,
    "dataflow_upload_interval": 3600
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | 是否开启对接Inhand Connect平台功能，0关闭，1开启 |
| server\_addr | string | \[1, 64]字符 | 平台地址 |
| register\_account | string | \[1, 64]字符 | 连接平台的账户，通常是一个邮箱，需要事先在平台注册。 |
| https\_proxy | string | \[1, 64]字符 | 历史遗留字段，置空 |
| http\_proxy | string | \[1, 64]字符 | 历史遗留字段，置空 |
| site\_name | string | \[1, 64]字符 | 历史遗留字段，置空 |
| asset\_number | string | \[1, 64]字符 | 历史遗留字段，置空 |
| location\_type | integer | \[0, 1] | 设备位置定位方法，0使用GPS，1使用蜂窝。需要设备型号支持蜂窝，GPS时才能使用。 |
| lbs\_upload\_interval | integer | \[60, 86400]秒 | 设备位置上报平台的周期，单位秒 |
| channel\_keepalive | integer | \[30, 3600]秒 | 设备和平台之间连接的心跳周期，单位秒 |
| dataflow\_upload\_interval | integer | \[3600, 86400]秒 | 设备蜂窝流量信息上报平台的周期 |

##### 查询配置

接口

```http
GET v1/inconnect/config
```

响应

```json
{
    "results": {
        "enable": 1,
        "server_addr": "ics.inhandiot.com",
        "tls": 1,
        "register_account": "test@qq.com",
        "https_proxy": "",
        "http_proxy": "",
        "site_name": "",
        "asset_number": "",
        "location_type": 0,
        "lbs_upload_interval": 120,
        "channel_keepalive": 60,
        "dataflow_upload_interval": 3600
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | 是否开启对接Inhand Connect平台功能，0关闭，1开启 |
| server\_addr | string | \[1, 64]字符 | 平台地址 |
| register\_account | string | \[1, 64]字符 | 连接平台的账户，通常是一个邮箱，需要事先在平台注册。 |
| https\_proxy | string | \[1, 64]字符 | 历史遗留字段，置空 |
| http\_proxy | string | \[1, 64]字符 | 历史遗留字段，置空 |
| site\_name | string | \[1, 64]字符 | 历史遗留字段，置空 |
| asset\_number | string | \[1, 64]字符 | 历史遗留字段，置空 |
| location\_type | integer | \[0, 1] | 设备位置定位方法，0使用GPS，1使用蜂窝。需要设备型号支持蜂窝，GPS时才能使用。 |
| lbs\_upload\_interval | integer | \[60, 86400]秒 | 设备位置上报平台的周期，单位秒 |
| channel\_keepalive | integer | \[30, 3600]秒 | 设备和平台之间连接的心跳周期，单位秒 |
| dataflow\_upload\_interval | integer | \[3600, 86400]秒 | 设备蜂窝流量信息上报平台的周期 |

##### 查询状态

接口

```http
GET v1/inconnect/status
```

响应

```json
{
    "results": {
        "status": "device_connected"
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| status | string | \[1, 32]字符 | 连接状态 |

#### Inhand Device Manager

##### 更新配置

接口

```http
v1/dm/config?autosave=1
```

负载

```json
{
    "enable": 1,
    "server_addr": "iot.inhand.com.cn",
    "tls": 1,
    "register_account": "test@qq.com",
    "https_proxy": "",
    "http_proxy": "",
    "site_name": "",
    "asset_number": "",
    "location_type": 1,
    "lbs_upload_interval": 120,
    "channel_keepalive": 60,
    "dataflow_upload_interval": 3600,
    "conn_mode": 0
}
```

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | 是否开启对接Inhand Device Manager平台功能，0关闭，1开启 |
| server\_addr | string | \[1, 64]字符 | 平台地址 |
| register\_account | string | \[1, 64]字符 | 连接平台的账户，通常是一个邮箱，需要事先在平台注册。 |
| https\_proxy | string | \[1, 64]字符 | 历史遗留字段，置空 |
| http\_proxy | string | \[1, 64]字符 | 历史遗留字段，置空 |
| site\_name | string | \[1, 64]字符 | 历史遗留字段，置空 |
| asset\_number | string | \[1, 64]字符 | 历史遗留字段，置空 |
| location\_type | integer | \[0, 1] | 设备位置定位方法，0使用GPS，1使用蜂窝。需要设备型号支持蜂窝，GPS时才能使用。 |
| lbs\_upload\_interval | integer | \[60, 86400]秒 | 设备位置上报平台的周期，单位秒 |
| channel\_keepalive | integer | \[30, 3600]秒 | 设备和平台之间连接的心跳周期，单位秒 |
| dataflow\_upload\_interval | integer | \[3600, 86400]秒 | 设备蜂窝流量信息上报平台的周期 |
| conn\_mode | integer |  | 历史遗留字段，置0 |

##### 查询配置

接口

```http
GET v1/dm/config
```

响应

```json
{
    "results": {
        "enable": 1,
        "conn_mode": 0,
        "server_addr": "iot.inhand.com.cn",
        "tls": 1,
        "register_account": "test@qq.com",
        "https_proxy": "",
        "http_proxy": "",
        "site_name": "",
        "asset_number": "",
        "location_type": 1,
        "lbs_upload_interval": 120,
        "channel_keepalive": 60,
        "dataflow_upload_interval": 3600
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | 是否开启对接Inhand Device Manager平台功能，0关闭，1开启 |
| server\_addr | string | \[1, 64]字符 | 平台地址 |
| register\_account | string | \[1, 64]字符 | 连接平台的账户，通常是一个邮箱，需要事先在平台注册。 |
| https\_proxy | string | \[1, 64]字符 | 历史遗留字段，置空 |
| http\_proxy | string | \[1, 64]字符 | 历史遗留字段，置空 |
| site\_name | string | \[1, 64]字符 | 历史遗留字段，置空 |
| asset\_number | string | \[1, 64]字符 | 历史遗留字段，置空 |
| location\_type | integer | \[0, 1] | 设备位置定位方法，0使用GPS，1使用蜂窝。需要设备型号支持蜂窝，GPS时才能使用。 |
| lbs\_upload\_interval | integer | \[60, 86400]秒 | 设备位置上报平台的周期，单位秒 |
| channel\_keepalive | integer | \[30, 3600]秒 | 设备和平台之间连接的心跳周期，单位秒 |
| dataflow\_upload\_interval | integer | \[3600, 86400]秒 | 设备蜂窝流量信息上报平台的周期 |
| conn\_mode | integer |  | 历史遗留字段，置0 |

##### 查询状态

接口

```http
GET v1/dm/status
```

响应

```json
{
    "results": {
        "status": "device_connected"
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| status | string | \[1, 32]字符 | 连接状态 |

#### Inhand Cloud Service

##### 更新配置

接口

```http
PUT v1/devicelive/config?autosave=1
```

负载

```json
{
    "mode": 1,
    "server_addr": "device.inhandcloud.cn",
    "channel_keepalive": 60,
    "config_source": 0
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| mode | integer | \[0, 1] | 对接Inhand iSCADE Cloud的开关，0关闭，1开启 |
| server\_addr | string | \[1, 64]字符 | 平台的地址 |
| channel\_keepalive | integer | \[30, 1200]秒 | 设备和平台之间连接的心跳周期，单位秒 |
| config\_source | integer | \[0, 1] | 固定为0 |

##### 查询配置

接口

```http
GET v1/devicelive/config
```

响应

```json
{
    "results": {
        "mode": 1,
        "server_addr": "device.inhandcloud.cn",
        "channel_keepalive": 60,
        "config_source": 0
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| mode | integer | \[0, 1] | 对接Inhand iSCADE Cloud的开关，0关闭，1开启 |
| server\_addr | string | \[1, 64]字符 | 平台的地址 |
| channel\_keepalive | integer | \[30, 1200]秒 | 设备和平台之间连接的心跳周期，单位秒 |
| config\_source | integer | \[0, 1] | 固定为0 |

##### 查询状态

接口

```http
GET v1/devicelive/status
```

响应

```json
{
    "results": {
        "status": 2
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| status | integer | \[0, 1] | 连接平台的状态<br/>0:  未连接<br/>1：正在连接<br/>2：已连接 |

#### 管理工具

##### web/ssh/telnet更新配置

接口

```http
PUT v1/services/config?autosave=1
```

负载

```json
{
    "https": {
        "enable": 1,
        "listen_ip_addr": "any",
        "port": 443,
        "remote_access": 0
    },
    "telnet": {
        "enable": 1,
        "listen_ip_addr": "any",
        "port": 23,
        "remote_access": 0
    },
    "ssh": {
        "enable": 1,
        "listen_ip_addr": "any",
        "port": 22,
        "timeout": 120,
        "key_mode": 0,
        "key_length": 1024,
        "remote_access": 0
    },
    "web_login_timeout": 300
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| https.enable | integer | \[0, 1] | Web Server开关，0关闭，1开启 |
| https.listen\_ip\_addr | string | \[1, 16]字符 | Web Server监听的地址，可以传any或者接口的IP地址 |
| https.port | integer | \[1, 65535] | Web Server监听的端口号 |
| https.remote\_access | integer | \[0, 1] | 开启远程控制开关，0关闭，1开启 |
| web\_login\_timeout | integer | \[100, 3600] | web空闲超时时间，空闲达到这个值之后，会自动退出登录 |
| telnet.enable | integer | \[0, 1] | Telnet Server开关，0关闭，1开启 |
| telnet.listen\_ip\_addr | string | \[1, 16]字符 | Telnet Server监听的地址，可以传any或者接口的IP地址 |
| telnet.port | integer | \[1, 65535] | Telnet Server监听端口号 |
| telnet.remote\_access | integer | \[0, 1] | 开启远程控制开关，0关闭，1开启 |
| ssh.enable | integer | \[0, 1] | SSH Server开关，0关闭，1开启 |
| ssh.listen\_ip\_addr | string | \[1, 16]字符 | SSH Server监听的地址，可以传any或者接口的IP地址 |
| ssh.port | integer | \[1, 65535] | SSH Server监听端口号 |
| ssh.timeout | integer | \[1, 120] | SSH连接超时时间，空闲达到这个值之后，会自动断开连接 |
| ssh.key\_mode | integer | \[0, 0] | 密钥模式，固定未0，表示RSA |
| ssh.key\_length | integer | 512, 1024, 2048, 4096 | 密钥长度 |
| ssh.remote\_access | integer | \[0, 1] | 开启远程控制开关，0关闭，1开启 |

##### web/ssh/telnet查询配置

接口

```http
GET v1/services/config
```

响应

```json
{
    "results": {
        "https": {
            "enable": 1,
            "listen_ip_addr": "any",
            "port": 443,
            "remote_access": 0
        },
        "telnet": {
            "enable": 1,
            "listen_ip_addr": "any",
            "port": 23,
            "remote_access": 0
        },
        "ssh": {
            "enable": 1,
            "listen_ip_addr": "any",
            "port": 22,
            "timeout": 120,
            "key_mode": 0,
            "key_length": 1024,
            "remote_access": 0
        },
        "web_login_timeout": 300
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| https.enable | integer | \[0, 1] | Web Server开关，0关闭，1开启 |
| https.listen\_ip\_addr | string | \[1, 16]字符 | Web Server监听的地址，可以传any或者接口的IP地址 |
| https.port | integer | \[1, 65535] | Web Server监听的端口号 |
| https.remote\_access | integer | \[0, 1] | 开启远程控制开关，0关闭，1开启 |
| web\_login\_timeout | integer | \[100, 3600] | web空闲超时时间，空闲达到这个值之后，会自动退出登录 |
| telnet.enable | integer | \[0, 1] | Telnet Server开关，0关闭，1开启 |
| telnet.listen\_ip\_addr | string | \[1, 16]字符 | Telnet Server监听的地址，可以传any或者接口的IP地址 |
| telnet.port | integer | \[1, 65535] | Telnet Server监听端口号 |
| telnet.remote\_access | integer | \[0, 1] | 开启远程控制开关，0关闭，1开启 |
| ssh.enable | integer | \[0, 1] | SSH Server开关，0关闭，1开启 |
| ssh.listen\_ip\_addr | string | \[1, 16]字符 | SSH Server监听的地址，可以传any或者接口的IP地址 |
| ssh.port | integer | \[1, 65535] | SSH Server监听端口号 |
| ssh.timeout | integer | \[1, 120] | SSH连接超时时间，空闲达到这个值之后，会自动断开连接 |
| ssh.key\_mode | integer | \[0, 0] | 密钥模式，固定未0，表示RSA |
| ssh.key\_length | integer | 512, 1024, 2048, 4096 | 密钥长度 |
| ssh.remote\_access | integer | \[0, 1] | 开启远程控制开关，0关闭，1开启 |

##### 开发者模式更新配置

接口

```http
PUT v1/python/agent/engine?autosave=1
```

负载

```json
{
    "debug_password": "123456",
    "debug_enable": 1,
    "fixed_passwd": 1,
    "debug_user": "developer"
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| debug\_enable | integer | \[0, 1] | 是否启用开发者模式，0关闭，1开启 |
| debug\_user | string | \[1, 16]字符 | 开发者模式用户名 |
| debug\_password | string | \[1, 32]字符 | 开发者模式密码 |
| fixed\_passwd | integer | \[0, 1] | 是否启用固件密码，0关闭，1启用 |

##### 开发者模式查询配置

接口

```http
GET v1/python/agent/status
```

响应

```json
{
    "results": {
        "app_manager_status": 0,
        "python_sdk": 0,
        "python_engine": 2,
        "python_version": "",
        "sdk_version": "",
        "sdk_version2": "",
        "debug_enable": 1,
        "debug_user": "pyuser",
        "debug_port": "222",
        "fixed_passwd": 1,
        "debug_password": "123456",
        "user_storage_space": 6837583872,
        "user_storage_use": 1826816,
        "extern_storage_card": 0,
        "extern_storage_use": 0,
        "extern_usb_card": 0,
        "extern_usb_use": 0
    }
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| debug\_enable | integer | \[0, 1] | 是否启用开发者模式，0关闭，1开启 |
| debug\_user | string | \[1, 16]字符 | 开发者模式用户名 |
| debug\_password | string | \[1, 32]字符 | 开发者模式密码 |
| fixed\_passwd | integer | \[0, 1] | 是否启用固件密码，0关闭，1启用 |

### 用户管理

##### 添加用户

接口

```http
POST v1/admind/user?autosave=1
```

负载

```json
{
    "privilege": 15,
    "password": "Aa123456",
    "username": "testuser"
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| username | string | \[1, 16] | 新建用户的用户名 |
| password | string | \[1, 32]字符 | 新建用户的密码 |
| privilege | integer | \[1, 15] | 新建用户的权限，数值越大，权限越高 |

##### 删除用户

接口

```http
DELETE v1/admind/user?autosave=1&username=testuser
```

##### 查询用户

接口

```http
GET v1/admind/user
```

响应

```json
{
    "results": [
        {
            "administrator": 1,
            "username": "adm",
            "password": "$1$e6ISIUYb$mRpJoJIIN/rMdHJtPjAoM.",
            "privilege": 15
        }
    ]
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| username | string | \[1, 16] | 用户名 |
| password | string | \[1, 32]字符 | 密码 |
| privilege | integer | \[1, 15] | 用户的权限 |
| administrator | integer | \[0, 1] | 是否为管理员账户，0否，1是 |

### 重启

##### 定时重启

接口

```http
PUT v1/admind/cron/config?autosave=1
```

负载

```json
{
    "cron_job": "reboot",
    "every_hour": 0,
    "week": 0,
    "month": 0,
    "day": 0,
    "hour": 6,
    "minutes": 0,
    "enable": 1
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0, 1] | 是否开启定时重启，0关闭，1开启 |
| cron\_job | string | \[1, 16] | 固定为reboot |
| month | integer |  | 固定为0 |
| week | integer |  | 固定为0 |
| day | integer |  | 固定为0 |
| hour | integer | \[0, 23] | 定时重启对应的小时 |
| minutes | integer | \[0, 59] | 定时重启对应的分钟 |

##### 手动重启

接口

```http
POST v1/system/reboot
```

### 工具

#### ping

##### 执行ping操作

接口

```http
POST v1/system/reboot
```

负载

```json
{
    "host": "www.baidu.com",
    "ping_count": 4,
    "packet_size": 32,
    "expert_options": ""
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| host | string | \[1, 64]字符 | ping探测的目标地址 |
| ping\_count | integer | \[1, 50] | 发送ping报文的个数 |
| packet\_size | integer | \[8, 1472] Byte | ping报文的大小，单位字节 |
| expert\_options | string | \[1, 64] | 高级选项 |

##### 查询ping结果

接口

```http
GET v1/task/status?type=ping
```

响应

```json
{
    "results": {
        "status": "success",
        "data": "PING www.baidu.com (39.156.66.18): 32 data bytes\n40 bytes from 39.156.66.18: seq=0 ttl=49 time=39.385 ms\n40 bytes from 39.156.66.18: seq=1 ttl=49 time=38.668 ms\n40 bytes from 39.156.66.18: seq=2 ttl=49 time=38.324 ms\n40 bytes from 39.156.66.18: seq=3 ttl=49 time=38.605 ms\n\n--- www.baidu.com ping statistics ---\n4 packets transmitted, 4 packets received, 0% packet loss\nround-trip min/avg/max = 38.324/38.745/39.385 ms\n"
    }
}
```

#### traceroute

##### 执行traceroute操作

接口

```http
POST v1/tools/traceroute
```

负载

```json
{
    "host": "www.baidu.com",
    "maximum_hops": 20,
    "timeout": 3,
    "transmit_protocol": 0,
    "expert_options": ""
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| host | string | \[1, 64]字符 | traceroute探测的目标地址 |
| maximum\_hops | integer | \[2, 40] | 最大跳数 |
| timeout | integer | \[2, 10] 秒 | 超时时间，单位秒 |
| transmit\_protocol | string | UDP或ICMP | 协议 |
| expert\_options | string | \[1, 64] | 高级选项 |

##### 查询traceroute结果

接口

```http
GET v1/task/status?type=traceroute
```

响应

```json
{
    "results": {
        "status": "doing",
        "data": "traceroute to www.baidu.com (39.156.66.18), 20 hops max, 38 byte packets\n 1  10.5.30.254 (10.5.30.254)  2.901 ms  1.191 ms  0.728 ms\n 2  *"
    }
}
```

#### tcpdump抓包

##### 执行tcpdump抓包

接口

```http
POST v1/tools/tcpdump
```

负载

```json
{
    "interface": "fastethernet 0/1",
    "capture_number": 20,
    "expert_options": "",
    "action": "capture"
}
```

参数

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| interface | string | \[1, 16]字符 | 基于哪个接口抓包 |
| capture\_number | integer | \[10, 1000] | 抓包个数 |
| action | string | \[1, 16] 字符 | 固定为capture |
| expert\_options | string | \[1, 64] | 高级选项 |
