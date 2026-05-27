# 告警 Webhook 接入文档

**InCloud Service** 提供了 Webhook 功能，帮助您实时接收告警信息。

## 1.配置 Webhook

在 **Incloud Service** 告警规则中注册 Webhook 时，请提供以下信息：

- URL（必填）：请输入您系统中接收告警的 URL 地址，如：[https://yourdomain.com/webhook-endpoint](https://yourdomain.com/webhook-endpoint)。
- 密钥（可选）：如果您希望对请求进行安全验证，可以提供一个密钥。系统将用此密钥对每个告警请求生成签名，以确保请求的安全性。

### 2.Webhook 请求说明

当 **Incloud Service** 生成告警时，将通过 POST 请求将告警信息发送到您配置的 Webhook URL。告警内容将通过 JSON 格式传输，并采用 UTF-8 编码。

请求头：

- <code>Content-Type</code>：<code>application/json</code>
- <code>X-Signature</code>（可选）：如果配置了密钥，<code>X-Signature</code> 头部包含对请求体进行签名的加密值，使用 HMAC 算法生成签名后采用 **Base64** 编码

```python
def verify_signature(data: dict, signature: str, secret: str):
    """验证webhook签名
    :param data: 请求收到的json数据
    :param signature: 请求头headers 中带入的X-Signature 值
    :param secret: 密匙
    """
    payload = json.dumps(data, ensure_ascii=False).encode()
    if not signature:  # 如果没有签名则直接返回True, 不做验签
        return True
    expected_signature = hmac.new(
        secret.encode('utf-8'),
        payload,
        hashlib.sha256
    ).digest()
    expected_signature = base64.b64encode(expected_signature).decode('utf-8')
    return hmac.compare_digest(signature, expected_signature)
```

请求体（告警信息示例）：

```json
{
  "oid": "65e6cd35361ee640b6a04ec7",
  "org": {
    "name": "inhand00356",
    "_id": "65e6cd35361ee640b6a04ec7"
  },
  "app": "nezha",
  "type": "reboot",
  "deviceId": "66ea69ab06eccf714c377403",
  "entityId": "66ea69ab06eccf714c377403",
  "entityName": "EF605231726YKLU",
  "data": {
    "ruleId": "677791e7c0015635b5df77aa",
    "reason": "reboot",
    "serialNumber": "EF605231726YKLU",
    "timestamp": "2025-01-06T10:01:38Z"
  },
  "createdAt": "2025-01-06T10:01:38Z",
  "updatedAt": "2025-01-06T10:01:38Z",
  "ack": false,
  "deviceGroupId": "66ea775522b4cd7a3dda4005",
  "deviceGroup": {
    "name": "605",
    "_id": "66ea775522b4cd7a3dda4005"
  },
  "_id": "677baa025a34db68978609b8"
}
```

字段说明：

| **字段** | **类型** | **说明** |
| :--- | :--- | :--- |
| <code>_id</code> | string | 告警标识 |
| <code>ack</code> | boolean | 是否确认 |
| <code>app</code> | string | 所属平台 |
| <code>content</code> | string | 告警内容 |
| <code>data</code> | object | 告警详细内容 |
| <code>data.serialNumber</code> | string | 告警设备序列号 |
| <code>data.reason</code> | string | 告警类型 |
| <code>data.retention</code> | string | 触发告警的剩余时间（许可证剩余多久产生告警，离线多长产生告警，单位秒） |
| <code>data.timestamp</code> | string | 告警产生时间 |
| <code>deviceId</code> | string | 告警设备id |
| <code>entityId</code> | string | 告警实体 |
| <code>entityName</code> | string | 告警实体名称 |
| <code>entityType</code> | string | 告警实体类型 |
| <code>oid</code> | string | 告警所属机构id |
| <code>org</code> | object | 机构信息 |
| <code>org._id</code> | string | 机构id |
| <code>org.name</code> | string | 机构名称 |
| <code>title</code> | string | 告警标题 |
| <code>type</code> | string | 告警类型，详情见下 |
| <code>updatedAt</code> | date | 告警修改时间 |
| <code>createdAt</code> | date | 告警创建时间 |
| <code>deviceGroupId</code> | string | 设备分组id |
| <code>deviceGroup</code> | object | 分组 |
| <code>deviceGroup._id</code> | string | 分组id |
| <code>deviceGroup.name</code> | string | 分组名称 |
| <code>closedAt</code> | date | 告警关闭时间 |
| <code>status</code> | string | 告警状态（active，closed） |
| <code>priority</code> | int | 告警优先级 |

告警类型：

```plain
connected,连接

disconnected,断开连接

config_sync_failed,配置同步失败

sim_switch,SIM卡切换

local_config_update,本地配置更新

reboot,重启

firmware_upgrade,固件升级

license_expiring,许可证即将过期

license_expired,许可证已过期

uplink_switch,上行链路切换

ethernet_wan_connected,以太网WAN连接

ethernet_wan_disconnected,以太网WAN断开连接

modem_wan_connected,调制解调器WAN连接

modem_wan_disconnected,调制解调器WAN断开连接

wwan_connected,无线WAN连接

wwan_disconnected,无线WAN断开连接

client_connected,客户端连接

client_disconnected,客户端断开连接

cell_operator_switch, 运营商切换

bridge_loop_detect, 环路检测

cell_traffic_reach_threshold,蜂窝流量到达阈值

uplink_status_change, 链路 up/down
```

重试机制：

当发生某些网络错误或请求超时时可能会导致请求失败，系统将自动重试请求，直到达到最大重试次数或成功为止，默认为3次，间隔10秒。

注意：当无法连接到服务时不触发重试，如 DNS 解析错误、服务关闭等。

### 3.推送验证

如果没有配置密钥，您无需验证签名。

如果配置了密钥，您可以按以下步骤验签：

- 计算签名：当您收到 Webhook 请求时，需要使用与配置相同的密钥和算法，重新计算请求体的签名
- 对比签名：比较您计算的签名与请求头中的 X-Signature 值，如果两者匹配，说明请求来自 Incloud Service，您可以放心处理

### 4.请求成功响应

当您的 Webhook 接口成功接收到并处理告警时，应返回 <code>200 OK</code> 状态码。

如果请求处理失败，请返回相应的错误状态码（如 <code>400</code> 或 <code>500</code>），并确保能够正确记录错误信息。

注意事项：

- 强烈建议使用 **HTTPS** 以确保数据传输安全
- 如果配置了密钥，请务必验证 <code>X-Signature</code> 确保请求来源可信
- 确保 Webhook 接口返回 HTTP 200 OK 状态码，表示告警已成功处理

通过上述步骤，您可以高效、安全地接收并处理 **InCloud Service** 的告警 Webhook 事件。
