# Industrial Router IR602 User manual

First and foremost, thank you for choosing our company's product. Before use, carefully read this user manual. Compliance with the following statements helps maintain intellectual property rights and legal compliance, ensuring that the user experience aligns with the latest product information. If there are any questions or if written permission is needed, contact the technical support team at any time.

- Copyright Statement

This user manual contains copyrighted content. The copyright belongs to InHand Networks Technology Co., Ltd. and its licensors. Without written permission, no organization or individual may excerpt, copy any part of the content of this manual, or distribute it in any form.

- Disclaimer

Due to ongoing updates in product technology and specifications, the company cannot guarantee that the information in the user manual is entirely consistent with the actual product. Therefore, the company does not accept any disputes arising from discrepancies between the actual technical parameters and the user manual. Any changes to the product will not be notified in advance. The company reserves the right to make final changes and interpretations.

- Copyright Information

The content of this user manual is protected by copyright law. The copyright belongs to InHand Networks Technology Co., Ltd. and its licensors. All rights reserved. Without written permission, no one may use, copy, or distribute the content of this manual.

## Graphical Interface Conventions

The following symbols are used throughout this manual.
![alt text](./img/image.png)

<p align="center"><strong>Figure 0-1 Graphical Interface Conventions</strong></p>

| Symbol | Meaning | Example |
|--------|---------|---------|
| `< >` | Indicates a variable or parameter to be replaced with an actual value | `<IP Address>` means enter a specific IP address |
| `" "` | Indicates a text label on the interface | Click the "Save" button |
| `→` | Indicates menu hierarchy or operation sequence | 【Network】→【Cellular】 |
| `【 】` | Indicates a menu or page name | Enter the 【System Settings】page |

## Technical Support
Email: support@inhandnetworks.com

URL: www.inhand.com

## How to Use This Manual

### Choose Your Path

- First-time users: Read in sequence: "Device Overview" → "Installation and First Use" → "Common Scenario Configuration" → "Function Description and Parameter Reference"
- Existing device users: Directly refer to "Function Description and Parameter Reference" or "Appendix A Troubleshooting"
- Cloud platform management users: Refer to "Common Scenario Configuration" for device remote management platform content (if applicable)


**Quick Task Navigation**:

