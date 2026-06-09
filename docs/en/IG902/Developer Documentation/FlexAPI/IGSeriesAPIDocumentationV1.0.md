# IG Series API Documentation V1.0

## API usage instructions

- IG Series products provide a set of HTTP APIs for network management and system management. Users can use tools such as curl and Postman or use code to build and send HTTP requests to manage devices.
- The API uses the HTTPS protocol. Because a self-signed certificate is used, the client does not need to verify the certificate. The method of not verifying the certificate is as follows:
  - curl Command plus `-k`parameters
  - Postman needs to close `SSL certificate verification`

![1742178463272-bac06fda-8921-4a71-ae8f-8f1f0bd8dab5.png](./img/Ujehw9NYP7nXO0yW/1742178463272-bac06fda-8921-4a71-ae8f-8f1f0bd8dab5-667031.webp)

```
- HTTP API Port fixed `443`, the URL needs to be prefixed when used: `https :// <IP>` or `https :// <IP>: 443 `
- under Linux system, you can use curl Command to call API, for more curl Command usage: [https://curl.se/docs/ ](https://curl.se/docs/)
- under Windows system, you can use Postman software to call API,Postman uses the document: 
```

[https://learning.postman.com/docs/introduction/overview/](https://learning.postman.com/docs/introduction/overview/)

## obtain authentication

Calling the HTTP-related API interface requires obtaining the Authorization token. The method of obtaining is to base64 encode the user name and password in the form of username:password to obtain the initial token, and then use this token to call the login interface to obtain the final Authorization token.

```http
POST /v1/user/login
```

\*\*Request Example \*\*

the token YWRtOjEyMzQ1Ng = = is obtained by base64 encoding the default username and password in the adm:123456 format.

```json
Authorization: Basic YWRtOjEyMzQ1Ng==
```

\*\*Return information \*\*

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

\*\*parameter Description \*\*

| \*\*parameter Name \*\* | \*\*parameter Description \*\* | \*\*parameter Type \*\* | \*\*value range \*\* |
| --- | --- | --- | --- |
| web\_session  |  | string  | |

\*\*return Example \*\*

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

## network Interface

### cellular network

#### update Configuration

interface

```http
PUT v1/cellular/config?autosave=1
```

load

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1] | Dial enable switch, 0 off, 1 on  |
| enable\_dual\_sim  | integer  | \[0,1]  | dual card enable switch, 0 off, 1 on  |
| main\_sim  | integer  | \[1, 2]  | main SIM card, 1 for sim1,2 for sim2  |
| max\_dial\_times  | integer  | \[1, 10]  | switch SIM cards after a number of SIM card dialing failures reaches the set number of times  |
| min\_dial\_times  | integer  | 0  | legacy field, fixed at 0  |
| backup\_sim\_timeout  | integer  | \[0, 8640000]s  | the time spent on the standby card, when the time is reached, it will be switched back to the main card, in seconds.  |
| network\_type  | integer  | \[0, 7]  | 0: Automatic <br/>1:2g <br/>2:3g<br/>3:4G <br/>6:5g <br/>7:4G5G <br/>there are differences in the network system supported by the settings of different models.  |
| sim1\_profile  | integer  | \[0,10]  | the dial parameters of the sim1 card and. 0 indicates the default dialing parameter set <br/>1~10 corresponds to the index value in the profile array  |
| sim2\_profile  | integer  | \[0,10]  | the dial parameters of the sim2 card and. 0 indicates the default dialing parameter set <br/>1~10 corresponds to the index value in the profile array  |
| sim1\_roaming  | integer  | \[0,1]  | does the sim1 card enable roaming, 0 off, 1 on  |
| sim2\_roaming  | integer  | \[0,1]  | does the sim2 card enable roaming, 0 off, 1 on  |
| sim1\_pincode  | string  | \[1, 6] character  | the pincode of the sim1 card |
| sim2\_pincode  | string  | \[1, 6] character  | pincode of sim2 card  |
| sim1\_csq\_threshold  | integer  | 0  | legacy field, fixed at 0  |
| sim2\_csq\_threshold  | integer  | 0  | legacy field, fixed at 0  |
| sim1\_csq\_detect\_interval  | integer  | 0  | legacy field, fixed at 0  |
| sim2\_csq\_detect\_interval  | integer  | 0  | legacy field, fixed at 0  |
| kan  | integer  | 0  | legacy field, fixed at 0  |
| kan  | integer  | 0 | Legacy field, fixed at 0  |
| static\_ip  | integer  | \[0,1]  | whether to enable static IP, 0 off, 1 enabled, only ppp dial-up modules support this configuration  |
| ip\_addr  | string  | \[1, 16] characters  | local IP address when static IP is enabled  |
| peer\_addr  | string  | \[1, 16] characters  | peer IP address when static IP is enabled  |
| connect\_mode  | integer  | 0  | legacy field, fixed at 0  |
| trig\_data  | integer  | 1  | legacy field, fixed at 1  |
| trig\_sms  | integer  | 0  | legacy field, fixed at 0  |
| max\_idle\_time  | integer  | 60 | Legacy field, fixed at 60  |
| radial\_interval  | integer  | \[1, 3600]s  | after dialing fails, it will dial again, but it will wait for a period of time before dialing again. The waiting time is set here.  |
| init\_command  | string  | \[1, 32] characters  | initialization command  |
| rssi\_poll\_interval  | integer  | \[1, 3600]s  | signal detection interval  |
| dial\_timeout  | integer  | \[10, 3600]s  | dial Timeout  |
| mtu  | integer  | \[128, 1500]  | MTU value for the dial-up Interface  |
| mru  | integer  | \[128, 1500]  | MRU value of the dial-up Interface  |
| use\_default\_asyncmap  | integer | 0  | legacy field, fixed at 0  |
| use\_peer\_dns  | integer  | \[0,1]  | whether to use the DNS assigned by dial-up, 0 does not use, 1 uses  |
| infinitely\_dial\_retry  | integer  | \[0,1]  | whether to turn on unlimited redial, after turning on, no matter how many times the dialing fails, the system will not restart; After turning off, when the dialing failure reaches a certain number of times, the system will automatically restart.  |
| debug  | integer  | \[0,1]  | whether to enable debug log, 0 off, 1 on  |
| expert\_options  | string  | \[1, 32] characters  | expert Options  |
| pdp\_type  | integer  | \[0,2]  | 0: IPV4 <br/>1: IPV6 <br/>2: IPV4V6  |
| sms.enable  | integer  | \[0,1] | Whether to enable SMS function, 0 off, 1 on  |
| sms.mode  | integer  | 1  | SMS mode, fixed at 1, indicates SMS in text format  |
| sms.enable\_reply  | integer  | \[0,1]  | after configuring the gateway through SMS, whether to reply to the configuration result through SMS, 0 does not reply, 1 reply.  |
| sms.interval  | integer  |  | cycle of processing SMS  |
| sms.phone\_num\_white\_lists  | array  | maximum of 10 members  | mobile phone number White List, only in the white list of mobile phone number to send text messages, the program will be processed.  |
|  |  |  |  |

#### Query Configuration

interface

```http
GET v1/cellular/config
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1] | Dial enable switch, 0 off, 1 on  |
| enable\_dual\_sim  | integer  | \[0,1]  | dual card enable switch, 0 off, 1 on  |
| main\_sim  | integer  | \[1, 2]  | main SIM card, 1 for sim1,2 for sim2  |
| max\_dial\_times  | integer  | \[1, 10]  | switch SIM cards after a number of SIM card dialing failures reaches the set number of times  |
| min\_dial\_times  | integer  | 0  | legacy field, fixed at 0  |
| backup\_sim\_timeout  | integer  | \[0, 8640000]s  | the time spent on the standby card, when the time is reached, it will be switched back to the main card, in seconds.  |
| network\_type  | integer  | \[0, 7]  | 0: Automatic <br/>1:2g <br/>2:3g<br/>3:4G <br/>6:5g <br/>7:4G5G <br/>there are differences in the network system supported by the settings of different models.  |
| sim1\_profile  | integer  | \[0,10]  | the dial parameters of the sim1 card and. 0 indicates the default dialing parameter set <br/>1~10 corresponds to the index value in the profile array  |
| sim2\_profile  | integer  | \[0,10]  | the dial parameters of the sim2 card and. 0 indicates the default dialing parameter set <br/>1~10 corresponds to the index value in the profile array  |
| sim1\_roaming  | integer  | \[0,1]  | does the sim1 card enable roaming, 0 off, 1 on  |
| sim2\_roaming  | integer  | \[0,1]  | does the sim2 card enable roaming, 0 off, 1 on  |
| sim1\_pincode  | string  | \[1, 6] character  | the pincode of the sim1 card |
| sim2\_pincode  | string  | \[1, 6] character  | pincode of sim2 card  |
| sim1\_csq\_threshold  | integer  | 0  | legacy field, fixed at 0  |
| sim2\_csq\_threshold  | integer  | 0  | legacy field, fixed at 0  |
| sim1\_csq\_detect\_interval  | integer  | 0  | legacy field, fixed at 0  |
| sim2\_csq\_detect\_interval  | integer  | 0  | legacy field, fixed at 0  |
| kan  | integer  | 0  | legacy field, fixed at 0  |
| kan  | integer  | 0 | Legacy field, fixed at 0  |
| static\_ip  | integer  | \[0,1]  | whether to enable static IP, 0 off, 1 enabled, only ppp dial-up modules support this configuration  |
| ip\_addr  | string  | \[1, 16] characters  | local IP address when static IP is enabled  |
| peer\_addr  | string  | \[1, 16] characters  | peer IP address when static IP is enabled  |
| connect\_mode  | integer  | 0  | legacy field, fixed at 0  |
| trig\_data  | integer  | 1  | legacy field, fixed at 1  |
| trig\_sms  | integer  | 0  | legacy field, fixed at 0  |
| max\_idle\_time  | integer  | 60 | Legacy field, fixed at 60  |
| radial\_interval  | integer  | \[1, 3600]s  | after dialing fails, it will dial again, but it will wait for a period of time before dialing again. The waiting time is set here.  |
| init\_command  | string  | \[1, 32] characters  | initialization command  |
| rssi\_poll\_interval  | integer  | \[1, 3600]s  | signal detection interval  |
| dial\_timeout  | integer  | \[10, 3600]s  | dial Timeout  |
| mtu  | integer  | \[128, 1500]  | MTU value for the dial-up Interface  |
| mru  | integer  | \[128, 1500]  | MRU value of the dial-up Interface  |
| use\_default\_asyncmap  | integer | 0  | legacy field, fixed at 0  |
| use\_peer\_dns  | integer  | \[0,1]  | whether to use the DNS assigned by dial-up, 0 does not use, 1 uses  |
| infinitely\_dial\_retry  | integer  | \[0,1]  | whether to turn on unlimited redial, after turning on, no matter how many times the dialing fails, the system will not restart; After turning off, when the dialing failure reaches a certain number of times, the system will automatically restart.  |
| debug  | integer  | \[0,1]  | whether to enable debug log, 0 off, 1 on  |
| expert\_options  | string  | \[1, 32] characters  | expert Options  |
| pdp\_type  | integer  | \[0,2]  | 0: IPV4 <br/>1: IPV6 <br/>2: IPV4V6  |
| sms.enable  | integer  | \[0,1] | Whether to enable SMS function, 0 off, 1 on  |
| sms.mode  | integer  | 1  | SMS mode, fixed at 1, indicates SMS in text format  |
| sms.enable\_reply  | integer  | \[0,1]  | after configuring the gateway through SMS, whether to reply to the configuration result through SMS, 0 does not reply, 1 reply.  |
| sms.interval  | integer  |  | cycle of processing SMS  |
| sms.phone\_num\_white\_lists  | array  | maximum of 10 members  | mobile phone number White List, only in the white list of mobile phone number to send text messages, the program will be processed.  |
|  |  |  |  |

