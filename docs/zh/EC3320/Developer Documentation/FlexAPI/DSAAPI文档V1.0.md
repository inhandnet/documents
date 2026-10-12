# DSA API文档V1.0

## 1 快函数API参考

本章节将介绍网关内部使用的 Python API，它提供了一组功能丰富的接口，使用户能够通过编写 Python 脚本来实现对网关的各种操作和数据处理。本章节会为您提供必要的信息和示例代码，帮助您充分利用产品的功能和性能。

### 1.1 发布测点/告警/自定义等数据到云端（发布快函数）

导入向云端发布数据的API：

```python
from quickfaas.remotebus import publish

publish(topic, payload, qos=1, wizard_data=None, cloud_name="default")
```

参数介绍：

topic: 发布数据的主题

payload: 发布的数据负载

qos: 发布数据的消息等级

wizard\_data：首次推送消息失败，按照wizard\_data指定的topic, payload, qos（如果没有指wizard\_data则使用发送的topic, payload, qos）存入离线缓存，等待连接恢复后按时间顺序上传至MQTT服务器，wizard\_data格式如下：{"topic":`<topic>`, "qos":`<qos>`, "payload":`<payload>`}

cloud\_name：指定发布到哪个云，多云协同使用时可用

配置"发布"快函数时，快函数的传参message有两种格式（根据是否传入wizard\_api决定)

入口函数包含wizard\_api参数，脚本示例如下（默认脚本）

```python
## Enter your python code.
import json
from common.Logger import logger
from quickfaas.remotebus import publish


def main(message, wizard_api, cloudName):
    logger.debug("publish topic:%s, payload: %s, cloudName: %s" % (__topic__, message, cloudName))
    publish(__topic__, json.dumps(message), __qos__, cloud_name=cloudName)
```

传入的message数据格式示例：

```json
{
    "timestamp": 1713498600,
    "timestampMsec": 1713498600121,
    "group_name": "default",
    "values": {
        "Modbus": {
            "word": {
                "raw_data": 22,
                "timestamp": 1713498592,
                "status": 1,
                "timestampMsec": 1713498592261
            }
        }
    }
}
```

入口函数不包含wizard\_api参数，脚本示例如下：

```python
## Enter your python code.
import json
from common.Logger import logger
from quickfaas.remotebus import publish


def main(message, cloudName):
    logger.debug("publish topic:%s, payload: %s, cloudName: %s" % (__topic__, message, cloudName))
    publish(__topic__, json.dumps(message), __qos__, cloud_name=cloudName)
```

传入的message数据格式示例：

```json
{
    "timestamp": 1713498680,
    "timestampMsec": 1713498680121,
    "group": "default",
    "measures": [
        {
            "ctrlName": "Modbus",
            "name": "word",
            "health": 1,
            "timestamp": 1713498672,
            "timestampMsec": 1713498672278,
            "value": 22
        }
    ]
}
```

### 1.2 更新控制器的测点值

#### 1.2.1 write

该接口为同步方式的写值接口，调用后会等到写值响应消息后再返回。

```python
def write(message, timeout=60, cloudName=None)
```

message: 写测点消息，格式如下：

格式1：{"measures1": 12}，测点名称如果重复或者不存在则会抛异常提示写值失败

格式2：{"controller1": {"measures1": 12}}

格式3：\[{"name": "controller1", "measures":\[{"name": "measures1", "value": 12}]}]

timeout: 写测点响应超时时间，默认60S

cloudName：代表哪个云平台调用写指令（用于判定当前云平台下的测点是否被屏蔽或者更名），选填

```python
from common.Logger import logger
from quickfaas.measure import write


def action_name():
    write_request = {"measures1": 12}
    logger.debug('write plc response: %s' % write(write_request))

    write_request = {"controller1": {"measures1": 12}}
    logger.debug('write plc response: %s' % write(write_request))
    
    write_request = [{"name": "controller1", "measures":[{"name": "measures1", "value": 12}]}]
    logger.debug('write plc response: %s' % write(write_request))
```

```json
[
    {
        "device": "controller1", 
        "var_name": "measures1", 
        "result": "OK", # "OK"代表成功，"Failed"代表失败
        "error": "Success"
    }
]
```

```json
[
    {
        "name": "controller1", 
        "measures":[
            {
                "name": "measures1", 
                "error_code": 0, # 0代表成功，非0代表失败
               "error_reason": "Success"
            }
        ]
    }
]
```

#### 1.2.2 write\_plc\_values（推荐）

该接口为异步方式的写值接口，写值响应消息会触发回调函数接口。

```python
def write_plc_values(message, callback=None, userdata=None, timeout=60, cloudName=None)
```

message: 写测点消息，格式如下：

格式1：{"measures1": 12}，测点名称如果重复或者不存在则会抛异常提示写值失败

格式2：{"controller1": {"measures1": 12}}

格式3：\[{"name": "controller1", "measures":\[{"name": "measures1", "value": 12}]}]

callback：写PLC值返回时执行的回调函数，为了兼容DS1.0，callback回调函数也支持三个参数

userdata：传递给回调函数的参数

timeout: 写测点响应超时时间，默认60S

cloudName：代表哪个云平台调用写指令（用于判定当前云平台下的测点是否被屏蔽或者更名），选填

```python
from common.Logger import logger
from quickfaas.measure import write_plc_values


def write_callback(message, userdata):
    logger.debug("write plc response: %s, userdata:%s" % (message, userdata))

def write_callback2(message, userdata, wizard_api):
    logger.debug("write plc response: %s, userdata:%s" % (message, userdata))
    
def action_name():
    write_request = {"measures1": 12}
    write_plc_values(message=write_request, callback=write_callback, userdata="")

    write_request = {"controller1": {"measures1": 12}}
    write_plc_values(message=write_request, callback=write_callback, userdata="")
    
    write_request = [{"name": "controller1", "measures":[{"name": "measures1", "value": 12}]}]
    write_plc_values(message=write_request, callback=write_callback2, userdata="")

    1
```

```json
[
    {
        "device": "controller1", 
        "var_name": "measures1", 
        "result": "OK", # "OK"代表成功，"Failed"代表失败
        "error": "Success"
    }
]
```

```json
[
    {
        "name": "controller1", 
        "measures":[
            {
                "name": "measures1", 
                "error_code": 0, # 0代表成功，非0代表失败
               "error_reason": "Success"
            }
        ]
    }
]
```

### 1.3  召读控制器的测点数据

#### 1.3.1 recall

该接口为同步方式的召读接口，调用后会等到响应消息后再返回。

```python
def recall(names=None, recall_type="measure", timeout=10, realTime=False)
```

names: 召回名称列表

recall\_type: 召回数据类型

