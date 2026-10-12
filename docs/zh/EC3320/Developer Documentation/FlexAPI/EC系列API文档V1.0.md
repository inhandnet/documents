# EC系列API文档V1.0

## API使用说明

- IEOS提供了一套HTTP API可以进行网络管理和系统管理，用户可以使用curl、Postman等工具或使用代码构建发送HTTP请求管理设备
- API使用了HTTPS协议，因为使用了自签名证书，客户端不需要校验证书，不校验证书的方法如下：
  - curl命令加上`-k`参数
  - Postman需要关闭`SSL certificate verification`
  - ![1742178463272-bac06fda-8921-4a71-ae8f-8f1f0bd8dab5.png](./img/ne4DKz1aucYZ4AOf/1742178463272-bac06fda-8921-4a71-ae8f-8f1f0bd8dab5-158220.png)
- HTTP API端口固定为`9100`，使用时URL需要带上前缀：`https://<IP>:9100`
- 在Linux系统下，你可以使用curl命令来调用API，有关更多curl命令的使用方法：<https://curl.se/docs/>
- 在Windows系统下，你可以使用Postman软件来调用API，Postman使用文档：<https://learning.postman.com/docs/introduction/overview/>

## 获取鉴权

- 在使用所有API前需要先使用用户名和密码登录到设备，获取鉴权token
- URL: `POST /api/v1/login`
- 请求参数：Json字符串
- 在设备外部调用登录API时，需要对用户名和密码进行RSA加密，加密后再使用base64编码
- RSA公钥：

```plain
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqHZd9ULLjVoU2BDkxH/7
HmeVUlEkZrHWPpWHPlBT9prXUk1iNJcPK85OIH2aQDz2GbNIdES7rqOZY/zObHj+
6g/QycW4IhLpAK/zYtvECFW89p/+O58zcM8C66NAbpOCTOnod/nPG0wafd4udJdp
c2Pfo9DQ5A5v4T+K/eyVisKu/gVYsorS3/gDROqlH+VrwnbCWBUZJwWe5I2FIQxb
RSLhhdKeUsrp/T8M+K73rincBWAksCTAYFf+Upn0ufskI/tf8Wn0gNzSuvIAbeo0
YF8+m95jqKMJooI2Zx1SNKS2Dv/3TKLsXiP7D/P0qCvIEREHNr0wWOkixE85Eu4F
8Vn3VWgOzK2Gimq6RJ3HmKxQm/zVcy/weg9/rPSuQ1zF7v9nOsmQc1Taup3pdmSi
osnyHTZDl+feoa0jgQmU5Kb9yojhO/awUlrgTvv/CgLLGCKUyPSgDlf6yHB63N9F
U09PEwu5iRt+M+u2W/69DebfBul1fSLBkt11RbuE5aF3OpbWg5TpqMQbPUzxkZYn
pnbKpX5ut6/66KiE12G5IERUyw7cpZ3qD856VnMmXMZfAFLETEwCPOg+mx92DTSM
dbI5MJM2wTiDEQJjUtfgwoY9zLjbe4HEJP1z7Mn08FHQlu9mu7jTpZHYVRhiVk81
CKanrySex3DNLC9ljlCaGakCAwEAAQ==
-----END PUBLIC KEY-----
```

```json
{
  "username":"base64(RSA(username))",
  "password":"base64(RSA(password))"
}
```

| **Attribute** | **In** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| username | body | string | true | 登录web的用户名 |
| password | body | string | true | 登录web的密码 |

- 注意：以下固件版本调用登录API时使用原始用户名密码：
  - EC5000系列小于V2.0.12
  - EC3320小于V2.0.4
  - EC312小于V2.0.17
  - EC954小于V2.1.9
  - EC942小于V2.0.15
- 响应
  - 登录成功

```json
{
    "result":{
        "token":"84c1760b-e7a9-43aa-9012-27e8d2a36816"
    }
}
```

```
- 登录失败
```

```json
{
  "error":"invalid_parameter",
  "message":"Username or password error"
}
```

- 示例
  - 示例中设备IP为192.168.3.100，用户名为adm，密码为123456
  - Postman
    - 打开Postman，新建一个请求
    - 选择POST方式，输入URL`https://192.168.3.100:9100/api/v1/login`
    - 依次点击Body-raw-JSON，输入`{"username":"IR56j9l1jOwBwbTkqEnbYINSyF5cI9zAArBeYmtHgFyiYeD7lAr5ohG1IB+uUiShz1uYoEmS0tKnE7c0QMFkO60KTcHq02oSQy9rMBRF9gLP7lxL+Lg/RKL5dRtR7ZsT6CCi460TI1jFISA77wojlyRM4sd1ewlxnXiE/d6tfxqo9x0fk6sT6dFKsjLnEvJ81Rd8rPWTfhWqA54BL9S+Vmlr0UGrn3DBrBqmyGHgtt3GycaemJfbnhLjJ0NEyVuAz2JhAhzooaqRZtj7yTtC2ioD+keIfPH5SG2njDVI/elPy3BEVgbPO09EzyKP3+d/CGfxBvoYRWwlE3M5IRULQD2Sq0WChTK81OYA9wI8lwD4ymHXVPkJtqKk7IyDACot1j0ilH/7YVkRxC7wc0rUfsv1KCVp2En/ADr1iMCSl5rxH/vdJLG8FB+cTLnQdVM4T/T3XiD2tUwatIc1xrPczJ6W0dxHov+sxz+T/e1MC3WidgoIgS7J9lvfERKge4whXOEB3BkTfIkuLrFHlwn9KH7LP0IR3XslTPcxH6wT1W4wGPRcsaPleGiS58IBD+g3//dLkt84RExidMYCErgqHgUiB2Ja3Hn7SvySftop/OpWsub7/k0d8urh1yhvlhOf6XkA6IexsPbuTOGn6GwGPVDZ91Vslm69LwpXVmn8RDE=","password":"SIjEk3z8FG0YtgvzvB7Cs7ceDnR1YZiRYl3fVnB9b84gwTAKZ3GGK5Uqz2KA0AU8eT1qBNiyn2pTm48IQLUTg2Kz5DWDv6sFwvFara36iNJxlfxNLGW7XcbUuFHeP2zLnrRLUx+XDMvYNk4naCtF1hHNzBQqGQ9oUMAELChchZlfYJIBM9Du8OpjH7zKkA2wdIZsNtCN4Ld9LME7GeQufGWTTuSoP4FZb74qgmnvplv8/MO0fWlrtwj0j15BSY98GO8+b2teaJLpXdYoUiLwQj12apKMHNJEI7pEEE/0XJ1mee5Adag6tWEh+wfvBr0YEWr1jzT+R3McjvnqdMH7h5f7imRLaDvrxgNTm+ZJ3kb+14+Y4wZMqsI7sTpPO8T1bfCa3u/4ZvG8Q4HReXu74Li5Zk1qpHnXwQYoHSzZsSO0URByDE/jSqbPhsoMLEmJuuMK3xJZsY1msTR0PiKcp5oOKZhbkEGpuxe9xN8neZWDAp04aaMv69Kzm9mGixzqUeDDTt2DTiH8lOq1Fxd9GMxgkt7KYzRTQ9mNTd+fKnTl27fnrm7YgxPXJhlkd2iT0kZojL7RIVkWUnl4lqd5m4MEuVq8CGA2ZdN/KKnEPJRha0lr6FVAzc8HwZyAgarLUbhty9i2h5cfJfGdoWM89VNIGUEa/FjnutMJsRLumkg="}`
    - 点击Send，如果Response中显示了token，则登录成功
    - ![1746585849773-98383fef-8527-45c9-87c7-d6a106699ef2.png](./img/ne4DKz1aucYZ4AOf/1746585849773-98383fef-8527-45c9-87c7-d6a106699ef2-871237.png)
  - curl