#### Query Status

##### module Status

interface

```http
GET v1/cellular/modem/status
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| active\_sim  | string | \[1, 16] characters  | SIM card currently in use  |
| imei\_code  | string  | \[1, 16] characters  | IEMI information of cellular module  |
| imsi\_code  | string  | \[1, 16] characters  | IMSI information of SIM card  |
| iccid\_code  | string  | \[1, 32] characters  | ICCID information of SIM card  |
| phone\_number  | string  | \[1, 16] characters  | mobile phone number  |
| signal\_level  | integer  | \[0, 31]  | signal quality  |
| rerp  | integer  |  | RERP  |
| rerq  | integer  |  | RERQ  |
| register\_status  | integer | \[0, 7]  | connection status: <br/>0: Registering to the network <br/>1: Register network successfully <br/>2: Registering to the network <br/>3: Registration network is denied <br/>4: Failed to register network for unknown reason <br/>5: Failed to register network for unknown reason <br/>6: Not yet registered to the network <br/>7: Turn off dialing, the registration status is not displayed at this time  |
| operator  | string  | \[1, 16] characters  | operator  |
| mcc\_mnc  | integer  |  | PLMN  |
| apns  | string  | \[1, 16] characters  | APN Information  |
| network\_type  | string  | \[1, 16] characters  | network Type  |
| lac  | string  | \[1, 16] characters  | location Area Code  |
| cell\_id | string  | \[1, 16] characters  | cell ID  |

##### connection status

interface

```http
GET v1/cellular/network/status
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| status  | integer  | \[0,1]  | 0: not connected; 1: Connected  |
| ip\_addr  | string  | \[1, 16] characters  | cellular interface IP address  |
| netmask  | string  | \[1, 16] characters  | cellular Interface Subnet Mask  |
| gateway  | string  | \[1, 16] characters  | gateway  |
| mtu  | integer  | \[68, 1500]  | interface MTU value  |
| dns | string  | \[1, 32]  | dns information  |
| connect\_time  | integer  |  | cellular interface connection duration  |

### WAN interface

#### update Configuration

interface

```http
PUT v1/eth/config?autosave=1
```

load

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| iface\_name  | string  | \[1, 16] characters  | interface Name  |
| internet  | integer  | \[0,1]  | 0: interface is configured as static IP <br/>1: The interface is configured as DHCP to obtain the address  |
| primary\_ip  | string  | \[1, 16] characters  | interface IP address  |
| netmask  | string  | \[1, 16] characters | Interface Subnet Mask  |
| mtu  | integer  | \[68, 1500]  | interface MTU value  |
| track\_l2\_state  | integer  | \[0,1]  | level 2 status linkage switch; 0 off, 1 on  |
| shutdown  | integer  | \[0,1]  | interface status switch; 0 on, 1 off  |
| description  | string  | \[0,32] characters  | interface Description Information  |
| multi\_ip  | object  | | interface from IP information  |

#### query Configuration

interface

```http
GET v1/eth/config?iface=eth1
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| iface\_name  | string | \[1, 16] characters  | interface Name  |
| internet  | integer  | \[0,1]  | 0: interface is configured as static IP <br/>1: The interface is configured as DHCP to obtain the address  |
| primary\_ip  | string  | \[1, 16] characters  | interface IP address  |
| netmask  | string  | \[1, 16] characters  | interface Subnet Mask  |
| mtu  | integer  | \[68, 1500]  | interface MTU value  |
| track\_l2\_state  | integer  | \[0,1]  | level 2 status linkage switch; 0 off, 1 on  |
| shutdown  | integer  | \[0,1]  | interface status switch; 0 on, 1 off  |
| description  | string | \[0,32] characters  | interface Description Information  |
| multi\_ip  | object  | | interface from IP information  |

#### query Status

interface

```http
GET v1/eth/status?iface=eth1
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| iface\_name  | string  | \[1, 16] characters  | interface Name  |
| connect\_type  | integer  | \[0,1]  | 0: interface is configured as static IP <br/>1: The interface is configured as DHCP to obtain the address  |
| ip\_addr  | string  | \[1, 16] characters  | interface IP address  |
| netmask  | string  | \[1, 16] characters  | interface Subnet Mask  |
| mtu | integer  | \[68, 1500]  | interface MTU value  |
| gateway  | string  | \[1, 16] characters  | IP address of the Gateway  |
| status  | integer  | \[0,1]  | interface status; 0 means interface down,1 means interface up  |
| dns  | string  | \[0,32] characters  | dns information  |
| connect\_time  | integer  | \[1, n]  | duration of interface up  |
| remaining\_lease  | integer  | \[0, 10080]  | the remaining lease period when the interface obtains the address through DHCP, in minutes.  |

### LAN interface

#### update Configuration

interface

```http
PUT v1/bridge/config?autosave=1&brid=1
```

load

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

parameters

| Attribute  | Type | Range  | Description  |
| --- | --- | --- | --- |
| iface\_name  | string  | \[1, 16] characters  | interface Name  |
| primary\_ip  | string  | \[1, 16] characters  | interface IP address  |
| netmask  | string  | \[1, 16] characters  | interface Subnet Mask  |
| shutdown  | bool  | true/false  | interface status switch; false on, true off  |
| bridge\_interfaces  | array  |  | LAN is a bridge interface. Here is a list of the physical interfaces that the bridge interface contains.  |
| description  | string  | \[0,32] characters  | interface Description Information  |
| multi\_ip  | object  | | interface from IP information  |

#### query Configuration

Interface

```http
GET v1/bridge/config?brid=1
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| iface\_name  | string  | \[1, 16] characters  | interface Name  |
| primary\_ip  | string  | \[1, 16] characters  | interface IP address  |
| netmask  | string  | \[1, 16] characters  | interface Subnet Mask  |
| shutdown  | bool  | true/false  | interface status switch; false on, true off  |
| bridge\_interfaces  | array  |  | LAN is a bridge interface. Here is a list of the physical interfaces that the bridge interface contains.  |
| description  | string  | \[0,32] characters | Interface Description Information  |
| multi\_ip  | object  | | interface from IP information  |

#### query Status

interface

```http
v1/bridge/status?brid=1
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| iface\_name  | string  | \[1, 16] characters  | interface Name  |
| connect\_type  | integer  | \[0,1]  | 0: interface is configured as static IP <br/>1: The interface is configured as DHCP to obtain the address  |
| ip\_addr  | string  | \[1, 16] characters  | interface IP address  |
| netmask  | string  | \[1, 16] characters  | interface Subnet Mask  |
| mtu  | integer | \[68, 1500]  | interface MTU value  |
| gateway  | string  | \[1, 16] characters  | IP address of the Gateway  |
| dns  | string  | \[0,32] characters  | dns information  |
| connect\_time  | integer  | \[1, n]  | duration of interface up  |
| description  | string  | \[0,32] characters  | interface Description Information  |
| status  | integer  | \[0,1]  | interface status; 0 means interface down,1 means interface up  |
| remaining\_lease  | integer  | \[0, 10080]  | the remaining lease period when the interface obtains the address through DHCP, in minutes.  |

