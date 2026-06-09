# Portable Router CR202-Lite Product User Manual

## Preface

### Statement

Thank you for choosing our product. Before use, please read this user manual carefully. Complying with the following statements will help maintain intellectual property rights and legal compliance, ensuring that the user experience aligns with the latest product information. If there are any questions or if written permission is required, please contact our technical support team at any time.

- Copyright Statement

This user manual contains copyrighted content, and the copyright belongs to Beijing InHand Networks Technology Co., Ltd. and its licensors. Without written permission, no organization or individual may excerpt or copy any part of the content of this manual, or distribute it in any form.

- Disclaimer

Due to ongoing updates in product technology and specifications, the company cannot guarantee that the information in this user manual is entirely consistent with the actual product. Therefore, no disputes arising from any discrepancies between the actual technical parameters and this user manual are accepted. Any changes to the product will not be notified in advance, and the company reserves the right to make the final changes and interpretations.

- Copyright Information

The content of this user manual is protected by copyright laws, and the copyright belongs to Beijing InHand Networks Technology Co., Ltd. and its licensors, reserving all rights. Without written permission, the content of this manual may not be used, copied, or distributed without authorization.

### GUI Conventions


| Symbol      | Meaning                                                                                    | Example                                             |
| ----------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| `< >`       | Indicates a variable or parameter to be replaced with an actual value                      | `<IP Address>` means to enter a specific IP address |
| `" "`       | Indicates a text label on the interface                                                    | Click the "Save" button                             |
| `→`         | Indicates menu hierarchy or operation sequence                                             | [Network] → [Cellular]                              |
| `[ ]`       | Indicates a menu or page name                                                              | Go to the [System Settings] page                    |
| **Caution** | Points to note during operation; improper actions may result in data loss or device damage | —                                                   |
| **Note**    | Provides supplementary and necessary explanations for the operation description            | —                                                   |


### Technical Support

**Beijing InHand Networks Technology Co., Ltd. (Headquarters)**

Phone: 010-8417 0010

Address: 5th Floor, Building 3, No. 18 Ziyue Road, Chaoyang District, Beijing

**Chengdu Office**

Phone: 028-8679 8244

Address: 14th Floor, China Taiping Financial Building, No. 1777 North Tianfu Avenue, Wuhou District, Chengdu, Sichuan

**Guangzhou Office**

Phone: 020-8562 9571

Address: Unit B-130, Yuanyang New Third Board Creative Park, No. 5 Tandong East Road, Tianhe District, Guangzhou

**Wuhan Office**

Phone: 027-8716 3566

Address: Room 2001, Building 11, Paris Haoting, No. 2 Luoyu East Road, Hongshan District, Wuhan, Hubei

**Shanghai Office**

Phone: 021-5480 8501

Address: Room 1103, No. 18 Shunyi Road, Putuo District, Shanghai

### How to Use This Manual

**Matching the right reader**

- First-time users: It is recommended to read in sequence: [Understanding the Device] → [Installation and First Use] → [Common Scenario Configuration] → [Function Description and Parameter Reference].
- Existing device users: Can directly refer to [Function Description and Parameter Reference] or [Appendix: Troubleshooting].
- Cloud platform management users: Can refer to [Common Scenario Configuration] for device remote management platform content.

**Quick navigation by task**


