# Portable Router CR202-Pro Product User Manual

## Preface

### Declaration

Thank you for choosing our product. Before using the product, please read this manual carefully. Compliance with the following statement will help maintain intellectual property rights and legal compliance, and ensure that your usage experience is consistent with the latest product information. If you have any questions or need to obtain written permission, please contact our technical support team at any time.

- **Copyright Notice**
  The contents of this user manual are protected by copyright and are owned by Beijing InHand Network Technology Co., Ltd. and its licensors. No part or all of the contents of this manual may be excerpted or copied without written permission, and may not be disseminated in any form.
- **Disclaimer**
  Due to continuous product technology and specification updates, the company cannot promise that the information in this user manual is completely consistent with the actual product. Therefore, the company does not assume any disputes arising from the inconsistency between actual technical parameters and this user manual. Any changes to the product will not be notified in advance, and the company reserves the right of final modification and interpretation.
- **Copyright Information**
  The contents of this user manual are protected by copyright law. The copyright is owned by Beijing InHand Network Technology Co., Ltd. and its licensors. All rights reserved. The contents of this manual may not be used, copied, or disseminated without written permission.

### Graphical Interface Conventions


| Symbol   | Meaning                                                                               | Example                         |
| -------- | ------------------------------------------------------------------------------------- | ------------------------------- |
| `< >`    | Indicates a button name or variable to be replaced with an actual value               | Click the `<OK>` button         |
| `" "`    | Indicates a window name or menu name                                                  | The pop-up window "New User"    |
| `→`      | Indicates menu hierarchy or operation sequence                                        | 【Network】→【Cellular】            |
| `【 】`    | Indicates a menu or page name                                                         | Enter the 【System Settings】page |
| Cautions | Means reader be careful. Improper action may result in loss of data or device damage. | -                               |
| Note     | Notes contain detailed descriptions and helpful suggestions.                          | -                               |


### Technical Support
Email: support@inhandnetworks.com

URL: www.inhand.com

### How to Use This Manual

**Find Your Role**

- First-time users: It is recommended to read in sequence: "Understanding the Device" → "Installation and First Use" → "Common Scenario Configuration" → "Function Description and Parameter Reference"
- Existing device users: You can directly refer to "Function Description and Parameter Reference" or "Appendix Troubleshooting"
- Cloud platform management users: Refer to "Common Scenario Configuration" for device remote management platform (if applicable)

**Quick Navigation by Task**