### WLAN

#### Update Station configuration

interface

```http
PUT v1/dot11radio/config?autosave=1
```

load

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

Parameters

| Attribute | Type | Range | Description |
| --- | --- | --- | --- |
| enable | integer | \[0,1] | WLAN switch, 0 off, 1 on |
| station\_role | integer | \[0,1] | Wi-Fi working mode<br/>0:AP<br/>1:Station |
| ap\_ssid | string | \[1, 32] characters | ssid name in AP mode |
| ap\_ssid\_broadcast | integer | \[0,1] | SSID broadcast switch, 0 is off, 1 is on |
| auth\_method | integer | \[0, 8] | authentication Method<br/>0: No certification<br/>1: Shared authentication<br/>2: Reserved Fields<br/>3:WPA-PSK<br/>4: WPA<br/>5: WPA2-PSK<br/>6: WPA2<br/>7: WPA/WPA2<br/>8: WPAPSK/WPA2PSK |
| wpa\_psk\_key | string | \[8,63] Characters | WPA/WPA2 PSK key. This option is valid only when the authentication method is WPA-PSK,WPA2-PSK,WPAPSK/WPA2PSK |
| ap\_max\_associations | integer | \[1, 128] | maximum number of clients |
| ap\_wpa\_group\_rekey | integer | \[600, 86400] | group Password Negotiation Time |
| ap\_isolate | integer | \[0,1] | AP isolating switch, 0 off, 1 on |
| ap\_band | integer | \[0,1] | Radio band, 0 is 2.4G,1 is 5G |
| ap\_radio\_type | integer | 0: 802.11b/g,<br/>1: 802.11b<br/>2: 802.11a<br/>4: 802.11g<br/>6: 802.11n<br/>7: 802.11g/n<br/>8: 802.11an/ac<br/>9: 802.11b/g/n,<br/>11: 802.11na | when the wireless frequency band is 2.4G, the drop-down options are: 0,1, 4,6, 7,9; When the wireless frequency band is 5G, the drop-down options are: 2,8, 11 |
| ap\_channel | integer | \[1, 11] | channel |
| encrypt\_mode | integer | \[0,4] | encryption Method<br/>0: Do not encrypt<br/>1: WEP40<br/>2: WEP104<br/>3: TKIP<br/>4: AES |
| wep\_key | string | \[0,16] character | network Key |
| ap\_radius\_ip | string | \[1, 16] characters | IP address of the radius server |
| ap\_radius\_port | integer | \[1, 65535] | port number of the radius server |
| ap\_radius\_key | string | \[1, 32] characters | shared key for radius server |
| ap\_radius\_srcif | string | \[1, 16] characters | name of the interface connected to the radius server |
| ap\_bandwidth | integer | 0,1,3 | wireless bandwidth<br/>0:20MHz<br/>1:40MHz<br/>3:80MHz |
| sta\_default\_route | integer | \[0,1] | when the mode is station, add the default route based on WLAN, 0 does not add, 1 adds |
| sta\_ssid | string | \[1, 64] characters | ssid name to be connected when the mode is station |
| sta\_auth\_method | integer | \[0,6] | authentication Method<br/>0: No certification<br/>1: Shared Certification<br/>2: Reserved Unused<br/>3: WPA-PSK certification<br/>4: WPA certification<br/>5: WPA2-PSK certification<br/>6: WPA2 certification |
| sta\_auth\_mode | integer | 1 | authentication mode (WPA/WPA2 mode needs to be configured)<br/>1: EAP-PEAP |
| sta\_iner\_auth | integer | \[1, 2] | Internal authentication (WPA/WPA2 mode needs to be configured)<br/>1:mschapv2<br/>2: md5 |
| sta\_username | string |  | user name (to be configured in WPA/WPA2 mode) |
| sta\_password | string |  | password (to be configured in WPA/WPA2 mode) |
| sta\_dhcp | integer | \[0,1] | whether to enable static IP:<br/>0: use static IP<br/>1: Do not use static IP, use DHCP to obtain IP address |
| ip\_addr | string | \[0,16] character | static IP address set when static IP is enabled |
| netmask | string | \[0,16] character | subnet mask set when static IP is enabled |

#### query Station configuration

interface

```http
GET v1/dot11radio/config?iface=dot11radio1
```

response

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

| Attribute | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1]  | WLAN switch, 0 off, 1 on  |
| station\_role  | integer  | \[0,1]  | Wi-Fi working mode <br/>0:AP <br/>1:Station  |
| ap\_ssid  | string  | \[1, 32] characters  | ssid name in AP mode  |
| ap\_ssid\_broadcast  | integer  | \[0,1]  | SSID broadcast switch, 0 is off, 1 is on  |
| auth\_method  | integer  | \[0, 8]  | authentication Method <br/>0: No certification <br/>1: Shared authentication <br/>2: Reserved Fields <br/>3:WPA-PSK<br/>4: WPA <br/>5: WPA2-PSK <br/>6: WPA2 <br/>7: WPA/WPA2 <br/>8: WPAPSK/WPA2PSK  |
| wpa\_psk\_key  | string  | \[8,63] Characters  | WPA/WPA2 PSK key. This option is valid only when the authentication method is WPA-PSK,WPA2-PSK,WPAPSK/WPA2PSK  |
| ap\_max\_associations  | integer  | \[1, 128]  | maximum number of clients  |
| ap\_wpa\_group\_rekey  | integer  | \[600, 86400]  | group Password Negotiation Time  |
| ap\_isolate  | integer  | \[0,1]  | AP isolating switch, 0 off, 1 on  |
| ap\_band  | integer  | \[0,1]  | radio band, 0 is 2.4G,1 is 5G |
| ap\_radio\_type  | integer  | 0: 802.11b/g, <br/>1: 802.11b <br/>2: 802.11a <br/>4: 802.11g <br/>6: 802.11n <br/>7: 802.11g/n <br/>8: 802.11an/ac <br/>9: 802.11b/g/n, <br/>11: 802.11na  | when the wireless frequency band is 2.4G, the drop-down options are: 0,1, 4,6, 7,9; When the wireless frequency band is 5G, the drop-down options are: 2,8, 11  |
| ap\_channel  | integer  | \[1, 11]  | channel  |
| encrypt\_mode  | integer  | \[0,4]  | encryption Method <br/>0: Do not encrypt <br/>1: WEP40 <br/>2: WEP104 <br/>3: TKIP <br/>4: AES  |
| wep\_key | string  | \[0,16] character  | network Key  |
| ap\_radius\_ip  | string  | \[1, 16] characters  | IP address of the radius server  |
| ap\_radius\_port  | integer  | \[1, 65535]  | port number of the radius server  |
| ap\_radius\_key  | string  | \[1, 32] characters  | shared key for radius server  |
| ap\_radius\_srcif  | string  | \[1, 16] characters  | name of the interface connected to the radius server  |
| ap\_bandwidth  | integer  | 0,1,3  | wireless bandwidth <br/>0:20MHz <br/>1:40MHz <br/>3:80MHz  |
| sta\_default\_route  | integer | \[0,1]  | when the mode is station, add the default route based on WLAN, 0 does not add, 1 adds  |
| sta\_ssid  | string  | \[1, 64] characters  | ssid name to be connected when the mode is station  |
| sta\_auth\_method  | integer  | \[0,6]  | authentication Method <br/>0: No certification <br/>1: Shared Certification <br/>2: Reserved Unused <br/>3: WPA-PSK certification <br/>4: WPA certification <br/>5: WPA2-PSK certification <br/>6: WPA2 certification  |
| sta\_auth\_mode  | integer  | 1  | authentication mode (WPA/WPA2 mode needs to be configured) <br/>1: EAP-PEAP  |
| sta\_iner\_auth  | integer  | \[1, 2]  | internal authentication (WPA/WPA2 mode needs to be configured) <br/>1:mschapv2 <br/>2: md5  |
| sta\_username  | string  |  | user name (to be configured in WPA/WPA2 mode)  |
| sta\_password  | string  |  | password (to be configured in WPA/WPA2 mode)  |
| sta\_dhcp  | integer  | \[0,1]  | whether to enable static IP: <br/>0: use static IP <br/>1: Do not use static IP, use DHCP to obtain IP address  |
| ip\_addr  | string  | \[0,16] character  | static IP address set when static IP is enabled  |
| netmask  | string  | \[0,16] character  | subnet mask set when static IP is enabled  |

#### query Station status

interface

```http
GET v1/dot11radio/status?iface=dot11radio1
```

response

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

