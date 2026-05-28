# IG supports IEC.API Documentation V1.0

## User Management

### get user expiration information

```http
GET /v1/admind/userinfo?username={username}
```

response:

```json
{
  "results": {
    "username":"adm",
    "privilege":15,
    "sys_time":1720432453,
    "last_change":1720432453,
    "expires_days":30 //"0 means permanent"
  }
}
```

### add User

```http
POST /v1/admind/user
```

parameters:

```json
{
  "privilege":1,
  "password":"Aaa.1234",
  "username":"u2",
  "expires_days":30,
}
```

### modify User

```http
PUT /v1/admind/user
```

parameters:

```json
{
  "privilege":2,
  "password":"Aaa.1234",
  "username":"u1",
  "expires_days":30
}
```

### user List

```http
GET /v1/admind/user
```

return:

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

### get Password Strength

```http
GET /v1/admind/pwquality
```

return:

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

### set password strength

```http
POST /v1/admind/pwquality
```

parameters:

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

### user Lock Configuration

```http
PUT /v1/lockconfuser/lockconf?autosave=1
```

parameters:

```http
{
    "enable" : 0/1,  //Switch, Default Off
    "locktime": 1,  //Time, 1-3600S
    "errornum": 5   //Error number 1-10
    "trytime": 6     //Try time window 10-60 min
}
```

return Value Return by Get User Lock Configuration

### get User Lockout Configuration

```http
GET /v1/lockconfuser/lockconf
```

```http
{
    "results": {
        "enable" : 0/1,  //Switch, Default Off
        "locktime": 1,  //Time, 1-3600S
        "errornum": 5   //Error number 1-10
        "trytime": 6     //Try time window 10-60 min
    }
}
```

### get user lock state

```http
GET /v1/user/userlockstatus
```

return:

```http
{
  "results" : ["user1"，"user2"]    //This endpoint will only return locked users. No information will be returned for unlocked users.
}
```

### unlock User

```http
PUT /v1/user/unlockuser
```

parameters:

```http
{
      "username"："user1",      //This interface can only be called one at a time.
}
```

return value: Return to obtain the user lock status

## antivirus protection

### scan

```http
GET /v1/tools/virus/scan
```

return:

```json
{
  "results":"/bin;/bin/ash;/bin/base64"
}
```

### validation

```http
POST /v1/tools/virus/check
```

parameters:

```json
{
  "file"："/bin/base64"
}
```

return:

```json
{
  "results":"ok"
}
```

## system Management

### get system usage notifications

```http
GET /v1/admind/notice
```

return:

```json
{
  "results":{
    "notice":"XXXXXXXXXXXX"
  }
}
```

### setup **system Usage Notification**

```http
POST /v1/admind/notice
```

parameters:

```json
{
  "notice":"XXXXXXXXXXXX"
}
```

### System Backup

```http
GET /v1/system/backup.bin
```

return:

```plain
Backing up files
```

### **system Restore**

```http
POST /v1/system/restore
```

parameters:

```http
Backing up files
```

return:

```json
{
  "results":"ok"
}
```