| Task                               | Corresponding Chapter                                                                                   | Estimated Time     |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------ |
| Device installation and Web login  | [Installation and First Use](#chapter-2-installation-and-first-use)                                     | Approx. 10 minutes |
| Configure cellular Internet access | [Common Scenario Configuration](#chapter-3-common-scenario-configuration)                               | Approx. 5 minutes  |
| Configure Wi-Fi AP                 | [Common Scenario Configuration](#chapter-3-common-scenario-configuration)                               | Approx. 5 minutes  |
| Connect to cloud platform          | [Common Scenario Configuration](#chapter-3-common-scenario-configuration)                               | Approx. 5 minutes  |
| Monitor device status              | [Function Description and Parameter Reference](#chapter-4-function-description-and-parameter-reference) | Approx. 10 minutes |
| Troubleshoot network issues        | [Appendix: Troubleshooting](#appendix-troubleshooting)                                                  | On demand          |


---

## Chapter 1 Understanding the Device

### 1.1 Overview

CR202-Lite is a portable 4G cellular router designed to provide reliable Internet connectivity for remote office, mobile, and field scenarios. It supports wired-to-wireless access, which increases network access diversity and helps ensure uninterrupted connectivity. The built-in battery (available on selected models) enables operation anytime and anywhere, while the lightweight design allows unrestricted device mobility.

Combined with the InHand Device Manager cloud management platform, CR202-Lite provides efficient device management capabilities, delivering high-speed network access and convenient network management services.

### 1.2 Appearance and Interfaces



**Figure 1-1 CR202-Lite Panel Introduction**


| Interface      | Position    | Function Description                                       |
| -------------- | ----------- | ---------------------------------------------------------- |
| Type-C Port    | Panel side  | Power input (5V/2A) and charging interface                 |
| SIM Card Slot  | Panel side  | Nano SIM card insertion slot                               |
| RESET Button   | Panel side  | Restore factory defaults and reboot                        |
| ON/OFF Button  | Panel side  | Power on/off (battery-equipped models only)                |
| LAN/WAN1 Port  | Panel side  | Ethernet interface for LAN or wired WAN access             |
| LED Indicators | Panel front | Display system, network, Wi-Fi, signal, and battery status |


### 1.3 LED Indicators

#### CR202-Lite (No Battery)


| LED     | Status          | Meaning                                              |
| ------- | --------------- | ---------------------------------------------------- |
| System  | Off             | Power off                                            |
|         | Blinking green  | Device starting                                      |
|         | Steady green    | Device working                                       |
|         | Blinking yellow | Upgrading                                            |
| Network | Off             | Cellular disabled                                    |
|         | Blinking green  | Dialing up                                           |
|         | Steady green    | Dialed successfully                                  |
|         | Blinking yellow | Dialing abnormal                                     |
|         | Blinking red    | No SIM card, cannot read SIM card, or modem abnormal |
| Wi-Fi   | Off             | Wi-Fi disabled                                       |
|         | Blinking green  | Wi-Fi connected, data transmitting                   |
|         | Steady green    | Wi-Fi enabled                                        |
| Signal  | Off             | Cellular disabled                                    |
|         | Steady green    | Dialed up, signal level ≥ 20                         |
|         | Steady yellow   | Dialed up, 19 ≥ signal level ≥ 10                    |
|         | Steady red      | Dialed up, 9 ≥ signal level                          |


#### CR202-Lite (With Battery)


| LED     | Status          | Meaning                                              |
| ------- | --------------- | ---------------------------------------------------- |
| System  | Off             | Power off                                            |
|         | Blinking green  | Device starting                                      |
|         | Steady green    | Device working                                       |
|         | Blinking yellow | Upgrading                                            |
| Network | Off             | Cellular disabled                                    |
|         | Blinking green  | Dialing up                                           |
|         | Blinking yellow | Dialing abnormal                                     |
|         | Blinking red    | No SIM card, cannot read SIM card, or modem abnormal |
|         | Steady green    | Dialed up, signal level ≥ 20                         |
|         | Steady yellow   | Dialed up, 19 ≥ signal level ≥ 10                    |
|         | Steady red      | Dialed up, 9 ≥ signal level                          |
| Wi-Fi   | Off             | Wi-Fi disabled                                       |
|         | Blinking green  | Wi-Fi connected, data transmitting                   |
|         | Steady green    | Wi-Fi enabled                                        |
| Battery | Blinking        | Battery charging                                     |
|         | Steady          | Battery discharging                                  |
|         | Green           | 80% < battery level ≤ 100%                           |
|         | Yellow          | 20% < battery level ≤ 80%                            |
|         | Red             | 0 < battery level ≤ 20%                              |


### 1.4 Restore Factory Settings

To restore the device to default settings using the reset button, perform the following steps:

1. Power on the device.
2. Press and hold the **RESET** button until the **System LED** turns **yellow**, then release the button.
3. When the **System LED** starts flashing **yellow**, press and hold the **RESET** button again.
4. When the **System LED** starts flashing **green** slowly, release the **RESET** button. The device will now be restored to its default settings and will restart normally.

### 1.5 Default Settings


| Parameter            | Default Value                     |
| -------------------- | --------------------------------- |
| LAN IP Address       | 192.168.2.1                       |
| Subnet Mask          | 255.255.255.0                     |
| Web Login Username   | adm (printed on device nameplate) |
| Web Login Password   | Printed on device nameplate       |
| Wi-Fi SSID           | inhand                            |
| Wi-Fi Authentication | Open type                         |
| Wi-Fi Encryption     | NONE                              |
| DHCP Service         | Enable                            |
| DHCP IP Pool Range   | 192.168.2.2 ~ 192.168.2.100       |


---

## Chapter 2 Installation and First Use

### 2.1 Pre-Installation Preparation

Before installing the device, ensure the following conditions are met:


| Item             | Requirement                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| Network Coverage | 3G/4G cellular network coverage is available at the installation location                          |
| PC               | Windows 7, Windows 10, or Windows 11; at least one Ethernet port (10M/100M)                        |
| SIM Card         | Enabled with data service; account is active (not suspended)                                       |
| Power Supply     | 5V/2A Type-C interface, or internal battery (battery-equipped models)                              |
| Environment      | Flat, stable surface; avoid direct sunlight, heat sources, and strong electromagnetic interference |


> **Caution**: The device shall be installed and operated in powered-off status!

> **Caution**: Do not use or leave the device at very high temperature conditions (for example, strong direct sunlight or a vehicle in extremely hot conditions). Otherwise, the built-in battery may overheat, catch fire, or its performance will degrade and its service life will decrease. Do not immerse the device in water. Store it in a cool and dry environment when not in use.

### 2.2 Installation Guide

#### 2.2.1 SIM/UIM Card Installation

CR202-Lite supports a single nano SIM card or eSIM. To install a nano SIM card, follow the illustration below.



**Figure 2-1 SIM Card Installation**

#### 2.2.2 Power Supply

CR202-Lite supports internal battery or Type-C interface (5V/2A). Pay attention to the power voltage level.

#### 2.2.3 PC Network Configuration

After hardware installation, ensure the Ethernet card is installed in the supervisory PC before logging in to the Web settings page.

**I. Automatic Acquisition of IP Address (Recommended)**

Set the supervisory computer to "automatic acquisition of IP address" and "automatic acquisition of DNS server address" (default computer system configuration) to allow the device to automatically assign an IP address to the supervisory computer.

**II. Set a Static IP Address**

Set the IP address of the supervisory PC (for example, 192.168.2.2) to the same network segment as the LAN interface of the device (initial IP address of LAN interface: 192.168.2.1, subnet mask: 255.255.255.0).



**Figure 2-2 Automatic Acquisition of IP Address (Left) and Static IP Address (Right)**

**III. Cancel the Proxy Server**

If the current supervisory PC uses a proxy server to access the Internet, cancel the proxy service. The operating steps are as follows:

1. In the browser window, select "Tools >> Internet options".
2. Select the "Connections" page and click the "LAN Settings" button to enter the "LAN Settings" window.
3. Confirm whether the option "Use a Proxy Server for LAN" is checked; if checked, cancel it and click the **OK** button.

**IV. Log In to / Exit the Web Settings Page**

Access the default IP address 192.168.2.1 in a browser, enter the username and password (refer to the nameplate at the bottom of the device for login credentials) in the pop-up window, and access the router's WEB management page. If the browser alarms that the connection is not private, select "Advanced" and proceed to the address.



**Figure 2-3 Web Login Page**

> **Caution**: For security, modify the default login password after the first login and keep the password information safe.

### 2.3 Quick Check

After installation is complete, verify the following items:

- The SIM card is properly inserted and the device is powered on.
- The System LED indicates the device is working (steady green).
- The Network LED indicates normal dialing status (steady green) or signal strength.
- The PC can obtain an IP address automatically or is configured in the same subnet as the device.
- The Web management page can be accessed at 192.168.2.1.

---

## Chapter 3 Common Scenario Configuration

### Scenario 1: Cellular Internet Access

**Goal**: Access the Internet via the 4G cellular network.

**Prerequisites**: A valid nano SIM card is installed, and the device is powered on.

**Estimated Time**: Approx. 5 minutes.

**Operation Steps**:

1. Install the nano SIM card according to [SIM/UIM Card Installation](#221-simuim-card-installation).
2. Log in to the Web management page.
3. Navigate to [Network] → [Cellular].
4. Ensure the "Enable" checkbox is selected.
5. Select the appropriate "SIM Network Provider" profile or configure the APN parameters provided by the carrier.
6. Click the **Save** button and wait for the connection to establish.

**Verification Method**:

1. Observe the Network LED; it should turn steady green when dialed successfully.
2. On a connected PC, open a browser and verify access to an external website.
3. Alternatively, use the Ping tool in [Tools] → [Ping] to test connectivity to a public IP address.

**Common Issues**:

- Network connection fails: Check whether the SIM card is correctly inserted and whether the APN parameters match the carrier requirements.
- Data transmission is abnormal: Check the signal strength indicator and verify the data plan balance.

### Scenario 2: Wired WAN Internet Access

**Goal**: Access the Internet via a wired broadband connection.

**Prerequisites**: An Ethernet cable is connected between the WAN/LAN1 port and the upstream network device.

**Estimated Time**: Approx. 5 minutes.

**Operation Steps**:

1. Connect the Ethernet cable to the WAN/LAN1 port.
2. Log in to the Web management page.
3. Navigate to [Network] → [WAN/LAN Switch].
4. Configure the port as WAN.
5. Select the access type: Static IP, Dynamic Address (DHCP), or ADSL Dialing (PPPoE), and fill in the parameters provided by the ISP.
6. Click the **Save** button.

**Verification Method**:

1. Navigate to [Status] → [Network Connections] and verify that the WAN connection shows a valid IP address.
2. On a connected PC, open a browser and verify access to an external website.

**Common Issues**:

- No IP address obtained: Check the Ethernet cable connection and confirm the upstream device is functioning.
- PPPoE dialing fails: Verify the username and password provided by the ISP.

### Scenario 3: Wi-Fi AP Configuration

**Goal**: Provide wireless LAN access for local devices.

**Prerequisites**: The device has established an Internet connection via cellular or wired WAN.

**Estimated Time**: Approx. 5 minutes.

**Operation Steps**:

1. Log in to the Web management page.
2. Navigate to [Network] → [Switch WLAN Mode] and ensure the device is set to AP mode. Save and reboot if the mode was changed.
3. Navigate to [Network] → [WLAN].
4. Configure the SSID, authentication method, and encryption type as required.
5. Click the **Save** button.

**Verification Method**:

1. Use a wireless client (such as a smartphone or laptop) to scan for the configured SSID.
2. Connect to the SSID and verify Internet access.

**Common Issues**:

- SSID not visible: Ensure "SSID broadcast" is enabled.
- Cannot connect to Wi-Fi: Verify the authentication method and password match the client configuration.

### Scenario 4: Cloud Management Platform Connection

**Goal**: Register the device to InHand Device Manager for remote management.

**Prerequisites**: The device can access the Internet, and a Device Manager account has been registered.

**Estimated Time**: Approx. 5 minutes.

**Operation Steps**:

1. Log in to the Web management page.
2. Navigate to [Services] → [Device Manager].
3. Enable the Device Manager function.
4. Select the appropriate server address: `iot.inhand.com.cn` (China) or `iot.inhandnetworks.com` (global).
5. Enter the registered account name.
6. Click the **Save** button.

**Verification Method**:

1. Navigate to [Status] → [Device Manager] to check the connection status between the router and the platform.
2. Log in to the Device Manager web portal and confirm the device appears in the device list.

**Common Issues**:

- Device cannot connect to the platform: Verify the device has Internet access and that the server address and account are correct.
- Device does not appear online: Check the firewall settings and ensure the Device Manager service port is not blocked.

---

## Chapter 4 Function Description and Parameter Reference

### 4.1 System

#### 4.1.1 Basic Setup

This part is used to check and configure the system time, router WEB configuration interface, language, and the name of the router.

Check and set the WEB configuration interface language and the name of the router.

From the navigation tree, select [System] → [Basic Setup], then enter the "Basic Setup" page.

Table 4-1-1 Basic Setup Parameters


| **Basic settings**                                                                              |                                                                        |             |
| ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ----------- |
| Function description: Select display language of the router web page and set personalized name. |                                                                        |             |
| **Parameters**                                                                                  | **Description**                                                        | **Default** |
| Language                                                                                        | Configure language of WEB configuration interface                      | English     |
| Host Name                                                                                       | Set a name for the host or device connected to the router for viewing. | Router      |


#### 4.1.2 System Time

To ensure coordination between this device and other devices, set the system time accurately. This function is used to configure and check the system time and system time zone.

From the navigation tree, select [System] → [Time], then enter the "Time" webpage. Click **Sync Time** to synchronize the time of the router with the system time of the PC.

Table 4-1-2 Parameters of System Time


| **System Time**                                                               |                                                                                                 |                        |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------- |
| Function description: Set local time zone and automatic updating time of NTP. |                                                                                                 |                        |
| **Parameters**                                                                | **Description**                                                                                 | **Default**            |
| Time of Router                                                                | Display present time of router                                                                  | 8:00:00 AM, 12/12/2015 |
| PC Time                                                                       | Display present time of PC                                                                      | Present time           |
| Timezone                                                                      | Set time zone of router                                                                         | Custom                 |
| Custom TZ String                                                              | Set TZ string of router                                                                         | CST-8                  |
| Auto update Time                                                              | Select whether to automatically update time; options include on startup or every 1/2/... hours. | On startup             |
| NTP Time Servers                                                              | Select NTP server to synchronize time                                                           | 1.pool.ntp.org         |


#### 4.1.3 Admin Access

Admin services include HTTP, HTTPS, TELNET, and SSHD.

- **HTTP**: Hypertext Transfer Protocol, used for transferring web pages on the Internet. After enabling HTTP service, users can log on via HTTP and access and control the device using a web browser.
- **HTTPS**: Secure Hypertext Transfer Protocol, the secure version of HTTP supporting SSL protocol.
- **TELNET**: Telnet protocol provides telnet and virtual terminal functions through a network. The device supports Telnet Client and Telnet Server.
- **SSHD**: SSH protocol provides security for remote login sessions and other network services. The SSHD service uses the SSH protocol, which has higher security than Telnet.

From the navigation tree, select [System] → [Admin Access], then enter the "Admin Access" page.

Table 4-1-3 Parameters of Admin Access


| **Admin Access**                                                                                                                                                                |                                                                                                                                                                   |                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Function description: 1. Modify username and password of router. 2. The router can be accessed by the following 4 methods: HTTP, HTTPS, TELNET, and SSHD. 3. Set login timeout. |                                                                                                                                                                   |                                                                                                       |
| **Parameters**                                                                                                                                                                  | **Description**                                                                                                                                                   | **Default**                                                                                           |
| **Username/Password**                                                                                                                                                           |                                                                                                                                                                   |                                                                                                       |
| Username                                                                                                                                                                        | Set name of user who logs in to WEB configuration page                                                                                                            | adm                                                                                                   |
| Old Password                                                                                                                                                                    | Previous password for access to WEB configuration page                                                                                                            |                                                                                                       |
| New Password                                                                                                                                                                    | New password for access to WEB configuration page                                                                                                                 | N/A                                                                                                   |
| Confirm New Password                                                                                                                                                            | Reconfirm the new password                                                                                                                                        | N/A                                                                                                   |
| **Admin functions**                                                                                                                                                             |                                                                                                                                                                   |                                                                                                       |
| Service Port                                                                                                                                                                    | Service port of HTTP/HTTPS/TELNET/SSHD                                                                                                                            | 80/443/23/22                                                                                          |
| Local Access                                                                                                                                                                    | Enable — Allow local LAN to administrate the router with corresponding service; Disable — Local LAN cannot administrate the router with corresponding service     | Enable                                                                                                |
| Remote Access                                                                                                                                                                   | Enable — Allow remote host to administrate the router with corresponding service; Disable — Remote host cannot administrate the router with corresponding service | Enable                                                                                                |
| Allowed Access from WAN (Optional)                                                                                                                                              | Set allowed access from WAN                                                                                                                                       | Set the hosts which are allowed to access the router, e.g. 192.168.2.1/30 or 192.168.2.1-192.168.2.10 |
| Description                                                                                                                                                                     | For recording significance of various parameters of admin functions (without influencing router configuration)                                                    | N/A                                                                                                   |
| **Non-privileged users**                                                                                                                                                        |                                                                                                                                                                   |                                                                                                       |
| Username                                                                                                                                                                        | Configure non-privileged login user name                                                                                                                          | N/A                                                                                                   |
| Password                                                                                                                                                                        | Configure the password of the non-privileged user                                                                                                                 | N/A                                                                                                   |
| **Other Parameters**                                                                                                                                                            |                                                                                                                                                                   |                                                                                                       |
| Log Timeout                                                                                                                                                                     | Set login timeout (router will automatically disconnect the configuration interface after login timeout)                                                          | 500 seconds                                                                                           |


#### 4.1.4 System Log

A remote log server can be set through "System Log", and all system logs will be uploaded to the remote log server through the Internet. This requires remote log software, such as Kiwi Syslog Daemon, on the remote log server.

Kiwi Syslog Daemon is a free log server software for Windows. It can receive, record, and display logs from hosts (such as routers, exchange boards, and Unix hosts). After downloading and installing Kiwi Syslog Daemon, it must be configured through the menus "File >> Setup >> Input >> UDP".

From the navigation tree, select [System] → [System Log], then enter the "System Log" page.

Table 4-1-4 Parameters of System Log


| **System Log**                                                                                                |                                           |             |
| ------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ----------- |
| Function description: Configure IP address and port number of remote log server which will record router log. |                                           |             |
| **Parameters**                                                                                                | **Description**                           | **Default** |
| Log to Remote System                                                                                          | Enable log server                         | Disable     |
| Log server address and port (UDP)                                                                             | Set address and port of remote log server | N/A: 514    |


#### 4.1.5 Configuration Management

Here you can back up the configuration parameters, import the desired parameter backup, and reset the router.

From the navigation tree, select [System] → [Config Management], then enter the "Config Management" page.

Table 4-1-5 Parameters of Configuration Management


| **Configuration Management**                                      |                                                                                                     |             |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------- |
| Function description: Set parameters of configuration management. |                                                                                                     |             |
| **Parameters**                                                    | **Description**                                                                                     | **Default** |
| Browse                                                            | Choose the configuration file                                                                       | N/A         |
| Import                                                            | Import configuration file to router                                                                 | N/A         |
| Backup                                                            | Backup configuration file to host                                                                   | N/A         |
| Restore default configuration                                     | Select to restore default configuration (effective after rebooting)                                 | N/A         |
| Disable the hardware reset button                                 | Select to disable hardware reset button of the router                                               | Disable     |
| Network Provider (ISP)                                            | For configuring APN, username, password, and other parameters of network providers across the world | N/A         |



|                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| icon Validity and order of imported configurations should be ensured. Acceptable configuration will later be serially executed in order after system reboot. If the configuration files are not arranged according to effective order, the system will not enter the desired state. |
| icon In order not to affect the operation of the current system, after performing an import configuration and restore default configuration, restart the device to make the new configuration take effect.                                                                          |


#### 4.1.6 Scheduler

After this function is enabled, the device will reboot at the scheduled time. The scheduler function will take effect after the router synchronizes time.

From the navigation tree, select [System] → [Scheduler], then enter the "Scheduler" page.

Table 4-1-6 Parameters of Scheduler


| **Scheduler**                                          |                                                                                                                                                                                         |             |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Function description: Set scheduler for system reboot. |                                                                                                                                                                                         |             |
| **Parameters**                                         | **Description**                                                                                                                                                                         | **Default** |
| Enable                                                 | Enable/disable this function                                                                                                                                                            | Disable     |
| Time                                                   | Select the reboot time                                                                                                                                                                  | 0:00        |
| Days                                                   | Reboot the router every day                                                                                                                                                             | Everyday    |
| Show advanced options                                  | Enable more detailed schedule rules, allowing multiple rules to reboot the router at specific times or intervals. Enabling this feature will disable the everyday reboot feature above. | Disable     |
| Reboot after dialed                                    | Router will reboot after dial-up successfully; will not take effect if this parameter is blank.                                                                                         | N/A         |


#### 4.1.7 Upgrade

The upgrading process can be divided into two steps. In the first step, firmware will be written to the backup file zone; in the second step, firmware in the backup file zone will be copied to the main firmware zone, which should be carried out during system restart. During software upgrading, any operation on the web page is not allowed, otherwise software upgrading may be interrupted.

From the navigation tree, select [System] → [Upgrade], then enter the "Upgrade" page.

To upgrade the system:

1. Click **Browse** to choose the upgrade file.
2. Click **Upgrade** and then click **OK** to begin the upgrade.
3. After the upgrade succeeds, click **Reboot** to restart the device.

#### 4.1.8 Reboot

Save the configurations before rebooting, otherwise the configurations that are not saved will be lost after reboot.

To reboot the system, click [System] → [Reboot], then click **OK**.

#### 4.1.9 Logout

To log out, click [System] → [Logout], and then click **OK**.

### 4.2 Network

#### 4.2.1 Cellular

Insert a SIM card and dial up to achieve the wireless network connection.

Click [Network] → [Cellular] in the navigation tree to enter the Cellular configuration page.

Table 4-2-1-1 Parameters of Cellular


| **Cellular**                                                                                                                                  |                                                                                                                                                                                                                                                                                                        |                |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| Function description: Configure parameters of PPP dial-up. Generally, users only need to set basic configuration instead of advanced options. |                                                                                                                                                                                                                                                                                                        |                |
| **Parameters**                                                                                                                                | **Description**                                                                                                                                                                                                                                                                                        | **Default**    |
| Enable                                                                                                                                        | Enable Cellular dial-up.                                                                                                                                                                                                                                                                               | Enable         |
| Time Schedule                                                                                                                                 | Set time schedule                                                                                                                                                                                                                                                                                      | ALL            |
| Force Reboot                                                                                                                                  | Router will reboot if it cannot dial up for a long time and reaches the max retry time                                                                                                                                                                                                                 | Enable         |
| Shared connection (NAT)                                                                                                                       | Enable — Local device connected to Router can access the Internet via Router; Disable — Local device connected to Router cannot access the Internet via Router.                                                                                                                                        | Enable         |
| Default Route                                                                                                                                 | Enable default route                                                                                                                                                                                                                                                                                   | Enable         |
| SIM Network Provider                                                                                                                          | Select network provider for inserted SIM card                                                                                                                                                                                                                                                          | Profile 1      |
| Network Select Type                                                                                                                           | Select network type; router will try 4G, 3G, 2G in proper order if Auto is selected                                                                                                                                                                                                                    | Auto           |
| Connection Mode                                                                                                                               | Optional: Always Online, Connect On Demand, Manual. It will support configuring Triggered by SMS if Connect On Demand mode is selected.                                                                                                                                                                | Always Online  |
| Redial Interval                                                                                                                               | Set the redialing time when dial-up fails.                                                                                                                                                                                                                                                             | 30 s           |
| **Show Advanced Options**                                                                                                                     |                                                                                                                                                                                                                                                                                                        |                |
| Dual SIM Enable                                                                                                                               | Some CR202-Lite types support eSIM; enable this option to enable eSIM dial-up                                                                                                                                                                                                                          | Disable        |
| eSIM Network Provider                                                                                                                         | Select network provider for eSIM card                                                                                                                                                                                                                                                                  | Profile 1      |
| eSIM Blinding ICCID                                                                                                                           | Set ICCID of eSIM                                                                                                                                                                                                                                                                                      | N/A            |
| eSIM PIN Code                                                                                                                                 | For setting eSIM PIN code                                                                                                                                                                                                                                                                              | N/A            |
| eSIM SIM Card Operator                                                                                                                        | Set the ISP that eSIM card connects to                                                                                                                                                                                                                                                                 | Auto           |
| Main SIM                                                                                                                                      | Set the SIM card that is used to dial up first                                                                                                                                                                                                                                                         | SIM            |
| Max Number of Dial                                                                                                                            | Set max number of dial attempts; if dial-up is not successful after this number, the router will switch SIM cards                                                                                                                                                                                      | 5              |
| CSQ Threshold                                                                                                                                 | Set threshold of signal; if current signal level is lower than this, the router will switch SIM cards                                                                                                                                                                                                  | 0 (Disable)    |
| Min Connect Time                                                                                                                              | Set the minimum connect time for each dial-up attempt                                                                                                                                                                                                                                                  | 0 (Disable)    |
| Initial Commands                                                                                                                              | Set customized initial AT commands which will be operated at the beginning of dialing up                                                                                                                                                                                                               | AT             |
| Blinding ICCID                                                                                                                                | Set ICCID of SIM                                                                                                                                                                                                                                                                                       | N/A            |
| PIN Code                                                                                                                                      | For setting PIN code of SIM                                                                                                                                                                                                                                                                            | N/A            |
| Static MTU                                                                                                                                    | Set max transmission unit after enable                                                                                                                                                                                                                                                                 | Disable        |
| Use Peer DNS                                                                                                                                  | Click to receive peer DNS assigned by the ISP                                                                                                                                                                                                                                                          | Enable         |
| Link detection interval                                                                                                                       | Set link detection interval                                                                                                                                                                                                                                                                            | 55 s           |
| Debug                                                                                                                                         | Enable debug mode; print debug log in system log                                                                                                                                                                                                                                                       | Disable        |
| ICMP Detection Mode                                                                                                                           | Set ICMP detection mode; router will check the link connection status via ICMP packet. Ignore Traffic: Router will send ICMP packet regardless of whether there is traffic in the cellular interface. Monitor Traffic: Router will not send ICMP packet if there is traffic in the cellular interface. | Ignore Traffic |
| ICMP Detection Server                                                                                                                         | Set the ICMP Detection Server. N/A represents not enabling ICMP detection.                                                                                                                                                                                                                             | N/A            |
| ICMP Detection Interval                                                                                                                       | Set ICMP Detection Interval                                                                                                                                                                                                                                                                            | 30 s           |
| ICMP Detection Timeout                                                                                                                        | Set ICMP Detection Timeout (the link will be regarded as down if ICMP times out)                                                                                                                                                                                                                       | 20 s           |
| ICMP Detection Retries                                                                                                                        | Set the max. number of retries if ICMP fails (router will redial if reaching max. times)                                                                                                                                                                                                               | 5              |


Table 4-2-1-2 Parameters of Cellular - Schedule


| **Administration of Cellular - Schedule**                            |                         |             |
| -------------------------------------------------------------------- | ----------------------- | ----------- |
| Function description: Online or offline based on the specified time. |                         |             |
| **Parameters**                                                       | **Description**         | **Default** |
| Name                                                                 | Name of Schedule        | Schedule_1  |
| Sunday ~ Saturday                                                    | Click to enable         |             |
| Time Range 1                                                         | Set time range 1        | 9:00-12:00  |
| Time Range 2                                                         | Set time range 2        | 14:00-18:00 |
| Time Range 3                                                         | Set time range 3        | 0:00-0:00   |
| Description                                                          | Set description content | N/A         |


#### 4.2.2 WAN/LAN Switch

Click [Network] → [WAN/LAN Switch] to set the WAN/LAN1 port.

When this port is configured as WAN, CR202-Lite supports three types of wired access: static IP, dynamic address (DHCP), and ADSL (PPPoE) dialing. When this port is configured as LAN, click the **Settings** button to jump to the LAN configuration page.

DHCP adopts Client/Server communication mode. The Client sends a configuration request to the Server, which feeds back corresponding configuration information, including the distributed IP address, to achieve the dynamic configuration of IP address and other information.

PPPoE is a point-to-point protocol over Ethernet. The user has to install a PPPoE Client on the basis of the original connection way. Through PPPoE, remote access devices can achieve the control and charging of each accessed user.

WAN/LAN1 is working as LAN by default.

Table 4-2-2-1 Static IP Parameters of WAN


| **WAN - Static IP**                                                      |                                                                                                                                                                 |                      |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Function description: Access the Internet via wired lines with fixed IP. |                                                                                                                                                                 |                      |
| **Parameters**                                                           | **Description**                                                                                                                                                 | **Default**          |
| Shared connection (NAT)                                                  | Enable — Local device connected to Router can access the Internet via Router; Disable — Local device connected to Router cannot access the Internet via Router. | Enable               |
| Default route                                                            | Enable default route                                                                                                                                            | Enable               |
| MAC Address                                                              | MAC Address of the device                                                                                                                                       | Device's MAC address |
| IP Address                                                               | Set IP address of WAN                                                                                                                                           | 192.168.1.29         |
| Netmask                                                                  | Set subnet mask of WAN                                                                                                                                          | 255.255.255.0        |
| Gateway                                                                  | Set gateway of WAN                                                                                                                                              | 192.168.1.1          |
| MTU                                                                      | Max. transmission unit, default/manual settings                                                                                                                 | default (1500)       |
| **Multiple IP support (at most 8 additional IP addresses can be set)**   |                                                                                                                                                                 |                      |
| IP Address                                                               | Set additional IP address of LAN                                                                                                                                | N/A                  |
| Subnet mask                                                              | Set subnet mask                                                                                                                                                 | N/A                  |
| Description                                                              | For recording significance of additional IP address                                                                                                             | N/A                  |


Table 4-2-2-2 Dynamic Address (DHCP) Parameters of WAN


| **WAN - Dynamic Address (DHCP)**                                                                        |                                                                                                                                                                 |                      |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Function description: Set WAN in DHCP mode to get the address allocated by other routers automatically. |                                                                                                                                                                 |                      |
| **Parameters**                                                                                          | **Description**                                                                                                                                                 | **Default**          |
| Shared connection (NAT)                                                                                 | Enable — Local device connected to Router can access the Internet via Router; Disable — Local device connected to Router cannot access the Internet via Router. | Enable               |
| Default route                                                                                           | Enable default route                                                                                                                                            | Enable               |
| MAC Address                                                                                             | MAC Address of the device                                                                                                                                       | Device's MAC address |
| MTU                                                                                                     | Max. transmission unit, default/manual settings                                                                                                                 | default (1500)       |


Table 4-2-2-3 ADSL Dialing (PPPoE) Parameters of WAN


| **WAN - ADSL Dialing (PPPoE)**                     |                                                                                                                                                                 |                      |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Function description: Set ADSL dialing parameters. |                                                                                                                                                                 |                      |
| **Parameters**                                     | **Description**                                                                                                                                                 | **Default**          |
| Shared connection                                  | Enable — Local device connected to Router can access the Internet via Router; Disable — Local device connected to Router cannot access the Internet via Router. | Enable               |
| Default route                                      | Enable default route                                                                                                                                            | Enable               |
| MAC Address                                        | MAC Address of the device                                                                                                                                       | Device's MAC address |
| MTU                                                | Max. transmission unit, default/manual settings                                                                                                                 | default (1492)       |
| **WAN - ADSL Dialing (PPPoE)**                     |                                                                                                                                                                 |                      |
| Username                                           | Set name of dialing user                                                                                                                                        | N/A                  |
| Password                                           | Set dialing password                                                                                                                                            | N/A                  |
| Static IP                                          | Click to enable and configure static IP                                                                                                                         | Disable              |
| Connection Mode                                    | Set dialing connection method (always online, dial on demand, manual dialing)                                                                                   | Always online        |
| **Parameters of Advanced Options**                 |                                                                                                                                                                 |                      |
| Service Name                                       | Set service name                                                                                                                                                | N/A                  |
| TX Queue Length                                    | Set length of transmit queue.                                                                                                                                   | 3                    |
| Enable IP header compression                       | Click to enable IP header compression                                                                                                                           | Disable              |
| Use Peer DNS                                       | Click to enable use peer DNS                                                                                                                                    | Enable               |
| Link detection interval                            | Set link detection interval                                                                                                                                     | 55 s                 |
| Link detection Max. Retries                        | Set link detection max. retries                                                                                                                                 | 10                   |
| Debug                                              | Click to enable debug mode                                                                                                                                      | Disable              |
| Expert Option                                      | Set expert options                                                                                                                                              | N/A                  |
| ICMP Detection Server                              | Set ICMP detection server; blank means disable ICMP detection feature                                                                                           | N/A                  |
| ICMP Detection Interval                            | Set ICMP Detection Interval                                                                                                                                     | 30 s                 |
| ICMP Detection Timeout                             | Set ICMP detection timeout                                                                                                                                      | 20 s                 |
| ICMP Detection Retries                             | Set ICMP detection max. retries                                                                                                                                 | 3                    |


#### 4.2.3 LAN

Click [Network] → [LAN] to configure the LAN interface of the router so that other devices can access the Internet via Ethernet cable in LAN.

Table 4-2-3 LAN Parameters


| **LAN – Static IP**                                                       |                                                             |                          |
| ------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------ |
| Function description: Devices in LAN use static IP to connect to network. |                                                             |                          |
| **Parameters**                                                            | **Description**                                             | **Default**              |
| MAC Address                                                               | MAC Address of router's LAN gateway                         | Router's LAN MAC address |
| IP Address                                                                | IP Address of router's LAN gateway                          | 192.168.2.1              |
| Netmask                                                                   | Subnet mask of LAN gateway                                  | 255.255.255.0            |
| MTU                                                                       | Max. transmission unit, default/manual settings             | default (1500)           |
| LAN Mode                                                                  | Set transport mode in LAN interface                         | Auto Negotiation         |
| **Multi-IP Settings (at most 8 additional IP addresses can be set)**      |                                                             |                          |
| IP Address                                                                | Set additional IP address of LAN                            | N/A                      |
| Subnet mask                                                               | Set subnet mask                                             | N/A                      |
| Description                                                               | For recording significance of additional IP address         | N/A                      |
| **LAN Port Enable**                                                       |                                                             |                          |
| port1/port2                                                               | Enable corresponding LAN port                               | Enable                   |
| **GARP**                                                                  |                                                             |                          |
| Enable                                                                    | Router will send ARP broadcast to LAN devices automatically | Disable                  |
| Broadcast Count                                                           | Set ARP broadcast times                                     | 5                        |
| Broadcast Timeout                                                         | Set ARP broadcast timeout time                              | 10                       |


#### 4.2.4 Switch WLAN Mode

CR202-Lite supports two types of WLAN mode: AP and STA.

Click [Network] → [Switch WLAN Mode] in the navigation tree to set the WLAN mode of the router. After changing and saving the configuration, reboot the device to make the configuration take effect.

#### 4.2.5 WLAN Client (AP Mode)

When working in AP mode, the CR202-Lite WLAN will provide a network access point for other wireless network devices. Ensure that CR202-Lite has already connected to the Internet via WAN or cellular.

Click [Network] → [WLAN] in the navigation tree to enter the "WLAN" interface.

Table 4-2-5 Parameters of WLAN Access Port


| WLAN                                                                                                                               |                                                                                                               |                              |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| Function description: Support Wi-Fi function and provide wireless LAN access on site and identity authentication of wireless user. |                                                                                                               |                              |
| **Parameters**                                                                                                                     | **Description**                                                                                               | **Default**                  |
| SSID broadcast                                                                                                                     | After turning on, users can search the WLAN via SSID name                                                     | Enable                       |
| Mode                                                                                                                               | Six types for options: 802.11g/n, 802.11g, 802.11n, 802.11b, 802.11b/g, 802.11b/g/n                           | 802.11b/g/n                  |
| Channel                                                                                                                            | Select the channel                                                                                            | 11                           |
| SSID                                                                                                                               | SSID name defined by user                                                                                     | Refer to equipment nameplate |
| Authentication method                                                                                                              | Support open type, shared type, auto selection of WEP, WPA-PSK, WPA, WPA2-PSK, WPA2, WPA/WPA2, WPAPSK/WPA2PSK | Refer to equipment nameplate |
| Encryption                                                                                                                         | Support NONE, WEP                                                                                             | NONE                         |
| Wireless bandwidth                                                                                                                 | Both 20MHz and 40MHz for selection                                                                            | 20MHz                        |
| Enable WDS                                                                                                                         | Click to enable WDS                                                                                           | Disable                      |
| Default Route                                                                                                                      | Click to enable Route                                                                                         | Disable                      |
| Bridged SSID                                                                                                                       | Set bridged SSID                                                                                              | None                         |
| Bridged BSSID                                                                                                                      | Set bridged BSSID                                                                                             | None                         |
| Scan                                                                                                                               | Click "Scan" to scan available APs nearby                                                                     |                              |
| Auth Mode                                                                                                                          | Open type, shared type, WPA-PSK, WPA2-PSK                                                                     | Refer to equipment nameplate |
| Encryption Method                                                                                                                  | Support NONE, WEP                                                                                             | None                         |


#### 4.2.6 WLAN Client (STA Mode)

When working in STA mode, the router can access the Internet by connecting to other APs.

Click [Network] → [WLAN Client] in the navigation tree to enter the "WLAN" interface. Select "Client" for the interface type and configure relevant parameters. (At this moment, the cellular interface in [Network] → [Cellular] should be closed.)

The SSID scan function is enabled only when "Client" is selected as the WLAN interface. Click the **Scan** button to get all available APs and their status, select an AP, and configure the corresponding parameters to connect. After configuring the WLAN Client, configure the access type in [Network] → [WAN(STA)].

Table 4-2-6 Parameters of WLAN Client


| **WLAN Client**                                                                    |                                                       |             |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------- | ----------- |
| Function description: Support Wi-Fi function and access to wireless LAN as client. |                                                       |             |
| **Parameters**                                                                     | **Description**                                       | **Default** |
| Mode                                                                               | Support many modes including 802.11b/g/n              | 802.11b/g/n |
| SSID                                                                               | Name of the SSID to be connected                      | inhand      |
| Authentication method                                                              | Keep consistent with the access point to be connected | Open type   |
| Encryption                                                                         | Keep consistent with the access point to be connected | NONE        |


#### 4.2.7 Link Backup

Click [Network] → [Link Backup] in the navigation tree to enter the configuration interface.

Table 4-2-7-1 Parameters of Link Backup


| **Link Backup**                                                                                                                                                                                                                  |                                                        |              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------ |
| Function description: When the system runs, the main link will first be enabled for communication. However, when the main link is disconnected, the system will automatically switch to the backup link to ensure communication. |                                                        |              |
| **Parameters**                                                                                                                                                                                                                   | **Description**                                        | **Default**  |
| Enable                                                                                                                                                                                                                           | Click to enable link backup                            | Disable      |
| Backup mode                                                                                                                                                                                                                      | Optional: hot failover, cold failover, or load balance | Hot failover |
| Main Link                                                                                                                                                                                                                        | Optional: WAN or dialing interface                     | WAN          |
| ICMP Detection Server                                                                                                                                                                                                            | Set ICMP detection server                              | N/A          |
| Backup Link                                                                                                                                                                                                                      | Optional: cellular or WAN                              | Cellular 1   |
| ICMP Detection Interval                                                                                                                                                                                                          | Set ICMP Detection Interval                            | 10 s         |
| ICMP Detection Timeout                                                                                                                                                                                                           | Set ICMP detection timeout                             | 3 s          |
| ICMP Detection Retries                                                                                                                                                                                                           | Set ICMP detection max. retries                        | 3            |
| Restart Interface When ICMP Failed                                                                                                                                                                                               | Restart main link when ICMP failed                     | Disable      |


Table 4-2-7-2 Parameters of Link Backup - Backup Mode


| **Link Backup - Backup Mode**                        |                                                                                       |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Function description: Select the way of link backup. |                                                                                       |
| **Parameters**                                       | **Description**                                                                       |
| Hot failover                                         | Main link and backup link keep online at the same time; switch if current link is off |
| Cold failover                                        | Backup line will only be online when the main link is disconnected.                   |
| Load balance                                         | Transfer data via corresponding route after ICMP detect succeed                       |


#### 4.2.8 IP Passthrough

IP passthrough function distributes the address obtained by the WAN port to the LAN port device. When external access to the router downstream devices is required, the router transmits data to the downstream device. Click [Network] → [IP Passthrough], then enter the "IP Passthrough" page.

Table 4-2-8 IP Passthrough Parameters


| **IP Passthrough**                                                                                                     |                                                    |                   |
| ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ----------------- |
| Function description: LAN port device obtains WAN port address; used for external access to router downstream devices. |                                                    |                   |
| **Parameters**                                                                                                         | **Description**                                    | **Default**       |
| IP Passthrough                                                                                                         | Enable IP Passthrough                              | Disable           |
| IP Passthrough Mode                                                                                                    | Select work mode (DHCP Dynamic / DHCP fix MAC)     | DHCP Dynamic      |
| Fix MAC Address                                                                                                        | Set fix MAC address if in DHCP fix MAC mode        | 00:00:00:00:00:00 |
| DHCP lease                                                                                                             | Set DHCP lease time and reacquire after expiration | 2 Minutes         |


#### 4.2.9 Static Route

Static routes need to be set manually, after which packets will be transferred to the appointed routes.

To set a static route, click [Network] → [Static Route] in the navigation tree, then enter the "Static Route" interface.

Table 4-2-9 Static Route Parameters


| **Static Route**                                                                                                      |                                                                                        |               |
| --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------- |
| Function description: Add/delete additional static route of router. Generally, it is unnecessary for users to set it. |                                                                                        |               |
| **Parameters**                                                                                                        | **Description**                                                                        | **Default**   |
| Destination Address                                                                                                   | Set IP address of the destination                                                      | 0.0.0.0       |
| Netmask                                                                                                               | Set subnet mask of the destination                                                     | 255.255.255.0 |
| Gateway                                                                                                               | Set the gateway of the destination                                                     | N/A           |
| Interface                                                                                                             | Select WAN/CELLULAR 1/LAN/WAN(STA) of the destination                                  | N/A           |
| Description                                                                                                           | For recording significance of static route address (not supporting Chinese characters) | N/A           |


### 4.3 Services

#### 4.3.1 DHCP Service

DHCP adopts Client/Server communication mode. The Client sends a configuration request to the Server, which feeds back corresponding configuration information, including the distributed IP address, to achieve the dynamic configuration of IP address and other information.

- The duty of the DHCP Server is to distribute an IP address when a workstation logs on and ensure each workstation is supplied with a different IP address. The DHCP Server has simplified some network management tasks requiring manual operations to the largest extent.
- As a DHCP Client, the device receives the IP address distributed by the DHCP server after logging in to the DHCP server, so the Ethernet interface of the device needs to be configured into an automatic mode.

To enable the DHCP service, select [Services] → [DHCP Service] in the navigation tree, then enter the "DHCP Service" page.

Table 4-3-1 Parameters of DHCP Service


| **DHCP Service**                                                                                                                                                                                                                                 |                                                                                           |               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | ------------- |
| Function description: If the host connected with the router chooses to obtain an IP address automatically, then such service must be activated. Static designation of DHCP allocation could help certain hosts to obtain a specified IP address. |                                                                                           |               |
| **Parameters**                                                                                                                                                                                                                                   | **Description**                                                                           | **Default**   |
| Enable DHCP                                                                                                                                                                                                                                      | Enable DHCP service and dynamically allocate IP address                                   | Enable        |
| IP Pool Starting Address                                                                                                                                                                                                                         | Set starting IP address of dynamic allocation                                             | 192.168.2.2   |
| IP Pool Ending Address                                                                                                                                                                                                                           | Set ending IP address of dynamic allocation                                               | 192.168.2.100 |
| Lease                                                                                                                                                                                                                                            | Set lease of IP allocated dynamically                                                     | 60 minutes    |
| DNS                                                                                                                                                                                                                                              | Set DNS Server                                                                            | 192.168.2.1   |
| Windows Name Server                                                                                                                                                                                                                              | Set Windows name server.                                                                  | N/A           |
| **Static designation of DHCP allocation (at most 20 DHCPs designated statically can be set)**                                                                                                                                                    |                                                                                           |               |
| MAC Address                                                                                                                                                                                                                                      | Set a statically specified DHCP MAC address (different from other MACs to avoid conflict) | N/A           |
| IP Address                                                                                                                                                                                                                                       | Set a statically specified IP address                                                     | 192.168.2.2   |
| Host                                                                                                                                                                                                                                             | Set the hostname.                                                                         | N/A           |


#### 4.3.2 DNS

DNS (Domain Name System) is a distributed database used in TCP/IP application programs, providing switch between domain name and IP address. Through DNS, users can directly use meaningful domain names which can be easily memorized, and the DNS Server in the network can resolve the domain name into the correct IP address. Manually set the DNS; use DNS via dialing if it is empty. Generally, it needs to be set only when a static IP is used on the WAN port.

Click [Service] → [Domain Name Service] in the navigation tree to enter the "Domain Name Service" interface.

Table 4-3-2 DNS Parameters


| **DNS (DNS Settings)**                             |                                          |             |
| -------------------------------------------------- | ---------------------------------------- | ----------- |
| Function description: Configure parameters of DNS. |                                          |             |
| **Parameters**                                     | **Description**                          | **Default** |
| Primary DNS                                        | Set Primary DNS                          | 0.0.0.0     |
| Secondary DNS                                      | Set Secondary DNS                        | 0.0.0.0     |
| Disable local DNS server                           | Not to transfer local DNS server address | Disable     |


#### 4.3.3 DNS Relay

CR202-Lite works as a DNS Agent and relays DNS request and response messages between DNS Client and DNS Server to carry out domain name resolution in lieu of DNS Client.

From the navigation tree, select [Service] → [DNS Relay], then enter the "DNS Relay" page.

Table 4-3-3 DNS Relay Parameters


| **DNS Relay service**                                                                                                                           |                                                          |                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------- |
| Function description: If the host connected with the router chooses to obtain a DNS address automatically, then such service must be activated. |                                                          |                                                            |
| **Parameters**                                                                                                                                  | **Description**                                          | **Default**                                                |
| Enable DNS Relay service                                                                                                                        | Click to enable DNS service                              | Enable (DNS will be enabled when DHCP service is enabled.) |
| **Designate [IP address <=> domain name] pair (20 IP address <=> domain name pairs can be designated)**                                         |                                                          |                                                            |
| IP Address                                                                                                                                      | Set IP address of designated IP address <=> domain name  | N/A                                                        |
| Host                                                                                                                                            | Domain Name                                              | N/A                                                        |
| Description                                                                                                                                     | For recording significance of IP address <=> domain name | N/A                                                        |


icon When enabling DHCP, the DHCP relay is also enabled automatically. Relay cannot be disabled without disabling DHCP.

#### 4.3.4 Device Manager

CR202-Lite supports connecting to InHand Device Manager for remotely managing InHand products. Customers can manage and operate routers, check status, and upgrade software in batch via this platform.

Click [Service] → [Device Manager] in the navigation tree to enter the "Device Manager" interface.

Table 4-3-4 Device Manager Parameters


| **Device Manager**                                                            |                                                                                           |                        |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ---------------------- |
| Function description: Connect the router to the platform for cloud management |                                                                                           |                        |
| **Parameters**                                                                | **Description**                                                                           | **Default**            |
| Enable                                                                        | Enable Device Manager                                                                     | Disable                |
| Service Type                                                                  | Platform work mode: Device Manager or Custom                                              | Device Manager         |
| Server                                                                        | Select cloud platform address: iot.inhand.com.cn (China), iot.inhandnetworks.com (global) | iot.inhandnetworks.com |
| Secure Channel                                                                | Use encryption protocol for secure data transmission between router and platform          | Enable                 |
| Registered Account                                                            | Account registered in Device Manager                                                      | N/A                    |
| LBS info Upload Interval                                                      | Cellular information upload interval                                                      | 1 Hour                 |
| Series Info Upload Interval                                                   | Traffic information upload interval                                                       | 1 Hour                 |
| Channel Keepalive                                                             | Keep alive packet interval                                                                | 30 Seconds             |


#### 4.3.5 SMS

SMS permits message-based reboot and manual dialing. Configure "Permit to Phone Number" and click **Apply and Save**. After that, send a "reboot" command to restart the device, or send a custom connection or disconnection command to redial or disconnect the device.

From the navigation tree, select [Service] → [SMS], then enter the "SMS" page.

Table 4-3-5 SMS Parameters


| **Short message**                                                                     |                                                                                       |             |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ----------- |
| Function description: Configure SMS function to manage the router in the form of SMS. |                                                                                       |             |
| **Parameters**                                                                        | **Description**                                                                       | **Default** |
| Enable                                                                                | Click to enable SMS function                                                          | Disable     |
| Status Query                                                                          | Define the English query instruction to inquire current working status of the router. | N/A         |
| Reboot                                                                                | Define the English query instruction to reboot the router.                            | N/A         |
| **SMS Access Control**                                                                |                                                                                       |             |
| Default Policy                                                                        | Select the manner of access processing.                                               | Accept      |
| Phone Number                                                                          | Fill in mobile number                                                                 | N/A         |
| Action                                                                                | Accept or block                                                                       | Accept      |
| Description                                                                           | Describe SMS control.                                                                 |             |


#### 4.3.6 Traffic Manager

This function is mainly used to count data traffic in the cellular interface. If the threshold is 0, the router will only count and the rules will not take effect. This function requires enabling the NTP function.

Choose [Services] → [Traffic Manager] to go to the "Traffic Manager" page.

Table 4-3-6 Traffic Manager Parameters


| **Traffic Manager**                                         |                                                                                                                                                                                       |                |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Function: Monitor and manage the traffic use of the router. |                                                                                                                                                                                       |                |
| **Parameters**                                              | **Description**                                                                                                                                                                       | **Default**    |
| Enable                                                      | Click to enable the traffic manager function.                                                                                                                                         | Disable        |
| Start Day                                                   | The day to start counting data traffic every month                                                                                                                                    | 1              |
| Monthly Threshold                                           | Data traffic threshold every month                                                                                                                                                    | 0MB            |
| When Over Monthly Threshold                                 | Operation when data traffic used within a month reaches the threshold: Only Reporting, Block Except Management (will not influence DM and management requirement), Shutdown Interface | Only Reporting |
| Last 24-Hours Threshold                                     | Data traffic threshold in last 24 Hours                                                                                                                                               | 0KB            |
| When Over 24-Hours Threshold                                | Operation when data traffic used within 24 hours reaches the threshold                                                                                                                | Only Reporting |
| Advance                                                     | Custom statistics and operations for the last several hours                                                                                                                           | Disable        |


#### 4.3.7 Alarm Settings

When an abnormality occurs, the router will report alarms according to the settings. Currently the router supports sending alarms in the following situations: System Service Fault, Memory Low, WAN/LAN1 Link-Up/Down, LAN2 Link-Up/Down, Cellular Up/Down, Traffic Alarm, Traffic Disconnect Alarm, SIM/UIM Card Switch, Active Link Switch, SIM/UIM Card Fault, Signal Quality Fault.

In the Alarm Manager interface, the following operations can be performed:

- Select alarm types in the "Alarm Input" area.
- Set the alarm notification method of the console in the "Alarm Output" area.

Choose [Services] → [Alarm Manager] to go to the "Alarm Manager" page.

#### 4.3.8 User Experience Plan

InHand Networks' User Experience Program is designed to improve product user experience and customer service quality.

Users can disable or enable the User Experience Plan in [Services] → [User Experience Plan].

### 4.4 Firewall

The firewall function of the router implements corresponding control to data flow at the entry direction (from Internet to LAN) and exit direction (from LAN to Internet) according to the content features of messages (such as protocol style, source/destination IP address, etc.) and ensures safe operation of the router and hosts in the local area network.

#### 4.4.1 Basic

From the navigation tree, select [Firewall] → [Basic], then enter the basic setup page.

Table 4-4-1 Firewall - Basic Parameters


| **Basic Setup of Firewall**                     |                                                            |             |
| ----------------------------------------------- | ---------------------------------------------------------- | ----------- |
| Function description: Set basic firewall rules. |                                                            |             |
| **Parameters**                                  | **Description**                                            | **Default** |
| Default Filter Policy                           | Select accept/block                                        | Accept      |
| Block Anonymous WAN Requests (ping)             | Select to filter WAN detection packets like PING detection | Disable     |
| Filter Multicast                                | Select to filter multicast function                        | Enable      |
| Defend DoS Attack                               | Select to defend DoS attack                                | Enable      |
| SIP ALG                                         | Select to enable SIP ALG                                   | Disable     |


#### 4.4.2 Filtering

Filter network data by customizing rules to allow or prohibit the specified data flow forwarded by the router.

To enable Access Control, select [Firewall] → [Filtering] from the navigation tree, then enter the "Filtering" page.

Table 4-4-2 Filtering Parameters


| **Filtering**                                                                                                                                                                 |                                                                                      |               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------- |
| Function description: Control the protocol, source/destination address, and source/destination port passing through network packets of the router to provide a safe intranet. |                                                                                      |               |
| **Parameters**                                                                                                                                                                | **Description**                                                                      | **Default**   |
| Enable                                                                                                                                                                        | Check to enable filtering.                                                           | Enable        |
| Protocol                                                                                                                                                                      | Select ALL/TCP/UDP/ICMP                                                              | ALL           |
| Source                                                                                                                                                                        | Set source address of access control                                                 | 0.0.0.0/0     |
| Source Port                                                                                                                                                                   | Set source port of access control                                                    | Not available |
| Destination                                                                                                                                                                   | Set destination address                                                              | N/A           |
| Destination Port                                                                                                                                                              | Set destination port of access control                                               | Not available |
| Action                                                                                                                                                                        | Select Accept/Block                                                                  | Accept        |
| Log                                                                                                                                                                           | Click to enable log and the log about access control will be recorded in the system. | Disable       |
| Description                                                                                                                                                                   | Convenient for recording parameters of access control                                | N/A           |


#### 4.4.3 Device Access Filtering

Set customized rules to allow or prohibit data access to the router.

From the navigation tree, select [Firewall] → [Device Access Filtering], then enter the "Device Access Filtering" page.

Table 4-4-3 Device Access Filtering Parameters


| **Device Access Filtering**                                                                                        |                                                                                      |               |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------- |
| Function description: Control the protocol, source/destination address, and source/destination port to the router. |                                                                                      |               |
| **Parameters**                                                                                                     | **Description**                                                                      | **Default**   |
| Enable                                                                                                             | Check to enable device access filtering.                                             | Enable        |
| Protocol                                                                                                           | Select ALL/TCP/UDP/ICMP                                                              | ALL           |
| Source                                                                                                             | Set source address of network access                                                 | 0.0.0.0/0     |
| Source Port                                                                                                        | Set source port of network access                                                    | Not available |
| Destination                                                                                                        | Set destination address                                                              | N/A           |
| Destination Port                                                                                                   | Set destination port of network access                                               | Not available |
| Interface                                                                                                          | Set interface of network access                                                      | All WANs      |
| Action                                                                                                             | Select Accept/Block                                                                  | Accept        |
| Log                                                                                                                | Click to enable log and the log about access control will be recorded in the system. | Disable       |
| Description                                                                                                        | Convenient for recording parameters of access control                                | N/A           |


#### 4.4.4 Content Filtering

Set rules to disable access to specific URLs.

From the navigation tree, select [Firewall] → [Content Filtering], then enter the "Content Filtering" page.

Table 4-4-4 Content Filtering Parameters


| **Content Filtering**                                                                           |                                                                                |             |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------- |
| Function description: Set firewall rules related to filtering and generally set forbidden URLs. |                                                                                |             |
| **Parameters**                                                                                  | **Description**                                                                | **Default** |
| Enable                                                                                          | Click to enable filtering                                                      | Enable      |
| URL                                                                                             | Set URL that needs to be filtered                                              | N/A         |
| Action                                                                                          | Select accept/block                                                            | Accept      |
| Log                                                                                             | Click to write log and the log about filtering will be recorded in the system. | Disable     |
| Description                                                                                     | Record the meanings of various parameters of filtering                         | N/A         |


#### 4.4.5 Port Mapping

Port mapping is also called virtual server. Setting port mapping can enable hosts on the extranet to access a specific port of a host corresponding to an IP address on the intranet.

To configure port mapping, select [Firewall] → [Port Mapping] from the navigation tree, then enter the "Port Mapping" page.

Table 4-4-5 Firewall - Port Mapping Parameters


| **Port Mapping (at most 100 port mappings can be set)**     |                                                                                    |             |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------- |
| Function description: Configure parameters of port mapping. |                                                                                    |             |
| **Parameters**                                              | **Description**                                                                    | **Default** |
| Enable                                                      | Check to enable port mapping.                                                      | Enable      |
| Proto                                                       | Select TCP/UDP/TCP&UDP                                                             | TCP         |
| Source                                                      | Set source address of port mapping                                                 | 0.0.0.0/0   |
| Service Port                                                | Set service port number of port mapping                                            | 8080        |
| Internal Address                                            | Set internal address of port mapping                                               | N/A         |
| Internal Port                                               | Set internal port of port mapping                                                  | 8080        |
| Log                                                         | Click to enable log and the log about port mapping will be recorded in the system. | Disable     |
| External Interface (optional)                               | Set external interface of port mapping                                             | N/A         |
| External Address (optional)                                 | Set external address/tunnel name of port mapping                                   | N/A         |
| Description                                                 | For recording significance of each port mapping rule                               | N/A         |


#### 4.4.6 Virtual IP Mapping

Both the router and the IP address of the host on the intranet can correspond with one virtual IP. Without changing the IP allocation of the intranet, the extranet can access the host on the intranet via the virtual IP. This function is always used with VPN.

To configure virtual IP mapping, select [Firewall] → [Virtual IP Mapping] from the navigation tree.

Table 4-4-6 Firewall - Virtual IP Mapping Parameters


| **Virtual IP Address**                                            |                                                                                          |             |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------- |
| Function description: Configure parameters of virtual IP address. |                                                                                          |             |
| **Parameters**                                                    | **Description**                                                                          | **Default** |
| Virtual IP address of router                                      | Set virtual IP address of router                                                         | N/A         |
| Range of source address                                           | Set range of the external source IP addresses.                                           | N/A         |
| Enable                                                            | Click to enable virtual IP address                                                       | Enable      |
| Virtual IP                                                        | Set virtual IP address of virtual IP mapping                                             | N/A         |
| Real IP                                                           | Set real IP address of virtual IP mapping                                                | N/A         |
| Log                                                               | Click to enable log and the log about virtual IP address will be recorded in the system. | Disable     |
| Description                                                       | For recording significance of each virtual IP address rule                               | N/A         |


#### 4.4.7 DMZ

After mapping all ports, an extranet PC can access all ports of an internal device by DMZ settings.

From the navigation tree, select [Firewall] → [DMZ], then enter the "DMZ" page.

Table 4-4-7 Firewall - DMZ Parameters


| **DMZ**                                       |                                        |             |
| --------------------------------------------- | -------------------------------------- | ----------- |
| Function description: Configure DMZ settings. |                                        |             |
| **Parameters**                                | **Description**                        | **Default** |
| Enable DMZ                                    | Check to enable the DMZ.               | Disable     |
| DMZ Host                                      | Set address of DMZ Host                | N/A         |
| Source Address Range                          | Enter range of external source address | N/A         |
| Interface                                     | Select external interface of DMZ       | N/A         |


#### 4.4.8 MAC-IP Binding

If the default filter policy in the basic setting of the firewall is disabled, only hosts specified in MAC-IP Binding can access the outer network.

From the navigation tree, select [Firewall] → [MAC-IP Binding], then enter the "MAC-IP Binding" page.

Table 4-4-8 Firewall - MAC-IP Binding Parameters


| **MAC-IP Binding (at most 20 MAC-IP Bindings can be set)** |                                                                     |                   |
| ---------------------------------------------------------- | ------------------------------------------------------------------- | ----------------- |
| Function description: Configure MAC-IP parameters.         |                                                                     |                   |
| **Parameters**                                             | **Description**                                                     | **Default**       |
| MAC Address                                                | Set the binding MAC address                                         | 00:00:00:00:00:00 |
| IP Address                                                 | Set the binding IP address                                          | 192.168.2.2       |
| Description                                                | For recording the significance of each MAC-IP binding configuration | N/A               |


#### 4.4.9 NAT

NAT is the network address translation function, including source address translation (SNAT) and destination address translation (DNAT).

SNAT refers to the communication between the internal network and the external network when the destination address remains unchanged. DNAT refers to the translation of the destination address of the internal network into the external network without changing the source address when accessing the internal network.

Table 4-4-9 NAT Parameters


| **NAT**                                           |                                                 |             |
| ------------------------------------------------- | ----------------------------------------------- | ----------- |
| Function description: Configure parameters of NAT |                                                 |             |
| **Parameters**                                    | **Description**                                 | **Default** |
| Enable                                            | Enable NAT                                      | Enable      |
| Type                                              | Set convert type                                | SNAT        |
| Proto                                             | Select protocol                                 | TCP         |
| Source IP                                         | Set source IP of the NAT rule                   | 0.0.0.0/0   |
| Source Port                                       | Set source port of the NAT rule                 | N/A         |
| Destination                                       | Set destination IP of the NAT rule              | 0.0.0.0/0   |
| Destination Port                                  | Set destination port of the NAT rule            | 0.0.0.0/0   |
| Interface                                         | Set interface of the NAT rule                   | N/A         |
| Translated Address                                | Translate the IP address if it matches the rule | 0.0.0.0     |
| Translated Port                                   | Translate the port if it matches the rule       | N/A         |


### 4.5 Tools

#### 4.5.1 PING

Enter the navigation tree, select [Tools] → [Ping].

Table 4-5-1 PING Detection Parameters


| **PING**                                                                                                       |                                          |             |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ----------- |
| Function description: Use ICMP to detect the connection status between the router and the destination address. |                                          |             |
| **Parameters**                                                                                                 | **Description**                          | **Default** |
| Host                                                                                                           | Address of the destination host          | N/A         |
| PING Count                                                                                                     | Set the PING count                       | 4           |
| Packet Size                                                                                                    | Set the size of PING detection           | 32 bytes    |
| Expert Option                                                                                                  | Advanced parameter of PING is available. | N/A         |


#### 4.5.2 Traceroute

To perform traceroute, select [Tools] → [Traceroute] in the navigation tree.

Table 4-5-2 Traceroute Parameters


| **Traceroute**                                                       |                                                                   |             |
| -------------------------------------------------------------------- | ----------------------------------------------------------------- | ----------- |
| Function description: Applied for network routing failure detection. |                                                                   |             |
| **Parameters**                                                       | **Description**                                                   | **Default** |
| Host                                                                 | Address of the destination host which to be detected is required. | N/A         |
| Maximum Hops                                                         | Set the max. hops for traceroute                                  | 20          |
| Timeout                                                              | Set the timeout of traceroute                                     | 3 s         |
| Protocol                                                             | ICMP/UDP                                                          | UDP         |
| Expert Option                                                        | Advanced parameter for traceroute is available.                   | N/A         |


### 4.6 Status

#### 4.6.1 System

From the navigation tree, select [Status] → [System], then enter the "System" page.

This page displays system statistics, including name, model, serial number, description, current version, current Bootloader version, router time, PC time, UP time, CPU load, and memory consumption. Click the **Sync Time** button to synchronize the router with the system time of the host, as covered in the setup chapter.

#### 4.6.2 Power

From the navigation tree, select [Status] → [Power], then enter the "Power" page.

This page displays the power information of version, type, and status, and also displays battery charge status, capacity, and voltage.

#### 4.6.3 Modem

From the navigation tree, select [Status] → [Modem], then enter the "Modem" page.

This page displays the basic information of dial-up, including status, signal level, register status, IMEI (ESN) code, IMSI code, LAC, and cell ID.

#### 4.6.4 Traffic Statistics

Choose [Status] → [Traffic Statistics] to go to the "Traffic Statistics" page to query traffic statistics.

This page displays the traffic statistics on the dialing interface, including the statistics on traffic received in the latest month, traffic transmitted in the latest month, traffic received on the last day, and traffic transmitted on the last day.

#### 4.6.5 Alarm

Choose [Status] → [Alarm] to go to the "Alarm" page to view all alarms generated in the system since power-on. Alarms can be cleared or confirmed.

The alarms have the following states:

- **Raise**: indicates that the alarm has been generated but has not been confirmed.
- **Confirm**: indicates that the alarm cannot be solved currently.
- **All**: indicates all generated alarms.

The alarms are classified into the following levels:

- **EMERG**: The device undergoes a serious error that causes a system reboot.
- **CRIT**: The device undergoes an unrecoverable error.
- **WARN**: The device undergoes an error that affects system functions.
- **NOTICE**: The device undergoes an error that affects system performance.
- **INFO**: A normal event occurs.

#### 4.6.6 WLAN

Choose [Status] → [WLAN] to go to the "WLAN" page to query the WLAN connection status.

This page displays the WLAN connection information, including channel, SSID, BSSID, security, signal (%), mode, and status.

#### 4.6.7 Network Connections

From the navigation tree, select [Status] → [Network Connections], then enter the "Network Connections" page to view the connection status.

This page shows the basic information of dial-up and LAN.

- WAN includes MAC address, connection type, IP address, netmask, gateway, DNS, MTU, status, etc.
- Dial-up includes connection type, IP address, netmask, gateway, DNS, MTU, status, and connection time.
- LAN includes connection type, MAC address, IP address, netmask, gateway, MTU, and DNS.

#### 4.6.8 Device Manager

From the navigation tree, select [Status] → [Device Manager], then enter the "Device Manager" page to check the connection status between the router and Device Manager.

#### 4.6.9 Route Table

From the navigation tree, select [Status] → [Route Table], then enter the "Route Table" page to view router status.

This page displays the active route table, including destination, netmask, gateway, metric, and interface.

#### 4.6.10 Device List

From the navigation tree, select [Status] → [Device List], then enter the "Device List" page to inquire the device list.

This page displays the device list, including interface, MAC address, IP address, host, and lease (click MAC address to link to IEEE to inquire validity of the address).

#### 4.6.11 Log

From the navigation tree, select [Status] → [Log], then enter the "Log" page.

This page displays the logs, including the option to select the number of log lines (20/50/....../all), log level (information, debug, and warning), time, module, and content. Options to clear log, download log file, and download system diagnosis record are available (refresh rate of this page is 5/10/…... 1min by default).

#### 4.6.12 Third Party Software Notices

From the navigation tree, select [Status] → [Third Party Software Notices], then enter the "Third Party Software Notices" page to check the third party software used in the router system.

---

## Appendix Troubleshooting

### 1 Network Connection Issues


| Symptom                                       | Possible Cause                         | Troubleshooting Steps                                                                                                         | Related Chapter                                                  |
| --------------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Cannot access the Internet                    | SIM card not inserted or not activated | 1. Check whether the SIM card is inserted 2. Verify the data service is enabled and the account is active                     | [SIM/UIM Card Installation](#221-simuim-card-installation)       |
| Cannot access the Internet                    | APN or dial-up parameters incorrect    | 1. Verify APN settings match carrier requirements 2. Check dial-up number, username, and password                             | [Cellular Internet Access](#scenario-1-cellular-internet-access) |
| Cannot access the Internet                    | Weak or no signal                      | 1. Check antenna connection 2. Adjust device position                                                                         | [LED Indicators](#14-led-indicators)                             |
| Cannot access the Internet                    | PC IP configuration error              | 1. Confirm the PC is in the same subnet as the router 2. Check the gateway address                                            | [Login Router](#223-pc-network-configuration)                    |
| Frequent auto restart                         | Module, SIM, or power issue            | 1. Check module status 2. Verify SIM card and data service 3. Check signal strength 4. Verify power supply voltage            | [Pre-Installation Preparation](#21-pre-installation-preparation) |
| Dial-up always fails                          | Configuration error or SIM issue       | 1. Restore factory defaults 2. Reconfigure parameters                                                                         | [Restore Factory Settings](#15-restore-factory-settings)         |
| Packet loss when pinging the router           | Network cable issue                    | 1. Check whether the network crossover cable is in good condition                                                             | [Installation Guide](#22-installation-guide)                     |
| Network LED not on when connected to PC       | Cable or port issue                    | 1. Check whether a network crossover cable is used 2. Check cable condition 3. Set the PC network card to 10/100M full duplex | [Installation Guide](#22-installation-guide)                     |
| Network LED normal but cannot ping the router | IP mismatch                            | 1. Check whether the PC IP and router are in the same subnet 2. Verify the gateway address                                    | [Login Router](#223-pc-network-configuration)                    |


### 2 Web Access Issues


| Symptom                                    | Possible Cause          | Troubleshooting Steps                                                                        | Related Chapter                                          |
| ------------------------------------------ | ----------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Cannot open the Web interface              | IP address error        | 1. Confirm the PC is in the same subnet as the router 2. Check the device default IP         | [Login Router](#223-pc-network-configuration)            |
| Cannot open the Web interface              | Browser or plugin issue | 1. Change browser (Chrome recommended) 2. Clear browser cache 3. Disable third-party plugins | [Login Router](#223-pc-network-configuration)            |
| Cannot open the Web interface              | PC firewall blocking    | 1. Check PC firewall settings 2. Ensure the configuration page is not blocked                | [Login Router](#223-pc-network-configuration)            |
| Cannot configure after changing IP address | Forgotten new IP        | 1. Restore factory defaults via the RESET button                                             | [Restore Factory Settings](#15-restore-factory-settings) |


### 3 Device Startup Issues


| Symptom                        | Possible Cause                | Troubleshooting Steps                                                                                | Related Chapter                                                  |
| ------------------------------ | ----------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Power LED not on               | Power supply fault            | 1. Check whether the protective fuse is burned out 2. Verify power supply voltage range and polarity | [Pre-Installation Preparation](#21-pre-installation-preparation) |
| Device does not start normally | System or configuration error | 1. Restore factory defaults 2. Reconfigure parameters                                                | [Restore Factory Settings](#15-restore-factory-settings)         |


### 4 VPN Issues


| Symptom                                                                | Possible Cause             | Troubleshooting Steps                                                                   | Related Chapter                      |
| ---------------------------------------------------------------------- | -------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------ |
| PC under router can connect to server, but center cannot connect to PC | PC firewall blocking       | 1. Disable the PC firewall                                                              | [Firewall](#44-firewall)             |
| PC under router cannot ping VPN server                                 | Shared connection disabled | 1. Ensure "Shared Connection" on [Network] → [WAN] or [Network] → [Cellular] is enabled | [WAN/LAN Switch](#422-wanlan-switch) |


### 5 Firmware Upgrade Issues


| Symptom                       | Possible Cause                   | Troubleshooting Steps                                                    | Related Chapter                                           |
| ----------------------------- | -------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------- |
| Firmware upgrade always fails | Network segment mismatch (local) | 1. Check whether the local PC and router are in the same network segment | [Upgrade](#417-upgrade)                                   |
| Firmware upgrade always fails | No Internet access (remote)      | 1. Ensure the router can access the Internet                             | [Network Connection Issues](#1-network-connection-issues) |


---

## Appendix Safety Precautions

1. Do not use or leave the cell near a heat source such as fire or heater.
2. Do not use or leave the cell under blazing sun (or in a heated car by sunshine).
3. Do not use or leave the battery at very high temperature conditions (for example, strong direct sunlight or a vehicle in extremely hot conditions). Otherwise, it can overheat, catch fire, or its performance will degrade and its service life will decrease.
4. Do not short circuit, over-charge, or over-discharge the cell.
5. Do not immerse the battery in water or seawater. Store it in a cool and dry environment when not in use.
6. Do not reverse the positive and negative terminals.
7. Do not disassemble or modify the cell.
8. Do not transport and store the battery together with metal objects such as necklaces, hairpins, coins, etc.
9. Do not use the cell with conspicuous damage or deformation.
10. Do not connect the cell to an electrical outlet directly.
11. If the cell leaks and the electrolyte gets into the eyes, do not wipe the eyes. Instead, thoroughly rinse the eyes with clean running water for at least 15 minutes, and immediately seek medical attention. Otherwise, eye injury can result.
12. Do not use lithium ion battery and other different lithium battery models in mixture.
13. Keep the battery away from babies.
14. Do not directly solder the battery or pierce the battery with a nail or other sharp object.
15. Do not strike, throw, or trample the battery.
16. Do not bend or fold the sealing edge. Do not open or deform the folding edge. Do not fillet the end of the folding edge.
17. When charging, use the battery charger specifically for that purpose.
18. When disposing of secondary cells, keep cells of different electrochemical systems separate from each other.
19. In case the battery terminals are dirty, clean the terminals with a dry cloth before use. Otherwise, power failure or charge failure may occur due to poor connection with the instrument.
20. If the battery gives off an odor, generates heat, becomes discolored or deformed, or in any way appears abnormal during use, recharging, or storage, immediately remove it from the device or battery charger and stop using it.
21. The battery replacement shall be done only by either the cell supplier or device supplier and never be done by the user.
22. Be aware discharged batteries may cause fire; tape the terminals to insulate them.
23. Do not use it in a location where electrostatic and magnetic fields are strong; otherwise, the safety devices may be damaged, causing hidden safety trouble.
24. Prohibition of use of damaged cells.
25. Battery pack designing and packing must not injure batteries.
26. Do not bend or fold the sealing edge. Do not open or deform the folding edge. Do not fillet or impact the end of the folding edge.
27. Any components contacting these two edges must be insulated.
28. Soft film wrapped Li-polymer is a soft cell wrapped by AL-film; it cannot be contacted by needle, nail, Ni-tab, or the sharp-cut edge of pack material, etc.
29. The ultrasonic joining and spot welding are recommended in assembly of the cell. In other cases, manual solder is recommended: the temperature of the soldering iron can be controlled (≤350℃) and guard against static; soldering tin time ≤3s; soldering tin less than 2 times and the second soldering is permitted after the cell seal side cools.
30. The intensity of the electrode is not high, especially the positive electrode is an Al-Ni tap (Ni-tab). Prohibit bending it repetitiously (intensity of drawing < 0.5kgf).
31. Prohibit soldering on the seal side (position of jointing is more than 2.0mm from glue of electrode). The high temperature of 60℃ will reduce the intensity of seal and result in leak. Prohibit heating the cell directly up to 100℃.

> **Warning**: Non-professionals should not open the device外壳, as there is a risk of electric shock.

---

## Appendix Command Line Reference

### 1 Help Commands


| Command        | Function              | View      | Parameter             | Example            |
| -------------- | --------------------- | --------- | --------------------- | ------------------ |
| `help [<cmd>]` | Get help from command | All views | `<cmd>`: command name | `help` `help show` |


**Example: View all available commands**

```
# help
```

**Example: View show command help**

```
# help show
```

### 2 View Switchover Commands


| Command                    | Function                                                                                 | View                            | Parameter                                                       | Example         |
| -------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------- | --------------------------------------------------------------- | --------------- |
| `enable [15 [<password>]]` | Switch to privileged user level                                                          | Ordinary user view              | `15`: user right limit level; `<password>`: privileged password | `enable 123456` |
| `disable`                  | Exit the privileged user level                                                           | Super user view, configure view | None                                                            | `disable`       |
| `end` or `!`               | Exit the current view and return to the last view                                        | Configure view                  | None                                                            | `end`           |
| `exit`                     | Exit the current view and return to the last view (exit console from ordinary user view) | All views                       | None                                                            | `exit`          |


### 3 Check System State Commands


| Command                | Function                                          | View                                | Parameter                                 | Example               |
| ---------------------- | ------------------------------------------------- | ----------------------------------- | ----------------------------------------- | --------------------- |
| `show version`         | Display the type and version of router software   | All views                           | None                                      | `show version`        |
| `show system`          | Display router system information                 | All views                           | None                                      | `show system`         |
| `show clock`           | Display router system time                        | All views                           | None                                      | `show clock`          |
| `show modem`           | Display MODEM state                               | All views                           | None                                      | `show modem`          |
| `show log [lines <n>]` | Display router system log (latest 100 by default) | All views                           | `lines <n>`: limits log numbers displayed | `show log`            |
| `show users`           | Display router user list                          | All views                           | None                                      | `show users`          |
| `show startup-config`  | Display router startup configuration              | Super user view, configuration view | None                                      | `show startup-config` |
| `show running-config`  | Display router operational configuration          | Super user view, configuration view | None                                      | `show running-config` |


**Example: Display system time**

```
# show clock
Sat Jan 1 00:01:28 UTC 2000
```

**Example: Display user list**

```
# show users
User:
-------------------------------------------------
* adm
------
```

The user marked with `*` is a super user.

### 4 Check Network Status Commands


| Command          | Function                       | View      | Parameter | Example          |
| ---------------- | ------------------------------ | --------- | --------- | ---------------- |
| `show interface` | Display port state information | All views | None      | `show interface` |
| `show ip`        | Display system IP status       | All views | None      | `show ip`        |
| `show route`     | Display routing list           | All views | None      | `show route`     |
| `show arp`       | Display ARP list               | All views | None      | `show arp`       |


### 5 Internet Testing Commands


| Command                                                | Function                              | View      | Parameter                                                                                                           | Example                      |
| ------------------------------------------------------ | ------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| `ping <hostname> [count <n>] [size <n>] [source <ip>]` | Apply ICMP testing to appointed host  | All views | `<hostname>`: address or domain name; `count <n>`: testing times; `size <n>`: packet size; `source <ip>`: source IP | `ping www.example.com`       |
| `telnet <hostname> [<port>] [source <ip>]`             | Telnet login to appointed host        | All views | `<hostname>`: address or domain name; `<port>`: telnet port; `source <ip>`: source IP                               | `telnet 192.168.2.2`         |
| `traceroute <hostname> [maxhops <n>] [timeout <n>]`    | Test acting routing of appointed host | All views | `<hostname>`: address or domain name; `maxhops <n>`: max routing jumps; `timeout <n>`: timeout per jump             | `traceroute www.example.com` |


### 6 Configuration Commands

In super user view, the router can use the `configure` command to switch to configuration view for management.

Some setting commands support `no` and `default`, wherein `no` indicates canceling a parameter setting and `default` indicates recovering the default setting of a parameter.


| Command                         | Function                                                             | View            | Parameter                                                                     | Example                   |
| ------------------------------- | -------------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------- | ------------------------- |
| `configure terminal`            | Switch to configuration view and input equipment at the terminal end | Super user view | None                                                                          | `configure terminal`      |
| `hostname [<hostname>]`         | Display or set router host name                                      | Configure view  | `<hostname>`: new host name                                                   | `hostname MyRouter`       |
| `clock timezone <timezone> <n>` | Set time zone information                                            | Configure view  | `<timezone>`: timezone name (3 capital letters); `<n>`: deviation (-12 ~ +12) | `clock timezone CST -8`   |
| `ntp server <hostname>`         | Set Internet time server client                                      | Configure view  | `<hostname>`: time server address or domain name                              | `ntp server pool.ntp.org` |
| `config export`                 | Export current config                                                | Configure view  | None                                                                          | `config export`           |
| `config import`                 | Import config                                                        | Configure view  | None                                                                          | `config import`           |


**Example: Set timezone to East Eighth Zone (CST)**

```
(config)# clock timezone CST -8
```

### 7 System Management Commands


| Command                                   | Function                   | View                                | Parameter                                  | Example                     |
| ----------------------------------------- | -------------------------- | ----------------------------------- | ------------------------------------------ | --------------------------- |
| `reboot`                                  | System restarts            | Super user view, configuration view | None                                       | `reboot`                    |
| `enable username <name>`                  | Modify super user username | Configure view                      | `<name>`: new super user username          | `enable username admin`     |
| `enable password [<password>]`            | Modify super user password | Configure view                      | `<password>`: new super user password      | `enable password`           |
| `username <name> [password [<password>]]` | Set user name and password | Configure view                      | `<name>`: username; `<password>`: password | `username abc password 123` |


---

## FAQ

### Question 1: The router is powered on, but cannot access the Internet through it?

1. Check whether a SIM card is inserted.
2. Check whether the SIM card is enabled with data service and whether the service is suspended due to an overdue charge.
3. Check whether the dial-up parameters (e.g., APN, dial-up number, username, and password) are correctly configured.
4. Check whether the IP address of the computer is in the same subnet as the router and whether the gateway address is the router LAN address.

### Question 2: The router is powered on; ping detection from the PC shows packet loss?

1. Check whether the network crossover cable is in good condition.

### Question 3: Forgot the settings after revising the IP address and cannot configure the router?

1. Try the following method to restore the device:
  - Press the RESET button immediately after powering on the device.
  - When the System LED is steady on, release the RESET button; the System LED will blink, then press the RESET button again.
  - When the System LED blinks slowly, release the RESET button. The device will be restored to default settings and will start up normally.

### Question 4: After the router is powered on, it frequently auto restarts. Why?

1. Check whether the module works normally.
2. Check whether a SIM card is inserted.
3. Check whether the SIM card is enabled with data service and whether the service is suspended due to an overdue charge.
4. Check whether the dial-up parameters (e.g., APN, dial-up number, username, and password) are correctly configured.
5. Check whether the signal is normal.
6. Check whether the power supply voltage is normal.

### Question 5: Why does upgrading the firmware always fail?

1. When upgrading locally, check whether the local PC and router are in the same network segment.
2. When upgrading remotely, ensure the router can access the Internet.

### Question 6: After the router establishes a VPN with the VPN server, the PC under the router can connect to the server, but the center cannot connect to the PC under the router?

1. Ensure the firewall of the computer is disabled.

### Question 7: After the router establishes a VPN with the VPN server, the PC under the router cannot ping the server?

1. Ensure "Shared Connection" on [Network] → [WAN] or [Network] → [Cellular] is enabled in the router configuration.

### Question 8: The router is powered on, but the Power LED is not on?

1. Check whether the protective fuse is burned out.
2. Check the power supply voltage range and whether the positive and negative electrodes are correctly connected.

### Question 9: The router is powered on, but the Network LED is not on when connected to the PC?

1. When the PC and router are connected with a network cable, check whether a network crossover cable is used.
2. Check whether the network cable is in good condition.
3. Set the network card of the PC to 10/100M and full duplex.

### Question 10: The router is powered on; when connected to the PC, the Network LED is normal but cannot ping the router?

1. Check whether the IP address of the PC and the router are in the same subnet and whether the gateway address is the router LAN address.

### Question 11: The router is powered on, but cannot be configured through the Web interface?

1. Check whether the IP address of the computer is in the same subnet as the router and whether the gateway address is the router LAN address.
2. Check the firewall settings of the PC used to configure the router; ensure this function is not blocked by the firewall.
3. Check whether the browser has any third-party plugin. It is recommended to configure after unloading the plugin.

### Question 12: The router dial-up always fails. Why?

1. Restore the router to factory default settings and configure the parameters again.

### Question 13: How to restore the router to factory default settings?

1. Power on the device.
2. Press and hold the **RESET** button until the **System LED** turns **yellow**, then release the button.
3. When the **System LED** starts flashing **yellow**, press and hold the **RESET** button again.
4. When the **System LED** starts flashing **green** slowly, release the **RESET** button. The device will be restored to its default settings and will restart normally.