```shell
curl -k -X POST \
-H "Content-Type: application/json" \
-d '{"username":"IR56j9l1jOwBwbTkqEnbYINSyF5cI9zAArBeYmtHgFyiYeD7lAr5ohG1IB+uUiShz1uYoEmS0tKnE7c0QMFkO60KTcHq02oSQy9rMBRF9gLP7lxL+Lg/RKL5dRtR7ZsT6CCi460TI1jFISA77wojlyRM4sd1ewlxnXiE/d6tfxqo9x0fk6sT6dFKsjLnEvJ81Rd8rPWTfhWqA54BL9S+Vmlr0UGrn3DBrBqmyGHgtt3GycaemJfbnhLjJ0NEyVuAz2JhAhzooaqRZtj7yTtC2ioD+keIfPH5SG2njDVI/elPy3BEVgbPO09EzyKP3+d/CGfxBvoYRWwlE3M5IRULQD2Sq0WChTK81OYA9wI8lwD4ymHXVPkJtqKk7IyDACot1j0ilH/7YVkRxC7wc0rUfsv1KCVp2En/ADr1iMCSl5rxH/vdJLG8FB+cTLnQdVM4T/T3XiD2tUwatIc1xrPczJ6W0dxHov+sxz+T/e1MC3WidgoIgS7J9lvfERKge4whXOEB3BkTfIkuLrFHlwn9KH7LP0IR3XslTPcxH6wT1W4wGPRcsaPleGiS58IBD+g3//dLkt84RExidMYCErgqHgUiB2Ja3Hn7SvySftop/OpWsub7/k0d8urh1yhvlhOf6XkA6IexsPbuTOGn6GwGPVDZ91Vslm69LwpXVmn8RDE=","password":"SIjEk3z8FG0YtgvzvB7Cs7ceDnR1YZiRYl3fVnB9b84gwTAKZ3GGK5Uqz2KA0AU8eT1qBNiyn2pTm48IQLUTg2Kz5DWDv6sFwvFara36iNJxlfxNLGW7XcbUuFHeP2zLnrRLUx+XDMvYNk4naCtF1hHNzBQqGQ9oUMAELChchZlfYJIBM9Du8OpjH7zKkA2wdIZsNtCN4Ld9LME7GeQufGWTTuSoP4FZb74qgmnvplv8/MO0fWlrtwj0j15BSY98GO8+b2teaJLpXdYoUiLwQj12apKMHNJEI7pEEE/0XJ1mee5Adag6tWEh+wfvBr0YEWr1jzT+R3McjvnqdMH7h5f7imRLaDvrxgNTm+ZJ3kb+14+Y4wZMqsI7sTpPO8T1bfCa3u/4ZvG8Q4HReXu74Li5Zk1qpHnXwQYoHSzZsSO0URByDE/jSqbPhsoMLEmJuuMK3xJZsY1msTR0PiKcp5oOKZhbkEGpuxe9xN8neZWDAp04aaMv69Kzm9mGixzqUeDDTt2DTiH8lOq1Fxd9GMxgkt7KYzRTQ9mNTd+fKnTl27fnrm7YgxPXJhlkd2iT0kZojL7RIVkWUnl4lqd5m4MEuVq8CGA2ZdN/KKnEPJRha0lr6FVAzc8HwZyAgarLUbhty9i2h5cfJfGdoWM89VNIGUEa/FjnutMJsRLumkg="}' \
https://192.168.3.100:9100/api/v1/login
```

```
    * ![1746586458572-92b48025-dbd5-400b-baab-10e2ac405414.png](./img/ne4DKz1aucYZ4AOf/1746586458572-92b48025-dbd5-400b-baab-10e2ac405414-830252.png)
```

- 鉴权使用方式
  - 保存响应中的token值，在其他HTTP API请求中添加请求头：`Authorization: Bearer <token>`
  - curl添加方法：加上参数`-H "Authorization: Bearer <token>"`
  - Postman添加方式：
    - ![1742195301510-d98ae5f3-5417-4b49-9568-fc7f879a8790.png](./img/ne4DKz1aucYZ4AOf/1742195301510-d98ae5f3-5417-4b49-9568-fc7f879a8790-835598.png)

## 内部获取鉴权

- 如果从设备内部访问API，可以直接使用无用户名密码登录接口：
- `GET http://127.0.0.1:9102/api/v1/internal/login`
- ![1746586599437-9c3b15fd-fc8b-480a-b014-87189879bdfe.png](./img/ne4DKz1aucYZ4AOf/1746586599437-9c3b15fd-fc8b-480a-b014-87189879bdfe-904343.png)
- 注意：以下固件版本无此功能：
  - EC5000系列小于V2.0.15
  - EC3320小于V2.0.7
  - EC312小于V2.0.22
  - EC954小于V2.1.10
  - EC942小于V2.0.16

## **系统管理**

### 响应说明

- 以下是调用API一些常见的响应说明
  - 成功一般会返回result为ok，失败会返回失败类型`error`和失败详细信息`message`
- 请求成功

```json
{
    "result": "ok"
}
```

- Token已失败，需要重新登录

```json
{
  "error":"invalid_verify_token",
  "message":"token invalid"
}
```

- 请求的输入参数错误

```json
{
  "error":"invalid_parameter",
  "message":"invalid password"
}
```

- 服务器错误

```json
{
  "error":"internal_error",
  "message":"unexpected EOF"
}
```

### 修改密码

#### 通过API修改密码

```http
PUT /api/v1/user/password
```

- 请求参数：Json

```json
{
  "old":"<old password>",
  "new":"<new password>"
}
```

| **Attribute** | **In** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| old | body | string | true | 当前密码，使用base64编码 |
| new | body | string | true | 新密码，使用base64编码，密码长度为8~128位，且包含大小字母，小写字母，数字，符号中至少3种 |

```
- 注意：小于以下版本号的固件username和password不需要base64编码：
```

| 型号 | 版本号 |
| --- | --- |
| EC5000系列 | V2.0.12 |
| EC3320 | V2.0.4 |
| EC312 | V2.0.17 |
| EC954 | V2.1.9 |
| EC942 | V2.0.15 |

- 响应
  - 成功

```json
{
    "result": "ok"
}
```

- 示例
  - Postman
    - ![1742200481920-b34b24c7-e7d2-402c-87a2-e4f87415eed7.png](./img/ne4DKz1aucYZ4AOf/1742200481920-b34b24c7-e7d2-402c-87a2-e4f87415eed7-248219.png)
  - curl

```http
curl -k -X PUT \
-H "Authorization: Bearer 528843f3-7749-4341-8cc8-1fcc5a7d8c0d" \
-H "Content-Type: application/json" \
-d '{"old":"QWRtaW5AMTIz","new":"UGFzc3dvcmRAMTIz"}' \
https://192.168.3.100:9100/api/v1/user/password
```

```
    * ![1742202715776-bedd9129-8aa9-4bd4-9925-f1f18497329d.png](./img/ne4DKz1aucYZ4AOf/1742202715776-bedd9129-8aa9-4bd4-9925-f1f18497329d-705573.png)
```

#### 通过配置文件修改密码