| Attribute  | Type  | Range | Description  |
| --- | --- | --- | --- |
| station\_role  | string  | \[0,1]  | Wi-Fi mode <br/>0: AP <br/>1: Station  |
| status  | integer  | \[0,1]  | Wi-Fi Status <br/>0: Closed <br/>1: Open  |
| mac\_addr  | string  | 17 characters  | MAC address of the Wi-Fi interface  |
| encrypt\_method  | integer  | \[0,4]  | encryption Method <br/>0: Do not encrypt <br/>1: WEP40 <br/>2: WEP104 <br/>3: TKIP <br/>4: AES  |
| sta\_ssid  | integer  | \[1, 32]  | SSID name of the connection |
| sta\_connection  | integer  | \[0,1]  | connection status: <br/>0: Not connected <br/>1: Connected  |
| sta\_auth\_method  | integer  | \[0,6]  | authentication Method <br/>0: No certification <br/>1: Shared Certification <br/>2: Reserved Unused <br/>3: WPA-PSK certification <br/>4: WPA certification <br/>5: WPA2-PSK certification <br/>6: WPA2 certification  |
| sta\_gateway  | string  | \[1, 16] characters  | the Gateway address of the Wi-Fi interface, that is, the IP address of the AP.  |
| sta\_dns  | string  | \[1, 16] characters  | dns address obtained from the Wi-Fi interface  |
| sta\_connect\_time  | integer  | \[0, 4294967296] | Wi-Fi connection duration  |
| ip\_addr  | string  | \[1, 16] characters  | IP address of the Wi-Fi interface  |
| netmask  | string  | \[1, 16] characters  | subnet mask of the Wi-Fi interface  |

#### update AP configuration

interface

```http
PUT v1/dot11radio/config?autosave=1
```

load

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1]  | WLAN switch, 0 off, 1 on  |
| station\_role  | integer  | \[0,1]  | Wi-Fi working mode <br/>0:AP <br/>1:Station  |
| ap\_ssid  | string  | \[1, 32] characters | ssid name in AP mode  |
| ap\_ssid\_broadcast  | integer  | \[0,1]  | SSID broadcast switch, 0 is off, 1 is on  |
| auth\_method  | integer  | \[0, 8]  | authentication Method <br/>0: No certification <br/>1: Shared authentication <br/>2: Reserved Fields <br/>3:WPA-PSK <br/>4: WPA <br/>5: WPA2-PSK <br/>6: WPA2 <br/>7: WPA/WPA2 <br/>8: WPAPSK/WPA2PSK  |
| wpa\_psk\_key  | string  | \[8,63] Characters  | WPA/WPA2 PSK key. This option is valid only when the authentication method is WPA-PSK,WPA2-PSK,WPAPSK/WPA2PSK  |
| ap\_max\_associations  | integer  | \[1, 128]  | maximum number of clients |
| ap\_wpa\_group\_rekey  | integer  | \[600, 86400]  | group Password Negotiation Time  |
| ap\_isolate  | integer  | \[0,1]  | AP isolating switch, 0 off, 1 on  |
| ap\_band  | integer  | \[0,1]  | radio band, 0 is 2.4G,1 is 5G  |
| ap\_radio\_type  | integer  | 0: 802.11b/g, <br/>1: 802.11b <br/>2: 802.11a <br/>4: 802.11g <br/>6: 802.11n <br/>7: 802.11g/n <br/>8: 802.11an/ac <br/>9: 802.11b/g/n, <br/>11: 802.11na  | when the wireless frequency band is 2.4G, the drop-down options are: 0,1, 4,6, 7,9; When the wireless frequency band is 5G, the drop-down options are: 2,8, 11  |
| ap\_channel | integer  | \[1, 11]  | channel  |
| encrypt\_mode  | integer  | \[0,4]  | encryption Method <br/>0: Do not encrypt <br/>1: WEP40 <br/>2: WEP104 <br/>3: TKIP <br/>4: AES  |
| wep\_key  | string  | \[0,16] character  | network Key  |
| ap\_radius\_ip  | string  | \[1, 16] characters  | IP address of the radius server  |
| ap\_radius\_port  | integer  | \[1, 65535]  | port number of the radius server  |
| ap\_radius\_key  | string  | \[1, 32] characters  | shared key for radius server  |
| ap\_radius\_srcif | string  | \[1, 16] characters  | name of the interface connected to the radius server  |
| ap\_bandwidth  | integer  | 0,1,3  | wireless bandwidth <br/>0:20MHz <br/>1:40MHz <br/>3:80MHz  |
| sta\_default\_route  | integer  | \[0,1]  | when the mode is station, add the default route based on WLAN, 0 does not add, 1 adds  |
| sta\_ssid  | string  | \[1, 64] characters  | ssid name to be connected when the mode is station  |
| sta\_auth\_method  | integer  | \[0,6]  | authentication Method <br/>0: No certification <br/>1: Shared Certification <br/>2: Reserved Unused <br/>3: WPA-PSK certification <br/>4: WPA certification<br/>5: WPA2-PSK certification <br/>6: WPA2 certification  |
| sta\_auth\_mode  | integer  | 1  | authentication mode (WPA/WPA2 mode needs to be configured) <br/>1: EAP-PEAP  |
| sta\_iner\_auth  | integer  | \[1, 2]  | internal authentication (WPA/WPA2 mode needs to be configured) <br/>1: mschapv2 <br/>2: md5  |
| sta\_username  | string  |  | user name (to be configured in WPA/WPA2 mode)  |
| sta\_password  | string  |  | password (to be configured in WPA/WPA2 mode)  |
| sta\_dhcp  | integer  | \[0,1]  | whether to enable static IP: <br/>0: use static IP <br/>1: Do not use static IP, use DHCP to obtain IP address  |
| ip\_addr | string  | \[0,16] character  | static IP address set when static IP is enabled  |
| netmask  | string  | \[0,16] character  | subnet mask set when static IP is enabled  |

#### query AP configuration

interface

```http
GET v1/dot11radio/config?iface=dot11radio1
```

response

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

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1]  | WLAN switch, 0 off, 1 on  |
| station\_role  | integer  | \[0,1]  | Wi-Fi working mode <br/>0:AP <br/>1:Station  |
| ap\_ssid  | string  | \[1, 32] characters  | ssid name in AP mode  |
| ap\_ssid\_broadcast | integer  | \[0,1]  | SSID broadcast switch, 0 is off, 1 is on  |
| auth\_method  | integer  | \[0, 8]  | authentication Method <br/>0: No certification <br/>1: Shared authentication <br/>2: Reserved Fields <br/>3:WPA-PSK <br/>4: WPA <br/>5: WPA2-PSK <br/>6: WPA2 <br/>7: WPA/WPA2 <br/>8: WPAPSK/WPA2PSK  |
| wpa\_psk\_key  | string  | \[8,63] Characters  | WPA/WPA2 PSK key. This option is valid only when the authentication method is WPA-PSK,WPA2-PSK,WPAPSK/WPA2PSK  |
| ap\_max\_associations  | integer  | \[1, 128]  | maximum number of clients  |
| ap\_wpa\_group\_rekey  | integer | \[600, 86400]  | group Password Negotiation Time  |
| ap\_isolate  | integer  | \[0,1]  | AP isolating switch, 0 off, 1 on  |
| ap\_band  | integer  | \[0,1]  | radio band, 0 is 2.4G,1 is 5G  |
| ap\_radio\_type  | integer  | 0: 802.11b/g, <br/>1: 802.11b <br/>2: 802.11a <br/>4: 802.11g <br/>6: 802.11n <br/>7: 802.11g/n <br/>8: 802.11an/ac <br/>9: 802.11b/g/n, <br/>11: 802.11na  | when the wireless frequency band is 2.4G, the drop-down options are: 0,1, 4,6, 7,9; When the wireless frequency band is 5G, the drop-down options are: 2,8, 11  |
| ap\_channel  | integer  | \[1, 11] | Channel  |
| encrypt\_mode  | integer  | \[0,4]  | encryption Method <br/>0: Do not encrypt <br/>1: WEP40 <br/>2: WEP104 <br/>3: TKIP <br/>4: AES  |
| wep\_key  | string  | \[0,16] character  | network Key  |
| ap\_radius\_ip  | string  | \[1, 16] characters  | IP address of the radius server  |
| ap\_radius\_port  | integer  | \[1, 65535]  | port number of the radius server  |
| ap\_radius\_key  | string  | \[1, 32] characters  | shared key for radius server  |
| ap\_radius\_srcif  | string  | \[1, 16] characters | Name of the interface connected to the radius server  |
| ap\_bandwidth  | integer  | 0,1,3  | wireless bandwidth <br/>0:20MHz <br/>1:40MHz <br/>3:80MHz  |
| sta\_default\_route  | integer  | \[0,1]  | when the mode is station, add the default route based on WLAN, 0 does not add, 1 adds  |
| sta\_ssid  | string  | \[1, 64] characters  | ssid name to be connected when the mode is station  |
| sta\_auth\_method  | integer  | \[0,6]  | authentication Method <br/>0: No certification <br/>1: Shared Certification <br/>2: Reserved Unused <br/>3: WPA-PSK certification <br/>4: WPA certification <br/>5: WPA2-PSK certification <br/>6: WPA2 certification |
| sta\_auth\_mode  | integer  | 1  | authentication mode (WPA/WPA2 mode needs to be configured) <br/>1: EAP-PEAP  |
| sta\_iner\_auth  | integer  | \[1, 2]  | internal authentication (WPA/WPA2 mode needs to be configured) <br/>1: mschapv2 <br/>2: md5  |
| sta\_username  | string  |  | user name (to be configured in WPA/WPA2 mode)  |
| sta\_password  | string  |  | password (to be configured in WPA/WPA2 mode)  |
| sta\_dhcp  | integer  | \[0,1]  | whether to enable static IP: <br/>0: use static IP <br/>1: Do not use static IP, use DHCP to obtain IP address  |
| ip\_addr  | string  | \[0,16] character | Static IP address set when static IP is enabled  |
| netmask  | string  | \[0,16] character  | subnet mask set when static IP is enabled  |

#### query AP status

interface