| Task                                           | Corresponding Chapter                                                                                   | Estimated Time   |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------- |
| Understanding device appearance and indicators | [Understanding the Device](#chapter-1-understanding-the-device)                                         | About 5 minutes  |
| Installing SIM card and powering on            | [Installation and First Use](#chapter-2-installation-and-first-use)                                     | About 10 minutes |
| Configuring cellular network access            | [Common Scenario Configuration](#chapter-3-common-scenario-configuration)                               | About 5 minutes  |
| Configuring Wi-Fi AP                           | [Common Scenario Configuration](#chapter-3-common-scenario-configuration)                               | About 5 minutes  |
| Viewing system status and logs                 | [Function Description and Parameter Reference](#chapter-4-function-description-and-parameter-reference) | About 10 minutes |
| Troubleshooting network failures               | [Appendix Troubleshooting](#appendix-troubleshooting)                                                   | As needed        |


---

## Chapter 1 Understanding the Device

### 1.1 Overview

The CR202-Pro is a portable 4G cellular router designed to provide reliable Internet connectivity for remote office, mobile scenarios, and field deployments. It supports wired-to-wireless access, which increases the diversity of device access methods and can effectively ensure network continuity. The built-in battery model allows users to work anytime and anywhere. Combined with the InHand Device Manager cloud management platform, the CR202-Pro provides efficient device management capabilities, high-speed network access, and simple network management services.

### 1.2 Package Contents


| Item              | Quantity | Description            |
| ----------------- | -------- | ---------------------- |
| CR202-Pro Router  | 1        | Main device            |
| Power Adapter     | 1        | 5V/2A Type-C interface |
| Quick Start Guide | 1        | Printed document       |


### 1.3 Appearance and Interfaces



**Figure 1-1 CR202-Pro Panel (with battery)**



**Figure 1-2 CR202-Pro Panel (without battery)**


| Interface         | Position | Function Description     |
| ----------------- | -------- | ------------------------ |
| Type-C Power Port | Side     | 5V/2A power input        |
| SIM Card Slot     | Side     | Nano SIM card or eSIM    |
| Antenna Interface | Top      | SMA-J cellular antenna   |
| RESET Button      | Panel    | Restore factory settings |


### 1.4 LED Indicators

**CR202-Pro (without battery)**


| Indicator | Status           | Meaning                                              |
| --------- | ---------------- | ---------------------------------------------------- |
| System    | Off              | Power off                                            |
|           | Blink in green   | Device starting                                      |
|           | Steady in green  | Device working                                       |
|           | Blink in yellow  | Upgrading                                            |
| Network   | Off              | Cellular disabled                                    |
|           | Blink in green   | Dialing up                                           |
|           | Steady in green  | Dialed successfully                                  |
|           | Blink in yellow  | Dialing abnormal                                     |
|           | Blink in red     | No SIM card, cannot read SIM card, or modem abnormal |
| Wi-Fi     | Off              | Wi-Fi disabled                                       |
|           | Blink in green   | Wi-Fi connected, data transmitting                   |
|           | Steady in green  | Wi-Fi enabled                                        |
| Signal    | Off              | Cellular disabled                                    |
|           | Steady in green  | Dialed up, signal level ≥ 20                         |
|           | Steady in yellow | Dialed up, 19 ≥ signal level ≥ 10                    |
|           | Steady in red    | Dialed up, 9 ≥ signal level                          |


**CR202-Pro (with battery)**


| Indicator | Status           | Meaning                                              |
| --------- | ---------------- | ---------------------------------------------------- |
| System    | Off              | Power off                                            |
|           | Blink in green   | Device starting                                      |
|           | Steady in green  | Device working                                       |
|           | Blink in yellow  | Upgrading                                            |
| Network   | Off              | Cellular disabled                                    |
|           | Blink in green   | Dialing up                                           |
|           | Blink in yellow  | Dialing abnormal                                     |
|           | Blink in red     | No SIM card, cannot read SIM card, or modem abnormal |
|           | Steady in green  | Dialed up, signal level ≥ 20                         |
|           | Steady in yellow | Dialed up, 19 ≥ signal level ≥ 10                    |
|           | Steady in red    | Dialed up, 9 ≥ signal level                          |
| Wi-Fi     | Off              | Wi-Fi disabled                                       |
|           | Blink in green   | Wi-Fi connected, data transmitting                   |
|           | Steady in green  | Wi-Fi enabled                                        |
| Battery   | Blink            | Battery charging                                     |
|           | Steady           | Battery discharging                                  |
|           | Green            | 80% < battery level ≤ 100%                           |
|           | Yellow           | 20% < battery level ≤ 80%                            |
|           | Red              | 0 < battery level ≤ 20%                              |


### 1.5 Restore Factory Settings

To restore the device to default settings using the reset button, perform the following steps:

1. Power on the device.
2. Press and hold the **RESET** button until the **System LED** turns **yellow**, then release the button.
3. When the **System LED** starts flashing **yellow**, press and hold the **RESET** button again.
4. When the **System LED** starts flashing **green** slowly, release the **RESET** button. The device will now be restored to its default settings and will restart normally.

### 1.6 Default Settings


| Parameter            | Default Value                               |
| -------------------- | ------------------------------------------- |
| LAN IP Address       | 192.168.2.1                                 |
| Subnet Mask          | 255.255.255.0                               |
| Web Login Username   | adm                                         |
| Web Login Password   | (See nameplate at the bottom of the device) |
| Wi-Fi SSID           | inhand                                      |
| Wi-Fi Authentication | Open type                                   |
| DHCP                 | Enable                                      |
| DHCP IP Pool Range   | 192.168.2.2 ~ 192.168.2.100                 |


---

## Chapter 2 Installation and First Use

### 2.1 Preparations

**Environment Requirements**

- Ensure there is 3G/4G network coverage at the installation location.
- Avoid direct sunlight, heat sources, or strong electromagnetic interference.
- The first installation should be performed under the guidance of an engineer recognized by InHand Networks.

**Tools and Materials Required**


| Item         | Specification          | Remarks                                      |
| ------------ | ---------------------- | -------------------------------------------- |
| PC           | OS: Windows 7/10/11    | At least one Ethernet port (10M/100M)        |
| SIM Card     | Nano SIM or eSIM       | Enabled with data service                    |
| Power Supply | 5V/2A Type-C interface | -                                            |
| Fixation     | Flat surface           | Environment with small vibrational frequency |


> **Caution**: The device shall be installed and operated in a powered-off status.

> **Caution**: Do not use or leave the device at very high temperature conditions (for example, strong direct sunlight or a vehicle in extremely hot conditions). Otherwise, the built-in battery may overheat or catch fire, or its performance will degrade and its service life will decrease. Do not immerse the device in water. Please place it in a cool and dry environment when not in use.

### 2.2 Installation Guide

#### 2.2.1 Install SIM/UIM Card

The CR202-Pro supports a single nano SIM card or eSIM. To install a nano SIM card, follow the steps below:



**Figure 2-1 SIM Card Installation Step 1**



**Figure 2-2 SIM Card Installation Step 2**



**Figure 2-3 SIM Card Installation Step 3**

#### 2.2.2 Install Antenna

Slightly rotate the movable part of the metal SMA-J interface until it cannot be rotated further (at this time, the external thread of the antenna cable should not be visible). Do not forcibly screw the antenna by holding the black rubber lining.

#### 2.2.3 Connect Power Supply

The CR202-Pro supports internal battery or Type-C interface (5V/2A). Pay attention to the power voltage level.

#### 2.2.4 Log In to the Router Web Interface

Upon completion of hardware installation, ensure the Ethernet card has been installed in the supervisory PC prior to logging in to the Web settings page of the router.

**I. Automatic Acquisition of IP Address (Recommended)**

Set the supervisory computer to "automatic acquisition of IP address" and "automatic acquisition of DNS server address" (default configuration of the computer system) to allow the device to automatically assign an IP address for the supervisory computer.

**II. Set a Static IP Address**

Set the IP address of the supervisory PC (such as 192.168.2.2) and the LAN interface of the device in the same network segment (initial IP address of the LAN interface of the device: 192.168.2.1, subnet mask: 255.255.255.0).



**Figure 2-4 IP Address Configuration**

**III. Cancel the Proxy Server**

If the current supervisory PC uses a proxy server to access the Internet, cancel the proxy service. The operating steps are as follows:

1. In the browser window, select "Tools >> Internet options".
2. Select the "Connections" page and click the "LAN Settings" button to enter the "LAN Settings" window.
3. Confirm whether the option "Use a Proxy Server for LAN" is checked; if it is checked, cancel it and click the `<OK>` button.

**IV. Log In to / Exit the Web Settings Page**

Access the default IP address 192.168.2.1 in a browser, enter the username and password (see the nameplate at the bottom of the device for login credentials) in the pop-up window, and then access the router's WEB management page. If the browser alarms that the connection is not private, click "Advanced" and proceed to the address.



**Figure 2-5 Web Login Page**

> **Caution**: For security purposes, modify the default login password after the first login and keep the password information secure.

### 2.3 Quick Check

After installation is complete, verify the following items:

- The SIM card is correctly inserted and the antenna is securely installed.
- The power supply is properly connected and the device is powered on.
- The System LED is steady green, indicating the device is working normally.
- The PC can obtain an IP address in the 192.168.2.x subnet via DHCP.
- The Web management page at 192.168.2.1 can be accessed via a browser.

---

## Chapter 3 Common Scenario Configuration

### Scenario 1: Cellular Network Access

**Objective**: Access the Internet via 4G cellular network.

**Prerequisites**: The SIM card has been inserted and the antenna is installed; the device is powered on.

**Estimated Time**: About 5 minutes.

**Operation Steps**:

1. Insert the SIM card and install the antenna. (Refer to [Section 2.2.1](#221-install-simuim-card) and [Section 2.2.2](#222-install-antenna).)
2. Log in to the Web management page, and enter 【Network】→【Cellular】.
3. Enable the "Cellular" dial-up function.
4. Select the SIM network provider profile (configure APN, username, and password if necessary).
5. Click `<Save>` and wait for the connection to be established.

**Verification Method**:

1. Check the Network LED status on the device to confirm the cellular connection is normal.
2. Access an Internet website from a PC connected to the router to confirm normal browsing.

**Common Issues**:

- Network connection fails: Check whether the SIM card is correctly inserted and whether the APN parameters are correct.
- Data transmission abnormality: Check the signal strength and data plan balance.

### Scenario 2: Wired WAN Access

**Objective**: Access the Internet via a wired WAN connection.

**Prerequisites**: An Ethernet cable is connected from the upstream network to the WAN/LAN1 port of the router.

**Estimated Time**: About 5 minutes.

**Operation Steps**:

1. Connect the Ethernet cable from the upstream router/switch to the WAN/LAN1 port of the CR202-Pro.
2. Log in to the Web management page, and enter 【Network】→【WAN/LAN Switch】.
3. Configure the WAN/LAN1 port as WAN mode.
4. Select the access type: Static IP, Dynamic Address (DHCP), or ADSL Dialing (PPPoE).
5. Enter the corresponding parameters according to the ISP requirements.
6. Click `<Save>` to apply the configuration.

**Verification Method**:

1. Check the Network Connections status page to confirm the WAN connection is established.
2. Access an Internet website from a PC connected to the router.

**Common Issues**:

- Unable to obtain an IP address: Confirm whether the upstream network supports DHCP, or whether the static IP parameters are correct.
- PPPoE dialing fails: Check whether the username and password are correct.

### Scenario 3: Wi-Fi AP Configuration

**Objective**: Provide wireless LAN access for other devices.

**Prerequisites**: The router has connected to the Internet via WAN or cellular.

**Estimated Time**: About 5 minutes.

**Operation Steps**:

1. Log in to the Web management page, and enter 【Network】→【Switch WLAN Mode】.
2. Set the WLAN mode to AP, and reboot the device to take effect.
3. Enter 【Network】→【WLAN】.
4. Configure the SSID name, authentication method, and encryption type.
5. Click `<Save>` to apply the configuration.

**Verification Method**:

1. Use a wireless device (such as a mobile phone or laptop) to search for the configured SSID.
2. Connect to the Wi-Fi and access the Internet to confirm normal operation.

**Common Issues**:

- Unable to find the Wi-Fi signal: Check whether the SSID broadcast is enabled.
- Connection successful but no Internet access: Confirm that the router's WAN/cellular connection is normal.

### Scenario 4: VPN Tunnel Configuration

**Objective**: Establish a secure VPN tunnel for remote access.

**Prerequisites**: The router can access the Internet; the VPN server parameters are known.

**Estimated Time**: About 10 minutes.

**Operation Steps**:

1. Log in to the Web management page, and enter 【VPN】.
2. Select the VPN type: IPSec Tunnels, OpenVPN, WireGuard Tunnels, or ZeroTier VPN.
3. Enter the tunnel name, server address, authentication method, and other parameters.
4. Click `<Add>` or `<Save>` to create the tunnel.
5. Check the VPN connection status on the corresponding configuration page.

**Verification Method**:

1. Check the VPN status on the Web page to confirm the tunnel is established.
2. Test the connectivity between the local network and the remote VPN network.

**Common Issues**:

- Tunnel establishment fails: Check whether the server address and authentication parameters are correct.
- Connected but unable to access remote resources: Check the routing and firewall settings.

### Scenario 5: Link Backup Configuration

**Objective**: Ensure network continuity by automatically switching to a backup link when the primary link fails.

**Prerequisites**: Both the primary link and the backup link are available (e.g., WAN and cellular).

**Estimated Time**: About 5 minutes.

**Operation Steps**:

1. Log in to the Web management page, and enter 【Network】→【Link Backup】.
2. Enable the link backup function.
3. Select the backup mode: Hot failover, Cold failover, or Load balance.
4. Set the primary link and backup link.
5. Configure the ICMP detection server, interval, timeout, and retry times.
6. Click `<Save>` to apply the configuration.

**Verification Method**:

1. Disconnect the primary link and observe whether the system automatically switches to the backup link.
2. Check the network connectivity to confirm uninterrupted service.

**Common Issues**:

- Backup link does not switch: Check whether the ICMP detection server address is reachable.
- Unstable switching: Adjust the ICMP detection timeout and retry parameters.

### Scenario 6: Cloud Platform Remote Management

**Objective**: Connect the router to the InHand Device Manager platform for remote management.

**Prerequisites**: The router can access the Internet; a Device Manager account has been registered.

**Estimated Time**: About 5 minutes.

**Operation Steps**:

1. Log in to the Web management page, and enter 【Services】→【Device Manager】.
2. Enable the Device Manager function.
3. Select the server address: `iot.inhand.com.cn` (China) or `iot.inhandnetworks.com` (Global).
4. Enter the registered account information.
5. Configure the upload intervals for LBS info and traffic info as needed.
6. Click `<Save>` to apply the configuration.

**Verification Method**:

1. Enter 【Status】→【Device Manager】 to check the connection status between the router and the platform.
2. Log in to the Device Manager Web portal to confirm the device is online.

**Common Issues**:

- Unable to connect to the platform: Check whether the router can access the Internet and whether the account is correct.
- Device not displayed online: Check the firewall settings and confirm the secure channel is enabled.

---

## Chapter 4 Function Description and Parameter Reference

### 4.1 System

This part is used to check and configure system time, router WEB configuration interface, language, and the name of the router.

#### 4.1.1 Basic Setup

Check and set the WEB configuration interface language and the name of the router.

From the navigation tree, select 【System】→【Basic Setup】, then enter the "Basic Setup" page.


| **Basic Settings**                                                                              |                                                                        |             |
| ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ----------- |
| Function description: Select display language of the router web page and set personalized name. |                                                                        |             |
| **Parameters**                                                                                  | **Description**                                                        | **Default** |
| Language                                                                                        | Configure language of WEB configuration interface                      | English     |
| Host Name                                                                                       | Set a name for the host or device connected to the router for viewing. | Router      |


#### 4.1.2 System Time

To ensure the coordination between this device and other devices, it is required to set the system time accurately. This function is used to configure and check system time as well as system time zone.

From the navigation tree, select 【System】→【Time】, then enter the "Time" webpage. Click `<Sync Time>` to synchronize the time of the router with the system time of the PC.


| **System Time**                                                               |                                                                                              |                        |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------- |
| Function description: Set local time zone and automatic updating time of NTP. |                                                                                              |                        |
| **Parameters**                                                                | **Description**                                                                              | **Default**            |
| Time of Router                                                                | Display present time of router                                                               | 8:00:00 AM, 12/12/2015 |
| PC Time                                                                       | Display present time of PC                                                                   | Present time           |
| Timezone                                                                      | Set time zone of router                                                                      | Custom                 |
| Custom TZ String                                                              | Set TZ string of router                                                                      | CST-8                  |
| Auto update Time                                                              | Select whether to automatically update time; options include startup or every 1/2/... hours. | On startup             |
| NTP Time Servers                                                              | Select NTP server to synchronize time                                                        | 1.pool.ntp.org         |


#### 4.1.3 Admin Access

Admin services include HTTP, HTTPS, TELNET, and SSHD.

- **HTTP**: Hypertext Transfer Protocol, used for transferring web pages on the Internet. After enabling HTTP service on the device, users can log on via HTTP and access and control the device using a web browser.
- **HTTPS**: Secure Hypertext Transfer Protocol, the secure version of HTTP, which supports the SSL protocol and is more secure.
- **TELNET**: Telnet protocol provides telnet and virtual terminal functions through a network. The device supports Telnet Client and Telnet Server.
- **SSHD**: SSH protocol provides security for remote login sessions and other network services. The SSHD service uses the SSH protocol, which has higher security than Telnet.

From the navigation tree, select 【System】→【Admin Access】, then enter the "Admin Access" page.


| **Admin Access**                                                                                                                                                                |                                                                                                                                                                                              |                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Function description: 1. Modify username and password of router. 2. The router can be accessed by the following 4 methods: HTTP, HTTPS, TELNET, and SSHD. 3. Set login timeout. |                                                                                                                                                                                              |                                                                                                        |
| **Parameters**                                                                                                                                                                  | **Description**                                                                                                                                                                              | **Default**                                                                                            |
| **Username/Password**                                                                                                                                                           |                                                                                                                                                                                              |                                                                                                        |
| Username                                                                                                                                                                        | Set name of user who logs in to WEB configuration page                                                                                                                                       | adm                                                                                                    |
| Old Password                                                                                                                                                                    | Previous password for accessing WEB configuration page                                                                                                                                       |                                                                                                        |
| New Password                                                                                                                                                                    | New password for accessing WEB configuration page                                                                                                                                            | N/A                                                                                                    |
| Confirm New Password                                                                                                                                                            | Reconfirm the new password                                                                                                                                                                   | N/A                                                                                                    |
| **Admin functions**                                                                                                                                                             |                                                                                                                                                                                              |                                                                                                        |
| Service Port                                                                                                                                                                    | Service port of HTTP/HTTPS/TELNET/SSHD                                                                                                                                                       | 80/443/23/22                                                                                           |
| Local Access                                                                                                                                                                    | Enable — Allow local LAN to administrate the router with corresponding service (e.g., HTTP). Disable — Local LAN cannot administrate the router with corresponding service (e.g., HTTP).     | Enable                                                                                                 |
| Remote Access                                                                                                                                                                   | Enable — Allow remote host to administrate the router with corresponding service (e.g., HTTP). Disable — Remote host cannot administrate the router with corresponding service (e.g., HTTP). | Enable                                                                                                 |
| Allowed Access from WAN (Optional)                                                                                                                                              | Set allowed access from WAN                                                                                                                                                                  | Set the hosts which are allowed to access the router, e.g., 192.168.2.1/30 or 192.168.2.1-192.168.2.10 |
| Description                                                                                                                                                                     | For recording significance of various parameters of admin functions (without influencing router configuration)                                                                               | N/A                                                                                                    |
| **Non-privileged users**                                                                                                                                                        |                                                                                                                                                                                              |                                                                                                        |
| Username                                                                                                                                                                        | Configure non-privileged login user name                                                                                                                                                     | N/A                                                                                                    |
| Password                                                                                                                                                                        | Configure the password of the non-privileged user                                                                                                                                            | N/A                                                                                                    |
| **Other Parameters**                                                                                                                                                            |                                                                                                                                                                                              |                                                                                                        |
| Log Timeout                                                                                                                                                                     | Set login timeout (router will automatically disconnect the configuration interface after login timeout)                                                                                     | 500 seconds                                                                                            |


#### 4.1.4 System Log

A remote log server can be set through "System Log", and all system logs will be uploaded to the remote log server through the Internet. This requires remote log software, such as Kiwi Syslog Daemon, on the remote log server.

Kiwi Syslog Daemon is a free log server software for Windows. It can receive, record, and display logs from hosts (such as routers, switches, and Unix hosts). After downloading and installing Kiwi Syslog Daemon, it must be configured through the menus "File >> Setup >> Input >> UDP".

From the navigation tree, select 【System】→【System Log】, then enter the "System Log" page.


| **System Log**                                                                                                |                                           |             |
| ------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ----------- |
| Function description: Configure IP address and port number of remote log server which will record router log. |                                           |             |
| **Parameters**                                                                                                | **Description**                           | **Default** |
| Log to Remote System                                                                                          | Enable log server                         | Disable     |
| Log server address and port (UDP)                                                                             | Set address and port of remote log server | N/A: 514    |


#### 4.1.5 Configuration Management

Here users can back up the configuration parameters, import the desired parameter backup, and reset the router.

From the navigation tree, select 【System】→【Config Management】, then enter the "Config Management" page.


| **Configuration Management**                                      |                                                                                                     |             |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------- |
| Function description: Set parameters of configuration management. |                                                                                                     |             |
| **Parameters**                                                    | **Description**                                                                                     | **Default** |
| Browse                                                            | Choose the configuration file                                                                       | N/A         |
| Import                                                            | Import configuration file to router                                                                 | N/A         |
| Backup                                                            | Backup configuration file to host                                                                   | N/A         |
| Restore default configuration                                     | Select to restore default configuration (effective after rebooting)                                 | N/A         |
| Disable the hardware reset button                                 | Select to disable hardware reset button of the router                                               | Disable     |
| Network Provider (ISP)                                            | For configuring APN, username, password, and other parameters of network providers across the world |             |


> **Note**: Validity and order of imported configurations should be ensured. Acceptable configurations will later be serially executed in order after system reboot. If the configuration files are not arranged according to effective order, the system will not enter the desired state.

> **Note**: In order not to affect the operation of the current system, after performing an import configuration or restore default configuration, restart the device to make the new configuration take effect.

#### 4.1.6 Scheduler

After this function is enabled, the device will reboot at the scheduled time. The scheduler function will take effect after the router synchronizes time.

From the navigation tree, select 【System】→【Scheduler】, then enter the "Scheduler" page.

| **Scheduler** | | |
| --- | --- | --- |
| Function description: Set scheduler for system reboot. |     |     |
| **Parameters** | **Description** | **Default** |
| Enable | Enable/disable this function | Disable |
| Time | Select the reboot time | 0:00 |
| Days | Reboot the router everyday | Everyday |
| Show advanced options | Enable more detailed schedule rules, allowing to set multiple rules to reboot the router at specific times or intervals. Enabling this feature will disable the everyday reboot feature above. | Disable |
| Reboot after dialed | Router will reboot after dial-up successfully; will not take effect if this parameter is blank. | N/A |

#### 4.1.7 Upgrade

The upgrading process can be divided into two steps. In the first step, firmware will be written to the backup file zone. In the second step, firmware in the backup file zone will be copied to the main firmware zone, which should be carried out during system restart. During software upgrading, any operation on the web page is not allowed; otherwise, software upgrading may be interrupted.

From the navigation tree, select 【System】→【Upgrade】, then enter the "Upgrade" page.

To upgrade the system:

1. Click `<Browse>` to choose the upgrade file.
2. Click `<Upgrade>` and then click `<OK>` to begin the upgrade.
3. After the firmware upgrade succeeds, click `<Reboot>` to restart the device.

#### 4.1.8 Reboot

Save the configurations before reboot; otherwise, the configurations that are not saved will be lost after reboot.

To reboot the system, click 【System】→【Reboot】, then click `<OK>`.

#### 4.1.9 Logout

To log out, click 【System】→【Logout】, and then click `<OK>`.

---

### 4.2 Network

#### 4.2.1 Cellular

Insert a SIM card and dial up to achieve wireless network connection.

Click 【Network】→【Cellular】 in the navigation tree to enter the Cellular configuration page.


| **Cellular**                                                                                                                                  |                                                                                                                                                                                                                                                                                                            |                |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Function description: Configure parameters of PPP dial-up. Generally, users only need to set basic configuration instead of advanced options. |                                                                                                                                                                                                                                                                                                            |                |
| **Parameters**                                                                                                                                | **Description**                                                                                                                                                                                                                                                                                            | **Default**    |
| Enable                                                                                                                                        | Enable Cellular dial-up.                                                                                                                                                                                                                                                                                   | Enable         |
| Time Schedule                                                                                                                                 | Set time schedule                                                                                                                                                                                                                                                                                          | ALL            |
| Force Reboot                                                                                                                                  | Router will reboot if it cannot dial up for a long time and reaches the max retry time                                                                                                                                                                                                                     | Enable         |
| Shared connection (NAT)                                                                                                                       | Enable — Local device connected to Router can access the Internet via Router. Disable — Local device connected to Router cannot access the Internet via Router.                                                                                                                                            | Enable         |
| Default Route                                                                                                                                 | Enable default route                                                                                                                                                                                                                                                                                       | Enable         |
| SIM Network Provider                                                                                                                          | Select network provider for inserted SIM card                                                                                                                                                                                                                                                              | Profile 1      |
| Network Select Type                                                                                                                           | Select network type; router will try 4G, 3G, 2G in proper order if Auto is selected                                                                                                                                                                                                                        | Auto           |
| Connection Mode                                                                                                                               | Optional: Always Online, Connect On Demand, Manual. It will support configuring Triggered by SMS if Connect On Demand mode is selected.                                                                                                                                                                    | Always Online  |
| Redial Interval                                                                                                                               | Set the redialing time when dial-up fails                                                                                                                                                                                                                                                                  | 30 s           |
| **Show Advanced Options**                                                                                                                     |                                                                                                                                                                                                                                                                                                            |                |
| Dual SIM Enable                                                                                                                               | Some CR202-Pro types support eSIM; enable this option to enable eSIM dial-up                                                                                                                                                                                                                               | Disable        |
| eSIM Network Provider                                                                                                                         | Select network provider for eSIM card                                                                                                                                                                                                                                                                      | Profile 1      |
| eSIM Blinding ICCID                                                                                                                           | Set ICCID of eSIM                                                                                                                                                                                                                                                                                          | N/A            |
| eSIM PIN Code                                                                                                                                 | For setting eSIM PIN code                                                                                                                                                                                                                                                                                  | N/A            |
| eSIM SIM Card Operator                                                                                                                        | Set the ISP that the eSIM card connects to                                                                                                                                                                                                                                                                 | Auto           |
| Main SIM                                                                                                                                      | Set the SIM card that is used to dial up first                                                                                                                                                                                                                                                             | SIM            |
| Max Number of Dial                                                                                                                            | Set max number of dial attempts; if dial-up is not successful after this number, the router will switch SIM cards                                                                                                                                                                                          | 5              |
| CSQ Threshold                                                                                                                                 | Set threshold of signal; if current signal level is lower than this, the router will switch SIM cards                                                                                                                                                                                                      | 0 (Disable)    |
| Min Connect Time                                                                                                                              | Set the minimum connect time for each dial-up attempt                                                                                                                                                                                                                                                      | 0 (Disable)    |
| Initial Commands                                                                                                                              | Set customized initial AT commands which will be operated at the beginning of dialing up                                                                                                                                                                                                                   | AT             |
| Blinding ICCID                                                                                                                                | Set ICCID of SIM                                                                                                                                                                                                                                                                                           | N/A            |
| PIN Code                                                                                                                                      | For setting PIN code of SIM                                                                                                                                                                                                                                                                                | N/A            |
| Static MTU                                                                                                                                    | Set max transmission unit after enabling                                                                                                                                                                                                                                                                   | Disable        |
| Use Peer DNS                                                                                                                                  | Click to receive peer DNS assigned by the ISP                                                                                                                                                                                                                                                              | Enable         |
| Link detection interval                                                                                                                       | Set link detection interval                                                                                                                                                                                                                                                                                | 55 s           |
| Debug                                                                                                                                         | Enable debug mode, print debug log in system log                                                                                                                                                                                                                                                           | Disable        |
| ICMP Detection Mode                                                                                                                           | Set ICMP detection mode; the router will check the link connection status via ICMP packet. Ignore Traffic: Router will send ICMP packet regardless of whether there is traffic in the cellular interface. Monitor Traffic: Router will not send ICMP packet if there is traffic in the cellular interface. | Ignore Traffic |
| ICMP Detection Server                                                                                                                         | Set the ICMP Detection Server. N/A represents not enabling ICMP detection.                                                                                                                                                                                                                                 | N/A            |
| ICMP Detection Interval                                                                                                                       | Set ICMP Detection Interval                                                                                                                                                                                                                                                                                | 30 s           |
| ICMP Detection Timeout                                                                                                                        | Set ICMP Detection Timeout (the link will be regarded as down if ICMP times out)                                                                                                                                                                                                                           | 20 s           |
| ICMP Detection Retries                                                                                                                        | Set the max. number of retries if ICMP fails (router will redial if reaching max. times)                                                                                                                                                                                                                   | 5              |



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

Click 【Network】→【WAN/LAN Switch】 to configure the WAN/LAN1 port.

When this port is configured as WAN, the CR202-Pro supports three types of wired access: static IP, dynamic address (DHCP), and ADSL (PPPoE) dialing. When this port is configured as LAN, it supports jumping to the LAN configuration page via the Settings button on the right of the select box.

**DHCP** adopts Client/Server communication mode. The Client sends a configuration request to the Server, which feeds back corresponding configuration information, including the distributed IP address to the Client, to achieve the dynamic configuration of the IP address and other information.

**PPPoE** is a point-to-point protocol over Ethernet. The user has to install a PPPoE Client on the basis of the original connection method. Through PPPoE, remote access devices can achieve the control and charging of each accessed user.

WAN/LAN1 works as LAN by default.


| **WAN - Static IP**                                                      |                                                                                                                                                                 |                      |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Function description: Access the Internet via wired lines with fixed IP. |                                                                                                                                                                 |                      |
| **Parameters**                                                           | **Description**                                                                                                                                                 | **Default**          |
| Shared connection (NAT)                                                  | Enable — Local device connected to Router can access the Internet via Router. Disable — Local device connected to Router cannot access the Internet via Router. | Enable               |
| Default route                                                            | Enable default route                                                                                                                                            | Enable               |
| MAC Address                                                              | MAC Address of the device                                                                                                                                       | Device's MAC address |
| IP Address                                                               | Set IP address of WAN                                                                                                                                           | 192.168.1.29         |
| Netmask                                                                  | Set subnet mask of WAN                                                                                                                                          | 255.255.255.0        |
| Gateway                                                                  | Set gateway of WAN                                                                                                                                              | 192.168.1.1          |
| MTU                                                                      | Max. transmission unit, default/manual settings                                                                                                                 | default (1500)       |
| **Multiple IP support (at most 8 additional IP addresses can be set)**   |                                                                                                                                                                 |                      |
| IP Address                                                               | Set additional IP address of WAN                                                                                                                                | N/A                  |
| Subnet mask                                                              | Set subnet mask                                                                                                                                                 | N/A                  |
| Description                                                              | For recording significance of additional IP address                                                                                                             | N/A                  |



| **WAN - Dynamic Address (DHCP)**                                                                        |                                                                                                                                                                 |                      |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Function description: Set WAN in DHCP mode to get the address allocated by other routers automatically. |                                                                                                                                                                 |                      |
| **Parameters**                                                                                          | **Description**                                                                                                                                                 | **Default**          |
| Shared connection (NAT)                                                                                 | Enable — Local device connected to Router can access the Internet via Router. Disable — Local device connected to Router cannot access the Internet via Router. | Enable               |
| Default route                                                                                           | Enable default route                                                                                                                                            | Enable               |
| MAC Address                                                                                             | MAC Address of the device                                                                                                                                       | Device's MAC address |
| MTU                                                                                                     | Max. transmission unit, default/manual settings                                                                                                                 | default (1500)       |



| **WAN - ADSL Dialing (PPPoE)**                     |                                                                                                                                                                 |                      |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Function description: Set ADSL dialing parameters. |                                                                                                                                                                 |                      |
| **Parameters**                                     | **Description**                                                                                                                                                 | **Default**          |
| Shared connection                                  | Enable — Local device connected to Router can access the Internet via Router. Disable — Local device connected to Router cannot access the Internet via Router. | Enable               |
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
| TX Queue Length                                    | Set length of transmit queue                                                                                                                                    | 3                    |
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

Click 【Network】→【LAN】 to configure the LAN interface of the router so that other devices can access the Internet via Ethernet cable in LAN.


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

The CR202-Pro supports two types of WLAN mode: AP and STA.

Click 【Network】→【Switch WLAN Mode】 in the navigation tree to set the WLAN mode of the router. After changing and saving the configuration, reboot the device to make the configuration take effect.

#### 4.2.5 WLAN Client (AP Mode)

When working in AP mode, the CR202-Pro WLAN will provide a network access point for other wireless network devices. Ensure that the CR202-Pro has already connected to the Internet via WAN or cellular.

Click 【Network】→【WLAN】 in the navigation tree to enter the "WLAN" interface.


| **WLAN**                                                                                                                          |                                                                                                               |                              |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| Function description: Support WiFi function and provide wireless LAN access on site and identity authentication of wireless user. |                                                                                                               |                              |
| **Parameters**                                                                                                                    | **Description**                                                                                               | **Default**                  |
| SSID broadcast                                                                                                                    | After turning on, users can search the WLAN via SSID name                                                     | Enable                       |
| Mode                                                                                                                              | Six types for options: 802.11g/n, 802.11g, 802.11n, 802.11b, 802.11b/g, 802.11b/g/n                           | 802.11b/g/n                  |
| Channel                                                                                                                           | Select the channel                                                                                            | 11                           |
| SSID                                                                                                                              | SSID name defined by user                                                                                     | Refer to equipment nameplate |
| Authentication method                                                                                                             | Support open type, shared type, auto selection of WEP, WPA-PSK, WPA, WPA2-PSK, WPA2, WPA/WPA2, WPAPSK/WPA2PSK | Refer to equipment nameplate |
| Encryption                                                                                                                        | Support NONE, WEP                                                                                             | NONE                         |
| Wireless bandwidth                                                                                                                | Both 20MHz and 40MHz for selection                                                                            | 20MHz                        |
| Enable WDS                                                                                                                        | Click to enable WDS                                                                                           | Disable                      |
| Default Route                                                                                                                     | Click to enable Route                                                                                         | Disable                      |
| Bridged SSID                                                                                                                      | Set bridged SSID                                                                                              | None                         |
| Bridged BSSID                                                                                                                     | Set bridged BSSID                                                                                             | None                         |
| Scan                                                                                                                              | Click "Scan" to scan available APs nearby                                                                     |                              |
| Auth Mode                                                                                                                         | Open type, shared type, WPA-PSK, WPA2-PSK                                                                     | Refer to equipment nameplate |
| Encryption Method                                                                                                                 | Support NONE, WEP                                                                                             | None                         |


#### 4.2.6 WLAN Client (STA Mode)

When working in STA mode, the router can access the Internet by connecting to other APs.

Click 【Network】→【WLAN Client】 in the navigation tree to enter the "WLAN" interface. Select "Client" for the interface type and configure relevant parameters. (At this moment, the cellular interface in 【Network】→【Cellular】 should be closed.)

The SSID scan function is enabled only when "Client" is selected as the WLAN interface. Click the "Scan" button to get all available APs and their status, select an AP, and configure the corresponding parameters to connect. After configuring the WLAN Client, configure the access type in 【Network】→【WAN(STA)】.


| **WLAN Client**                                                                    |                                                       |             |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------- | ----------- |
| Function description: Support Wi-Fi function and access to wireless LAN as client. |                                                       |             |
| **Parameters**                                                                     | **Description**                                       | **Default** |
| Mode                                                                               | Support many modes including 802.11b/g/n              | 802.11b/g/n |
| SSID                                                                               | Name of the SSID to be connected                      | inhand      |
| Authentication method                                                              | Keep consistent with the access point to be connected | Open type   |
| Encryption                                                                         | Keep consistent with the access point to be connected | NONE        |


#### 4.2.7 Link Backup

Click 【Network】→【Link Backup】 in the navigation tree to enter the configuration interface.


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



| **Link Backup - Backup Mode**                        |                                                                                        |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Function description: Select the way of link backup. |                                                                                        |
| **Parameters**                                       | **Description**                                                                        |
| Hot failover                                         | Main link and backup link keep online at the same time; switch if current link is off. |
| Cold failover                                        | Backup line will only be online when the main link is disconnected.                    |
| Load balance                                         | Transfer data via corresponding route after ICMP detection succeeds.                   |


#### 4.2.8 IP Passthrough

The IP passthrough function distributes the address obtained by the WAN port to the device at the lower end of the LAN port. When external access to the router downstream devices is required, the router transmits data to the downstream device. Click 【Network】→【IP Passthrough】, then enter the "IP Passthrough" page.


| **IP Passthrough**                                                                                                             |                                                    |                   |
| ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- | ----------------- |
| Function description: Allow LAN port device to obtain WAN port address; used for external access to router downstream devices. |                                                    |                   |
| **Parameters**                                                                                                                 | **Description**                                    | **Default**       |
| IP Passthrough                                                                                                                 | Enable IP Passthrough                              | Disable           |
| IP Passthrough Mode                                                                                                            | Select work mode (DHCP Dynamic / DHCP fix MAC)     | DHCP Dynamic      |
| Fix MAC Address                                                                                                                | Set fixed MAC address if in DHCP fix MAC mode      | 00:00:00:00:00:00 |
| DHCP lease                                                                                                                     | Set DHCP lease time and reacquire after expiration | 2 Minutes         |


#### 4.2.9 Static Route

Static routes need to be set manually, after which packets will be transferred to appointed routes.

To set a static route, click 【Network】→【Static Route】 in the navigation tree, then enter the "Static Route" interface.


| **Static Route**                                                                                                      |                                                       |               |
| --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ------------- |
| Function description: Add/delete additional static route of router. Generally, it is unnecessary for users to set it. |                                                       |               |
| **Parameters**                                                                                                        | **Description**                                       | **Default**   |
| Destination Address                                                                                                   | Set IP address of the destination                     | 0.0.0.0       |
| Netmask                                                                                                               | Set subnet mask of the destination                    | 255.255.255.0 |
| Gateway                                                                                                               | Set the gateway of the destination                    | N/A           |
| Interface                                                                                                             | Select WAN/CELLULAR 1/LAN/WAN(STA) of the destination | N/A           |
| Description                                                                                                           | For recording significance of static route address    | N/A           |


---

### 4.3 Services

#### 4.3.1 DHCP Service

DHCP adopts Client/Server communication mode. The Client sends a configuration request to the Server, which feeds back corresponding configuration information, including the distributed IP address to the Client, to achieve the dynamic configuration of the IP address and other information.

- The duty of the DHCP Server is to distribute an IP address when a workstation logs on and ensure each workstation is supplied with a different IP address. The DHCP Server has simplified some network management tasks requiring manual operations to the largest extent.
- As a DHCP Client, the device receives the IP address distributed by the DHCP server after logging in to the DHCP server, so the Ethernet interface of the device needs to be configured into an automatic mode.

To enable the DHCP service, select 【Services】→【DHCP Service】 in the navigation tree, then enter the "DHCP Service" page.


| **DHCP Service**                                                                                                                                                                                                                                 |                                                                                           |               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | ------------- |
| Function description: If the host connected with the router chooses to obtain an IP address automatically, then such service must be activated. Static designation of DHCP allocation could help certain hosts to obtain specified IP addresses. |                                                                                           |               |
| **Parameters**                                                                                                                                                                                                                                   | **Description**                                                                           | **Default**   |
| Enable DHCP                                                                                                                                                                                                                                      | Enable DHCP service and dynamically allocate IP address                                   | Enable        |
| IP Pool Starting Address                                                                                                                                                                                                                         | Set starting IP address of dynamic allocation                                             | 192.168.2.2   |
| IP Pool Ending Address                                                                                                                                                                                                                           | Set ending IP address of dynamic allocation                                               | 192.168.2.100 |
| Lease                                                                                                                                                                                                                                            | Set lease of IP allocated dynamically                                                     | 60 minutes    |
| DNS                                                                                                                                                                                                                                              | Set DNS Server                                                                            | 192.168.2.1   |
| Windows Name Server                                                                                                                                                                                                                              | Set Windows name server                                                                   | N/A           |
| **Static designation of DHCP allocation (at most 20 DHCPs designated statically can be set)**                                                                                                                                                    |                                                                                           |               |
| MAC Address                                                                                                                                                                                                                                      | Set a statically specified DHCP MAC address (different from other MACs to avoid conflict) | N/A           |
| IP Address                                                                                                                                                                                                                                       | Set a statically specified IP address                                                     | 192.168.2.2   |
| Host                                                                                                                                                                                                                                             | Set the hostname                                                                          | N/A           |


#### 4.3.2 DNS

DNS (Domain Name System) is a distributed database used in TCP/IP application programs, providing switching between domain names and IP addresses. Through DNS, users can directly use meaningful domain names that are easy to memorize, and the DNS Server in the network can resolve the domain name into the correct IP address. Manually set the DNS; use DNS via dialing if it is empty. Generally, it needs to be set only when a static IP is used on the WAN port.

Click 【Services】→【Domain Name Service】 in the navigation tree to enter the "Domain Name Service" interface.


| **DNS (DNS Settings)**                             |                                          |             |
| -------------------------------------------------- | ---------------------------------------- | ----------- |
| Function description: Configure parameters of DNS. |                                          |             |
| **Parameters**                                     | **Description**                          | **Default** |
| Primary DNS                                        | Set Primary DNS                          | 0.0.0.0     |
| Secondary DNS                                      | Set Secondary DNS                        | 0.0.0.0     |
| Disable local DNS server                           | Not to transfer local DNS server address | Disable     |


#### 4.3.3 DNS Relay

The CR202-Pro works as a DNS Agent and relays DNS request and response messages between the DNS Client and DNS Server to carry out domain name resolution on behalf of the DNS Client.

From the navigation tree, select 【Services】→【DNS Relay】, then enter the "DNS Relay" page.


| **DNS Relay service**                                                                                                                           |                                                          |                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------- |
| Function description: If the host connected with the router chooses to obtain a DNS address automatically, then such service must be activated. |                                                          |                                                            |
| **Parameters**                                                                                                                                  | **Description**                                          | **Default**                                                |
| Enable DNS Relay service                                                                                                                        | Click to enable DNS service                              | Enable (DNS will be enabled when DHCP service is enabled.) |
| **Designate [IP address <=> domain name] pair (20 IP address <=> domain name pairs can be designated)**                                         |                                                          |                                                            |
| IP Address                                                                                                                                      | Set IP address of designated IP address <=> domain name  | N/A                                                        |
| Host                                                                                                                                            | Domain Name                                              | N/A                                                        |
| Description                                                                                                                                     | For recording significance of IP address <=> domain name | N/A                                                        |


> **Note**: When enabling DHCP, the DHCP relay is also enabled automatically. The relay cannot be disabled without disabling DHCP.

#### 4.3.4 DDNS

DDNS maps the user's dynamic IP address to a fixed DNS service. When the user connects to the network, the client program will pass the host's dynamic IP address to the server program on the service provider's host through information passing. The server program is responsible for providing DNS service and realizing dynamic DNS. This means that DDNS captures the user's each change of IP address and matches it with the domain name, so that other Internet users can communicate through the domain name. What end customers have to remember is the domain name assigned by the dynamic domain name registrar, regardless of how it is achieved.

DDNS serves as a client tool of DDNS and is required to coordinate with a DDNS Server. Before applying this function, a domain name shall be applied for and registered on a proper website such as [www.3322.org](http://www.3322.org).

The CR202-Pro DDNS service types include QDNS (3322)-Dynamic, QDNS(3322)-Static, DynDNS-Dynamic, DynDNS-Static, DynDNS-Custom, and No-IP.com.

To set DDNS, click 【Services】→【Dynamic Domain Name】 in the navigation tree, then enter the "Dynamic Domain Name" interface.


| **Dynamic Domain Name**                                |                                         |             |
| ------------------------------------------------------ | --------------------------------------- | ----------- |
| Function description: Set dynamic domain name binding. |                                         |             |
| **Parameters**                                         | **Description**                         | **Default** |
| Current Address                                        | Display present IP of router            | N/A         |
| Service Type                                           | Select the domain name service provider | Disable     |



| **Enable function of dynamic domain name**                                                                     |                                                               |                                              |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | -------------------------------------------- |
| Function description: Set dynamic domain name binding. (Explained with the configuration of QDNS service type) |                                                               |                                              |
| **Parameters**                                                                                                 | **Description**                                               | **Default**                                  |
| Service Type                                                                                                   | QDNS (3322)-Dynamic                                           | Disable                                      |
| URL                                                                                                            | [http://www.3322.org/](http://www.3322.org/)                  | [http://www.3322.org/](http://www.3322.org/) |
| Username                                                                                                       | User name assigned in the application for dynamic domain name | N/A                                          |
| Password                                                                                                       | Password assigned in the application for dynamic domain name  | N/A                                          |
| Host Name                                                                                                      | Host name assigned in the application for dynamic domain name | N/A                                          |
| Wildcard                                                                                                       | Enable wildcard character                                     | Disable                                      |
| MX                                                                                                             | Set MX                                                        | N/A                                          |
| Backup MX                                                                                                      | Enable backup MX                                              | Disable                                      |
| Force Update                                                                                                   | Enable force update                                           | Disable                                      |


#### 4.3.5 Device Manager

The CR202-Pro supports connection to InHand Device Manager for remotely managing InHand products. Customers can manage and operate routers, check status, and upgrade software in batches via this platform.

Click 【Services】→【Device Manager】 in the navigation tree to enter the "Device Manager" interface.


| **Device Manager**                                                             |                                                                                           |                        |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | ---------------------- |
| Function description: Connect the router to the platform for cloud management. |                                                                                           |                        |
| **Parameters**                                                                 | **Description**                                                                           | **Default**            |
| Enable                                                                         | Enable Device Manager                                                                     | Disable                |
| Service Type                                                                   | Platform work mode: Device Manager or Custom                                              | Device Manager         |
| Server                                                                         | Select cloud platform address: iot.inhand.com.cn (China), iot.inhandnetworks.com (Global) | iot.inhandnetworks.com |
| Secure Channel                                                                 | Use encryption protocol for secure data transmission between router and platform          | Enable                 |
| Registered Account                                                             | Account registered in Device Manager                                                      | N/A                    |
| LBS info Upload Interval                                                       | Cellular information upload interval                                                      | 1 Hour                 |
| Series Info Upload Interval                                                    | Traffic information upload interval                                                       | 1 Hour                 |
| Channel Keepalive                                                              | Keep alive packet interval                                                                | 30 Seconds             |


#### 4.3.6 SNMP

Network devices are usually sparsely-located on a network. It is time-consuming for the administrator to configure and manage these network devices on site. In addition, if these devices are from different vendors, each of which provides a suite of independent management interfaces (for example, different command line interfaces), the workload of configuring the devices in batches is huge. In this situation, the traditional manual configuration method has the deficiencies of high cost and low efficiency. The network administrator can use the Simple Network Management Protocol (SNMP) to remotely configure and manage the devices and perform real-time monitoring on them.



**Figure 4-4 SNMP Topology**

To run the SNMP protocol on a network, configure the NMS program on the management side and the SNMP agent on the managed devices.

By using SNMP:

1. The NMS can collect status information of the managed devices anytime and anywhere through agents and remotely control these devices.
2. The agents can promptly report the current status and faults of managed devices to the NMS.

Currently, the SNMP agents support SNMPv1, SNMPv2c, and SNMPv3. SNMPv1 and SNMPv2c use community names for authentication; SNMPv3 uses user names and passwords for authentication. Click 【Services】→【SNMP】 to configure.


| **SNMPv1 and SNMPv2c Parameters** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                    |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **Parameters**                    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Default**        |
| Enable                            | Enable/disable the SNMP function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Disabled           |
| Version                           | Set the version of the SNMP protocol used to manage the router. The versions of SNMPv1, v2c, and v3 are available. SNMPv1 is applicable to small-sized networks with simple networking and low security requirements, or secure and stable small networks, such as campus networks and small enterprise networks. SNMPv2c is applicable to medium- and large-sized networks with low security requirements, or with good security (for example, VPNs) but running many services, which may lead to traffic congestion. SNMPv3 is applicable to networks of various sizes, especially networks that have strict security requirements and can be managed only by authorized network administrators. For example, SNMPv3 can be used if data between the NMS and managed device is transmitted over a public network. | v1                 |
| Contact Information               | Fill in the contact information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Empty              |
| Location Information              | Fill in the location.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Empty              |
| **Community Management**          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                    |
| Community Name                    | User-defined community name. The community names of SNMPv1 and SNMPv2c are the passwords used by the NMS to read and write data on agents. This parameter must be set the same on both agents and NMS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | public and private |
| Access Limit                      | Access limit includes the MIB objects that can be read only or read/written by the NMS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Read-Only          |
| MIB View                          | Select the MIB objects that can be monitored and managed by the NMS. Only the default view is supported currently.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | defaultView        |



| **SNMPv3 Parameters**     |                                                                                                                                               |               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Parameters**            | **Description**                                                                                                                               | **Default**   |
| **User Group Management** |                                                                                                                                               |               |
| Groupname                 | User-defined user group name. The length is 1 to 32 characters.                                                                               | None          |
| Security Level            | Select a security level for the group. The values include NoAuth/NoPriv, Auth/NoPriv, and Auth/Priv.                                          | NoAuth/NoPriv |
| Read-only View            | Select the SNMP read-only view. Only the default view is supported currently.                                                                 | defaultView   |
| Read-write View           | Select the SNMP read-write view. Only the default view is supported currently.                                                                | defaultView   |
| Inform View               | Select the SNMP inform view. Only the default view is supported currently.                                                                    | defaultView   |
| **Usm Management**        |                                                                                                                                               |               |
| Username                  | User-defined user name. The length is 1 to 32 characters.                                                                                     | None          |
| Groupname                 | The group to which a user is added must have been configured in the user group management table.                                              | None          |
| Authentication            | Select an authentication mode. Three authentication modes are available: MD5, SHA, and None. If None is selected, authentication is disabled. | None          |
| Authentication Password   | This parameter is available only when the authentication mode is not None. The length is 8 to 32 characters.                                  | None          |
| Encryption                | Select the encryption mode. The values are None, AES, and DES.                                                                                | None          |
| Encryption Password       | This parameter is available only when the authentication mode is not None. The length is 8 to 32 characters.                                  | None          |


#### 4.3.7 SNMP Trap

SNMP trap is a type of entrance. When this entrance is reached, the SNMP managed devices actively notify the NMS, instead of waiting for the polling of the NMS. On an SNMP-enabled network, the agents on managed devices can report errors to the NMS anytime, without the need of waiting for the polling of the NMS. The errors are reported to the NMS through traps. Click 【Services】→【SNMP Trap】 to configure.


| **SNMP Trap Configuration Parameters** |                                                                                                                           |             |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **Parameters**                         | **Description**                                                                                                           | **Default** |
| Trap SigLevel                          | Set the trap signal threshold. When this threshold is reached, the agent outputs logs to the NMS.                         | 10          |
| Destination Address                    | Fill in the IP address of the NMS.                                                                                        | None        |
| Security Name                          | Fill in the community name for SNMPv1 or SNMPv2c, and fill in the user name for SNMPv3. The length is 1 to 32 characters. | None        |
| UDP Port                               | Fill in the UDP port number, ranging from 1 to 65535.                                                                     | 162         |


#### 4.3.8 SMS

SMS permits message-based reboot and manual dialing. Configure "Permit to Phone Number" and click `<Apply and Save>`. After that, users can send a "reboot" command to restart the device or send a custom connection or disconnection command to redial or disconnect the device.

From the navigation tree, select 【Services】→【SMS】, then enter the "SMS" page.


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
| Description                                                                           | Describe SMS control.                                                                 | N/A         |


#### 4.3.9 Traffic Manager

This function is mainly used to count data traffic on the cellular interface. If the threshold is 0, the router will only count and the rules will not take effect. This function requires enabling the NTP function.

Choose 【Services】→【Traffic Manager】 to go to the "Traffic Manager" page.


| **Traffic Manager**                                                     |                                                                                                                                                                                       |                |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Function description: Monitor and manage the traffic use of the router. |                                                                                                                                                                                       |                |
| **Parameters**                                                          | **Description**                                                                                                                                                                       | **Default**    |
| Enable                                                                  | Click to enable the traffic manager function.                                                                                                                                         | Disable        |
| Start Day                                                               | The day to start counting data traffic every month                                                                                                                                    | 1              |
| Monthly Threshold                                                       | Data traffic threshold every month                                                                                                                                                    | 0MB            |
| When Over Monthly Threshold                                             | Operation when data traffic used within a month reaches the threshold: Only Reporting, Block Except Management (will not influence DM and management requirement), Shutdown Interface | Only Reporting |
| Last 24-Hours Threshold                                                 | Data traffic threshold in last 24 Hours                                                                                                                                               | 0KB            |
| When Over 24-Hours Threshold                                            | Operation when data traffic used within 24 hours reaches the threshold                                                                                                                | Only Reporting |
| Advance                                                                 | Custom statistics and operations for the last several hours                                                                                                                           | Disable        |


#### 4.3.10 Alarm Settings

When an abnormality occurs, the router will report an alarm according to the settings. Currently, the router supports sending alarms in the following situations: System Service Fault, Memory Low, WAN/LAN1 Link-Up/Down, LAN2 Link-Up/Down, Cellular Up/Down, Traffic Alarm, Traffic Disconnect Alarm, SIM/UIM Card Switch, Active Link Switch, SIM/UIM Card Fault, Signal Quality Fault.

In the Alarm Manager interface, users can perform the following operations:

- Select alarm types in the "Alarm Input" area.
- Set the alarm notification method of the console in the "Alarm Output" area.

Choose 【Services】→【Alarm Manager】 to go to the "Alarm Manager" page.

#### 4.3.11 User Experience Plan

InHand Networks' User Experience Program is designed to improve the product user experience and customer service quality.

Users can disable or enable the User Experience Plan in 【Services】→【User Experience Plan】.

---

### 4.4 Firewall

The firewall function of the router implements corresponding control to data flow at the entry direction (from Internet to LAN) and exit direction (from LAN to Internet) according to the content features of messages (such as protocol style, source/destination IP address, etc.) and ensures safe operation of the router and hosts in the local area network.

#### 4.4.1 Basic

From the navigation tree, select 【Firewall】→【Basic】, then enter the basic setup page.


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

Filter network data by customized rules to allow or prohibit the specified data flow forwarded by the router.

To enable Access Control, from the navigation tree, select 【Firewall】→【Filtering】, then enter the "Filtering" page.


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

From the navigation tree, select 【Firewall】→【Device Access Filtering】, then enter the "Device Access Filtering" page.


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

From the navigation tree, select 【Firewall】→【Content Filtering】, then enter the "Content Filtering" page.


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

Port mapping is also called virtual server. Setting port mapping can enable extranet hosts to access a specific port of a host corresponding to an IP address on the intranet.

To configure port mapping, go to the navigation tree, select 【Firewall】→【Port Mapping】, then enter the "Port Mapping" page.


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

Both the router and the IP address of the host on the intranet can correspond with one virtual IP. Without changing the IP allocation of the intranet, the extranet can access the host on the intranet via virtual IP. This function is always used with VPN.

To configure virtual IP mapping, go to the navigation tree, select 【Firewall】→【Virtual IP Mapping】.


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

From the navigation tree, select 【Firewall】→【DMZ】, then enter the "DMZ" page.


| **DMZ**                                       |                                        |             |
| --------------------------------------------- | -------------------------------------- | ----------- |
| Function description: Configure DMZ settings. |                                        |             |
| **Parameters**                                | **Description**                        | **Default** |
| Enable DMZ                                    | Check to enable the DMZ.               | Disable     |
| DMZ Host                                      | Set address of DMZ Host                | N/A         |
| Source Address Range                          | Enter range of external source address | N/A         |
| Interface                                     | Select external interface of DMZ       | N/A         |


#### 4.4.8 MAC-IP Binding

If the default filter policy in the basic setting of the firewall is disabled, only hosts specified in MAC-IP Binding can have access to the outer net.

From the navigation tree, select 【Firewall】→【MAC-IP Binding】, then enter the "MAC-IP Binding" page.


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


| **NAT**                                            |                                                 |             |
| -------------------------------------------------- | ----------------------------------------------- | ----------- |
| Function description: Configure parameters of NAT. |                                                 |             |
| **Parameters**                                     | **Description**                                 | **Default** |
| Enable                                             | Enable NAT                                      | Enable      |
| Type                                               | Set convert type                                | SNAT        |
| Proto                                              | Select protocol                                 | TCP         |
| Source IP                                          | Set source IP of the NAT rule                   | 0.0.0.0/0   |
| Source Port                                        | Set source port of the NAT rule                 | N/A         |
| Destination                                        | Set destination IP of the NAT rule              | 0.0.0.0/0   |
| Destination Port                                   | Set destination port of the NAT rule            | 0.0.0.0/0   |
| Interface                                          | Set interface of the NAT rule                   | N/A         |
| Translated Address                                 | Translate the IP address if it matches the rule | 0.0.0.0     |
| Translated Port                                    | Translate the port if it matches the rule       | N/A         |


---

### 4.5 QoS

To ensure all LAN users can normally access network resources, the IP traffic control function can limit the flow of specified hosts in LAN. QoS provides dedicated bandwidth and different service quality for different applications, greatly improving the network service capabilities.

#### 4.5.1 IP BW Limit

Bandwidth control sets a limit on the upload and download speeds when accessing external networks.

From the navigation tree, select 【QoS】→【IP BW Limit】.


| **IP Bandwidth Limit**                                            |                                    |             |
| ----------------------------------------------------------------- | ---------------------------------- | ----------- |
| Function description: Configure parameters of IP bandwidth limit. |                                    |             |
| **Parameters**                                                    | **Description**                    | **Default** |
| Enable                                                            | Click to enable IP bandwidth limit | Disable     |
| Download bandwidth                                                | Set download total bandwidth       | 1000kbit/s  |
| Upload bandwidth                                                  | Set upload total bandwidth         | 1000kbit/s  |
| Control port of flow                                              | Select CELLULAR/WAN                | CELLULAR    |
| **Host Download Bandwidth**                                       |                                    |             |
| Enable                                                            | Click to enable                    | Enable      |
| IP Address                                                        | Set IP address                     | N/A         |
| Guaranteed Rate (kbit/s)                                          | Set rate                           | 1000kbit/s  |
| Priority                                                          | Select priority                    | Medium      |
| Description                                                       | Describe IP bandwidth limit        | N/A         |


---

### 4.6 VPN

VPN is for building a private dedicated network on a public network via the Internet. "Virtuality" indicates a logical network.

Two Basic Features of VPN:

1. **Private**: The resources of VPN are unavailable to unauthorized VPN users on the internet; VPN can ensure and protect its internal information from external intrusion.
2. **Virtual**: The communication among VPN users is realized via a public network which, meanwhile, can be used by unauthorized VPN users so that what VPN users obtain is only a logical private network. This public network is regarded as the VPN Backbone.

Build a credible and secure link by connecting remote users, company branches, and partners to the network of the headquarters via VPN so as to realize secure transmission of data.



**Figure 4-5 VPN Fundamental Principle**

The fundamental principle of VPN indicates enclosing a VPN message into a tunnel with tunneling technology and establishing a private data transmission channel utilizing the VPN Backbone so as to realize transparent message transmission.

Tunneling technology encloses another protocol message with one protocol. Also, the encapsulation protocol itself can be enclosed or carried by other encapsulation protocols. To the users, the tunnel is a logical extension of PSTN/link of ISDN, which is similar to the operation of an actual physical link.

VPN settings include IPSec settings, IPSec tunnels, OpenVPN, OpenVPN Advanced, and certificate management, etc.

#### 4.6.1 IPSec Settings

A majority of data contents are transmitted in plaintext on the Internet, which has many potential dangers such as password and bank account information being stolen and tampered with, user identity being imitated, and suffering from malicious network attacks. After deployment of IPSec on the network, it can protect data transmission and reduce the risk of information disclosure.

IPSec is a group of open network security protocols made by IETF, which can ensure the security of data transmission between two parties on the Internet via data origin authentication, data encryption, data integrity, and anti-replay function on the IP level. It is able to reduce the risk of disclosure and guarantee data integrity and confidentiality as well as maintain the security of service transmission of users.

IPSec, including AH, ESP, and IKE, can protect one or more data flows between hosts, between host and gateway, and between gateways. The security protocols of AH and ESP can ensure security, and IKE is used for cipher code exchange.

IPSec can establish bidirectional Security Alliance on the IPSec peer pairs to form a secure and interworking IPSec tunnel and to realize the secure transmission of data on the Internet.

From the navigation tree, select 【VPN】→【IPSec Settings】, then enter the "IPSec Settings" page.


| **IPSec settings**                                   |                                                                                                                                                                                 |             |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Function description: Select the log level of IPSec. |                                                                                                                                                                                 |             |
| **Parameters**                                       | **Description**                                                                                                                                                                 | **Default** |
| Log level                                            | Click to select log level. Normal: Only key logs will be printed into the system log. Debug: More logs in debug level will be printed. Data: All logs of IPSec will be printed. | Normal      |


#### 4.6.2 IPSec Tunnels

From the navigation tree, select 【VPN】→【IPSec Tunnels】, enter "IPSec Tunnels", and click `<add>`.


| **IPSec Tunnels**                               |                                                                                                                   |                                                |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Function description: Configure IPSec tunnels.  |                                                                                                                   |                                                |
| **Parameters**                                  | **Description**                                                                                                   | **Default**                                    |
| Show Advanced Options                           | Click to enable advanced options                                                                                  | Disable (open advanced options after enabling) |
| **Basic parameters**                            |                                                                                                                   |                                                |
| Tunnel Name                                     | User defines tunnel name                                                                                          | IPSec_tunnel_1                                 |
| Destination Address                             | Set destination IP address or domain name                                                                         | 0.0.0.0                                        |
| IKE Version                                     | Set IKE version: IKEv1/IKEv2                                                                                      | IKEv1                                          |
| Startup Modes                                   | Select Auto Activated/Triggered by Data/Passive/Manually Activated                                                | Auto Activated                                 |
| Restart WAN when failed                         | Click to enable                                                                                                   | Enable                                         |
| Negotiation Mode (IKEv1)                        | Select main mode or aggressive mode                                                                               | Main Mode                                      |
| IPSec Protocol (Advanced Option)                | Select ESP/AH                                                                                                     | ESP                                            |
| IPSec Mode (Advanced Option)                    | Select tunnel mode/transmission mode                                                                              | Tunnel Mode                                    |
| VPN over IPSec (Advanced Option)                | Select L2TP over IPSec/GRE over IPSec/None                                                                        | None                                           |
| Tunnel Type                                     | Select Host-Host/Host-Subnet/Subnet-Host/Subnet-Subnet                                                            | Subnet-Subnet                                  |
| Local subnet address                            | Set local subnet IP address                                                                                       | 192.168.2.1                                    |
| Local Subnet Mask                               | Set local subnet mask                                                                                             | 255.255.255.0                                  |
| Peer Subnet Address                             | Set peer subnet IP address                                                                                        | 0.0.0.0                                        |
| Peer Subnet Mask                                | Set remote netmask                                                                                                | 255.255.255.0                                  |
| **Phase I Parameters**                          |                                                                                                                   |                                                |
| IKE Strategy                                    | Multiple strategies available                                                                                     | 3DES-MD5-DH2                                   |
| IKE Life Cycle                                  | Set IKE life cycle                                                                                                | 86400 s                                        |
| Local ID Type                                   | Select IP address/User FQDN/FQDN. Fill in the ID according to the ID type (USERFQDN is in standard email format). | IP Address                                     |
| Peer ID Type                                    | Select IP address/User FQDN/FQDN                                                                                  | IP Address                                     |
| Authentication method                           | Select shared key/digital certificate                                                                             | Shared key                                     |
| Key                                             | Set IPSec VPN key                                                                                                 | N/A                                            |
| **XAUTH Parameters (Advanced Option)**          |                                                                                                                   |                                                |
| XAUTH Mode                                      | Click to enable XAUTH mode                                                                                        | Disable                                        |
| XAUTH username                                  | User defines XAUTH username                                                                                       | N/A                                            |
| XAUTH password                                  | User defines XAUTH password                                                                                       | N/A                                            |
| MODECFG                                         | Click to enable MODECFG                                                                                           | Disable                                        |
| **Phase II Parameters**                         |                                                                                                                   |                                                |
| IPSec Strategy                                  | Multiple strategies available                                                                                     | 3DES-MD5-96                                    |
| IPSec Life Cycle                                | Set IPSec life cycle                                                                                              | 3600 s                                         |
| Perfect Forward Secrecy (PFS) (Advanced Option) | Select disable/Group 1/Group 2/Group 5                                                                            | Disable (this needs to match the server)       |
| **Link Detection Parameters (Advanced Option)** |                                                                                                                   |                                                |
| DPD Interval                                    | Set time interval.                                                                                                | 60 s                                           |
| DPD Timeout                                     | Set the timeout for dropped packets.                                                                              | 180 s                                          |
| ICMP Detection Server                           | Set ICMP detection server                                                                                         | N/A                                            |
| ICMP Detection Local IP                         | Set ICMP detection local IP                                                                                       | N/A                                            |
| ICMP Detection Interval                         | Set ICMP Detection Interval                                                                                       | 60 s                                           |
| ICMP Detection Timeout                          | Set ICMP detection timeout                                                                                        | 5 s                                            |
| ICMP Detection Retries                          | Set ICMP detection max. retries                                                                                   |                                                |


Note:The security level of three encryption algorithms ranks successively: AES, 3DES, DES. The implementation mechanism of the encryption algorithm with stricter security is complex and has slow arithmetic speed. The DES algorithm can satisfy ordinary safety requirements.

#### 4.6.3 OpenVPN

A single point participating in the establishment of VPN is allowed to carry out ID verification by preset private key, third-party certificate, or username/password. OpenSSL encryption library and SSLv3/TLSv1 protocol are massively used.

In OpenVPN, if a user needs to access a remote virtual address (address family matching virtual network card), then the OS will send the data packet (TUN mode) or data frame (TAP mode) to the virtual network card through the routing mechanism. Upon reception, the service program will receive and process those data and send them out through the outer net by SOCKET, owing to which the remote service program will receive those data and carry out processing, then send them to the virtual network card, then application software receives and accomplishes a complete unidirectional transmission, and vice versa.

From the navigation tree, select 【VPN】→【OpenVPN】, then enter the "OpenVPN" page, and click `<Add>`.


| **OpenVPN**                                         |                                                                                                                                  |               |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| Function description: Configure OpenVPN parameters. |                                                                                                                                  |               |
| **Parameters**                                      | **Description**                                                                                                                  | **Default**   |
| Tunnel Name                                         | OpenVPN tunnel name, cannot be changed by the system                                                                             | OpenVPN_T_1   |
| Enable                                              | Click to enable                                                                                                                  | Enable        |
| Mode                                                | Client/server                                                                                                                    | Client        |
| Protocol                                            | UDP/ICMP                                                                                                                         | UDP           |
| Port                                                | Set port                                                                                                                         | 1194          |
| OPENVPN Server                                      | Set OPENVPN Server address                                                                                                       | N/A           |
| Authentication method                               | N/A, pre-shared key, username/password, digital certificate (multiple client), digital certificate, username+digital certificate | N/A           |
| Local IP Address                                    | Set local IP address                                                                                                             | N/A           |
| Remote IP Address                                   | Set remote IP address                                                                                                            | N/A           |
| Remote Subnet                                       | Set remote subnet address                                                                                                        | N/A           |
| Remote Netmask                                      | Set remote subnet mask                                                                                                           | 255.255.255.0 |
| Link Detection Interval                             | Set link detection interval                                                                                                      | 60 s          |
| Link Detection Timeout                              | Set link detection timeout                                                                                                       | 300 s         |
| Enable NAT                                          | Click to enable NAT                                                                                                              | Enable        |
| Enable LZO                                          | Click to enable LZO compression                                                                                                  | Enable        |
| Encryption Algorithms                               | Blowfish(128)/DES(128)/3DES(192)/AES(128)/AES(192)/AES(256)                                                                      | Blowfish(128) |
| MTU                                                 | Set max. transmission unit                                                                                                       | 1500          |
| Max. Fragment Size                                  | Set max. fragment size                                                                                                           | N/A           |
| Debug Level                                         | Error/warning/information/debug                                                                                                  | Warning       |
| Interface Type                                      | TUN/TAP                                                                                                                          | TUN           |
| Expert Option (not recommended)                     | Set expert option, not recommended                                                                                               | N/A           |


#### 4.6.4 OpenVPN Advanced

From the navigation tree, select 【VPN】→【OpenVPN Advanced】 and enter the "OpenVPN Advanced" interface.


| **OpenVPN Advanced**                                            |                                   |             |
| --------------------------------------------------------------- | --------------------------------- | ----------- |
| Function description: Configure parameters of OpenVPN Advanced. |                                   |             |
| **Parameters**                                                  | **Description**                   | **Default** |
| Enable Client-to-Client (Server Mode Only)                      | Click to enable                   | Disable     |
| **Client Management**                                           |                                   |             |
| Enable                                                          | Click to enable client management | Enable      |
| Tunnel Name                                                     | Set tunnel name                   | OpenVPN_T_1 |
| Username/CommonName                                             | Set username/common name          | N/A         |
| Password                                                        | Set client password               | N/A         |
| Client IP (4th byte must be 4n+1)                               | Set client IP address             | N/A         |
| Local Static Route                                              | Set local static route            | N/A         |
| Remote Static Route                                             | Set remote static route           | N/A         |


#### 4.6.5 WireGuard Tunnels

WireGuard is a new generation VPN which aims at providing more efficient and more secure VPN service with an advanced encryption algorithm.

Click the `Add` button to configure and create a WireGuard tunnel, and check the VPN status on this page.

From the navigation tree, select 【VPN】→【WireGuard Tunnels】, then enter the WireGuard VPN configuration page.


| **WireGuard Tunnels**                                                                                                                                                                                                                                                  |                                                                                                                                                                           |                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Function description: Configure WireGuard VPN.                                                                                                                                                                                                                         |                                                                                                                                                                           |                 |
| **Parameters**                                                                                                                                                                                                                                                         | **Description**                                                                                                                                                           | **Default**     |
| Tunnel Name                                                                                                                                                                                                                                                            | Set the name of WireGuard tunnel                                                                                                                                          | WireGuard_tun_1 |
| Enable                                                                                                                                                                                                                                                                 | Enable/Disable tunnel                                                                                                                                                     | Enable          |
| Address                                                                                                                                                                                                                                                                | Local virtual IP address and mask in CIDR format, for example 192.168.2.1/24                                                                                              | N/A             |
| Shared Connection(NAT)                                                                                                                                                                                                                                                 | Enable — Local device connected to Router can access the Internet via this tunnel. Disable — Local device connected to Router cannot access the Internet via this tunnel. | Enable          |
| Listening Port                                                                                                                                                                                                                                                         | VPN port; the system will listen to the default port (51820) if this parameter is blank. Different tunnels need to use different listening ports.                         | 51820           |
| Private Key                                                                                                                                                                                                                                                            | Private key generated by WireGuard                                                                                                                                        | N/A             |
| MTU                                                                                                                                                                                                                                                                    | MTU of VPN packet                                                                                                                                                         | 1500            |
| **Peer Parameters**                                                                                                                                                                                                                                                    |                                                                                                                                                                           |                 |
| Name                                                                                                                                                                                                                                                                   | Name of VPN peer side                                                                                                                                                     | N/A             |
| End Point                                                                                                                                                                                                                                                              | IP address and port of remote side, for example 1.2.3.4:51820                                                                                                             | N/A             |
| Allowed IPs                                                                                                                                                                                                                                                            | Limit the local address that can access via this tunnel                                                                                                                   | 0.0.0.0/0 (all) |
| Public Key                                                                                                                                                                                                                                                             | Generated by WireGuard, corresponding to the local private key                                                                                                            | N/A             |
| Pre-shared Key (Optional)                                                                                                                                                                                                                                              | Generated by WireGuard, can increase the security of the tunnel                                                                                                           | N/A             |
| Persistent Keepalive                                                                                                                                                                                                                                                   | Keep alive interval when NAT is enabled; 0 means disable                                                                                                                  | 25              |
| **WireGuard Key Generator**                                                                                                                                                                                                                                            |                                                                                                                                                                           |                 |
| Click the Generate button to create a private key, public key, or pre-shared key by WireGuard. It also supports creating a public key after entering a private key. The private key is used in local tunnel parameters; the public key is used in the peer public key. |                                                                                                                                                                           |                 |


#### 4.6.6 ZeroTier VPN

ZeroTier VPN supports users to build a network that allows all client devices to access each other. There are two network types in ZeroTier VPN: planet and moon. In a planet network, the user needs to log in and create a VPN network on [https://www.zerotier.com/](https://www.zerotier.com/) first. A moon network is a private VPN network created by the user.

From the navigation tree, select 【VPN】→【ZeroTier VPN】, then enter the "ZeroTier VPN" configuration page.


| **ZeroTier VPN**                                            |                                                      |             |
| ----------------------------------------------------------- | ---------------------------------------------------- | ----------- |
| Function description: Configure parameters of ZeroTier VPN. |                                                      |             |
| **Parameters**                                              | **Description**                                      | **Default** |
| Enable                                                      | Click to enable/disable ZeroTier VPN                 | Disable     |
| Tunnel Name                                                 | Set local VPN tunnel name to identify tunnel         | N/A         |
| Network Type                                                | Select network type: planet or moon                  | planet      |
| Network ID                                                  | Set network ID (16 letters) to connect to VPN server | N/A         |


#### 4.6.7 Certificate Management

From the navigation tree, select 【VPN】→【Certificate Management】, then enter the "Certificate Management" page.


| **Certificate Management**                                            |                                                                  |                               |
| --------------------------------------------------------------------- | ---------------------------------------------------------------- | ----------------------------- |
| Function description: Configure parameters of certificate management. |                                                                  |                               |
| **Parameters**                                                        | **Description**                                                  | **Default**                   |
| Enable SCEP (Simple Certificate Enrollment Protocol)                  | Click to enable                                                  | Disable                       |
| Protect Key                                                           | Set protect key                                                  | N/A                           |
| Protect Key Confirm                                                   | Confirm protect key                                              | N/A                           |
| **Enable SCEP (Simple Certificate Enrollment Protocol)**              |                                                                  |                               |
| Force to Re-enroll                                                    | Click to enable force to re-enroll                               | Disable                       |
| Request Status                                                        | The system is "ready to refile an enrollment"; cannot be changed | Ready to refile an enrollment |
| Server URL                                                            | Set server URL                                                   | N/A                           |
| Common Name                                                           | Set common name                                                  | N/A                           |
| FQDN                                                                  | Set FQDN                                                         | N/A                           |
| Unit 1                                                                | Set unit 1                                                       | N/A                           |
| Unit 2                                                                | Set unit 2                                                       | N/A                           |
| Domain                                                                | Set domain                                                       | N/A                           |
| Serial Number                                                         | Set serial number                                                | N/A                           |
| Challenge                                                             | Set challenge                                                    | N/A                           |
| Challenge Confirm                                                     | Challenge confirm                                                | N/A                           |
| Protect Key                                                           | Set protect key                                                  | N/A                           |
| Protect Key Confirm                                                   | Confirm protect key                                              | N/A                           |
| Unstructured address                                                  | Set unstructured address                                         | N/A                           |
| RSA Key Length                                                        | Set RSA key length                                               | 1024                          |
| Poll Interval                                                         | Set poll interval                                                | 60 s                          |
| Poll Timeout                                                          | Set poll timeout                                                 | 3600 s                        |
| **Import/Export Certificate**                                         |                                                                  |                               |
| Import CA Certificate                                                 | Manually import local CA to the router                           | N/A                           |
| Export CA Certificate                                                 | Manually export CA to local computer                             | N/A                           |
| Import CRL                                                            | Manually import CRL to the router                                | N/A                           |
| Export CRL                                                            | Manually export CRL to local computer                            | N/A                           |
| Import Public Key Certificate                                         | Manually import Public Key Certificate to the router             | N/A                           |
| Export Public Key Certificate                                         | Manually export Public Key Certificate to local computer         | N/A                           |
| Import Private Key Certificate                                        | Manually import Private Key Certificate to the router            | N/A                           |
| Export Private Key Certificate                                        | Manually export Private Key Certificate to local computer        | N/A                           |
| Import PKCS12                                                         | Manually import PKCS12 to the router                             | N/A                           |
| Export PKCS12                                                         | Manually export PKCS12 to local computer                         | N/A                           |


> **Note**: When using certificates, make sure the time of the router is synchronized with real time.

---

### 4.7 Tools

#### 4.7.1 PING

Enter the navigation tree, select 【Tools】→【Ping】.


| **PING**                                                                                                       |                                          |             |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ----------- |
| Function description: Use ICMP to detect the connection status between the router and the destination address. |                                          |             |
| **Parameters**                                                                                                 | **Description**                          | **Default** |
| Host                                                                                                           | Address of the destination host          | N/A         |
| PING Count                                                                                                     | Set the PING count                       | 4           |
| Packet Size                                                                                                    | Set the size of PING detection           | 32 bytes    |
| Expert Option                                                                                                  | Advanced parameter of PING is available. | N/A         |


#### 4.7.2 Traceroute

To perform traceroute, select 【Tools】→【Traceroute】 in the navigation tree.


| **Traceroute**                                                       |                                                                   |             |
| -------------------------------------------------------------------- | ----------------------------------------------------------------- | ----------- |
| Function description: Applied for network routing failure detection. |                                                                   |             |
| **Parameters**                                                       | **Description**                                                   | **Default** |
| Host                                                                 | Address of the destination host which to be detected is required. | N/A         |
| Maximum Hops                                                         | Set the max. hops for traceroute                                  | 20          |
| Timeout                                                              | Set the timeout of traceroute                                     | 3 s         |
| Protocol                                                             | ICMP/UDP                                                          | UDP         |
| Expert Option                                                        | Advanced parameter for traceroute is available.                   | N/A         |


#### 4.7.3 Link Speed Test

Enter the navigation tree, select 【Tools】→【Link Speed Test】, then enter the "Link Speed Test" page.

Select a file locally and click upload/download, then check the network speed in the log.

#### 4.7.4 TCPDUMP

Enter the navigation tree, select 【Tools】→【TCPDUMP】, then enter the TCP dump page.


| **TCPDUMP**                                                                          |                                                      |             |
| ------------------------------------------------------------------------------------ | ---------------------------------------------------- | ----------- |
| Function description: Capture the packets transferring through a specific interface. |                                                      |             |
| **Parameters**                                                                       | **Description**                                      | **Default** |
| Interface                                                                            | Select the interface to capture the packet           | ANY         |
| Capture number                                                                       | Stop TCP dump after capturing this number of packets | 10          |
| Expert Option                                                                        | Advanced parameter for TCPDUMP                       | N/A         |


---

### 4.8 Status

#### 4.8.1 System

From the navigation tree, select 【Status】→【System】, then enter the "System" page.

This page displays system statistics, including name, model, serial number, description, current version, current Bootloader version, router time, PC time, UP time, CPU load, and memory consumption. Users can click the `<Sync Time>` button to synchronize the router with the system time of the host, as covered in the setup chapter.

#### 4.8.2 Power

From the navigation tree, select 【Status】→【Power】, then enter the "Power" page.

This page displays the power information, including power version, type, and status. Also, this page displays battery charge status, battery full charge time, battery capacity, battery health status, battery voltage, battery temperature, and battery remaining time.

#### 4.8.3 Modem

From the navigation tree, select 【Status】→【Modem】, then enter the "Modem" page.

This page displays the basic information of dial-up, including status, signal level, register status, IMEI (ESN) code, IMSI code, LAC, and cell ID.

#### 4.8.4 Traffic Statistics

Choose 【Status】→【Traffic Statistics】 to go to the "Traffic Statistics" page to query traffic statistics.

This page displays the traffic statistics on the dialing interface, including the statistics on traffic received in the latest month, traffic transmitted in the latest month, traffic received on the last day, and traffic transmitted on the last day.

#### 4.8.5 Alarm

Choose 【Status】→【Alarm】 to go to the "Alarm" page to view all alarms generated in the system since power-on. Users can clear or confirm the alarms.

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

#### 4.8.6 WLAN

Choose 【Status】→【WLAN】 to go to the "WLAN" page to query the WLAN connection status.

This page displays the WLAN connection information, including channel, SSID, BSSID, security, signal (%), mode, and status.

#### 4.8.7 Network Connections

From the navigation tree, select 【Status】→【Network Connections】, then enter the "Network Connections" page to see the connection status.

This page shows the basic information of dial-up and LAN.

- **WAN** includes MAC address, connection type, IP address, netmask, gateway, DNS, MTU, status, etc.
- **Dial-up** includes connection type, IP address, netmask, gateway, DNS, MTU, status, and connection time.
- **LAN** includes connection type, MAC address, IP address, netmask, gateway, MTU, and DNS.

#### 4.8.8 Device Manager

From the navigation tree, select 【Status】→【Device Manager】, then enter the "Device Manager" page to check the connection status between the router and Device Manager.

#### 4.8.9 Route Table

From the navigation tree, select 【Status】→【Route Table】, then enter the "Route Table" page to see router status.

This page displays the active route table, including destination, netmask, gateway, metric, and interface.

#### 4.8.10 Device List

From the navigation tree, select 【Status】→【Device List】, then enter the "Device List" page to inquire the device list.

This page displays the device list, including interface, MAC address, IP address, host, and lease (click MAC address to link to IEEE to inquire validity of the address).

#### 4.8.11 Log

From the navigation tree, select 【Status】→【Log】, then enter the "Log" page.

This page displays the logs, including selecting the number of log lines to view (20/50/....../all), log level (information, debug, and warning), time, module, and content. Users can clear logs, download log files, and download system diagnosis records (refresh rate of this page is 5/10/…... 1min by default).

#### 4.8.12 Third Party Software Notices

From the navigation tree, select 【Status】→【Third Party Software Notices】, then enter the "Third Party Software Notices" page to check the third party software used in the router system.

---

## Chapter 5 Typical Applications

*(Original manuscript does not contain detailed typical application cases, to be supplemented)*

### Case 1: Mobile Office Remote Access

**Scenario Description**: A small branch or mobile worker needs to access the company headquarters network securely via the Internet.

**Device Role**: The CR202-Pro acts as an edge gateway, providing cellular Internet access and establishing a VPN tunnel to the headquarters.

**Configuration Steps**:

1. Insert the SIM card and power on the CR202-Pro.
2. Configure cellular network access via 【Network】→【Cellular】.
3. Configure the VPN tunnel (IPSec/OpenVPN) via 【VPN】.
4. Verify the VPN connection status on 【Status】→【Network Connections】.

**Reference Chapters**:

- [Cellular Network Configuration](#421-cellular)
- [VPN Tunnel Configuration](#46-vpn)

---

## Appendix Troubleshooting

### 1 Network Connection Issues


| Phenomenon                              | Possible Cause                            | Troubleshooting Steps                                                                                               | Reference Chapter                                 |
| --------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Cannot access the Internet via cellular | SIM card not inserted or poorly contacted | 1. Check whether the SIM card is correctly inserted. 2. Reinsert the SIM card.                                      | [SIM Card Installation](#221-install-simuim-card) |
| Cannot access the Internet via cellular | APN parameter configuration error         | 1. Verify whether the APN parameters are correct. 2. Contact the operator to obtain the correct APN.                | [Cellular Network Configuration](#421-cellular)   |
| Cannot access the Internet via cellular | Weak or no signal                         | 1. Check whether the antenna is connected. 2. Adjust the device position.                                           | [Install Antenna](#222-install-antenna)           |
| Cannot access the Internet via WAN      | IP address configuration error            | 1. Confirm whether the WAN parameters match the ISP requirements. 2. Check the connection mode (DHCP/Static/PPPoE). | [WAN/LAN Switch](#422-wanlan-switch)              |
| Backup link does not switch             | ICMP detection server unreachable         | 1. Verify the ICMP detection server address. 2. Check whether the primary link can access the Internet.             | [Link Backup](#427-link-backup)                   |


### 2 Web Access Issues


| Phenomenon                    | Possible Cause              | Troubleshooting Steps                                                                              | Reference Chapter                                                  |
| ----------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Cannot open the Web interface | IP address error            | 1. Confirm the PC and device are in the same subnet. 2. Check the device default IP (192.168.2.1). | [Log In to Web Interface](#224-log-in-to-the-router-web-interface) |
| Cannot open the Web interface | Browser compatibility issue | 1. Change the browser (Chrome is recommended). 2. Clear the browser cache.                         | [Log In to Web Interface](#224-log-in-to-the-router-web-interface) |
| Forgot the login password     | Password lost               | Restore the device to factory default settings via the RESET button.                               | [Restore Factory Settings](#15-restore-factory-settings)           |


### 3 Wi-Fi Issues


| Phenomenon                         | Possible Cause             | Troubleshooting Steps                                                                         | Reference Chapter                        |
| ---------------------------------- | -------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------- |
| Cannot find the Wi-Fi signal       | SSID broadcast disabled    | 1. Log in to the Web page and check the SSID broadcast setting. 2. Enable the SSID broadcast. | [WLAN AP Mode](#425-wlan-client-ap-mode) |
| Connected to Wi-Fi but no Internet | WAN/cellular not connected | 1. Check the WAN or cellular connection status. 2. Verify the upstream network is normal.     | [Cellular Network](#421-cellular)        |


### 4 VPN Issues


| Phenomenon                                       | Possible Cause                         | Troubleshooting Steps                                                                                   | Reference Chapter                   |
| ------------------------------------------------ | -------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| VPN tunnel cannot be established                 | Server address or authentication error | 1. Verify the server address and port. 2. Check the authentication parameters (shared key/certificate). | [IPSec Tunnels](#462-ipsec-tunnels) |
| VPN connected but cannot access remote resources | Routing or firewall issue              | 1. Check the static route configuration. 2. Verify the firewall filtering rules.                        | [Static Route](#429-static-route)   |


### 5 Device Operation Issues


| Phenomenon                      | Possible Cause                    | Troubleshooting Steps                                                                                                                                                                                     | Reference Chapter                 |
| ------------------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| Device frequently auto-restarts | Module abnormal or power unstable | 1. Check whether the module works normally. 2. Check whether the power supply voltage is normal. 3. Check the SIM card and signal status.                                                                 | [Cellular Network](#421-cellular) |
| Firmware upgrade fails          | Network issue or wrong file       | 1. When upgrading locally, check whether the PC and router are in the same network segment. 2. When upgrading remotely, ensure the router can access the Internet. 3. Verify the upgrade file is correct. | [Upgrade](#417-upgrade)           |


---

## Appendix Safety Precautions

1. The device should be used within the specified temperature and humidity range.
2. Do not use the device in flammable or explosive environments.
3. Before connecting the power supply, confirm that the voltage complies with the device specifications.
4. Do not use or leave the device near a heat source such as fire or a heater.
5. Do not use or leave the device under blazing sun or in a heated car by sunshine.
6. Do not short circuit, over-charge, or over-discharge the built-in battery.
7. Do not immerse the device or battery in water or seawater. Please place it in a cool and dry environment when not in use.
8. Do not reverse the positive and negative terminals of the power supply.
9. Do not disassemble or modify the device or cell.
10. Do not transport and store the battery together with metal objects such as necklaces, hairpins, or coins.
11. Do not use the cell with conspicuous damage or deformation.
12. Do not connect the cell to an electrical outlet directly.
13. If the cell leaks and the electrolyte gets into the eyes, do not wipe the eyes. Instead, thoroughly rinse the eyes with clean running water for at least 15 minutes, and immediately seek medical attention. Otherwise, eye injury can result.
14. Do not use lithium ion batteries and other different lithium battery models in mixture.
15. Keep the battery away from babies.
16. Do not directly solder the battery or pierce the battery with a nail or other sharp object.
17. Do not strike, throw, or trample the battery.
18. Do not bend or fold the sealing edge. Do not open or deform the folding edge. Do not fillet the end of the folding edge.
19. Being charged, use the battery charger specifically for that purpose.
20. When disposing of secondary cells, keep cells of different electrochemical systems separate from each other.
21. In case the battery terminals are dirty, clean the terminals with a dry cloth before use. Otherwise, power failure or charge failure may occur due to poor connection with the instrument.
22. If the battery gives off an odor, generates heat, becomes discolored or deformed, or in any way appears abnormal during use, recharging, or storage, immediately remove it from the device or battery charger and stop using it.
23. The battery replacement shall be done only by either the cell supplier or device supplier and never be done by the user.
24. Be aware that discharged batteries may cause fire; tape the terminals to insulate them.
25. Do not use the device in a location where electrostatic and magnetic fields are strong; otherwise, the safety devices may be damaged, causing hidden safety trouble.
26. Prohibition of use of damaged cells.

> **Warning**: Non-professionals should not open the device enclosure. Risk of electric shock.

---

## Appendix Command Line Reference

### 1 Help Command

Help commands can be obtained after entering `help` or `?` into the console. `?` can be entered at any time during the process of command input to obtain the current command or help from command parameters. Commands or parameters can be automatically complemented in case of only a command or command parameter being entered.

#### 1.1 Help

**[Command]** `Help [<cmd>]`

**[Function]** Get help from a command.

**[View]** All views

**[Parameter]**

`<cmd>` — command name

**[Example]**

- Enter:
  `help`
  Get the list of all currently available commands.
- Enter:
  `help show`
  Display all the parameters of the `show` command and usage instructions.

---

### 2 View Switchover Commands

#### 2.1 Enable

**[Command]** `Enable [15 [<password>]]`

**[Function]** Switch over to privileged user level.

**[View]** Ordinary user view.

**[Parameter]** `15` — User right limit level; currently only supports right limit 15 (super users).

`<password>` — Password corresponding to the privileged user limit level; a password input prompt will be given if not entered.

**[Example]**

Enter in ordinary user view:

`enable 123456`

Switch over to super user with the password 123456.

#### 2.2 Disable

**[Command]** `Disable`

**[Function]** Exit the privileged user level.

**[View]** Super user view, configure view

**[Parameter]** No

**[Example]**

Enter in super user view:

`disable`

Return to ordinary user view.

#### 2.3 End and !

**[Command]** `End` or `!`

**[Function]** Exit the current view and return to the last view.

**[View]** Configure view.

**[Parameter]** No

**[Example]**

Enter in configured view:

`end`

Return to super user view.

#### 2.4 Exit

**[Command]** `Exit`

**[Function]** Exit the current view and return to the last view (exit console in case that it is the ordinary user view).

**[View]** All views

**[Parameter]** No

**[Example]**

- Enter in configured view:
  `exit`
  Return to super user view.
- Enter `exit` in ordinary user view:
  `exit`
  Exit console.

---

### 3 Check System State Commands

#### 3.1 Show version

**[Command]** `Show version`

**[Function]** Display the type and version of software of the router.

**[View]** All views

**[Parameter]** No

**[Example]**

Enter:

`show version`

Display the following information:

- **Type**: display the current factory type of equipment
- **Serial number**: display the current factory serial number of equipment
- **Description**: [www.inhand.com.cn](http://www.inhand.com.cn/)
- **Current version**: display the current version of equipment
- **Current version of Bootloader**: display the current version of equipment

#### 3.2 Show system

**[Command]** `Show system`

**[Function]** Display the information of the router system.

**[View]** All views

**[Parameter]** No

**[Example]**

Enter:

`show system`

Display the following information:

Example: `00:00:38 up 0 min, load average: 0.00, 0.00, 0.00`

#### 3.3 Show clock

**[Command]** `Show clock`

**[Function]** Display the system time of the router.

**[View]** All views

**[Parameter]** No

**[Example]**

Enter:

`show clock`

Display the following information:

For example: `Sat Jan 1 00:01:28 UTC 2000`

#### 3.4 Show modem

**[Command]** `Show modem`

**[Function]** Display the MODEM state of the router.

**[View]** All views

**[Parameter]** No

**[Example]**

Enter:

`show modem`

Display the following information:

- Modem type
- State
- Manufacturer
- Product name
- Signal level
- Register state
- IMSI number
- Network Type

#### 3.5 Show log

**[Command]** `Show log [lines <n>]`

**[Function]** Display the log of the router system and display the latest 100 logs by default.

**[View]** All views

**[Parameter]**

`Lines <n>` limits the number of logs displayed, wherein `n` indicates the latest `n` logs if it is a positive integer, and indicates the earliest `n` logs if it is a negative integer, and indicates all the logs if it is 0.

**[Example]**

Enter:

`show log`

Display the latest 100 log records.

#### 3.6 Show users

**[Command]** `Show users`

**[Function]** Display the user list of the router.

**[View]** All views

**[Parameter]** No

**[Example]**

Enter:

`show users`

Displayed user list of the system is as follows:

```
User:
-------------------------------------------------
* adm
------
```

Wherein, the user marked with `*` is the super user.

#### 3.7 Show startup-config

**[Command]** `Show startup-config`

**[Function]** Display the starting device configuration of the router.

**[View]** Super user view and configuration view

**[Parameter]** No

**[Example]**

Enter:

`show startup-config`

Display the starting configuration of the system.

#### 3.8 Show running-config

**[Command]** `Show running-config`

**[Function]** Display the operational configuration of the router.

**[View]** Super user view and configuration view

**[Parameter]** No

**[Example]**

Enter:

`show running-config`

Display the operational configuration of the system.

---

### 4 Check Network Status Commands

#### 4.1 Show interface

**[Command]** `Show interface`

**[Function]** Display the information of the port state of the router.

**[View]** All views

**[Parameter]** No

**[Example]**

Enter:

`show interface`

Display the state of all ports.

#### 4.2 Show ip

**[Command]** `Show ip`

**[Function]** Display the IP status of the router.

**[View]** All views

**[Parameter]** No

**[Example]**

Enter:

`show ip`

Display system IP status.

#### 4.3 Show route

**[Command]** `Show route`

**[Function]** Display the routing list of the router.

**[View]** All views

**[Parameter]** No

**[Example]**

Enter:

`show route`

Display the routing list of the system.

#### 4.4 Show arp

**[Command]** `Show arp`

**[Function]** Display the ARP list of the router.

**[View]** All views

**[Parameter]** No

**[Example]**

Enter:

`show arp`

Display the ARP list of the system.

---

### 5 Internet Testing Commands

The router provides `ping`, `telnet`, and `traceroute` for Internet testing.

#### 5.1 Ping

**[Command]** `Ping <hostname> [count <n>] [size <n>] [source <ip>]`

**[Function]** Apply ICMP testing for an appointed mainframe.

**[View]** All views

**[Parameter]**

`<hostname>` — tests the address or domain name of the mainframe.

`count <n>` — testing times.

`size <n>` — tests the size of the data package (bytes).

`source <ip>` — IP address of appointed testing.

**[Example]**

Enter:

`ping www.g.cn`

Test [www.g.cn](http://www.g.cn) and display the testing results.

#### 5.2 Telnet

**[Command]** `Telnet <hostname> [<port>] [source <ip>]`

**[Function]** Telnet logs in to the appointed mainframe.

**[View]** All views

**[Parameter]**

`<hostname>` — address or domain name of the mainframe to be logged in to.

`<port>` — telnet port.

`source <ip>` — appoints the IP address of telnet login.

**[Example]**

Enter:

`telnet 192.168.2.2`

Telnet logs in to 192.168.2.2.

#### 5.3 Traceroute

**[Command]** `Traceroute <hostname> [maxhops <n>] [timeout <n>]`

**[Function]** Test the acting routing of an appointed mainframe.

**[View]** All views

**[Parameter]**

`<hostname>` — tests the address or domain name of the mainframe.

`maxhops <n>` — tests the maximum routing jumps.

`timeout <n>` — timeout of each jumping testing (seconds).

**[Example]**

Enter:

`traceroute www.g.cn`

Apply the routing of [www.g.cn](http://www.g.cn) and display the testing results.

---

### 6 Configuration Commands

In super user view, the router can use the `configure` command to switch over to the configure view for management.

Some setting commands can support `no` and `default`, wherein `no` indicates the setting of canceling some parameter and `default` indicates the recovery of the default setting of some parameter.

#### 6.1 Configure

**[Command]** `Configure terminal`

**[Function]** Switch over to the configuration view and input the equipment at the terminal end.

**[View]** Super user view

**[Parameter]** No

**[Example]**

Enter in super user view:

`configure terminal`

Switch over to the configuration view.

#### 6.2 Hostname

**[Command]** `Hostname [<hostname>]` / `default hostname`

**[Function]** Display or set the mainframe name of the router.

**[View]** Configure view.

**[Parameter]**

`<hostname>` — new mainframe name.

**[Example]**

- Enter in configured view:
  `hostname`
  Display the mainframe name of the router.
- Enter in configured view:
  `hostname MyRouter`
  Set the mainframe name of the router to MyRouter.
- Enter in configured view:
  `default hostname`
  Recover the mainframe name of the router to the factory setting.

#### 6.3 Clock timezone

**[Command]** `Clock timezone <timezone><n>` / `default clock timezone`

**[Function]** Set the time zone information of the router.

**[View]** Configure view.

**[Parameter]**

`<timezone>` — timezone name, 3 capitalized English letters.

`<n>` — time zone deviation value, -12 ~ +12.

**[Example]**

- Enter in configured view:
  `clock timezone CST -8`
  The time zone of the router is east eighth area and the name is CST (China Standard Time).
- Enter in configured view:
  `default clock timezone`
  Recover the timezone of the router to the factory setting.

#### 6.4 Ntp server

**[Command]**

`ntp server <hostname>`

`no ntp server`

`default ntp server`

**[Function]** Set the client of the Internet time server.

**[View]** Configure view.

**[Parameter]**

`<hostname>` — address or domain name of the time server mainframe.

**[Example]**

- Enter in configured view:
  `ntp server pool.ntp.org`
  Set the address of the Internet time server pool.ntp.org.
- Enter in configured view:
  `no ntp server`
  Disable the router from getting system time via the network.
- Enter in configured view:
  `default ntp server`
  Recover the network time server of the router to the factory setting.

#### 6.5 Config export

**[Command]** `Config export`

**[Function]** Export config.

**[View]** Configure view.

**[Parameter]** No

**[Example]**

Enter in configured view:

`config export`

The current config is exported.

#### 6.6 Config import

**[Command]** `Config import`

**[Function]** Import config.

**[View]** Configure view.

**[Parameter]** No

**[Example]**

Enter in configured view:

`config import`

The config is imported.

---

### 7 System Management Commands

#### 7.1 Reboot

**[Command]** `Reboot`

**[Function]** System restarts.

**[View]** Super user view and configuration view

**[Parameter]** No

**[Example]**

Enter in super user view:

`reboot`

System restarts.

#### 7.2 Enable username

**[Command]** `Enable password [<name>]`

**[Function]** Modify the username of the super user.

**[View]** Configure view.

**[Parameter]**

`<name>` — new super user username.

**[Example]**

Enter in configured view:

`enable username admin`

The username of the super user is changed to admin.

#### 7.3 Enable password

**[Command]** `Enable password [<password>]`

**[Function]** Modify the password of the super user.

**[View]** Configure view.

**[Parameter]**

`<password>` — new super user password.

**[Example]**

- Enter in configured view:
  `enable password`
  Enter the password according to the prompt.

---

## FAQ

### Question 1: The router is powered on, but cannot access the Internet through it?

1. Check whether the router is inserted with a SIM card.
2. Check whether the SIM card is enabled with data service and whether the service of the SIM card is suspended because of an overdue charge.
3. Check whether the dial-up parameters, e.g., APN, dial-up number, username, and password are correctly configured.
4. Check whether the IP Address of the computer is in the same subnet with the router and whether the gateway address is the router LAN address.

### Question 2: The router is powered on, have a ping to detect the router from the PC and find packet loss?

1. Check whether the network crossover cable is in good condition.

### Question 3: Forgot the setting after revising the IP address and cannot configure the router?

Try the following method to restore the device:

1. Press the RESET button immediately after powering on the device.
2. When the System LED is steady on, release the RESET button; the system LED will blink, and press the RESET button again.
3. When the System LED blinks slowly, release the RESET button. The device has been restored to default settings and will start up normally later.

### Question 4: After the router is powered on, it frequently auto-restarts. Why does this happen?

1. Check whether the module works normally.
2. Check whether the router is inserted with a SIM card.
3. Check whether the SIM card is enabled with data service and whether the service of the SIM card is suspended because of an overdue charge.
4. Check whether the dial-up parameters, e.g., APN, dial-up number, username, and password are correctly configured.
5. Check whether the signal is normal.
6. Check whether the power supply voltage is normal.

### Question 5: Why does upgrading the firmware of the router always fail?

1. When upgrading locally, check whether the local PC and router are in the same network segment.
2. When upgrading remotely, first make sure the router can access the Internet.

### Question 6: After the router establishes a VPN with the VPN server, the PC under the router can connect to the server, but the center cannot connect to the PC under the router?

1. Make sure the firewall of the computer is disabled.

### Question 7: After the router establishes a VPN with the VPN server, the PC under the router cannot connect to the server ping?

1. Make sure "Shared Connection" on "Network => WAN" or "Network => Dial-up" is enabled in the configuration of the router.

### Question 8: The router is powered on, but the Power LED is not on?

1. Check whether the protective tube is burned out.
2. Check the power supply voltage range and whether the positive and negative electrodes are correctly connected.

### Question 9: The router is powered on, but the Network LED is not on when connected to the PC?

1. When the PC and router are connected with a network cable, check whether a network crossover cable is used.
2. Check whether the network cable is in good condition.
3. Set the network card of the PC to 10/100M and full duplex.

### Question 10: The router is powered on, when connected with the PC, the Network LED is normal but cannot have a ping detection to the router?

1. Check whether the IP Address of the PC and router are in the same subnet and whether the gateway address is the router LAN address.

### Question 11: The router is powered on, but cannot be configured through the web interface?

1. Check whether the IP Address of the computer is in the same subnet with the router and whether the gateway address is the router LAN address.
2. Check the firewall settings of the PC used to configure the router; whether this function is shielded by the firewall.
3. Check whether the browser has any third-party plugin. It is recommended to configure after unloading the plugin.

### Question 12: The router dial-up always fails, cannot find out why?

1. Restore the router to factory default settings and configure the parameters again.

### Question 13: How to restore the router to factory default settings?

To restore the device to default settings using the reset button, perform the following steps:

1. Power on the device.
2. Press and hold the **RESET** button until the **System LED** turns **yellow**, then release the button.
3. When the **System LED** starts flashing **yellow**, press and hold the **RESET** button again.
4. When the **System LED** starts flashing **green** slowly, release the **RESET** button. The device will now be restored to its default settings and will restart normally.