- 导出配置文件
- 生成密码hash
  - 安装htpasswd工具：`apt install apache2-utils`
  - 生成密码hash：`htpasswd -bnBC 10 "" "password" | tr -d ':'`
- 替换配置文件中的`password`参数
- 导入配置文件

### 状态查询

```http
GET /api/v1/view
```

- **请求参数**
  - 无
- **响应**

```json
{
  "result":{
    "hostname":"edge-computer",
    "model":"EC5350",
    "alias":"",
    "sn":"EC5000000000000",
    "interface":[
      {
        "Name":"eth1",
        "Mac":"00:00:00:AA:AA:AA"
      }],
    "bootLoader":"1.0.0",
    "kernel":"5.15.136-tegra",
    "version":"V1.0.0",
    "cpuLoad":"0.08, 0.07, 0.11",
    "startedAt":"31 minutes",
    "time":"2025-03-14 15:46:50 UTC +08:00",
    "rates":[
      {"usage":815,
        "total":7620,
        "rate":0.11,
        "name":"memory"
      },
      {
        "usage":1.6129032258064515,
        "total":100,
        "rate":0.02,
        "name":"cpu"
      },
      {
        "usage":235,
        "total":102022,
        "rate":0,
        "name":"user"
      }],
    "os":"Ubuntu 22.04.4 LTS"
  }
}
```

- **响应参数说明**

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| hostname | String | 系统的主机名 |
| model | String | 设备型号 |
| sn | String | 设备序列号 |
| bootLoader | String | bootLoader版本号 |
| kernel | String | 内核版本号 |
| version | String | 软件版本号 |
| cpuLoad | String | 分别为过去 1、5 和 15 分钟内可用的系统负载的平均值 |
| startedAt | String | 系统启动时长 |
| time | String | 系统时间 |
| rates | Array | 资源使用率 |
| rates.total | Number | 总量 |
| rates.usage | Number | 已使用 |
| rates.rate | Number | 使用率 |
| rates.name | String | 资源名称<br/>memory：内存<br/>cpu：CPU<br/>user：用户Flash空间 |
| os | String | 系统版本号 |

- **示例**

```shell
curl -k -X GET \
-H "Authorization: Bearer be88eabc-019c-40c2-a0f0-7fd668c20342" \
https://10.5.30.68:9100/api/v1/view
```

```
- ![1741938423162-cf78106d-b174-439d-922e-8d3fa3b5f223.png](./img/ne4DKz1aucYZ4AOf/1741938423162-cf78106d-b174-439d-922e-8d3fa3b5f223-390749.png)
```

### 重启设备

```http
PUT /api/v1/reboot
```

- **请求参数**
  - 无
- **响应**

```json
{
    "result": "ok"
}
```

- **说明**
  - 返回响应数据后设备会立即重启

### 恢复出厂

```http
PUT /api/v1/reset/factory
```

- **请求参数**
  - **无**
- **响应**

```json
{
    "result": "ok"
}
```

- **说明**
  - 会恢复通过IEOS配置的参数，不会删除用户安装的软件等数据

### 重置系统

```http
PUT /api/v1/reset
```

- **请求参数**
  - **无**
- **响应**

```json
{
    "result": "ok"
}
```

- **说明**
  - 会删除用户所有数据，恢复系统到初始状态

### 导出配置

```http
GET /api/v1/config/export
```

- 请求参数：
  - 无
- 响应
  - 配置文件内容
- 示例
  - 获取配置文件并保存到config.json中

```json
curl -k -X GET \
-H "Authorization: Bearer be88eabc-019c-40c2-a0f0-7fd668c20342" \
https://10.5.30.68:9100/api/v1/config/export > config.json
```

```
- ![1741938930606-4c5b483f-497c-4162-aba2-015d5f8162fa.png](./img/ne4DKz1aucYZ4AOf/1741938930606-4c5b483f-497c-4162-aba2-015d5f8162fa-963554.png)
```

- 说明
  - 导出用户通过IEOS配置的参数，格式为json

### 导入配置

```http
PUT /api/v1/config/import
```

- 请求参数：

| **Attribute** | **In** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| file | body | file | true | 配置文件 |

- 响应

```json
{
    "result": "ok"
}
```

- 示例

```json
curl -k -X PUT \
-H "Authorization: Bearer be88eabc-019c-40c2-a0f0-7fd668c20342" \
-F "file=@config.json" \
https://10.5.30.68:9100/api/v1/config/import
```

```
- ![1741939441225-fd07da5f-2083-4aa9-8661-309fc8f39a87.png](./img/ne4DKz1aucYZ4AOf/1741939441225-fd07da5f-2083-4aa9-8661-309fc8f39a87-420163.png)
```

- 说明
  - 导入配置成功后会设备会自动重启

### 获取配置

```http
GET /api/v1/config
```

- 请求参数

| **Attribute** | **In** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| fields | query | string arrays | false | 需要查询的字段，支持多个字段，使用符号","连接<br/>支持的格式：<br/>baseSystem<br/>baseSystem.setting<br/>networkServices.dhcp<br/>networkServices.wifi\_config,networkServices.dhcp |

- 响应

```json
{
  "result":{
    "config":{
      "baseSystem":{
        "setting":{
          "hostname":"edge-computer",
          "zone":"Asia/Shanghai",
          "ntp":{
            "enabled":true,
            "servers":[
              "0.debian.pool.ntp.org:123",
              "1.debian.pool.ntp.org:123",
              "2.debian.pool.ntp.org:123",
              "3.debian.pool.ntp.org:123"
            ],
            "period":3600
          },
          "locale":"zh-CN",
          "disableSSH":false,
          "disableResetKey":true
        }
      }
    }
  }
}
```

- 示例

```json
curl -k -X GET \
-H "Authorization: Bearer bac14114-c77d-4849-81db-7b8dea95acea" \
-F "file=@config.json" \
https://10.5.30.68:9100/api/v1/config?fields=baseSystem.setting
```

```
- ![1741940395223-c27d15a6-5af3-4bf9-86f5-e202e242c241.png](./img/ne4DKz1aucYZ4AOf/1741940395223-c27d15a6-5af3-4bf9-86f5-e202e242c241-466060.png)
```

### 更新配置

```http
PUT /api/v1/config
```

- 请求参数
  - Json字符串，格式参考获取系统配置的响应数据
- 响应

```json
{
  "result": "ok"
}
```

- 示例
  - 以修改hostname为例

```json
curl -k -X PUT \
-H "Authorization: Bearer bac14114-c77d-4849-81db-7b8dea95acea" \
-H "Content-Type: application/json" \
-d '{"baseSystem":{"setting":{"hostname":"test"}}}' \
https://10.5.30.68:9100/api/v1/config
```

```
- ![1741941168158-a8ec4a26-fced-4ea5-8f84-5fa5e861e612.png](./img/ne4DKz1aucYZ4AOf/1741941168158-a8ec4a26-fced-4ea5-8f84-5fa5e861e612-988250.png)
```

## 云服务

### 启动云服务

```http
PUT /api/v1/cloud/on/{region}
```

- 请求参数

| **Attribute** | **In** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| region | url | String | true | 只能为cn或us<br/>cn：国内平台<br/>us：海外平台 |

- 响应

```json
{
    "result": "ok"
}
```

### 停止云服务

```http
PUT /api/v1/cloud/off
```

- 请求参数：
  - 无
- 响应

```json
{
    "result": "ok"
}
```

### 查询云服务状态

```http
GET /api/v1/cloud
```

- 请求参数：
  - 无
- 响应

```json
{
    "result": {
        "enabled": true,
        "region": "cn",
        "status": "offline"
    }
}
```