```http
GET v1/dot11radio/status?iface=dot11radio1
```

response

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

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| station\_role  | string  | \[0,1]  | Wi-Fi mode <br/>0: AP <br/>1: Station  |
| status  | integer  | \[0,1]  | Wi-Fi Status <br/>0: Closed <br/>1: Open  |
| mac\_addr  | string  | 17 characters  | MAC address of the Wi-Fi interface  |
| ap\_ssid  | string | \[1,32] characters  | name of AP SSID  |
| ap\_channel  | integer  | \[1, 11]  | channel |

### Loopback

### Loopback

#### update Configuration

interface

```http
PUT v1/loopback/config?autosave=1
```

load

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| ip\_addr  | string  | \[1, 16] characters  | loopback port IP address  |
| netmask  | string  | \[1, 16] characters  | interface Subnet Mask  |
| description | string  | \[0,32] characters  | interface Description Information  |
| multi\_ip  | object  | | call back information from IP  |

#### query Configuration

interface

```http
GET v1/loopback/config
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| ip\_addr  | string  | \[1, 16] characters  | loopback port IP address  |
| netmask  | string  | \[1, 16] characters  | interface Subnet Mask  |
| description  | string  | \[0,32] characters  | interface Description Information  |
| multi\_ip  | object  | | call back information from IP  |

## network Services

### DHCP server

#### Update Configuration

interface

```http
PUT v1/dhcp/services/config?autosave=1
```

load

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| dhcp\_services  | object  |  | DHCP Server configuration  |
| enable  | integer  | \[0,1]  | DHCP Server switch, 0 off, 1 on  |
| start\_addr  | string  | \[1, 16] characters  | start address of DHCP address pool  |
| end\_addr  | string  | \[1, 16] characters  | end address of DHCP address pool  |
| lease  | integer  | \[30, 10080] minutes  | lease Duration  |
| windows\_name\_server  | string | \[1, 16] characters  | Windows name server  |
| macip\_bind\_config  | object  |  | MAC and IP binding configuration  |
| mac\_addr  | string  | \[1,18] character  | MAC address to be bound  |
| ip\_addr  | string  | \[1, 16] characters  | IP address to be bound  |
| dhcp\_relay\_enable  | integer  | \[0,1]  | whether to enable DHCP Relay, 0 off, 1 on  |
| isChecked  | interger  | \[0,1]  | whether to enable IP address conflict detection, fixed at 1  |

#### query Configuration

interface

```http
GET v1/dhcp/services/config
```

response

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

parameters

| Attribute  | Type  | Range  | Description |
| --- | --- | --- | --- |
| dhcp\_services  | object  |  | DHCP Server configuration  |
| enable  | integer  | \[0,1]  | DHCP Server switch, 0 off, 1 on  |
| start\_addr  | string  | \[1, 16] characters  | start address of DHCP address pool  |
| end\_addr  | string  | \[1, 16] characters  | end address of DHCP address pool  |
| lease  | integer  | \[30, 10080] minutes  | lease Duration  |
| windows\_name\_server  | string  | \[1, 16] characters  | Windows name server  |
| macip\_bind\_config  | object  |  | MAC and IP binding configuration  |
| mac\_addr  | string | \[1,18] character  | MAC address to be bound  |
| ip\_addr  | string  | \[1, 16] characters  | IP address to be bound  |
| dhcp\_relay\_enable  | integer  | \[0,1]  | whether to enable DHCP Relay, 0 off, 1 on  |

### DNS service

the DNS service page is divided into domain name service and relay service.

#### Domain Name Service

##### update Configuration

interface

```http
v1/dns/server/config?autosave=1
```

load

```json
{
    "primary_dns": "8.8.8.8",
    "secondary_dns": "114.114.114.114"
}
```

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| primary\_dns  | string  | \[1, 16] characters  | preferred Domain Name Server  |
| secondary\_dns  | string  | \[1, 16] characters  | alternate Domain Name Server  |

##### query Configuration

Interface

```http
GET v1/dns/server/config
```

response

```json
{
    "results": {
        "primary_dns": "8.8.8.8",
        "secondary_dns": "114.114.114.114"
    }
}
```

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| primary\_dns  | string  | \[1, 16] characters  | preferred Domain Name Server  |
| secondary\_dns  | string  | \[1, 16] characters  | alternate Domain Name Server  |

#### relay Service

##### update Configuration

interface

```http
PUT v1/dns/relay/config?autosave=1
```

load

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1]  | DNS relay service switch, 0 off, 1 on  |
| dhcp\_enable  | integer  | \[0,1] | DHCP Server switch, 0 is turned off and 1 is turned on. Before calling this interface, query the status of DHCP Server. The values passed here remain the same.  |
| host\_ip\_relation  | object  |  | domain name and IP mapping  |
| host  | string  | \[1, 64] characters  |  |
| ip\_addr1  | string  | \[1, 16] characters  | the first IP address corresponding to the domain name  |
| ip\_addr2  | string  | \[1, 16] characters  | the second IP address corresponding to the domain name  |

##### query Configuration

interface

```http
GET v1/dns/relay/config
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1]  | DNS relay service switch, 0 off, 1 on  |
| dhcp\_enable | integer  | \[0,1]  | DHCP Server switch, 0 is turned off and 1 is turned on. Before calling this interface, query the status of DHCP Server. The values passed here remain the same.  |
| host\_ip\_relation  | object  |  | domain name and IP mapping  |
| host  | string  | \[1, 64] characters  |  |
| ip\_addr1  | string  | \[1, 16] characters  | the first IP address corresponding to the domain name  |
| ip\_addr2  | string  | \[1, 16] characters  | the second IP address corresponding to the domain name  |

## host List

#### query Status

interface

```http
v1/dhcp/services/status
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| interface  | string  | \[1, 32] characters | Name of the interface connected to the host  |
| mac\_addr  | string  | \[1,18] character  | host mac address  |
| ip\_addr  | string  | \[1, 16] characters  | host IP address  |
| host\_addr  | string  | \[1, 64] characters  | host Name  |
| lease  | string  | \[0, 10080] character  | the duration of the lease period when the host obtains the address through DHCP  |

## routing

the routing menu is divided into routing status and static routing configuration.

#### Routing Status

##### query Status

```http
GET v1/route/status
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| type  | string  | \[1, 16] characters | static: static route <br/>connected: Directly connected route  |
| interface  | string  | \[1, 16] characters  | name of the interface corresponding to the route  |
| destination  | string  | \[1, 16] characters  | the destination address of the route  |
| netmask  | string  | \[1, 16] characters  | subnet mask of the destination address of the route  |
| distance\_metric  | string  | \[1, 16] characters  | route distance and metric information  |
| gateway  | string  | \[1, 16] characters  | the IP address of the next hop.  |
| time  | string  | \[0,32] characters  |  |

#### static Routing

##### update Configuration

interface

```http
v1/route/static/config?autosave=1
```

load

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| destination  | string  | \[1, 16] characters  | the destination address of the route  |
| netmask  | string  | \[1, 16] characters  | subnet mask of the destination address of the route  |
| interface  | string  | \[1, 16] characters  | interface information corresponding to the route  |
| gateway  | string  | \[1, 16] characters  | the IP address of the next hop.  |
| distance  | integer  | \[2, 255]  | distance information of the route  |
| track  | integer  | \[1, 10]  | the track identifier of the route.  |

##### Query Configuration

interface

```http
GET v1/route/static/config
```

Response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| destination  | string  | \[1, 16] characters  | the destination address of the route  |
| netmask  | string  | \[1, 16] characters  | subnet mask of the destination address of the route  |
| interface  | string  | \[1, 16] characters  | interface information corresponding to the route  |
| gateway  | string  | \[1, 16] characters  | the IP address of the next hop.  |
| distance  | integer  | \[2, 255]  | distance information of the route  |
| track  | integer  | \[1, 10]  | the track identifier of the route. |

## Firewall

firewall contains access control list and network address translation two sub-functions

#### access Control List

##### update Configuration

interface

```http
PUT v1/firewall/acl/config?autosave=1
```

load

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| destination  | string  | \[1, 16] characters  | the destination address of the route  |
| netmask  | string  | \[1, 16] characters  | subnet mask of the destination address of the route  |
| interface  | string  | \[1, 16] characters  | interface information corresponding to the route  |
| gateway  | string  | \[1, 16] characters  | the IP address of the next hop.  |
| distance  | integer  | \[2, 255] | Distance information of the route  |
| track  | integer  | \[1, 10]  | the track identifier of the route.  |

##### Query Configuration

interface

```http
GET v1/firewall/acl/config
```

response

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

#### network Address Translation

##### update Configuration

interface

```http
PUT v1/firewall/nat/config?autosave=1
```

load

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

##### query Configuration

interface

```http
GET v1/firewall/nat/config
```

response

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

## edge Computing

### Python APP

#### install the Python APP

Since the Python APP installation package may be relatively large, the installation process needs to transmit the APP installation package in blocks. In this process, three types of interfaces need to be called:

1. block Transfer Start Interface

```http
GET /v1/files/before/app/import?md5=02c22f0493471e0bc3d25cbdf3893481&name=device_supervisor-V3.1.5.tar.gz
```

\*\*parameter Description \*\*

| \*\*parameter Name \*\* | \*\*parameter Description \*\* | \*\*parameter Type \*\* | \*\*value range \*\* |
| --- | --- | --- | --- |
| name  | name of the app installation package  | string  | |
| md5  | md5 value of the app installation package  | string | |

