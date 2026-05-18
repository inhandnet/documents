InGateway Series

User's manual

(Applicable to IG500, IG900 series products)

Version V1.0, June 2024

[www.inhand.com](http://www.inhand.com.cn/)

![](images/img_9131ee8f.png)

The software described in this manual is according to the license agreement, can only be used in accordance with the terms of the agreement.

**Copyright Notice**

© 2024 InHand Networks All rights reserved.

**Trademarks**

The InHand logo is a registered trademark of InHand Networks.

All other trademarks or registered trademarks in this manual belong to their respective manufacturers.

**Disclaimer**

The company reserves the right to change this manual, and the products are subject to subsequent changes without prior notice.We shall not be responsible for any direct, indirect, intentional or unintentional damage or hidden trouble caused by improper installation or use.

# 1 Introduction

The InGateway series is an edge computing gateway for the industrial IoT sector from InHand. This series of products has rich interfaces and global cellular access capability. It supports users to use Python secondary development, and can be built-in InHand DeviceSupervisor™ Agent service, which supports hundreds of data collection protocols, and easily achieves device data collection, processing and cloud, and also supports InHand DeviceLive cloud management, helping enterprises to accelerate the process of digitisation.

The product models to which this manual applies are listed below:

| Product Model | Firmware version |
| --- | --- |
| IG502 | V2.1.23 and above |
| IG504 | \-- |
| IG532 | V2.1.9 and above |
| IG902 | V2.1.13 and above |
| IG974 | V2.0.6 and above |

# 2 Description of equipment configuration  

## 2.1 Access to the gateway

Connect to the IG using the following default IP address (address information is also available from the device panel)

| Ports | Default IP |
| --- | --- |
| Interface 1 | 192.168.1.1 |
| Interface 2 | 192.168.2.1 |

1.  Step 1: Set the IP address of the PC and the device network interface is in the same network segment, take the computer network interface plugged into the device interface 2 as an example    
    

1.  Method 1: Obtain an IP address automatically (recommended)  
    

![](images/img_5ab4a0dd.png)  

1.  Method 2: Use a fixed I address

            Select "Use the following IP address", enter the IP address (default is any value from 192.168.2.2 to 192.168.2.254), subnet mask (default is 255.255.255.0), default gateway (default is 192.168.2.1), and DNS server address, click <OK>.

![](images/img_3a57ebb7.png)  

1.  Step 2: Open a browser, access the IP address of Interface 2 of the IG and enter the login username and password.   
    

> Device factory default password:   
> 
> username: adm   
> 
> password: check the nameplate on the device panel for initial password information

![](images/img_e1256655.png)  

1.  Step 3: After successful login, you can see the overview page as shown below.  
    

![](images/img_57d966aa.png)  

## 2.2 Overview

This page provides an overview of the gateway's system status, system performance, system storage, network connectivity, network flow, and other information. This page allows you to get a quick overview of the device basics.  

1.  **Network Connection Status:** Show the network connection situation of IG and the network configuration  
    

1.  External Network: To configure the routing of data forwarding to an external network, click [](https://inhandnetworks.yuque.com/unup4w/cznaqm/csyzewggkogwkefw#8Xqy2)[Static Routing](https://help.inhand.com/portal/en/kb/articles/ig-series-user-s-manual-v1-0-12-8-2024#233_Routing:~:text=2.3.3.2%20Static%20Routing) page  
    
2.  Interface Network: To configure the interface, click the "Set UP" button after the interface to jump to the [Ethernet](https://help.inhand.com/portal/en/kb/articles/ig-series-user-s-manual-v1-0-12-8-2024#231_Network_Interface:~:text=the%20Expert%20Options.-,2.3.1.2%20Ethernet,-The%20%22Ethernet%22%20page) page.  
    

![](images/img_10442e9e.png)

1.  **Data usage Monitoring:** Show the flow usage in the last 24 hours and the last month, generating one piece of data per hour.

![](images/img_e2b2e417.png)

1.  **Performance & Storage:** Shows the device's current CPU, memory, Flash, MicroSD, USB usage  
    

![](images/img_20db853d.png)  

1.  **System Information: Click the "Edit" Botton to modify IG's Name**  
    

![](images/img_ebd8b427.png)  

## 2.3 Network

### 2.3.1 Network Interface

#### 2.3.1.1 Cellular

This page shows the current cellular status and configuration information of the gateway. You can configure the cellular network parameters by using the "Enable Cellular" button.

  

![](images/img_03b02980.png)  

  

The cellular network parameters are described below:

  

1.  Enable Cellular: Enable/Disable Cellular function  
    

  

1.  Profile: Profile for configuring the APN, username, password and authentication method when used for dialing with a decicated network card. If it is not a dedicated network card, you usually do not need to modify the configuration here. Up to 10 records can be added to the Profile.  
    

  

> 1.  Network Type: User selects the type of mobile network used by the device, GSM, CDMA can be selected.  
>     
> 
>   
> 
> 1.  APN: APN (Access Point Name) is used to identify the service type of WCDMA/LTE network, and the WCDMA/LTE system provides corresponding services according to the APN of the user connecting to the WCDMA/LTE network. Provided by the operator (this item is not set for CDMA2000 series).  
>     
> 
>   
> 
> 1.  Access Number: The dialling string used for dialling. The dialling string is provided by the operator, please obtain it from the operator.  
>     
> 
>   
> 
> > 1.  When the 3G/LTE data card supports WCDMA or LTE standard, the default dialling string is \*99\*\*\*1#.  
> >     
> > 
> >   
> > 
> > 1.  When the 3G data card supports the CDMA2000 standard, the default dialling string is #777.  
> >     
> 
>   
> 
> 1.  Auth Method  
>     
> 
> > 1.  Auto: automatically selects an authentication method  
> >     
> > 
> >   
> > 
> > 1.  PAP: Password Authentication Protocol, which provides a simple plaintext authentication method through two handshakes.  
> >     
> > 
> >   
> > 
> > 1.  CHAP: Challenge Handshake Authentication Protocol, which confirms the digest information through three handshakes for secure authentication.  
> >     
> > 
> >   
> > 
> > 1.  MS-CHAP: Microsoft's CHAP standard.  
> >     
> > 
> >   
> > 
> > 1.  MS-CHAPv2: An upgraded version of MS-CHAP, which requires two-way authentication.  
> >     
> 
>   
> 
> 1.  Username: Specifies the user name of the user accessing the external PDN network. Provided by the operator. The default username is gprs.  
>     
> 
>   
> 
> 1.  Password: Specifies the password for users accessing the external PDN network. Provided by the operator. The default username is gprs.

  

![](images/img_5a5c0ab0.png)

1.  Enable Dual SIM: Enable Dual SIM function. In order to improve the reliability of the network, dual SIM card single dialling is supported. 2 SIM cards need to be inserted on the device, which is disabled by default.  
    

  

> 1.  Select primary card: support SIM1, SIM2, random and sequence four ways  
>     
> 
>   
> 
> 1.  Max Number of Redials: when SIM1 has not dialled successfully within the set maximum dialling times, the device will switch to SIM2 for dialling.  
>     
> 
>   
> 
> 1.  Min Connected Time: When the device's dial-up connection success time is less than the set minimum connection time, the device's dial-up times are accumulated. When greater than the set minimum connection. The dialling times of the device will be cleared to zero. 0 is to disable this function  
>     
> 
>   
> 
> 1.  Backup SIM Timeout: If the current card is a backup sim, after the successful dialling of the backup sim, the device will switch to the main card for dialling when the set timeout time of the spare card is reached.  
>     

  

1.  Network Type: Auto, 2G, 3G, 4G, 5G and other networks can be selected. ((Note: different devices support different types of networks, you can check the corresponding product specifications)) Users can select a specific network mode according to the equipment used and the SIM card applicable, or use the automatic mode, the device can register itself to the network mode applicable to the current network conditions.  
    

  

1.  Profile: dialling policy selection, corresponding to the dialling parameter set configuration index item, if it is not a dedicated Network card, just select the default.  
    

  

1.  Roaming: Tick Enable Roaming, you can dial-up normally in roaming status, when cancelling the roaming option, the roaming SIM card can't dial-up; when using local card, ticking Roaming and cancelling Roaming won't affect the dial-up of the SIM card.  
    

  

1.  PIN code: PIN code is the personal identification number of the SIM card. If PIN code is enabled, the device will fail to dial up when no PIN code or wrong PIN code is set; and the device can dial up normally when normal PIN code is set.

![](images/img_7a908903.png)

  

1.  Static IP: Whether to use static IP when dialling, you can manually specify the IP address of the device. The device gets the configured static IP every time it dials.  
    

  

1.  Redial Interval: the amount of time the device waits to redial each time it drops.  
    

![](images/img_38937d08.png)  

1.  ICMP Probe: Cellular networks sometimes have the problem of dialling up successfully and obtaining an IP address, but not being able to access the Internet, which is usually resolved by redialling. ICMP Probe can be used to detect whether the network is working properly, and if the network is abnormal, a redial will be triggered to solve the problem of the network not being able to access the Internet. This feature is turned off by default and is recommended to be enabled when deploying a cellular network.  
    

  

1.  ICMP Probe Server: the remote IP address or domain name to be probed (to enable two ICMP probe servers at the same time, it is recommended that you enter both IP addresses or domain names at the same time). The device supports two ICMP probe servers: the primary server and the backup server. When two servers are configured, the first server is detected first, and the second server is detected only when the first server reaches the maximum number of retries. When both servers fail to detect, the device will redial and perform the next round of ICMP detection.  
    

  

1.  ICMP Probe Interval: the time interval between ICMP probe messages sent by the device.  
    

  

1.  ICMP Probe Timeout: If no ICMP response packet is received within the set ICMP Probe Timeout, it is considered that the ICMP Probe has timed out.  
    

  

1.  ICMP Probe Maximum Retries: Sets the maximum number of retries when an ICMP probe fails (the number will be redialled after the maximum number is reached).  
    

  

1.  ICMP Strict Detection: When ICMP Strict Detection is turned off, if there is traffic on the dial-up interface, ICMP probes are not sent to save traffic; when ICMP Strict Detection is turned on, ICMP probe messages are sent regardless of whether there is traffic on the dial-up interface.

![](images/img_e2c38004.png)  

  

1.  SMS: SMS function is used to set cellular parameters, query cellular status, configure io output and reboot the system.  
    

  

> 1.  Enable SMS: enable/disable SMS function  
>     
> 
>   
> 
> 1.  Reply result: When enabled, when the user configures the cellular via SMS, io or reboots the system, the device will reply with an SMS to inform whether the result of the configuration is successful or not.  
>     
> 2.  Query interval: the device will periodically query the received SMS, set the interval of periodic query here  
>     
> 
>   
> 
> 1.  Mobile number whitelist: only mobile phone numbers in the whitelist can send SMS to set cellular parameters and other information.

Details of the SMS configuration are given below:

1、SMS set cellular dialling parameters 

SMS format:

cellular slot=sim1 apn=hello username=abcd password=123456 network=4g dialnumber=\*99\*1 auth=pap  

The cellular dialling parameters are configured as described below:

1.  cellular: means set cellular service related parameters, the cellular keyword should be located at the beginning of the SMS content; the content after cellular is the cellular configuration item.  
    

1.  slot: flag to set which card's dialling parameter, the available values are: sim1 , sim2 ;  
    

1.  Mandatory parameter apn: Configure apn information;  
    

1.  Non-required parameter username: Configure the user name;  
    

1.  Non-required parameter password: Configure the password;  
    

1.  Non-required parameter auth: authentication method; settable values are: none , auto , pap , chap; strictly case-sensitive;  
    

1.  Non-required parameter network: configure the network system; the available values are: 2g , 3g , 4g , auto; strictly case-sensitive;  
    

1.  Non-required parameter dialnumber: dialling number; non-required parameter   
    

**Caveats:**

1.  At least 1 non-required parameter is required; the order of the parameters is not required, except for cellular, which must be at the beginning of the SMS content; each parameter is separated by a space;   
    

1.  Parameter names and some parameter values are strictly case sensitive;  
    

1.  If there is an unrecognised configuration item in the SMS content, for example icmp\_interval=10, the configuration will fail;   
    

1.  SMS content cannot exceed 140 characters in length;   
    

1.  Since the default parameter set is not allowed to be modified, when sim1/sim2 selects the default parameter set, the configuration of dialling parameters via SMS will fail   
    

  

2、SMS to restart the system

SMS format:

system command=reboot  

Reboot System Parameter Description:

1.  system: indicates the execution of system-related settings; the position of the system keyword needs to be at the beginning of the SMS content;   
    

1.  command: the command to be executed, can take the value: reboot; required parameters 

3、SMS query dialling information

SMS format:

status object=cellular  

Query Dialling Information Parameter Description:

1.  status: indicates the execution of the status query; the position of the status keyword needs to be at the beginning of the SMS content;   
    

1.  object: indicates which service's status should be queried, value: cellular; mandatory parameter 

After sending the enquiry SMS, you will receive an SMS with the following content: 

cellular\_status signal=none network=4g hostname=EdgeGateway uptime=150 ip=10.48.104.247 

The response content parameters are described below:

1.  cellular\_status: Status of the cellular   
    

1.  signal: signal quality of the cellular; can take values: none , poor , moderate , good , great   
    

1.  network: network standard; values: 2g , 3g , 4g , unknown   
    

1.  hostname: hostname of the device   
    

1.  ip: ip address of the dial-up interface   
    

1.  uptime: startup time of the device, in s 

4、SMS device digital output DO

SMS format:

io do0=1 do1=1 do2=0 do3=0  

DO Setup Parameter Description:

1.  io: means to set the parameters related to io service, the position of the io keyword needs to be at the beginning of the SMS content   
    

1.  do0~do3: configure the output of do0~do3, you can configure more than one do, there is no order requirement between the configuration items, for example, you can configure this way: io do0=1 do1=1 do3=0 do2=0; you can also configure only one do, for example, io do0=1; at least you need to configure 1 do; the value of do can only be 0 or 1 

5、Changes in DI for SMS reception 

To use this feature, you need to configure the mobile phone number to receive SMS on the io page and add the mobile phone number to the whitelist on the dialling page.

![](images/img_40562204.png)  

The user's mobile phone number receives an SMS with the following content after the value of di changes: 

io\_status sn=GL5022221013941 di0=0 timestamp=2024-05-15T10:03:12+0000 

Note: Currently, only the basic models IG502-FF53 and IG502-FQ58 support the SMS function, e.g. IG502-FQ58-W-G, IG502-FF53-IO-W-G. Please refer to the Ordering Information section in the datasheet for the specific models.  

![](images/img_601712cc.png)  

1.  Advanced Settings  
    

> 1.  Initial Commands: you can configure some AT commands to query the module status.  
>     
> 
> 1.  RSSI Poll Interval: After the device dials up successfully, it will query the signal status regularly with the set query interval time, such as setting the RSSI Poll Interval as 60s. For example, if the RSSI Poll Interval is set to 60s, after the device dials up, unplug the device antenna and wait for 60s, the signal of the device should be lowered, and the signal of the device will not be changed within 60s. 0 means disabled.  
>     
> 
> 1.  Dial Timeout: If the device does not dial successfully within the set Dial Timeout, it is considered as dialling timeout, and the device re-detects the module and re-dials.  
>     
> 
> 1.  MRU: Maximum Receive Unit, in bytes.  
>     
> 
> 1.  MTU: Maximum Transmission Unit, in bytes.  
>     
> 
> 1.  Use Default Asyncmap: Enable/Disable the default Asyncmap  
>     
> 
> 1.  Use peer DNS: Use the DNS servers assigned in the dial-up network connection when enabled  
>     
> 
> 1.  LCP Interval: detects whether the dial-up connection is normal at specified intervals  
>     
> 
> 1.  LCP Max Retries: number of retries after detection of connection disconnection  
>     
> 
> 1.  Infinitely Dial Retry: when enabled, unlimited dialling retries if dialling fails  
>     
> 
> 1.  Debug: The system log will print more detailed information when debug mode is enabled.  
>     
> 
> 1.  Expert Options: You can configure the corresponding command parameters in the Expert Options.

#### 2.3.1.2 Ethernet

The "Ethernet" page shows the configuration and status information of the Ethernet interface of the device, and you can configure the Ethernet interface parameters or view the detailed status information on this page. The steps to configure the Ethernet interface are as follows:  

1.  Select "Network > Network Interface > Ethernet/LAN/WAN" to enter the Ethernet interface configuration interface (different models of IG series devices are equipped with different types and numbers of interfaces, but the configuration method is the same).
2.  Select the network type of the interface.
3.  Select or enter each parameter in turn
4.  Click "Submit".

Take the IG902 as an example, the IG902 has two Gigabit Ethernet ports, the specific configuration and description are as follows

Configure dynamic address acquisition for the interface (network type selected as DHCP) as shown below:

![](images/img_44c8f225.png)  

  

1.  Network Type

1.  Dynamic address (DHCP): Configure the interface as a DHCP client, using DHCP to obtain IP address and subnet mask and other information  
    

1.  Description: descriptive information of the Ethernet interface, identifying the role.

Configure the interface with a static IP (network type is selected as static IP) as shown below:

![](images/img_409c6b94.png)

1.  Network Type (Static IP by default)

1.  Static IP: Manually configure the IP address and subnet mask for the Ethernet interface.  
    

1.  Primary IP Address: IP address of the Ethernet interface, customisable.  
    

1.  Netmask: Subnet mask of the Ethernet interface.  
    

1.  MTU: Maximum Transmission Unit, in bytes, default value is 1500.

![](images/img_9d34a06f.png)

If the interface type is WAN port, you can also set the gateway and DNS:

1.  Gateway: IP address of the device gateway  
    

1.  DNS: IP address for DNS can be specified manually  
    

1.  Speed/Duplex：  
    

> 1.  Auto Negotiation  
>     
> 
> 1.  1000M Full Duplex  
>     
> 
> 1.  1000M Half Duplex  
>     
> 
> 1.  100M Full Duplex  
>     
> 
> 1.  100M Half Duplex  
>     
> 
> 1.  10M Full Duplex  
>     
> 
> 1.  10M Half Duplex  
>     

1.  Track L2 State: when it is turned on, the state of the port without physical connection is Down, and when it is physically connected, it is UP; when it is turned off, the port displays UP when it is physically connected or not.  
    

1.  Shutdown: Disables the interface  
    

1.  Description: descriptive information of the Ethernet interface, identifying the role.  
    

1.  Secondary IP Settings: In addition to the master IP, users can also assign secondary IP addresses, up to a maximum of 10.

#### 2.3.1.3 WLAN

The "WLAN" page shows the IG's WLAN configuration and status information, where you can configure WLAN parameters or view detailed status information.

Note: Not all models of IG series support WLAN function, please refer to the official website [Resource Centre for](https://www.inhand.com/en/resources-center/#/IndustrialDigitalization/IoTEdgeGateways/IG502) specific support, and go to the corresponding product list to check the "Ordering Guide" section in the product specification.

Configure the WLAN as the access point as shown below:

![](images/img_aa190ca1.png)  

The parameters when configuring the WLAN as an access point are described below:

1.  Enable Wi-Fi: Enables or disables the WLAN service. Enabling WLAN service allows you to configure the basic parameters of the wireless network and security authentication options, enabling wireless access to the Internet.  
    

1.  Station Role: Select the WLAN mode of operation, here select the AP
2.  AP:  
    

> 1.  SSID Broadcast: enable SSID broadcasting after the wireless client can scan the SSID, disable that is, hide the SSID, SSID hidden, the device sends a beacon frame does not contain SSID information, access to the client must be manually configured in the wireless client to access the device SSID identification  
>     
> 
> 1.  Bridge: Bridges the WLAN to the bridge interface when enabled  
>     
> 
> 1.  Band: the AP's wireless band, different equipment models support different situations, details can be found in the product specifications   
>     
> 
> 1.  Radio Type: Different Radio types are supported by different wireless bands. Details can be found in the product datasheet  
>     
> 
> 1.  802.11b: operates in the 2.4G frequency band with a maximum speed of 11Mbps  
>     
> 
> 1.  802.11g: operates in the 2.4G band with a maximum speed of 54Mbps  
>     
> 
> 1.  802.11n: operates in the 2.4G band, but can also operate in the 5G band, with a theoretical maximum speed of 300Mbps.  
>     
> 
> 1.  Channel: A channel is a data signal transmission channel that uses wireless signals as a transmission medium. There are 13 channels in the 2.4G band, each with a different carrier frequency.  
>     
> 
> > 1.  Channel 1, centre frequency 2.412 GHz;  
> >     
> > 
> > 1.  Channel 2, centre frequency 2.417 GHz  
> >     
> > 
> > 1.  Channel 3, centre frequency 2.422GHz;  
> >     
> > 
> > 1.  Channel 4, centre frequency 2.427 GHz  
> >     
> > 
> > 1.  Channel 5, centre frequency 2.432GHz;  
> >     
> > 
> > 1.  Channel 6, centre frequency 2.437GHz  
> >     
> > 
> > 1.  Channel 7, centre frequency 2.442GHz;  
> >     
> > 
> > 1.  Channel 8, centre frequency 2.447 GHz  
> >     
> > 
> > 1.  Channel 9, centre frequency 2.452GHz;  
> >     
> > 
> > 1.  Channel 10, centre frequency 2.457 GHz  
> >     
> > 
> > 1.  Channel 11, centre frequency 2.462GHz;  
> >     
> > 
> > 1.  Channel 12, centre frequency 2.467GHz  
> >     
> > 
> > 1.  Channel 13, centre frequency 2.472GHz  
> >     
> 
> 1.  SSID: Service Set Identifier. SSID technology can divide a wireless LAN into several sub-networks that require different authentication, each sub-network has to be independently authenticated, and only authenticated users can enter the corresponding sub-network, preventing unauthorised users from entering the network.  
>     
> 
> 1.  Auth Method: Five authentication methods are available: OPEN, SHARED, WPA-PSK, WPA2-PSK, WPAPSK/WPA2PSK. encrypted authentication methods There are currently three authentication methods: WPA-PSK, WPA2-PSK, WPAPSK/WPA2PSK  
>     
> 
> 1.  Encrypt Mode: Support TKIP and AES encryption  
>     
> 
> 1.  WPA/WPA2 PSK key: authentication key, key length 8-63  
>     
> 
> 1.  Bandwidth: Specify the channel bandwidth corresponding to the AP radio frequency, e.g. 20MHz, 40MHz for 2.4G band.  
>     
> 
> 1.  Station Limit: Maximum number of clients the device can connect to at one time (up to 128)  
>     
> 
> 1.  Wpa Group Rekey Time: the time interval (in ms) between authentication and key exchange required by a client device when attempting to access the encrypted network

Configure the WLAN as a client as shown below:

![](images/img_148a4f08.png)  

The parameters when configuring the WLAN as a client are described below:

1.  Enable Wi-Fi: Enables or disables the WLAN service. Enabling WLAN service allows you to configure the basic parameters of the wireless network and security authentication options, enabling wireless access to the Internet.  
    

1.  Station Role: Select the WLAN operating mode, here select Client  
    

1.  Client Mode:  
    

> 1.  Client SSID: Fill in the name of the SSID that the gateway wants to connect to.  
>     
> 
> 1.  Auth Method: consistent with the authentication method of the SSID to which you want to connect  
>     
> 
> 1.  Encrypt Mode: consistent with the encryption method of the SSID to which you want to connect  
>     
> 
> 1.  WPA/WPA2 PSK key: consistent with the key of the SSID to which you want to connect  
>     
> 
> 1.  Network Type: Select the mode of obtaining IP address for the client, there are two kinds of static IP and dynamic address (DHCP).

#### 2.3.1.4 Loopback interface

A loopback interface is a logical, virtual interface on the device. After you create and configure a loopback interface, its address can be pinged or telnetted, which can be used to test network connectivity. You can configure or view the loopback interface parameters on the Loopback Interface page.  

![](images/img_479ffb62.png)  

1.  IP address: IP address of the loopback interface  
    

1.  Subnet Mask: Subnet mask of the loopback interface IP address

NOTE: A maximum of 10 slave IP addresses can be configured.

### 2.3.2 Network services

#### 2.3.2.1 DHCP services

DHCP uses a client/server communication model, in which the client requests an address from the server, and the server returns the IP address assigned to the client and related information (such as the lease period) to enable dynamic configuration of IP addresses and other information. You can set and view the configuration of the DHCP server on the DHCP Server page.

Start the dhcp server function on the interface to assign addresses to the downstream devices on that interface

![](images/img_ca67656e.png)  

1.  The DHCP server parameters are described below:  
    

> 1.  Enable DHCP service: enable/disable DHCP service.  
>     
> 
> 1.  Interface: select the corresponding interface, the type and number of interfaces supported by different devices are not the same, select according to the actual situation  
>     
> 
> 1.  Starting Address: Sets the starting IP address assigned to the client device in the address pool.  
>     
> 
> 1.  Ending Address: Sets the ending IP address assigned to the client device from the address pool.  
>     
> 
> 1.  Lease: Set the lease period of the assigned IP address, after the expiration date, the DHCP server will recall the IP address assigned to the client and re-assign the IP address, it cannot be empty.  
>     

1.  Windows Name Server (WINS): IP address of the WINS server.  
    

1.  Static IP Setting: If some scenarios require fixed IP addresses for some terminals, you can use the Static IP Setting function to bind the MAC of the terminal with the IP in the address pool, and the bound terminal will be assigned a fixed address every time it connects to the network, as shown in the following figure:

![](images/img_875d95b0.png)  

#### 2.3.2.2 DNS services

The Domain Name System (DNS) is a distributed database for TCP/IP applications that provides translation between domain names and IP addresses. With the DNS, users can use easy-to-remember, meaningful domain names for certain applications, and DNS servers in the network will resolve the domain names to the correct IP addresses. You can set up and view the domain name servers and DNS relay service in the "DNS Service" page.

Configure DNS servers to support up to two domain name servers, as shown in the following figure:  

![](images/img_e0ed1230.png)  

Configure the DNS relay service, as shown in the following figure:

     ![](images/img_fdd9ebb8.png)

Note: Enable the DNS relay service and do not disable the DNS relay service when DHCP server is enabled.

#### 2.3.2.3 GNSS

GNSS stands for Global Navigation Satellite System. Common GNSS systems include GPS (Global Positioning System) of the United States, GLONASS (GLONASS) of Russia, and BeiDou (BDS) of China. On the "GNSS" page, you can view the status of GNSS and configure GNSS.

Remarks:

Not all models of IG series support GNSS function, for details, please refer to the website [Resource Centre](https://www.inhand.com/en/resources-center/#/IndustrialDigitalization/IoTEdgeGateways/IG502), and enter the corresponding product list to check the "Ordering Guide" section in the product specification.

GNSS configuration

![](images/img_3a08b8bd.png)  

GNSS configuration page parameter descriptions:

1.  Enable GNSS: Enable/disable GNSS function  
    

1.  GNSS Type: select the appropriate satellite navigation system in the drop-down box  
    

> 1.  GPS: Global Positioning System  
>     
> 
> 1.  BDS: China's Beidou Satellite Navigation System  
>     
> 
> 1.  GLONASS: Russia's GLONASS satellite navigation system

GNSS IP Forwarding

![](images/img_567ad076.png)

The GNSS IP forwarding parameters are described below:

1.  Enable: enable/disable GNSS IP forwarding  
    

1.  Type: GNSS IP Forwarding Type  
    

> 1.  Client  
>     
> 
> > 1.  Transmit Protocol: Two protocols available, TCP and UDP.  
> >     
> > 
> > 1.  Connection Type: two types are available: Long-Lived and Short-Lived. Needs to be consistent with the server side  
> >     
> > 
> > 1.  Keepalive Interval: when the TCP connection is successfully established, the time interval between the device and the server for one heartbeat message interaction to determine whether the connection status is normal or not  
> >     
> > 
> > 1.  Keepalive Retry: after the heartbeat timeout, the number of times the heartbeat continues to be sent, when the set number of times the heartbeat still times out, the device disconnects the TCP connection.  
> >     
> > 
> > 1.  Min Reconnect Interval: the connection interval used when the device establishes a TCP connection, incremented every 30 seconds until the maximum reconnect interval is reached  
> >     
> > 
> > 1.  Max Reconnect Interval: Maximum time between reconnections when the device establishes a TCP connection.  
> >     
> > 
> > 1.  Source Interface: When the device connects to the server, it uses the address of the source interface as the source address to establish a TCP connection.  
> >     
> > 
> > 1.  Reporting Interval: the time interval for the device to report GNSS information.  
> >     
> > 
> > 1.  Include RMC: Whether to send RMC data for GNSS data  
> >     
> > 
> > 1.  Include GSA: Whether to send GSA data for GNSS data  
> >     
> > 
> > 1.  Include GGA: Whether to send GGA data for GNSS data  
> >     
> > 
> > 1.  Include GSV: whether to send GSV data for GNSS data or not  
> >     
> > 
> > 1.  Message Prefix: user-defined header content for GNSS messages sent by the device  
> >     
> > 
> > 1.  Message Suffix: user-defined message endings for GNSS messages sent by the device  
> >     
> > 
> > 1.  Destination IP address: IP of the server and port of the server

![](images/img_eca63383.png)  

1.  Server   
    

> 1.  Connection Type: two types are available,Long-Lived and Short-Lived. Needs to be consistent with the client  
>     
> 
> 1.  Keepalive Interval: when the TCP connection is successfully established, the time interval between the device and the client for one heartbeat message interaction to determine whether the connection state is normal or not  
>     
> 
> 1.  Keepalive Retry: after the heartbeat timeout, the number of times the heartbeat continues to be sent, when the heartbeat timeout reaches the set number of heartbeat retries, the device disconnects the TCP connection  
>     
> 
> 1.  Local Port: the service port number defined by the device when it is a TCP server.  
>     
> 
> 1.  Reporting Interval: the time interval for the device to report GNSS information to the server.  
>     
> 
> 1.  Include RMC: Whether to send PMC data for GNSS data  
>     
> 
> 1.  Include GSA: Whether to send GSA data for GNSS data  
>     
> 
> 1.  Include GGA: Whether to send GGA data for GNSS data  
>     
> 
> 1.  Include GSV: Whether to send GSV data for GNSS data  
>     
> 
> 1.  Message Prefix: user-defined header content for GNSS messages sent by the device  
>     
> 
> 1.  Message Suffix: user-defined message endings for GNSS messages sent by the device

GNSS Serial Forwarding

![](images/img_9efe6c8d.png)

The GNSS Serial Forwarding parameters are described below:

1.  Enable: Enable/disable GNSS serial port forwarding  
    

1.  Serial port type: consistent with the counterpart (RS232/RS485)  
    

1.  Baud rate: consistent with counterpart  
    

1.  Data bits: consistent with counterpart  
    

1.  Check digit: consistent with the counterpart  
    

1.  Stop bit: consistent with the counterpart  
    

1.  Software flow control: enable/disable software flow control  
    

1.  Include RMC: Whether to send RMC data for GNSS data  
    

1.  Include GSA: Whether to send GSA data for GNSS data  
    

1.  Include GGA: whether to send GGA data for GNSS data  
    

1.  Include GSV: whether to send GSV data for GNSS data or not

#### 2.3.2.4 Host List

You can view information about the hosts connected to IG on the Host List screen.

![](images/img_82e8789a.png)

### 2.3.3 Routing

#### 2.3.3.1 Routing status

Select "Network > Routing > Routing Status" to enter the "Routing Status" interface. You can view the detailed information of routes in this screen, as shown in the following figure:

![](images/img_bf157b09.png)

#### 2.3.3.2 Static Routing

You can manually set up a static route on the Static Routing page. After you set up a static route, messages to the specified destination will be forwarded in accordance with the path you specify.

Configure static routes as shown below:  

![](images/img_64bccc49.png)  

The static route parameters are described below:

1.  Destination network: the destination IP address/network segment to be reached  
    

1.  Subnet Mask: the subnet mask of the destination address to be reached  
    

1.  Interface: the outgoing interface through which the data reaches the destination network  
    

1.  Gateway: the gateway corresponding to the IP of the device's outgoing interface  
    

1.  Distance: overhead to the target network, smaller values are preferred  
    

1.  Track identification: index or ID of the Track (for Track configuration see: [3.3.2 Track module](https://help.inhand.com/portal/en/kb/articles/ig-series-user-s-manual-v1-0-12-8-2024#332_Track_module:~:text=immediately%20after%20configuration\)-,3.3.2%20Track%20module,-The%20purpose%20of))

### 2.3.4 Firewalls

#### 2.3.4.1 Access control lists

An ACL is an access control list that filters network interface data by configuring a series of matching rules to allow or disallow the passage of specified data streams (e.g., restricted source IP addresses, account numbers, etc.). You can set the filtering policy for network interface data in the "Access Control List" page.

Configure the standard access control policy, as shown in the following figure:

![](images/img_c475916f.png)  

1.  The standard access control policy parameters are described below:  
    

> 1.  ID: ACL rule ID, range 1-99, used to uniquely identify an access control policy  
>     
> 
> 1.  Sequence Number: ACL rule serial number, the saller the value, the higher the priority  
>     
> 
> 1.  Action: Permit/Deny messages to pass  
>     
> 
> 1.  Source IP: the source address of the matching message of the ACL rule, if it is empty, it means any, that is, all network segments.  
>     
> 
> 1.  Source Wildcard: The source address backmask of the ACL rule matching message, for example, if the source address segment is 192.168.2.0 and its mask is 255.255.255.0, then its backmask is 0.0.0.255.  
>     
> 
> 1.  Log: When enabled, the system records logs about access control.  
>     
> 
> 1.  Description: Used to provide a description of the ACL rule, making it easy to see at a glance what the ACL does.

Configure the extended access control policy as shown in the following figure:  

![](images/img_7360040c.png)  

1.  The Extended Access Control Policy parameters are described below:  
    

> 1.  ID: ACL rule ID, range 100-199   
>     
> 
> 1.  Sequence Number: ACL rule serial number, the smaller the value, the higher the priority  
>     
> 
> 1.  Action: Permit/Deny the passage of the message  
>     
> 
> 1.  Protocol: Access Control Protocol  
>     
> 
> 1.  Source IP: the source address of the ACL rule matching message, when it is empty, it means any, that is, all networks.  
>     
> 
> 1.  Source Wildcard: The source address backmask of the ACL rule matching message.  
>     
> 
> 1.  Source Port: source port number, any means any source port of TCP/UDP message matches. The source port number can only be specified if the protocol is TCP or UDP.  
>     
> 
> 1.  Destination IP: the destination address of the matching message of the ACL rule, if it is empty, it means any, that is, all networks.  
>     
> 
> 1.  Destination wildcard: the backmask of the destination address of the ACL rule match message.  
>     
> 
> 1.  Destination Port: Destination port number, any means any destination port of TCP/UDP message matches. The destination port number can only be specified if the protocol is TCP or UDP.  
>     
> 
> 1.  Established: when enabled, it controls the messages of established TCP connections, not the TCP messages of unestablished connections; when not enabled, it controls both established and unestablished TCP messages. This parameter can be configured only when the protocol is TCP.  
>     
> 
> 1.  Segment: Controls the message that is fragmented when the packet is sent out of the interface. (This is only available if the protocol type is IP.)  
>     
> 
> 1.  Log: When enabled, the system records logs about access control.  
>     
> 
> 1.  Description: Used to provide a description of the ACL rule, making it easy to see at a glance what the ACL does.

![](images/img_134fe88c.png)  

1.  The access control list parameters are described below:  
    

> 1.  Interface: the name of the interface that needs to set the access control policy  
>     
> 
> 1.  In ACL: Select an ACL rule for messages that enter from this interface and are then forwarded by the device  
>     
> 
> 1.  Out ACL: Select an ACL rule for messages forwarded through the device and whose egress is this interface.  
>     
> 
> 1.  Admin ACL: Select an ACL control rule for messages coming in from this interface with a destination address on the device itself, usually used to restrict access to this machine

#### 2.3.4.2 Network address translation

Network Address Translation (NAT) enables multiple hosts on a LAN to access the public network through one or more public IP addresses, i.e., using a small number of public IP addresses to represent a large number of private IP addresses, thus saving IP addresses on the public network. You can view and set the NAT rules in the Network Address Translation page.

As shown in the following configuration, configure the IG lower device to access the upper device through WAN:

![](images/img_a975c6f8.png)

The network address translation rule parameters are described below:

1.  Action  
    

> 1.  SNAT: Source Address Translation, translates the source address of an IP packet into another address. Generally used for data sent from inside the gateway to the outside.  
>     
> 
> 1.  DNAT: Destination Address Translation, converts the destination address of an IP packet to another address. Generally used for data sent from outside the gateway to the inside.  
>     
> 
> 1.  1:1NAT: Add one SNAT and one DNAT at the same time  
>     

1.  Source Network (supported when the action is SNAT and DNAT):  
    

> 1.  Internal: internal address  
>     
> 
> 1.  External: external address

In this example, the WAN port is the converted outgoing interface, so set the type of WAN to "Outside" interface.

![](images/img_8adc7a35.png)  

1.  Translation Type  
    

> 1.  IP to IP  
>     
> 
> 1.  IP to INTERFACE  
>     
> 
> 1.  IP PORT to IP PORT  
>     
> 
> 1.  ACL to INTERFACE  
>     
> 
> 1.  ACL to IP  
>     

1.  Match Conditions:  
    

> 1.  IP address: the IP address to be converted  
>     
> 
> 1.  Port: the port number where the conversion needs to be done  
>     
> 
> 1.  Access Control List: The access control lists that need to be converted are pre-configured in the "Access Control Lists".  
>     

1.  Translated Address  
    

> 1.  IP Address: converted IP address  
>     
> 
> 1.  Interface: Converts data to that interface for forwarding  
>     
> 
> 1.  Log: when turned on, logs related to network address translation will be printed in the log, which is turned off by default  
>     
> 
> 1.  Description: describes this NAT rule

### 2.3.5 VPN

Layer 2 Tunneling Protocol L2TP is a type of Virtual Private Dial-up Network VPDN tunneling protocol that extends the application of Point-to-Point Protocol PPP and is an important VPN technology for remote dial-up users to access the corporate headquarters network.

Note: Detailed configuration of IPSEC, GRE, OPENVPN can be found in the catalogue ["](https://inhandnetworks.yuque.com/unup4w/cznaqm/csyzewggkogwkefw#A0j1I) [Advanced Functions > VPN](https://help.inhand.com/portal/en/kb/articles/ig-series-user-s-manual-v1-0-12-8-2024#34_VPN:~:text=the%20tracking%20probe.-,3.4%20VPN,-VPN%20is%20a)".

#### 2.3.5.1 L2TP

##### 2.3.5.1.1 L2TP client

![](images/img_33b3c8f0.png)  

1.  L2TP Class  
    

> 1.  Name: Custom L2TP Class Name  
>     
> 
> 1.  Authentication: Tap Enable to require authentication when connecting to the network.  
>     
> 
> 1.  Hostname: the hostname of the local end of the network connection, can not be matched  
>     
> 
> 1.  Challenge Secrets: The tunnel authentication key must be configured when the authentication point selection is enabled, otherwise it does not need to be configured.  
>     

![](images/img_886a9a28.png)  

1.  Pseudowire Class  
    

> 1.  Name: Custom Pseudowire Class Name  
>     
> 
> 1.  L2TP Class: The name of the defined L2TP Class.  
>     
> 
> 1.  Source Interface: Select the source interface name  
>     
> 
> 1.  Data Encapsulation Method: optional L2TPV2, L2TPV3  
>     
> 
> 1.  Tunnel Management Protocol: L2TPV2, L2TPV3, NONE can be selected

![](images/img_8df2814d.png)

1.  L2TPv2 Tunnel  
    

> 1.  Enable: enables or disables L2TP Tunnel  
>     
> 
> 1.  ID: L2TP virtual interface identification number  
>     
> 
> 1.  L2TP Server: Set the IP address or domain name of the L2TP server.  
>     
> 
> 1.  Pseudowire Class: the name of the defined Pseudowire Class.  
>     
> 
> 1.  Authentication Type: Auto, PAP, CHAP can be selected  
>     
> 
> 1.  Username: the legitimate user name set by the counterpart server  
>     
> 
> 1.  Password: a legitimate password set by the counterpart server of the network.  
>     
> 
> 1.  Local IP Address: Set the IP address of the L2TP virtual interface address, or leave it unassigned for the peer server to assign automatically.  
>     
> 
> 1.  Remote IP Address: gateway to the server-side L2TP address pool, may or may not be assigned

![](images/img_26ad8670.png)  

1.  L2TPv3 Tunnel  
    

> 1.  Enable: enables or disables L2TPV3 Tunnel  
>     
> 
> 1.  ID: L2TPV3 virtual interface identification number  
>     
> 
> 1.  Peer ID: Set the IP address or domain name of the L2TPV3 server.  
>     
> 
> 1.  Pseudowire Class: the name of the defined Pseudowire Class.  
>     
> 
> 1.  Protocol: IP, UDP optional  
>     
> 
> 1.  Source Port: the source port used when establishing L2TP using the UDP protocol  
>     
> 
> 1.  Destination Port: the destination port when L2TP is established using the UDP protocol  
>     
> 
> 1.  Xconnect Interface: L2TPV3 Bridge Port

![](images/img_07acbfd1.png)  

1.  L2TPv3 session  
    

> 1.  Local Session ID: the local tunnel ID specified in the static configuration of L2TPV3, in the range 1-65535  
>     
> 
> 1.  Remote Session ID: Remote tunnel ID specified in the static configuration of L2TPV3, in the range 1-65535  
>     
> 
> 1.  Local Tunnel ID: the L2TPv3 tunnel identifier configured above  
>     
> 
> 1.  Local Session IP Address: address of the statically configured L2TPV3 virtual interface

##### 2.3.5.1.2 L2TP Service

![](images/img_499615b5.png)  

The L2TP server parameters are described below:

1.  Enable L2TP Server: Enables or disables the L2TP server  
    

1.  Username: the access account of the L2TP server  
    

1.  Password: Access password for the L2TP server  
    

1.  Authentication Type: selectable Auto, PAP, CHAP  
    

1.  Local IP Address: virtual address of the L2TP server interface  
    

1.  Address Client Start IP: start address of the L2TP server address pool  
    

1.  Address Client End IP Address: end address of the L2TP server address pool  
    

1.  Link Detection Interval(s): the time interval for sending connection detection messages after L2TP is successfully established. Legitimate value: 0-32767, unit: sec.  
    

1.  Max Retries for Link Detection: after L2TP connection detection fails, L2TP re-establishes the connection when the maximum number of failures is reached. Legal value: 0-100  
    

1.  Enable MPPE: Enable/disable MPPE data encryption scheme  
    

1.  Enable Tunnel Authentication  
    

> 1.  Challenge Secrets: Tunnel key to be authenticated when L2TP is established, must be the same at both ends  
>     
> 
> 1.  Server Name: Name of the server when establishing L2TP.  
>     
> 
> 1.  Client Name: Specifies the name of the L2TP client for access.  
>     

![](images/img_d7065ba2.png)  

1.  Expert Options (Expert Only): parameters for debugging L2TP  
    

## 2.4 Edge computing

### 2.4.1 Python Edge Computing

The "Python Edge Computing" page shows information about the IG's Python secondary development environment and the app configuration and running status on the device. You can develop your customised Python App with the secondary development environment information on this page, and you can also configure and view the App status on this page.

The Python environment configuration steps are as follows:

1.  Select "Edge Computing > Python Edge Computing" to enter the "Python Edge Computing" interface;
2.  Enable the Python Engine;
3.  Install/upgrade the Python SDK;
4.  Just enable debug mode. See [Python Development Quickstart](https://sdk.ig.inhandnetworks.com/en/latest/) how to do secondary Python development.

![](images/img_082fd458.png)  

App configuration steps are as follows:

1.  APP install, uninstall, start, stop
2.  APP configuration import, export
3.  APP Log View

![](images/img_ef68867f.png)  

![](images/img_a7358539.png)  

App configuration features are described below:

1.  APP Status  
    

> 1.  Start All: Starts all deactivated apps  
>     
> 
> 1.  Stop All: stops all enabled apps  
>     
> 
> 1.  Restart All: Restart all apps in the list  
>     
> 
> 1.  Download: Download the runtime logs of the specified apps  
>     
> 
> 1.  Delete: Empty the runtime log of the specified app  
>     
> 
> 1.  View: View the runtime log of the specified App  
>     
> 
> 1.  Stop: Stop running the specified app  
>     
> 
> 1.  Restart: Restart the specified App  
>     

1.  App List  
    

> 1.  Enable: Enable the App, the App will run automatically every time you reboot your device after you enable it  
>     
> 
> 1.  Startup Parameters: You can configure the startup parameters of the app here.  
>     
> 
> 1.  Export Configuration: Export App Configuration File  
>     
> 
> 1.  Import Configuration: Import the App configuration file, after importing the configuration file and restarting the App it will run according to the imported configuration file.  
>     
> 
> 1.  Uninstall: Uninstall the App

![](images/img_d01bbe2d.png)  

> 1.  Edit: Edit the size and number of App log files, as well as the App's startup parameters  
>     
> 
> 1.  Add: Add App

### 2.4.2 Docker Management

IG supports hosted docker images, you can publish your docker images to IG to quickly deploy and run your self-developed applications.The steps to configure the Docker environment are as follows:

1.  Install the Docker SDK;
2.  Enable the Docker Manager;
3.  Go to the Docker management page (portianer) to configure images and containers.

Note: Only IG902 and IG974 support Docker function.

Enable the Docker Manager as shown below:

![](images/img_09c6afd0.png)

The parameters of the Docker management page are described below:

1.  Enable Docker Manager: Enable/Disable Docker Manager  
    

1.  Docker Version: install or upgrade Docker version  
    

1.  Enable Portainer Manager: Enable/Disable Portainer Manager  
    

1.  User Name: the username used to log in to portianer  
    

1.  Password: the password used to log in to portianer  
    

1.  Registry Mirrors: Configure the addresses of docker image repositories, up to 4

### 2.4.3 Cloud Edge Computing

The gateway supports both Azure IoT Edge and AWS IoT Greengrass edge computing components. They can be configured on the Edge Computing -> Cloud Edge Computing page. Note: Only the IG902 supports the Cloud Edge Computing function.

#### 2.4.3.1 Azure IOT Edge

![](images/img_cc4a9cd8.png)  

The configuration steps are as follows:

1、Install/Upgrade SDK: Click the Upgrade button to install Azure IoT Edge version V1.1.3.  

2、Configuring Azure IoT Edge: Configuration for Azure IoT Edge is divided into manual configuration and importing profiles   

1.  Manual Configuration: When Manual is selected for the source, only a device connection string needs to be configured.   
    

1.  DPS: When the source selects DPS, you need to configure the global terminal node, region ID, method, and import the certificate file.  
    

1.  If there are still end nodes under the gateway that need to connect to the gateway, you can click Enable Certificates and import the relevant certificate files.   
    

3、Import Configuration File: With the Enable Configuration File button, you can edit the configuration file and import it into the device. If you need a certificate in the configuration, you need to import the certificate first, the path of the certificate can be viewed by hovering the mouse over the "?" after the "Import" button. behind the "Import" button.   

4、To view the logs: In the Export Log File line, click the Export button to export the Azure IoT Edge runtime logs.

#### 2.4.3.1 AWS IoT Greengrass

![](images/img_bbbdb550.png)  

The configuration steps are as follows:

1.  Install/Upgrade SDK: Click the Upgrade button to install AWS IoT Greengrass version V1.
2.  Supports importing root CAs, device certificates, device keys and configuration files, as well as exporting configuration files and log files.

### 2.4.4 IO module

An I/O module (Input/Output Module) is a device or component used to implement input and output functions. It can input signals from external devices into the control system or output signals from the control system to external devices, thus realising the interaction between the system and the external environment.

Configure the IOs on the Edge Computing -> IO Module page. the gateway supports 4 input IOs and 4 output IOs. 

Note: Support models IG502/IG504/IG532/IG902

Input IOs: 4 input IOs can be configured as "Digital Input" or "Counter".

![](images/img_ada72d5e.png)  

Output IOs: 4 output IOs can be configured as "Digital Output", "Continuous Pulse Output" and "Fixed total Pulse Output".

![](images/img_96aa5ea5.png)  

Supports reading and writing IO data via Modbus TCP protocol when Modbus TCP slave function is enabled.  

![](images/img_f94bcf02.png)  

1.  Enable: Enable Modbus TCP slave function  
    

1.  External Access: when disabled, only internal requests will be allowed, and the IP address of Modbus slave can only be 127.0.0.1 when internal access is configured. when enabled, external access will be allowed, and the external access is configured as the IP address of the corresponding Ethernet interface.  
    

1.  Port: port information of the slave  
    

1.  Slave Address: unique identification of the slave device  
    

1.  Byte order: default ABCD byte order  
    

1.  Maximum TCP Connections: Maximum number of TCP connections, range: 1-32

You can view Modbus coil status information and holding register information in the Modbus Mapping Table page.

![](images/img_ecfb2268.png)  

### 2.4.5 Telegraf 

Configure Telegraf functionality on the Edge Computing -> Telegraf page. Support for installing Telegraf sdk, importing and exporting configuration files and exporting log files 

Note: Only IG502 supports this function. 

![](images/img_2f6a37bf.png)  

## 2.5 Systems management

### 2.5.1 System Time

In order for the IG to work better with other devices, the system time needs to be configured accurately. The configuration method and steps are as follows:

1.  Method 1: Configure the system time using the time zone  
    

> 1.  Select "System > System Time" to enter the "System Time" interface.  
>     
> 
> 1.  Select the time zone of the gateway in the "Time zone" of "System Time".  
>     
> 
> 1.  Select and click "Apply".

![](images/img_3e4cc7e6.png)  

1.  Method 2: Configure the system time using the PC's local time  
    

> 1.  Select "System Management > System Time" to enter the "System Time" interface.  
>     
> 
> 1.  The gateway automatically gets the PC's time as the local time  
>     
> 
> 1.  Click "Synchronise" in the device time, the device time will be synchronised with the local time.

![](images/img_b317e78b.png)  

1.  Method 3: Configure the system time using the manual time setting method  
    

> 1.  Select "System Management > System Time" to enter the "System Time" interface.  
>     
> 
> 1.  Manually set the device time directly in the "Set Time".  
>     
> 
> 1.  Click "Apply" when you are done with the settings.  
>     

![](images/img_2d2b58d5.png)  

1.  Method 4: Configure the system time using the SNTP client  
    

> 1.  Select "System Management > System Time" to enter the "System Time" interface.  
>     
> 
> 1.  Tick "Enable SNTP Clients".  
>     
> 
> 1.  Configure each parameter in turn  
>     
> 
> 1.  Click "Submit" to apply the configuration.  
>     

![](images/img_40295f46.png)  

The SNTP client parameters are described below:

1.  Enable SNTP Client: enable/disable SNTP clients.  
    

1.  Update interval: Synchronise the device time to the server according to the update interval after enabling the SNTP client.  
    

1.  SNTP Servers List  
    

> 1.  Server Address: SNTP server address (domain name/IP), you can fill in up to 10 servers. When setting up multiple SNTP servers, the system will poll all SNTP servers until it finds an available one.  
>     
> 
> 1.  Port: SNTP service port of the SNTP server

The IG can also be used as an NTP server to synchronise time for other devices as follows:

1.  Select "System Management > System Time" to enter the "System Time" interface.
2.  Tick "Enable NTP server".
3.  Configure each parameter in turn
4.  Click "Submit" to apply the configuration.

![](images/img_cdb71492.png)

The NTP server parameters are described below:  

1.  Enable NTP Server: enable/disable NTP server  
    

1.  Preferred NTP Server: NTP adopts a layered synchronisation method, generally the n+1th level is synchronised with the nth level clock source.NTP supports a maximum of 16 levels of synchronisation, i.e. 0-15 levels. NTP supports up to 16 levels of synchronisation, i.e., 0-15 levels, and cannot synchronise with more than 16 levels.  
    

1.  Source Interface: The interface on which the gateway sends NTP messages. The source interface and source address cannot be used at the same time.  
    

1.  Source address: the source address carried by the gateway for SNTP messages. Source interface and source address cannot be used at the same time.  
    

1.  NTP Servers List  
    

> 1.  Primary NTP Server: Set multiple NTP servers, when primary NTP server is ticked, it means our device synchronises time with this NTP server. Checking more than one will poll all the ticked NTP servers until we find an available one.  
>     
> 
> 1.  Server Address: NTP server address (domain name/IP), up to 10 servers.

### 2.5.2 System logs

You can select "System > Log" to enter the "Log" page. This page contains a lot of information about the network and IG, including operational status, configuration changes, and so on.

![](images/img_dc773769.png)  

In the "Configure" page, you can set the gateway to interface with the remote logging server, after the setup is completed, the gateway will upload all system logs to the remote logging server, which requires the cooperation of the remote logging software on the host computer (e.g., Kiwi Syslog Daemon).

![](images/img_a1b9030c.png)  

1.  Send to remote log server: Enable/disable device docking to remote log server  
    

1.  Server Address: the address of the remote logging server  
    

1.  Port Number: port number of the remote logging server  
    

When logs are stored locally, you can set the size of the log file and the level of log output:

![](images/img_523a46b0.png)

1.  History Log File Size: The amount of space the host is allocated to store logs.  
    

1.  Historical log file severity level: Sorts the logs in the device by "Emergency > Alarm > Serious > Error > Warning > Notice > Information > Debug". If the log level is set to "Notice" and above, the log file will output "Notice" and logs with higher priority than "Notice".  
    

### 2.5.3 Configuration Management  

Select "System > Configuration Management" to enter the "Configuration Management" interface. You can backup the configuration parameters, import the corresponding parameter configurations, and restore the IG to the factory settings in this screen.

![](images/img_d3faedef.png)  

1.  configuration management  
    

> 1.  Autosave: when checked, the configuration in running-config will be automatically synchronised to startup-config every time the configuration is modified to ensure that the configuration is not lost after the device is powered off and on.  
>     
> 
> 1.  Encrypted: When enabled, all parameters configured by the IG on the WEB with passwords will be displayed in the configuration in an encrypted way. Improve password security.  
>     

1.  Configuration Files Operations  
    

> 1.  Import Startup Config: Import the configuration file into startup-config, the imported configuration will be loaded after reboot. (Note: During this process, make sure that the imported configuration is legal and in order. When importing configurations, IG will filter the commands with illegal format and re-store the remaining correct configurations into startup-config, and then execute the legal configurations in order after system reboot. If the imported configuration is not in a valid order, the system will not be able to enter the desired configuration state.)  
>     
> 
> 1.  Export Startup Config: Backup startup-config to the host. startup-config is the configuration of the gateway at boot time.  
>     
> 
> 1.  Export Running Config: Backs up running-config to the host. running-config is the current running configuration of the gateway.  
>     
> 
> 1.  Restore Factory Configuration: restores the IG to the factory configuration, all configurations of the gateway are restored to the default parameters. A restart of the IG is required for the factory restoration to take effect.  
>     

### 2.5.4 InHand Cloud  

The device cloud platform developed by InHand supports monitoring IG status, remote maintenance of field devices, remote batch issuance of IG configurations and batch upgrade of IGs, helping users manage IGs and field devices conveniently and efficiently. At present, IGs support interfacing with InHand cloud platforms: InHand Connect Service, InHand Device Manager, InHand iSCADA Cloud, and InHand Device Live Manager.

Configure the IG to connect to the InHand Connect Service (InConnect) platform as shown below:  

![](images/img_f9fade45.png)  

Connecting to the InHand Connect Service platform parameters are described below:

1.  Enable: Enables/Disables device connection to the InConnect platform  
    

1.  Server Address: Select the server address you want to connect to from the drop-down box, or select "Custom" to customise the server address.  
    

1.  Register Account: the name of the account already registered on the cloud platform  
    

1.  Advanced Settings  
    

> 1.  Enable Secure Channel: Enable/Disable the secure channel; when this function is enabled, a dedicated, encrypted communication channel will be established to ensure the security, integrity and confidentiality of data transmission during remote access to the device.  
>     
> 
> 1.  Location: Source of location information, either Cellular or GPS.  
>     
> 
> 1.  LBS Upload Interval: time interval for LBS information reporting, legal value 60-86400, unit: sec.  
>     
> 
> 1.  Heartbeat Interval: heartbeat interval with the cloud platform, legal value 30-3600, unit: second  
>     
> 
> 1.  Data Upload Interval: time interval of traffic information report, legal value 3600-86400. unit: second.

Configure the IG to connect to the InHand Device Manager (DM) platform as shown below:

![](images/img_f6a23bea.png)  

Connecting to the InHand Device Manager platform parameters are described below:

1.  Enable: Enable/disable device connection to the DM platform  
    

1.  Server Address: Select the server address you want to connect to from the drop-down box, or select "Custom" to customise the server address.  
    

1.  Register Account: the name of the account already registered on the cloud platform  
    

1.  Advanced Settings  
    

> 1.  Enable Secure Channel: Enable/disable the secure channel; when this function is enabled, a dedicated, encrypted communication channel will be established to ensure the security, integrity and confidentiality of data transmission during remote access to the device.  
>     
> 
> 1.  Location: Source of position information, either Cellular or GPS.  
>     
> 
> 1.  LBS Upload Interval: time interval for LBS information reporting, legal value 60-86400, unit: sec.  
>     
> 
> 1.  Heartbeat Interval: heartbeat interval with the cloud platform, legal value 30-3600. unit: second.  
>     
> 
> 1.  Data Upload Interval: time interval for reporting traffic information, legal value 3600-86400, unit: second  
>     

Configure the IG to connect to the InHand iSCADA Cloud platform as shown below:

![](images/img_70d7281c.png)  

Connecting to the InHand iSCADA Cloud platform parameters are described below:

1.  Enable: Enable/Disable device connection to the platform  
    

1.  Server Address: Select the server address you want to connect to from the drop-down box, or select "Custom" to customise the server address.  
    

1.  Heartbeat Interval: heartbeat interval with the cloud platform, legal value 30-1200, unit: second

Configure the IG to connect to the InHand Device Live Manager (DeviceLive) platform as shown below:

![](images/img_02258054.png)  

Connecting to the InHand Device Live Manager platform parameters are described below:

1.  Enable: Enable/Disable device connection to the platform  
    

1.  Server Address: Select the server address you want to connect to from the drop-down box  
    

1.  Heartbeat Interval: heartbeat interval with the cloud platform, legal value 30-1200, unit: second

### 2.5.5 Firmware upgrades

You can upgrade the firmware version of IG to support new features or to get a better experience on the "Firmware Upgrade" page. The steps to upgrade the firmware version are as follows:

1.  Select "System > Firmware Upgrade" to enter the "Firmware Upgrade" interface.
2.  Click "Select File" to select the IG firmware file.
3.  Click "Start Upgrading" and "Confirm" to start the upgrade.
4.  Wait for the upgrade to be successful, after the upgrade is successful, click the "Rebot" button to restart the IG to complete the upgrade.

![](images/img_3413b0af.png)

  

![](images/img_dc36c9b4.png)  

### 2.5.6 Access Tools

To manage and configure the IG, you can configure how to manage and access the IG in the "Access Tools" screen. The configuration steps are as follows:

1.  Configuring HTTPS

![](images/img_51d07315.png)

  

The HTTPS parameters are described below:

1.  Listening IP Address: Any, 127.0.0.1 and other IP addresses can be selected. Any is the default choice, that is, the device listens to HTTPS requests from any address.  
    

  

1.  Port: HTTPS access port number, default port 443 is used  
    

  

1.  web Login Timeout: the timeout time for logging in web page, default is 300s, when the web idle time exceeds 300s, it will exit the web login; you can also manually change the timeout time for web login, legal value is 100-3600, unit: second.  
    

  

1.  Remote Control: Enabled for remote access to IG via HTTPS  
    

  

1.  Source Network: the legal source address for accessing the WEB page of the device; if not set, it means any address can be connected to the IG via HTTPS.

1.  Configuring TELNET

![](images/img_d550ff72.png)

The TELNET parameters are described below:

1.  Listening IP Address: Any, 127.0.0.1 and other IP addresses can be selected. Any is the default choice, that is, the device listens to TELNET requests from any address. 
2.  Port: TELNET access port number, default is port 23
3.  Remote Control: Enabled to access the IG remotely via TELNET.
4.  Source Network: Legal source address for accessing the device; if not set it means any address can be connected to the IG via TELNET.

1.  Configuring SSH  
    

![](images/img_abe51724.png)  

The SSH parameters are described below:

1.  Listening IP Address: Any, 127.0.0.1 and other IP addresses can be selected. Any is the default choice, i.e., the device listens to SSH requests from any address.   
    

1.  Port: SSH access port number, port 22 is used by default.  
    

1.  Timeout: SSH timeout time, legal value 0-120; if SSH does not connect successfully within the timeout time, it is regarded as the connection failure.  
    

1.  Private Key Mode: SSH connections typically use asymmetric encryption algorithms for secure communication, involving both public and private keys. A common key mode is RSA mode.  
    

1.  Private Key Length: The key length of the RSA algorithm can be chosen according to requirements. Generally speaking, the longer the key length, the higher the security, but the computational resources required to generate and process the key will also increase. You can choose 512/1024/2048/4096, the default length is 1024.  
    

1.  Remote Control: when turned on, you can access the IG remotely via SSH.  
    

1.  Source Network: Legal source address for accessing the device; if not set it means any address can be connected to the IG via SSH.

1.  Configuring Developer Mode  
    

![](images/img_16f12f55.png)  

The developer mode parameters are described below:

1.  User name: the user name for developer mode login, fixed to pyuser   
    

1.  SSH Port: The port number for developer mode login, default is 222.  
    

1.  Enable Fixed Password: when enabled, you can manually set a fixed password to log in to the device, otherwise the password is a random password generated by the device

### 2.5.7 User management

You can add a new user or manage the user's account password and access rights in the "User Management" page to achieve multi-user access and management of IG.

  

### 2.5.8 Restart

In the "Reboot" page, you can reboot the device every day or immediately. As shown in the figure below, if you enable "Regularly Daily Reboot", the device will be rebooted at "00:00" every day, and this function is disabled by default.

![](images/img_9eba3a98.png)  

### 2.5.9 Network Tools

Select "System > Network Tools" to enter the "Networks Tools" page. You can diagnose IG network problems on this page. You can enter some extended options in Expert Options, e.g. -s 100 for sending 100-byte packets in Expert Options Configuration in Ping tool.

Use the Ping tool to detect whether the network is reachable, as shown below:

![](images/img_176b8fdb.png)  

Use the route probing tool to determine the path through which IP datagrams access the destination, as shown in the following figure:

![](images/img_9867238a.png)  

Use the network packet capture tool to capture the data transmitted on the specified interface, as shown in the following figure:

![](images/img_af94fc2e.png)  

### 2.5.10 Third party software statements

Select "System> 3rd Party Notification" to enter the Third Party Software Notification page. You can view the third-party software notification of IG software here.

![](images/img_93811165.png)  

## 2.6 Navigation bar operation

### 2.6.1 Return to home page

You can click on the InGateway logo in the upper left corner of any web interface of the gateway to quickly jump to the "Overview" page.

![](images/img_d1a84a88.png)  

### 2.6.2 Logout

You can click on your username in the top right corner to log out.

![](images/img_5f23d99c.png)  

### 2.6.3 Switching languages

You can click "Language" in the upper right corner to switch the language display of the WEB interface, the gateway supports both Simplified Chinese and English.

![](images/img_4c0a0b1c.png)  

# 3 Advanced Functions

## 3.1 Management

### 3.1.1 Systems

Here, you can view the system status and network status; in the system status section, you can view the name, model, serial number, MAC address, version information, device time, device startup time, performance, storage and other information, you can also click on the Synchronise Time button to set the system time; in the network status section, click on the interface of the "Settings" to enter the configuration page of the corresponding interface. Click "Settings" after the interface in the Network Status section to enter the configuration page of the corresponding interface.

![](images/img_ac6e4e0a.png)  

### 3.1.2 AAA

#### 3.1.2.1 Radius

The RADIUS protocol uses a client/server (C/S) mode of operation. the RADIUS protocol entity consists of three parts: the user side, the RADIUS client (NAS), and the RADIUS server. The authentication process is shown in the following figure:

![](images/img_95e5e9b5.png)  

The authentication steps are as follows:

1\. When a user accesses the network, the user initiates a connection request and sends a username and password to the RADIUS client.

2\. The RADIUS client sends an authentication request message containing user name and password information to the RADIUS server. (NAS and RADIUS server use a pre-shared key, and the user password is encrypted and hidden by MD5 encryption algorithm using this shared key, which increases the security of the password.)

3\. The RADIUS server checks the legitimacy of the user's identity:

(1) If the user's identity is legitimate, the RADIUS server returns an authentication acceptance message to the RADIUS client, allowing the user to proceed to the next action. Since the RADIUS protocol merges the processes of authentication and authorisation, the authentication acceptance message also contains the user's authorisation information.

(2) If the user's identity is not legitimate, the RADIUS server returns an authentication denial message to the RADIUS client, denying the user access to the access network.

4\. The RADIUS client informs the user whether the authentication is successful.

The Radius authentication configuration is shown below:

![](images/img_41342ece.png)  

The Radius parameter is described below:

1.  Server: address of Radius server (domain name/IP), supports up to 10 entries  
    

1.  Port: service port number of the Radius server  
    

1.  Key: Authentication key to be verified when establishing a connection with a Radius server. Only if the authentication key is the same, you can establish a connection with the Radius server.  
    

1.  Source interface: the source interface of Radius

#### 3.1.2.2 Tacacs+

Tacacs+ (Terminal Access Controller Access Control System) is a security protocol with enhanced functionality based on the Tacacs protocol, which is similar in function to the RADIUS protocol. The protocol is similar to the RADIUS protocol, using a client/server model to achieve communication between the NAS and the TACACS+ server. TACACS+ holds independent authentication (Authentication), authorisation (Authorization) and billing (Accounting) functions. 

The Tacacs+ authentication configuration is shown below:

![](images/img_8914e2ec.png)  

The Tacacs+ parameters are described below:

1.  Server: Address (domain/IP) of the Tacacs+ server, up to 10 entries supported  
    

1.  Port: Service port number of the Tacacs+ server  
    

1.  Key: Authentication key to be verified when establishing a connection with the Tacacs+ server. Only if the authentication key is the same can a connection be established with the Tacacs+ server.

#### 3.1.2.3 LDAP

Lightweight Directory Access Protocol LDAP is a directory access protocol based on TCP/IP, mainly used to store infrequent data, such as email addresses, contact lists, etc. LDAP defines a variety of operations, and user authentication and authorisation can be achieved through binding and query operations. LDAP is based on Client/Server structure, the directory information is stored on the server, and does not support billing.LADP authentication process is shown in the following figure:

![](images/img_7ecaf865.png)  

LADP certification is described below:

1、When the user needs to access the LDAP server, the user enters the user name and password and initiates an authentication request to the device

2\. The device obtains the user name and password of the user and sends an administrator binding request message to the LDAP server with the administrator DN and administrator password as parameters to obtain query privileges.

3\. When the LDAP server receives the administrator binding request message, it verifies whether the administrator DN and administrator password are correct. If the administrator DN and administrator password are correct, the binding is successful and the LDAP server sends an administrator binding response message to the device.

4\. When the device receives the binding response message, it constructs a filter condition with the parameter of the user name entered by the user and sends a user DN query request message to the LDAP server. For example, the filter condition is CN=User2.

5\. After the LDAP server receives the user DN query request message, it looks up the user DN according to the query starting point, query range, and filter conditions in the message. If the query is successful, it sends a successful query response message to the device. The queried user DN can be one or more.

6\. The device sends a user binding request message to the LDAP server based on the user DN obtained from the query and the password entered by the user as parameters.

7\. After the LDAP server receives the user binding request message, it checks whether the password entered by the user is correct.

(1) If the password entered by the user is correct, a binding response message of successful binding is sent to the device.

(2) If the password entered by the user is incorrect, a binding failure response message is sent to the device. The device takes the next user DN queried as a parameter and continues to send binding requests to the LDAP server until one DN binds successfully. If all user DNs fail to bind, the device notifies the user of the authentication failure.

8、After successful authentication, the device notifies the user of successful login.

The LADP authentication configuration is shown below:

![](images/img_8bba915d.png)  

The LDAP parameters are described below:

1.  Name: User-defined server list name  
    

1.  Server: server address (domain name/IP), supports up to 10 entries  
    

1.  Port: Same as server port  
    

1.  Base DN: Top of the LDAP directory tree  
    

1.  Username: the username to access the server  
    

1.  Password: Password to access the server  
    

1.  Security: 3 options for encryption: None, SSL and StartTLS.  
    

1.  Verify the opposite end: Tap to turn on  
    

3.1.2.4 AAA authentication

![](images/img_8a59d915.png)  

The following authentication methods are supported:

1.  No authentication (none): the user is trusted so much that it is not checked for legitimacy; this is not normally used.  
    

1.  Local authentication (local): user information is configured on the network access server. The advantages of local authentication is fast, can reduce costs for the operation, the disadvantage is that the amount of information stored by the equipment hardware conditions.  
    

1.  Remote Authentication (ldap): Configure user information on the authentication server. Supports remote authentication via Radius protocol, Tacacs+ protocol and LDAP.  
    

The following authorisation methods are supported:  

1.  No authorisation (none): no authorisation processing for the user.  
    

1.  Local authorisation (local): authorisation is based on the relevant attributes configured by the network access server for the local user account.  
    

1.  Tacacs+ Authorisation: Authorisation of users by the Tacacs+ server.  
    

1.  Authorisation after successful Radius authentication: Authentication and authorisation are bound together and cannot be authorised using Radius alone.  
    

1.  LDAP authorisation

NOTE: Authentication 1 and Authorisation 1 should be set up consistently; Authentication 2 and Authorisation 2 should be set up consistently; Authentication 3 and Authorisation 3 should be set up consistently.

## 3.2 Services

### 3.2.1 Dynamic domain names

Dynamic domain name is a service that bundles dynamically assigned IP addresses with fixed domain names. In networks, in many cases the IP address that users are given when they access the Internet changes dynamically. To access specific network services or devices through a domain name, a dynamic domain name service is required.

![](images/img_481a16de.png)  

The dynamic domain name parameters are described below:

DDNS Method List：

1.  Method name: name of the custom dynamic domain update method  
    

1.  Service type: The service type is mainly decided by the dynamic domain name service provider, and different dynamic domain name service providers set different service types and functional features. Users will pick from these service types according to their actual situation and needs when choosing and using them.  
    

> 1.  Disable: Indicates that the dynamic domain name function is disabled.  
>     
> 
> 1.  DynAccess  
>     
> 
> 1.  QDNS(3322)-Dynamic  
>     
> 
> 1.  QDNS(3322)-Static  
>     
> 
> 1.  DynDNS-Dynamic  
>     
> 
> 1.  DynDNS -Static  
>     
> 
> 1.  NoIP  
>     
> 
> 1.  Custom: a customisation option that allows you to configure other dynamic domain name services not listed in the list according to your specific needs.  
>     

1.  Username: the user name applied on the dynamic domain name server  
    

1.  Password: the password configured in the dynamic domain name server  
    

1.  Hostname: Domain name applied for on a dynamic domain name server  
    

1.  Period minutes (in minutes): the time interval between synchronisation of domain names and IPs by dynamic DNS servers

Note: Up to 4 dynamic domain name update methods can be configured

Specify A Method To Interface

1.  Interface: Interface required for dynamic domain name resolution  
    

1.  Method: Select the dynamic domain name update method configured above

### 3.2.2 Flow control

Flow control is the process of managing and limiting network flow to ensure network stability, performance, and rational allocation of resources.IG can set limits for daily/monthly flow, and after the flow exceeds the set threshold, it can be set to only Reporting/Stop Forward/Shutdown Interface to remind users or disable the flow.

The configuration of flow control is shown below:  

![](images/img_dff8b2af.png)  

## 3.3 Link Backup

In order to maintain the stability of the network, in the network environment composed of devices, usually use some backup connections to improve the robustness and stability of the network, where the backup connection is also known as the backup link or redundant link.

### 3.3.1 SLA

InHand SLA Fundamentals: 1. Object tracking: the reachability of a specified object is tracked.2. SLA probe: the object tracking feature can be used to issue different types of probes to an object using the InHand SLA.3. using the static routing and tracking options.SLA Configuration Steps The SLA configuration steps are as follows:

1.  Define one or more SLA operations (probes).
2.  Define one or more Track objects to track the status of SLA operations.
3.  Define the measures associated with the tracked object.

![](images/img_3e073800.png)  

The SLA parameters are described below:

1.  Index: Index or ID of the SLA, user-defined or automatically generated up to 10 SLAs can be added  
    

1.  Type: type of probe, default is icmp-echo, by simply sending an ICMP-ECHO (Type8) packet to the target host, if the ICMP-ECHO-Reply (ICMPtype0) packet is received, it means that the host is alive  
    

1.  Destination Address: IP address to be probed  
    

1.  Data size: user-defined size of probe packets  
    

1.  Interval (s): the device sends ICMP probes at a regular interval according to the set probe interval.  
    

1.  Timeout (ms): If the device does not receive a packet within the configured timeout period after sending an ICMP probe, the probe is considered to have failed and the next probe is performed.  
    

1.  Consecutive: i.e., how many times the detection fails for link failure. When the configured number of times of detection is reached, the SLA detection is considered to have failed, and then the SLA state is DOWN.  
    

1.  Life: default is forever (i.e., it will take effect forever after configuration), and cannot be changed by the user.  
    

1.  Start-time: default is now (effective immediately after configuration) 

### 3.3.2 Track module

The purpose of Track is to realise the linkage function, which consists of three parts: the application module, the Track module and the monitoring module.  the Track module is located between the application module and the monitoring module, and its main function is to shield the differences between the different monitoring modules and provide a uniform interface for the application module.

![](images/img_c7a1a653.png)  

The Track module parameters are described below:

Track Object:

1.  Index: Index or ID of the Track, user-defined or auto-generated, up to 10 can be created.  
    

1.  Type: sla or interface selectable  
    

1.  SLA ID/VRRP ID: index or ID of the defined SLA, not available when interface is selected as type  
    

1.  Interface: not available when sla is selected as type  
    

1.  Negative delay(s): when the interface or sla state is DOWN, how long it takes for the track to display the abnormality. 0 means display immediately, unit: second.  
    

1.  Normal state delay: When a fault is recovered, switchover can be delayed instead of immediate according to the set time (0 for immediate switchover)

Track Action:

1.  Index: Index or ID of the Track, user-defined or auto-generated, up to 10 can be created.  
    

1.  Control Service: default is ipsec, i.e. this Track is used to detect the status of IPSec connection establishment.  
    

1.  Action:  
    

> 1.  positive-start/negative-stop: When the result of IPSec-related probing or monitoring is "positive" (IPSEC tunnel status is normal), the corresponding operation or process will be started; and when the result is "negative" (IPSEC tunnel status is abnormal), the corresponding operation or process will be stopped. negative" (IPSEC tunnel status abnormal), the corresponding operation or process will be stopped.  
>     
> 
> 1.  positive-stop/negative-start: When the result of IPSec-related probing or monitoring is "positive" (IPSEC tunnel status is normal), the corresponding operation or process will be stopped; and when the result is "negative" (IPSEC tunnel status is abnormal), the corresponding operation or process will be started. negative" (IPSEC tunnel status abnormal), the corresponding operation or process will be started.

### 3.3.3 Interface Backup

Interface backup refers to the formation of a master-backup relationship between specified interfaces of the same device. When an interface fails or the bandwidth is insufficient and the service transmission cannot be carried out normally, the flow can be quickly switched to the backup interface, which will take over the service transmission or share the network flow, thus improving the reliability of the communication of data devices.

![](images/img_8421f58c.png)  

The interface backup parameters are described below:

1.  Primary interface: the interface in use  
    

1.  Backup interface: interface waiting to be switched over  
    

1.  Startup delay: Set how long to wait for the startup trace detection policy to take effect  
    

1.  Up delay: when the main interface switches from detection failure to detection success, the switchover can be delayed according to the set time (0 for immediate switchover) instead of immediate switchover  
    

1.  Down delay: when the main interface switches from detecting success to detecting failure, it can delay the switchover according to the set time (0 represents immediate switchover) instead of immediate switchover  
    

1.  Track ID: the index or ID of the Track that has been defined by the tracking probe.  
    

  

## 3.4 VPN

VPN is a "virtual" private communications network built on top of a public network (such as the Internet). By "virtual", we mean that it does not have independent physical links and infrastructure like traditional private networks, but rather, through network technology, it establishes a logically isolated and dedicated communication channel on the public network to achieve functions and security similar to those of private networks.

By means of tunneling technology, encryption technology, etc., it makes users feel like they are communicating in an independent and secure private network when using a VPN, but in reality the data is transmitted on top of the public network and is only logically dedicated and private.

### 3.4.1 IPsec

IPsec is a set of open network security protocols developed by IETF, which performs authentication and encryption operations on packets at the IP layer to ensure the integrity and security of communication data. It reduces the risk of data leakage and eavesdropping, and guarantees the security of user business data transmission.

#### 3.4.1.1 IPsec Configuration

![](images/img_9922b1e1.png)  

The IPsec configuration parameters are described below:

1.  IKEv1 Policy  
    

> 1.  ID: Custom IKEv1 policy identifier  
>     
> 
> 1.  Encryption: 3DES, DES, AES128, AES192, AES256 can be selected  
>     
> 
> > 1.  3DES: encrypts plaintext using three 64bit DES keys  
> >     
> > 
> > 1.  DES: encrypts a 64bit block of plaintext with a 64bit key  
> >     
> > 
> > 1.  AES: Encrypts plaintext using the AES algorithm with a 128bit, 192bit or 256bit key length  
> >     
> 
> 1.  Hash: optional MD5, SHA1, SHA2-256, SHA2-384, SHA2-512  
>     
> 
> > 1.  MD5: Generate a 128bit message digest by entering a message of arbitrary length.  
> >     
> > 
> > 1.  SHA1: Input message length less than 128bit, generate 160bit message digest.  
> >     
> > 
> > 1.  SHA2-256: Output 256bit  
> >     
> > 
> > 1.  SHA2-384: Output 384bit  
> >     
> > 
> > 1.  SHA2-512: Output 512bit  
> >     
> 
> 1.  Diffie-Hellman Group: the Diffie-Hellman algorithm is a public key algorithm. The communicating parties compute a shared key by exchanging some data without transmitting the key. The prerequisite for encryption is that the two parties exchanging encrypted data must have a shared key. the essence of IKE is that it never transmits the key directly over an insecure network, but rather through a series of data exchanges, it eventually computes the key shared by the two parties. Even if a third party (e.g. a hacker) intercepts all the data exchanged between the two parties used to calculate the key, it will not be enough to calculate the real key.  
>     
> 
> 1.  Lifetime: set the survival time of the IKE SA, another SA will be negotiated in advance to replace the old one before the set survival time is exceeded.  
>     

1.  IKEv2 Policy  
    

> 1.  ID: Custom IKEv2 policy identifier  
>     
> 
> 1.  Encryption: 3DES, DES, AES128, AES192, AES256 can be selected  
>     
> 
> > 1.  3DES: encrypts plaintext using three 64bit DES keys  
> >     
> > 
> > 1.  DES: encrypts a 64bit plaintext block with a 64bit key  
> >     
> > 
> > 1.  AES: Encrypts plaintext using the AES algorithm with a 128bit, 192bit or 256bit key length  
> >     
> 
> 1.  integrity: optional MD5, SHA1, SHA2-256, SHA2-384, SHA2-512  
>     
> 
> > 1.  MD5: Generate a 128bit message digest by entering a message of arbitrary length.  
> >     
> > 
> > 1.  SHA1: Input message length less than 128bit, generate 160bit message digest.  
> >     
> > 
> > 1.  SHA2-256: Output 256bit  
> >     
> > 
> > 1.  SHA2-384: Output 384bit  
> >     
> > 
> > 1.  SHA2-512: Output 512bit  
> >     
> 
> 1.  Diffie-Hellman Key Exchange: the Diffie-Hellman algorithm is a public key algorithm. The communicating parties compute a shared key by exchanging some data without transmitting the key. The prerequisite for encryption is that the two parties exchanging encrypted data must have a shared key. the essence of IKE is that it never transmits the key directly over an insecure network, but rather through a series of data exchanges, it eventually computes the key shared by the two parties. Even if a third party (e.g. a hacker) intercepts all the data exchanged between the two parties used to calculate the key, it will not be enough to calculate the real key.  
>     
> 
> 1.  Lifetime: set the survival time of the IKE SA, another SA will be negotiated in advance to replace the old one before the set survival time is exceeded.  
>     

1.  IPsec policy  
    

> 1.  Name: Sets the name of the IPSec policy. This parameter cannot be modified after the IPSec policy is successfully configured.  
>     
> 
> 1.  Encapsulation: The AH protocol of the IPSec protocol defines the application method of authentication, providing data source authentication and integrity assurance; the ESP protocol defines the application method of encryption and optional authentication, providing data reliability assurance  
>     
> 
> > 1.  AH: Provides data source authentication, data integrity checking and message anti-replay. The sender performs discrete operations on the invariant part of the IP header and the IP net load to generate a digest field. The receiving end recalculates the digest field of the message according to the received IP message and determines whether the message has been tampered with during network transmission by comparing the digest fields.  
> >     
> > 
> > 1.  ESP: ESP Encapsulating Security Payload Protocol: provides all the features of the AH Authentication Header Protocol, but also encrypts the IP message payload. the ESP protocol allows the content of the IP header of an IP message to be protected.  
> >     
> 
> 1.  Encryption: 3DES, DES, AES128, AES192, AES256 can be selected  
>     
> 
> > 1.  3DES: encrypts plaintext using three 64bit DES keys  
> >     
> > 
> > 1.  DES: encrypts a 64bit plaintext block with a 64bit key  
> >     
> > 
> > 1.  AES: Encrypts plaintext using the AES algorithm with a 128bit, 192bit, or 256bit key length  
> >     
> 
> 1.  Authentication: optional MD5, SHA1, SHA2-256, SHA2-384, SHA2-512  
>     
> 
> > 1.  MD5: Generate a 128bit message digest by entering a message of any length.  
> >     
> > 
> > 1.  SHA1: Input message length less than 128bit, generate 160bit message digest.  
> >     
> > 
> > 1.  SHA2-256: Output 256bit  
> >     
> > 
> > 1.  SHA2-384: Output 384bit  
> >     
> > 
> > 1.  SHA2-512: Output 512bit  
> >     
> 
> 1.  IPsec Mode: Encapsulation mode of the IPSec protocol  
>     
> 
> > 1.  Tunnel mode: Encapsulates an IPSec header (AH or ESP) outside the original IP header and then encapsulates the new IP header in the outermost layer, with the original IP message being protected by IPSec as part of the payload. Tunnel mode is typically used between two security gateways. A message encrypted at one security gateway can only be decrypted when it reaches the other security gateway.  
> >     
> > 
> > 1.  Transport mode: An IPSec header (AH or ESP) is inserted between the IP header and the upper layer protocol header. In this mode, the original IP header remains unchanged, except that the IP Protocol field is changed to AH or ESP and the IP header checksum is recalculated. Transport mode is used for communication between two hosts, or a host and a Security Gateway.  
> >     

1.  IPsec Tunnel Configuration

![](images/img_aa0a5dae.png)  

  

Basic Parameters  

1.  Destination Address: set the IP address or domain name of the counterpart IKE peer (configured as 0.0.0.0 when IG is server)  
    

1.  Map Interface: set the interface to which IPSec policy is applied  
    

1.  IKE Version: Set the version number of IKE protocol, IKEv1 and IKEv2 are supported.  
    

1.  IKEv1 Policy: the policy identifier defined in the IKEv1 policy list.  
    

1.  IKEv2 policy: the policy identifier defined in the IKEv2 policy list.  
    

1.  IPsec Policy: Policy identifiers that have been defined in the IPsec Policies list.  
    

1.  Authentication Type: two authentication methods are available, shared key and digital certificate.  
    

> 1.  Shared Key: user enters the shared key  
>     
> 
> 1.  Certificate: Users need to import the corresponding valid certificates in the certificate management page.  
>     

1.  Negotiation Mode: Sets the negotiation mode of IKEv1.  
    

> 1.  Main Mode: Main mode separates key exchange information from authentication information. This separation protects the identity information and thus provides a higher level of security  
>     
> 
> 1.  Aggressive Mode: Aggressive mode lacks authentication, but can meet the needs of some specific network environments. If the initiator's address is not known in advance, or if the initiator's address is always changing, and both parties want to use pre-shared key authentication to create an IKE SA, then brute force mode can be used.  
>     

1.  Local Subnet: the source network in the stream of interest as defined by IPESC  
    

1.  Remote Subnet: the destination network in the stream of interest as defined by IPESC

![](images/img_7d499773.png)  

1.  IKE Advance(Phase 1)

1.  Local ID: Sets the identity type of the local device in IKE negotiation  
    

> > 1.  IP Address: Fill in the address of the peer to establish the IPsec interface.  
> >     
> > 
> > 1.  FQDN: Use string as local identity  
> >     
> > 
> > 1.  User FQDN: Use the full domain name as the local identity.

1.  Remote ID: Sets the identity type of the counterpart device in IKE negotiation  
    

> > 1.  IP address: Use the IP address of the interface as the identity of the local end, and conduct IKE negotiation with the other end to interact with the identity information.  
> >     
> > 
> > 1.  FQDN: Set the name used for the identity of the peer device in IKE negotiation, which needs to be consistent with that set on the peer device.  
> >     
> > 
> > 1.  User FQDN: Same as the full domain name configured on the other end

1.  IKE Keeplive: Sets whether to enable the Peer Survival Detection DPD feature  
    

> > 1.  DPD Timeout: when the receiving end triggers a DPD query and actively sends a request message to the opposite end for detection and does not receive a DPD response message from the opposite end after the timeout time has elapsed, this IPsec SA will be deleted. legal value: 10-3600 Unit: sec.  
> >     
> > 
> > 1.  DPD Interval: used for the detection interval of IPSec neighbour status. After the DPD function is activated, when the receiving end does not receive the IPSec encrypted message from the opposite end within the time interval of triggering the DPD, it can trigger the DPD query to actively send a request message to the opposite end to detect the existence of IKE peers. Legitimate value: 1-60, unit: sec.

![](images/img_6afd54d7.png)  

IPsec Advanced (Phase 2)  

1.  Perfect Forward Stratification (PFS): PFS is a security feature that means that the cracking of one key does not affect the security of the other keys because there is no derivation between these keys. the IPSec phase 2 key is derived from the phase 1 key, and when the phase 1 IKE key is stolen, it is possible for an attacker to gather enough information to derive a key for the phase 2 IPSec SA. The PFS secures the phase 2 keys by performing an additional DH exchange.  
    

1.  IPsec SA lifetime: sets the lifecycle of the IPSec SA. the IPSec negotiation establishes the SA with the smaller of the lifecycle set at the local end or the lifecycle at the peer end.  
    

1.  IPsec SA Idle Idletime: When no data is transmitted within the configured idle time after IPsec is successfully established, the IPSec SA expires. before the IPSec SA is about to expire, IPSec negotiates to establish a new SA so that the new SA is ready before the old one expires.

![](images/img_3b34ce8e.png)  

Tunnel Advanced Options  

1.  Tunnel Start Mode: Setting the IPsec Enablement Method  
    

> 1.  Automatically: Automatically completes IKE negotiation to establish an IPSec tunnel after applying an IPSec policy. Commonly used in client mode  
>     
> 
> 1.  Respond Only: Only passively receives IPSEC requests and does not actively initiate connections. Commonly used in server mode  
>     
> 
> 1.  On-demand: IKE negotiation is completed and an IPSec tunnel is established only when an IPsec-defined packet passes through the interface.  
>     

1.  Fail times to Restart Interface: when the number of tunnel connection failures reaches the set value, restart the physical interface on which the tunnel was established; the default is 0, i.e., the interface is not restarted even after a failure, legal value: 1-12 times  
    

1.  Fail times to Rebot: when the number of tunnel connection failures reaches the set value, restart the current device; the default is 0, i.e., the device is not restarted even after the failure, legal value: 1-32 times  
    

1.  Local/Remote Send Cert Mode: you can choose to send certificate on request, always send certificate, do not send certificate  
    

> 1.  Send cert always: Some ipsec services do not send "request certificates" requests, but they do not store the peer's certificate locally, so the peer must be configured to "always send certificates" in order to establish IPSEC.  
>     
> 
> 1.  Send Cert if asked: local certificate is sent only when the peer sends a request  
>     
> 
> 1.  No certificates are sent: the local will send its own certificate to the other side, regardless of whether the other side sends a request or not  
>     

1.  ICMP Detect  
    

> 1.  ICMP Detect Server: address of the counterpart host for IPsec probes  
>     
> 
> 1.  ICMP Detection Local IP: source address of IPsec-protected traffic  
>     
> 
> 1.  ICMP Detection Interval: the time interval between ICMP probe messages sent by the device  
>     
> 
> 1.  ICMP Detection Timeout: If no ICMP response packet is received within the set ICMP detection timeout, the ICMP detection timeout is considered to have expired.  
>     
> 
> 1.  ICMP Detection Maximum Retries: Sets the maximum number of retries if an ICMP probe fails (the IPsec service will be restarted after the maximum number is reached)

#### 3.4.1.2 IPsec Extern Setting

![](images/img_9664b7de.png)  

The IPSec extension parameters are described below:

1.  Basic Parameters  
    

> 1.  Name: Sets the name of the IPsec Profile  
>     
> 
> 1.  IKE vVersion: Set the version number of IKE protocol, IKEv1 and IKEv2 are supported.  
>     
> 
> 1.  IKEv1 Policy: the policy identifier defined in the IKEv1 policy list.  
>     
> 
> 1.  IKEv2 Policy: the policy identifier defined in the IKEv2 policy list.  
>     
> 
> 1.  IPsec Policy: Policy identifiers that have been defined in the IPsec Policies list.  
>     
> 
> 1.  Negotiation Mode: Sets the negotiation mode of IKEv1.  
>     
> 
> > 1.  Main Mode: Main mode separates key exchange information from authentication information. This separation protects the identity information and thus provides a higher level of security  
> >     
> > 
> > 1.  Aggressive Mode: Aggresive mode lacks authentication, but can meet the needs of some specific network environments. If the initiator's address is not known in advance, or if the initiator's address is always changing, and both parties want to use pre-shared key authentication to create an IKE SA, then brute force mode can be used.  
> >     
> 
> 1.  Authentication methods: Two authentication methods are available, Shared key and Certificate  
>     
> 
> > 1.  Shared Key: user enters the shared key  
> >     
> > 
> > 1.  Certificate: Users need to import the corresponding valid certificates in the certificate management page.

![](images/img_3d9ca2e4.png)  

  

1.  IKE Advance(Phase 1)  
    

> 1.  Local ID: the local identifier corresponding to the selected local identifier type  
>     
> 
> 1.  Remote ID: the end-user identification corresponding to the selected end-user identification type  
>     
> 
> 1.  IKE Keepalive: Sets whether to enable the peer survival detection DPD function  
>     
> 
> > 1.  DPD Timeout: When the receiving end triggers the DPD query and actively sends a request message to the opposite end for detection, and does not receive the IPSec encryption message from the opposite end even after the timeout period, this ISAKMP Profile will be deleted.  
> >     
> > 
> > 1.  DPD Interval: used for the detection interval of IPSec neighbour status. After the DPD function is activated, when the receiving end does not receive the IPSec encrypted message from the other end within the time interval of triggering the DPD function, it can trigger the DPD query to send a request message to the other end to detect the existence of IKE peers.

![](images/img_7d5407af.png)  

1.  IPsec Advanced Options (Phase 2)  
    

> 1.  Perfect Forward Stratification (PFS): PFS is a security feature that means that the cracking of one key does not affect the security of the other keys because there is no derivation between these keys. the IPSec phase 2 key is derived from the phase 1 key, and when the phase 1 IKE key is stolen, it is possible for an attacker to gather enough information to derive the key for the phase 2 IPSec SA. The PFS secures the phase 2 keys by performing an additional DH exchange.  
>     
> 
> 1.  IPsec SA Lifetime: sets the lifecycle of the IPSec SA. the IPSec negotiation establishes the SA with the smaller of the lifecycle set at the local end or the lifecycle at the peer end.  
>     
> 
> 1.  Fail times to Restart Interface: when the number of tunnel connection failures reaches the set value, restart the physical interface on which the tunnel was established; the default is 0, i.e., the interface is not restarted even after a failure, legal value: 1-12 times  
>     
> 
> 1.  Fail times to Reboot: when the number of tunnel connection failures reaches the set value, restart the current device; the default is 0, i.e., the device is not restarted even after the failure, legal value: 1-32 times

Description:  

1.  The security of encryption algorithms in descending order is: AES, 3DES, DES, high security encryption algorithm implementation mechanism is complex, but slow computing speed. For general security requirements, DES algorithm can meet the needs  
    

1.  When the IG is used as an IPsec server, please configure the address of the counterpart as 0.0.0.0, which is generally used in scenarios where one end has a public network address and the other end has an unfixed dial-up address.  
    

1.  IPsec extensions are typically used in conjunction with GRE to build DMVP or GRE over IPsec networks.

### 3.4.2 GRE

Generic Routing Encapsulation (GRE) defines a protocol that encapsulates any other network layer protocol over any other network layer protocol.GRE can be used as a Layer 3 tunneling protocol for VPNs, providing a transparent transmission channel for VPN data. Simply put, GRE is a tunneling technology that provides a pathway on which encapsulated data messages can be transmitted, and encapsulates and decapsulates the data messages at both ends of the tunnel.

![](images/img_55fce68f.png)  

The GRE parameters are described below:

1.  Enable: Enables or disables the GRE function  
    

1.  Index: Sets the GRE tunnel name, in the range of 1-100.  
    

1.  Network Type: Select the GRE network type  
    

1.  Local Virtual IP: Set the local virtual IP address  
    

1.  Peer Virtual IP: set the counterparty virtual IP address, if subnet type, this item is the local subnet mask  
    

1.  Source Type: Select the source address type and set the IP address or interface name of the corresponding type.  
    

1.  Local IP: Configure the source address of the GRE tunnel  
    

1.  Peer IP: configures the destination address of the GRE tunnel  
    

1.  Key: Set the authentication key of the tunnel, the configuration should be the same at both ends.  
    

1.  MTU: Sets the maximum transmission unit of the GRE tunnel, in bytes  
    

1.  NHRP Enable: Next Hop Resolution Protocol, which is used by a source station connected to a Non-Broadcast Multi-Access (NBMA)-style subnetwork to determine the interconnecting Internet layer address and the NBMA subnet address of the NBMA next hop between arriving destination stations.  
    

> 1.  NHS IP Address: the address of the counterpart NHS server  
>     
> 
> 1.  Authentication Key: NHRP's authentication key  
>     
> 
> 1.  Hold Time: legal value 1-65535  
>     
> 
> 1.  Purge Forbid: enable/disable  
>     

1.  IPsec Profile: disabled, used in conjunction with IPsec extensions  
    

1.  Description: Descriptive information about the GRE tunnel

Description:

1.  NHRP is only used in DMVP networks, and generally GRE does not need to enable NHRP.  
    

1.  GRE is generally used in cases where both addresses are fixed public networks.

### 3.4.3 OpenVPN

In OpenVPN, if a user accesses a remote virtual address (belonging to the address series assigned to the virtual NIC, different from the real address), the operating system will send data packets (TUN mode) or data frames (TAP mode) to the virtual NIC through the routing mechanism, and the service programme receives the data and processes them accordingly, and sends them out from the extranet through SOCKET, the remote The service programme receives the data from the extranet via SOCKET and processes it accordingly, then sends it to the virtual NIC, which can be received by the application software, completing a unidirectional transmission process, and vice versa.

#### 3.4.3.1 OpenVPN Client

![](images/img_3e645093.png)  

The OpenVPN client parameters are described below:

1.  Enable: Enables or disables OpenVPN client  
    

1.  Index: Sets the tunnel ID  
    

1.  OpenVPN Server: Set the IP address or domain name of the OpenVPN server.  
    

1.  Port: the port number used when establishing OpenVPN   
    

1.  Protocol Type: selectable udp, tcp  
    

1.  Authentication Type: Select the authentication class and configure the parameters of the corresponding authentication type.  
    

1.  Description: customise the content of the tunnel description

![](images/img_44d84015.png)  

1.  Show Advanced Options  
    

> 1.  Virtual IP-start address: The client's virtual IP starting address is usually assigned and set by the server side.  
>     
> 
> 1.  Netmask: Subnet Mask of the Virtual IP  
>     
> 
> 1.  IP address number: the number of virtual IPs that can be assigned to the server  
>     
> 
> 1.  Source Interface: the interface used to establish OpenVPN  
>     
> 
> 1.  Interface Type: select the form of data sent out from this interface  
>     
> 
> > 1.  tun: Mostly used for IP-based communication.  
> >     
> > 
> > 1.  tap: Allows full Ethernet frames to pass through Openvpn tunnels, providing support for non-ip protocols.  
> >     
> 
> 1.  Network type: net30, p2p, subnet can be selected (this item can be ignored when the interface type is tap)  
>     
> 
> > 1.  net30: select 4 ips with mask 30 from the pool, use the larger of the two middle ips as the client's virtual NIC ip; use the smaller one as the client's peer ip.  
> >     
> > 
> > 1.  p2p: select an ip from the pool as the client's virtual NIC ip, and use your actual virtual NIC ip as the client's peer ip.  
> >     
> > 
> > 1.  subnet: select an ip from the pool as the client's virtual NIC ip, and use its own subnet mask as the client's subnet mask.  
> >     
> 
> 1.  Bridge Interface: used to connect multiple virtual machines or network devices so that they can communicate on the same network (this can be ignored when the interface type is configured in tun mode)  
>     
> 
> 1.  Cipher: The encryption protocol used by OpenVPN to transmit data, must be consistent with the server  
>     
> 
> 1.  HMAC: The checksum method used by OpenVPN to transmit data, data transmission fails if the checksum is not passed, and must be consistent with the server.  
>     
> 
> 1.  Compression LZO: The form of compression used for OpenVPN data transmission.  
>     
> 
> 1.  Redirect-Gateway: Directs the Client's default gateway to OpenVPN so that all Client traffic is forwarded through the OpenVPN interface.  
>     
> 
> 1.  Remote Float: allows the remote end to change its IP address/port  
>     
> 
> 1.  Link Detection Interval: The time to send connection detection messages after OpenVPN is successfully established.  
>     
> 
> 1.  Link Detection Timeout Time: After OpenVPN connection detection fails, L2TP re-establishes the connection when the maximum number of failures is reached.  
>     
> 
> 1.  MTU: Maximum Transmission Unit of the OpenVPN interface, in bytes  
>     
> 
> 1.  Enable Debug: Tap Enable  
>     
> 
> 1.  Expert Configuration: Configuring OpenVPN Extended Parameters  
>     
> 
> 1.  Import Configuration: Select the OpenVPN configuration file to be imported.

#### 3.4.3.2 OpenVPN server

![](images/img_f4afb7de.png)  

The OpenVPN server parameters are described below:

1.  Enable: Enables or disables the OpenVPN server.  
    

1.  Config Mode: Manual config, Import Config File can be selected  
    

1.  Manual Configuration  
    

> 1.  Authentication Type: Select the appropriate authentication type  
>     
> 
> 1.  Local IP Address: virtual IP address of the OpenVPN server interface  
>     
> 
> 1.  Remote IP Address: virtual IP address of the OpenVPN client  
>     
> 
> 1.  Description: Description information of the OpenVPN tunnel  
>     
> 
> 1.  Show Advanced Options: tap Enable  
>     
> 
> > 1.  Source Interface: Interface used to establish OpenVPN  
> >     
> > 
> > 1.  Interface Type: Select the form of data sent out of this interface.  
> >     
> > 
> > > 1.  tun: Mostly used for IP-based communication.  
> > >     
> > > 
> > > 1.  tap: Allows full Ethernet frames to pass through Openvpn tunnels, providing support for non-ip protocols.  
> > >     
> > 
> > 1.  Network Type: net30, p2p, subnet can be selected (this item can be ignored when the interface type is tap).  
> >     
> > 
> > 1.  Bridge Interface: used to connect multiple virtual machines or network devices so that they can communicate on the same network (this can be ignored when the interface type is configured in tun mode)  
> >     
> > 
> > 1.  Protocol Type: consistent with the client  
> >     
> > 
> > 1.  Port: the port number used by the OpenVPN service  
> >     
> > 
> > 1.  Cipher: The encryption protocol used by OpenVPN to transmit data, which must be consistent with the client's  
> >     
> > 
> > 1.  HMAC: The checksum method used by OpenVPN to transmit data; data transmission fails if the checksum is not passed. Must be consistent with the client  
> >     
> > 
> > 1.  Compression lZO: The form of compression used for OpenVPN data transmission. Consistent with the client  
> >     
> > 
> > 1.  Link Detection Interval: The time to send connection detection messages after OpenVPN is successfully established.  
> >     
> > 
> > 1.  Link Detection Timeout Time: After OpenVPN connection detection fails, L2TP re-establishes the connection when the maximum number of failures is reached.  
> >     
> > 
> > 1.  MTU: Maximum Transmission Unit of the OpenVPN interface, in bytes  
> >     
> > 
> > 1.  TCPMSS: Maximum data length that can be transmitted in a single TCP message  
> >     
> > 
> > 1.  Fragment: When the length of a message in the network exceeds the MTU (Maximum Transmission Unit) in the path, it may be necessary to fragment the message into smaller pieces for transmission.  
> >     
> > 
> > 1.  Enable Debug: Tap Enable  
> >     
> > 
> > 1.  Expert Configuration: Configuring OpenVPN Extended Parameters

![](images/img_1a847ed4.png)  

1.  User Password: the user/password configured by the server when using the user password authentication type  
    

1.  Local Subnet: the route from OpenVPN server to client, usually fill in the subnet where the client actually communicates.  
    

1.  Client Subnet: static route pushed to the client by the OpenVPN server

### 3.4.4 Certificate Management

Scep (Simple Certificate Enrollment Protocol) is a communication protocol for device certificate management developed by cisco and Verisign. It utilises a combination of existing PKCS#7 and PKCS#10 protocol technologies and enjoys extensive support for client and CA implementations.

Certificate Management:

![](images/img_e752282b.png)  

The certificate management parameters are described below:

1.  Enable SCEP(Simple Certificate Enrollment Protocol): Enable or disable Certificate Request Protocol  
    

1.  Forced to re-enroll: Forced reapplication means not detecting the current certificate status and restarting the certificate application service every time.  
    

1.  Status: the current state of the device applying for a certificate, divided into initialize Enrolling, Re-Enrolling, Complete four states  
    

1.  Protect Key: the certificate protection key set when applying for certificates, plays a role in digital certificate encryption, when importing and exporting certificates configured to protect the key and the key when applying for certificates can be used in the same way  
    

1.  Protect Key Confirm: verify the certificate protection key.  
    

1.  Strict CA: Set the CA identifier trusted by the device, when applying for certificates through a trusted entity certification authority to complete the registration and issuance of entity certificates, so it is necessary to specify a trusted CA identifier will be bound to the device and the CA, the device certificate application, acquisition, revocation and query are implemented through the CA  
    

1.  Server URL: URL address of the certificate server, the URL of the enrolment server must be specified before the certificate application, and then the entity can make the certificate application to this server through SCEP. For example: [http://100.17.145.158:8080/certsrv/mscep/mscep.dll](http://invalid.uri/)  
    

1.  Common Name: Specify the name of the certificate to be applied for, i.e., the certificate common name.  
    

1.  FQDN: Set the certificate's FQDN (Fully Qualified Domain Name) FQDN is a unique identifier for an entity on a network, consisting of a hostname and domain name that can be resolved to an IP address. For example, www is a host name and whatever.com is a domain name, then [www.whatever.com](http://invalid.uri/) is an FQDN.  
    

1.  Unit 1: Name of the unit to which the configuration certificate belongs 1  
    

1.  Unit 2: Name of the unit to which the configuration certificate belongs 2  
    

1.  Domain: Qualified domain name to configure the certificate  
    

1.  Serial Number: Configure the serial number of the requested certificate  
    

1.  Challenge: set the challenge password for certificate application, the challenge code is the password to be used when revoking the certificate (optional)  
    

1.  Challenge Confirm: Verify the authentication password, same as the above configuration.  
    

1.  Unstructured address: Sets the IP address used for the certificate  
    

1.  RSA Key Length: legal value: 128-2048, unit: bit  
    

1.  Poll Interval: the time interval for the device to query the current certificate status to the certificate server, legal value: 30-3600, unit: second  
    

1.  Poll Timeout: Set the maximum time for the device to query the certificate status, when the timeout time is reached, it is considered that this certificate application fails. Legal value: 30-86400, unit: second  
    

1.  Revocation: enable or disable certificate revocation  
    

> 1.  CRL URL: CRL is Certificate Revocation List, set the URL of the CRL issuing point.  
>     
> 
> 1.  OCSP URL: Configure the URL of the OCSP server, which is usually the same as the URL of the certificate server.  
>     

1.  Certificates: import relevant certificates

![](images/img_a1c6a4dc.png)

Note: When using certificates, ensure that the device time is synchronised with the actual time

ROOT CA:

Import the pre-registered ROOT CA certificate

![](images/img_e1b53b79.png)

## 3.5 Industrial interfaces

### 3.5.1 DTU

#### 3.5.1.1 Serial port settings

Set the parameters of the IG serial port according to the serial port parameters of the terminal device connected to the IG to achieve normal communication between the IG and the terminal device.

![](images/img_e1abc1d9.png)  

The serial port setting parameters are described below:

1.  Serial Type: The type and number of serial ports of different series of IG are not the same, so choose according to the actual situation.   
    

1.  Baudrate: This is a parameter that measures the rate at which symbols are transmitted. It indicates the number of symbols transmitted per second  
    

1.  Data Bits: parameter to set the actual data bits in the communication  
    

1.  Parity: the error checking method in serial communication, generally parity or no parity in two ways  
    

1.  Stop Bit: Used to indicate the last bit of a single packet. Typical values are 1, 1.5, and 2 bits.  
    

1.  Software Flow Control: Flow control for serial communications provides a mechanism for blocking communication when it is not possible for some reason. Flow control allows the data receiving device to notify the data sending device when it is unable to receive data, causing it to stop sending.  
    

1.  Description: custom description  
    

Attention:

1.  The serial port parameters of the IG and the serial port parameters of the connected terminal device must be set the same way.  
    

1.  DTU function and GNSS serial port forwarding function cannot be enabled at the same time.

#### 3.5.1.2 DTU1

![](images/img_825fa747.png)  

The DTU 1 parameters are described below:

1.  Enable: Tap Enable  
    

1.  DTU Protocol: Transparent transmission, TCP server, RFC2217 mode, IEC101 to 104, Modbus bridge, DC protocol can be selected.  
    

> 1.  Transparent transport and TCP-Server: if a transparent transport device is selected as client, a TCP server device is selected as server.  
>     
> 
> 1.  RFC2217: No need to set up the serial port configuration after selecting this mode.  
>     
> 
> 1.  IEC101 to 104: for the power industry, similar to TCP  
>     

1.  Transmit Protocol: TCP and UDP optional  
    

1.  Connection Type: long and short connections available  
    

> 1.  Long-Lived: TCP client and TCP server establish a connection and then keep the TCP connection.  
>     
> 
> 1.  Short-Lived: After the TCP client and TCP server establish a connection, when there is no data transmission during the idle time, it will automatically disconnect from the server TCP connection.  
>     

1.  Keepalive Interval: the time interval between TCP client and TCP server to send TCP heartbeat messages periodically after the connection is established, which is used to detect the connectivity between the client and the server.  
    

1.  Keepalive Retry: When the TCP heartbeat timeout, the device re-sends the TCP heartbeat and reestablishes the TCP connection after reaching the set heartbeat retry times.  
    

1.  Serial Buffer Frame: the size of serial port buffer set when sending and receiving data, default 4K.  
    

1.  Packet Size: the size of a frame of data set when the serial port sends data. It starts to send when the set value is reached. Legal value: 1-1024, unit: byte  
    

1.  Force Transmit Timer: when the serial port sends data, when the sending interval is greater than the set sub-frame interval, the device will automatically send the sub-frame, legal value: 10-65535, unit: milliseconds  
    

1.  Min Reconnect Interval: user-defined minimum reconnect interval. When the device starts to connect, if it does not connect successfully, it will reconnect according to this minimum reconnection interval. Until the user-defined maximum reconnection interval is reached. Legal value: 15-60, unit: sec.  
    

1.  Max Reconnect Interval: User-defined maximum reconnect interval. After the device starts to connect and the connection time reaches the maximum reconnection interval, it will connect once every this interval (i.e. user-defined maximum reconnection interval). Legitimate value: 60-3600 in seconds.  
    

1.  Multi-server policy: optional concurrency, polling  
    

> 1.  Parallel: simultaneous de-connection to the centre of the destination IP address list  
>     
> 
> 1.  Polling: connect to the centre at the front of the list first, and if it is connected, then no more connections to the back; if it is not connected, then it is connected in descending order until it is connected to a centre.  
>     

1.  Source Interface: general users do not have to choose  
    

1.  Local IP Address: the IP address of the device interface when IP is selected for the source interface. Generally, users do not need to configure it, and it can be empty.  
    

1.  DTU ID: customised, DTU identification automatically sent to the server after successfully connecting to the server. It can also not be configured, keep empty state  
    

1.  Enable Debug: Tap on to print DTU related logs when it is turned on  
    

1.  Enable Report ID: Tap Enable  
    

> 1.  Heartbeat Interval: This is only required if ReportID is enabled Legal value: 1-65535, unit: sec.  
>     
> 
> 1.  Heartbeat Packet Content: This is required to enable ReportID.  
>     

1.  Destination IP Address  
    

> 1.  Server Address: Customise the IP address of the server to which the device will connect.  
>     
> 
> 1.  Server Port: customise the server port to which the device will connect

Description: Up to 10 destination IP addresses can be set.

#### 3.5.1.3 DTU2

Same as DTU1.