- 参数说明
  - enabled：功能开启状态
  - region：连接的云平台
  - status：online：在线，offline：离线

## 插件管理

### 插件安装

```http
POST /api/v1/plugin
```

- 请求参数：

| **Attribute** | **In** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| file | body | file | true | 插件安装包，以.tar.gz结尾 |

- 响应

```json
{
    "result": {
        "pkg": {
            "name": "plugin-network-v1.0.1-none-2x3aie8l.tar.gz"
        },
        "metadata": {
            "name": "network",
            "image": "plugin-network.img",
            "tag": "v1.0.1",
            "url_prefix": "network",
            "build_time": "2023-05-29 18:32:20",
            "locales": {
                "en-US": "Networking",
                "zh-CN": "网络设置"
            },
            "menu_index": 2
        }
    }
}
```

### 插件卸载

```http
DELETE /api/v1/plugin/{name}
```

- 请求参数：Json

| **Attribute** | **In** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| name | url | string | true | 插件名称 |
| retain | body | boolen | true | 是否保留数据，默认保留<br/>true-保留<br/>false-不保留 |

- 响应

```json
{
    "result": "ok"
}
```

### 插件列表

```http
GET /api/v1/plugin/list
```

- 请求参数：
  - 无
- 响应

```json
{
    "result": [
        {
            "pkg": {
                "name": "plugin-network-v1.0.1-none-2x3aie8l.tar.gz"
            },
            "metadata": {
                "name": "network",
                "image": "plugin-network.img",
                "tag": "v1.0.1",
                "url_prefix": "network",
                "locales": {
                    "en-US": "Networking",
                    "zh-CN": "网络设置"
                },
                "menu_index": 2
            },
            "startedAt": 1686106880,
            "createdAt": 1686106880
        }
    ]
}
```

```
- 插件列表返回插件基本信息和前端路由配置
```

### 插件运行

```http
PUT /api/v1/plugin/{name}/start
```

- 请求参数：
  - name：插件名称
- 响应
  - 成功

```json
{
    "result": "ok"
}
```

```
- 异常信息：
```

```json
{
 "error": "resource_not_found",
 "message": "Requested plugin network not found",
 "ext": {
  "type": "plugin",
  "value": "network"
 }
}
```

### 插件停止

```http
PUT /api/v1/plugin/{name}/stop
```

- 请求参数：
  - name：插件名称
- 响应

```json
{
    "result": "ok"
}
```

## 网络管理

### 查询网口配置

```http
GET /api/v1/config?fields=networkServices.network.interface
```

- **响应**

```json
{
    "result": {
        "config": {
            "networkServices": {,
                "network": {
                    "interface": {
                        "0001000000000000": {
                            "config-name": "lo",
                            "ifname": "lo",
                            "ipaddr": "127.0.0.1",
                            "netmask": "255.0.0.0",
                            "proto": "static"
                        },
                        "0002000000000000": {
                            "config-name": "eth1",
                            "ifname": "eth1",
                            "ipaddr": "10.5.30.213",
                            "netmask": "255.255.255.0",
                            "proto": "static"
                        },
                        "0003000000000000": {
                            "config-name": "eth2",
                            "ifname": "eth2",
                            "ipaddr": "192.168.4.100",
                            "netmask": "255.255.255.0",
                            "proto": "static"
                        }
                    }
                }
            }
        }
    }
}
```

```
- 字段含义参考`更新网口配置`章节
```

### 更新网口配置

```http
PUT /api/v1/config
```

- **请求参数示例**

```json
{
    "networkServices":{
        "network":{
            "interface":{
                "0002000000000000":{
                    "config-name":"eth1",
                    "ifname":"eth1",
                    "proto":"static",
                    "ipaddr":"10.5.30.213",
                    "netmask":"255.255.255.0"
                }
            }
        }
    }
}
```

**参数说明**

- `networkServices`，`network`，`interface`，`config_id(即示例中的0002000000000000)`，`config-name`以及`ifname`为固定字段，它们的值由厂商负责维护，调用更新网口配置API之前，需要先调用查询网口配置API，获取这些字段的值。`proto`, `ipaddr`和`netmask`字段由客户维护。

| **Attribute** | **Type** | **Required** | **Range** | **Description** |
| --- | --- | --- | --- | --- |
| proto | string | true | | 协议类型；可取值：`static`<br/>, `dhcp` |
| ipaddr | string | true | | 接口IP地址; 当`proto`<br/>为`dhcp`<br/>时，将`ipaddr`<br/>得设置为"" |
| netmask | string | true | | 网络掩码; 当`proto`<br/>为`dhcp`<br/>时，将`netmask`<br/>得设置为"" |

### 查询蜂窝配置

```http
GET /api/v1/config?fields=networkServices.dial
```

- **响应**

```json
{
    "result": {
        "config": {
            "networkServices": {
                "dial": {
                    "debug": 0,
                    "dial_interval": 10,
                    "dualsim_config": {
                        "retries": 3
                    },
                    "enable": 1,
                    "modem_config": {
                        "enable_dualsim": 0,
                        "main_sim": 0,
                        "network_mode": 0,
                        "sim1_pin_code": "",
                        "sim2_pin_code": ""
                    },
                    "netwatcher": {
                        "addr": [],
                        "interval": 60,
                        "is_strict_detect": 0,
                        "retries": 3,
                        "timeout": 5
                    },
                    "profile_config": {
                        "enable_infinitely_redial": 0,
                        "sim1_profile_id": 0,
                        "sim2_profile_id": 0,
                        "sim_profiles": [
                            {
                                "apn": "3gnet",
                                "auth_type": 0,
                                "index": 1,
                                "password": "",
                                "username": ""
                            }
                        ]
                    },
                    "route": {
                        "enable_default_route": 1,
                        "route_metric": 200
                    },
                    "signal_interval": 120
                }
            }
        }
    }
}
```

```
- 字段含义参考`更新蜂窝配置`章节
```

### 更新蜂窝配置

```http
PUT /api/v1/config
```

- **请求参数示例**

```json
{
    "networkServices":{
        "dial":{
            "enable":1,
            "profile_config":{
                "sim_profiles":[
                    {
                        "apn":"3gnet",
                        "auth_type":0,
                        "index":1,
                        "password":"",
                        "username":""
                    }
                ],
                "sim1_profile_id":0,
                "enable_infinitely_redial":1,
                "sim2_profile_id":0
            },
            "modem_config":{
                "network_mode":0,
                "enable_dualsim":1,
                "main_sim":0
            },
            "route":{
                "enable_default_route":1,
                "route_metric":200
            },
            "debug":0,
            "dial_interval":10,
            "signal_interval":120,
            "dualsim_config":{
                "retries":3
            },
            "netwatcher":{
                "addr":[
                    "",
                    ""
                ],
                "interval":60,
                "timeout":5,
                "retries":3,
                "is_strict_detect":0
            }
        }
    }
}
```

- **参数说明**