1. Block transfer interface

it is recommended to block the app installation package with a size of 5*1024*1024 bytes.

```http
POST /v1/files/app/import?type=app&sub_type=app&fileName=device_supervisor-V3.1.5.tar.gz&chunks=27&chunk=17&size=82408268&md5=02c22f0493471e0bc3d25
```

| \*\*Parameter Name \*\* | \*\*parameter Description \*\* | \*\*parameter Type \*\* | \*\*value range \*\* |
| --- | --- | --- | --- |
| type  | the type of the imported file. When installing python app, the value is app.  |  | |
| sub\_type  | the subtype of the import file. When installing python app, the value is app.  |  | |
| fileName  | name of the app installation package  |  | |
| chunks  | total number of blocks  |  | |
| chunk  | what chunk is the current package  |  | |
| size  | the total size of the app installation package, in bytes  |  | |
| md5  | md5 value of the app installation package  |  | |

1. merging blocks into app whole package interface

```http
POST /v1/files/merge/app/import
```

\*\*request Example \*\*

```json
{
    "data": {
        "name": "device_supervisor-V3.1.5.tar.gz",
        "total": 82408268
    }
}
```

parameter Description

| parameter Name  | parameter Description  | parameter Type  | value range  |
| --- | --- | --- | --- |
| name  | name of the app installation package |  | |
| total  | the size of the app installation package, in bytes  |  | |

#### delete Python APP

```http
POST /v1/python/agent/uninstall/app?autosave=1&app_name=device_supervisor
```

\*\*parameter Description \*\*

| parameter Name  | parameter Description  | parameter Type  | value range  |
| --- | --- | --- | --- |
| app\_name  | name of the app to be deleted  | string  | |

#### obtain the configuration of the Python APP

```http
GET /v1/python/agent/app/config
```

\*\*return Example \*\*

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

\*\*parameter Description \*\*

| parameter Name  | parameter Description  | parameter Type  | value range  |
| --- | --- | --- | --- |
| python\_engine  | configure the python engine on/off status  | numerical  | \[0,1];0 indicates that the python engine is disabled; 1 indicates that the python engine is enabled.  |
| enable  | python app on/off status  | numerical  | \[0,1];0 means to close the python app,1 means to open the python app.  |
| app\_name | The name of python app; The program will be automatically set after app installation;  | string  |  |
| app\_version  | version of python app; The program will be set automatically after app installation.  | String  | |
| sdk\_version  | the python sdk version that the python app depends on; The program is automatically set after the app is installed  | string  | |
| start\_args  | startup parameters of python app; The default is empty after app installation.  | String  | |
| log\_size  | log size of python app; The default is 1m after app installation.  | Numerical  | \[1,100], unit is M.  |
| microfrontend\_app  | whether python app is a micro front-end program, fixed to 1 after app installation;  | numerical  | fixed to 1  |
| log\_file\_num  | number of logs of python app; Fixed to 2 after app installation  | numerical  | \[1, 2]  |

#### update the configuration of a Python APP

```http
v1/python/agent/app/config?autosave=1
```

\*\*Request Example \*\*

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

\*\*parameter Description \*\*

| parameter Name  | parameter Description  | parameter Type  | value range  |
| --- | --- | --- | --- |
| python\_engine  | configure the python engine to enable/disable. Because the python app depends on the python engine, this configuration item needs to be configured as 1 to enable the python engine.  | Numerical  | \[0,1];0 indicates that the python engine is disabled; 1 indicates that the python engine is enabled.  |
| enable  | python app on/off;  | numerical  | \[0,1];0 means to close the python app,1 means to open the python app.  |
| app\_name  | configure the name of the python app;  | string  | this information is generated by the program after app installation and needs to be obtained from the interface for obtaining configuration. Cannot be configured as other values;  |
| app\_version  | configure the version of the python app;  | string  | this information is generated by the program after app installation and needs to be obtained from the interface for obtaining configuration. Cannot be configured as other values; |
| sdk\_version  | configure the python sdk version that the python app depends on;  | string  | this information is generated by the program after app installation and needs to be obtained from the interface for obtaining configuration. Cannot be configured as other values;  |
| start\_args  | python app startup parameters  | string  | |
| log\_size  | python app log size  | numerical  | \[1,100], unit is M.  |
| microfrontend\_app  | whether the flag is a micro front end; When configuring, the value of this parameter needs to be fixed to 1  | numerical  | fixed to 1  |
| log\_file\_num  | number of log files, fixed at 2  | numerical  | fixed to 2  |

***

\*\*response example \*\*

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

#### start/stop Python APP

```http
PUT /v1/python/agent/app/management?app_name=device_supervisor&action=start
```

\*\*parameter Description \*\*

| parameter Name  | parameter Description  | parameter Type  | value range  |
| --- | --- | --- | --- |
| app\_name | Name of the app that needs to be launched  | string  |  |
| action  | python app on/off;  | string  | start means to start the app;stop means to close the app  |

#### query the running status of a Python APP

```http
GET /v1/python/agent/app/status
```

***

\*\*response example \*\*

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

\*\*parameter Description \*\*

| parameter Name  | parameter Description  | parameter Type  | value range  |
| --- | --- | --- | --- |
| state  | running status of python app  | string  |  |

## system Management

### system Time

#### set Time Zone

interface

```http
PUT v1/system/timezone?autosave=1
```

load

```json
{
    "timezone": "UTC-8"
}
```

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| timezone  | string  | \[1, 32] characters  | time Zone Encoding  |

#### query Time Zone

interface

```http
GET v1/system/timeinfo
```

> In addition to time zone information, this interface also returns device time information.

Response

```json
{
    "results": {
        "device_time": "2024-08-02 15:58:14",
        "timezone": "UTC-8"
    }
}
```

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| timezone  | string  | \[1, 32] characters  | time Zone Encoding  |
| device\_time  | string  | \[1, 32] characters  | equipment Time  |

#### set time

interface

```http
PUT v1/system/settime
```

load

```json
{
    "device_time": "2024-08-01 16:00:17"
}
```

#### SNTP client

##### update Configuration

interface

```http
PUT v1/sntp/client/config?autosave=1
```

load

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1]  | SNTP switch, 0 off, 1 on |
| update\_interval  | integer  | \[60, 2592000 ] seconds  | SNTP The period of the synchronization time between the client and the server, unit s  |
| source\_ip  | string  | \[1, 16] characters  | the source IP address of the request message, which can be left blank, is automatically selected by the system.  |
| server\_addr  | string  | \[1, 64] characters  | address of the sntp server  |
| port  | port  | \[1, 65535]  | port of the sntp server  |

##### query Configuration

interface

