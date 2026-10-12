# EC Series API Documentation V1.0

## API usage instructions

- IEOS provides a set of HTTP APIs for network management and system management. Users can use tools such as curl and Postman or use code to build and send HTTP requests to manage devices.
- The API uses the HTTPS protocol. Because a self-signed certificate is used, the client does not need to verify the certificate. The method of not verifying the certificate is as follows:
  - curl Command plus `-k`parameters
  - Postman needs to close `SSL certificate verification`
  - ![1742178463272-bac06fda-8921-4a71-ae8f-8f1f0bd8dab5.png](./img/O-PDu4iRRdZrb15a/1742178463272-bac06fda-8921-4a71-ae8f-8f1f0bd8dab5-879613.png)
- HTTP API Port fixed `9100`, the URL needs to be prefixed when used: `https://<IP>:9100`
- under Linux system, you can use curl Command to call API, for more curl Command usage: [https://curl.se/docs/](https://curl.se/docs/)
- under Windows system, you can use Postman software to call API,Postman uses the document: [https://learning.postman.com/docs/introduction/overview/](https://learning.postman.com/docs/introduction/overview/)

## obtain authentication

- before using all APIs, you need to log on to the device by using the user name and password to obtain the authentication token.
- URL: `POST /api/v1/login`
- request parameter: Json string
- when calling the logon API outside the device, you need to perform RSA encryption on the user name and password, and then use base64 encoding after encryption.
- RSA public key:

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

| \*\*Attribute \*\* | \*\*In \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| username  | body  | string  | true  | user name for web login  |
| password  | body  | string  | true  | password for web login  |

- note: The following firmware versions use the original username and password when calling the login API:
  - EC5000 Series Less Than V2.0.12
  - EC3320 Less than V2.0.4
  - EC312 Less Than V2.0.17
  - EC954 is less V2.1.9
  - EC942 is less than V2.0.15
- Response
  - login succeeded

```json
{
    "result":{
        "token":"84c1760b-e7a9-43aa-9012-27e8d2a36816"
    }
}
```

```
- login failed 
```

```json
{
  "error":"invalid_parameter",
  "message":"Username or password error"
}
```

- example
  - in the example, the device IP is 192.168.3.100, the user name is adm, and the password is 123456.
  - Postman
    - open Postman and create a new request
    - select POST mode and enter URL `https://192.168.3.100:9100/api/v1/login`
    - click Body-raw-JSON, enter`{"username":"IR56j9l1jOwBwbTkqEnbYINSyF5cI9zAArBeYmtHgFyiYeD7lAr5ohG1IB+uUiShz1uYoEmS0tKnE7c0QMFkO60KTcHq02oSQy9rMBRF9gLP7lxL+Lg/RKL5dRtR7ZsT6CCi460TI1jFISA77wojlyRM4sd1ewlxnXiE/d6tfxqo9x0fk6sT6dFKsjLnEvJ81Rd8rPWTfhWqA54BL9S+Vmlr0UGrn3DBrBqmyGHgtt3GycaemJfbnhLjJ0NEyVuAz2JhAhzooaqRZtj7yTtC2ioD+keIfPH5SG2njDVI/elPy3BEVgbPO09EzyKP3+d/CGfxBvoYRWwlE3M5IRULQD2Sq0WChTK81OYA9wI8lwD4ymHXVPkJtqKk7IyDACot1j0ilH/7YVkRxC7wc0rUfsv1KCVp2En/ADr1iMCSl5rxH/vdJLG8FB+cTLnQdVM4T/T3XiD2tUwatIc1xrPczJ6W0dxHov+sxz+T/e1MC3WidgoIgS7J9lvfERKge4whXOEB3BkTfIkuLrFHlwn9KH7LP0IR3XslTPcxH6wT1W4wGPRcsaPleGiS58IBD+g3//dLkt84RExidMYCErgqHgUiB2Ja3Hn7SvySftop/OpWsub7/k0d8urh1yhvlhOf6XkA6IexsPbuTOGn6GwGPVDZ91Vslm69LwpXVmn8RDE=","password":"SIjEk3z8FG0YtgvzvB7Cs7ceDnR1YZiRYl3fVnB9b84gwTAKZ3GGK5Uqz2KA0AU8eT1qBNiyn2pTm48IQLUTg2Kz5DWDv6sFwvFara36iNJxlfxNLGW7XcbUuFHeP2zLnrRLUx+XDMvYNk4naCtF1hHNzBQqGQ9oUMAELChchZlfYJIBM9Du8OpjH7zKkA2wdIZsNtCN4Ld9LME7GeQufGWTTuSoP4FZb74qgmnvplv8/MO0fWlrtwj0j15BSY98GO8+b2teaJLpXdYoUiLwQj12apKMHNJEI7pEEE/0XJ1mee5Adag6tWEh+wfvBr0YEWr1jzT+R3McjvnqdMH7h5f7imRLaDvrxgNTm+ZJ3kb+14+Y4wZMqsI7sTpPO8T1bfCa3u/4ZvG8Q4HReXu74Li5Zk1qpHnXwQYoHSzZsSO0URByDE/jSqbPhsoMLEmJuuMK3xJZsY1msTR0PiKcp5oOKZhbkEGpuxe9xN8neZWDAp04aaMv69Kzm9mGixzqUeDDTt2DTiH8lOq1Fxd9GMxgkt7KYzRTQ9mNTd+fKnTl27fnrm7YgxPXJhlkd2iT0kZojL7RIVkWUnl4lqd5m4MEuVq8CGA2ZdN/KKnEPJRha0lr6FVAzc8HwZyAgarLUbhty9i2h5cfJfGdoWM89VNIGUEa/FjnutMJsRLumkg="}`
    - Click Send, and if the token is displayed in the Response, the login is successful.
    - ![1746585849773-98383fef-8527-45c9-87c7-d6a106699ef2.png](./img/O-PDu4iRRdZrb15a/1746585849773-98383fef-8527-45c9-87c7-d6a106699ef2-199025.png)
  - curl

```shell
curl -k -X POST \
-H "Content-Type: application/json" \
-d '{"username":"IR56j9l1jOwBwbTkqEnbYINSyF5cI9zAArBeYmtHgFyiYeD7lAr5ohG1IB+uUiShz1uYoEmS0tKnE7c0QMFkO60KTcHq02oSQy9rMBRF9gLP7lxL+Lg/RKL5dRtR7ZsT6CCi460TI1jFISA77wojlyRM4sd1ewlxnXiE/d6tfxqo9x0fk6sT6dFKsjLnEvJ81Rd8rPWTfhWqA54BL9S+Vmlr0UGrn3DBrBqmyGHgtt3GycaemJfbnhLjJ0NEyVuAz2JhAhzooaqRZtj7yTtC2ioD+keIfPH5SG2njDVI/elPy3BEVgbPO09EzyKP3+d/CGfxBvoYRWwlE3M5IRULQD2Sq0WChTK81OYA9wI8lwD4ymHXVPkJtqKk7IyDACot1j0ilH/7YVkRxC7wc0rUfsv1KCVp2En/ADr1iMCSl5rxH/vdJLG8FB+cTLnQdVM4T/T3XiD2tUwatIc1xrPczJ6W0dxHov+sxz+T/e1MC3WidgoIgS7J9lvfERKge4whXOEB3BkTfIkuLrFHlwn9KH7LP0IR3XslTPcxH6wT1W4wGPRcsaPleGiS58IBD+g3//dLkt84RExidMYCErgqHgUiB2Ja3Hn7SvySftop/OpWsub7/k0d8urh1yhvlhOf6XkA6IexsPbuTOGn6GwGPVDZ91Vslm69LwpXVmn8RDE=","password":"SIjEk3z8FG0YtgvzvB7Cs7ceDnR1YZiRYl3fVnB9b84gwTAKZ3GGK5Uqz2KA0AU8eT1qBNiyn2pTm48IQLUTg2Kz5DWDv6sFwvFara36iNJxlfxNLGW7XcbUuFHeP2zLnrRLUx+XDMvYNk4naCtF1hHNzBQqGQ9oUMAELChchZlfYJIBM9Du8OpjH7zKkA2wdIZsNtCN4Ld9LME7GeQufGWTTuSoP4FZb74qgmnvplv8/MO0fWlrtwj0j15BSY98GO8+b2teaJLpXdYoUiLwQj12apKMHNJEI7pEEE/0XJ1mee5Adag6tWEh+wfvBr0YEWr1jzT+R3McjvnqdMH7h5f7imRLaDvrxgNTm+ZJ3kb+14+Y4wZMqsI7sTpPO8T1bfCa3u/4ZvG8Q4HReXu74Li5Zk1qpHnXwQYoHSzZsSO0URByDE/jSqbPhsoMLEmJuuMK3xJZsY1msTR0PiKcp5oOKZhbkEGpuxe9xN8neZWDAp04aaMv69Kzm9mGixzqUeDDTt2DTiH8lOq1Fxd9GMxgkt7KYzRTQ9mNTd+fKnTl27fnrm7YgxPXJhlkd2iT0kZojL7RIVkWUnl4lqd5m4MEuVq8CGA2ZdN/KKnEPJRha0lr6FVAzc8HwZyAgarLUbhty9i2h5cfJfGdoWM89VNIGUEa/FjnutMJsRLumkg="}' \
https://192.168.3.100:9100/api/v1/login
```

```
    * ![1746586458572-92b48025-dbd5-400b-baab-10e2ac405414.png](./img/O-PDu4iRRdZrb15a/1746586458572-92b48025-dbd5-400b-baab-10e2ac405414-489538.png)
```

- authentication Usage
  - save the token value in the response and add the request header to other HTTP API requests: `Authorization: Bearer <token>`
  - curl add method: plus parameters `-H "Authorization: Bearer <token>"`
  - how to add Postman:
    - ![1742195301510-d98ae5f3-5417-4b49-9568-fc7f879a8790.png](./img/O-PDu4iRRdZrb15a/1742195301510-d98ae5f3-5417-4b49-9568-fc7f879a8790-087742.png)

## internal acquisition authentication

- if you access the API from within the device, you can directly log on to the API without a username and password:
- `GET http://127.0.0.1:9102/api/v1/internal/login`
- ![1746586599437-9c3b15fd-fc8b-480a-b014-87189879bdfe.png](./img/O-PDu4iRRdZrb15a/1746586599437-9c3b15fd-fc8b-480a-b014-87189879bdfe-018860.png)
- note: the following firmware versions do not have this feature:
  - EC5000 Series Less Than V2.0.15
  - EC3320 Less than V2.0.7
  - EC312 Less than V2.0.22
  - EC954 is less V2.1.10
  - EC942 is less than V2.0.16

## \*\*system Management \*\*

### response Description

- the following are some common response instructions for calling API
  - Success will generally return result as OK, failure will return failure type `error`and failure details `message`
- request successful

***CODE_BLOCK_PLACEHOLDER___7___CODE_BLOCK_PLACEHOLDER***

- Token failed, need to login again

***CODE_BLOCK_PLACEHOLDER___8___CODE_BLOCK_PLACEHOLDER***

- wrong input parameter for request

***CODE_BLOCK_PLACEHOLDER___9___CODE_BLOCK_PLACEHOLDER***

- server Error

***CODE_BLOCK_PLACEHOLDER___10___CODE_BLOCK_PLACEHOLDER***

### change Password

#### change the password through API

***CODE_BLOCK_PLACEHOLDER___11___CODE_BLOCK_PLACEHOLDER***

- request parameters: Json

***CODE_BLOCK_PLACEHOLDER___12___CODE_BLOCK_PLACEHOLDER***

| \*\*Attribute \*\* | \*\*In \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| old  | body  | string  | true  | current password, encoded in base64  |
| new  | body  | string  | true  | the new password is encoded in base64. The password is 8 to 128 characters in length and contains at least three types of letters, lowercase letters, numbers, and symbols.  |

***CODE_BLOCK_PLACEHOLDER___13___CODE_BLOCK_PLACEHOLDER***

| Model  | version Number  |
| --- | --- |
| EC5000 Series  | V2.0.12  |
| EC3320  | V2.0.4  |
| EC312  | V2.0.17  |
| EC954  | V2.1.9  |
| EC942  | V2.0.15  |

- response
  - success

***CODE_BLOCK_PLACEHOLDER___14___CODE_BLOCK_PLACEHOLDER***

- example
  - Postman
    - ![1742200481920-b34b24c7-e7d2-402c-87a2-e4f87415eed7.png](./img/O-PDu4iRRdZrb15a/1742200481920-b34b24c7-e7d2-402c-87a2-e4f87415eed7-354947.png)
  - curl

***CODE_BLOCK_PLACEHOLDER___15___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___16___CODE_BLOCK_PLACEHOLDER***

#### change password through configuration file

- export Configuration File
- generate password hash
  - install the htpasswd tool: `apt install apache2-utils`
  - generate password hash: `htpasswd -bnBC 10 "" "password" | tr -d ':'`
- replace `password`parameters
- import Configuration File

### status Query

***CODE_BLOCK_PLACEHOLDER___17___CODE_BLOCK_PLACEHOLDER***

- **request Parameters**
  - None
- \*\*response \*\*

***CODE_BLOCK_PLACEHOLDER___18___CODE_BLOCK_PLACEHOLDER***

- \*\*response parameter description \*\*

| parameter Name  | type  | description  |
| --- | --- | --- |
| hostname  | String  | host name of the system  |
| model  | String  | equipment Model  |
| sn  | String  | device Serial Number  |
| bootLoader  | String  | bootLoader version number  |
| kernel  | String  | kernel version number  |
| version  | String  | software version number  |
| cpuLoad  | String  | average of the available system load over the past 1, 5, and 15 minutes, respectively  |
| startedAt  | String  | system startup time  |
| time  | String | System Time  |
| rates  | Array  | resource Usage  |
| rates.total  | Number  | total  |
| rates.usage  | Number  | used  |
| rates.rate  | Number  | utilization rate  |
| rates.name  | String  | resource Name <br/>memory: memory <br/>cpu:CPU <br/>user: user Flash space  |
| OS  | String  | system version number  |

- \*\*example \*\*

***CODE_BLOCK_PLACEHOLDER___19___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___20___CODE_BLOCK_PLACEHOLDER***

### restart device

***CODE_BLOCK_PLACEHOLDER___21___CODE_BLOCK_PLACEHOLDER***

- \*\*request Parameters \*\*
  - none
- \*\*response \*\*

***CODE_BLOCK_PLACEHOLDER___22___CODE_BLOCK_PLACEHOLDER***

- \*\*description \*\*
  - the device restarts immediately after the response data is returned

### restore factory

***CODE_BLOCK_PLACEHOLDER___23___CODE_BLOCK_PLACEHOLDER***

- \*\*request Parameters \*\*
  - \*\*none \*\*
- **response**

***CODE_BLOCK_PLACEHOLDER___24___CODE_BLOCK_PLACEHOLDER***

- \*\*Description \*\*
  - restores parameters configured through IEOS, does not delete data such as software installed by the user

### reset the system

***CODE_BLOCK_PLACEHOLDER___25___CODE_BLOCK_PLACEHOLDER***

- \*\*request Parameters \*\*
  - \*\*none \*\*
- \*\*response \*\*

***CODE_BLOCK_PLACEHOLDER___26___CODE_BLOCK_PLACEHOLDER***

- \*\*description \*\*
  - all user data will be deleted and the system will be restored to its initial state.

### Export Configuration

***CODE_BLOCK_PLACEHOLDER___27___CODE_BLOCK_PLACEHOLDER***

- request parameters:
  - none
- response
  - profile Contents
- example
  - get the configuration file and save it to config.json

***CODE_BLOCK_PLACEHOLDER___28___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___29___CODE_BLOCK_PLACEHOLDER***

- description
  - export the parameters configured by the user through IEOS, in the format of json

### import Configuration

***CODE_BLOCK_PLACEHOLDER___30___CODE_BLOCK_PLACEHOLDER***

- request parameters:

| \*\*Attribute \*\* | \*\*In \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| file  | body  | file  | true  | profile  |

- response

***CODE_BLOCK_PLACEHOLDER___31___CODE_BLOCK_PLACEHOLDER***

- example

***CODE_BLOCK_PLACEHOLDER___32___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___33___CODE_BLOCK_PLACEHOLDER***

- description
  - After the import configuration is successful, the device will automatically restart

### get Configuration

***CODE_BLOCK_PLACEHOLDER___34___CODE_BLOCK_PLACEHOLDER***

- request Parameters

| \*\*Attribute \*\* | \*\*In \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| fields  | query  | string arrays  | false  | the field to be queried, supporting multiple fields, using the symbol "," <br/>supported formats: <br/>baseSystem <br/>baseSystem.setting <br/>networkServices.dhcp <br/>networkServices.wifi\_config,networkServices.dhcp  |

- response

***CODE_BLOCK_PLACEHOLDER___35___CODE_BLOCK_PLACEHOLDER***

- example

***CODE_BLOCK_PLACEHOLDER___36___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___37___CODE_BLOCK_PLACEHOLDER***

### update Configuration

***CODE_BLOCK_PLACEHOLDER___38___CODE_BLOCK_PLACEHOLDER***

- request Parameters
  - Json string, format reference Obtaining System Configuration Response Data
- response

***CODE_BLOCK_PLACEHOLDER___39___CODE_BLOCK_PLACEHOLDER***

- example
  - take modifying hostname as an example

***CODE_BLOCK_PLACEHOLDER___40___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___41___CODE_BLOCK_PLACEHOLDER***

## cloud Services

### start Cloud Service

***CODE_BLOCK_PLACEHOLDER___42___CODE_BLOCK_PLACEHOLDER***

- Request Parameters

| \*\*Attribute \*\* | \*\*In \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| region  | url  | String  | true  | can only be cn or us <br/>cn: domestic platform <br/>us: Overseas Platform  |

- response

***CODE_BLOCK_PLACEHOLDER___43___CODE_BLOCK_PLACEHOLDER***

### stop Cloud Service

***CODE_BLOCK_PLACEHOLDER___44___CODE_BLOCK_PLACEHOLDER***

- request parameters:
  - none
- response

***CODE_BLOCK_PLACEHOLDER___45___CODE_BLOCK_PLACEHOLDER***

### querying Cloud Service Status

***CODE_BLOCK_PLACEHOLDER___46___CODE_BLOCK_PLACEHOLDER***

- request parameters:
  - none
- response

***CODE_BLOCK_PLACEHOLDER___47___CODE_BLOCK_PLACEHOLDER***

- parameter Description
  - enabled: function on state
  - region: connected cloud platform
  - status:online, offline: offline

## plug-in Management

### plug-in installation

***CODE_BLOCK_PLACEHOLDER___48___CODE_BLOCK_PLACEHOLDER***

- request parameters:

| \*\*Attribute \*\* | \*\*In \*\* | **Type** | \*\*Required \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| file  | body  | file  | true  | plugin installation package, ending with .tar.gz  |

- response

***CODE_BLOCK_PLACEHOLDER___49___CODE_BLOCK_PLACEHOLDER***

### plugin Uninstall

***CODE_BLOCK_PLACEHOLDER___50___CODE_BLOCK_PLACEHOLDER***

- request parameters: Json

| \*\*Attribute \*\* | \*\*In \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| name  | url  | string  | true  | plug-in name  |
| retain  | body  | boolen  | true  | whether to retain data, by default <br/>true-reserved <br/>false-do not reserve  |

- response

***CODE_BLOCK_PLACEHOLDER___51___CODE_BLOCK_PLACEHOLDER***

### plug-in List

***CODE_BLOCK_PLACEHOLDER___52___CODE_BLOCK_PLACEHOLDER***

- request parameters:
  - none
- response

***CODE_BLOCK_PLACEHOLDER___53___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___54___CODE_BLOCK_PLACEHOLDER***

### plugin running

***CODE_BLOCK_PLACEHOLDER___55___CODE_BLOCK_PLACEHOLDER***

- request parameters:
  - name: plug-in name
- response
  - success

***CODE_BLOCK_PLACEHOLDER___56___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___57___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___58___CODE_BLOCK_PLACEHOLDER***

### plug-in Stop

***CODE_BLOCK_PLACEHOLDER___59___CODE_BLOCK_PLACEHOLDER***

- request parameters:
  - name: plug-in name
- response

***CODE_BLOCK_PLACEHOLDER___60___CODE_BLOCK_PLACEHOLDER***

## network Management

### querying Network Port Configuration

***CODE_BLOCK_PLACEHOLDER___61___CODE_BLOCK_PLACEHOLDER***

- \*\*response \*\*

***CODE_BLOCK_PLACEHOLDER___62___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___63___CODE_BLOCK_PLACEHOLDER***

### update network port configuration

***CODE_BLOCK_PLACEHOLDER___64___CODE_BLOCK_PLACEHOLDER***

- \*\*request parameter example \*\*

***CODE_BLOCK_PLACEHOLDER___65___CODE_BLOCK_PLACEHOLDER***

\*\*parameter Description \*\*

- `networkServices`, `network`, `interface`, `config_id (that is, the 0002000000000000 in the example)`, `config-name`and `ifname`They are fixed fields, and their values are maintained by the vendor. Before calling the update port configuration API, you need to call the query port configuration API to obtain the values of these fields. `proto`, `ipaddr`and `netmask`fields are maintained by the customer.

| \*\*Attribute \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Range \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| proto  | string  | true  | | protocol Type; Available value: `static`<br/>, `dhcp` |
| ipaddr  | string  | true  | | interface IP address; When `proto`<br/>for `dhcp`<br/>when, will `ipaddr`<br/>set ""  |
| netmask  | string | true  | | network mask; When `proto`<br/>for `dhcp`<br/>when, will `netmask`<br/>set ""  |

### query cellular configuration

***CODE_BLOCK_PLACEHOLDER___66___CODE_BLOCK_PLACEHOLDER***

- \*\*response \*\*

***CODE_BLOCK_PLACEHOLDER___67___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___68___CODE_BLOCK_PLACEHOLDER***

### update cellular configuration

***CODE_BLOCK_PLACEHOLDER___69___CODE_BLOCK_PLACEHOLDER***

- \*\*request parameter example \*\*

***CODE_BLOCK_PLACEHOLDER___70___CODE_BLOCK_PLACEHOLDER***

- \*\*parameter Description \*\*

| \*\*Attribute \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Range \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| enable  | int  | true  | \[0,1]  | cellular function enable switch  |
| sim\_profiles  | array  | true  | 10 | Cellular network configuration candidates, up to 10; Each candidate contains information such as apn/user/password; Select one when dialing; Non-private network environment can be configured, and the default configuration can be retained. Configure up to 10 group members  |
| index  | int  | true  | \[1, 10]  | configure the index value of the candidate  |
| apn  | string  | true  | \[1,128] characters  | apn configuration item  |
| username  | string  | true  | \[1,128] characters  | user name configuration item  |
| password  | string  | true  | \[1,128] characters  | password Configuration Item  |
| auth\_type  | int  | true  | \[0,3]  | authentication method; 0: No authentication; 1:pap,2:chap;3:auto(pap or chap, device auto selection) |
| sim1\_profile\_id  | int  | true  | \[0,10]  | the index value of the configuration candidate selected by the SIM1 card; 0 indicates that automatic configuration is used; Other values correspond to indexes in sim\_profiles.  |
| sim2\_profile\_id  | int  | true  | \[0,10]  | the index value of the configuration candidate selected by the SIM2 card; 0 indicates that automatic configuration is used; Other values correspond to indexes in sim\_profiles.  |
| enable\_infinitely\_redial  | int  | true  | \[0,1]  | infinite redial enable switch; Closed by default; When dialing fails 120 times in a row, the system will be restarted to try to solve the problem of dialing failure. For devices without SIM card, this option can be turned on. After it is turned on, the system will not be restarted no matter how many times dialing fails.  |
| enable\_dualsim  | int  | true  | \[0,1]  | dual card enable switch; Off by default and use SIM1 card for dialing  |
| main\_sim  | int  | true | \[0,1]  | after the dual card is turned on, the SIM card selected for dialing is preferred; It is only valid when the dual card is turned on; 0:SIM1 card; 1:SIM2  |
| dualsim\_config.retries  | int  | true  | \[1, 10]  | after opening dual cards, switch to another SIM card for dialing when the current SIM card fails to dial for the number of times set by retires; Default value 3  |
| network\_mode  | int  | true  | \[0, 13]  | network system; 0: automatic; 1:GSM;2:WCDMA;3:LTE;4:TD-SCDMA;5:UMTS;6:CDMA;7:HDR;8:CDMA and HDR;9: reserved; 10: reserved; 11:5g; 12:5g SA;13:5g NSA; The network system here is for all modules supported by inhand, specific modules only support some of these options  |
| enable\_default\_route  | int  | true  | \[0,1]  | cellular Port default route enable switch; After opening, a default route based on cellular network will be automatically created after successful dialing  |
| route\_metric  | int  | true | \[2, 255]  | priority of default route for cellular network  |
| dial\_interval  | int  | true  | \[1, 3600]s  | redial interval; When the current dialing fails, the interval of the next dialing automatically starts; The default is 10s.  |
| signal\_interval  | int  | true  | \[1, 3600]s  | signal query interval; Default 120s  |
| addr  | array  | false  | 2  | imp detection address, that is, ICMP detection enable switch; Closed by default; Turning on detection helps to solve the problem of fake connection in cellular network, and it is recommended that customers turn it on. The opening method is to configure at least one address that can be reached by ICMP messages. However, only 2 probe addresses can be configured at most. The shutdown method is to delete all probe addresses; When two addresses are configured, the first address is detected first, will not detect the second address;  |
| interval  | int  | true  | \[1, 86400]s  | detection interval; Sending an ICMP detection packet every interval  |
| timeout | int  | true  | \[1, 60]s  | the timeout time of the probe message; When the probe message is still not received after waiting for the timeout time, the next probe is triggered.  |
| netwatcher.retries  | int  | true  | \[1, 5]  | how many times after the probe fails, the redial is triggered; If two probe addresses are configured, each probe address needs to fail reattempts before The redial is triggered.  |
| is\_strict\_detect  | int  | true  | \[0,1]  | ICMP strictly detects the enable switch; The default is off; In order to save the user's cellular traffic, the program will regularly check whether the number of messages received by the cellular port has changed. When the message received by the cellular port changes, it means that there is no false connection in the network. ICMP detection is not triggered; However, if ICMP strict detection is turned on, ICMP detection will be carried out according to the detection strategy regardless of whether the Interface Message changes.  |

### Query cellular status

***CODE_BLOCK_PLACEHOLDER___71___CODE_BLOCK_PLACEHOLDER***

- \*\*response \*\*

***CODE_BLOCK_PLACEHOLDER___72___CODE_BLOCK_PLACEHOLDER***

- \*\*parameter Description \*\*

| \*\*Attribute \*\* | \*\*Type \*\* | \*\*Description \*\* |
| --- | --- | --- |
| asu  | int  | signal strength |
| band  | int  | band  |
| carrierCode  | int  | plmn  |
| carrierString  | string  | network Operator Name  |
| cellid  | string  | cell ID  |
| currentSim  | int  | the SIM card currently in use, 0 means to use sim1;1 means to use sim2  |
| dbm  | int  | power Information  |
| generation  | string  | generation cellular technology, possible values are 2G,3G,4G and 5G  |
| iccid  | string  | iccid  |
| imei  | string  | imei  |
| imsi  | string  | imsi  |
| lac | string  | location Area Code  |
| modemVersion  | string  | the firmware version of the module  |
| netType  | string  | network Type  |
| pci  | int  | pci  |
| regStatus  | int  | note network status; 0: unregistered, 1: Network registration successful, 2: Network registration being, 3: Network registration rejected, 4. Network registration failed, reason unknown, 5: roaming successful; 6: dial-up closed, do not display status  |
| rsrp  | int  | rsrp  |
| rsrq  | int  | rsrq  |
| rssi  | int  | rssi  |
| sigLevel  | int  | signal level, program Internal use  |
| sigbar  | int  | number of signals; Minimum 0 signals, maximum 5 signals  |
| sinr | int  | sinr  |
| connDuration  | int  | length of cellular connection; Unit s  |
| connStatus  | int  | cellular Connection Status; 3: Connected; Other Values: Not Connected  |
| dns  | string  | dns information of cellular network  |
| ip  | string  | IP address of the cellular interface  |
| netmask  | string  | network mask for the cellular interface  |
| gateway  | string  | gateway for Cellular Interface  |
| ifaceName  | string  | name of the cellular interface  |
| mtu  | int  | mtu value for cellular interface  |

### query GPS configuration

***CODE_BLOCK_PLACEHOLDER___73___CODE_BLOCK_PLACEHOLDER***

- \*\*response \*\*

***CODE_BLOCK_PLACEHOLDER___74___CODE_BLOCK_PLACEHOLDER***

- parameter Description

| \*\*Attribute \*\* | **Type** | \*\*Description \*\* |
| --- | --- | --- |
| enable  | int  | open GPS 1: Start 0: Close  |

### update GPS configuration

***CODE_BLOCK_PLACEHOLDER___75___CODE_BLOCK_PLACEHOLDER***

- request parameter example

***CODE_BLOCK_PLACEHOLDER___76___CODE_BLOCK_PLACEHOLDER***

- response

***CODE_BLOCK_PLACEHOLDER___77___CODE_BLOCK_PLACEHOLDER***

### query GPS status

***CODE_BLOCK_PLACEHOLDER___78___CODE_BLOCK_PLACEHOLDER***

- response

***CODE_BLOCK_PLACEHOLDER___79___CODE_BLOCK_PLACEHOLDER***

### querying Wi-Fi Configuration

***CODE_BLOCK_PLACEHOLDER___80___CODE_BLOCK_PLACEHOLDER***

- \*\*response \*\*

***CODE_BLOCK_PLACEHOLDER___81___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___82___CODE_BLOCK_PLACEHOLDER***

### update Wi-Fi configuration

***CODE_BLOCK_PLACEHOLDER___83___CODE_BLOCK_PLACEHOLDER***

- \*\*request parameter example \*\*
  - turn off WIFI:

***CODE_BLOCK_PLACEHOLDER___84___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___85___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___86___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___87___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___88___CODE_BLOCK_PLACEHOLDER***

- \*\*request Parameters \*\*

| \*\*Attribute \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Range \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| enable  | int  | true  | \[0,1]  | Wi-Fi Station enable switch  |
| interface  | string | true  | wlan0  | interface Name  |
| station\_role  | int  | true  | \[0,1]  | 0 means AP 1 for STA  |
| ssid  | string  | true  | | SSID to be connected  |
| key\_mgmt  | int  | true  | \[0,3]  | encryption mode; 0: No authentication; 1:WPA-PSK;2:WPA2-PSK; 3. WPA-PSK/WPA2-PSK Mixed  |
| algorithm  | int  | true  | \[0,2]  | encryption algorithm; 0:CCMP;1:TKIP;2:CCMP and TKIP  |
| psk  | string  | true  | | password of the SSID to be connected  |
| enable\_default\_route  | int | true  | \[0,1]  | Wi-Fi interface default route enable switch; When enabled, a default route based on the Wi-Fi interface is automatically created after the Wi-Fi is successfully connected.  |
| route\_metric  | int  | true  | \[2,255]  | Wi-Fi the priority of the default route  |
| | | | | |
| ap\_ssid\_broadcast  | int  | true  | \[0,1]  | whether SSID broadcast is enabled  |
| ap\_frequency  | int  | true  | \[0,1]  | 0 2.4g 1 5.8g  |
| ap\_radio\_type  | int  | true  | 0/1/2/4/6/7/8/9  | 0 802.11B/G 1 802.11B 2 802.11A 4 802.11G <br/>6 802.11N<br/>7 802.11G/N <br/>8 802.11GA/N/AC <br/>9 802.11B/G/N  |
| ap\_channel  | int  | true  | 2.4G:1-11 5.8G:36/40/44/48/149/153/157/161  | channel  |
| ap\_ssid  | string  | true  | | AP SSID  |
| wpa\_psk\_key  | string  | true  | | AP password  |
| auth\_method  | int  | true  | \[0-3]  | NONE: 0 <br/>WPA-PSK: 1 <br/>WPA2-PSK: 2 <br/>MIXED: 3  |
| encrypt\_mode  | int  | true  | \[3,4] | 3: TKIP 4: AES  |
| ap\_bandwidth  | int  | true  | \[0-2]  | 0: 20m <br/>1:40 m 2: 80m  |
| ap\_max\_associations  | int  | true  | \[1-128]  | maximum number of client connections  |
| ip\_addr  | string  | true  | xx.xx.xx.xx  | AP IPV4 address  |
| netmask  | string  | true  | xx.xx.xx.xx  | mask  |

- response

***CODE_BLOCK_PLACEHOLDER___89___CODE_BLOCK_PLACEHOLDER***

#### set DHCP interface address

- DHCP information needs to be issued after opening AP

***CODE_BLOCK_PLACEHOLDER___90___CODE_BLOCK_PLACEHOLDER***

- request parameter example

***CODE_BLOCK_PLACEHOLDER___91___CODE_BLOCK_PLACEHOLDER***

- \*\*request Parameters \*\*

| \*\*Attribute \*\* | **Type** | \*\*Required \*\* | \*\*Range \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| ipaddr  | string  | true  | xx.xx.xx.xx  | AP IPV4 address  |
| netmask  | string  | true  | xx.xx.xx.xx  | mask  |

- please send this interface after updating the WIFI configuration and returning OK. Only the ip and netmask parameters are modified, and the other parameters remain unchanged
- response

***CODE_BLOCK_PLACEHOLDER___92___CODE_BLOCK_PLACEHOLDER***

### perform a Wi-Fi scan

***CODE_BLOCK_PLACEHOLDER___93___CODE_BLOCK_PLACEHOLDER***

- \*\*response \*\*

***CODE_BLOCK_PLACEHOLDER___94___CODE_BLOCK_PLACEHOLDER***

- \*\*parameter Description \*\*

| \*\*Attribute \*\* | Type  | \*\*Description \*\* |
| --- | --- | --- |
| bssid  | string  | bssid information  |
| channel  | int  | channel information  |
| encryption  | string  | encryption Method |
| signal  | string  | signal value  |
| ssid  | string  | ssid information  |

### query Wi-Fi Status

***CODE_BLOCK_PLACEHOLDER___95___CODE_BLOCK_PLACEHOLDER***

- \*\*response \*\*
  - STA:

***CODE_BLOCK_PLACEHOLDER___96___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___97___CODE_BLOCK_PLACEHOLDER***

***CODE_BLOCK_PLACEHOLDER___98___CODE_BLOCK_PLACEHOLDER***

- \*\*parameter Description \*\*

| \*\*Attribute \*\* | Type  | \*\*Description \*\* |
| --- | --- | --- |
| connDuration  | int  | Wi-Fi connection duration, unit s  |
| connStatus  | int  | Wi-Fi status information; 3: connected; Other values: not connected  |
| ifaceName  | string  | Wi-Fi interface name  |
| ip  | string  | Wi-Fi interface IP address  |
| netmask  | string  | Wi-Fi Interface Network Mask  |
| gateway  | string | Gateway Information  |
| mtu  | int  | interface MTU value  |
| signal  | string  | Wi-Fi signal strength  |

- AP partial response see update WIFI configuration

### query Routing configuration

***CODE_BLOCK_PLACEHOLDER___99___CODE_BLOCK_PLACEHOLDER***

- \*\*response \*\*

***CODE_BLOCK_PLACEHOLDER___100___CODE_BLOCK_PLACEHOLDER***

- please refer to the parameter description `update routing configuration`

### update routing configuration

***CODE_BLOCK_PLACEHOLDER___101___CODE_BLOCK_PLACEHOLDER***

- \*\*request parameter example \*\*

***CODE_BLOCK_PLACEHOLDER___102___CODE_BLOCK_PLACEHOLDER***

- \*\*request Parameters \*\*
  - configuration id `0000657fa834cea`needs to be generated based on the following rules:
  - 4-digit hexadecimal index value, 1-65535 increment. The hexadecimal character is expressed by writing
  - 8-bit hexadecimal timestamp
  - 4-digit hexadecimal random value

| \*\*Attribute \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Range \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| interface  | string  | true  | \[0,1] | Wi-Fi Station enable switch  |
| target  | string  | true  | | SSID to be connected  |
| netmask  | string  | true  | \[0,3]  | encryption mode; 0: No authentication; 1:WPA-PSK;2:WPA2-PSK; 3. WPA-PSK/WPA2-PSK Mixed  |
| gateway  | string  | true  | \[0,2]  | encryption algorithm; 0:CCMP;1:TKIP;2:CCMP and TKIP  |
| metric  | int  | true  | | password of the SSID to be connected  |

### querying Routing Status

***CODE_BLOCK_PLACEHOLDER___103___CODE_BLOCK_PLACEHOLDER***

- response

***CODE_BLOCK_PLACEHOLDER___104___CODE_BLOCK_PLACEHOLDER***

- \*\*parameter Description \*\*

| \*\*Attribute \*\* | Type  | \*\*Description \*\* |
| --- | --- | --- |
| kan  | string | Which interface does the neighbor belong to in the IPv4 network neighbor information  |
| kan  | string  | IP address of the neighbor device in the IPv4 network neighbor information  |
| kan  | string  | MAC address of neighbor device in IPv4 network neighbor information  |
| ipv4\_route\_table.interface  | string  | interface information in the IPv4 routing table  |
| ipv4\_route\_table.target  | string  | target network in IPv4 routing table  |
| ipv4\_route\_table.gateway  | string  | next hop IP address in IPv4 routing table  |
| ipv4\_route\_table.protocol  | string  | routing protocol used by IPv4 routing table entries  |
| ipv4\_route\_table.table  | string  | which routing table belongs to under the IPv4 routing table |
| ipv4\_route\_table.metric  | string  | IPv4 routing table metrics  |

### query DNS configuration

***CODE_BLOCK_PLACEHOLDER___105___CODE_BLOCK_PLACEHOLDER***

- \*\*response \*\*

***CODE_BLOCK_PLACEHOLDER___106___CODE_BLOCK_PLACEHOLDER***

- \*\*parameter Description \*\*
  - you only need to configure the server. Other values are the default values and are not recommended to be modified.

| \*\*Attribute \*\* | Type  | \*\*Description \*\* |
| --- | --- | --- |
| server  | array  | DNS server address, configure up to 5  |

### UPDATE DNS configuration

***CODE_BLOCK_PLACEHOLDER___107___CODE_BLOCK_PLACEHOLDER***

- \*\*request parameter example \*\*

***CODE_BLOCK_PLACEHOLDER___108___CODE_BLOCK_PLACEHOLDER***

- \*\*parameter Description \*\*

| \*\*Attribute \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Range \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| server  | array  | true  | | DNS server address, configure up to 5  |

### query domain name hijacking

***CODE_BLOCK_PLACEHOLDER___109___CODE_BLOCK_PLACEHOLDER***

- \*\*response \*\*

***CODE_BLOCK_PLACEHOLDER___110___CODE_BLOCK_PLACEHOLDER***

- \*\*parameter Description \*\*
  - `0000657fb450e3c`config-id is, the generation rules are as follows:
  - 4-digit hexadecimal index value, 1-65535 increment. The hexadecimal character is expressed by writing
  - 8-bit hexadecimal timestamp
  - 4-digit hexadecimal random value

| \*\*Attribute \*\* | Type  | \*\*Description \*\* |
| --- | --- | --- |
| name  | string  | domain name to be hijacked  |
| ip  | sring  | hijack the domain name to this IP address  |

### update domain name hijacking

***CODE_BLOCK_PLACEHOLDER___111___CODE_BLOCK_PLACEHOLDER***

- \*\*request parameter example \*\*

***CODE_BLOCK_PLACEHOLDER___112___CODE_BLOCK_PLACEHOLDER***

- \*\*parameter Description \*\*

| \*\*Attribute \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Range \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| name  | string  | true  | | domain name to be hijacked  |
| ip  | string  | true  | | hijacking domain names to IP addresses  |
| comments | string  | false  | | remarks on domain name hijacking records  |

### query the DHCP Server configuration

***CODE_BLOCK_PLACEHOLDER___113___CODE_BLOCK_PLACEHOLDER***

- \*\*Response \*\*

***CODE_BLOCK_PLACEHOLDER___114___CODE_BLOCK_PLACEHOLDER***

- for parameter descriptions, see `update DHCP Server configuration`

### update DHCP Server configuration

***CODE_BLOCK_PLACEHOLDER___115___CODE_BLOCK_PLACEHOLDER***

- \*\*request parameter example \*\*

***CODE_BLOCK_PLACEHOLDER___116___CODE_BLOCK_PLACEHOLDER***

- \*\*parameter Description \*\*
  - `config-id`the value `0003000000000000`generated by the vendor program. Before updating the DHCP Server configuration, query the current configuration. You can go to `config-id`value.

| \*\*Attribute \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Range \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| config-name  | string  | true  | | the interface name does not need to be changed.  |
| interface  | string  | true | | The corresponding physical interface under the interface name does not need to be changed.  |
| ignore  | string  | true  | | whether to enable the DHCP Server function; It is turned off when "1"; And it is turned on when.  |
| start  | int  | true  | | start allocation mechanism; Interface Network segment + start = start address of DHCP server address pool;  |
| limit  | int  | true  | | maximum number of addresses in the address pool  |
| leasetime  | string  | true  | | lease time; Support 1h,6h,12h and 24h.  |

### Querying Custom Firewall Configuration

***CODE_BLOCK_PLACEHOLDER___117___CODE_BLOCK_PLACEHOLDER***

- \*\*response \*\*

***CODE_BLOCK_PLACEHOLDER___118___CODE_BLOCK_PLACEHOLDER***

### update custom firewall configuration

***CODE_BLOCK_PLACEHOLDER___119___CODE_BLOCK_PLACEHOLDER***

- \*\*request parameter example \*\*

***CODE_BLOCK_PLACEHOLDER___120___CODE_BLOCK_PLACEHOLDER***

- \*\*request Parameters \*\*

| \*\*Attribute \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Range \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| rules | array  | true  | | firewall Rules  |

## system Upgrade

### upgrade Image Preprocessing

- use the md5sum command to calculate the md5 of a file:
  - `md5sum EC312-V2.0.0.img`
  - ![1741675594901-b46059b9-8a6d-454e-bf06-2a23bb5a3660.png](./img/O-PDu4iRRdZrb15a/1741675594901-b46059b9-8a6d-454e-bf06-2a23bb5a3660-093903.png)
- split a file into chunks of 10m size using the split command
  - `split -b 10M --numeric-suffixes --suffix-length=2 EC312-V2.0.0.img EC312.`
  - ![1741675635291-297fba99-2059-4a2b-81c5-610a95cf299d.png](./img/O-PDu4iRRdZrb15a/1741675635291-297fba99-2059-4a2b-81c5-610a95cf299d-183228.png)

#### Prepare to Upload

- URL: `POST /api/v1/upgrade/prepare/upload`
- request parameters:

| \*\*Attribute \*\* | \*\*In \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| md5  | body  | string  | true  | upgrade package md5  |
| name  | body  | string  | true | Upgrade package name  |
| upgradeBoot  | body  | bool  | true  | whether to upgrade bootloader  |

- response

***CODE_BLOCK_PLACEHOLDER___121___CODE_BLOCK_PLACEHOLDER***

- example:
  - `curl -k -X POST -H "Authorization: Bearer 7327088e-c3c3-479d-b399-384f808d55d4" -H "Content-Type: application/json" -d '{"md5":"b252322b8d1700fcfb423094e3ed5b26","name":"EC312-V2.0.0.img","upgradeBoot":false}' https://10.5.30.191:9100/api/v1/upgrade/prepare/upload`
  - ![1741677611824-46e4af62-5357-4e5e-8b93-23f7e48ae308.png](./img/O-PDu4iRRdZrb15a/1741677611824-46e4af62-5357-4e5e-8b93-23f7e48ae308-841455.png)

#### chunked Upload

- URL: `POST /api/v1/upgrade/chunk/upload`
- request parameters:

| \*\*Attribute \*\* | \*\*In \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| md5 | query  | string  | true  | upgrade package md5  |
| name  | query  | string  | true  | upgrade package name  |
| chunks  | query  | int  | true  | total number of blocks  |
| chunk  | query  | int  | true  | number of blocks  |
| file  | body  | binary  | ture  | chunk content  |

- response

***CODE_BLOCK_PLACEHOLDER___122___CODE_BLOCK_PLACEHOLDER***

- example:
  - `curl -k -X POST -H "Authorization: Bearer 7327088e-c3c3-479d-b399-384f808d55d4" -F "file=@EC312.00" "https://10.5.30.191:9100/api/v1/upgrade/chunk/upload? md5=b252322b8d1700fcfb423094e3ed5b26&amp;name=EC312-V2.0.0.img&amp;chunks=51&amp;chunk=1"`
  - ![1741677723727-7fcab78c-8330-492a-813b-0a6918763064.png](./img/O-PDu4iRRdZrb15a/1741677723727-7fcab78c-8330-492a-813b-0a6918763064-751312.png)
- note: All block files need to be transferred in sequence. Do not miss or repeat the upload. Otherwise, the upgrade will fail and you need to upgrade again.

#### Upload complete

- URL: `PUT /api/v1/upgrade/finish/upload`
- request parameters:

| \*\*Attribute \*\* | \*\*In \*\* | \*\*Type \*\* | \*\*Required \*\* | \*\*Description \*\* |
| --- | --- | --- | --- | --- |
| md5  | body  | string  | true  | upgrade package md5  |
| name  | body  | string  | true | Upgrade package name  |

- response

***CODE_BLOCK_PLACEHOLDER___123___CODE_BLOCK_PLACEHOLDER***

- example:
  - `curl -k -X PUT -H "Authorization: Bearer 7327088e-c3c3-479d-b399-384f808d55d4" -H "Content-Type: application/json" -d '{"md5":"b252322b8d1700fcfb423094e3ed5b26","name":"EC312-V2.0.0.img"}' "https://10.5.30.191:9100/api/v1/upgrade/finish/upload"`
  - ![1741678587788-37a9c035-b5b8-4cb1-9ff9-703f3f8876ca.png](./img/O-PDu4iRRdZrb15a/1741678587788-37a9c035-b5b8-4cb1-9ff9-703f3f8876ca-247624.png)
- note: The system will not restart automatically after the upgrade is completed. You need to call the restart API or execute the reboot command to restart.