| **Attribute** | **Type** | **Required** | \*\*Range \*\* | **Description** |
| --- | --- | --- | --- | --- |
| enable | int | true | \[0, 1] | 蜂窝功能使能开关 |
| sim\_profiles | array | true | 10 | 蜂窝网配置候选项，最多10条；每个候选项中包含apn/user/password等信息；拨号的时候从中选择一个；非专网环境可不配置，保留默认的配置即可。最多配置10个数组成员 |
| index | int | true | \[1, 10] | 配置候选项的索引值 |
| apn | string | true | \[1, 128]字符 | apn配置项 |
| username | string | true | \[1, 128]字符 | 用户名配置项 |
| password | string | true | \[1, 128]字符 | 密码配置项 |
| auth\_type | int | true | \[0,  3] | 认证方式；0:  无认证；1：pap，2：chap；3：auto(pap或chap，设备自动选择) |
| sim1\_profile\_id | int | true | \[0, 10] | SIM1卡选择的配置候选项的索引值；0表示使用自动配置；其他值对应sim\_profiles中的index。 |
| sim2\_profile\_id | int | true | \[0, 10] | SIM2卡选择的配置候选项的索引值；0表示使用自动配置；其他值对应sim\_profiles中的index。 |
| enable\_infinitely\_redial | int | true | \[0, 1] | 无限重拨使能开关；默认关闭；当拨号连续失败120次之后，会重启系统来尝试解决拨号失败的问题；针对没有SIM卡的设备，可以开启该选项，开启后，拨号无论失败多少次，都不会重启系统。 |
| enable\_dualsim | int | true | \[0, 1] | 双卡使能开关；默认关闭并使用SIM1卡进行拨号 |
| main\_sim | int | true | \[0, 1] | 开启双卡后，优先拨号选用的SIM卡；只有在开启双卡的情况下才有效；0：SIM1卡；1：SIM2看 |
| dualsim\_config.retries | int | true | \[1, 10] | 开启双卡后，当前SIM卡拨号失败达到retires设定的次数后，切换到另外一张SIM卡进行拨号；默认值3 |
| network\_mode | int | true | \[0, 13] | 网络制式；0：自动；1：GSM；2：WCDMA；3：LTE；4：TD-SCDMA；5：UMTS；6：CDMA；7：HDR；8：CDMA and HDR；9：预留；10：预留；11：5G；12：5G SA；13：5G NSA；这里的网络制式是针对inhand支持的所有模组的，具体的模组只支持其中部分选项 |
| enable\_default\_route | int | true | \[0, 1] | 蜂窝网口默认路由使能开关；开启后，拨号成功后会自动创建一条基于蜂窝网的默认路由 |
| route\_metric | int | true | \[2, 255] | 蜂窝网默认路由的优先级 |
| dial\_interval | int | true | \[1, 3600]s | 重拨间隔；当此次拨号失败后，具体自动开始下次拨号的间隔；默认10s |
| signal\_interval | int | true | \[1, 3600]s | 信号查询间隔；默认120s |
| addr | array | false | 2 | ICMP探测地址，即ICMP探测使能开关；默认关闭；开启探测有助于解决蜂窝网假连接问题，建议客户开启；开启方法为配置至少1个ICMP报文可达的地址；但最多只能配置2个探测地址；关闭方法为删除所有探测地址；当配置2个地址的时候，优先探测第一个地址；第一个地址探测成功，就不会去探测第二个地址； |
| interval | int | true | \[1, 86400]s | 探测间隔；每个interval的时间发送一次ICMP探测报文 |
| timeout | int | true | \[1, 60]s | 探测报文超时时间；当等待timeout时间后仍然未收到探测报文；则触发下一次探测 |
| netwatcher.retries | int | true | \[1, 5] | 探测失败多少次之后，触发重新拨号；如果配置了2个探测地址；每个探测地址都需要失败retries之后，才会触发重新拨号。 |
| is\_strict\_detect | int | true | \[0, 1] | ICMP严格探测使能开关；默认关闭；为了节省用户的蜂窝流量，程序会定期检测蜂窝口接收的报文数量是否发生变化；当蜂窝口接收报文发生变化时，说明网络没有出现假连接；不触发ICMP探测；但如果开启了ICMP严格探测，则无论接口报文是否发生变化，都会按照探测策略进行ICMP探测。 |

### 查询蜂窝状态

```http
GET /network/api/v1/status?service=dial
```

- **响应**

```json
{
    "result": {
        "modem_status": {
            "asu": 57,
            "band": 40039,
            "carrierCode": 46000,
            "carrierString": "CMCC",
            "cellid": "0x3FD4EC2",
            "currentSim": 0,
            "dbm": -83,
            "generation": "4G",
            "iccid": "898600F0221109E25905",
            "imei": "863674046816953",
            "imsi": "460026001115905",
            "lac": "0x8005",
            "modemVersion": "EC20CNHDLGR09A05M1G",
            "netType": "LTE/TDD LTE B39",
            "pci": 68,
            "regStatus": 1,
            "rsrp": -83,
            "rsrq": -9,
            "rssi": -55,
            "sigLevel": 29,
            "sigbar": 4,
            "sinr": -9
        },
        "network_status": {
            "connDuration": 3276,
            "connStatus": 3,
            "dns": "192.168.225.1",
            "gateway": "192.168.225.1",
            "ifaceName": "cellular0",
            "ip": "192.168.225.22",
            "mtu": 1500,
            "netmask": "255.255.255.0"
        }
    }
}
```

- **参数说明**

| **Attribute** | **Type** | **Description** |
| --- | --- | --- |
| asu | int | 信号强度 |
| band | int | band |
| carrierCode | int | plmn |
| carrierString | string | 网络运营商名称 |
| cellid | string | 小区ID |
| currentSim | int | 当前使用的sim卡，0表示使用sim1；1表示使用sim2 |
| dbm | int | 功率信息 |
| generation | string | 第几代蜂窝技术，可能的取值为2G，3G，4G和5G |
| iccid | string | iccid |
| imei | string | imei |
| imsi | string | imsi |
| lac | string | 位置区码 |
| modemVersion | string | 模组的固件版本 |
| netType | string | 网络类型 |
| pci | int | pci |
| regStatus | int | 注网状态；0:未注册, 1: 注册网络成功, 2:正在注册网络, 3:注册网络被拒绝, 4.注册网络失败，原因未知, 5: 漫游成功；6: 拨号关闭，不显示状态 |
| rsrp | int | rsrp |
| rsrq | int | rsrq |
| rssi | int | rssi |
| sigLevel | int | 信号等级，程序内部使用 |
| sigbar | int | 信号个数；最少0格信号，最多5格信号 |
| sinr | int | sinr |
| connDuration | int | 蜂窝连接时长；单位s |
| connStatus | int | 蜂窝连接状态；3：已连接；其他值：未连接 |
| dns | string | 蜂窝网的dns信息 |
| ip | string | 蜂窝接口的ip地址 |
| netmask | string | 蜂窝接口的网络掩码 |
| gateway | string | 蜂窝接口的网关 |
| ifaceName | string | 蜂窝接口的名称 |
| mtu | int | 蜂窝接口的mtu值 |

### 查询GPS配置

```http
GET /api/v1/config?fields=networkServices.gnss
```

- **响应**

```http
{
    "config": {
        "networkServices": {
            "gnss": {
                "enable": 1
            }
        }
    }
}
```

- 参数说明

| **Attribute** | **Type** | **Description** |
| --- | --- | --- |
| enable | int | 开启GPS  1：开始   0：关闭 |

### 更新GPS配置

```http
PUT /api/v1/config
```

- 请求参数示例

```http
{
    "networkServices": {
        "gnss": {
            "enable": 0
        }
    }
}
```

- 响应

```http
{"result":"ok"}
```

### 查询GPS状态

```http
GET /network/api/v1/status?service=gnss_status
```

- 响应

```http
{
    "result": {
        "gnss_status": {
            "enable": 1,
            "latitude": "30 \u00b0 34.523750' N",
            "longitude": "104 \u00b0 4.065930' E",
            "speed": "0.0010 Knots (1knot = 1.852km/h)"
        }
    }
}
```