```http
GET v1/sntp/client/config
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1] | SNTP switch, 0 off, 1 on  |
| update\_interval  | integer  | \[60, 2592000 ] seconds  | SNTP The period of the synchronization time between the client and the server, unit s  |
| source\_ip  | string  | \[1, 16] characters  | the source IP address of the request message, which can be left blank, is automatically selected by the system.  |
| server\_addr  | string  | \[1, 64] characters  | address of the sntp server  |
| port  | port  | \[1, 65535]  | port of the sntp server  |

#### NTP server

##### update Configuration

interface

```http
PUT v1/ntp/server/config?autosave=1
```

load

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable | integer  | \[0,1]  | NTP server switch, 0 off, 1 on  |
| master  | integer  | \[2, 15]  | NTP server hierarchy  |
| source\_interface  | string  | \[1, 16] characters  | the interface of the NTP server source listening, and source\_ip are selected, one is configured, and the other needs to be empty.  |
| source\_ip  | string  | \[1, 16] characters  | the IP address that the NTP server listens to, and source\_interface, one is configured, and the other needs to be empty.  |
| server\_addr  | string  | \[1, 64] characters  | NTP server address  |
| prefer\_ntp\_server  | integer  | \[0,1]  | primary server, 0 No, 1 Yes  |

##### query Configuration

interface

```http
GET v1/ntp/server/config
```

response

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

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1]  | NTP server switch, 0 off, 1 on  |
| master  | integer  | \[2, 15]  | NTP server hierarchy  |
| source\_interface  | string  | \[1, 16] characters  | the interface of the NTP server source listening, and source\_ip are selected, one is configured, and the other needs to be empty.  |
| source\_ip  | string  | \[1, 16] characters  | the IP address that the NTP server listens to, and source\_interface, one is configured, and the other needs to be empty.  |
| server\_addr  | string  | \[1, 64] characters  | NTP server address  |
| prefer\_ntp\_server  | integer | \[0,1]  | primary server, 0 No, 1 Yes  |

### system Log

#### query Log

interface

```http
GET v1/syslog/view?lines=20
```

> lines = 20 indicates that the latest 20 logs are returned. If all logs are returned, lines = all

response

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

> each array Member contains three elements, the first is the log level, the second is the time when the log is generated, and the third is the specific log content.

#### Update Configuration

interface

```http
PUT v1/syslog/config?autosave=1
```

load

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| log\_to\_remote\_enable  | integer  | \[0,1]  | send to remote log server switch, 0 off, 1 on  |
| history\_log\_size  | integer  | \[64,2048]KB  | history Log Size  |
| history\_log\_severity  | integer  | \[0, 7] | History Log Level <br/>0: Urgent <br/>1: The alarm <br/>2: Serious <br/>3: Error <br/>4: Warning <br/>5: Notice <br/>6: The Information <br/>7: Debugging  |
| server\_addr  | string  | \[1, 16] characters  | IP address of the remote log server  |
| server\_port  | integer  | \[1, 65535]  | port number of the remote log server  |
| log\_to\_console  | integer  | \[0,1]  | fixed to 0  |

### system Upgrade

#### import Firmware

interface

```http
POST v1/import/firmware
```

example

```shell
curl -k -X POST -H "Authorization: Bearer 6nwWSPQ6AEe18L4zi4sbr9SM0xJLI2nE" -F "file=@/home/nowlan/Temp/IG502.bin" https://10.5.30.206/v1/import/firmware
```

response

```json
{
    "results": "ok"
}
```

#### device restart

after the firmware is upgraded to the device, you need to restart the device to switch the version. For the device restart api, see `restart`-> `manual restart`chapter.

### Configuration Management

##### configure Auto Save

interface

```http
PUT v1/system/autosave?autosave=1
```

load

```json
{
    "auto_save": 1
}
```

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| auto\_save  | integer  | \[0,1]  | auto save switch, 0 off, 1 on  |

##### configure an encryption password

interface

```http
PUT v1/system/encrypt/password?autosave=1
```

load

```json
{
    "encrypt_passwd": 1
}
```

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| encrypt\_passwd  | integer  | \[0,1]  | encrypt plaintext password switch, 0 off, 1 on  |

##### querying System Configuration

interface

```http
GET v1/system/sysinfo
```

response

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

parameters

| Attribute  | Type  | Range | Description  |
| --- | --- | --- | --- |
| auto\_save  | integer  | \[0,1]  | auto save switch, 0 off, 1 on  |
| encrypt\_passwd  | integer  | \[0,1]  | encrypt plaintext password switch, 0 off, 1 on  |

##### restore factory settings

interface

```http
PUT /v1/system/restore/config
```

load

```json
{
    "restore_all_data": 1
}
```

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| restore\_all\_data  | integer  | \[0,1]  | whether to clear personal data, installed app;0 keep, 1 clear  |

### device Cloud Platform

#### Inhand Inconect Service

##### update Configuration

interface

```http
PUT v1/inconnect/config?autosave=1
```

load

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

parameters

| Attribute  | Type  | Range | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1]  | whether to enable the docking Inhand Connect platform function, 0 off, 1 on  |
| server\_addr  | string  | \[1, 64] characters  | platform Address  |
| register\_account  | string  | \[1, 64] characters  | the account connected to the platform, usually a mailbox, needs to be registered with the platform in advance.  |
| https\_proxy  | string  | \[1, 64] characters  | legacy field, blank  |
| http\_proxy  | string  | \[1, 64] characters  | legacy field, blank  |
| site\_name  | string  | \[1, 64] characters  | legacy field, blank  |
| asset\_number  | string | \[1, 64] characters  | legacy field, blank  |
| location\_type  | integer  | \[0,1]  | device location method, 0 using GPS,1 using cellular. Requires the device model to support cellular, GPS can be used.  |
| lbs\_upload\_interval  | integer  | \[60, 86400] seconds  | period of reporting the equipment location to the platform, unit second  |
| channel\_keepalive  | integer  | \[30, 3600] seconds  | the heartbeat period of the connection between the device and the platform, in seconds.  |
| dataflow\_upload\_interval  | integer  | \[3600, 86400] seconds  | period of reporting platform for cellular traffic information of equipment  |

##### query Configuration

interface

```http
GET v1/inconnect/config
```

response

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

parameters

| Attribute  | Type  | Range  | Description |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1]  | whether to enable the docking Inhand Connect platform function, 0 off, 1 on  |
| server\_addr  | string  | \[1, 64] characters  | platform Address  |
| register\_account  | string  | \[1, 64] characters  | the account connected to the platform, usually a mailbox, needs to be registered with the platform in advance.  |
| https\_proxy  | string  | \[1, 64] characters  | legacy field, blank  |
| http\_proxy  | string  | \[1, 64] characters  | legacy field, blank  |
| site\_name  | string  | \[1, 64] characters  | legacy field, blank  |
| asset\_number  | string  | \[1, 64] characters | Legacy field, blank  |
| location\_type  | integer  | \[0,1]  | device location method, 0 using GPS,1 using cellular. Requires the device model to support cellular, GPS can be used.  |
| lbs\_upload\_interval  | integer  | \[60, 86400] seconds  | period of reporting the equipment location to the platform, unit second  |
| channel\_keepalive  | integer  | \[30, 3600] seconds  | the heartbeat period of the connection between the device and the platform, in seconds.  |
| dataflow\_upload\_interval  | integer  | \[3600, 86400] seconds  | period of reporting platform for cellular traffic information of equipment  |

##### query Status

interface

```http
GET v1/inconnect/status
```

response

```json
{
    "results": {
        "status": "device_connected"
    }
}
```

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| status | string  | \[1, 32] characters  | connection status  |

#### Inhand Device Manager

##### update Configuration

interface

```http
v1/dm/config?autosave=1
```

load

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

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1]  | whether to enable the docking Inhand Device Manager platform function, 0 off, 1 on  |
| server\_addr  | string  | \[1, 64] characters  | platform Address  |
| register\_account  | string  | \[1, 64] characters  | the account connected to the platform, usually a mailbox, needs to be registered with the platform in advance.  |
| https\_proxy  | string  | \[1, 64] characters  | legacy field, blank  |
| http\_proxy | string  | \[1, 64] characters  | legacy field, blank  |
| site\_name  | string  | \[1, 64] characters  | legacy field, blank  |
| asset\_number  | string  | \[1, 64] characters  | legacy field, blank  |
| location\_type  | integer  | \[0,1]  | device location method, 0 using GPS,1 using cellular. Requires the device model to support cellular, GPS can be used.  |
| lbs\_upload\_interval  | integer  | \[60, 86400] seconds  | period of reporting the equipment location to the platform, unit second  |
| channel\_keepalive  | integer  | \[30, 3600] seconds  | the heartbeat period of the connection between the device and the platform, in seconds.  |
| dataflow\_upload\_interval  | integer | \[3600, 86400] seconds  | period of reporting platform for cellular traffic information of equipment  |
| conn\_mode  | integer  |  | legacy field, set to 0  |

##### query Configuration

interface

```http
GET v1/dm/config
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1]  | whether to enable the docking Inhand Device Manager platform function, 0 off, 1 on  |
| server\_addr  | string  | \[1, 64] characters  | platform Address  |
| register\_account  | string  | \[1, 64] characters  | the account connected to the platform, usually a mailbox, needs to be registered with the platform in advance.  |
| https\_proxy  | string  | \[1, 64] characters | Legacy field, blank  |
| http\_proxy  | string  | \[1, 64] characters  | legacy field, blank  |
| site\_name  | string  | \[1, 64] characters  | legacy field, blank  |
| asset\_number  | string  | \[1, 64] characters  | legacy field, blank  |
| location\_type  | integer  | \[0,1]  | device location method, 0 using GPS,1 using cellular. Requires the device model to support cellular, GPS can be used.  |
| lbs\_upload\_interval  | integer  | \[60, 86400] seconds  | period of reporting the equipment location to the platform, unit second  |
| channel\_keepalive  | integer  | \[30, 3600] seconds  | the heartbeat period of the connection between the device and the platform, in seconds. |
| dataflow\_upload\_interval  | integer  | \[3600, 86400] seconds  | period of reporting platform for cellular traffic information of equipment  |
| conn\_mode  | integer  |  | legacy field, set to 0  |

##### query Status

interface

```http
GET v1/dm/status
```

response

```json
{
    "results": {
        "status": "device_connected"
    }
}
```

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| status  | string  | \[1, 32] characters  | connection status  |

#### Inhand Cloud Service

##### update Configuration

interface

```http
PUT v1/devicelive/config?autosave=1
```

load

```json
{
    "mode": 1,
    "server_addr": "device.inhandcloud.cn",
    "channel_keepalive": 60,
    "config_source": 0
}
```

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| mode  | integer | \[0,1]  | switch to Inhand iSCADE Cloud, 0 off, 1 on  |
| server\_addr  | string  | \[1, 64] characters  | address of the platform  |
| channel\_keepalive  | integer  | \[30, 1200] seconds  | the heartbeat period of the connection between the device and the platform, in seconds.  |
| config\_source  | integer  | \[0,1]  | fixed to 0  |

##### query Configuration

interface

