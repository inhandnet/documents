# Portable Router CR202 Product User Manual

## Preface

### Declaration

Thank you for choosing our product. Before using the product, read this manual carefully. Observing the following statements will help maintain intellectual property rights and legal compliance, and ensure that the usage experience is consistent with the latest product information. If there are any questions or if a written license is required, contact the technical support team at any time.

- **Copyright Statement**

The contents of this user manual are protected by copyright and are the property of Beijing InHand Network Technology Co., Ltd. and its licensors. No part or all of this manual may be excerpted, copied, or distributed in any form without written permission.

- **Disclaimer**

Due to continuous product technology and specification updates, the company cannot guarantee that the information in this manual is completely consistent with the actual product. Therefore, the company does not assume any disputes arising from inconsistencies between actual technical parameters and this manual. Any product changes will not be notified in advance. The company reserves the right of final change and interpretation.

- **Copyright Information**

The contents of this user manual are protected by copyright law. The copyright belongs to Beijing InHand Network Technology Co., Ltd. and its licensors. All rights reserved. No part of this manual may be used, copied, or distributed without written permission.

### GUI Conventions


| Symbol | Meaning                                                               | Example                                                            |
| ------ | --------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `< >`  | Indicates a variable or parameter to be replaced with an actual value | `<IP Address>` indicates a specific IP address needs to be entered |
| `" "`  | Indicates text labels on the interface                                | Click the "Save" button                                            |
| `→`    | Indicates menu hierarchy or operation sequence                        | 【Network】→【Cellular】                                               |
| `【 】`  | Indicates a menu or page name                                         | Enter the 【System Settings】page                                    |
|        | Reminds the user to pay attention to matters during operation         | -                                                                  |
|        | Reminds the user of important warnings                                | -                                                                  |


### Technical Support
Email: support@inhandnetworks.com

URL: www.inhand.com

### How to Use This Manual

**Find Your Starting Point**