### 查询Wi-Fi配置

```http
GET /api/v1/config?fields=networkServices.wifi_sta
```

- **响应**

```json
{
    "result": {
        "config": {
            "networkServices": {
                "wifi_config": {
                    "ap_network": {
                        "ap_bandwidth": 3,
                        "ap_channel": 36,
                        "ap_frequency": 1,
                        "ap_max_associations": 128,
                        "ap_radio_type": 8,
                        "ap_ssid": "EdgeComputer-AP",
                        "ap_ssid_broadcast": 1,
                        "auth_method": 1,
                        "encrypt_mode": 4,
                        "ip_addr": "192.168.200.13",
                        "netmask": "255.255.255.0",
                        "wpa_psk_key": "123456789"
                    },
                    "enable": 1,
                    "iface": "wlan0",
                    "sta_network": {
                        "algorithm": 0,
                        "key_mgmt": 2,
                        "psk": "",
                        "route": {
                            "enable_defult_route": 1,
                            "route_metric": 200
                        },
                        "ssid": ""
                    },
                    "station_role": 0
                }
            }
        }
    }
}
```

```
- 参数说明请参考`更新Wi-Fi配置`
```

### 更新Wi-Fi配置

```http
PUT /api/v1/config
```

- **请求参数示例**
  - 关闭WIFI：

```http
{
    "networkServices": {
        "wifi_config": {
            "enable": 0,
            "iface": "wlan0"
        }
    }
}
```

```
- 配置为AP：
```

```http
{
    "networkServices": {
        "wifi_config": {
            "enable": 1,
            "station_role": 0,
            "ap_network": {
                "ap_ssid_broadcast": 1,
                "ap_frequency": 1,
                "ap_radio_type": 8,
                "ap_channel": 36,
                "ap_ssid": "EdgeComputer-AP",
                "auth_method": 1,
                "ap_bandwidth": 3,
                "ap_max_associations": 128,
                "ip_addr": "192.168.100.100",
                "netmask": "255.255.255.0",
                "encrypt_mode": 4,
                "wpa_psk_key": "123456789"
            },
            "iface": "wlan0"
        }
    }
}
```

```
- 配置为STA:
```

```http
{
    "networkServices": {
        "wifi_config": {
            "enable": 1,
            "station_role": 1,
            "sta_network": {
                "ssid": "inhand-visitor",
                "route": {
                    "enable_default_route": 1,
                    "route_metric": 205
                },
                "key_mgmt": 3,
                "algorithm": 0,
                "psk": "inhand@visitor"
            },
            "iface": "wlan0"
        }
    }
}
```

- **请求参数**

| **Attribute** | **Type** | **Required** | **Range** | **Description** |
| --- | --- | --- | --- | --- |
| enable | int | true | \[0, 1] | Wi-Fi Station使能开关 |
| interface | string | true | wlan0 | 接口名称 |
| station\_role | int | true | \[0,1] | 0表示AP   1表示STA |
| ssid | string | true | | 待连接的SSID |
| key\_mgmt | int | true | \[0, 3] | 加密方式；0：无认证；1：WPA-PSK；2：WPA2-PSK； 3. WPA-PSK/WPA2-PSK Mixed |
| algorithm | int | true | \[0, 2] | 加密算法；0：CCMP；1：TKIP；2：CCMP和TKIP |
| psk | string | true | | 待连接的SSID的密码 |
| enable\_default\_route | int | true | \[0, 1] | Wi-Fi接口默认路由使能开关；开启后，Wi-Fi连接成功后会自动创建一条基于Wi-Fi接口的默认路由 |
| route\_metric | int | true | \[2,255] | Wi-Fi默认路由的优先级 |
| | | | | |
| ap\_ssid\_broadcast | int | true | \[0,1] | 是否开启SSID广播 |
| ap\_frequency | int | true | \[0,1] | 0   2.4G   1   5.8G |
| ap\_radio\_type | int  | true | 0/1/2/4/6/7/8/9 | 0   802.11B/G   1   802.11B   2   802.11A   4   802.11G<br/>6   802.11N<br/>7   802.11G/N<br/>8   802.11GA/N/AC<br/>9   802.11B/G/N |
| ap\_channel | int | true | 2.4G：1-11   5.8G：36/40/44/48/149/153/157/161 | 信道 |
| ap\_ssid | string | true | | AP SSID |
| wpa\_psk\_key | string | true | | AP 密码 |
| auth\_method | int | true | \[0-3] | NONE:  0<br/>WPA-PSK: 1<br/>WPA2-PSK: 2<br/>MIXED: 3 |
| encrypt\_mode | int | true | \[3,4] | 3: TKIP   4: AES |
| ap\_bandwidth | int | true | \[0-2] | 0: 20M<br/>1: 40M   2: 80M |
| ap\_max\_associations | int | true | \[1-128] | 最大客户端连接数 |
| ip\_addr | string | true | xx.xx.xx.xx | AP IPV4地址 |
| netmask | string | true | xx.xx.xx.xx | 掩码 |

- 响应

```http
{"result":"ok"}
```

#### 设置DHCP接口地址

- 开启AP后需要下发DHCP信息

```http
PUT /api/v1/config
```

- 请求参数示例

```http
{
    "networkServices": {
        "dhcp": {
            "dhcp": {
                "0007000000000000": {
                    "config-name": "wlan0",
                    "ignore": "",
                    "interface": "wlan0",
                    "leasetime": "6h",
                    "limit": 254,
                    "start": 1
                }
            }
        },
        "network": {
            "interface": {
                "0007000000000000": {
                    "config-name": "wlan0",
                    "ifname": "wlan0",
                    "ipaddr": "192.168.100.100",
                    "netmask": "255.255.255.0",
                    "proto": "static"
                }
            }
        }
    }
}
```

- **请求参数**

| **Attribute** | **Type** | **Required** | **Range** | **Description** |
| --- | --- | --- | --- | --- |
| ipaddr | string | true | xx.xx.xx.xx | AP IPV4地址 |
| netmask | string | true | xx.xx.xx.xx | 掩码 |

- 请在更新WIFI配置返回OK后，下发该接口。仅修改ip和netmask参数，其余参数不变
- 响应

```http
{"result":"ok"}
```

### 执行Wi-Fi扫描

```http
GET /network/api/v1/status?service=wifi_sta_ssid_list
```

- **响应**

```json
{
    "result": {
        "ssids": [
            {
                "bssid": "80:8D:B7:EB:80:90",
                "channel": 161,
                "encryption": "WPA2 PSK (CCMP)",
                "signal": "-67",
                "ssid": "inhand-visitor"
            },
            {
                "bssid": "00:18:05:25:B8:25",
                "channel": 36,
                "encryption": "WPA2 PSK (TKIP, CCMP)",
                "signal": "-75",
                "ssid": "BoxII556"
            }
        ]
    }
}
```

- **参数说明**

| **Attribute** | Type | **Description** |
| --- | --- | --- |
| bssid | string | bssid信息 |
| channel | int | channel信息 |
| encryption | string | 加密方式 |
| signal | string | 信号值 |
| ssid | string | ssid信息 |

### 查询Wi-Fi状态

```http
GET /network/api/v1/status?service=wifi_status
```

- **响应**
  - STA:

```json
{
    "result": {
        "network_status": {
            "connDuration": 3,
            "connStatus": 3,
            "dns": "61.139.2.69 183.221.253.100",
            "gateway": "10.5.60.254",
            "ifaceName": "wlan0",
            "ip": "10.5.60.188",
            "macAderess": "f4:3c:3b:ca:e9:3c",
            "mtu": 1500,
            "netmask": "255.255.255.0",
            "signal": "",
            "stationRole": 1
        }
    }
}
```

