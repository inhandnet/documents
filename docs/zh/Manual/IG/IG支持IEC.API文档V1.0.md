# IG支持IEC.API文档V1.0

## 用户管理

### 获取用户到期信息

```http
GET /v1/admind/userinfo?username={username}
```

响应：

```json
{
  "results": {
    "username":"adm",
    "privilege":15,
    "sys_time":1720432453,
    "last_change":1720432453,
    "expires_days":30 //"0表示永久"
  }
}
```

### 添加用户

```http
POST /v1/admind/user
```

参数：

```json
{
  "privilege":1,
  "password":"Aaa.1234",
  "username":"u2",
  "expires_days":30,
}
```

### 修改用户

```http
PUT /v1/admind/user
```

参数：

```json
{
  "privilege":2,
  "password":"Aaa.1234",
  "username":"u1",
  "expires_days":30
}
```

### 用户列表

```http
GET /v1/admind/user
```

返回：

```json
{
  "results": [
    {
      "administrator": 1,
      "username": "adm",
      "password": "$1$3h1ZJB06$QuJ.JRF5uATkL3b3LpAN4/",
      "privilege": 15,
      "expires_days":30
    },
  ]
}
```

### 获取密码强度

```http
GET /v1/admind/pwquality
```

返回：

```json
{
  "result": {
    "enable":1,
    "minlen":8,
    "dcredit":1,
    "ucredit":1,
    "lcredit":1,
    "ocredit":1
  }
}
```

### 设置密码强度

```http
POST /v1/admind/pwquality
```

参数：

```json
{
    "enable":1,
    "minlen":8,
    "dcredit":1,
    "ucredit":1,
    "lcredit":1,
    "ocredit":1
}
```

### 用户锁定配置

```http
PUT /v1/lockconfuser/lockconf?autosave=1
```

参数：

```http
{
    "enable" : 0/1,  //开关  默认关
    "locktime": 1,  //时间，1-3600S
    "errornum": 5   //错误次数1-10
    "trytime": 6     // 尝试时间窗口 10-60 min
}
```

返回值按获取用户锁定配置返回

### 获取用户锁定配置

```http
GET /v1/lockconfuser/lockconf
```

```http
{
    "results": {
        "enable" : 0/1,  //开关  默认关
        "locktime": 1,  //时间，1-3600S
        "errornum": 5   //错误次数1-10
        "trytime": 6     // 尝试时间窗口 10-60 min
    }
}
```

### 获取用户锁定状态

```http
GET /v1/user/userlockstatus
```

返回：

```http
{
  "results" : ["用户1"，"用户2"]    //这个接口只会返回锁定的用户。没有锁定的用户不会存在返回信息。
}
```

### 解锁用户

```http
PUT /v1/user/unlockuser
```

参数：

```http
{
      "username"："用户1",      //这个接口只能一次一个调用
}
```

返回值：返回获取用户锁定状态

## 防病毒保护

### 扫描

```http
GET /v1/tools/virus/scan
```

返回：

```json
{
  "results":"/bin;/bin/ash;/bin/base64"
}
```

### 验证

```http
POST /v1/tools/virus/check
```

参数：

```json
{
  "file"："/bin/base64"
}
```

返回：

```json
{
  "results":"ok"
}
```

## 系统管理

### 获取系统使用通知

```http
GET /v1/admind/notice
```

返回：

```json
{
  "results":{
    "notice":"XXXXXXXXXXXX"
  }
}
```

### 设置**系统使用通知**

```http
POST /v1/admind/notice
```

参数：

```json
{
  "notice":"XXXXXXXXXXXX"
}
```

### 系统备份

```http
GET /v1/system/backup.bin
```

返回：

```plain
备份文件
```

### **系统还原**

```http
POST /v1/system/restore
```

参数：

```http
备份文件
```

返回：

```json
{
  "results":"ok"
}
```