"measure": 按照测点召回数据(如果names=\[], 即没指定任何测点名称时，则召回设备上所有测点数据）

"group": 按照测点召回数据(这种模式数据通过组数据消息通道上传）

recall\_type为"measure"时：

None或者\[]，代表获取所有控制器下的所有测点数据

\[{"name": "controller1", "measures": \[]}]，代表获取控制器(controller1)下的所有测点数据

\[{"name": "controller1", "measures": \["measure1", "measure2"]}]，代表获取控制器(controller1)下测点"measure1"和"measure2"的数据

recall\_type为"group"时：

\["group1", "group2"]，代表获取组"group1"和"group2"的数据

timeout: recall测点响应超时时间,默认10秒

realTime：是否读取实时数据，设置为True会立刻重新读取一次recall的测点，并返回最新读取到的值；默认为False，仅recall\_type = "measure" 时有效

```python
from common.Logger import logger
from quickfaas.measure import recall


def action_name():
    # 召回所有控制器下的所有测点数据
    logger.debug('recall all plc measures: %s' % recall())
    
    # 召回控制器(controller1)下的所有测点数据
    logger.debug('recall controller1 plc measures: %s' % recall([{"name": "controller1", "measures": []}]))
    
    # 召回控制器(controller1)下测点"measure1"和"measure2"的数据
    logger.debug('recall controller1 plc measures: %s' % recall([{"name": "controller1", "measures": ["measure1", "measure2"]}]))
    
    # 召回组"group1"和"group2"的数据
    recall(["group1", "group2"], "group")
```

```json
[
      {
          "name": "controller1",
          "health": 1,
          "timestamp": 1582771955,
          "measures":[
              {
                  "name": "measures1",
                  "health": 1,
                  "timestamp": 1582771955,
                  "value": 12
              },
             {
                  "name": "measures2",
                  "health": 1,
                  "timestamp": 1582771955,
                  "value": 1.23
              }
          ]
      }
]
```

#### 1.3.2 recall2（推荐）

该接口为异步方式的召读接口，响应消息会触发回调函数接口。

```python
def recall2(names=None, recall_type="measure", callback=None, userdata=None, timeout=10, realTime=False)
```

names: 召回名称列表

recall\_type: 召回数据类型

"measure": 按照测点召回数据(如果names=\[], 即没指定任何测点名称时，则召回设备上所有测点数据)

"group": 按照测点召回数据(这种模式数据通过组数据消息通道上传)

recall\_type为"measure"时：

None或者\[]，代表获取所有控制器下的所有测点数据

\[{"name": "controller1", "measures": \[]}]，代表获取控制器(controller1)下的所有测点数据

\[{"name": "controller1", "measures": \["measure1", "measure2"]}]，代表获取控制器(controller1)下测点"measure1"和"measure2"的数据

recall\_type为"group"时：

\["group1", "group2"]，代表获取组"group1"和"group2"的数据

callback：召回数据时执行的回调函数，为了兼容DS1.0，callback回调函数也支持三个参数

userdata：传递给回调函数的参数

timeout: recall测点响应超时时间,默认10秒

realTime：是否读取实时数据，设置为True会立刻重新读取一次recall的测点，并返回最新读取到的值；默认为False，仅recall\_type = "measure" 时有效

```python
from common.Logger import logger
from quickfaas.measure import recall2


def recall2_callback(message, userdata):
    logger.debug("recall2 response message: %s, userdata:%s" % (message, userdata))

def recall2_callback2(message, userdata, wizard_api):
    logger.debug("recall2 response message: %s, userdata:%s" % (message, userdata))
    
def action_name():
    # 召回所有控制器下的所有测点数据
    recall2(callback=recall2_callback, userdata="")
    
    # 召回控制器(controller1)下的所有测点数据
    recall2(names=[{"name": "controller1", "measures": []}], callback=recall2_callback, userdata="")
    
    # 召回控制器(controller1)下测点"measure1"和"measure2"的数据
    recall2(names=[{"name": "controller1", "measures": ["measure1", "measure2"]}], callback=recall2_callback2, userdata="")
    
    # 召回组"group1"和"group2"的数据
    recall2(["group1", "group2"], "group")
```

```json
{
    "timestamp": 1589507333.2521989,
    "values": {
        "controller1": {
            "measure1": {
                "raw_data": 12,
               "timestamp": 1582771955,
                "status": 1
            },
            "measure2": {
                "raw_data": 1.23,
               "timestamp": 1582771955,
                "status": 1
            }
        }
    }
}
```

### 1.4 获取全局参数

#### 1.4.1 get

```python
def get()
```

```python
from common.Logger import logger
from quickfaas.global_dict import get


def action_name():
    logger.debug('get global dict: %s' % get())

```

```json
[
    {
        "key": "SN",
        "value": "GL9021025088033"
    }
]
```

#### 1.4.2 get\_global\_parameter

```python
def get_global_parameter()
```

```python
from common.Logger import logger
from quickfaas.global_dict import get_global_parameter


def action_name():
    logger.debug('get global dict: %s' % get_global_parameter()) 

```

```json
{
  "SN": "GL9021025088033"
 }
```

### 1.5 获取控制器连接状态

#### 1.5.1 get\_status

```python
def get_status(controller=None)
```

```python
from common.Logger import logger
from quickfaas.controller import get_status


def action_name():
    logger.debug('controller status: %s' % get_status())

```

```json
[
    {
        "name": "dev1",
        "health": 0,
        "timestamp": 1606784851
    }
]
```

#### 1.5.2 get\_controller\_status

```python
def get_controller_status(controller=None)
```

```json
from common.Logger import logger
from quickfaas.controller import get_controller_status


def action_name():
  logger.debug('controller status: %s' % get_controller_status())
```

```json
 {
  "dev1": {
   "health": 0,
    "timestamp": 1606784851
  }
 }
```

### 1.6 获取云连接状态

导入获取控制器连接状态的API：

```python
def get_status(cloud_name="default")
```

```python
from common.Logger import logger
from quickfaas.clouds import get_status


def action_name():
    logger.debug('cloud connection status: %s' % get_status())

```

返回数据内容：

## 在线返回True

## 离线返回False

### 1.7 获取全局配置

```python
def get(runningConfig=True, timeout=10)
```

```python
from common.Logger import logger
from quickfaas.config import get


def action_name():
    logger.debug('globle config: %s' % get())

```

返回数据内容：

\#全局配置文件信息

### 1.8 设置全局配置

```python
def set(config, timeout=10)
```

```python
from common.Logger import logger
from quickfaas.config import get, set


def action_name():
    global_config = get()

    #Example Modify the global_config configuration

    logger.debug('set config result: %s' % set(global_config))

```

返回数据内容：

\#成功返回：success

\#失败返回：failed

### 1.9 在脚本中读取文件

```python
def faas_read_file(filePath, mode='r', encode='utf-8', size=-1)
```

filePath：文件路径；

mode：mode 决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。和python中open函数接口中的mode参数一致

encode：编码格式，和python中open函数接口中的encoding参数一致，默认为utf-8

size：读取的字节长度，size 未指定则返回整个文件，和python中read函数接口中的size参数一致

```python
## Enter your python code.
import json
from common.Logger import logger
from quickfaas.file import faas_read_file

def main(message):
    try:
        file_path = "/var/user/app/device_supervisor/test.txt"
        data = faas_read_file(file_path, mode='r', encode='utf-8')
        if data:
            logger.info("data: %s" % data)
    except Exception as e:
        logger.error("Exception: %s" % (e))
```

返回数据内容：

\#文件中所有内容的字符串；若出现错误会抛出异常

### 1.10 在脚本中写入文件

```python
def faas_write_file(filePath, mode='w', data='', encode='utf-8')
```

filePath：文件路径；

mode：mode 决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只写 'w'。和python中open函数接口中的mode参数一致

data：需要写入文件的内容（字符串）；默认为空字符串

encode：编码格式，和python中open函数接口中的encoding参数一致，默认为utf-8

```python
## Enter your python code.
import json
from common.Logger import logger
from quickfaas.file import faas_write_file,faas_read_file

def main(message):
    try:
        file_path = "/var/user/app/device_supervisor/test.txt"
        faas_write_file(file_path, mode='w', data="test3", encode='utf-8')
    except Exception as e:
        logger.error("Exception: %s" % (e))
```

返回数据内容：无；若出现错误会抛出异常

### 1.11 兼容DS1 API描述

#### 1.11.1 get\_group

```python
def get_group(self)
```

```python
## Enter your python code.
import json
from common.Logger import logger


def main(message, wizard_api):
    # 获取分组配置
    response = wizard_api.get_group()
    logger.debug("group config:%s" % response)

```

```json
[
    {
        "name": "default",
        "uploadInterval": 10
    },
    {
        "name": "group1",
        "uploadInterval": 10
    }
]
```

#### 1.11.2 update\_group

```python
def update_group(self, group_data)
```

```python
## Enter your python code.
import json
from common.Logger import logger


def main(message, wizard_api):
    # 更新分组配置信息
    group_data = {"group_name":"group1", "upload_interval": 10}
    response = wizard_api.update_group(group_data)
    logger.debug("update group config response:%s" % response)

```

```json
{
  "results": {
    "group_name":"group1",
    "upload_interval": 10
  }
}
```

### 1.12 历史数据库通用API

#### 1.12.1 插入

```python
def insert_request(table_name, insert_data, noack=0, callback=None, userdata=None, timeout=30)
```

参数说明：

table\_name：数据表名称

insert\_data：需要插入到数据库的数据

格式为：{"`<timestamp>`": {"controller1": {"measure1": \[\<measure1\_health>, \<measure1\_value>], "measure2": \[\<measure2\_health>, \<measure2\_value>]}}}

noack：是否需要响应；0：需要响应，1：不需要响应

callback：数据返回的回调函数；可以为None表示不接收返回数据（noack为0时该参数才有意义）

原型：：def insert\_callback(message, userdata)

userdata：回调函数的传参（noack为0时该参数才有意义）

timeout：请求超时时间（默认30秒）

```python
import time
from common.Logger import logger
from quickfaas.LWTSDB import insert_request


def insert_callback(message, userdata):
 logger.debug("%s response message:%s" % (userdata, message))


def action_name():
    insert_data = [
        {str(int(time.time())): {"controller1": {"measure1": [1, 100], "measure2": [1, "test"]}}}
    ]

    #向时序数据库插入一条数据，不需要响应
    insert_request('default', insert_data, 1)

    #向时序数据库插入一条数据，需要响应
    insert_request('default', insert_data, 0, callback=insert_callback, userdata="insert")
    
```

```json
{
  "return_code": 0,
  "return_msg":"okay"
}
```

#### 1.12.2 查找

```python
def query_request(table_name, start_time=None, end_time=None, filter=None, limit=1000, offest=0, callback=None, userdata=None, timeout=30)
```

参数说明：

table\_name：数据表名称

start\_time：开始时间；格式为：%Y-%m-%d %H:%M:%S，如：2023-01-09 12:00:00

end\_time：结束时间；格式为：%Y-%m-%d %H:%M:%S，如：2023-01-09 16:00:00

filter：获取数据的过滤规则(过滤测点名称，设置黑白名单)；格式为：

{"default": "accept\_all", "black\_list": {"controller1": \["measure1", "measure2"]}, "white\_list": {}}

default:

"accept\_all"：默认返回所有测点，黑名单列表中的测点除外；

"deny\_all"：默认所有测点都不返回，白名单列表中的测点除外；

black\_list：黑名单测点名称列表

white\_list：白名单测点名称列表

limit：限制一次获取到记录的最大条目数；

offest：跳过符合记录的记录条数，通常和limit组合使用；

callback：获取数据返回的回调函数

原型：def query\_callback(message, userdata)

userdata：回调函数的传参

timeout：请求超时时间（默认30秒）

备注：

当start\_time字段为None时，表示 TIMESTAMP < end\_time，默认为降序排列

当end\_time字段为None时，表示 TIMESTAMP >= start\_time，默认为升序排列

当start\_time和end\_time同时为None时，表示查询整个数据表，默认为升序排列

```python
from common.Logger import logger
from quickfaas.LWTSDB import query_request


def query_callback(message, userdata):
 logger.debug("%s response message:%s" % (userdata, message))


def action_name():
    #查询default数据表所有数据
    query_request('default', callback=query_callback, userdata="query")

    #查询default数据表数据('2023-01-09 12:00:00'之后的数据)
    query_request('default', '2023-01-09 12:00:00', callback=query_callback, userdata="query")

    #查询default数据表数据('2023-01-09 16:00:00'之后的最新一条数据)
    query_request('default', '2022-12-09 16:00:00', limit=1, callback=query_callback, userdata="query")
    
    # 查询default数据表数据('2023-01-09 16:00:00'之前的数据)
    query_request('default', end_time='2023-01-09 16:00:00', callback=query_callback, userdata="query")
    
    # 查询default数据表数据('2023-01-09 16:00:00'之前的最后一条数据)
    query_request('default', end_time='2023-01-09 16:00:00', limit=1, callback=query_callback, userdata="query")
    
    # 查询default数据表数据(从'2023-01-09 12:00:00'到'2023-01-09 16:00:00')
    query_request('default', '2023-01-09 12:00:00', '2023-01-09 16:00:00', callback=query_callback, userdata="query")
    
    # 查询default数据表数据(从'2023-01-09 12:00:00'到'2023-01-09 16:00:00'，并过滤掉测点名称为"measure1"的测点)
    filter = {"default": "accept_all", "black_list": {"controller1": ["measure1"]}}
    query_request('default', '2023-01-09 12:00:00', '2023-01-09 16:00:00', filter, callback=query_callback, userdata="query")
    
    # 查询default数据表数据(从'2023-01-09 12:00:00'到'2023-01-09 16:00:00'，并只要测点名称为"measure1"的测点)
    filter = {"default": "deny_all", "white_list": {"controller1": ["measure1"]}}
    query_request('default', '2023-01-09 12:00:00', '2023-01-09 16:00:00', filter, callback=query_callback, userdata="query")

```

```json
{
  "total": 1000,
 "offset": 0,
 "size": 100,
  "data":[
    {"1669630340": {"controller1": {"measure1": [1, 100], "measure2": [1, "test1"]}}},
    {"1669630350": {"controller1": {"measure1": [1, 101], "measure2": [1, "test2"]}}}
  ]
}
```

#### 1.12.3 删除

```python
def remove_request(table_name, start_time=None, end_time=None, noack=0, callback=None, userdata=None, timeout=30)
```

参数说明：

table\_name：数据表名称；

start\_time：时序数据的起始时间；当start\_time为None时，表示 TIMESTAMP < end\_time

end\_time：时序数据的截止时间；当end\_time为None时，表示 TIMESTAMP >= start\_time

noack：是否需要响应；0：需要响应，1：不需要响应

callback：数据返回的回调函数；可以为None表示不接收返回数据（noack为0时该参数才有意义）

原型：def remove\_callback(message, userdata)

userdata：回调函数的传参（noack为0时该参数才有意义）

timeout：请求超时时间（默认30秒）

说明：当start\_time和end\_time同时为None时，表示清空整个数据表

```python
from common.Logger import logger
from quickfaas.LWTSDB import remove_request


def remove_callback(message, userdata):
 logger.debug("%s response message:%s" % (userdata, message))


def action_name():
    # 清空时序数据库数据，并且需要响应
    remove_request('default', callback=remove_callback, userdata="remove")

    # 清空时序数据库数据，不需要响应
    remove_request('default', noack=1)
    
    # 删除时序数据库数据(从'2023-01-09 12:00:00'到'2023-01-09 16:00:00')，并且需要响应
    remove_request('default', '2023-01-09 12:00:00', '2022-12-09 16:00:00', 0, callback=remove_callback, userdata="remove")
    
    # 删除时序数据库数据(删除'2023-01-09 16:00:00'以后的数据)，并且需要响应
    remove_request('default', '2023-01-09 16:00:00', callback=remove_callback, userdata="remove")
    
    # 删除时序数据库数据(删除'2023-01-09 16:00:00'以前的数据)，并且需要响应
    remove_request('default', end_time='2023-01-09 16:00:00', callback=remove_callback, userdata="remove")

```

```json
{
  "return_code": 0,
  "return_msg":"okay"
}
```

### 1.13 MQTT SparkPlug B云服务API

#### 1.13.1 发布NBIRTH消息：publish\_node\_online

```python
def publish_node_online(cloud_name, nbirth_pub_metrics=None)
```

参数说明：

cloud\_name：连接成功的云服务名称

nbirth\_pub\_metrics：待发布的自定义metric，格式必须按照：{"云服务名称": {"metric名称": {"value": "具体的值或者是None", "dataType": "metric的数据类型"}}}

#### 1.13.1 发布NDATA消息：SparkPlugB\_publish\_ndata

```python
def SparkPlugB_publish_ndata(pub_metrics=None, cloud_name="default")
```

参数说明：

pub\_metrics：在NDATA消息中待发布的metrics，格式必须按照\[{"name": "metric名称"，"value": None或者是需要上传的实际值}]。（没有"value"字段等同于"value": None）

cloud\_name：发布NDATA消息的云服务名称

#### 1.13.2 订阅NCMD消息：node\_cmd\_handler

```python
def node_cmd_handler(message, cloud_name="default", file_path=None)
```

参数说明：

message：订阅到的NCMD消息

cloud\_name：云服务名称

file\_path：保存更新后的metric文件路径。

### 1.14 获取全局变量

导入获取全局变量的API：

from quickfaas.global\_variables import get

API原型：

```python
def get(key=None)
```

脚本示例如下：

```python
from common.Logger import logger
from quickfaas.global_variables import get


def action_name():
    logger.debug('globle variables: %s' % get())
```

返回数据内容：

传参key为空时返回所有全局变量对应的值

传参key不为空时返回指定key对应的值

### 1.15 设置全局变量

导入获取全局变量的API：

from quickfaas.global\_variables import set

API原型：

```python
def set(key, value)
```

脚本示例如下：

```python

from quickfaas.global_variables import set


def action_name():
    set("key", "value")
```

### 2 内部MQTT消息总线

本章节将介绍网关内部消息总线的重要 topic 和 Payload。通过阅读本章节，可以了解以及如何利用特定的 topic 和 Payload 实现数据的传输和处，这将有利于更加灵活地使用网关功能。

### 2.1 连接内部MQTT Broker

#### 2.1.1 EC系列设备

MQTT服务器地址：127.0.0.1

端口号：9105

用户名：inhand

密码：inhand

在测点监控里创建添加一个控制器和测点。如图所示：

![1717381296907-c959c92d-9c61-449f-b560-7d827617d89b.png](./img/WyPIJ-P8oa9ASDB-/1717381296907-c959c92d-9c61-449f-b560-7d827617d89b-005302.png)

添加完控制器和测点后，进入EC设备后台，在后台安装mosquitto。执行如图所示命令：

![1717381621742-403eb8cf-39fd-4f44-8613-4cd5a5b418eb.png](./img/WyPIJ-P8oa9ASDB-/1717381621742-403eb8cf-39fd-4f44-8613-4cd5a5b418eb-051200.png)

安装后，执行如图所示命令，订阅driverServiceId为2000的driver发布的测点消息：

![1717381666042-8173a777-35c4-4db6-8e1f-50681bb4aa2c.png](./img/WyPIJ-P8oa9ASDB-/1717381666042-8173a777-35c4-4db6-8e1f-50681bb4aa2c-244060.png)

#### 2.1.2 IG系列设备

MQTT服务器地址：127.0.0.1

端口号：9009

在测点监控里创建一个控制器和测点，如图所示：

![1717381115219-3a08db94-f4cd-40db-84b8-c6f6ac427e49.png](./img/WyPIJ-P8oa9ASDB-/1717381115219-3a08db94-f4cd-40db-84b8-c6f6ac427e49-885917.png)

进入IG系列设备后台执行如下命令后可以订阅到driverServiceId为2000的driver发布的测点消息

![1717381002296-f8ecf158-e010-4c36-b38f-635208aedf9a.png](./img/WyPIJ-P8oa9ASDB-/1717381002296-f8ecf158-e010-4c36-b38f-635208aedf9a-533103.png)

### 2.2 南向消息

#### 2.2.1 driver发布控制器测点采集值

```plain
ds2/eventbus/south/read/{driverServiceId} 
```

{driverServiceId}：当前driver的ServiceId，可在日志中查看当前driver的ServiceId。

下图是展示的启用的ModbusDriver如何查看ServiceId（注意：ModbusDriver不是固定是2000，根据启用控制器的顺序不同，ServiceId也不同。实际的driverServiceId请以日志中显示的ServiceId为准）：

![1715753976197-e8439cc8-1f1d-4f78-8cab-61660a06cdc4.png](./img/WyPIJ-P8oa9ASDB-/1715753976197-e8439cc8-1f1d-4f78-8cab-61660a06cdc4-739460.png)

```json
{
    "controllers": [
        {
            "name": "con1",
           "version": "d3b0c5fc05cb72e7759c95f346e29f8d",
            "health": 1,
            "timestamp": 1582771955,
            "measures":[
                {
                    "name": "measures1",
                    "health": 1,
                    "timestamp": 1582771955,
                    "timestampMsec": 1582771955000,
                    "value": 12
                }
            ]
        }
    ]
}
```

controllers里的name：控制器名称

version：控制器配置版本信息(虚拟控制器可以不要该字段)

controllers里的health：控制器健康状态，1 --正常，0 --异常

timestamp：控制器健康状态更新的秒级时间

timestampMsec：控制器健康状态更新的毫秒级时间

measures里的name：测点名称

measures里的health：测点健康状态，1 --正常，0 --异常

timestamp：查询操作Unix时间戳

value：测点值

#### 2.2.2 driver发布毫秒级数据信息

```plain
ds2/eventbus/south/upload/msec/data/{controllerName} 
```

{controllerName}：为发布毫秒级数据的控制器名称

```json
[
  {
    "controller":["con1", 1, 1646910377],
    "measure": {
      "mea1": [1, 100],
      "mea2": [1, 100]
    }
  },
 {
    "controller":["con1", 1, 1646910377],
    "measure": {
      "mea1": [1, 100],
      "mea2": [1, 100]
    }
  }
]
```

controller数据：controller\[0]代表控制器名称，controller\[1]代表控制器健康状态，controller\[2]代表采集时间戳

measure数据：key代表测点名称，measure\[0]代表测点健康状态，measure\[1]代表测点的值

#### 2.2.3 向driver写测点值

```plain
ds2/eventbus/south/write/{requestServiceId}
```

{requestServiceId}：消息发布者，DataHub的ServiceId为1010

```json
{
  "msg_id": 43461834341,
  "timestamp": 1610335020088,
  "payload": [
    {
        "name": "con1",
        "measures":[
            {
                "name": "measures1",
                "value": 12
            }
        ]
    }
 ]
}
```

msg\_id： 消息ID

timestamp： 时间戳

payload里的name：控制器名称

measure里的name：测点名称

value：测点值

#### 2.2.4 driver返回写测点值结果

```plain
ds2/eventbus/south/write/{requestServiceId}/response
```

{requestServiceId}：消息发布者，DataHub的ServiceId为1010

```json
{
  "msg_id": 43461834341,
  "timestamp": 1610335020088,
  "payload": [
    {
        "name": "con1",
        "measures":[
            {
                "name": "measures1",
               "value": 12,
                "error_code": 0,
               "error_reason": ""
            }
        ]
    }
 ]
}
```

msg\_id： 消息ID

timestamp： 时间戳

payload里的name：控制器名称

measure里的name：测点名称

value：测点值

error\_code： 0:成功，1：写入失败

error\_reason：错误原因描述

#### 2.2.5 Modbus广播写

```plain
ds2/eventbus/south/modbus/broadcast/write
```

```json
{
 "protocol": "Modbus-RTU",
 "endpoint": "rs485",
 "slave": 1,
 "registers": [
    {
      "function": 1,
      "address": 100,
      "length": 1,
      "value": ""
    }
  ]
}
```

protocol： 通讯协议，Modbus-RTU/Modbus-TCP

endpoint：串口/IP地址

slave：从站地址

function： 功能码

address： 地址

length： 长度

value： 需要写入寄存器的值，base64编码

### 2.3 北向消息

#### 2.3.1 发布测点分组数据，包含分组内所有测点

```plain
ds2/eventbus/north/measures/{groupName}
```

{groupName}：分组名

```json
{
    "group": "group_aaa", 
    "measures":[
      {
        "ctrlName": "con1",
        "name": "measures1",
        "health": 1,
        "timestamp": 1582771955,
        "timestampMsec": 1582771955000,
        "value": 12,
      }
    ]
}
```

group：上传消息分组

name：测点名称

health：0 测点离线，1测点在线

timestamp：数据上报时刻的秒级时间戳

timestampMsec：数据上报时刻的毫秒级时间戳

value：测点值

#### 2.3.2 发布测点分组数据，仅包含分组内数值变化的测点

```plain
ds2/eventbus/north/changed/measures/{groupName}
```

{groupName}：分组名

```json
{
    "group": "group_aaa",
    "measures":[
      {
        "ctrlName": "con1",
        "name": "measures1",
        "health": 1,
        "timestamp": 1582771955,
        "timestampMsec": 1582771955000,
        "value": 12,
      }
    ]
}
```

group：上传消息分组

name：测点名称

health：0 测点离线，1测点在线

timestamp：数据上报时刻的秒级时间戳

timestampMsec：数据上报时刻的毫秒级时间戳

value：测点值

#### 2.3.3 发布告警触发/消除事件消息

```plain
ds2/eventbus/north/alarm/{alarmName}
```

{alarmName}：告警名称

```json
{
  "name": "alarm1",
  "ctrlName": "",
  "measureName": "",
  "priority": 1,
  "timestamp": 1234646484,
  "timestampMsec": 1582771955000,
  "status": 0,
  "value": 60,
  "alarm_value": 60,
  "content": "DATA IS OUT OF RANGE"
}
```

name：告警名称

ctrlName：控制器名称

measureName：测点名称

priority：内置好的告警等级，最大可支持定义5个级别 取值范围\[1,5]

timestamp：秒级时间戳

timestampMsec：毫秒级时间戳

status：0:解除告警 1:触发告警

value：当前测点值

alarm\_value：告警触发时测点值

content：描述

#### 2.3.4 控制器状态更新消息上报

```plain
ds2/eventbus/north/controllers/delta
```

```json
[
  {
    "name": "dev1",
    "health": 0,
    "timestamp": 1606784851
  }, 
  {
    "name": "dev2",
    "health": 1,
    "timestamp": 1606784852
  }
]
```

name：控制器名称

health：0设备离线， 1设备在线

timestamp：控制器状态更新时刻的Unix时间戳

#### 2.3.5 更新控制器测点值（写PLC值）

```plain
ds2/eventbus/north/write/measures
```

```json
{
  "task_id": 43461834341,
  "controllers": [
    {
        "name": "con1",
        "measures":[
            {
                "name": "measures1", 
                "value": 12
            },
            {
                "name": "measures2",
                "value": 13
            }
        ]
    }
 ]
}
```

task\_id：任务ID

controllers里的name：控制器名称

measures里的name：测点名称

value：值

#### 2.3.6 响应控制器测点写值

```plain
ds2/eventbus/north/write/measures/response
```

```json
{
   "task_id": "43461834341",
  "controllers": [
    {
        "name": "con1",
        "measures":[
            {
                "name": "measures1",
                "error_code": 0,
                "error_reason": ""
            },
            {
                "name": "measures2",
                "error_code": 1,
                "error_reason": "write failed"
            },
        ]
    }
 ]
}
```

task\_id：任务ID

controllers里的name：控制器名称

measures里的name：测点名称

error\_code：0:成功，1：写入失败

error\_reason：错误原因描述

#### 2.3.7 数据召读

主动获取控制器测点值（召唤数据）。

```plain
ds2/eventbus/north/recall/measures
```

```json
{
  "task_id": "43461834341",
  "recallType": "group",
  "groups": ["group_name_1"],
  "controllers": [
    {
      "name": "ctrl1",
      "measures": ["measure_name_1"]
    }
  ]
}
```

task\_id：任务ID，仅"recallType" == "measure"有效

recallType：支持group, measure

当"recallType" == "group"时测点数据通过ds2/eventbus/north/measures/{groupName}上传，内容见测点分组上报。

当"recallType" == "measure"时测点数据通过ds2/eventbus/north/recall/measures/response上传，此时会获取最后一次轮询到的测点值，内容如下：如果controllers == \[]，即没指定测点名称

当"recallType" == "realtime"时测点数据通过ds2/eventbus/north/recall/measures/response上传，此时会实时轮询一次所有召读的测点，内容如下：如果controllers == \[]，即没指定测点名称

groups：测点组列表，仅"recallType" == "group"有效。

controllers：控制器列表，仅"recallType" == "measure"有效。测点总数需要限制，具体值待定。

name：控制器名称

measures：测点列表

#### 2.3.8 响应数据召读

仅当"recallType" == "measure"时。

```plain
ds2/eventbus/north/recall/measures/response
```

```json
{
  "task_id": "43461834341",
  "recallType": "measure",
  "controllers": [
      {
          "name": "con1",
          "health": 1,
          "timestamp": 1582771955,
          "measures":[
              {
                  "name": "measures1",
                  "health": 1, 
                  "timestamp": 1582771955,
                  "value": 12
              }
          ]
      }
  ]
}
```

task\_id：任务ID

recallType：measure

controllers里的name：设备名称

controllers里的health：设备健康状态，1 -- 设备正常，0 -- 设备异常

controllers里的timestamp：设备健康状态更新时间

measures里的name：变量名称

measures里的health：0 -- measure查询失败(rawbytes字段无效)，1 -- measure查询成功

measures里的timestamp：查询操作Unix时间戳

value：值

### 2.4 系统消息

#### 2.4.1 云连接状态更新

```plain
ds2/eventbus/system/cloud/connection/notice
```

```json
{
  "cloud_name": "name",
  "status": 2,               
  "timestamp": 1614735490  
}
```

cloud\_name：上传消息分组

status：连接状态。0未启用，1连接中，2连接成功，3未知错误，4注册中，5已注册

timestamp：状态变化时刻的时间戳

### 2.5 历史数据库

历史数据库是映翰通系列边缘计算网关上的一个轻量级时序数据库。它包含如下功能：

- DSA可以为测点分组创建数据表，并把分组数据按指定的存盘策略存入数据库；（通过Web配置）
- 快函数或其他数据分析程序，可以通过网关内部MQTT消息总线查询/插入/删除历史数据

#### 2.5.1 插入请求

```plain
insert/req/<table_name>/<client_id>/<operation_id>
```

\<table\_name>：操作的数据表名称（也就是分组名称）；

\<client\_id>: 数据库客户端ID，用于区分不同的客户端。每个客户端只应订阅属于自己ID的数据库消息。

- \<client\_id>的建议格式为`ext-<MAC>-<pid>`

\<operation\_id>：数据库操作ID，用于区分某一次请求操作，由客户端生成，建议使用UUID

```json
{
  "noack": 0,
  "data":[
    {"<timestamp>": {"controller1": {"measure1": [<measure1_health>, <measure1_value>], "measure2": [<measure2_health>, <measure2_value>]}}}
  ]
}
```

noack：0代表需要响应；1代表不需要响应（当请求payload中没有noack字段时，默认为0）

data：插入的数据，支持多条插入

| 参数 | 说明 |
| :--- | :--- |
| timestamp | 插入数据时的时间戳(单位秒) |
| controller1 | 控制器名称 |
| measure1 | 测点名称 |
| measure1\_health | 测点健康状态(0:离线，1在线) |
| measure1\_value | 该时刻测点的值 |

#### 2.5.2 插入响应

插入请求payload的noack为0时才会收到插入响应。

```plain
insert/rsp/<table_name>/<client_id>/<operation_id>
```

请求Topic参数说明：同插入请求报文定义。

```json
{
  "return_code": 0,
  "return_msg":"okay"
}
```

#### 2.5.3 查询请求

```plain
query/req/<table_name>/<client_id>/<operation_id>
```

请求Topic参数说明：同插入请求报文定义。

```json
{
  "start_time": 1669696164, 
  "end_time": 1669696264, 
  "filter": {
    "default": "accept_all", 
    "black_list": {"controller1": ["measure1", "measure2"]}, 
    "white_list": {}, 
  },
  "limit": 1000,
  "offset": 0
}
```

参数说明：

| 参数 | 数据类型 | 参数说明 | 举例 |
| --- | --- | --- | --- |
| start\_time | INTEGER<br/> | INTEGER：时序数据的起始时间，单位秒，包含start\_time.<br/><br/>当start\_time字段为负数或不存在时，表示 TIMESTAMP < end\_time，默认为降序排列 | 1669696164 |
| end\_time | INTEGER<br/> | 时序数据的截止时间，单位秒，不包含end\_time。<br/><br/>当end\_time字段为负数或不存在时，表示 TIMESTAMP >= start\_time，默认为升序排列 | 1669697264 |
| filter.default | ENUM | "accept\_all"：默认返回所有测点，黑名单列表中的测点除外；<br/> "deny\_all"：默认所有测点都不返回，白名单列表中的测点除外； | "filter": {<br/>    "default": "deny\_all",<br/>    "white\_list": {"controller1": ["measure1", "measure2"]}<br/>  } |
| filter.black\_list | STRING  ARRAY | 黑名单测点名称列表 | |
| filter.white\_list | STRING  ARRAY | 白名单测点名称列表 | |
| limit | INTEGER | 如果你需要在LwTSDB中读取指定数量的数据记录，可以使用LwTSDB的Limit方法，limit方法接受一个数字参数，该参数指定从LwTSDB中读取的记录条数。如果你们没有指定limit方法(或者limit为0)中的参数则显示集合中的所有数据。<br/><br/>LwTSDB本身限制最大读取数量为xxxx条，当预测查询数量超过限制时，建议查询应用按时间段分次查询。 | limit:100 |
| offset | INTEGER | 可以使用offset方法来跳过指定数量的数据，offset方法同样接受一个数字参数作为跳过的记录条数。<br/>offset通常与limit组合使用。 | offset: 10 |

注：当start\_time和end\_time同时为负数时，表示查询整个数据表。

#### 2.5.4 查询响应

```plain
query/rsp/<table_name>/<client_id>/<operation_id>
```

请求Topic参数说明：同插入请求报文定义。

```json
{
  "total": 1000,
 "offset": 0,
 "size": 100,
  "data":[
    {"1669630340": {"controller1": {"measure1": [1, 100], "measure2": [1, "test1"]}}},
    {"1669630350": {"controller1": {"measure1": [1, 101], "measure2": [1, "test2"]}}}
  ]
}
```

参数说明：

| 参数 | 数据类型 | 参数说明 | 举例 |
| --- | --- | --- | --- |
| total | INTEGER | 不考虑limit和skip方法，查询结果的总行数 | 1000 |
| offset | INTEGER | 本消息中的第一行在total中的偏移位置，从0开始。 | 0 |
| size | INTEGER | 本消息中的数据行数 | 100 |
| data\[i].timestamp | INTEGER | 数据行时间戳 | 1669696164 |
| data\[i].value | dict  object | 字典对象的控制器集合 | {"controller1": {"measure1": \[1, 100], "measure2": \[1, "test1"]}}} |

#### 2.5.5 删除请求

```plain
remove/req/<table_name>/<client_id>/<operation_id>
```

请求Topic参数说明：同插入请求报文定义。

```json
{
  "noack": 0,
  "start_time": 1, 
  "end_time": 100, 
}
```

参数说明：

| 参数 | 数据类型 | 参数说明 | 举例 |
| --- | --- | --- | --- |
| noack | INTEGER | 0代表需要响应；1代表不需要响应 | 1 |
| start\_time | INTEGER<br/> | INTEGER：时序数据的起始时间，单位秒，包含start\_time.<br/><br/>当start\_time字段为负数或不存在时，表示 TIMESTAMP < end\_time | 1669696164 |
| end\_time | INTEGER<br/> | 时序数据的截止时间，单位秒，不包含end\_time。<br/><br/>当end\_time字段为负数或不存在时，表示 TIMESTAMP >= start\_time | 1669697164 |

注：当start\_time和end\_time同时为负数时，表示清空整个数据表。

#### 2.5.6 删除响应

删除请求payload的noack为0时才会收到删除响应。

```plain
remove/rsp/<table_name>/<client_id>/<operation_id>
```

请求Topic参数说明：同插入请求报文定义。

```json
{
  "return_code": 0,
  "return_msg":"okay"
}
```

#### 2.5.7 返回值说明

| 返回值 | 返回信息 | 备注 |
| --- | --- | --- |
| 0 | Okay | 成功 |
| -1 | Request parameter error | 请求参数错误 |
| -2 | Table \<table\_name> not exist | 数据表不存在 |
| -3 | SQL error | SQL语句执行出错 |
| -4 | Request timeout | 请求超时 |

### 3 **Restful** API

DSA提供了获取状态信息的Restful API，可以通过API来获取采集信息和状态信息。

### 3.1 登录

```plain
POST /v1/user/login
```

请求头部参数：

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Authorization | Basic YWRtOjEyMzQ1Ng== | 登录名和登录密码需要进行base64加密后放在http头部；如登录名：adm,密码：123456，需要拼接成"adm:123456"字符串进行base64加密得到" YWRtOjEyMzQ1Ng==" |

```plain
POST https://10.5.30.23/v1/user/login

Request Headers:
Authorization: Basic YWRtOjEyMzQ1Ng==
```

```json
{
  "results": {
    "name": "adm",
    "priv": 15,
    "from": "10.5.30.20",
    "web_session": "MTSVVdC1RwlpmBy30g6G0sErVNKfS0yv",
    "first_login": 0
  }
}
```

说明：web\_session是认证后的token信息，后续接口请求时都需要在请求头里包含该信息。

### 3.2 获取控制器状态

```plain
POST /v1/apps/device/supervisor2/controller/status
```

请求头：Authorization: Bearer MTSVVdC1RwlpmBy30g6G0sErVNKfS0yv

```json
{
  "names":["Modbus TCP"]
}
```

参数说明：

| 参数名称 | 说明 |
| --- | --- |
| names | 控制器名称列表，多个以,号隔开。 |

```json
{
  "result": [
    {
      "name": "Modbus TCP", 
      "status": 1
    }
  ]
}
```

参数说明：

| 参数名称 | 说明 |
| --- | --- |
| name | 控制器名称 |
| status | 控制器状态。0表示离线，1表示在线 |

### 3.3 获取控制器下测点值

```plain
POST /v1/apps/device/supervisor2/measure/reading
```

请求头：Authorization: Bearer MTSVVdC1RwlpmBy30g6G0sErVNKfS0yv

```json
{
  "ctrlName":"Modbus TCP",
  "names":["INT","WORD","FLOAT"]
}
```

参数说明：

| 参数名称 | 说明 |
| --- | --- |
| ctrlName | 控制器名称 |
| names | 测点名称列表，多个以,号隔开 |

```json
{
    "result": [
        {
            "ctrlName": "Modbus TCP",
            "name": "INT",
            "status": 1,
            "timestamp": 1721203547,
            "value": 1
        },
        {
            "ctrlName": "Modbus TCP",
            "name": "WORD",
            "status": 1,
            "timestamp": 1721203547,
            "value": 2
        },
        {
            "ctrlName": "Modbus TCP",
            "name": "FLOAT",
            "status": 1,
            "timestamp": 1721203547,
            "value": 3.12
        }
    ]
}
```

参数说明：

| 参数名称 | 说明 |
| --- | --- |
| ctrlName | 控制器名称 |
| name | 测点名称 |
| status | 测点采集状态。0表示离线，1表示在线 |
| timestamp | 采集时间戳，以秒为单位 |
| value | 采集值 |

### 3.4 更新控制器下测点值

```plain
PUT /v1/apps/device/supervisor2/measure/writing
```

请求头：Authorization: Bearer MTSVVdC1RwlpmBy30g6G0sErVNKfS0yv

```json
[
  {
    "name":"Modbus TCP",
    "measures":[
      {
        "name":"INT",
        "value":10
      }
    ]
  }
]
```

参数说明：

| 参数名称 | 说明 |
| --- | --- |
| name | 控制器名称 |
| measures.name | 测点名称 |
| measures.value | 需要写的测点值 |

```json
{
    "result": [
        {
            "name": "Modbus TCP",
            "measures": [
                {
                    "name": "INT",
                    "error_code": 0,
                    "error_reason": "Success",
                    "value": 10
                }
            ]
        }
    ]
}
```

参数说明：

| 参数名称 | 说明 |
| --- | --- |
| name | 控制器名称 |
| measures.name | 测点名称 |
| measures.error\_code | 写值错误码。0表示成功，非0表示失败 |
| measures.error\_reason | 写值错误原因描述 |
| measures.value | 写值后获取到测点最新的值 |

### 3.5 获取实时告警信息

```plain
GET /v1/apps/device/supervisor2/alarm/realtime?cursor=0&limit=50
```

请求头：Authorization: Bearer MTSVVdC1RwlpmBy30g6G0sErVNKfS0yv

请求URL参数说明：

| 参数名称 | 说明 |
| --- | --- |
| cursor | 实时告警开始条目位置 |
| limit | 实时告警请求返回最大条目数 |

```json
{
    "cursor": 0,
    "limit": 50,
    "total": 1,
    "result": [
        {
            "name": "test",
            "ctrlName": "Modbus TCP",
            "measureName": "WORD",
            "priority": 1,
            "cond1": {
                "op": "gt",
                "value": 10.0
            },
            "condOp": "none",
            "content": "超过阈值10",
            "addr": "40002",
            "value": 20,
            "timestamp": 1721204607,
            "status": 1
        }
    ]
}
```

参数说明：

| 参数名称 | 说明 |
| --- | --- |
| cursor | 实时告警开始条目位置 |
| limit | 实时告警请求返回最大条目数 |
| total | 实时告警当前返回的条目数 |
| result.name | 告警名称 |
| result.ctrlName | 告警关联的控制器名称 |
| result.measureName | 告警关联的测点名称 |
| result.priority | 告警等级。1提醒，2警告，3次要，4重要，5严重 |
| result.cond1.op | 告警条件。eq等于, neq不等于, gt大于, egt大于等于, lt小于, elt小于等于 |
| result.cond1.value | 告警阈值 |
| result.condOp | 条件组合逻辑。and，or，none |
| result.content | 告警描述内容 |
| result.addr | 告警关联测点的地址 |
| result.value | 告警产生/解除时的采集值 |
| result.timestamp | 告警产生/解除时的时间戳 |
| result.status | 告警状态。0解除告警，1产生告警 |

### 3.6 获取云连接状态

```plain
GET /v1/apps/device/supervisor2/cloud/status?name=default
```

请求头：Authorization: Bearer MTSVVdC1RwlpmBy30g6G0sErVNKfS0yv

请求URL参数说明：

| 参数名称 | 说明 |
| --- | --- |
| name | 云服务名称 |

```json
{
  "result": {
    "status": 2,
    "connTime": 127
  }
}
```

参数说明：

| 参数名称 | 说明 |
| --- | --- |
| status | 云服务状态。0未启用，1连接中，2连接成功，3未知错误，4注册中，5已注册 |
| connTime | 连接时长，以秒为单位 |

### 3.7 获取协议转换状态

```plain
GET /v1/apps/device/supervisor2/north/basic/status?service=modbustcp-slave
```

请求头：Authorization: Bearer MTSVVdC1RwlpmBy30g6G0sErVNKfS0yv

请求URL参数说明：

| 参数名称 | 说明 |
| --- | --- |
| service | 协议转换类型。<br/>modbustcp-slave：Modbus TCP Server<br/>iec104-server：IEC 104 Server<br/>opcua-server：OPCUA Server<br/>modbusrtu-slave：Modbus RTU Server<br/>iec101-server：IEC 101 Server<br/>sl651-client：SL651-2014<br/>hj212-client：HJ212 Client<br/>bacnetbip-server：BACnet IP Server<br/>bacnetmstp-server：BACnet MS/TP Server<br/>dnp3-server：DNP3 Outstation<br/>iec61850Server：IEC 61850 Server<br/>snmp\_agent：SNMP Agent |

```json
{
    "result": {
        "service_status": {
            "status": 2,
            "runtime": 84221
        },
        "link_status": [
            {
                "id": 12,
                "ip": "10.5.30.20",
                "port": 58220,
                "status": 1,
                "linktime": 84145
            }
        ]
    }
}
```

参数说明：

| 参数名称 | 说明 |
| --- | --- |
| service\_status.status | 服务状态。0未启动，2运行中 |
| service\_status.runtime | 运行时长，以秒为单位 |
| link\_status.ip | 连接设备IP地址 |
| link\_status.port | 连接设备端口号 |
| link\_status.status | 连接状态 |
| link\_status.linktime | 连接时长 |

### 4 全局配置文件

```json
{
    "controllers": [],
    "measures": [],
    "alarms": [],
    "alarmLables": ["default"],
    "groups": [
      {
        "_id":"group59b64649c93",
        "name": "default",
        "uploadInterval": 10,
        "LwTSDBSize": 1000,
        "strategy": 1,
        "enablePerOnchange": 0,
        "historyDataMode": "gateway",
        "historyDataPath": "/var/user/data/dbhome/device_supervisor/LwTSDB"
      }
    ],
    "misc": {
      "maxAlarmRecordSz": 2000,
      "logLvl": "INFO",
      "coms": [
        {
          "name": "rs232",
          "baud": 9600,
          "bits": 8,
          "stopbits": 1,
          "parityChk": "n"
        },
        {
          "name": "rs485",
          "baud": 9600,
          "bits": 8,
          "stopbits": 1,
          "parityChk": "n"
        }
      ],
      "cachePath": "/var/user/data/dbhome/device_supervisor/offlinedata",
      "cacheSize": 10000,
      "debugLogPath": "/var/user/data/dbhome/device_supervisor/debugLog",
      "debugLogSize": 2000,
      "cacheMode": "gateway",
      "cacheUploadPeriod": 200,
      "cacheStrategy": 0,
      "pubTimeout": 1000,
      "pubRepeatNum": 3,
      "debugLogMode": "gateway",
      "logNum": 2,
      "logSize": 1
    },
    "clouds": [
      {
        "_id": "cloud59b6464bd03",
        "cacheSize": 10000,
        "enable": 0,
        "name": "default",
        "type": "Standard MQTT",
        "args": {
          "host": "",
          "port": 1883,
          "clientId": "",
          "auth": 0,
          "tls": 0,
          "tlsAuth": "caSelfSigned",
          "groupId": "",
          "cleanSession": 0,
          "mqttVersion": "v3.1.1",
          "keepalive": 60,
          "key": "",
          "cert": "",
          "rootCA": "",
          "verifyServer": 0,
          "verifyClient": 0,
          "username": "",
          "passwd": "",
          "willQos": 0,
          "willRetain": 0,
          "willTopic": "",
          "willPayload": ""
        },
        "uploadRules": []
    }
  ],
  "labels": [],
  "serverList": [],
  "quickfaas": {
    "genericFuncs": [],
    "uploadFuncs": [],
    "downloadFuncs": []
  },
  "mindspheres": [
    {
      "name": "mindsphere",
      "enable": 0,
      "_id": "mindsphereeafcdf",
      "args": {
        "hostEnvironment": "eu1",
        "hostDomain": "mindsphere.io",
        "appName": "",
        "appVersion": "",
        "clientId": "",
        "clientSecret": "",
        "authType": "tenant",
        "hostTenant": "",
        "userTenant": "",
        "timeout": 10,
        "statusTimeout": 300,
        "enableOfflinePut": 0
      },
      "mindsphereputs": []
    }
  ],
  "modbusSlave": {
    "enable": 0,
    "protocol": "Modbus-TCP",
    "port": 502,
    "slaveAddr": 1,
    "useRawvalue": 1,
    "int16Ord": "ab",
    "int32Ord": "abcd",
    "float32Ord": "abcd",
    "maxConnection": 5,
    "mapping_table":[],
    "mappingTable": [
      {
        "name": "1",
        "slaveAddr": 1,
        "_id": "modbusTCPSlave01",
        "measures": []
      }
    ]
  },
  "modbusRTUSlave": {
    "enable": 0,
    "protocol": "Modbus-RTU",
    "coms": "rs485",
    "useRawvalue": 1,
    "slaveAddr": 1,
    "int16Ord": "ab",
    "int32Ord": "abcd",
    "float32Ord": "abcd",
    "mapping_table":[],
    "mappingTable": [
      {
        "name": "1",
        "slaveAddr": 1,
        "_id": "modbusRTUSlave01",
        "measures": []
      }
    ]
  },
  "iec104Server": {
    "enable": 0,
    "cotSize": 2,
    "port": 2404,
    "asduLen": 2,
    "connectMode": "tcpServer",
    "enableSpontaneous": 1,
    "uploadPeriod": 0,
    "useRawvalue": 1,
    "serverList": [
      {
        "asduAddr": 1
      }
    ],
    "kValue": 12,
    "wValue": 8,
    "t0": 30,
    "t1": 15,
    "t2": 10,
    "t3": 20,
    "maximumLink" : 5,
    "timeSet": 1,
    "byteOrder": "abcd",
    "mapping_table":[]
  },
  "iec101Server": {
  "enable": 0,
  "coms": "rs485",
  "mode": "UnBalance",
  "enableSpontaneous": 1,
  "uploadPeriod": 0,
  "protocolMode": 0,
  "useRawvalue": 1,
  "linkLen": 2,
  "linkAddr": 1,
  "asduLen": 2,
  "ioaLen": 3,
  "cotLen": 2,
  "serverList": [
   {
    "asduAddr": 1
   }
  ],
  "linkTimeOut": 2000,
  "timeSet": 1,
  "idleTimeOut": 10000,
  "byteOrder": "abcd",
  "mappingTable": {
    "YX": [],
    "YC": [],
    "YK": []
  }
  },
  "iec104Client": {
    "enable": 0,
    "connectType": 2,
    "serverAddr": "ipower.inhandcloud.cn",
    "serverPort": 2406,
    "communicationCode": "",
    "protocol": 1,
    "asduAddr": 1,
    "tls": 1,
    "verification": 1,
    "mapping_table": {
      "YX": [],
      "YC": [],
      "YK": []
    }
  },
  "opcuaServer": {
    "enable": 0,
    "port": 4840,
    "maximumLink" : 5,
    "securityMode": 0,
    "certificate": "None",
    "privateKey": "None",
    "useRawvalue": 1,
    "identifierType": "String",
    "pubsub": 0,
    "mapping_table":[]
  },
  "iec61850Server": {
    "enable": 0,
    "protocol": "iec61850Server",
    "port": 102,
    "iedName": "INHAND",
    "LDName": "Gateway",
    "ctrlMode": 1,
    "authentication": 0,
    "password": "123456",
    "useRawvalue": 1,
    "dataSet": [],
    "mapping_table": []
 },
 "sl651Slave": {
    "enable": 0,
    "centerAaddr": 1,
    "remoteAddr": "",
    "addressIdentifier": "00F1",
    "timeLeader": "00F0",
    "reverseCRC": 0,
    "addrCode": "",
    "password": "",
    "platform_list": [],
    "useRawvalue": 1,
    "mapping_table": []
 },
 "hj212Client": {
    "enable": 0,
    "useRawvalue": 1,
    "platform_list": [],
    "block_list": [],
    "mapping_table": []
 },
 "bacnetServer": {
    "enable": 0,
    "protocol": "BACnet/IP",
    "deviceId": 0,
    "port": 47808,
    "bbmdEnable": 0,
    "useRawvalue": 1,
    "mapping_table": []
 },
 "bacnetMSTPServer": {
    "enable": 0,
    "protocol": "BACnet/MSTP",
    "deviceId": 0,
    "coms": "rs485",
    "maxInfoFrame": 6,
    "mstpMac": 1,
    "maxMaster": 1,
    "useRawvalue": 1,
    "mapping_table": []
 },
 "Dnp3Server": {
    "enable": 0,
    "protocol": "Dnp3-TCP",
    "slaveAddr": 1,
    "masterAddr": 2,
    "port": 20000,
    "useRawvalue": 1,
    "enableUnsol": 0,
    "maxFrasize": 4096,
    "layerTimeout": 1000,
    "linkRetry": 5,
    "enableLink": 0,
    "mapping_table": []
 },
 "snmpAgent": {
    "enable": 0,
    "port": 161,
    "useRawvalue": 1,
    "version": 3,
    "userName": "",
    "enableAuth": 0,
    "readWrite": "ro",
    "enable_trap": 0,
    "mapping_table": []
 },
 "templates": {},
  "bindConfig": {
    "enable": 0,
    "bind":{
      "modelId": "",
      "modelName": "",
      "srcId": "",
      "srcName": "",
      "devId": "",
      "devName": ""
    },
    "varGroups": [],
    "variables": [],
    "alerts":[]
    }
}

```

全局配置文件参数说明：

| 参数名称 | 说明 |
| --- | --- |
| controllers | 测点监控的控制器列表 |
| measures | 测点监控的测点列表 |
| alarms | 告警规则列表 |
| alarmLables | 告警标签列表 |
| groups | 测点监控的分组列表 |
| misc | 参数设置信息 |
| clouds | 云服务列表 |
| labels | 参数设置的自定义参数列表 |
| quickfaas | 发布，订阅和自定义快函数列表 |
| mindspheres | \*MindSphere IoT云服务 |
| modbusSlave | Modbus TCP Slave协议转换配置 |
| modbusRTUSlave | Modbus RTU Slave协议转换配置 |
| iec104Server | IEC 104 Server协议转换配置 |
| iec101Server | IEC 101 Server协议转换配置 |
| iec104Client | 白鹰能源管家(IEC 104)云服务配置 |
| opcuaServer | OPCUA Server协议转换配置 |
| iec61850Server | IEC 61850 Server协议转换配置 |
| sl651Slave | SL651-2014协议转换配置 |
| hj212Client | HJ212 Client协议转换配置 |
| bacnetServer | BACnet IP Server协议转换配置 |
| bacnetMSTPServer | BACnet MS/TP Server协议转换配置 |
| Dnp3Server | DNP3 Outstation协议转换配置 |
| snmpAgent | SNMP Agent协议转换配置 |