```
- AP:
```

```http
{
   "result": {
        "network_status": {
            "Frequency": 0,
            "SSID": "EdgeComputer-AP",
            "authMethod": 2,
            "channel": 36,
            "connStatus": 3,
            "encryptMode": 3,
            "ifaceName": "wlan0",
            "ip": "192.168.200.13",
            "macAderess": "f4:3c:3b:ca:e9:3c",
            "netmask": "255.255.255.0",
            "startDuration": 388,
            "stationRole": 0
        }
    }
}
```

- **参数说明**

| **Attribute** | Type | **Description** |
| --- | --- | --- |
| connDuration | int | Wi-Fi连接时长，单位s |
| connStatus | int | Wi-Fi状态信息；3：已连接；其他值：未连接 |
| ifaceName | string | Wi-Fi接口名称 |
| ip | string | Wi-Fi接口IP地址 |
| netmask | string | Wi-Fi接口网络掩码 |
| gateway | string | 网关信息 |
| mtu | int | 接口MTU值 |
| signal | string | Wi-Fi信号强度 |

- AP部分响应参见更新WIFI配置

### 查询路由配置

```http
GET /api/v1/config?fields=networkServices.network.route,networkServices.network.interface
```

- **响应**

```json
{
    "result": {
        "config": {
            "networkServices": {
                "network": {
                    "route": {
                        "0000657fa834ceea": {
                            "gateway": "10.5.30.254",
                            "interface": "eth1",
                            "metric": 20,
                            "netmask": "0.0.0.0",
                            "target": "0.0.0.0"
                        }
                    }
                }
            }
        }
    }
}
```

- 参数说明请参考`更新路由配置`

### 更新路由配置

```http
PUT /api/v1/config
```

- **请求参数示例**

```json
{
    "networkServices":{
        "network":{
            "route":{
                "0000657fa834ceea":{
                    "interface":"eth1",
                    "target":"0.0.0.0",
                    "netmask":"0.0.0.0",
                    "gateway":"10.5.30.254",
                    "metric":20
                }
            }
        }
    }
}
```

- **请求参数**
  - 配置id `0000657fa834ceea`需要基于以下规则生成：
  - 4位16进制 index 值，1-65535递增。16进制字⺟统⼀⽤⼩写表示
  - 8位16进制时间戳
  - 4位16进制随机值

| **Attribute** | **Type** | **Required** | **Range** | **Description** |
| --- | --- | --- | --- | --- |
| interface | string | true | \[0, 1] | Wi-Fi Station使能开关 |
| target | string | true | | 待连接的SSID |
| netmask | string | true | \[0, 3] | 加密方式；0：无认证；1：WPA-PSK；2：WPA2-PSK； 3. WPA-PSK/WPA2-PSK Mixed |
| gateway | string | true | \[0, 2] | 加密算法；0：CCMP；1：TKIP；2：CCMP和TKIP |
| metric | int | true | | 待连接的SSID的密码 |

### 查询路由状态

```http
GET /network/api/v1/status?service=ipv4_route
```

- 响应

```json
{
    "result": {
        "ipv4_route_neighbor": [
            {
                "interface": "eth1",
                "ip_address": "10.5.30.215",
                "mac_address": "e4:54:e8:d2:1a:be"
            },
            {
                "interface": "wlan0",
                "ip_address": "10.5.62.254",
                "mac_address": "78:17:be:ca:0d:78"
            }
        ],
        "ipv4_route_table": [
            {
                "gateway": "10.5.30.254",
                "interface": "eth1",
                "metric": "20",
                "protocol": "static",
                "table": "main",
                "target": "0.0.0.0"
            }
        ]
    }
}
```

- **参数说明**

| **Attribute** | Type | **Description** |
| --- | --- | --- |
| ipv4\_route\_neighbor.interface | string | IPv4网络邻居信息中邻居属于哪个接口 |
| ipv4\_route\_neighbor.ip\_address | string | IPv4网络邻居信息中的邻居设备的IP地址 |
| ipv4\_route\_neighbor.mac\_address | string | IPv4网络邻居信息中的邻居设备的MAC地址 |
| ipv4\_route\_table.interface | string | IPv4路由表中的接口信息 |
| ipv4\_route\_table.target | string | IPv4路由表中的目标网络 |
| ipv4\_route\_table.gateway | string | IPv4路由表中的下一跳IP地址 |
| ipv4\_route\_table.protocol | string | IPv4路由表项使用的路由协议 |
| ipv4\_route\_table.table | string | IPv4路由表下属于哪个路由表 |
| ipv4\_route\_table.metric | string | IPv4路由表的度量值 |

### 查询DNS配置

```http
GET /api/v1/config?fields=networkServices.dhcp.dnsmasq
```

- **响应**

```json
{
    "result": {
        "config": {
            "networkServices": {
                "dhcp": {
                    "dnsmasq": {
                        "0001000000000000": {
                            "cachesize": 150,
                            "domainneeded": 1,
                            "ednspacket_max": 1500,
                            "expandhosts": 1,
                            "localise_queries": 1,
                            "localservice": 1,
                            "nonwildcard": 0,
                            "rebind_localhost": 1,
                            "rebind_protection": 0,
                            "resolvfile": "/tmp/resolv.conf.auto",
                            "server": [
                                "114.114.114.114",
                                "8.8.8.8"
                            ]
                        }
                    }
                }
            }
        }
    }
}
```

- **参数说明**
  - 用户只需要配置server，其他值是默认值，不建议用户修改。

| **Attribute** | Type | **Description** |
| --- | --- | --- |
| server | array | DNS服务器地址，最多配置5个 |

### 更新DNS配置

```http
PUT /api/v1/config
```

- **请求参数示例**

```json
{
    "networkServices":{
        "dhcp":{
            "dnsmasq":{
                "0001000000000000":{
                    "server":[
                        "114.114.114.114",
                        "8.8.8.8"
                    ]
                }
            }
        }
    }
}
```

- **参数说明**

| **Attribute** | **Type** | **Required** | **Range** | **Description** |
| --- | --- | --- | --- | --- |
| server | array | true | | DNS服务器地址，最多配置5个 |

### 查询域名劫持

```http
GET /api/v1/config?fields=networkServices.dhcp.domain
```

- **响应**

```json
{
    "result": {
        "config": {
            "networkServices": {
                "dhcp": {
                    "domain": {
                        "0000657fb450ee3c": {
                            "ip": "192.168.1.1",
                            "name": "www.test.com"
                        }
                    }
                }
            }
        }
    }
}
```

- **参数说明**
  - `0000657fb450ee3c`是config-id，生成规则如下：
  - 4位16进制 index 值，1-65535递增。16进制字⺟统⼀⽤⼩写表示
  - 8位16进制时间戳
  - 4位16进制随机值

| **Attribute** | Type | **Description** |
| --- | --- | --- |
| name | string | 待劫持的域名 |
| ip | sring | 将域名劫持到该ip地址 |

### 更新域名劫持

```http
PUT /api/v1/config
```

- **请求参数示例**

```json
{
    "networkServices":{
        "dhcp":{
            "domain":{
                "0000657fb450ee3c":{
                    "name":"www.test.com",
                    "ip":"192.168.1.1",
                    "comments":"example"
                }
            }
        }
    }
}
```

- **参数说明**