- **First-time users**: It is recommended to read in sequence: [Device Overview](#chapter-1-device-overview) → [Installation and First Use](#chapter-2-installation-and-first-use) → [Common Scenario Configuration](#chapter-3-common-scenario-configuration) → [Feature Description and Parameter Reference](#chapter-4-feature-description-and-parameter-reference)
- **Existing device users**: Refer directly to [Feature Description and Parameter Reference](#chapter-4-feature-description-and-parameter-reference) or [Appendix Troubleshooting](#appendix-troubleshooting)
- **Cloud platform management users**: Refer to [Common Scenario Configuration](#chapter-3-common-scenario-configuration) for device remote management platform content

**Quick Task Navigation**


| Task                                        | Corresponding Chapter                                                                                 | Estimated Time   |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------- |
| Understand device appearance and interfaces | [Device Overview](#chapter-1-device-overview)                                                         | About 5 minutes  |
| Complete device installation and power-on   | [Installation and First Use](#chapter-2-installation-and-first-use)                                   | About 10 minutes |
| Configure cellular network access           | [Scenario 1: Cellular Networking](#scenario-1-cellular-networking)                                    | About 5 minutes  |
| Configure Wi-Fi AP                          | [Scenario 3: Wi-Fi AP Configuration](#scenario-3-wi-fi-ap-configuration)                              | About 5 minutes  |
| Check device status and parameters          | [Feature Description and Parameter Reference](#chapter-4-feature-description-and-parameter-reference) | As needed        |
| Troubleshoot common faults                  | [Appendix Troubleshooting](#appendix-troubleshooting)                                                 | As needed        |


---

# Chapter 1 Device Overview

## 1.1 Overview

The CR202 is a portable 4G cellular router designed to provide reliable Internet connectivity for remote offices, mobile scenarios, and field applications. It supports wired-to-wireless access, increasing the diversity of network access methods and effectively ensuring network continuity. The built-in battery model enables operation anytime and anywhere, while the lightweight design allows unrestricted device mobility. Combined with the InHand Device Manager cloud management platform, the CR202 provides efficient device management capabilities, delivering high-speed network access and simplified network management services.

## 1.2 Packing List


| Item                          | Quantity | Description             |
| ----------------------------- | -------- | ----------------------- |
| CR202 Router                  | 1        | Main device             |
| Power Adapter (5V/2A, Type-C) | 1        | Power supply            |
| Cellular Antenna              | 2        | For 4G signal reception |
| User Manual                   | 1        | This document           |


## 1.3 Appearance and Interfaces



**Figure 1-1 CR202 Panel (with Battery)**

Devices without a battery do not have an ON/OFF button. The panel appearance is shown below.



**Figure 1-2 CR202 Panel (without Battery)**


| Interface                   | Position | Function Description              |
| --------------------------- | -------- | --------------------------------- |
| Type-C Power Port           | Side     | 5V/2A power input                 |
| SIM Card Slot               | Side     | nano SIM card insertion           |
| RESET Button                | Side     | Restore factory settings          |
| ON/OFF Button               | Side     | Power on/off (battery model only) |
| LAN Ports                   | Side     | Ethernet LAN interfaces           |
| WAN/LAN1 Port               | Side     | Configurable WAN or LAN interface |
| Cellular Antenna Interfaces | Side     | SMA-J antenna connectors          |


## 1.4 LED Indication

### CR202 (No Battery)


| LED     | Status           | Meaning                                              |
| ------- | ---------------- | ---------------------------------------------------- |
| System  | Off              | Power off                                            |
|         | Blink in green   | Device starting                                      |
|         | Steady in green  | Device working                                       |
|         | Blink in yellow  | Upgrading                                            |
| Network | Off              | Cellular disabled                                    |
|         | Blink in green   | Dialing up                                           |
|         | Steady in green  | Dialed successfully                                  |
|         | Blink in yellow  | Dialing abnormal                                     |
|         | Blink in red     | No SIM card, cannot read SIM card, or modem abnormal |
| Wi-Fi   | Off              | Wi-Fi disabled                                       |
|         | Blink in green   | Wi-Fi connected, data transmitting                   |
|         | Steady in green  | Wi-Fi enabled                                        |
| Signal  | Off              | Cellular disabled                                    |
|         | Steady in green  | Dialed up, signal level ≥ 20                         |
|         | Steady in yellow | Dialed up, 19 ≥ signal level ≥ 10                    |
|         | Steady in red    | Dialed up, 9 ≥ signal level                          |


### CR202 (With Battery)


| LED     | Status           | Meaning                                              |
| ------- | ---------------- | ---------------------------------------------------- |
| System  | Off              | Power off                                            |
|         | Blink in green   | Device starting                                      |
|         | Steady in green  | Device working                                       |
|         | Blink in yellow  | Upgrading                                            |
| Network | Off              | Cellular disabled                                    |
|         | Blink in green   | Dialing up                                           |
|         | Blink in yellow  | Dialing abnormal                                     |
|         | Blink in red     | No SIM card, cannot read SIM card, or modem abnormal |
|         | Steady in green  | Dialed up, signal level ≥ 20                         |
|         | Steady in yellow | Dialed up, 19 ≥ signal level ≥ 10                    |
|         | Steady in red    | Dialed up, 9 ≥ signal level                          |
| Wi-Fi   | Off              | Wi-Fi disabled                                       |
|         | Blink in green   | Wi-Fi connected, data transmitting                   |
|         | Steady in green  | Wi-Fi enabled                                        |
| Battery | Blink            | Battery charging                                     |
|         | Steady           | Battery discharging                                  |
|         | Green            | 80% < battery level ≤ 100%                           |
|         | Yellow           | 20% < battery level ≤ 80%                            |
|         | Red              | 0 < battery level ≤ 20%                              |


## 1.5 Restore Factory Settings

To restore the device to default settings using the reset button, follow these steps:

1. Power on the device.
2. Press and hold the **RESET** button until the **System LED** turns **yellow**, then release the button.
3. When the **System LED** starts flashing **yellow**, press and hold the **RESET** button again.
4. When the **System LED** starts flashing **green** slowly, release the **RESET** button. The device will now be restored to its default settings and will restart normally.

## 1.6 Default Settings


| Parameter            | Default Value               |
| -------------------- | --------------------------- |
| LAN IP Address       | 192.168.2.1                 |
| Subnet Mask          | 255.255.255.0               |
| Web Login Username   | adm                         |
| Web Login Password   | (See device nameplate)      |
| Wi-Fi SSID           | inhand                      |
| Wi-Fi Authentication | Open type                   |
| DHCP Service         | Enabled                     |
| DHCP IP Pool Range   | 192.168.2.2 ~ 192.168.2.100 |


---

# Chapter 2 Installation and First Use

## 2.1 Pre-Installation Preparation

### 2.1.1 Environment Requirements

Ensure that 3G/4G network coverage is available at the installation site. Avoid direct sunlight, heat sources, and strong electromagnetic interference. The first installation should be performed under the guidance of an engineer recognized by InHand Networks.

### 2.1.2 Tools and Materials


| Item         | Specification           | Remarks                                 |
| ------------ | ----------------------- | --------------------------------------- |
| PC           | OS: Windows 7/10/11     | At least one Ethernet port (10M/100M)   |
| SIM Card     | nano SIM                | Data service enabled, not suspended     |
| Power Supply | 5V/2A, Type-C interface | -                                       |
| Fixation     | Flat surface            | Small vibrational frequency environment |


> **Warning**: The device shall be installed and operated in a powered-off status!

> **Warning**: Do not use or leave the device at very high temperature conditions (for example, strong direct sunlight or a vehicle in extremely hot conditions). Otherwise, the built-in battery may overheat, catch fire, or its performance will degrade and its service life will decrease. Do not immerse the device in water. Store it in a cool and dry environment when not in use.

## 2.2 Installation Guide

### 2.2.1 Install SIM/UIM Card

The CR202 supports a single nano SIM card or eSIM. To install a nano SIM card, follow the steps below.



**Figure 2-1 SIM Card Installation (Step 1)**



**Figure 2-2 SIM Card Installation (Step 2)**



**Figure 2-3 SIM Card Installation (Step 3)**

### 2.2.2 Install Antenna

Slightly rotate the movable part of the metal SMA-J interface until it cannot be rotated further (at this point, the external thread of the antenna cable should not be visible). Do not forcibly screw the antenna by holding the black rubber lining.

### 2.2.3 Connect Power Supply

The CR202 supports an internal battery or Type-C interface (5V/2A). Pay attention to the power voltage level.

### 2.2.4 Log in to the Router

After hardware installation, ensure the Ethernet card has been installed in the supervisory PC before logging in to the Web settings page of the router.

**I. Automatic Acquisition of IP Address (Recommended)**

Set the supervisory computer to "automatic acquisition of IP address" and "automatic acquisition of DNS server address" (default configuration of the computer system) to let the device automatically assign an IP address to the supervisory computer.

**II. Set a Static IP Address**

Set the IP address of the supervisory PC (such as 192.168.2.2) and the LAN interface of the device in the same network segment (initial IP address of the LAN interface of the device: 192.168.2.1, subnet mask: 255.255.255.0).



**Figure 2-4 Automatic Acquisition of IP Address (Left) and Static IP Address (Right)**

**III. Cancel the Proxy Server**

If the current supervisory PC uses a proxy server to access the Internet, cancel the proxy service. The operating steps are as follows:

1. In the browser window, select "Tools >> Internet options".
2. Select the "Connections" page and click the "LAN Settings" button to enter the "LAN Settings" window.
3. Confirm whether the option "Use a Proxy Server for LAN" is checked; if checked, cancel it and click the `<OK>` button.

**IV. Log in to / Exit the Web Settings Page**

Access the default IP address 192.168.2.1 in a browser. Enter the username and password (see the nameplate at the bottom of the device for login credentials) in the pop-up window to access the router's WEB management page. If the browser alarms that the connection is not private, click "Advanced" and proceed to the address.



**Figure 2-5 Web Login Page**

> **Warning**: For security, modify the default login password after the first login and keep the password information safe.

## 2.3 Quick Check

After installation is complete, verify the following items:

- The SIM card is correctly inserted and the antenna is securely installed.
- The power supply is properly connected and the device is powered on.
- The System LED indicates that the device is working (steady green).
- The PC has obtained an IP address in the 192.168.2.x segment.
- The Web management page can be accessed via 192.168.2.1.

---

# Chapter 3 Common Scenario Configuration

## Scenario 1: Cellular Networking

**Objective**: Access the Internet via 4G cellular network.

**Prerequisites**: The SIM card has been inserted and the antenna installed; the device is powered on.

**Estimated Time**: About 5 minutes.

**Operation Steps**:

1. Insert the SIM card and install the antenna.
2. Power on the device and wait for the System LED to turn steady green.
3. Log in to the Web management page (192.168.2.1).
4. Enter the 【Network】→【Cellular】menu.
5. Configure the APN parameters (obtain the APN from the network operator).
6. Click the `<Save>` button and wait for the connection to be established.

**Verification Method**:

1. Check the LED status to confirm that the Network LED is steady green.
2. Visit any Internet website from the PC to confirm normal access.

**Common Issues**:

- Network connection failure: Check whether the SIM card is correctly inserted and whether the APN parameters are correct.
- Data transmission/reception abnormality: Check the signal strength and data balance.

## Scenario 2: Wired WAN Access

**Objective**: Access the Internet via a wired WAN connection.

**Prerequisites**: An Ethernet cable is available and connected to the upstream network device; the CR202 is powered on.

**Estimated Time**: About 5 minutes.

**Operation Steps**:

1. Connect the Ethernet cable from the upstream device to the WAN/LAN1 port of the CR202.
2. Log in to the Web management page (192.168.2.1).
3. Enter the 【Network】→【WAN/LAN Switch】menu.
4. Configure the WAN/LAN1 port as WAN.
5. Select the access type: Static IP, Dynamic Address (DHCP), or ADSL (PPPoE).
6. Enter the corresponding parameters and click the `<Save>` button.

**Verification Method**:

1. Check the Network Connections status page to confirm that the WAN interface has obtained an IP address.
2. Visit any Internet website from the PC to confirm normal access.

**Common Issues**:

- Unable to obtain an IP address: Check whether the upstream device is working properly and whether the cable connection is normal.
- PPPoE dialing failure: Verify that the username and password are correct.

## Scenario 3: Wi-Fi AP Configuration

**Objective**: Provide a wireless access point for other devices.

**Prerequisites**: The CR202 has already connected to the Internet via WAN or cellular.

**Estimated Time**: About 5 minutes.

**Operation Steps**:

1. Log in to the Web management page (192.168.2.1).
2. Ensure the WLAN mode is set to AP via 【Network】→【Switch WLAN Mode】.
3. Enter the 【Network】→【WLAN】menu.
4. Configure the SSID, authentication method, and encryption.
5. Click the `<Save>` button.
6. Reboot the device if required for the configuration to take effect.

**Verification Method**:

1. Use a wireless terminal to search for the configured SSID.
2. Connect to the SSID and confirm Internet access.

**Common Issues**:

- SSID not found: Check whether SSID broadcast is enabled.
- Connection failure: Verify that the authentication password is correct.

## Scenario 4: Wi-Fi STA Relay

**Objective**: Access the Internet by connecting the CR202 to another wireless AP.

**Prerequisites**: The target wireless AP is working normally and its SSID and password are known.

**Estimated Time**: About 5 minutes.

**Operation Steps**:

1. Log in to the Web management page (192.168.2.1).
2. Switch the WLAN mode to STA via 【Network】→【Switch WLAN Mode】 and reboot.
3. Enter the 【Network】→【WLAN Client】menu.
4. Select "Client" as the interface type.
5. Click the "Scan" button, select the target AP, and configure the corresponding parameters.
6. Configure the access type in 【Network】→【WAN(STA)】.
7. Close the cellular interface in 【Network】→【Cellular】 if necessary.

**Verification Method**:

1. Check the WLAN connection status page to confirm successful connection to the upstream AP.
2. Visit any Internet website from the PC to confirm normal access.

**Common Issues**:

- Scan result is empty: Check whether the target AP is within range.
- Connection failure: Verify that the authentication method and encryption match the upstream AP.

## Scenario 5: Device Manager Remote Management

**Objective**: Connect the CR202 to the InHand Device Manager platform for remote management.

**Prerequisites**: An account has been registered on the Device Manager platform; the device can access the Internet.

**Estimated Time**: About 5 minutes.

**Operation Steps**:

1. Log in to the Web management page (192.168.2.1).
2. Enter the 【Services】→【Device Manager】menu.
3. Enable the Device Manager function.
4. Select the server address (iot.inhand.com.cn for China, iot.inhandnetworks.com for global).
5. Enter the registered account.
6. Configure the upload intervals and keepalive parameters as needed.
7. Click the `<Save>` button.

**Verification Method**:

1. Enter the 【Status】→【Device Manager】page to check the connection status.
2. Log in to the Device Manager platform and confirm that the device is online.

**Common Issues**:

- Device is not online: Check whether the device can access the Internet and whether the account is correct.
- Connection is unstable: Adjust the keepalive interval or check the signal quality.

---

# Chapter 4 Feature Description and Parameter Reference

The device needs to be effectively configured before use. This chapter introduces how to configure the router via the Web interface and describes the function and parameters of each module.

## 4.1 System

### 4.1.1 Basic Setup

This function is used to check and configure the system time, router WEB configuration interface, language, and router name.

From the navigation tree, select 【System】→【Basic Setup】, then enter the "Basic Setup" page.

**Table 4-1-1 Basic Setup Parameters**


| Parameters | Description                                                           | Default |
| ---------- | --------------------------------------------------------------------- | ------- |
| Language   | Configure the language of the WEB configuration interface             | English |
| Host Name  | Set a name for the host or device connected to the router for viewing | Router  |


### 4.1.2 System Time

To ensure coordination between this device and other devices, it is required to set the system time accurately. This function is used to configure and check the system time and system time zone.

From the navigation tree, select 【System】→【Time】, then enter the "Time" webpage. Click `<Sync Time>` to synchronize the router time with the PC system time.

**Table 4-1-2 System Time Parameters**


| Parameters       | Description                                                                     | Default                |
| ---------------- | ------------------------------------------------------------------------------- | ---------------------- |
| Time of Router   | Display the present time of the router                                          | 8:00:00 AM, 12/12/2015 |
| PC Time          | Display the present time of the PC                                              | Present time           |
| Timezone         | Set the time zone of the router                                                 | Custom                 |
| Custom TZ String | Set the TZ string of the router                                                 | CST-8                  |
| Auto update Time | Select whether to automatically update time (on startup or every 1/2/... hours) | On startup             |
| NTP Time Servers | Select the NTP server to synchronize time                                       | 1.pool.ntp.org         |


### 4.1.3 Admin Access

Admin services include HTTP, HTTPS, TELNET, and SSHD.

- **HTTP**: Hypertext Transfer Protocol, used for transferring web pages on the Internet.
- **HTTPS**: Secure Hypertext Transfer Protocol, the secure version of HTTP supporting the SSL protocol.
- **TELNET**: Provides telnet and virtual terminal functions through a network. The device supports Telnet Client and Telnet Server.
- **SSHD**: SSH protocol provides security for remote login sessions and other network services. SSHD has higher security than Telnet.

From the navigation tree, select 【System】→【Admin Access】, then enter the "Admin Access" page.

**Table 4-1-3 Admin Access Parameters**


| Parameters                         | Description                                                                                                                                                             | Default                                                                                     |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Username/Password**              |                                                                                                                                                                         |                                                                                             |
| Username                           | Set the name of the user who logs in to the WEB configuration page                                                                                                      | adm                                                                                         |
| Old Password                       | Previous password to access the WEB configuration page                                                                                                                  | -                                                                                           |
| New Password                       | New password to access the WEB configuration page                                                                                                                       | N/A                                                                                         |
| Confirm New Password               | Reconfirm the new password                                                                                                                                              | N/A                                                                                         |
| **Admin functions**                |                                                                                                                                                                         |                                                                                             |
| Service Port                       | Service port of HTTP/HTTPS/TELNET/SSHD                                                                                                                                  | 80/443/23/22                                                                                |
| Local Access                       | Enable — Allow the local LAN to administer the router with the corresponding service; Disable — Local LAN cannot administer the router with the corresponding service   | Enable                                                                                      |
| Remote Access                      | Enable — Allow a remote host to administer the router with the corresponding service; Disable — Remote host cannot administer the router with the corresponding service | Enable                                                                                      |
| Allowed Access from WAN (Optional) | Set allowed access from WAN                                                                                                                                             | Set the hosts allowed to access the router, e.g. 192.168.2.1/30 or 192.168.2.1-192.168.2.10 |
| Description                        | For recording the significance of various parameters of admin functions (without influencing router configuration)                                                      | N/A                                                                                         |
| **Non-privileged users**           |                                                                                                                                                                         |                                                                                             |
| Username                           | Configure the non-privileged login user name                                                                                                                            | N/A                                                                                         |
| Password                           | Configure the password of the non-privileged user                                                                                                                       | N/A                                                                                         |
| **Other Parameters**               |                                                                                                                                                                         |                                                                                             |
| Log Timeout                        | Set the login timeout (the router will automatically disconnect the configuration interface after the login timeout)                                                    | 500 seconds                                                                                 |


### 4.1.4 System Log

A remote log server can be set through "System Log", and all system logs will be uploaded to the remote log server through the Internet. This requires remote log software (such as Kiwi Syslog Daemon) on the remote log server.

From the navigation tree, select 【System】→【System Log】, then enter the "System Log" page.

**Table 4-1-4 System Log Parameters**


| Parameters                        | Description                                       | Default  |
| --------------------------------- | ------------------------------------------------- | -------- |
| Log to Remote System              | Enable log server                                 | Disable  |
| Log server address and port (UDP) | Set the address and port of the remote log server | N/A: 514 |


### 4.1.5 Configuration Management

Here the configuration parameters can be backed up, the desired parameter backup can be imported, and the router can be reset.

From the navigation tree, select 【System】→【Config Management】, then enter the "Config Management" page.

**Table 4-1-5 Configuration Management Parameters**


| Parameters                        | Description                                                                                         | Default |
| --------------------------------- | --------------------------------------------------------------------------------------------------- | ------- |
| Browse                            | Choose the configuration file                                                                       | N/A     |
| Import                            | Import the configuration file to the router                                                         | N/A     |
| Backup                            | Backup the configuration file to the host                                                           | N/A     |
| Restore default configuration     | Select to restore the default configuration (effective after rebooting)                             | N/A     |
| Disable the hardware reset button | Select to disable the hardware reset button of the router                                           | Disable |
| Network Provider (ISP)            | For configuring APN, username, password, and other parameters of network providers across the world | N/A     |


>  **Warning**: The validity and order of imported configurations should be ensured. Acceptable configurations will be serially executed in order after system reboot. If the configuration files are not arranged according to the effective order, the system will not enter the desired state.

>  **Note**: In order not to affect the operation of the current system, after performing an import configuration or restoring the default configuration, restart the device to make the new configuration take effect.

### 4.1.6 Scheduler

After this function is enabled, the device will reboot at the scheduled time. The scheduler function will take effect after the router synchronizes time.

From the navigation tree, select 【System】→【Scheduler】, then enter the "Scheduler" page.

**Table 4-1-6 Scheduler Parameters**


| Parameters            | Description                                                                                                                                                                             | Default  |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Enable                | Enable/disable this function                                                                                                                                                            | Disable  |
| Time                  | Select the reboot time                                                                                                                                                                  | 0:00     |
| Days                  | Reboot the router every day                                                                                                                                                             | Everyday |
| Show advanced options | Enable more detailed schedule rules, allowing multiple rules to reboot the router at a specific time or interval. Enabling this feature will disable the everyday reboot feature above. | Disable  |
| Reboot after dialed   | The router will reboot after dial-up successfully. Will not take effect if this parameter is blank.                                                                                     | N/A      |


### 4.1.7 Upgrade

The upgrading process can be divided into two steps. In the first step, firmware will be written to the backup file zone. In the second step, firmware in the backup file zone will be copied to the main firmware zone, which should be carried out during system restart. During software upgrading, any operation on the web page is not allowed, otherwise the software upgrading may be interrupted.

From the navigation tree, select 【System】→【Upgrade】, then enter the "Upgrade" page.

To upgrade the system: firstly, click `<Browse>` to choose the upgrade file; secondly, click `<Upgrade>` and then click `<OK>` to begin the upgrade; thirdly, after the firmware upgrade succeeds, click `<Reboot>` to restart the device.

### 4.1.8 Reboot

Save the configurations before rebooting, otherwise the configurations that are not saved will be lost after the reboot.

To reboot the system, click 【System】→【Reboot】, then click `<OK>`.

### 4.1.9 Logout

To log out, click 【System】→【Logout】, and then click `<OK>`.

## 4.2 Network

### 4.2.1 Cellular

Insert a SIM card and dial up to achieve the wireless network connection.

Click 【Network】→【Cellular】 in the navigation tree to enter the Cellular configuration page.

**Table 4-2-1-1 Cellular Parameters**


| Parameters                | Description                                                                                                                                                                                                                                                                                                              | Default        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| Enable                    | Enable cellular dial-up                                                                                                                                                                                                                                                                                                  | Enable         |
| Time Schedule             | Set the time schedule                                                                                                                                                                                                                                                                                                    | ALL            |
| Force Reboot              | The router will reboot if it cannot dial up for a long time and reaches the max retry time                                                                                                                                                                                                                               | Enable         |
| Shared connection (NAT)   | Enable — Local devices connected to the router can access the Internet via the router; Disable — Local devices connected to the router cannot access the Internet via the router                                                                                                                                         | Enable         |
| Default Route             | Enable default route                                                                                                                                                                                                                                                                                                     | Enable         |
| SIM Network Provider      | Select the network provider for the inserted SIM card                                                                                                                                                                                                                                                                    | Profile 1      |
| Network Select Type       | Select the network type. The router will try 4G, 3G, 2G in proper order if Auto is selected                                                                                                                                                                                                                              | Auto           |
| Connection Mode           | Optional: Always Online, Connect On Demand, Manual. Supports configuring Triggered by SMS if Connect On Demand mode is selected                                                                                                                                                                                          | Always Online  |
| Redial Interval           | Set the redialing time when dial-up fails                                                                                                                                                                                                                                                                                | 30 s           |
| **Show Advanced Options** |                                                                                                                                                                                                                                                                                                                          |                |
| Dual SIM Enable           | Some CR202 types support eSIM. Enable this option to enable eSIM dial-up                                                                                                                                                                                                                                                 | Disable        |
| eSIM Network Provider     | Select the network provider for the eSIM card                                                                                                                                                                                                                                                                            | Profile 1      |
| eSIM Blinding ICCID       | Set the ICCID of the eSIM                                                                                                                                                                                                                                                                                                | N/A            |
| eSIM PIN Code             | For setting the eSIM PIN code                                                                                                                                                                                                                                                                                            | N/A            |
| eSIM SIM Card Operator    | Set the ISP that the eSIM card connects to                                                                                                                                                                                                                                                                               | Auto           |
| Main SIM                  | Set the SIM card that is used to dial up first                                                                                                                                                                                                                                                                           | SIM            |
| Max Number of Dial        | Set the max number of dial attempts. If dial-up is not successful after this number, the router will switch the SIM card                                                                                                                                                                                                 | 5              |
| CSQ Threshold             | Set the threshold of signal. If the current signal level is lower than this, the router will switch the SIM card                                                                                                                                                                                                         | 0 (Disable)    |
| Min Connect Time          | Set the minimum connect time for each dial-up attempt                                                                                                                                                                                                                                                                    | 0 (Disable)    |
| Initial Commands          | Set customized initial AT commands which will be operated at the beginning of dialing up                                                                                                                                                                                                                                 | AT             |
| Blinding ICCID            | Set the ICCID of the SIM                                                                                                                                                                                                                                                                                                 | N/A            |
| PIN Code                  | For setting the PIN code of the SIM                                                                                                                                                                                                                                                                                      | N/A            |
| Static MTU                | Set the max transmission unit after enabling                                                                                                                                                                                                                                                                             | Disable        |
| Use Peer DNS              | Click to receive peer DNS assigned by the ISP                                                                                                                                                                                                                                                                            | Enable         |
| Link detection interval   | Set the link detection interval                                                                                                                                                                                                                                                                                          | 55 s           |
| Debug                     | Enable debug mode, print debug log in the system log                                                                                                                                                                                                                                                                     | Disable        |
| ICMP Detection Mode       | Set the ICMP detection mode. The router will check the link connection status via ICMP packet. Ignore Traffic: The router will send ICMP packets regardless of whether there is traffic in the cellular interface. Monitor Traffic: The router will not send ICMP packets if there is traffic in the cellular interface. | Ignore Traffic |
| ICMP Detection Server     | Set the ICMP Detection Server. N/A means not to enable ICMP detection.                                                                                                                                                                                                                                                   | N/A            |
| ICMP Detection Interval   | Set the ICMP Detection Interval                                                                                                                                                                                                                                                                                          | 30 s           |
| ICMP Detection Timeout    | Set the ICMP Detection Timeout (the link will be regarded as down if ICMP times out)                                                                                                                                                                                                                                     | 20 s           |
| ICMP Detection Retries    | Set the max number of retries if ICMP fails (the router will redial if reaching the max times)                                                                                                                                                                                                                           | 5              |


**Table 4-2-1-2 Cellular Schedule Parameters**


| Parameters        | Description                 | Default     |
| ----------------- | --------------------------- | ----------- |
| Name              | Name of the schedule        | Schedule_1  |
| Sunday ~ Saturday | Click to enable             | -           |
| Time Range 1      | Set time range 1            | 9:00-12:00  |
| Time Range 2      | Set time range 2            | 14:00-18:00 |
| Time Range 3      | Set time range 3            | 0:00-0:00   |
| Description       | Set the description content | N/A         |


### 4.2.2 WAN/LAN Switch

Click 【Network】→【WAN/LAN Switch】 to set the WAN/LAN1 port.

When this port is configured as WAN, the CR202 supports three types of wired access: static IP, dynamic address (DHCP), and ADSL (PPPoE) dialing. When this port is configured as LAN, it supports jumping to the LAN configuration page via the Settings button on the right of the select box.

DHCP adopts a Client/Server communication mode. The Client sends a configuration request to the Server, which feeds back the corresponding configuration information, including the distributed IP address to the Client, to achieve dynamic configuration of the IP address and other information.

PPPoE is a point-to-point protocol over Ethernet. The user has to install a PPPoE Client on the basis of the original connection way. Through PPPoE, remote access devices can achieve control and charging of each accessed user.

WAN/LAN1 is working as LAN by default.

**Table 4-2-2-1 WAN Static IP Parameters**


| Parameters                                                             | Description                                                                                                                                                                      | Default              |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Shared connection (NAT)                                                | Enable — Local devices connected to the router can access the Internet via the router; Disable — Local devices connected to the router cannot access the Internet via the router | Enable               |
| Default route                                                          | Enable default route                                                                                                                                                             | Enable               |
| MAC Address                                                            | MAC address of the device                                                                                                                                                        | Device's MAC address |
| IP Address                                                             | Set the IP address of WAN                                                                                                                                                        | 192.168.1.29         |
| Netmask                                                                | Set the subnet mask of WAN                                                                                                                                                       | 255.255.255.0        |
| Gateway                                                                | Set the gateway of WAN                                                                                                                                                           | 192.168.1.1          |
| MTU                                                                    | Max transmission unit, default/manual settings                                                                                                                                   | default (1500)       |
| **Multiple IP support (at most 8 additional IP addresses can be set)** |                                                                                                                                                                                  |                      |
| IP Address                                                             | Set the additional IP address of LAN                                                                                                                                             | N/A                  |
| Subnet mask                                                            | Set the subnet mask                                                                                                                                                              | N/A                  |
| Description                                                            | For recording the significance of the additional IP address                                                                                                                      | N/A                  |


**Table 4-2-2-2 WAN Dynamic Address (DHCP) Parameters**


| Parameters              | Description                                                                                                                                                                      | Default              |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Shared connection (NAT) | Enable — Local devices connected to the router can access the Internet via the router; Disable — Local devices connected to the router cannot access the Internet via the router | Enable               |
| Default route           | Enable default route                                                                                                                                                             | Enable               |
| MAC Address             | MAC address of the device                                                                                                                                                        | Device's MAC address |
| MTU                     | Max transmission unit, default/manual settings                                                                                                                                   | default (1500)       |


**Table 4-2-2-3WAN ADSL Dialing (PPPoE) Parameters**


| Parameters                         | Description                                                                                                                                                                      | Default              |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Shared connection                  | Enable — Local devices connected to the router can access the Internet via the router; Disable — Local devices connected to the router cannot access the Internet via the router | Enable               |
| Default route                      | Enable default route                                                                                                                                                             | Enable               |
| MAC Address                        | MAC address of the device                                                                                                                                                        | Device's MAC address |
| MTU                                | Max transmission unit, default/manual settings                                                                                                                                   | default (1492)       |
| **WAN - ADSL Dialing (PPPoE)**     |                                                                                                                                                                                  |                      |
| Username                           | Set the name of the dialing user                                                                                                                                                 | N/A                  |
| Password                           | Set the dialing password                                                                                                                                                         | N/A                  |
| Static IP                          | Click to enable and configure static IP                                                                                                                                          | Disable              |
| Connection Mode                    | Set the dialing connection method (always online, dial on demand, manual dialing)                                                                                                | Always online        |
| **Parameters of Advanced Options** |                                                                                                                                                                                  |                      |
| Service Name                       | Set the service name                                                                                                                                                             | N/A                  |
| TX Queue Length                    | Set the length of the transmit queue                                                                                                                                             | 3                    |
| Enable IP header compression       | Click to enable IP header compression                                                                                                                                            | Disable              |
| Use Peer DNS                       | Click to enable use peer DNS                                                                                                                                                     | Enable               |
| Link detection interval            | Set the link detection interval                                                                                                                                                  | 55 s                 |
| Link detection Max. Retries        | Set the link detection max retries                                                                                                                                               | 10                   |
| Debug                              | Click to enable debug mode                                                                                                                                                       | Disable              |
| Expert Option                      | Set expert options                                                                                                                                                               | N/A                  |
| ICMP Detection Server              | Set the ICMP detection server. Blank means disable ICMP detection feature.                                                                                                       | N/A                  |
| ICMP Detection Interval            | Set the ICMP Detection Interval                                                                                                                                                  | 30 s                 |
| ICMP Detection Timeout             | Set the ICMP detection timeout                                                                                                                                                   | 20 s                 |
| ICMP Detection Retries             | Set the ICMP detection max retries                                                                                                                                               | 3                    |


### 4.2.3 LAN

Click 【Network】→【LAN】 to configure the LAN interface of the router so that other devices can access the Internet via an Ethernet cable in the LAN.

**Table 4-2-3 LAN Parameters**


| Parameters                                                           | Description                                                     | Default                  |
| -------------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------ |
| MAC Address                                                          | MAC address of the router's LAN gateway                         | Router's LAN MAC address |
| IP Address                                                           | IP address of the router's LAN gateway                          | 192.168.2.1              |
| Netmask                                                              | Subnet mask of the LAN gateway                                  | 255.255.255.0            |
| MTU                                                                  | Max transmission unit, default/manual settings                  | default (1500)           |
| LAN Mode                                                             | Set the transport mode in the LAN interface                     | Auto Negotiation         |
| **Multi-IP Settings (at most 8 additional IP addresses can be set)** |                                                                 |                          |
| IP Address                                                           | Set the additional IP address of LAN                            | N/A                      |
| Subnet mask                                                          | Set the subnet mask                                             | N/A                      |
| Description                                                          | For recording the significance of the additional IP address     | N/A                      |
| **LAN Port Enable**                                                  |                                                                 |                          |
| port1/port2                                                          | Enable the corresponding LAN port                               | Enable                   |
| **GARP**                                                             |                                                                 |                          |
| Enable                                                               | The router will send ARP broadcast to LAN devices automatically | Disable                  |
| Broadcast Count                                                      | Set the ARP broadcast times                                     | 5                        |
| Broadcast Timeout                                                    | Set the ARP broadcast timeout time                              | 10                       |


### 4.2.4 Switch WLAN Mode

The CR202 supports two types of WLAN mode: AP and STA.

Click the 【Network】→【Switch WLAN Mode】 menu in the navigation tree to set the WLAN mode of the router. After changing and saving the configuration, reboot the device to make the configuration take effect.

### 4.2.5 WLAN Client (AP Mode)

When working in AP mode, the CR202 WLAN will provide a network access point for other wireless network devices. Ensure that the CR202 has already connected to the Internet via WAN or cellular.

Click the 【Network】→【WLAN】 menu in the navigation tree to enter the "WLAN" interface.

**Table 4-2-5 WLAN AP Mode Parameters**


| Parameters            | Description                                                                                                    | Default                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| SSID broadcast        | After turning on, users can search for the WLAN via the SSID name                                              | Enable                       |
| Mode                  | Six types for options: 802.11g/n, 802.11g, 802.11n, 802.11b, 802.11b/g, 802.11b/g/n                            | 802.11b/g/n                  |
| Channel               | Select the channel                                                                                             | 11                           |
| SSID                  | SSID name defined by the user                                                                                  | Refer to equipment nameplate |
| Authentication method | Supports open type, shared type, auto selection of WEP, WPA-PSK, WPA, WPA2-PSK, WPA2, WPA/WPA2, WPAPSK/WPA2PSK | Refer to equipment nameplate |
| Encryption            | Supports NONE, WEP                                                                                             | NONE                         |
| Wireless bandwidth    | Both 20MHz and 40MHz for selection                                                                             | 20MHz                        |
| Enable WDS            | Click to enable WDS                                                                                            | Disable                      |
| Default Route         | Click to enable Route                                                                                          | Disable                      |
| Bridged SSID          | Set the bridged SSID                                                                                           | None                         |
| Bridged BSSID         | Set the bridged BSSID                                                                                          | None                         |
| Scan                  | Click "Scan" to scan available APs nearby                                                                      | -                            |
| Auth Mode             | Open type, shared type, WPA-PSK, WPA2-PSK                                                                      | Refer to equipment nameplate |
| Encryption Method     | Supports NONE, WEP                                                                                             | None                         |


### 4.2.6 WLAN Client (STA Mode)

When working in STA mode, the router can access the Internet by connecting to another AP.

Click the 【Network】→【WLAN Client】 menu in the navigation tree to enter the "WLAN" interface. Select "Client" for the interface type and configure the relevant parameters. (At this moment, the cellular interface in 【Network】→【Cellular】 should be closed.)

The SSID scan function is enabled only when Client is selected as the WLAN interface. Click the "Scan" button to get all available APs and their status, select an AP, and configure the corresponding parameters to connect. After configuring the WLAN Client, configure the access type in 【Network】→【WAN(STA)】.

**Table 4-2-6 WLAN Client Parameters**


| Parameters            | Description                                           | Default     |
| --------------------- | ----------------------------------------------------- | ----------- |
| Mode                  | Supports many modes including 802.11b/g/n             | 802.11b/g/n |
| SSID                  | Name of the SSID to be connected                      | inhand      |
| Authentication method | Keep consistent with the access point to be connected | Open type   |
| Encryption            | Keep consistent with the access point to be connected | NONE        |


### 4.2.7 IP Passthrough

The IP passthrough function distributes the address obtained by the WAN port to the device at the lower end of the LAN port. When external access to the router downstream devices is required, the router transmits data to the downstream device. Click 【Network】→【IP Passthrough】 menu, then enter the "IP Passthrough" page.

**Table 4-2-7 IP Passthrough Parameters**


| Parameters          | Description                                            | Default           |
| ------------------- | ------------------------------------------------------ | ----------------- |
| IP Passthrough      | Enable IP Passthrough                                  | Disable           |
| IP Passthrough Mode | Select work mode (DHCP Dynamic / DHCP fix MAC)         | DHCP Dynamic      |
| Fix MAC Address     | Set the fixed MAC address if in DHCP fix MAC mode      | 00:00:00:00:00:00 |
| DHCP lease          | Set the DHCP lease time and reacquire after expiration | 2 Minutes         |


### 4.2.8 Static Route

Static routes need to be set manually, after which packets will be transferred to the appointed routes.

To set a static route, click the 【Network】→【Static Route】 menu in the navigation tree, then enter the "Static Route" interface.

**Table 4-2-8 Static Route Parameters**


| Parameters          | Description                                                | Default       |
| ------------------- | ---------------------------------------------------------- | ------------- |
| Destination Address | Set the IP address of the destination                      | 0.0.0.0       |
| Netmask             | Set the subnet mask of the destination                     | 255.255.255.0 |
| Gateway             | Set the gateway of the destination                         | N/A           |
| Interface           | Select WAN/CELLULAR 1/LAN/WAN(STA) of the destination      | N/A           |
| Description         | For recording the significance of the static route address | N/A           |


## 4.3 Services

### 4.3.1 DHCP Service

DHCP adopts a Client/Server communication mode. The Client sends a configuration request to the Server, which feeds back the corresponding configuration information, including the distributed IP address to the Client, to achieve the dynamic configuration of the IP address and other information.

- The duty of the DHCP Server is to distribute an IP address when a workstation logs on and ensure each workstation is supplied with a different IP address. The DHCP Server has simplified some network management tasks requiring manual operations to the largest extent.
- As a DHCP Client, the device receives the IP address distributed by the DHCP server after logging in to the DHCP server, so the Ethernet interface of the device needs to be configured into automatic mode.

To enable the DHCP service, select 【Services】→【DHCP Service】 from the navigation tree, then enter the "DHCP Service" page.

**Table 4-3-1 DHCP Service Parameters**


| Parameters                                                                                    | Description                                                                                 | Default       |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------- |
| Enable DHCP                                                                                   | Enable DHCP service and dynamically allocate IP address                                     | Enable        |
| IP Pool Starting Address                                                                      | Set the starting IP address of dynamic allocation                                           | 192.168.2.2   |
| IP Pool Ending Address                                                                        | Set the ending IP address of dynamic allocation                                             | 192.168.2.100 |
| Lease                                                                                         | Set the lease of the IP allocated dynamically                                               | 60 minutes    |
| DNS                                                                                           | Set the DNS Server                                                                          | 192.168.2.1   |
| Windows Name Server                                                                           | Set the Windows name server                                                                 | N/A           |
| **Static designation of DHCP allocation (at most 20 DHCPs designated statically can be set)** |                                                                                             |               |
| MAC Address                                                                                   | Set a statically specified DHCP's MAC address (different from other MACs to avoid conflict) | N/A           |
| IP Address                                                                                    | Set a statically specified IP address                                                       | 192.168.2.2   |
| Host                                                                                          | Set the hostname                                                                            | N/A           |


### 4.3.2 DNS

DNS (Domain Name System) is a DDB used in TCP/IP application programs, providing switching between domain names and IP addresses. Through DNS, users can directly use meaningful domain names which can be easily memorized, and the DNS Server in the network can resolve the domain name into the correct IP address. Manually set the DNS; use DNS via dialing if it is empty. Generally, it only needs to be set when a static IP is used on the WAN port.

Click the 【Services】→【Domain Name Service】 menu in the navigation tree to enter the "Domain Name Service" interface.

**Table 4-3-2 DNS Parameters**


| Parameters               | Description                                  | Default |
| ------------------------ | -------------------------------------------- | ------- |
| Primary DNS              | Set the Primary DNS                          | 0.0.0.0 |
| Secondary DNS            | Set the Secondary DNS                        | 0.0.0.0 |
| Disable local DNS server | Do not transfer the local DNS server address | Disable |


### 4.3.3 DNS Relay

The CR202 works as a DNS Agent and relays DNS request and response messages between the DNS Client and DNS Server to carry out domain name resolution in lieu of the DNS Client.

From the navigation tree, select 【Services】→【DNS Relay】 menu, then enter the "DNS Relay" page.

**Table 4-3-3 DNS Relay Parameters**


| Parameters                                                                                              | Description                                                      | Default                                                    |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------- |
| Enable DNS Relay service                                                                                | Click to enable DNS service                                      | Enable (DNS will be enabled when DHCP service is enabled.) |
| **Designate [IP address <=> domain name] pair (20 IP address <=> domain name pairs can be designated)** |                                                                  |                                                            |
| IP Address                                                                                              | Set the IP address of the designated IP address <=> domain name  | N/A                                                        |
| Host                                                                                                    | Domain Name                                                      | N/A                                                        |
| Description                                                                                             | For recording the significance of the IP address <=> domain name | N/A                                                        |


 When enabling DHCP, the DHCP relay is also enabled automatically. The relay cannot be disabled without disabling DHCP.

### 4.3.4 DDNS

DDNS maps the user's dynamic IP address to a fixed DNS service. When the user connects to the network, the client program will pass the host's dynamic IP address to the server program on the service provider's host through information passing. The server program is responsible for providing DNS service and realizing dynamic DNS. DDNS captures the user's each change of IP address and matches it with the domain name, so that other Internet users can communicate through the domain name.

DDNS serves as a client tool of DDNS and is required to coordinate with a DDNS Server. Before the application of this function, a domain name shall be applied for and registered on a proper website such as [www.3322.org](http://www.3322.org).

The CR202 DDNS service types include QDNS (3322)-Dynamic, QDNS(3322)-Static, DynDNS-Dynamic, DynDNS-Static, DynDNS-Custom, and No-IP.com.

To set DDNS, click the 【Services】→【Dynamic Domain Name】 menu in the navigation tree, then enter the "Dynamic Domain Name" interface.

**Table 4-3-4 -1DDNS Parameters**


| Parameters      | Description                              | Default |
| --------------- | ---------------------------------------- | ------- |
| Current Address | Display the present IP of the router     | N/A     |
| Service Type    | Select the domain name service providers | Disable |


**Table 4-3-4-2 DDNS Main Parameters**


| Parameters   | Description                                                   | Default                                      |
| ------------ | ------------------------------------------------------------- | -------------------------------------------- |
| Service Type | QDNS (3322)-Dynamic                                           | Disable                                      |
| URL          | [http://www.3322.org/](http://www.3322.org/)                  | [http://www.3322.org/](http://www.3322.org/) |
| Username     | User name assigned in the application for dynamic domain name | N/A                                          |
| Password     | Password assigned in the application for dynamic domain name  | N/A                                          |
| Host Name    | Host name assigned in the application for dynamic domain name | N/A                                          |
| Wildcard     | Enable wildcard character                                     | Disable                                      |
| MX           | Set MX                                                        | N/A                                          |
| Backup MX    | Enable backup MX                                              | Disable                                      |
| Force Update | Enable force update                                           | Disable                                      |


### 4.3.5 Device Manager

The CR202 supports connecting to InHand Device Manager for remotely managing InHand products. Customers can manage and operate routers, check status, and upgrade software in batch via this platform.

Click the 【Services】→【Device Manager】 menu in the navigation tree to enter the "Device Manager" interface.

**Table 4-3-5 Device Manager Parameters**


| Parameters                  | Description                                                                                   | Default                |
| --------------------------- | --------------------------------------------------------------------------------------------- | ---------------------- |
| Enable                      | Enable Device Manager                                                                         | Disable                |
| Service Type                | Platform work mode: Device Manager or Custom                                                  | Device Manager         |
| Server                      | Select the cloud platform address: iot.inhand.com.cn (China), iot.inhandnetworks.com (global) | iot.inhandnetworks.com |
| Secure Channel              | Use encryption protocol for secure data transmission between router and platform              | Enable                 |
| Registered Account          | Account registered in Device Manager                                                          | N/A                    |
| LBS info Upload Interval    | Cellular information upload interval                                                          | 1 Hour                 |
| Series Info Upload Interval | Traffic information upload interval                                                           | 1 Hour                 |
| Channel Keepalive           | Keep alive packet interval                                                                    | 30 Seconds             |


### 4.3.6 SMS

SMS permits message-based reboot and manual dialing. Configure "Permit to Phone Number" and click `<Apply and Save>`. After that, send the "reboot" command to restart the device or send a custom connection or disconnection command to redial or disconnect the device.

From the navigation tree, select 【Services】→【SMS】 menu, then enter the "SMS" page.

**Table 4-3-6 SMS Parameters**


| Parameters             | Description                                                                                    | Default |
| ---------------------- | ---------------------------------------------------------------------------------------------- | ------- |
| Enable                 | Click to enable SMS function                                                                   | Disable |
| Status Query           | Define the English query instruction to inquire about the current working status of the router | N/A     |
| Reboot                 | Define the English query instruction to reboot the router                                      | N/A     |
| **SMS Access Control** |                                                                                                |         |
| Default Policy         | Select the manner of access processing                                                         | Accept  |
| Phone Number           | Fill in the mobile number                                                                      | N/A     |
| Action                 | Accept or block                                                                                | Accept  |
| Description            | Describe SMS control                                                                           | -       |


### 4.3.7 Traffic Manager

This function is mainly used to count data traffic in the cellular interface. If the threshold is 0, the router will only count and the rules will not take effect. This function requires enabling the NTP function.

Select 【Services】→【Traffic Manager】 to go to the "Traffic Manager" page.

**Table 4-3-7 Traffic Manager Parameters**


| Parameters                   | Description                                                                                                                                                                           | Default        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Enable                       | Click to enable the traffic manager function                                                                                                                                          | Disable        |
| Start Day                    | The day to start counting data traffic every month                                                                                                                                    | 1              |
| Monthly Threshold            | Data traffic threshold every month                                                                                                                                                    | 0MB            |
| When Over Monthly Threshold  | Operation when data traffic used within a month reaches the threshold: Only Reporting, Block Except Management (will not influence DM and management requirement), Shutdown Interface | Only Reporting |
| Last 24-Hours Threshold      | Data traffic threshold in the last 24 hours                                                                                                                                           | 0KB            |
| When Over 24-Hours Threshold | Operation when data traffic used within 24 hours reaches the threshold                                                                                                                | Only Reporting |
| Advance                      | Custom statistics and operations for the last several hours                                                                                                                           | Disable        |


### 4.3.8 Alarm Settings

When an abnormality occurs, the router will report an alarm according to the settings. Currently the router supports sending alarms in the following situations: System Service Fault, Memory Low, WAN/LAN1 Link-Up/Down, LAN2 Link-Up/Down, Cellular Up/Down, Traffic Alarm, Traffic Disconnect Alarm, SIM/UIM Card Switch, Active Link Switch, SIM/UIM Card Fault, Signal Quality Fault.

In the Alarm Manager interface, the following operations can be performed:

- Select alarm types in the "Alarm Input" area.
- Set the alarm notification method of the console in the "Alarm Output" area.

Select 【Services】→【Alarm Manager】 to go to the "Alarm Manager" page.

### 4.3.9 User Experience Plan

InHand Networks' User Experience Program is designed to improve the product user experience and customer service quality.

The user can disable or enable the User Experience Plan in 【Services】→【User Experience Plan】.

## 4.4 Firewall

The firewall function of the router implements corresponding control to data flow at the entry direction (from Internet to LAN) and exit direction (from LAN to Internet) according to the content features of the message (such as protocol style, source/destination IP address, etc.) and ensures safe operation of the router and hosts in the local area network.

### 4.4.1 Basic

From the navigation tree, select 【Firewall】→【Basic】, then enter the basic setup page.

**Table 4-4-1 Firewall Basic Parameters**


| Parameters                          | Description                                                | Default |
| ----------------------------------- | ---------------------------------------------------------- | ------- |
| Default Filter Policy               | Select accept/block                                        | Accept  |
| Block Anonymous WAN Requests (ping) | Select to filter WAN detection packets like PING detection | Disable |
| Filter Multicast                    | Select to filter multicast function                        | Enable  |
| Defend DoS Attack                   | Select to defend DoS attack                                | Enable  |
| SIP ALG                             | Select to enable SIP ALG                                   | Disable |


### 4.4.2 Filtering

Filter the network data by customized rules to allow or prohibit the specified data flow forwarded by the router.

To enable Access Control, select 【Firewall】→【Filtering】 from the navigation tree, then enter the "Filtering" page.

**Table 4-4-2 Filtering Parameters**


| Parameters       | Description                                                                         | Default       |
| ---------------- | ----------------------------------------------------------------------------------- | ------------- |
| Enable           | Check to enable filtering                                                           | Enable        |
| Protocol         | Select ALL/TCP/UDP/ICMP                                                             | ALL           |
| Source           | Set the source address of access control                                            | 0.0.0.0/0     |
| Source Port      | Set the source port of access control                                               | Not available |
| Destination      | Set the destination address                                                         | N/A           |
| Destination Port | Set the destination port of access control                                          | Not available |
| Action           | Select Accept/Block                                                                 | Accept        |
| Log              | Click to enable log and the log about access control will be recorded in the system | Disable       |
| Description      | Convenient for recording parameters of access control                               | N/A           |


### 4.4.3 Device Access Filtering

Set customized rules to allow or prohibit data and access to the router.

From the navigation tree, select 【Firewall】→【Device Access Filtering】, then enter the "Device Access Filtering" page.

**Table 4-4-3 Device Access Filtering Parameters**


| Parameters       | Description                                                                         | Default       |
| ---------------- | ----------------------------------------------------------------------------------- | ------------- |
| Enable           | Check to enable device access filtering                                             | Enable        |
| Protocol         | Select ALL/TCP/UDP/ICMP                                                             | ALL           |
| Source           | Set the source address of network access                                            | 0.0.0.0/0     |
| Source Port      | Set the source port of network access                                               | Not available |
| Destination      | Set the destination address                                                         | N/A           |
| Destination Port | Set the destination port of network access                                          | Not available |
| Interface        | Set the interface of network access                                                 | All WANs      |
| Action           | Select Accept/Block                                                                 | Accept        |
| Log              | Click to enable log and the log about access control will be recorded in the system | Disable       |
| Description      | Convenient for recording parameters of access control                               | N/A           |


### 4.4.4 Content Filtering

Set rules to disable access to specific URLs.

From the navigation tree, select 【Firewall】→【Content Filtering】 menu, then enter the "Content Filtering" page.

**Table 4-4-4 Content Filtering Parameters**


| Parameters  | Description                                                                   | Default |
| ----------- | ----------------------------------------------------------------------------- | ------- |
| Enable      | Click to enable filtering                                                     | Enable  |
| URL         | Set the URL that needs to be filtered                                         | N/A     |
| Action      | Select accept/block                                                           | Accept  |
| Log         | Click to write log and the log about filtering will be recorded in the system | Disable |
| Description | Record the meanings of various parameters of filtering                        | N/A     |


### 4.4.5 Port Mapping

Port mapping is also called a virtual server. The setting of port mapping can enable a host on the extranet to access a specific port of a host corresponding to an IP address on the intranet.

To configure port mapping, select 【Firewall】→【Port Mapping】 from the navigation tree, then enter the "Port Mapping" page.

**Table 4-4-5 Port Mapping Parameters**


| Parameters                    | Description                                                                       | Default   |
| ----------------------------- | --------------------------------------------------------------------------------- | --------- |
| Enable                        | Check to enable port mapping                                                      | Enable    |
| Proto                         | Select TCP/UDP/TCP&UDP                                                            | TCP       |
| Source                        | Set the source address of port mapping                                            | 0.0.0.0/0 |
| Service Port                  | Set the service port number of port mapping                                       | 8080      |
| Internal Address              | Set the internal address of port mapping                                          | N/A       |
| Internal Port                 | Set the internal port of port mapping                                             | 8080      |
| Log                           | Click to enable log and the log about port mapping will be recorded in the system | Disable   |
| External Interface (optional) | Set the external interface of port mapping                                        | N/A       |
| External Address (optional)   | Set the external address/tunnel name of port mapping                              | N/A       |
| Description                   | For recording the significance of each port mapping rule                          | N/A       |


### 4.4.6 Virtual IP Mapping

Both the router and the IP address of the host on the intranet can correspond with one virtual IP. Without changing the IP allocation of the intranet, the extranet can access the host on the intranet via the virtual IP. This function is always used with VPN.

To configure virtual IP mapping, select 【Firewall】→【Virtual IP Mapping】 from the navigation tree.

**Table 4--4-6 Virtual IP Mapping Parameters**


| Parameters                   | Description                                                                             | Default |
| ---------------------------- | --------------------------------------------------------------------------------------- | ------- |
| Virtual IP address of router | Set the virtual IP address of the router                                                | N/A     |
| Range of source address      | Set the range of the external source IP addresses                                       | N/A     |
| Enable                       | Click to enable virtual IP address                                                      | Enable  |
| Virtual IP                   | Set the virtual IP address of virtual IP mapping                                        | N/A     |
| Real IP                      | Set the real IP address of virtual IP mapping                                           | N/A     |
| Log                          | Click to enable log and the log about virtual IP address will be recorded in the system | Disable |
| Description                  | For recording the significance of each virtual IP address rule                          | N/A     |


### 4.4.7 DMZ

After mapping all ports, an extranet PC can access all ports of an internal device by DMZ settings.

From the navigation tree, select 【Firewall】→【DMZ】, then enter the "DMZ" page.

**Table 4-4-7 DMZ Parameters**


| Parameters           | Description                                    | Default |
| -------------------- | ---------------------------------------------- | ------- |
| Enable DMZ           | Check to enable the DMZ                        | Disable |
| DMZ Host             | Set the address of the DMZ Host                | N/A     |
| Source Address Range | Enter the range of the external source address | N/A     |
| Interface            | Select the external interface of DMZ           | N/A     |


### 4.4.8 MAC-IP Binding

If the default filter policy in the basic setting of the firewall is disabled, only hosts specified in MAC-IP Binding can access the outer net.

From the navigation tree, select 【Firewall】→【MAC-IP Binding】, then enter the "MAC-IP Binding" page.

**Table 4-4-8 MAC-IP Binding Parameters**


| Parameters  | Description                                                         | Default           |
| ----------- | ------------------------------------------------------------------- | ----------------- |
| MAC Address | Set the binding MAC address                                         | 00:00:00:00:00:00 |
| IP Address  | Set the binding IP address                                          | 192.168.2.2       |
| Description | For recording the significance of each MAC-IP binding configuration | N/A               |


### 4.4.9 NAT

NAT is the network address translation function, including source address translation (SNAT) and destination address translation (DNAT).

SNAT refers to the communication between the internal network and the external network when the destination address remains unchanged. DNAT refers to the translation of the destination address of the internal network into the external network without changing the source address when accessing the internal network.

**Table 4-4-9 NAT Parameters**


| Parameters         | Description                                     | Default   |
| ------------------ | ----------------------------------------------- | --------- |
| Enable             | Enable NAT                                      | Enable    |
| Type               | Set convert type                                | SNAT      |
| Proto              | Select protocol                                 | TCP       |
| Source IP          | Set the source IP of the NAT rule               | 0.0.0.0/0 |
| Source Port        | Set the source port of the NAT rule             | N/A       |
| Destination        | Set the destination IP of the NAT rule          | 0.0.0.0/0 |
| Destination Port   | Set the destination port of the NAT rule        | 0.0.0.0/0 |
| Interface          | Set the interface of the NAT rule               | N/A       |
| Translated Address | Translate the IP address if it matches the rule | 0.0.0.0   |
| Translated Port    | Translate the port if it matches the rule       | N/A       |


## 4.5 QoS

To ensure all LAN users can normally access network resources, the IP traffic control function can limit the flow of specified hosts in the LAN. QoS provides dedicated bandwidth and different service quality for different applications, greatly improving the network service capabilities.

### 4.5.1 IP BW Limit

Bandwidth control sets a limit on the upload and download speeds when accessing external networks.

From the navigation tree, select 【QoS】→【IP BW Limit】.

**Table 4-5-1 IP BW Limit Parameters**


| Parameters                  | Description                        | Default    |
| --------------------------- | ---------------------------------- | ---------- |
| Enable                      | Click to enable IP bandwidth limit | Disable    |
| Download bandwidth          | Set the download total bandwidth   | 1000kbit/s |
| Upload bandwidth            | Set the upload total bandwidth     | 1000kbit/s |
| Control port of flow        | Select CELLULAR/WAN                | CELLULAR   |
| **Host Download Bandwidth** |                                    |            |
| Enable                      | Click to enable                    | Enable     |
| IP Address                  | Set the IP address                 | N/A        |
| Guaranteed Rate (kbit/s)    | Set the rate                       | 1000kbit/s |
| Priority                    | Select priority                    | Medium     |
| Description                 | Describe the IP bandwidth limit    | N/A        |


## 4.6 Tools

### 4.6.1 PING

Select 【Tools】→【Ping】 from the navigation tree.

**Table 4-6-1 PING Detection Parameters**


| Parameters    | Description                             | Default  |
| ------------- | --------------------------------------- | -------- |
| Host          | Address of the destination host         | N/A      |
| PING Count    | Set the PING count                      | 4        |
| Packet Size   | Set the size of PING detection          | 32 bytes |
| Expert Option | Advanced parameter of PING is available | N/A      |


### 4.6.2 Traceroute

To perform traceroute, select 【Tools】→【Traceroute】 from the navigation tree.

**Table 4-6-2 Traceroute Parameters**


| Parameters    | Description                                    | Default |
| ------------- | ---------------------------------------------- | ------- |
| Host          | Address of the destination host to be detected | N/A     |
| Maximum Hops  | Set the max hops for traceroute                | 20      |
| Timeout       | Set the timeout of traceroute                  | 3 s     |
| Protocol      | ICMP/UDP                                       | UDP     |
| Expert Option | Advanced parameter for traceroute is available | N/A     |


### 4.6.3 Link Speed Test

Select 【Tools】→【Link Speed Test】 from the navigation tree, then enter the "Link Speed Test" page.

Select a file locally and click upload/download, then check the network speed in the log.

### 4.6.4 TCPDUMP

Select 【Tools】→【TCPDUMP】 from the navigation tree, then enter the TCP dump page.

**Table 4-6-4 TCPDUMP Parameters**


| Parameters     | Description                                          | Default |
| -------------- | ---------------------------------------------------- | ------- |
| Interface      | Select the interface to capture the packet           | ANY     |
| Capture number | Stop TCP dump after capturing this number of packets | 10      |
| Expert Option  | Advanced parameter for TCPDUMP                       | N/A     |


## 4.7 Status

### 4.7.1 System

From the navigation tree, select 【Status】→【System】, then enter the "System" page.

This page displays system statistics, including name, model, serial number, description, current version, current Bootloader version, router time, PC time, UP time, CPU load, and memory consumption. Click the `<Sync Time>` button to synchronize the router with the system time of the host, as covered in the setup chapter.

### 4.7.2 Modem

From the navigation tree, select 【Status】→【Modem】, then enter the "Modem" page.

This page displays the basic information of dial-up, including status, signal level, register status, IMEI (ESN) code, IMSI code, LAC, and cell ID.

### 4.7.3 Traffic Statistics

Select 【Status】→【Traffic Statistics】 to go to the "Traffic Statistics" page to query traffic statistics.

This page displays the traffic statistics on the dialing interface, including the statistics on the traffic received in the latest month, traffic transmitted in the latest month, traffic received on the last day, and traffic transmitted on the last day.

### 4.7.4 Alarm

Select 【Status】→【Alarm】 to go to the "Alarm" page to view all alarms generated in the system since power-on. The alarms can be cleared or confirmed.

The alarms have the following states:

- **Raise**: The alarm has been generated but not been confirmed.
- **Confirm**: The alarm cannot be solved currently.
- **All**: All generated alarms.

The alarms are classified into the following levels:

- **EMERG**: The device undergoes a serious error that causes a system reboot.
- **CRIT**: The device undergoes an unrecoverable error.
- **WARN**: The device undergoes an error that affects system functions.
- **NOTICE**: The device undergoes an error that affects system performance.
- **INFO**: A normal event occurs.

### 4.7.5 WLAN

Select 【Status】→【WLAN】 to go to the "WLAN" page to query the WLAN connection status.

This page displays the WLAN connection information, including channel, SSID, BSSID, security, signal (%), mode, and status.

### 4.7.6 Network Connections

From the navigation tree, select 【Status】→【Network Connections】, then enter the "Network Connections" page to see the connection status.

This page shows the basic information of dial-up and LAN.

- WAN includes MAC address, connection type, IP address, netmask, gateway, DNS, MTU, status, etc.
- Dial-up includes connection type, IP address, netmask, gateway, DNS, MTU, status, and connection time.
- LAN includes connection type, MAC address, IP address, netmask, gateway, MTU, and DNS.

### 4.7.7 Device Manager

From the navigation tree, select 【Status】→【Device Manager】, then enter the "Device Manager" page to check the connection status between the router and Device Manager.

### 4.7.8 Route Table

From the navigation tree, select 【Status】→【Route Table】, then enter the "Route Table" page to see the router status.

This page displays the active route table, including destination, netmask, gateway, metric, and interface.

### 4.7.9 Device List

From the navigation tree, select 【Status】→【Device List】, then enter the "Device List" page to inquire the device list.

This page displays the device list, including interface, MAC address, IP address, host, and lease (click the MAC address to link to IEEE to inquire about the validity of the address).

### 4.7.10 Log

From the navigation tree, select 【Status】→【Log】, then enter the "Log" page.

This page displays the logs, including selection to see the number of log lines (20/50/....../all), log level (information, debug, and warning), time, module, and content. Clear log, download log file, download system diagnosis record (refresh rate of this page is 5/10/…... 1min by default).

### 4.7.11 Third Party Software Notices

From the navigation tree, select 【Status】→【Third Party Software Notices】, then enter the "Third Party Software Notices" page to check the third-party software used in the router system.

---

# Appendix Troubleshooting

## A.1 Network Connection Problems


| Symptom                                 | Possible Cause                               | Troubleshooting Steps                                                                             | Reference Chapter                                      |
| --------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Cannot access the Internet via cellular | SIM card not inserted or poor contact        | 1. Check whether the SIM card is correctly inserted. 2. Reinsert the SIM card.                    | [Install SIM/UIM Card](#221-install-simuim-card)       |
| Cannot access the Internet via cellular | APN parameters configured incorrectly        | 1. Verify that the APN parameters are correct. 2. Contact the operator to obtain the correct APN. | [Cellular Networking](#scenario-1-cellular-networking) |
| Cannot access the Internet via cellular | Weak signal or no signal                     | 1. Check whether the antenna is connected. 2. Adjust the device position.                         | [Install Antenna](#222-install-antenna)                |
| Cannot access the Internet via WAN      | Upstream device malfunction or cable issue   | 1. Check whether the upstream device is working. 2. Replace the network cable.                    | [Wired WAN Access](#scenario-2-wired-wan-access)       |
| Cannot access the Internet via WAN      | PPPoE username/password error                | 1. Verify the PPPoE username and password. 2. Contact the ISP for confirmation.                   | [Wired WAN Access](#scenario-2-wired-wan-access)       |
| Wi-Fi STA relay fails                   | Target AP out of range or incorrect password | 1. Check whether the target AP is within range. 2. Verify the authentication method and password. | [Wi-Fi STA Relay](#scenario-4-wi-fi-sta-relay)         |


## A.2 Web Access Problems


| Symptom                                | Possible Cause              | Troubleshooting Steps                                                                                       | Reference Chapter                                        |
| -------------------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Cannot open the Web interface          | IP address error            | 1. Confirm that the PC and the device are in the same subnet. 2. Check the device default IP (192.168.2.1). | [Log in to the Router](#224-log-in-to-the-router)        |
| Cannot open the Web interface          | Browser compatibility issue | 1. Change the browser (Chrome is recommended). 2. Clear the browser cache.                                  | [Log in to the Router](#224-log-in-to-the-router)        |
| Cannot open the Web interface          | Proxy server enabled        | 1. Cancel the proxy server in the browser settings. 2. Retry access.                                        | [Cancel the Proxy Server](#224-log-in-to-the-router)     |
| Forgot the password after modification | Password lost               | 1. Restore the device to factory default settings. 2. Log in with the default credentials on the nameplate. | [Restore Factory Settings](#15-restore-factory-settings) |


## A.3 Device Startup and Hardware Problems


| Symptom                                    | Possible Cause                | Troubleshooting Steps                                                                                               | Reference Chapter                                      |
| ------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Device frequently auto-restarts            | Module abnormality            | 1. Check whether the module works normally. 2. Contact technical support if the problem persists.                   | [LED Indication](#14-led-indication)                   |
| Device frequently auto-restarts            | SIM card or signal issue      | 1. Check the SIM card and signal strength. 2. Verify the dial-up parameters.                                        | [Cellular Networking](#scenario-1-cellular-networking) |
| Device frequently auto-restarts            | Abnormal power supply voltage | 1. Check the power supply voltage. 2. Replace the power adapter if necessary.                                       | [Connect Power Supply](#223-connect-power-supply)      |
| Power LED is not on                        | Fuse blown or power issue     | 1. Check whether the protective fuse is blown. 2. Check the power supply voltage range and polarity.                | [Connect Power Supply](#223-connect-power-supply)      |
| Network LED is not on when connected to PC | Cable or NIC issue            | 1. Check whether a crossover cable is used. 2. Check the cable condition. 3. Set the PC NIC to 10/100M full duplex. | [Install WAN/LAN Cable](#scenario-2-wired-wan-access)  |


## A.4 VPN and Forwarding Problems


| Symptom                                                               | Possible Cause                   | Troubleshooting Steps                                                                              | Reference Chapter         |
| --------------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------- |
| Center cannot connect to PC under the router after VPN is established | PC firewall blocking             | 1. Disable the firewall of the PC under the router. 2. Add an allow rule if necessary.             | [Firewall](#44-firewall)  |
| PC under the router cannot ping the VPN server                        | Shared Connection disabled       | 1. Enable "Shared Connection" on the WAN or Cellular page. 2. Save and reboot.                     | [Cellular](#421-cellular) |
| Firmware upgrade fails                                                | Network segment mismatch (local) | 1. Confirm that the local PC and the router are in the same network segment. 2. Retry the upgrade. | [Upgrade](#417-upgrade)   |
| Firmware upgrade fails                                                | No Internet access (remote)      | 1. Confirm that the router can access the Internet. 2. Retry the remote upgrade.                   | [Upgrade](#417-upgrade)   |


---

# Appendix Safety Precautions

1. The device shall be installed and operated in a powered-off status.
2. Do not use or leave the device at very high temperature conditions (for example, strong direct sunlight or a vehicle in extremely hot conditions). Otherwise, the built-in battery may overheat or catch fire, or its performance will degrade and its service life will decrease.
3. Do not immerse the device in water. Store it in a cool and dry environment when not in use.
4. Do not use or leave the cell near a heat source such as fire or heater.
5. Do not short circuit, over-charge, or over-discharge the battery.
6. Do not reverse the positive and negative terminals.
7. Do not disassemble or modify the cell.
8. Do not transport and store the battery together with metal objects such as necklaces, hairpins, coins, etc.
9. Do not use the cell with conspicuous damage or deformation.
10. Do not connect the cell to an electrical outlet directly.
11. If the cell leaks and the electrolyte gets into the eyes, do not wipe the eyes; instead, thoroughly rinse the eyes with clean running water for at least 15 minutes, and immediately seek medical attention.
12. Do not use lithium-ion batteries and other different lithium battery models in mixture.
13. Keep the battery away from babies.
14. Do not directly solder the battery or pierce the battery with a nail or other sharp object.
15. Do not strike, throw, or trample the battery.
16. The battery replacement shall be done only by either the cell supplier or the device supplier and never by the user.
17. Be aware that discharged batteries may cause fire; tape the terminals to insulate them.
18. Do not use the battery in a location where electrostatic and magnetic fields are strong, otherwise the safety devices may be damaged.

> **Warning**: Non-professionals should not open the device enclosure. Risk of electric shock.

---

# Appendix Command Line Reference

## B.1 Help Command

### B.1.1 Help

**Command**: `help [<cmd>]`

**Function**: Get help from a command.

**View**: All views

**Parameter**:

- `<cmd>`: Command name

**Example**:

- Enter `help` to get the list of all currently available commands.
- Enter `help show` to display all the parameters of the show command and usage instructions.

## B.2 View Switchover Command

### B.2.1 Enable

**Command**: `enable [15 [<password>]]`

**Function**: Switch over to the privileged user level.

**View**: Ordinary user view

**Parameters**:

- `15`: User right limit level. Currently only supports right limit 15 (super users).
- `<password>`: Password corresponding to the privileged user limit level. A password input hint will be given if not entered.

**Example**:

```
enable 123456
```

Switch over to super user with the password 123456.

### B.2.2 Disable

**Command**: `disable`

**Function**: Exit the privileged user level.

**View**: Super user view, configure view

**Example**:

```
disable
```

Return to ordinary user view.

### B.2.3 End and !

**Command**: `end` or `!`

**Function**: Exit the current view and return to the last view.

**View**: Configure view

**Example**:

```
end
```

Return to super user view.

### B.2.4 Exit

**Command**: `exit`

**Function**: Exit the current view and return to the last view (exit console if in ordinary user view).

**View**: All views

**Example**:

- Enter `exit` in configure view to return to super user view.
- Enter `exit` in ordinary user view to exit the console.

## B.3 Check System State Command

### B.3.1 Show version

**Command**: `show version`

**Function**: Display the type and version of the router software.

**View**: All views

**Example**:

```
show version
```

Display the following information:

- Type: Current factory type of equipment
- Serial number: Current factory serial number of equipment
- Description: [www.inhand.com.cn](http://www.inhand.com.cn)
- Current version: Current version of equipment
- Current version of Bootloader: Current Bootloader version of equipment

### B.3.2 Show system

**Command**: `show system`

**Function**: Display the router system information.

**View**: All views

**Example**:

```
show system
```

Display system uptime and load average.

### B.3.3 Show clock

**Command**: `show clock`

**Function**: Display the system time of the router.

**View**: All views

**Example**:

```
show clock
```

Display the system time (e.g., Sat Jan 1 00:01:28 UTC 2000).

### B.3.4 Show modem

**Command**: `show modem`

**Function**: Display the MODEM state of the router.

**View**: All views

**Example**:

```
show modem
```

Display modem type, state, manufacturer, product name, signal level, register state, IMSI number, and network type.

### B.3.5 Show log

**Command**: `show log [lines <n>]`

**Function**: Display the router system log. By default, the latest 100 logs are displayed.

**View**: All views

**Parameter**:

- `lines <n>`: Limits the number of logs displayed. `n` as a positive integer indicates the latest n logs; as a negative integer indicates the earliest n logs; 0 indicates all logs.

**Example**:

```
show log
```

Display the latest 100 log records.

### B.3.6 Show users

**Command**: `show users`

**Function**: Display the user list of the router.

**View**: All views

**Example**:

```
show users
```

Display the system user list. The user marked with * is the super user.

### B.3.7 Show startup-config

**Command**: `show startup-config`

**Function**: Display the startup configuration of the router.

**View**: Super user view and configuration view

**Example**:

```
show startup-config
```

Display the startup configuration of the system.

### B.3.8 Show running-config

**Command**: `show running-config`

**Function**: Display the operational configuration of the router.

**View**: Super user view and configuration view

**Example**:

```
show running-config
```

Display the operational configuration of the system.

## B.4 Check Network Status Command

### B.4.1 Show interface

**Command**: `show interface`

**Function**: Display the port state information of the router.

**View**: All views

**Example**:

```
show interface
```

Display the state of all ports.

### B.4.2 Show ip

**Command**: `show ip`

**Function**: Display the IP status of the router.

**View**: All views

**Example**:

```
show ip
```

Display the system IP status.

### B.4.3 Show route

**Command**: `show route`

**Function**: Display the routing list of the router.

**View**: All views

**Example**:

```
show route
```

Display the routing list of the system.

### B.4.4 Show arp

**Command**: `show arp`

**Function**: Display the ARP list of the router.

**View**: All views

**Example**:

```
show arp
```

Display the ARP list of the system.

## B.5 Internet Testing Command

The router provides `ping`, `telnet`, and `traceroute` for Internet testing.

### B.5.1 Ping

**Command**: `ping <hostname> [count <n>] [size <n>] [source <ip>]`

**Function**: Apply ICMP testing for an appointed host.

**View**: All views

**Parameters**:

- `<hostname>`: Address or domain name of the host to be tested.
- `count <n>`: Testing times.
- `size <n>`: Size of the data package (bytes).
- `source <ip>`: Appointed testing IP address.

**Example**:

```
ping www.g.cn
```

Test [www.g.cn](http://www.g.cn) and display the testing results.

### B.5.2 Telnet

**Command**: `telnet <hostname> [<port>] [source <ip>]`

**Function**: Telnet login to the appointed host.

**View**: All views

**Parameters**:

- `<hostname>`: Address or domain name of the host to log in to.
- `<port>`: Telnet port.
- `source <ip>`: Appoints the IP address of the Telnet login.

**Example**:

```
telnet 192.168.2.2
```

Telnet login to 192.168.2.2.

### B.5.3 Traceroute

**Command**: `traceroute <hostname> [maxhops <n>] [timeout <n>]`

**Function**: Test the acting routing of the appointed host.

**View**: All views

**Parameters**:

- `<hostname>`: Address or domain name of the host to be tested.
- `maxhops <n>`: Maximum routing jumps.
- `timeout <n>`: Timeout of each jumping test (seconds).

**Example**:

```
traceroute www.g.cn
```

Apply the routing of [www.g.cn](http://www.g.cn) and display the testing results.

## B.6 Configuration Command

In super user view, the router can use the `configure` command to switch over to the configure view for management.

Some setting commands support `no` and `default`, wherein `no` indicates canceling some parameter setting and `default` indicates recovering the default setting of some parameter.

### B.6.1 Configure terminal

**Command**: `configure terminal`

**Function**: Switch over to the configuration view and input equipment at the terminal end.

**View**: Super user view

**Example**:

```
configure terminal
```

Switch over to the configuration view.

### B.6.2 Hostname

**Command**: `hostname [<hostname>]` / `default hostname`

**Function**: Display or set the host name of the router.

**View**: Configure view

**Parameter**:

- `<hostname>`: New host name.

**Example**:

```
hostname MyRouter
```

Set the host name of the router to MyRouter.

```
default hostname
```

Recover the host name of the router to the factory setting.

### B.6.3 Clock timezone

**Command**: `clock timezone <timezone> <n>` / `default clock timezone`

**Function**: Set the time zone information of the router.

**View**: Configure view

**Parameters**:

- `<timezone>`: Time zone name, 3 capitalized English letters.
- `<n>`: Time zone deviation value, -12 to +12.

**Example**:

```
clock timezone CST -8
```

Set the time zone to east eighth area and the name to CST (China Standard Time).

```
default clock timezone
```

Recover the time zone of the router to the factory setting.

### B.6.4 Ntp server

**Command**: `ntp server <hostname>` / `no ntp server` / `default ntp server`

**Function**: Set the client of the Internet time server.

**View**: Configure view

**Parameter**:

- `<hostname>`: Address or domain name of the time server host.

**Example**:

```
ntp server pool.ntp.org
```

Set the address of the Internet time server to pool.ntp.org.

```
no ntp server
```

Disable the router from getting system time via the network.

```
default ntp server
```

Recover the network time server of the router to the factory setting.

### B.6.5 Config export

**Command**: `config export`

**Function**: Export the current configuration.

**View**: Configure view

**Example**:

```
config export
```

The current configuration is exported.

### B.6.6 Config import

**Command**: `config import`

**Function**: Import a configuration.

**View**: Configure view

**Example**:

```
config import
```

The configuration is imported.

## B.7 System Management Command

### B.7.1 Reboot

**Command**: `reboot`

**Function**: System restarts.

**View**: Super user view and configuration view

**Example**:

```
reboot
```

System restarts.

### B.7.2 Enable username

**Command**: `enable username [<name>]`

**Function**: Modify the username of the super user.

**View**: Configure view

**Parameter**:

- `<name>`: New super user username.

**Example**:

```
enable username admin
```

The username of the super user is changed to admin.

### B.7.3 Enable password

**Command**: `enable password [<password>]`

**Function**: Modify the password of the super user.

**View**: Configure view

**Parameter**:

- `<password>`: New super user password.

**Example**:

```
enable password
```

Enter the password according to the hint.

### B.7.4 Username

**Command**: `username <name> [password [<password>]]` / `no username <name>` / `default username`

**Function**: Set the username and password.

**View**: Configure view

**Example**:

```
username abc password 123
```

Add an ordinary user; the name is abc and the password is 123.

```
no username abc
```

Delete the ordinary user with the name abc.

```
default username
```

Delete all ordinary users.

---

# FAQ

**Question 1: The router is powered on, but cannot access the Internet through it. How to troubleshoot?**

1. Check whether the router has a SIM card inserted.
2. Check whether the SIM card is enabled with data service and whether the service is suspended due to an overdue charge.
3. Check whether the dial-up parameters (e.g., APN, dial-up number, username, and password) are correctly configured.
4. Check whether the IP address of the computer is in the same subnet as the router and whether the gateway address is the router's LAN address.

**Question 2: The router is powered on. PING detection from the PC finds packet loss. How to troubleshoot?**

1. Check whether the network crossover cable is in good condition.
2. Check whether the PC network card is set to 10/100M full duplex.

**Question 3: The setting is forgotten after revising the IP address and the router cannot be configured. How to restore it?**

1. Press the RESET button immediately after powering on the device.
2. When the System LED is steady on, release the RESET button; the system LED will blink, then press the RESET button again.
3. When the System LED blinks slowly, release the RESET button. The device will be restored to default settings and will start up normally.

**Question 4: After the router is powered on, it frequently auto-restarts. Why?**

1. Check whether the module works normally.
2. Check whether the router has a SIM card inserted.
3. Check whether the SIM card is enabled with data service and whether the service is suspended due to an overdue charge.
4. Check whether the dial-up parameters (e.g., APN, dial-up number, username, and password) are correctly configured.
5. Check whether the signal is normal.
6. Check whether the power supply voltage is normal.

**Question 5: Why does upgrading the firmware always fail?**

1. When upgrading locally, check whether the local PC and the router are in the same network segment.
2. When upgrading remotely, first make sure the router can access the Internet.

**Question 6: After the router establishes a VPN with the VPN server, the PC under the router can connect to the server, but the center cannot connect to the PC under the router. How to fix it?**

Make sure the firewall of the PC under the router is disabled or has an allow rule.

**Question 7: After the router establishes a VPN with the VPN server, the PC under the router cannot ping the server. How to fix it?**

Make sure "Shared Connection" on the WAN or Cellular page is enabled in the router configuration.

**Question 8: The router is powered on, but the Power LED is not on. How to troubleshoot?**

1. Check whether the protective fuse is blown.
2. Check the power supply voltage range and whether the positive and negative electrodes are correctly connected.

**Question 9: The router is powered on, but the Network LED is not on when connected to the PC. How to troubleshoot?**

1. When the PC and the router are connected with a network cable, check whether a network crossover cable is used.
2. Check whether the network cable is in good condition.
3. Set the PC network card to 10/100M full duplex.

**Question 10: The router is powered on. When connected to the PC, the Network LED is normal but ping detection to the router fails. How to troubleshoot?**

1. Check whether the IP address of the PC and the router are in the same subnet and whether the gateway address is the router's LAN address.

**Question 11: The router is powered on, but cannot be configured through the Web interface. How to troubleshoot?**

1. Check whether the IP address of the computer is in the same subnet as the router and whether the gateway address is the router's LAN address.
2. Check the firewall settings of the PC used to configure the router; verify whether this function is blocked by the firewall.
3. Check whether the browser has any third-party plugin. It is recommended to configure after unloading the plugin.

**Question 12: The router dial-up always fails. What to do?**

Restore the router to factory default settings and configure the parameters again.

**Question 13: How to restore the router to factory default settings?**

To restore the device to default settings using the reset button, follow these steps:

1. Power on the device.
2. Press and hold the **RESET** button until the **System LED** turns **yellow**, then release the button.
3. When the **System LED** starts flashing **yellow**, press and hold the **RESET** button again.
4. When the **System LED** starts flashing **green** slowly, release the **RESET** button. The device will now be restored to its default settings and will restart normally.