| Task | Chapter | Estimated Time |
|------|---------|----------------|
| Get to know the device appearance and LED indicators | [Getting to Know the Device](#chapter-1-getting-to-know-the-device) | About 5 minutes |
| Install the device and connect to the network for the first time | [Installation and First-Time Use](#chapter-2-installation-and-first-time-use) | About 10 minutes |
| Configure cellular network access | [Common Scenario Configurations](#chapter-3-common-scenario-configurations) | About 5 minutes |
| Configure DeviceLive cloud management | [Common Scenario Configurations](#chapter-4-feature-descriptions-and-parameter-reference) | About 10 minutes |
| View device parameters and status | [Feature Descriptions and Parameter Reference](#chapter-4-feature-descriptions-and-parameter-reference) | As needed |
| Troubleshoot device issues | [Safety Precautions](#appendix-safety-precautions) | As needed |

---

# Chapter 1 Getting to Know the Device

## 1.1 Overview

The IR602 series is a lightweight 5G RedCap industrial router developed by InHand Networks for large-scale, medium-rate Industrial IoT scenarios. The product integrates 5G RedCap, Wi-Fi 6, and 2.5G Ethernet, and supports 5G SA, link redundancy, intelligent link scheduling, encrypted tunnels, and DeviceLive cloud-based centralized management. It provides stable, secure, and easy-to-maintain network connectivity for distributed industrial sites across factories, remote areas, and unattended locations.

Built with industrial-grade design, the IR602 series can adapt to complex industrial environments, meeting the long-term, reliable operation requirements of industrial sites and distributed stations, providing a solid network foundation for large-scale Industrial IoT deployments.

![alt text](./img/image-1.png)
<p align="center"><strong>Figure 1-1 IR602 Device Overview</strong></p>

## 1.2 LED Indicators

| LED Indicator | Status | Meaning |
|--------------|--------|---------|
| SYS | Off | Power off |
| | Steady red | Device starting |
| | Blink red | System error |
| | Steady green | Working properly |
| | Blink red | Firmware updating |
| NET | Off | The WAN port is not connected |
| | Steady green | The WAN port is connected normally |
| | Blink green | Data transferring |
| Cellular | Steady green with one indicator | Poor cellular signal |
| | Steady green with two indicators | Medium cellular signal |
| | Steady green with three indicators | Good cellular signal |
| Wi-Fi 2.4G | Off | AP&STA is disabled |
| | Blink green | Working properly |
| | Steady green | Work as STA and AP is not associated |
| Wi-Fi 5G | Off | AP&STA is disabled |
| | Blink green | Working properly |
| | Steady green | Work as STA and AP is not associated |
| | Steady green | Other abnormalities |


## 1.3 Restore Factory Defaults

![alt text](./img/image-2.png)

<p align="center"><strong>Figure 1-2 Reset Button</strong></p>

To reset to factory default settings using the Reset button:

1. Power on the device. As soon as the SYS indicator light goes out, press and hold the Reset button for 5 to 10 seconds, then release it promptly. The SYS indicator light will then start flashing.
2. While the SYS indicator light is flashing, press and hold the SYS indicator until the light stays on, and then release the button. At this time, the factory reset operation of the device is successful.


## 1.4 Default Settings

| No. | Function | Default Settings |
|-----|----------|-----------------|
| 1 | Cellular Dialing | Default dialing is set to "SIM1" |
| 2 | Wi-Fi | 1. Wi-Fi 2.4G access point enabled, SSID: Prefixed with "IR602-", followed by the last 6 digits of the wireless MAC address. 2. Wi-Fi 5G access point enabled, SSID: Prefixed with "IR602-5G-", followed by the last 6 digits of the wireless MAC address. 3. The authentication method is WPA2-PSK. 4. The password for both is the last 8 digits of the serial number. |
| 3 | Ethernet | 1. Enable all 3 LAN ports. 2. IP Address: 192.168.2.1 Subnet Mask: 255.255.255.0 3. DHCP server enabled, with an address pool from 192.168.2.2 to 192.168.2.100 for automatic IP address assignment to connected devices. |
| 4 | Network Access Control | Local HTTP and HTTPS are enabled with port numbers 80 and 443 respectively. Disable access from the cellular network. |
| 5 | Username/Password | The login credentials are printed on the nameplate at the bottom of the device |


# Chapter 2 Installation and First-Time Use

## 2.1 Pre-installation Preparation

Before installing the IR602, the following items must be prepared:

| Item | Quantity | Description |
|------|----------|-------------|
| IR602 router | 1 | Main device |
| Power adapter | 1 | Original power adapter included with the device |
| Antennas | 3+ | 4G/5G antennas and Wi-Fi antennas (quantity depends on model) |
| SIM card | 1 | Valid SIM card from a supported carrier (for cellular models) |
| Ethernet cable | 1+ | Standard RJ45 Ethernet cable |
| PC or laptop | 1 | For initial configuration and verification |

> **Note:** Use the original power adapter to avoid device damage caused by mismatched power adapters.

> **Note:** The device should not be placed in an environment with strong electromagnetic interference. Keep it at a safe distance from high-power equipment.

## 2.2 Installation Guide

### 2.2.1 Physical Installation

1. Install the 4G/5G and Wi-Fi antennas onto the corresponding antenna connectors on the device.
2. Insert the SIM card into the SIM card slot (for cellular models).
3. Connect the power cable to the device and power it on.
4. Connect an Ethernet cable from any LAN port on the IR602 to the PC.

### 2.2.2 PC Network Configuration

The device's LAN port has DHCP Server functionality enabled by default. Once the PC has automatically obtained an IP address, ensure that the PC and router are in the same address range.

If the PC fails to obtain an IP address automatically, configure it with a static IP address and the following parameters:

- IP Address: 192.168.2.x (Choose an available address within the range of 192.168.2.2 to 192.168.2.254)
- Subnet Mask: 255.255.255.0
- Default Gateway: 192.168.2.1
- DNS Servers: 8.8.8.8 (or the ISP's DNS server address)

### 2.2.3 Access the Web Management Interface

1. Enter the default device address 192.168.2.1 in the browser's address bar.
2. Enter the username and password (the login credentials are printed on the nameplate at the bottom of the device).
3. Access the device's web management interface. If the page shows a security warning, click the "Hide" or "Advanced" button and select "Proceed" to continue.

![alt text](./img/image-3.png)

<p align="center"><strong>Figure 2-2 Web Login Interface</strong></p>


## 2.3 Quick Check

| Check Item | Check Method | Expected Result |
|--------|----------|----------|
| Device Power-up | Observe the SYS indicator | Solid red: System booting / System operating normally |
| Cellular Network Connection | Observe the cellular status LED | Solid green: Cellular connection established successfully |
| Web UI Access | Enter 192.168.2.1 in the web browser | Login page opens normally |
| PC IP Acquisition | Check PC network status | | IP address belongs to the 192.168.2.0 subnet |


# Chapter 3 Common Scenario Configurations


## Scenario 1: Cellular Networking

**Objective**: Access the internet via 4G/5G cellular network.

**Prerequisites**: SIM card inserted and antennas installed, device powered on.

**Estimated Time**: About 5 minutes.

**Operation Steps**:
1. Insert the SIM card and install the cellular antennas.
2. Power on the device. The IR602 router will automatically establish a dial-up connection and connect to the network.
3. To configure APN (Access Point Name, which can be understood as the "address" of the operator's network) parameters, navigate to 【Internet】→【Cellular】 and click the "Edit" button.

![alt text](./img/image-4.png)=
<p align="center"><strong>Figure 3-1 Cellular APN Configuration</strong></p>

4. Enter the APN parameters provided by the carrier and click "Save."
5. (Optional) To configure a traffic policy, navigate to 【Internet】→【Cellular】 and click the "Policy" button.

![alt text](./img/image-5.png)
<p align="center"><strong>Figure 3-2 Cellular Traffic Policy</strong></p>

| Action | Description |
|--------|-------------|
| Notification | Generates an event when traffic reaches the threshold but does not stop forwarding regular business traffic |
| Cloud Management Only | Generates an event when traffic reaches the threshold, allowing only cloud-based management traffic while blocking regular business internet access |
| Switch the SIM Card | Generates an event when traffic reaches the threshold and switches to another SIM card for internet access |

**Verification Methods**:
1. Check the NET indicator light. A steady green light indicates the WAN port is connected normally.
2. Navigate to 【Status】→【Link Monitor】 to verify the cellular link status.

**Common Issues**:
- Unable to connect to cellular network: Verify the SIM card is properly inserted and the APN parameters are correct.
- Poor signal: Check antenna connections and adjust the device position.

**Cautions**:
1. In certain dedicated network scenarios, it may be necessary to manually disable the "Link Detection" function under the 【Internet】 menu to prevent cellular connectivity issues caused by unsuccessful detection.
2. In some cases, manual configuration of the subnet mask for the cellular interface may be required to ensure the proper functioning of the ARP (Address Resolution Protocol, which can be understood as a network "directory inquiry" service) feature.
3. When inserting or removing a SIM card, it is essential to disconnect the power to prevent data loss or damage to the device.

## Scenario 2: Wired Networking

**Objective**: Connect the IR602 to the internet via a wired Ethernet connection.

**Prerequisites**: An Ethernet cable is available, and the upstream network device is functioning properly.

**Estimated Time**: About 5 minutes.

**Operation Steps**:
1. Connect an Ethernet cable from the WAN port of the IR602 to the upstream network device (such as a modem or another router).
2. The device's WAN interface has DHCP service enabled by default. It will automatically obtain an IP address and establish an internet connection.

![alt text](./img/image-6.png)
<p align="center"><strong>Figure 3-3 Wired Connection</strong></p>

3. To configure wired connection parameters, navigate to 【Internet】→【Uplink Table】, add or select the WAN interface, and click "Edit."
4. Select the connection type:
   - **DHCP**: The default mode. The device automatically obtains an IP address from the upstream device.
   - **Static IP**: Manually configure an IP address, subnet mask, gateway, and DNS provided by the ISP or within the same network segment as the upstream device.

![alt text](./img/image-7.png)
<p align="center"><strong>Figure 3-5 Static IP Configuration</strong></p>

   - **PPPoE**: Configure broadband dial-up with the username and password provided by the ISP.

![alt text](./img/image-8.png)
<p align="center"><strong>Figure 3-6 PPPoE Configuration</strong></p>

5. Click "Save" to apply the settings.

**Verification Methods**:
1. Check the NET indicator light. A steady green light indicates the WAN port is connected normally.
2. Navigate to 【Status】→【Link Monitor】 to verify the WAN link status.

**Common Issues**:
- Unable to obtain an IP address automatically: Verify the upstream device has DHCP enabled, or configure a static IP.
- PPPoE dial-up failure: Verify the username and password are correct.


## Scenario 3: Wi-Fi STA Networking

**Objective**: Connect the IR602 to an existing Wi-Fi network as a client (STA).

**Prerequisites**: The target Wi-Fi network (SSID) is within range, and the SSID name and password are known.

**Estimated Time**: About 5 minutes.

**Operation Steps**：
1. Navigate to the menu: 【Wi-Fi】→【Wi-Fi List】.
2. Click the **Add/Edit** button, then configure parameters such as SSID name, authentication method and password.
3. Click **Save**.

**Verification Methods**：
1. Use a wireless terminal to search for the configured SSID.
2. Enter the password and confirm successful connection and network access.

**Cautions**：
- The device comes with two primary SSIDs for 2.4 GHz and 5 GHz by default. The frequency bands of primary SSIDs cannot be modified or deleted.
- The frequency band of an added SSID is not editable. Its channel automatically matches that of its associated primary SSID.
- If a Wi-Fi (STA) interface is created under the 【Internet】 menu, all SSIDs operating on the same frequency band as the Wi-Fi (STA) interface will remain disabled until the Wi-Fi (STA) interface is removed.

---


## Scenario 4: Connect to DeviceLive Cloud Platform

**Objective**: Connect the device to the DeviceLive Platform to enable remote management and monitoring.

**Prerequisites**: The device has Internet access. The device serial number and MAC address are available.

**Estimated Time**: About 10 minutes.

**Operation Steps**：
1. Open a web browser (Google Chrome recommended) and navigate to [https://device.inhandcloud.com]to access the DeviceLive login/registration page. Click **Create Now** to create a platform account.

![alt text](./img/image-9.png)
<p align="center"><strong>Figure 3-1 DeviceLive Register</strong></p>

2. After completing account registration, log in to the InHand Cloud Service Platform with your username and password, then select the **DeviceLive** service.

![alt text](./img/image-10.png)
<p align="center"><strong>Figure 3-2 DeviceLive Login</strong></p>

3. Once inside the DeviceLive platform, go to the **Devices** menu and click the **Add** button. Fill in the device name, serial number and MAC address, then click **Finish**.

![alt text](./img/image-11.png)
<p align="center"><strong>Figure 3-3 Add Device</strong></p>

**Verification Methods**：
1. Check the device online status in the **Devices** list on the DeviceLive platform.
2. Click the **Device Name** to view detailed device information.

**Common Issues**：
- Device shows offline: Verify that the device has normal Internet connectivity and confirm the serial number and MAC address are entered correctly.
- The IR602 applies a license policy with free basic features and paid advanced features. Standard device management and monitoring functions are available for free. To use features such as cloud connectivity, purchase an advanced license under **Subscriptions > Licenses**.

# Chapter 4 Feature Descriptions and Parameter Reference

## 4.1 Device Monitoring

After the device is added to the DeviceLive platform, you can manage and monitor the network via the cloud platform. Remote access to the device’s local Web UI through the cloud platform is also supported.

### 4.1.1 Device Overview

**Overview**

In the **Devices** list, click the **Device Name** to view detailed device information, including basic device information, interface status, traffic statistics, cellular signal strength, and the number of Wi‑Fi connected client devices.

![alt text](./img/image-12.png)
<p align="center"><strong>Figure 4-1 Overview</strong></p>

**Traffic Usage**

On the **Device > Data Usage** page, you can view historical traffic data for each uplink port.

![alt text](./img/image-13.png)
<p align="center"><strong>Figure 4-2 Data Usage</strong></p>

**Cellular Signal**

On the **Device > Cellular Signal** page, you can view historical data of various cellular signal parameters, including signal strength, RSSI, RSRP, RSRQ and SINR.

![alt text](./img/image-14.png)
<p align="center"><strong>Figure 4-3 Cellular Signal</strong></p>

### 4.1.2 Device Information

With the **Remote Access** feature of DeviceLive, you can view and configure the device in real time. Check the target device and click **Remote Access** to open the local login page of the device.

![alt text](./img/image-15.png)
<p align="center"><strong>Figure 4-4 Remote Access</strong></p>

**Device Information**

In the 【Dashboard】 interface, basic device information is displayed at the top, including the device name, model, serial number, MAC address, online duration, and upstream interface address.

![alt text](./img/image-17.png)
<p align="center"><strong>Figure 4-5 Dashboard Device Information</strong></p>

| Parameter | Description |
|-----------|-------------|
| Name | Identifies the device's name, initially set to "IR602" but can be customized |
| MAC Address | Identifies the device's physical MAC address |
| Local Gateway Address | The default gateway address of the device's subnet |
| Model | Specifies the device's specific model, which can help determine if it supports cellular and WLAN features |
| Uptime | Reflects the device's running time since it was powered on |
| System Time | Displays the device's time zone and system time |
| Serial | A unique code that serves as an identifier for the device and can be used for indexing or adding the device to a platform account |
| Internet Access | The upstream interface used by the device for internet connectivity |
| License Status | Information about the applied license on the device, distinguishing between Small Star Cloud Manager Basic and Small Star Cloud Manager Professional |
| Firmware Version | Shows the device's current software version |
| Uplink IP | The IP address of the upstream interface used for device internet connectivity |

**Interface Status**

In the **Dashboard > Interface Status** feature, the operational status of each interface can be visually inspected. By clicking the "Interface Icon," detailed information for each interface can be accessed in a pop-up box on the right-hand side of the interface.

![alt text](./img/image-16.png)
<p align="center"><strong>Figure 4-6 Interface Status</strong></p>

**Traffic Statistics**

The usage of traffic on each upstream interface since the router was powered on can be monitored through the **Dashboard > Traffic Statistics** feature. The data in traffic statistics will reset after the device is rebooted. If historical traffic records are needed, they can be accessed on the device's details page within DeviceLive.

![alt text](./img/image-18.png)
<p align="center"><strong>Figure 4-7 Traffic Statistics</strong></p>

**Wi-Fi Connections**

In the **Dashboard > Wi-Fi Client Count** feature, the number of active SSIDs on the IR602 and the number of connected clients under each SSID can be checked.

![alt text](./img/image-19.png)
<p align="center"><strong>Figure 4-8 Wi-Fi Connections</strong></p>

**Clients Traffic Top 5**

In the **Dashboard > Top 5 Client Traffic** feature, the current ranking of client traffic usage for devices connected to the router can be viewed. It displays up to 5 records, and when a client disconnects, its statistical data will be cleared.

![alt text](./img/image-20.png)
<p align="center"><strong>Figure 4-9 Clients Traffic Top 5</strong></p>

## 4.2 Status

Under the **Status** function, the device uplink status, operation logs, and events can be viewed to accurately grasp the device operation status.

### 4.2.1 Link Monitor

The **Status > Link Monitoring** feature displays the health status of each upstream link, along with information about throughput, latency, packet loss, and signal strength for each interface.

![alt text](./img/image-21.png)
<p align="center"><strong>Figure 4-10 Link Monitoring</strong></p>

### 4.2.2 Cellular Signal

The **Status > Cellular Signal** feature displays the signal strength of SIM cards under the cellular interface, along with parameters such as RSSI, SINR, and RSRP.

![alt text](./img/image-22.png)
<p align="center"><strong>Figure 4-11 Cellular Signal</strong></p>

### 4.2.3 Clients

The **Status > Clients** feature displays detailed information about wired and wireless clients connected to the router, including names, addresses, MAC addresses, VLANs, connected subnets, traffic usage, and online duration.

![alt text](./img/image-23.png)
<p align="center"><strong>Figure 4-12 Clients</strong></p>

### 4.2.4 VPN

The **Status > VPN** feature displays information about IPsec VPN and L2TP VPN, including their status, traffic, and the duration of the most recent connection.

![alt text](./img/image-24.png)
<p align="center"><strong>Figure 4-13 VPN Status</strong></p>

**Routing Table**

You can view routing status under **Status > Routing Table**. Connected indicates an active route, while Disconnected indicates an inactive route.

![alt text](./img/image-25.png)
<p align="center"><strong>Figure 4-14 Routing Table</strong></p>

**Passthrough**

You can judge whether IPPT works normally through the configuration status of Passthrough.

![alt text](./img/image-26.png)

<p align="center"><strong>Figure 4-15 Passthrough Status</strong></p>

| Parameter | Description |
|------|------|
| Status | Indicates whether Passthrough operates normally |
| Passthrough WAN | Shows the WAN interface where Passthrough runs |
| Passthrough LAN | Shows the physical interface designated for Passthrough to obtain the passthrough IP address |
| Passthrough IP/Mask | Shows the IP address and subnet mask obtained via Passthrough |
| Passthrough Gateway Address | Shows the gateway address for Passthrough |
| Passthrough DNS1/2 | Shows the DNS servers used for address resolution by the Passthrough function |
| Passthrough MAC | Shows the MAC address of the terminal acquiring the passthrough address |
| Address Allocation Status | Shows the status of passthrough address assignment |
| Lease Timeout | Shows the DHCP lease time for Passthrough |


**Session**

The Session page provides real-time monitoring of all active network connections and historical session records on the device. It helps you understand the network communication status of the device and troubleshoot connection anomalies.

![alt text](./img/image-27.png)
<p align="center"><strong>Figure 4-16 Session</strong></p>

**I/O**

You can check the operating status of the device’s I/O ports via **Status > I/O**.
| Parameter | Description |
|------|------|
| Port | Corresponding physical IO1 and IO2 ports |
| Mode | IO operating mode: Input, Output |
| Current Level | Current logic level of the IO port: High Level, Low Level|

![alt text](./img/image-28.png)
<p align="center"><strong>Figure 4-17 I/O Status</strong></p>

**Events**

The **Status > Events** feature displays event information related to the device's operation to help users understand the device's operational status.

![alt text](./img/image-29.png)
<p align="center"><strong>Figure 4-18 Events</strong></p>

Currently supported event types are as follows:
- Login Successful/Failed
- Configuration changed
- CPU uilization is too high
- Memory utilization is too high
- VPN status changed
- Uplink status changed
- Client status changed
- Uplink switched
- WAN/LAN1 switched
- Upgrade
- Reboot
- Detection status changed
- Cellular traffic reaches the threshold
- Carrier switched

**Logs**

The **Status > Logs** feature allows users to examine the system logs, which contain information about the device's operational history. When the device encounters issues, technical personnel can use these logs for troubleshooting and diagnosis.

![alt text](./img/image-30.png)
<p align="center"><strong>Figure 4-19 Logs</strong></p>

The log management functions are as follows:

1. **Download Logs**: Download the device's operational logs.
2. **Download Diagnostic Logs**: Download the device's diagnostic logs, which include system operation logs, device information, and device configurations.
3. **Clear Logs**: Clear the device's operational logs. This does not clear the device's diagnostic logs.

## 4.3 Internet

The Internet function is used to configure the parameters and operational modes of each upstream interface. The IR602 supports three access network modes: wired, cellular, and Wi-Fi. The device comes with two non-removable upstream links by default: WAN1 and Cellular. It can support up to four upstream links, including WAN1, Cellular, and Wi-Fi (STA). Wi-Fi (STA) interfaces need to be manually added and can be removed as needed.

### 4.3.1 Wired Connection

The parameters and operation modes for each upstream interface can be configured under the **Internet** function. The IR602 supports three access network modes: wired, cellular, and Wi-Fi. It can support up to three upstream links, including WAN, cellular, and Wi-Fi (STA).
The WAN and Wi-Fi (STA) interfaces need to be manually added and can be deleted as needed; the cellular upstream link cannot be deleted.

![alt text](./img/image-31.png)
<p align="center"><strong>Figure 4-20 Wired Connection Configuration</strong></p>

**DHCP**: The device's WAN interface has DHCP service enabled by default. Simply connect the WAN interface to the internet using an Ethernet cable, and it will automatically establish an internet connection.

**Static IP**: Users have the option to manually configure an address either obtained from their internet service provider or one that is within the same network segment as their upstream device. Once the configuration is complete, the router will access the network via the specified static IP address.

![alt text](./img/image-32.png)
<p align="center"><strong>Figure 4-21 Static IP Configuration</strong></p>

**PPPoE**: Users have the option to configure broadband dial-up. Once the configuration is complete, the router will establish an internet connection through the broadband dial-up.

![alt text](./img/image-33.png)
<p align="center"><strong>Figure 4-22 PPPoE Configuration</strong></p>

**Cautions**：
- After adding a WAN interface, the original LAN1 port will switch its role to WAN.
- After deleting the WAN interface, the former WAN port will revert to LAN1.
- Deleting the WAN interface will remove all associated configurations including static routes, inbound/outbound rules, port forwarding, policy routing.

### 4.3.2 Wireless Connection

The IR602 supports connecting as a client to an on-site AP's network. To do this, click the "Add" button, select "Wi-Fi (STA)," and fill in the required parameters, including the SSID name and password.

![alt text](./img/image-36.png)
<p align="center"><strong>Figure 4-23 Wi-Fi STA Configuration</strong></p>

**Cautions:**
1. Upon adding Wi-Fi (STA), the IR602 will automatically disable SSIDs in the same frequency band within the Wi-Fi settings, and the status field for those SSIDs cannot be modified.
2. After removing Wi-Fi (STA), the "Status" field and SSIDs in the same frequency band within the Wi-Fi settings can be modified.
3. When Wi-Fi (STA) is deleted, all configuration associated with the Wi-Fi (STA) interface, including static routes, inbound/outbound rules, port forwarding, policy routing, and traffic shaping settings, will be removed.


### 4.3.3 5G/4G Connection

In the usual scenario, upon inserting the SIM card and connecting the antennas, the IR602 router will automatically establish a dial-up connection and connect to the network when powered on.

To configure APN (Access Point Name) parameters, select the "Cellular" interface in the 【Internet】 menu and click the "Edit" button to access the APN parameter configuration interface.

![alt text](./img/image-34.png)
<p align="center"><strong>Figure 4-24 Cellular APN Configuration</strong></p>

The IR602 also includes a traffic policy feature. Once the policy is enabled, the SIM card will take specific actions when the traffic reaches a threshold. Traffic usage statistics will reset at the beginning of the next month.

Select the "Cellular" interface in the 【Internet】 menu and click the "Policy" button to access the SIM card's policy parameter configuration interface.

![alt text](./img/image-35.png)
<p align="center"><strong>Figure 4-25 Cellular Traffic Policy</strong></p>

| Action | Description |
|--------|-------------|
| Notification | Generates an event when traffic reaches the threshold but does not stop forwarding regular business traffic |
| Cloud Management Only | Generates an event when traffic reaches the threshold, allowing only the forwarding of cloud-based management traffic while blocking access to the internet for regular business traffic |
| Switch the SIM Card | Generates an event when traffic reaches the threshold and switches to another SIM card for internet access |

**Cautions:**
1. In certain dedicated network scenarios, it may be necessary to manually disable the "Link Detection" function under the 【Internet】 menu to prevent cellular connectivity issues caused by unsuccessful detection.
2. In some cases, manual configuration of the subnet mask for the cellular interface may be required to ensure the proper functioning of the ARP feature.
3. When inserting or removing a SIM card, it is essential to disconnect the power to prevent data loss or damage to the device.


### 4.3.4 Uplink Table

The WAN and Wi-Fi (STA) interfaces can be added, edited, or removed in the **Internet > Uplink Table**. The priority of each interface can also be adjusted by dragging the "Priority" icon. Interfaces are arranged from top to bottom based on their priority, with higher priority interfaces taking precedence in determining the current upstream interface for device operation.

![alt text](./img/image-37.png)
<p align="center"><strong>Figure 4-26 Uplink Table</strong></p>

### 4.3.5 Uplink Settings

Link detection settings and collaboration modes between different upstream interfaces can be configured through the **Internet > Upstream Link Settings** feature.

![alt text](./img/image-38.png)
<p align="center"><strong>Figure 4-27 Uplink Settings</strong></p>

**Link Detection Switch:** The device has link detection functionality enabled by default. However, in certain specialized network environments where external communication is not possible, users may need to manually disable link detection. When link detection is turned off, latency, jitter, packet loss, signal strength, and other information for upstream interfaces will not be viewable in the 【Status】 menu.

**Notes:**
1. Modifying settings in the Internet menu can potentially lead to a disruption in device connectivity. Exercise caution when making changes.
2. When the link detection address is left empty, the default behavior is to detect the DNS address via the upstream interface. If a detection address is specified, all upstream interfaces will only detect the address provided.
3. In the router's link backup mode, users can customize detection parameters, and the device will switch links based on the enabled detection items. When detection items are not enabled, upstream link switching will only occur based on priority and link connectivity.
4. In the device's load balancing mode, all operational upstream links will forward business traffic, provided they are functioning correctly.

## 4.4 Local Network

The Local Network feature allows users to define local subnets, including the address range, VLAN ID, DHCP services, and other related parameters. After the configuration is complete, the settings must be applied to the device's LAN port through Interface Management or to the desired SSID in the Wi-Fi settings. This ensures that client devices can connect to the local network according to the planned network addresses.

![alt text](./img/image-40.png)
<p align="center"><strong>Figure 4-28 Local Network List</strong></p>

Click the "Add/Edit" button to add a new local network or edit an existing one.

![alt text](./img/image-39.png)

<p align="center"><strong>Figure 4-29 Local Network Add/Edit</strong></p>

### Parameter Description

- Name: Identifies the network. Users can select this network for application under **Wi-Fi** and **Interface Management**.
- IP Address/Mask: Gateway address to access the router via LAN port or Wi-Fi. Default value: 192.168.2.1.
- DHCP Server: Clients connected to the router obtain IP addresses through this function. Enabled by default. The address pool range is automatically generated based on the **IP Address/Mask**.

### Notes

1. The default local network cannot be deleted. Only the IP address/subnet mask and DHCP server settings can be modified.
2. Once a local network is added, its mode cannot be changed.

## 4.5 Wi-Fi

### 4.5.1 SSIDs

The IR602 functions as an Access Point (AP) to provide multiple SSID wireless network access. Different SSIDs can be configured for various purposes and configurations.

![alt text](./img/image-41.png)
<p align="center"><strong>Figure 4-30 Wi-Fi List</strong></p>

To add a new SSID or edit an existing one, navigate to 【Wi-Fi】→【Wi-Fi List】 and click the "Add/Edit" button.

![alt text](./img/image-42.png)
<p align="center"><strong>Figure 4-31 SSID Add/Edit</strong></p>

**Notes:**

1. The device is equipped with default 2.4GHz and 5GHz main SSIDs. The frequency bands of these main SSIDs cannot be modified, and the main SSIDs cannot be deleted.
2. Once an SSID is added, its frequency band cannot be changed. The added SSID automatically uses the same channel as its corresponding main SSID.
3. If a user creates a Wi-Fi (STA) interface in the 【Internet】 menu with the same frequency band as an existing SSID, that SSID cannot be enabled until the Wi-Fi (STA) interface is deleted.

### 4.5.2 Radio

Navigate to the **Radio** page to configure radio parameters for the 2.4 GHz and 5 GHz wireless bands. These parameters directly affect Wi-Fi coverage range, stability and throughput.

![alt text](./img/image-38.png)
<p align="center"><strong>Figure 4-32 Radio configuration</strong></p>

## 4.6 Routing

### 4.6.1 Static Routes

Static routing refers to fixed routing rules manually configured by the user, which specify the next-hop gateway through which traffic destined for a given destination network should be forwarded.

![alt text](./img/image-43.png)
<p align="center"><strong>Figure 4-33 Static Routes</strong></p>

### 4.6.2 BGP

BGP (Border Gateway Protocol) is a path-vector routing protocol commonly used to exchange reachability information between different autonomous systems (AS).
![alt text](./img/image-44.png)
<p align="center"><strong>Figure 4-34 BGP</strong></p>

### 4.6.3 OSPF

OSPF (Open Shortest Path First) is a link-state-based dynamic routing protocol used to automatically discover the network topology and compute optimal paths in large or multi-segment networks.

![alt text](./img/image-45.png)
<p align="center"><strong>Figure 4-35 OSPF</strong></p>

## 4.7 VPN

In the **VPN** menu, users can configure IPSec VPN and L2TP VPN parameters to establish secure network connections.

### 4.7.1 IPSec VPN

IPSec (Internet Protocol Security) VPN is a protocol suite designed to enhance network communication security by encrypting and authenticating data transmission. It is widely used for establishing secure remote access, site-to-site connections, and virtual private networks. IPSec VPN ensures data protection and security through encryption and authentication methods.

To add a new IPSec VPN, navigate to **VPN > IPSec VPN** and click the "Add" button.

![alt text](./img/image-46.png)
<p align="center"><strong>Figure 4-36 IPSec VPN Configuration</strong></p>

Once configurations are completed at both ends, the tunnel can be established. The tunnel establishment status can be checked in the **Status > VPN** menu.

The IPSec VPN parameters are described in the following table.

| Parameter | Description |
|-----------|-------------|
| Name | The user-assigned name for the IPSec VPN, used for local management and identification |
| IKE Version | The version of the Internet Key Exchange (IKE) protocol. Supports IKEv1 and IKEv2 |
| Pre-Shared Key | A secret shared key that must be configured identically on both devices for authentication during IKE negotiation |
| Internet Interface | The upstream interface used to establish the IPSec VPN locally |
| Tunnel Mode | The encapsulation mode for IPSec on IP packets. Supports tunnel mode and transport mode |
| Peer Address | The address of the remote endpoint with which the IR602 establishes the IPSec tunnel |
| Local Subnet | The subnet addresses that need to communicate through the IR602 IPSec VPN tunnel |
| Remote Subnet | The subnet address on the other end of the tunnel that needs to communicate through the IPSec VPN tunnel |

**IKE Policy Parameters:**

| Parameter | Description |
|-----------|-------------|
| Encryption Method | The encryption algorithm used by IKE. Options: DES, 3DES, AES128, AES192, AES256. Default: AES128 |
| Authentication Method | The authentication algorithm used by IKE. Options: MD5, SHA1, SHA2-256, SHA2-384, SHA2-512. Default: SHA1 |
| DH Group | The Diffie-Hellman exchange parameters used during IKE phase key negotiation. Options: 1, 2, 5, 14, 15, 16, 19, 20 |
| Timeout | The IKE SA (Security Association) lifetime, in seconds. Default: 86400 |

**IPSec Policy Parameters:**

| Parameter | Description |
|-----------|-------------|
| Security Protocol | The security protocol used by the ESP protocol |
| Encryption Method | The encryption algorithm used by the ESP protocol. Options: DES, 3DES, AES128, AES192, AES256. Default: AES128 |
| Authentication Method | The authentication algorithm used by the ESP protocol. Options: MD5, SHA1, SHA2-256, SHA2-384, SHA2-512. Default: SHA1 |
| PFS Group | An additional key exchange performed in Phase 2 to enhance communication security. Options: 1, 2, 5, 14, 15, 16, 19, 20 |
| Timeout | The IPSec SA lifetime, in seconds. Default: 86400 |

**Notes:**

1. The device with the public IP address acts as the server, and client devices connect to it using the server's public IP address.


### 4.7.2 L2TP VPN

The Layer 2 Tunneling Protocol (L2TP) is a Layer 2 VPN protocol designed to establish secure point-to-point or site-to-site virtual private network connections. It is commonly used for remote access and branch office connectivity, creating secure communication channels to protect the privacy and integrity of data transmission.

**L2TP Work as Client**

The IR602 can act as an L2TP client and establish a tunnel with a remote L2TP server. To configure an L2TP client, navigate to **VPN > L2TP VPN > Client** and click the "Add" button.

![alt text](./img/image-47.png)
<p align="center"><strong>Figure 4-37 L2TP VPN Client Configuration</strong></p>

The L2TP client parameters are described in the following table.

| Parameter | Description |
|-----------|-------------|
| Name | The name of the L2TP client for local identification |
| Status | The switch to enable or disable the L2TP client tunnel |
| NAT | The switch for NAT functionality when forwarding with the L2TP client |
| Upstream Interface | The upstream interface used for communication between the L2TP client and the server |
| Server Address | The communication address of the remote L2TP server |
| Username/Password | Credentials that must be configured identically on both ends during L2TP negotiation |
| Authentication Mode | The L2TP authentication mode |
| Enable Tunnel Authentication | When enabled, both ends must configure identical usernames and passwords for tunnel authentication |

**Work as Server**

A typical L2TP server is usually deployed at the headquarters of an enterprise, serving as a remote access server for mobile office or branch offices. To configure the L2TP server settings, navigate to **VPN > L2TP VPN > Server** to access the L2TP server editing page.

![alt text](./img/image-48.png)
<p align="center"><strong>Figure 4-38 L2TP VPN Server Configuration</strong></p>

The L2TP server parameters are described in the following table.

| Parameter | Description |
|-----------|-------------|
| Name | The name of the L2TP server. Not editable |
| Status | The on/off switch for the L2TP server function. Default: off |
| Upstream Interface | The upstream interface used by the L2TP server |
| VPN Communication Address | The gateway address for L2TP clients, which can be assigned to devices within the IP address pool |
| Address Pool | The IP address pool used for communication when L2TP clients connect |
| Username/Password | Credentials that must be identical on both ends for L2TP negotiation |
| Authentication Mode | The L2TP authentication mode |
| Enable Tunnel Verification Function | When enabled, the usernames and passwords for tunnel verification on both ends must be identical |

### 4.7.3 WireGuard VPN

WireGuard is a lightweight, high-performance VPN protocol optimized for low-latency, secure communication in industrial IoT scenarios.

![alt text](./img/image-55.png)
<p align="center"><strong>Figure 4-39 WireGuard VPN Configuration</strong></p>

**Core Configuration Items**
| Parameter | Description | Configuration Guidelines |
|-----------|-------------|-------------|
| Name | User-defined name for the WireGuard tunnel | Enter a descriptive name (e.g., Factory-Site-VPN) to identify the tunnel for management purposes. |
| Status | Toggle to enable/disable the WireGuard tunnel | Defaults to Enabled (green) to activate the tunnel once configured. |
| Tunnel IP Address/Netmask | 	Virtual IP address and subnet mask for the local tunnel interface | Enter an IP (e.g., 10.0.0.1) and netmask (e.g., 255.255.255.0) to define the tunnel’s internal network segment. |
| Shared Connection(NAT) | Toggle to enable NAT for shared tunnel access	 | Disable for point-to-point industrial connections; enable if multiple devices need to share the tunnel. |
| Listening Port | UDP port on which the router listens for WireGuard connections | Defaults to 51820 (standard WireGuard port); keep unless conflicting with other services. |
| MTU | Maximum | Transmission Unit for the tunnel	Defaults to 1500; reduce to 1420 if encountering fragmentation over public networks. |
| Private Key | Local private key for WireGuard encryption | Generate using the WireGuard key generator at the bottom of the page, then paste here. |


**Peer Settings**

This section configures remote peers (other devices connecting to this WireGuard tunnel).

| Field | Description |
| Peer Name | Descriptive name for the remote peer (e.g., Remote-Sensor-Gateway). |
| End Point | Public IP address and port of the remote peer (e.g., 203.0.113.5:51820). |
| Permitted IP / Mask | IP segments allowed to communicate through the peer (e.g., 192.168.2.0/24 for a remote factory subnet). |
| Public Key | Public key of the remote peer (provided by the peer device). |
| Pre-Shared Key | Optional additional encryption key for enhanced security (generate via the key generator). |
| Persistent Keepalive | Interval (seconds) for sending keepalive packets (e.g., 25 to maintain NAT traversal). |
	
**WireGuard Key Generator**

Built-in tool to generate secure keys for the tunnel:
● Private Key: Local device’s private key (keep confidential).
● Public Key: Corresponding public key (share with peers).
● Pre-Shared Key: Optional per-peer key for extra security.
Click Generator to create a new key, then copy it to the corresponding field.

**Operation Steps**
1. Enter a Name and configure the Tunnel IP Address/Netmask.
2. Generate a Private Key using the key generator and paste it into the field.
3. (Optional) Enable Shared Connection(NAT) if needed.
4. Add peers by clicking + Add and filling in their details (End Point, Public Key, etc.).
5. Click Save to apply the configuration.

### 4.7.4 OpenVPN

OpenVPN is an open-source, flexible VPN protocol that establishes secure point-to-point or site-to-site connections over public networks via encrypted tunnels, and is widely used in industrial remote operation and maintenance as well as cross-network data transmission.

 **Work as Server**

The Server mode is used to accept VPN connection requests from clients.

Key configuration items are as follows:
| Configuration Item | Description | Configuration Recommendation |
| Status | Toggle to enable/disable the OpenVPN Server | Disabled by default; enable after completing configuration. |
| Server Name  | Custom identifier for the server | Enter a descriptive name (e.g., Factory-OpenVPN-Server) for easier management. |
| Server Address | Public address the server uses to accept connections | Two options: 1. Specify the Uplink Interface: Select an existing interface (e.g., Cellular) to automatically use its public IP. 2. Customize: Manually enter a public IP or domain name. |
| Port | Listening port for OpenVPN connections | Defaults to 1194 (standard port); keep unless conflicting with other services. |
| Protocol Type | Transport protocol | Defaults to UDP (lower latency, ideal for industrial scenarios); select TCP if firewall traversal is needed. |
| Server's Virtual Address / Mask Length | Virtual IP of the server within the VPN tunnel | Enter a network segment (e.g., 10.8.0.1/24) for communication between tunneled devices. |
| Client's Virtual IP Range | Pool of virtual IPs assigned to connecting clients | Enter a range within the same subnet as the server (e.g., 10.8.0.10-20). |
| Update Client DNS | Whether to push DNS server addresses to clients	 | Enable in industrial scenarios to ensure proper resolution of internal domain names. |
	
Advanced Settings:
| Configuration Item | Description |
| Client to Client | Allow VPN clients to communicate with each other |
| Shared Login Credentials | Allow multiple clients to log in with the same account |
| Redirect the Client's Gateway | Force all client traffic to pass through the VPN tunnel |
| Interface Type | Virtual interface type for the VPN tunnel |
| Reset Certificates | Regenerate encryption certificates for the server and clients |
| Local Subnet | Local network segments accessible to clients |

Client Settings:
| Configuration Item | Description |
| Username | Unique identifier for the VPN client, used for authentication. |
| Password | Secure password for the client account, must be kept confidential and shared only with authorized users. |
| IP Address/Subnet Mask | Fill in the subnet of the client network.   |

	
 **Work as Client**
The Client mode is used to connect to a remote OpenVPN Server, configured via the "Add OpenVPN Client" pop-up:

| Configuration Item | Description | Configuration Recommendation |
| Name | Custom identifier for the client | Enter a descriptive name (e.g., Connect-to-HQ-OpenVPN). |
| Status | Toggle to enable/disable the OpenVPN Client | Disabled by default; enable after completing configuration. |
| OpenVPN configuration file | Import the .ovpn configuration file provided by the server | Click Upload to avoid manual parameter entry errors. |
| Username / Password | Credentials for server authentication | Provided by the server administrator for identity verification. |
| Interface Type | Virtual interface type | Must match the server setting (default: TUN). |

## 4.8 Security

In the **Security** menu, users can configure advanced features related to firewalls, policy routing, and traffic shaping.

### 4.8.1 Firewall

The firewall includes functions such as inbound rules, outbound rules, port forwarding, MAC address filtering, and more.

**Inbound/Outbound Rules**

Traffic in/out control can be implemented based on interfaces through the **Security > Firewall > Outbound Rules/Inbound Rules** feature. For example, if a user is subjected to a significant amount of attacks from a specific source IP address, inbound firewall rules can be used to restrict traffic from that IP address.

![alt text](./img/image-49.png)
<p align="center"><strong>Figure 4-40 Inbound/Outbound Rules Configuration</strong></p>

Furthermore, IT personnel can utilize outbound firewall rules to restrict certain users' access to external networks. Inbound and outbound rules share the same configurable content, with the only distinction being the default rules.

The parameters for inbound/outbound rules are described in the following table.

| Parameter | Description |
|-----------|-------------|
| Name | The name of the inbound/outbound rule for local identification. |
| Status | Rule function switch. |
| Interface | For outbound rules, it specifies the upstream interface where traffic leaves the router. For inbound rules, it specifies the upstream interface where traffic enters the router. |
| Protocol | Match traffic based on the protocol type, with options like Any, TCP, UDP, ICMP, or custom. |
| Source | Match the source address for traffic, supporting custom, with the default as Any. |
| Destination | Match the destination address for traffic, supporting custom, with the default as Any. |
| Action | Action taken for matching traffic in inbound/outbound rules, supporting allow and deny. |
| Inbound Rules | Traffic management rules for external network accessing the router, with the default as deny all. |
| Outbound Rules | Traffic management rules for traffic going out through the router, with the default allowing all. |

Users can adjust the priority of inbound and outbound rules.

**Port Forwarding**

Port forwarding, also known as port mapping or port redirection, is used to redirect network packets from one network port (or address) to another network port or address. Users can configure port forwarding rules under **Security > Firewall > Port Forwarding**. When external traffic accesses a specific port on the router, the device forwards the data to the corresponding port of an internal client, enabling external access to services inside the router.

For example, when a user needs to access the service on port 1024 of the internal client at 192.168.2.10 from the external network, this client's port can be mapped to port 1024 under the WAN1 interface. External users only need to enter `https://WAN address:1024` in their browser to access the target device's data, where the "WAN address" is the IP address of the WAN interface.

![alt text](./img/image-50.png)
<p align="center"><strong>Figure 4-41 Port Forwarding Configuration</strong></p>

The parameters for port forwarding rules are described in the following table.

| Parameter | Description |
|-----------|-------------|
| Name | The name of the port forwarding rule, used for local identification. |
| Status | The on/off switch for the port forwarding rule. |
| Interface | The upstream interface that provides mapping functionality for internal clients. The upstream interface needs public IP address support. |
| Protocol | The protocol type of the traffic for port mapping, supports TCP, UDP, and TCP & UDP. |
| Public Port | The port number on the upstream interface that provides mapping. |
| Local Address | The address of the target device located under the router that the external network needs to access. |
| Local Port | The port of the target device that the external network needs to access. It needs to be consistent with the public port input range. |

**NAT**

NAT (Network Address Translator) is a technology used to use a private address in a local network and switch to a global IP address when connecting to the Internet. You can set source or destination address translation as needed  in "Security > Firewall > NAT".

![alt text](./img/image-51.png)
<p align="center"><strong>Figure 4-42 NAT</strong></p>

The parameters for NAT rules are described in the following table.

| Parameter | Description |
|-----------|-------------|
| Name | The user sets a name for the rule. |
| Type | The type of this rule. |
| Protocol | The scope of the rule. |
| Source | The source IP address that needs to be translated. |
| Destination | The destination IP address that needs to be translated. |
| Converted Address | Translated address. |

The Type parameter supports the following options:

| Type | Description |
|------|-------------|
| SNAT | Translate the source IP address. |
| DNAT | Translate the destination IP address. |

The Protocol parameter supports the following options:

| Protocol | Description |
|----------|-------------|
| Any | This rule is effective for all protocols. |
| TCP | This rule takes effect only for TCP protocol. |
| UDP | This rule takes effect only for UDP protocol. |
| TCP&UDP | This rule takes effect only for TCP and UDP protocols. |

**MAC Address Filter**

MAC address filtering involves allowing or disallowing devices in a MAC address list to access the internet, which means controlling LAN devices' internet access requests through MAC address filtering on the router. Users can configure MAC address filtering rules in **Security > Firewall > MAC Address Filtering**.

Multiple MAC addresses can be created in the list, address descriptions can be added, and the list can be set to allow only the MAC addresses to access the network (whitelist), or block MAC addresses in the list from accessing the network (blacklist).

![alt text](./img/image-52.png)
<p align="center"><strong>Figure 4-43 MAC Address Filtering Configuration</strong></p>

**Domain Name Filtering**

Domain filtering allows you to block (or allow) client access to the domains specified in the list. You can configure which domains are accessible or blocked under **Security > Firewall > Domain Filtering**.

You can add multiple rules to the domain filtering table to either allow clients to access certain domains (whitelist) or prohibit clients from accessing certain domains (blacklist).

![alt text](./img/image-53.png)
<p align="center"><strong>Figure 4-44 Domain Name Filtering</strong></p>

### 4.8.2 Policy-Based Routing

**Policy-Based Routing** is a feature that allows you to define routing policies based on actual requirements, enabling different data flows to be forwarded over different links as needed. This enhances the flexibility and controllability of routing selection, while improving link utilization efficiency and reducing enterprise costs.

Click **Add** under **Security > Policy-Based Routing** to create a new policy-based routing rule.
 
> **Note:** The source address and destination address must not both be set to **Any** during configuration.

![alt text](./img/image-54.png)
<p align="center"><strong>Figure 4-45 Policy-Based Routing Configuration</strong></p>

## 4.9 Authentication

The IR602 currently supports Portal authentication and 802.1X authentication.

### 4.9.1 Portal

The IR602 provides two types of Portal authentication: built-in lightweight authentication on the device and external RADIUS wireless authentication.

![alt text](./img/image-56.png)
<p align="center"><strong>Figure 4-46 Portal Configuration</strong></p>

1. Internal Portal
Users can choose between two local authentication modes: **Click-Passthrough** and **User Authentication**. The device also supports authenticating specified SSIDs, as well as customizing the welcome message, title, logo, background image, etc. on the redirected access page.
![alt text](./img/image-57.png)
<p align="center"><strong>Figure 4-47 Internal Portal Configuration</strong></p>

2.External Portal
You can choose either Third-Party Authentication or Radius authentication. When a third-party RADIUS server is deployed, wireless terminals can join the network via RADIUS authentication. Under **Wi-Fi > SSIDs**, select WPA or WPA2, and enter the authentication server address, port, and shared key.
![alt text](./img/image-57.png)
<p align="center"><strong>Figure 4-48 External Portal Configuration</strong></p>

### 4.9.2 802.1X

802.1X is a port-based network access control protocol used to authenticate devices attempting to access a LAN or WLAN. By enabling 802.1X, the network ensures that only authenticated devices or users can access network resources, thereby enhancing network security. This feature is typically deployed in enterprise, campus, or branch office networks and can work with a RADIUS server for centralized authentication and management.

![alt text](./img/image-54.png)
<p align="center"><strong>Figure 4-49 802.1X Configuration</strong></p>

- **802.1X Function Switch**: Enables or disables the 802.1X function. It is recommended to keep this enabled in scenarios where network access control is required; otherwise, keep it disabled.
  - **Enabled**: Enables the 802.1X authentication function, and authentication will be performed on all configured authentication ports.
  - **Disabled**: Disables the 802.1X function, and no authentication will be performed on the ports.
- **Server**: Specifies the IP address or domain name of the RADIUS server used for 802.1X authentication.
- **Authentication Port**: The physical or logical ports on which 802.1X authentication is enabled. When a device connects, the port triggers an authentication request, and unauthenticated devices will be isolated.
- **Accounting Port**: The port used for accounting or traffic statistics after 802.1X authentication succeeds. This applies only to networks where the accounting function is enabled. If accounting or traffic statistics are not required, this field can be left blank or disabled.
- **Shared Key**: Used for secure communication between the 802.1X client and the RADIUS server.

## 4.10 Services

### 4.10.1 Interface Management

The local networks allowed through a specific interface and the interface speed can be configured in the **Service > Interface Management** function.

![alt text](./img/image-58.png)
<p align="center"><strong>Figure 4-50 Interface Management List</strong></p>

![alt text](./img/image-59.png)
<p align="center"><strong>Figure 4-51 Interface Management Configuration</strong></p>

### 4.10.2 DHCP Server

The DHCP (Dynamic Host Configuration Protocol) service operates in a client/server communication mode, where clients request IP addresses from servers, and servers respond by assigning IP addresses dynamically to clients. The DHCP server's IP address pool can be configured using the **Service > DHCP Server** feature.

![alt text](./img/image-60.png)
<p align="center"><strong>Figure 4-52 DHCP Server Configuration</strong></p>

**Notes:**

1. The device's DHCP service is generated based on the network information in the local network. If a local subnet is removed from the Local Network list, the DHCP server for that local subnet will also be deleted.
2. Local network entries need to be set in "IP" mode for the DHCP server function to take effect. Networks in "VLAN Only" mode are not within the selectable range.

### 4.10.3 DNS Server

DNS (Domain Name System) servers are a crucial network component responsible for translating human-readable domain names into computer-understandable IP addresses. DNS servers act as the address book of the internet, helping computers and devices locate other devices and ensuring that information can be correctly delivered across the network.

When DNS server addresses are not configured in **Service > DNS Server**, the DNS addresses obtained from the device's upstream interface will be used for domain name resolution. When DNS server addresses are configured, the configured DNS addresses will be used for domain name resolution.

![alt text](./img/image-61.png)
<p align="center"><strong>Figure 4-53 DNS Server Configuration</strong></p>

### 4.10.4 Fixed Address List

The **Service > Fixed Address List** function can be used to allocate a fixed IP address to a device based on its MAC address. This means that the device will consistently receive the same IP address every time it connects to the IR602.

![alt text](./img/image-62.png)
<p align="center"><strong>Figure 4-54 Fixed Address List Configuration</strong></p>

**Cautions:**

1. The available addresses for allocation must fall within the address range of the local network in IP mode, or the configuration will not take effect.
2. When the local network is deleted, all fixed address allocation rules within the local network's address range will be removed.

### 4.10.5 Dynamic DNS

Dynamic DNS (Dynamic Domain Name System) is used to automatically update the name server content in the domain system. According to internet domain rules, domain names are typically associated with fixed IP addresses. Dynamic DNS technology allows users with dynamic IP addresses to have a fixed name server, enabling external users to connect through regular updates.

The Dynamic DNS server address can be manually configured under the **Service > Dynamic DNS** feature.

![alt text](./img/image-63.png)
<p align="center"><strong>Figure 4-55 Dynamic DNS Configuration</strong></p>

The Dynamic DNS parameters are described in the following table.

| Parameter | Description |
|-----------|-------------|
| Service Provider | Provided by the Dynamic DNS service operator. Options: dyndns, 3322, oray, no-ip, or custom (requires a URL) |
| Hostname | The hostname registered with the service provider |
| Username | The username registered with the service provider |
| Password | The password set during registration |

### 4.10.6 SMS Control

The IR602 supports remote control of the device via SMS. Users can configure this feature under **Services > SMS Control**.

![alt text](./img/image-64.png)
<p align="center"><strong>Figure 4-56 SMS Control</strong></p>

### 4.10.7 AT Services
The IR602 supports interaction with the built-in cellular communication module via AT commands, allowing you to query (e.g., signal strength, network status), configure (e.g., network mode, APN parameters), and control (e.g., module reboot, dial-up connection) the module.

Users can access the configuration page under **Services > AT Services**.

![alt text](./img/image-65.png)
<p align="center"><strong>Figure 4-57 AT Services</strong></p>

### 4.10.8 SNMP Configuration

The IR602 supports the SNMP protocol. Users can export the MIB file by clicking the **Export MIB File** option.

![alt text](./img/image-66.png)
<p align="center"><strong>Figure 4-58 SNMP Configuration</strong></p>

### 4.10.9 Passthrough Settings

The IP Passthrough feature passes the uplink interface address through to the client device. To access the client device, you need to allow inbound rules.

| Parameter | Description |
|------|------|
| Passthrough | When enabled, only one client can access the Internet. The following features will not work: Static Routing, VPN, Policy-Based Routing, Fixed Address Assignment, and Connector. |
| Working Mode | Can be configured as Default Mode or Flexible Mode. |
| Passthrough MAC | The MAC address of the terminal. Only the terminal with the specified MAC address can receive the uplink interface IP via passthrough. |
| Passthrough WAN | Select a WAN port as the uplink interface for IP Passthrough. |
| Passthrough LAN | Select a LAN port to obtain the passthrough IP. |
| Passthrough IP Mask | Configures the subnet mask used while IP Passthrough is in operation. |
| DHCP Server | The DHCP service on the uplink, used only for IP Passthrough. |
| Lease Time |The validity period of the lease.  |

![alt text](./img/image-67.png)
<p align="center"><strong>Figure 4-59 Passthrough Configuration</strong></p>

## 4.11 Industrial Interface

The IR602 supports IO interface configuration, allowing you to set the working modes of the IO1 and IO2 interfaces.

| Parameter | Description |
|------|------|
| IO1 Mode | The working mode of the IO1 interface. Can be set to Input or Output. |
| IO1 Default Level | Low Level / High Level |
| IO2 Mode | The working mode of the IO2 interface. Can be set to Input or Output. |
| IO1 Default Level | Low Level / High Level |

![alt text](./img/image-68.png)
<p align="center"><strong>Figure 4-60 IO Configuration</strong></p>

## 4.12 System

In the **System** menu, settings related to cloud management, remote access control, clock settings, device options, configuration management, device alarms, tools, scheduled reboot, log server, account management, and other functions can be configured.

### 4.12.1 Cloud Management

DeviceLive (device.inhandcloud.com) is a cloud platform developed by InHand Networks to address challenges in industrial networks, such as slow deployment, complex operations, and poor user experiences. This platform integrates features like zero-touch deployment, intelligent operations and maintenance, security protection, and user experience capabilities. Once devices are connected to the cloud platform, remote management, batch configuration, traffic monitoring, and other operations can be performed through the platform.

The IR602 automatically connects to Device Live after establishing an internet connection by default. If the cloud management function is not required, it can be disabled manually in the **System > Cloud Management** function.

![alt text](./img/image-69.png)
<p align="center"><strong>Figure 4-61 Cloud Management Configuration</strong></p>

### 4.12.2 Remote Access Control

Whether to allow external access to the router's web configuration interface from the internet can be configured through the **System > Remote Access Control** function. The service port for this purpose can also be set.

![alt text](./img/image-70.png)
<p align="center"><strong>Figure 4-62 Remote Access Control Configuration</strong></p>

The remote access control parameters are described in the following table.

| Parameter | Description |
|-----------|-------------|
| HTTPS | When enabled, the router's web interface can be accessed remotely by entering the public IP address and port number of the upstream interface in a web browser |
| SSH | When enabled, the router's backend can be accessed remotely using remote tools by providing the public IP address, port number, username, and password |
| Telnet | Once enabled, users can remotely log in to the router's management interface from a remote tool (e.g., CRT) by entering the public address & port of the device's uplink interface, along with the username and password. |
| Ping | When enabled, the upstream interface allows external networks to initiate ping requests |

### 4.12.3 Country & System Clock

The Country & Clock feature is used to coordinate and synchronize time among network devices. The clock function in a network is essential for data transmission, logging, security, coordination, and troubleshooting.

You can select the current time zone under **System > Country & Clock**, and configure the NTP server address to synchronize the device's system time with the target NTP server.

![alt text](./img/image-71.png)
<p align="center"><strong>Figure 4-63 Country & System Clock Configuration</strong></p>

### 4.12.4 Device Option

In the **System > Device Options** section, various device operations can be performed, such as rebooting, upgrading firmware, and restoring factory settings.

![alt text](./img/image-72.png)
<p align="center"><strong>Figure 4-64 Device Options</strong></p>

**Cautions:**

1. When performing a local firmware upgrade, it is essential to ensure that the firmware is obtained from a legitimate source to avoid rendering the device inoperable due to incorrect firmware imports.
2. When a device is connected to the cloud platform, the platform will synchronize the previous configuration to the device again due to cloud-based configuration synchronization. The device will only clear historical data during the factory reset.

### 4.12.5 Configuration Management

Configuration backups and backup recovery are critical tasks in network management and maintenance. They involve saving the configuration information of network devices so that it can be quickly restored or transferred when needed.

Device configurations can be exported to local storage in the **System > Configuration Management** menu. This backup can be imported into the device in case of configuration loss or when overwriting the existing configuration is required.

![alt text](./img/image-73.png)
<p align="center"><strong>Figure 4-65 Configuration Management</strong></p>

### 4.12.6 Device Alarms

Specific events that may occur on the device can be selected as alarm events, and the email address for receiving alerts can be configured. When an alarm event occurs, the device will automatically send an email notification. Even if certain alarm options are not selected, related alarm events will still be recorded in the device's local logs.

Alarm event types and email addresses for alarm notifications can be configured in the **System > Device Alarms** menu.

![alt text](./img/image-74.png)
<p align="center"><strong>Figure 4-66 Device Alarms Configuration</strong></p>

After configuring the outgoing email server address, port, username, and password, the device will use this email account to send alarm notifications. The "Send Test Email" option can be used to verify whether the outgoing email configuration is correct.

![alt text](./img/image-75.png)
<p align="center"><strong>Figure 4-67 Email Server Configuration</strong></p>

### 4.12.7 Tools

**Ping**

ICMP (Internet Control Message Protocol) can be used to check the device's external network connectivity. In the "Target" field, enter any domain name or IP address to test the device's connectivity to, and click "Start" to check the connectivity status between the device and the specified target.

This function is accessed via **System > Tools > Ping**.

![alt text](./img/image-76.png)
<p align="center"><strong>Figure 4-68 Ping Tool</strong></p>

**Traceroute**

Traceroute is a network diagnostic tool used to determine the network path that data packets take from the source to the destination, as well as the intermediate routers or hops along that path.

The target host's IP address can be entered in **System > Tools > Traceroute**, the outgoing interface for the traffic can be selected, and "Start" can be clicked to check the device's connectivity to the target IP by tracing the route.

![alt text](./img/image-77.png)
<p align="center"><strong>Figure 4-69 Traceroute Tool</strong></p>

**Packet Capture**

Packet capturing is a network monitoring and analysis technique used to capture and record data packets transmitted over a computer network. Packet capture tools are typically used for network troubleshooting, network performance analysis, security auditing, and protocol analysis.

Packets passing through a specific interface can be captured in **System > Tools > Packet Capture**. By selecting the "Output" option, the captured data can be displayed within the interface or exported locally for further analysis.

![alt text](./img/image-78.png)
<p align="center"><strong>Figure 4-70 Packet Capture Tool</strong></p>

**Iperf**

Iperf is commonly used for traffic generation on the device to test network bandwidth and throughput, thereby evaluating link quality.

![alt text](./img/image-79.png)
<p align="center"><strong>Figure 4-71 Iperf Tool</strong></p>

### 4.12.8 Scheduled Reboot

Scheduled reboot is a network device management strategy that allows administrators to automatically restart a device at a specific time or under certain conditions to ensure normal operation and performance.

Scheduled reboots can be configured in the **System > Scheduled Reboot** function based on business requirements. The device supports scheduled reboots at fixed times daily, weekly, or monthly.

In the case of monthly reboots, if the selected reboot day exceeds the actual number of days in the month, the device will reboot on the last day of the month. For example, if the 31st of every month is selected, the device will reboot on the 30th in a month with only 30 days.

![alt text](./img/image-80.png)
<p align="center"><strong>Figure 4-72 Scheduled Reboot Configuration</strong></p>

### 4.12.9 Log Server

A log server is a dedicated server or software application used to collect, store, and manage log information generated by network devices, applications, and operating systems. These log records include events, warnings, errors, activities, and other relevant information and are crucial for monitoring, troubleshooting, and performance optimization.

When the log file server function is enabled in the **System > Log Server** feature, the device will periodically upload log files to the specified log server.

![alt text](./img/image-81.png)
<p align="center"><strong>Figure 4-73 Log Server Configuration</strong></p>

### 4.12.10 Account Management

The username and password for logging in to the device's web page can be changed in the **System > Account Management** menu.

![alt text](./img/image-82.png)
<p align="center"><strong>Figure 4-74 Account Management</strong></p>

### 4.12.11 Other Settings

![alt text](./img/image-83.png)
<p align="center"><strong>Figure 4-75 Other Settings</strong></p>

**Web Login Management**

When a user logs in to the local interface of the device through the web and the session remains active for a certain period, it will automatically log out or disconnect to protect privacy and security.

The logout time can be configured in **System > Other Settings > Web Login Management**. If the online time during a single login session on the device's web page exceeds the configured time, the system will automatically log the user out, and re-login will be required to continue operations.

**Automatically Restarts**

Industrial routers are designed with an auto-reboot mechanism to address situations where a manual reboot on site would otherwise be required to restore network connectivity. After enabling this feature under **System > Other Settings > Automatically Restarts**, the device will automatically reboot if it loses network connectivity and still cannot re-establish the connection after one hour of retries.

**SIP ALG**
SIP ALG (Session Initiation Protocol Application Layer Gateway) is a network function used to manage VoIP (Voice over IP) calls traversing NAT (Network Address Translation). It performs proper address translation and forwarding for SIP signaling and RTP media streams, ensuring that VoIP calls can be established and maintained correctly in a router environment.

# Appendix Safety Precautions

1. The original power adapter must be used to avoid device damage caused by mismatched power adapters.

2. When installing the device, it should not be placed in an environment with strong electromagnetic interference. The device must be kept at a safe distance from high-power equipment. After installation, the device must be secured to prevent accidental drops and potential damage.

3. The device's operating environment must meet the temperature and humidity requirements specified in the user manual.

4. The device's cables, including Ethernet cables and power adapter connections, must be inspected regularly. Cables must be kept clean and replaced if any damage is detected.

5. When cleaning the device, chemical agents must not be sprayed directly on the device's surface to prevent damage to the housing or internal components. A soft cloth must be used for cleaning.

6. The device must not be disassembled or modified by unauthorized personnel, as this can pose safety risks and may void the device's warranty.