| **Attribute** | **Type** | **Required** | **Range** | **Description** |
| --- | --- | --- | --- | --- |
| name | string | true | | 待劫持的域名 |
| ip | string | true | | 将域名劫持到IP地址 |
| comments | string | false | | 域名劫持记录的备注说明 |

### 查询DHCP Server配置

```http
GET /api/v1/config?fields=networkServices.dhcp.dhcp
```

- **响应**

```json
{
    "result": {
        "config": {
            "networkServices": {
                "dhcp": {
                    "dhcp": {
                        "0001000000000000": {
                            "config-name": "lo",
                            "ignore": "1",
                            "interface": "lo"
                        },
                        "0002000000000000": {
                            "config-name": "eth1",
                            "ignore": "1",
                            "interface": "eth1",
                            "leasetime": "",
                            "limit": "",
                            "start": ""
                        },
                        "0003000000000000": {
                            "config-name": "eth2",
                            "ignore": "",
                            "interface": "eth2",
                            "leasetime": "1h",
                            "limit": 254,
                            "start": 1
                        }
                    }
                }
            }
        }
    }
}
```

- 参数说明请见`更新DHCP Server配置`

### 更新DHCP Server配置

```http
PUT /api/v1/config
```

- **请求参数示例**

```json
{
    "networkServices":{
        "dhcp":{
            "dhcp":{
                "0003000000000000":{
                    "config-name":"eth2",
                    "interface":"eth2",
                    "ignore":"",
                    "start":1,
                    "limit":254,
                    "leasetime":"6h"
                }
            }
        }
    }
}
```

- **参数说明**
  - `config-id`的值`0003000000000000`由厂商程序生成，更新DHCP Server配置之前，先查询当前的配置，可以到每个接口对应的`config-id`值。

| **Attribute** | **Type** | **Required** | **Range** | **Description** |
| --- | --- | --- | --- | --- |
| config-name | string | true | | 接口名称，不需要更改。 |
| interface | string | true | | 接口名称下对应的物理接口，不需要更改。 |
| ignore | string | true | | 是否开启DHCP Server功能；为"1"时关闭；为""时开启。 |
| start | int | true | | 起始分配机制；接口网段 + start = DHCP server地址池的起始地址； |
| limit | int | true | | 地址池的最大地址数量 |
| leasetime | string | true | | 租期时间；支持1h，6h，12h和24h。 |

### 查询自定义防火墙配置

```http
GET /api/v1/config?fields=networkServices.custom_firewall.rules
```

- **响应**

```json
{
    "result": {
        "config": {
            "networkServices": {
                "custom_firewall": {
                    "rules": [
                        "iptables -t nat -I POSTROUTING -o cellular0 -j MASQUERADE",
                        "iptables -t nat -I POSTROUTING -s 172.17.0.0/16 ! -o docker0 -j MASQUERADE"
                    ]
                }
            }
        }
    }
}
```

### 更新自定义防火墙配置

```http
PUT /api/v1/config
```

- **请求参数示例**

```json
{
    "networkServices":{
        "custom_firewall":{
            "rules":[
                "iptables -t nat -I POSTROUTING -o cellular0 -j MASQUERADE",
                "iptables -t nat -I POSTROUTING -s 172.17.0.0/16 ! -o docker0 -j MASQUERADE"
            ]
        }
    }
}
```

- **请求参数**

| **Attribute** | **Type** | **Required** | **Range** | **Description** |
| --- | --- | --- | --- | --- |
| rules | array | true | | 防火墙规则 |

## 系统升级

### 升级镜像预处理

- 使用md5sum命令计算文件的md5:
  - `md5sum EC312-V2.0.0.img`
  - ![1741675594901-b46059b9-8a6d-454e-bf06-2a23bb5a3660.png](./img/ne4DKz1aucYZ4AOf/1741675594901-b46059b9-8a6d-454e-bf06-2a23bb5a3660-754603.png)
- 使用split命令拆分文件为10M大小的分块
  - `split -b 10M --numeric-suffixes --suffix-length=2 EC312-V2.0.0.img EC312.`
  - ![1741675635291-297fba99-2059-4a2b-81c5-610a95cf299d.png](./img/ne4DKz1aucYZ4AOf/1741675635291-297fba99-2059-4a2b-81c5-610a95cf299d-060849.png)

#### 准备上传

- URL: `POST /api/v1/upgrade/prepare/upload`
- 请求参数：

| **Attribute** | **In** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| md5 | body | string | true | 升级包的md5 |
| name | body | string | true | 升级包名称 |
| upgradeBoot | body | bool | true | 是否升级 bootloader |

- 响应

```json
{
    "result": {
        "md5": "b252322b8d1700fcfb423094e3ed5b26",
        "name": "EC312-V2.0.0.img"
    }
}
```

- 示例：
  - `curl -k -X POST -H "Authorization: Bearer 7327088e-c3c3-479d-b399-384f808d55d4" -H "Content-Type: application/json" -d '{"md5":"b252322b8d1700fcfb423094e3ed5b26","name":"EC312-V2.0.0.img","upgradeBoot":false}' https://10.5.30.191:9100/api/v1/upgrade/prepare/upload`
  - ![1741677611824-46e4af62-5357-4e5e-8b93-23f7e48ae308.png](./img/ne4DKz1aucYZ4AOf/1741677611824-46e4af62-5357-4e5e-8b93-23f7e48ae308-743520.png)

#### 分块上传

- URL: `POST /api/v1/upgrade/chunk/upload`
- 请求参数：

| **Attribute** | **In** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| md5 | query | string | true | 升级包的md5 |
| name | query | string | true | 升级包名称 |
| chunks | query | int | true | 总分块数 |
| chunk | query | int | true | 第几个分块 |
| file | body | binary | ture | 分块内容 |

- 响应

```json
{
    "result": "ok"
}
```

- 示例：
  - `curl -k -X POST -H "Authorization: Bearer 7327088e-c3c3-479d-b399-384f808d55d4" -F "file=@EC312.00" "https://10.5.30.191:9100/api/v1/upgrade/chunk/upload?md5=b252322b8d1700fcfb423094e3ed5b26&name=EC312-V2.0.0.img&chunks=51&chunk=1"`
  - ![1741677723727-7fcab78c-8330-492a-813b-0a6918763064.png](./img/ne4DKz1aucYZ4AOf/1741677723727-7fcab78c-8330-492a-813b-0a6918763064-407063.png)
- 注意：需要按顺序依次传输全部分块文件，不可漏传或重复上传，否则会导致升级失败，需要重新升级

#### 上传完毕

- URL: `PUT /api/v1/upgrade/finish/upload`
- 请求参数：

| **Attribute** | **In** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| md5 | body | string | true | 升级包的md5 |
| name | body | string | true | 升级包名称 |

- 响应

```json
{
    "result": "ok"
}
```

- 示例：
  - `curl -k -X PUT -H "Authorization: Bearer 7327088e-c3c3-479d-b399-384f808d55d4" -H "Content-Type: application/json" -d '{"md5":"b252322b8d1700fcfb423094e3ed5b26","name":"EC312-V2.0.0.img"}' "https://10.5.30.191:9100/api/v1/upgrade/finish/upload"`
  - ![1741678587788-37a9c035-b5b8-4cb1-9ff9-703f3f8876ca.png](./img/ne4DKz1aucYZ4AOf/1741678587788-37a9c035-b5b8-4cb1-9ff9-703f3f8876ca-223516.png)
- 注意：升级完成后系统不会自动重启，需要调用重启API或执行reboot命令重启