```http
GET v1/devicelive/config
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| mode  | integer  | \[0,1]  | switch to Inhand iSCADE Cloud, 0 off, 1 on  |
| server\_addr  | string | \[1, 64] characters  | address of the platform  |
| channel\_keepalive  | integer  | \[30, 1200] seconds  | the heartbeat period of the connection between the device and the platform, in seconds.  |
| config\_source  | integer  | \[0,1]  | fixed to 0  |

##### query Status

interface

```http
GET v1/devicelive/status
```

response

```json
{
    "results": {
        "status": 2
    }
}
```

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| status  | integer  | \[0,1]  | status of the connected platform <br/>0: Not connected <br/>1: Connecting <br/>2: Connected  |

#### management Tools

##### web/ssh/telnet update configuration

interface

```http
PUT v1/services/config?autosave=1
```

load

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

parameters

| Attribute | Type  | Range  | Description  |
| --- | --- | --- | --- |
| https.enable  | integer  | \[0,1]  | Web Server switch, 0 off, 1 on  |
| https.listen\_ip\_addr  | string  | \[1, 16] characters  | the address that the Web Server listens to. You can pass any or the IP address of the interface.  |
| https.port  | integer  | \[1, 65535]  | port number on which the Web Server listens  |
| https.remote\_access  | integer  | \[0,1]  | on remote control switch, 0 off, 1 on  |
| web\_login\_timeout  | integer  | \[100, 3600]  | the web idle timeout period, after idle reaches this value, will automatically exit the login.  |
| telnet.enable  | integer | \[0,1]  | Telnet Server switch, 0 off, 1 on  |
| telnet.listen\_ip\_addr  | string  | \[1, 16] characters  | the address that the Telnet Server listens to. You can pass any or the IP address of the interface.  |
| telnet.port  | integer  | \[1, 65535]  | Telnet Server listening port number  |
| telnet.remote\_access  | integer  | \[0,1]  | on remote control switch, 0 off, 1 on  |
| ssh.enable  | integer  | \[0,1]  | SSH Server switch, 0 off, 1 on  |
| ssh.listen\_ip\_addr  | string  | \[1, 16] characters  | SSH Server listening address, which can be transmitted to any or the IP address of the interface.  |
| ssh.port  | integer | \[1, 65535]  | SSH Server listening port number  |
| ssh.timeout  | integer  | \[1, 120]  | SSH connection timeout, after idle reaches this value, the connection will be automatically disconnected  |
| ssh.key\_mode  | integer  | \[0,0]  | key mode, fixed not 0, representing RSA  |
| ssh.key\_length  | integer  | 512, 1024, 2048, 4096  | key Length  |
| ssh.remote\_access  | integer  | \[0,1]  | on remote control switch, 0 off, 1 on  |

##### web/ssh/telnet query configuration

interface

```http
GET v1/services/config
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| https.enable | integer  | \[0,1]  | Web Server switch, 0 off, 1 on  |
| https.listen\_ip\_addr  | string  | \[1, 16] characters  | the address that the Web Server listens to. You can pass any or the IP address of the interface.  |
| https.port  | integer  | \[1, 65535]  | port number on which the Web Server listens  |
| https.remote\_access  | integer  | \[0,1]  | on remote control switch, 0 off, 1 on  |
| web\_login\_timeout  | integer  | \[100, 3600]  | the web idle timeout period, after idle reaches this value, will automatically exit the login.  |
| telnet.enable  | integer  | \[0,1]  | Telnet Server switch, 0 off, 1 on  |
| telnet.listen\_ip\_addr | string  | \[1, 16] characters  | the address that the Telnet Server listens to. You can pass any or the IP address of the interface.  |
| telnet.port  | integer  | \[1, 65535]  | Telnet Server listening port number  |
| telnet.remote\_access  | integer  | \[0,1]  | on remote control switch, 0 off, 1 on  |
| ssh.enable  | integer  | \[0,1]  | SSH Server switch, 0 off, 1 on  |
| ssh.listen\_ip\_addr  | string  | \[1, 16] characters  | SSH Server listening address, which can be transmitted to any or the IP address of the interface.  |
| ssh.port  | integer  | \[1, 65535]  | SSH Server listening port number  |
| ssh.timeout  | integer | \[1, 120]  | SSH connection timeout, after idle reaches this value, the connection will be automatically disconnected  |
| ssh.key\_mode  | integer  | \[0,0]  | key mode, fixed not 0, representing RSA  |
| ssh.key\_length  | integer  | 512, 1024, 2048, 4096  | key Length  |
| ssh.remote\_access  | integer  | \[0,1]  | on remote control switch, 0 off, 1 on  |

##### developer Mode Update Configuration

interface

```http
PUT v1/python/agent/engine?autosave=1
```

load

```json
{
    "debug_password": "123456",
    "debug_enable": 1,
    "fixed_passwd": 1,
    "debug_user": "developer"
}
```

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| debug\_enable  | integer  | \[0,1]  | whether to enable developer mode, 0 off, 1 on  |
| debug\_user  | string | \[1, 16] characters  | developer Mode User Name  |
| debug\_password  | string  | \[1, 32] characters  | developer Mode Password  |
| fixed\_passwd  | integer  | \[0,1]  | whether the firmware password is enabled, 0 off, 1 on  |

##### developer mode query configuration

interface

```http
GET v1/python/agent/status
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| debug\_enable  | integer  | \[0,1]  | whether to enable developer mode, 0 off, 1 on  |
| debug\_user  | string  | \[1, 16] characters  | developer Mode User Name  |
| debug\_password  | string  | \[1, 32] characters | Developer Mode Password  |
| fixed\_passwd  | integer  | \[0,1]  | whether the firmware password is enabled, 0 off, 1 on  |

### User Management

##### add User

interface

```http
POST v1/admind/user?autosave=1
```

load

```json
{
    "privilege": 15,
    "password": "Aa123456",
    "username": "testuser"
}
```

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| username  | string  | \[1, 16]  | user name of the new user  |
| password  | string  | \[1, 32] characters  | password for new user  |
| privilege  | integer  | \[1, 15]  | the permissions of the new user. The larger the value, the higher the permissions.  |

##### delete User

interface

```http
DELETE v1/admind/user?autosave=1&username=testuser
```

##### query User

interface

```http
GET v1/admind/user
```

response

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| username  | string  | \[1, 16]  | user Name  |
| password  | string  | \[1, 32] characters  | password  |
| privilege  | integer  | \[1, 15]  | permissions for the user  |
| administrator  | integer  | \[0,1]  | administrator account, 0 No, 1 Yes  |

### restart

##### timed restart

interface

```http
PUT v1/admind/cron/config?autosave=1
```

load

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

parameters

| Attribute  | Type  | Range  | Description  |
| --- | --- | --- | --- |
| enable  | integer  | \[0,1] | Whether to enable timing restart, 0 off, 1 on  |
| cron\_job  | string  | \[1, 16]  | fixed as reboot  |
| month  | integer  |  | fixed to 0  |
| week  | integer  |  | fixed to 0  |
| day  | integer  |  | fixed to 0  |
| hour  | integer  | \[0, 23]  | timed restart corresponding Hour  |
| minutes  | integer  | \[0, 59]  | minutes corresponding to the timing restart  |

##### manual restart

interface

```http
POST v1/system/reboot
```

### tools

#### ping

##### performing a ping operation

interface

```http
POST v1/system/reboot
```

load

```json
{
    "host": "www.baidu.com",
    "ping_count": 4,
    "packet_size": 32,
    "expert_options": ""
}
```

parameters

| Attribute  | Type | Range  | Description  |
| --- | --- | --- | --- |
| host  | string  | \[1, 64] characters  | the destination address of the ping probe  |
| ping\_count  | integer  | \[1, 50]  | number of ping messages sent  |
| packet\_size  | integer  | \[8, 1472] Byte  | the size of the ping message, in bytes  |
| expert\_options  | string  | \[1, 64]  | advanced Options  |

##### query ping results

interface

```http
GET v1/task/status?type=ping
```

response

```json
{
    "results": {
        "status": "success",
        "data": "PING www.baidu.com (39.156.66.18): 32 data bytes\n40 bytes from 39.156.66.18: seq=0 ttl=49 time=39.385 ms\n40 bytes from 39.156.66.18: seq=1 ttl=49 time=38.668 ms\n40 bytes from 39.156.66.18: seq=2 ttl=49 time=38.324 ms\n40 bytes from 39.156.66.18: seq=3 ttl=49 time=38.605 ms\n\n--- www.baidu.com ping statistics ---\n4 packets transmitted, 4 packets received, 0% packet loss\nround-trip min/avg/max = 38.324/38.745/39.385 ms\n"
    }
}
```

#### traceroute

##### performing a traceroute operation

interface

```http
POST v1/tools/traceroute
```

load

```json
{
    "host": "www.baidu.com",
    "maximum_hops": 20,
    "timeout": 3,
    "transmit_protocol": 0,
    "expert_options": ""
}
```

parameters

| Attribute  | Type  | Range  | Description |
| --- | --- | --- | --- |
| host  | string  | \[1, 64] characters  | the target address of the traceroute probe.  |
| maximum\_hops  | integer  | \[2, 40]  | max Hops  |
| timeout  | integer  | \[2, 10] seconds  | timeout, in seconds  |
| transmit\_protocol  | string  | UDP or ICMP  | agreement  |
| expert\_options  | string  | \[1, 64]  | advanced Options  |

##### query traceroute results

interface

```http
GET v1/task/status?type=traceroute
```

response

```json
{
    "results": {
        "status": "doing",
        "data": "traceroute to www.baidu.com (39.156.66.18), 20 hops max, 38 byte packets\n 1  10.5.30.254 (10.5.30.254)  2.901 ms  1.191 ms  0.728 ms\n 2  *"
    }
}
```

#### tcpdump packets capture

##### execute tcpdump to capture packets

interface

```http
POST v1/tools/tcpdump
```

load

```json
{
    "interface": "fastethernet 0/1",
    "capture_number": 20,
    "expert_options": "",
    "action": "capture"
}
```

parameters

| Attribute  | Type  | Range | Description  |
| --- | --- | --- | --- |
| interface  | string  | \[1, 16] characters  | based on which interface to capture packets  |
| capture\_number  | integer  | \[10, 1000]  | number of bag grabbing  |
| action  | string  | \[1, 16] characters  | fixed as capture  |
| expert\_options  | string  | \[1, 64]  | advanced Options |
