# Enterprise Router ER2000 Product User Manual

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

| Symbol | Meaning | Example |
|--------|---------|---------|
| `< >` | Indicates a variable or parameter to be replaced with an actual value | `<IP Address>` means to enter a specific IP address |
| `" "` | Indicates a text label on the interface | Click the "Save" button |
| `→` | Indicates menu hierarchy or operation sequence | [Network] → [Cellular] |
| `[ ]` | Indicates a menu or page name | Go to the [System Settings] page |
| **Caution** | Points to note during operation; improper actions may result in data loss or device damage | — |
| **Note** | Provides supplementary and necessary explanations for the operation description | — |

### Technical Support
Email: support@inhandnetworks.com

URL: www.inhand.com

### How to Use This Manual

**Matching the right reader**

- First-time users: It is recommended to read in sequence: [Getting to Know the Device] → [Installation and First Use] → [Common Scenario Configuration] → [Function Description and Parameter Reference].
- Existing device users: Can directly refer to [Function Description and Parameter Reference] or [Appendix: Troubleshooting].
- Cloud platform management users: Can refer to [Common Scenario Configuration] for device remote management platform content (if applicable).

**Quick navigation by task**

| Task | Corresponding Chapter | Estimated Time |
|------|----------------------|----------------|
| Device installation and Web login | [Installation and First Use](#chapter-2-installation-and-first-use) | Approx. 10 minutes |
| Configure Internet access | [Common Scenario Configuration](#chapter-3-common-scenario-configuration) | Approx. 5 minutes |
| Connect to cloud platform | [Common Scenario Configuration](#chapter-3-common-scenario-configuration) | Approx. 5 minutes |
| Monitor device status | [Function Description and Parameter Reference](#chapter-4-function-description-and-parameter-reference) | Approx. 10 minutes |
| Configure VPN | [Function Description and Parameter Reference](#chapter-4-function-description-and-parameter-reference) | Approx. 15 minutes |
| Troubleshoot network issues | [Appendix: Troubleshooting](#appendix-troubleshooting) | On demand |

---

## Chapter 1 Getting to Know the Device

### 1.1 Overview

ER2000 is a high-performance enterprise router/gateway designed for mid-to-large retail sites, branch offices, and small campuses. It offers 10G uplinks and aggregation connectivity, supports SD-WAN for rapid site-to-site deployment, and enables unified provisioning, configuration, monitoring, and remote diagnostics via a cloud management platform. Selected models also support PoE to power APs, IP cameras, and IP phones directly, helping organizations improve bandwidth and reliability across multi-site networks while reducing deployment and O&M costs.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770297900091-5605e078-508f-4d39-a3ee-dcfb42d9a5fc-461617.webp" alt="ER2000 Application Scenario"></p>

<p align="center"><strong>Figure 1-1 ER2000 Application Scenario</strong></p>

### 1.2 LED Indicators

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770300928326-b31e1324-36b1-455b-85de-77f054739b90-518601.webp" alt="Factory Reset"></p>

<p align="center"><strong>Figure 1-2 Factory Reset Button Location</strong></p>

| LED | Status | Meaning |
|-----|--------|---------|
| SYS | Off | Device is not powered on |
| | Steady Red | System starting up |
| | Steady Green | System operating normally |
| | Blinking Red | System fault |
| | Blinking Blue | System upgrading |

### 1.3 Restore to Factory Defaults

Restore factory settings via the Reset button:

1. Power on the device. When the SYS indicator is solid red, press and hold the Reset button (for about 50 seconds) until the SYS indicator starts flashing red.
2. Release the Reset button. The SYS indicator will then flash blue, indicating that the device has entered the factory reset process.

### 1.4 Default Settings

| No. | Function | Default Settings |
|:---:|----------|------------------|
| 1 | Ethernet Default Configuration | Four WAN ports obtain IP addresses via DHCP by default. **IP Address:** 192.168.100.1 **Subnet Mask:** 255.255.255.0 |
| 2 | Network Access Control | Local HTTP and HTTPS access enabled, using ports **80** and **443** respectively. |
| 3 | Username and Password | adm / 123456 |

---

## Chapter 2 Installation and First Use

### 2.1 Pre-Installation Preparation

Before installing the device, ensure the following conditions are met:

- The operating environment temperature and humidity meet the device specifications.
- The necessary tools and accessories (power adapter, Ethernet cables) are prepared.
- A PC with a Web browser (Google Chrome is recommended) is available for configuration.

> **Caution:** Use the original power adapter to avoid device damage caused by mismatch.

### 2.2 Installation Guide

1. Connect the device to power using the supplied power adapter.
2. Connect any LAN port of the device to the PC using an Ethernet cable.
3. Configure the PC's IP address to be in the same subnet as the router.
   - a. The device has DHCP enabled by default. Set the PC to "Obtain an IP address automatically." The router will automatically assign an IP address to the PC. Verify that the PC has obtained an IP address and that it is within the **192.168.100.0** subnet.
   - b. If the PC cannot obtain an IP address automatically, manually configure the PC's IP address to any value between **192.168.100.2–192.168.100.254**, set the default gateway to **192.168.100.1**, the subnet mask to **255.255.255.0**, and the DNS server to **223.5.5.5** or the carrier's DNS server address.
4. Enter the device's default address **192.168.100.1** in the browser address bar. After entering the username and password (refer to the nameplate information or [Default Settings](#16-default-settings)), the device's Web management interface will be accessed. If the browser displays a security warning, open the hidden or advanced options and choose to proceed.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770301433054-a48d4d9c-ecce-4f96-9e7e-a0f4b558fe09-802686.webp" alt="Configure PC IP Address"></p>

<p align="center"><strong>Figure 2-1 Configure PC IP Address</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770345601032-fdcddf8f-585b-45b6-bf7c-5439d58bf366-580301.webp" alt="ER2000 Web Interface Login"></p>

<p align="center"><strong>Figure 2-2 ER2000 Web Interface Login</strong></p>

### 2.3 Quick Checklist

After installation, verify the following items:

- [ ] The SYS LED is steady green, indicating normal operation.
- [ ] The PC has obtained an IP address in the 192.168.100.0/24 subnet.
- [ ] The Web management interface at 192.168.100.1 is accessible.

---

## Chapter 3 Common Scenario Configuration

### Scenario 1: Quick Internet Access

**Objective**: Connect the ER2000 to the Internet via a wired WAN connection.

**Prerequisites**: The device is powered on, and an Ethernet cable is available to connect the WAN port to the upstream network.

**Estimated Time**: Approx. 5 minutes.

**Operation Steps**:
1. Connect any WAN port (WAN1/WAN2/WAN3/WAN4) to the upstream network with an Ethernet cable.
2. By default, the WAN ports use DHCP. The device will automatically obtain an IP address and access the Internet.
3. If a static IP or PPPoE is required, log in to the Web interface, go to [Internet], select the corresponding WAN interface, and change the connection method as needed.

**Verification Method**:
1. Check that the WAN port LED indicates a normal link.
2. On the [Dashboard] page, verify that the uplink interface has obtained an IP address.
3. Use the Ping tool under [System] → [Tools] to test connectivity to a public IP address (e.g., 8.8.8.8).

**Common Issues**:
- No Internet access: Confirm that the upstream network is functional and that the WAN cable is securely connected.
- Cannot obtain an IP address: Verify whether the ISP requires PPPoE credentials or a static IP configuration.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1741863745864-c42c261a-3892-4d76-96ff-b590fb3c93b3-550533.webp" alt="Device WAN Port Configuration"></p>

<p align="center"><strong>Figure 3-1 Device WAN Port Configuration</strong></p>

### Scenario 2: Connect to InCloud Manager Platform

**Objective**: Add the ER2000 to the InCloud Manager cloud platform for centralized management.

**Prerequisites**: The device has Internet access, and a valid email address is available for platform registration.

**Estimated Time**: Approx. 10 minutes.

**Operation Steps**:
1. In a Web browser (Google Chrome is recommended), navigate to [https://star.inhandcloud.com](https://star.inhandcloud.com). The page will be automatically redirected to the portal. Click "Create Now" to create a new platform account.
2. After completing email registration, log in to the InHand Cloud portal with the registered username and password, and select the [InCloud Manager] service.
3. After logging in to InCloud Manager, go to the [Devices] menu, click "Add", enter the device name, serial number, and MAC address, then click "Finish" to complete adding the device.

**Verification Method**:
1. On the InCloud Manager [Devices] page, confirm that the ER2000 device status is online.
2. Click the device name to enter the device details page and verify that basic information and interface status are displayed.

**Common Issues**:
- Device remains offline: Confirm that the device has Internet access and that the serial number and MAC address were entered correctly.
- License expired: When ER2000 connects to the cloud platform for the first time, the platform automatically issues a one-year Basic license. Users can renew the license or upgrade it to the Branch Professional Edition under "Enterprise Management > Subscriptions > Licenses".

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770347037798-74cce7c8-5386-467a-9ac3-eaf602df2bf9-283188.webp" alt="Register an InHand Cloud Services Account"></p>

<p align="center"><strong>Figure 3-2 Register an InHand Cloud Services Account</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770347161493-a01790a4-0d9a-4d6b-be39-af28b0bd97e1-049982.webp" alt="Select SaaS Service"></p>

<p align="center"><strong>Figure 3-3 Select SaaS Service</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770347265329-b7cf2ce8-9010-42ba-9d32-b39f944e40ba-505192.webp" alt="Add the Device to InCloud Manager"></p>

<p align="center"><strong>Figure 3-4 Add the Device to InCloud Manager</strong></p>

---

## Chapter 4 Function Description and Parameter Reference

### 4.1 Device Monitoring

After adding the device to the platform, the network can be managed and monitored from the platform. The platform also supports remotely viewing real-time status information via the device's local interface.

#### 4.1.1 Device Overview

In the [Devices] section, click the [Device Name] to access the device details page.

**Overview**

On the Overview page, the device's basic information, interface status, traffic statistics, license status, software version, and more can be viewed.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770347575707-90b7d423-faac-4f7a-ad7d-7d4819156628-511704.webp" alt="Device Information Overview"></p>

<p align="center"><strong>Figure 4-1 Device Information Overview</strong></p>

**Traffic Usage**

On the "Devices > Traffic" page, historical traffic usage data for each uplink port can be viewed.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770347602840-d1633e74-a98c-42dd-b673-cdd3d221ffdc-666238.webp" alt="Traffic Statistics"></p>

<p align="center"><strong>Figure 4-2 Traffic Statistics</strong></p>

#### 4.1.2 Local Device Information

Using InCloud Manager's "Remote Access" feature, the device can be viewed and configured in real time. Select the target device and click "Remote Access" to open the device's local login page.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770347773568-d9e622c7-fe9d-49ec-9009-b9cc863f0fde-504708.webp" alt="Select Target Device for Remote Access"></p>

<p align="center"><strong>Figure 4-3 Select Target Device for Remote Access</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770347841349-f5cf095d-9415-4a13-a2f5-2a911d4bb4d8-433853.webp" alt="Remote Access Login Page"></p>

<p align="center"><strong>Figure 4-4 Remote Access Login Page</strong></p>

**Device Information**

On the [Dashboard] page, the device's basic information is displayed at the top of the page, including device name, model, serial number, MAC address, uptime, uplink interface address, etc.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770347935368-7f1bf193-9464-4a36-beb9-88dec9bd20d8-760473.webp" alt="View Device Information"></p>

<p align="center"><strong>Figure 4-5 View Device Information</strong></p>

| Parameter | Description |
|-----------|-------------|
| Name | Device name identifier. Default is "ER2000"; can be modified. |
| MAC Address | Physical MAC identifier of the device. |
| Local Gateway Address | Gateway address of the device's default subnet. |
| Model | Specific device model; helps determine whether the device supports cellular and WLAN features. |
| Uptime | Running time since the device was powered on. |
| System Time | Displays the device time zone and system time. |
| Serial Number | Unique device identifier; used for indexing or adding the device to a platform account. |
| Connection Method | Uplink interface used for Internet access. |
| License Status | License applied to the device: InCloud Manager Basic Edition or Branch Professional Edition. |
| Firmware Version | Current software version number. |
| Uplink Interface Address | IP address of the uplink interface used for Internet access. |

**Interface Status**

In "Dashboard → Interface Status", the operating status of each interface can be viewed. Click an interface icon to view detailed information in the pop-up panel on the right.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770348043955-85696357-cfe0-4b8c-a3c9-6f2b4b4115ea-864852.webp" alt="Detailed Port Information"></p>

<p align="center"><strong>Figure 4-6 Detailed Port Information</strong></p>

**Traffic Statistics**

In "Dashboard → Traffic Statistics", traffic usage for each uplink interface since power-on can be viewed. Traffic statistics reset after a reboot. If historical traffic records are needed, view them on the device details page in InCloud Manager.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770348112909-8e3125ba-775a-4ea2-9cc9-35aeadf0de15-934378.webp" alt="Uplink Traffic Statistics"></p>

<p align="center"><strong>Figure 4-7 Uplink Traffic Statistics</strong></p>

**Link Monitoring**

In "Status → Link Monitoring", the uplink health status and metrics such as throughput, latency, packet loss, and signal strength can be viewed.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770348174316-44ce2593-6c00-4a78-b5b1-5e15f66f0ce4-490895.webp" alt="Uplink Link Information"></p>

<p align="center"><strong>Figure 4-8 Uplink Link Information</strong></p>

**Clients**

In "Status → Clients", detailed information about wired/wireless clients connected to the router can be viewed, such as name, IP address, MAC address, VLAN, connected subnet, traffic usage, uptime, etc.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770348200204-624595d0-f98d-4cc8-a2eb-722ec9f8f9ca-059378.webp" alt="Client Status"></p>

<p align="center"><strong>Figure 4-9 Client Status</strong></p>

**VPN**

In "Status → VPN", information such as status name, traffic, and last connection duration for IPSec VPN and L2TP VPN can be viewed.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770348233298-9e4db675-da2e-4ab6-91f1-567e92d624ff-054349.webp" alt="VPN Status Information"></p>

<p align="center"><strong>Figure 4-10 VPN Status Information</strong></p>

**Routing Table**

In "Status → Routing Table", all routing table information on the device can be viewed, including directly connected routes, static routes, and dynamic routes.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770348451048-cafc79a8-0726-40ad-baf8-e4102bce543d-393956.webp" alt="Routing Table"></p>

<p align="center"><strong>Figure 4-11 Routing Table</strong></p>

**Events**

In "Status → Events", device event records can be viewed to better understand device operating status.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770348619003-fd5cdd96-aab4-4bf1-8d05-2804f2f7430a-509495.webp" alt="Device Event Records"></p>

<p align="center"><strong>Figure 4-12 Device Event Records</strong></p>

Currently supported event types:

- User login success
- User login failure
- Configuration changes
- CPU utilization too high in the last 5 minutes
- Memory utilization too high in the last 5 minutes
- Probe status change
- VPN status change
- Client status change
- Uplink link status change
- Uplink link switchover
- Reboot
- Upgrade

**Logs**

In "Status → Logs", system logs can be viewed. When the device fails, technicians can troubleshoot based on system logs.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770348692161-f8029695-6449-4cd1-a76e-3f46022f5d43-865450.webp" alt="Device Log Records"></p>

<p align="center"><strong>Figure 4-13 Device Log Records</strong></p>

Supported log operations:

- Download Logs: Download device runtime logs.
- Download Diagnostic Logs: Download diagnostic logs, including runtime logs, device info, device configuration, etc.
- Clear Logs: Clear runtime logs (diagnostic logs are not cleared).

### 4.2 Internet

ER2000 supports three wired Internet connection methods: DHCP, Static IP, and PPPoE. Click "Edit" to change the connection method as needed. The default method is DHCP.

Under "Internet", parameters and operating mode for each uplink interface can be configured. ER2000 supports up to four WAN ports. Select the appropriate interface based on the uplink port type; configuration items are the same for all ports.

- WAN1: 10G SFP+ optical port
- WAN2: 1G SFP optical port
- WAN3/4: 1G Ethernet ports

#### 4.2.1 Wired Connection (DHCP)

DHCP is enabled by default on the WAN1 interface. Connect the WAN interface to the Internet with an Ethernet cable and the device will access the Internet automatically.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770348844223-0618a24c-086c-477d-996f-a6a79cc5bc14-802219.webp" alt="Enable DHCP Service on WAN1 Interface"></p>

<p align="center"><strong>Figure 4-14 Enable DHCP Service on WAN1 Interface</strong></p>

#### 4.2.2 Wired Connection (Static IP)

Static IP: The IP address obtained from the ISP or assigned by the network administrator can be manually configured. After configuration, the router will access the network using the specified static IP.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770348903030-ffe7f5df-ee5c-4b0b-8dde-927c67f8dd8a-949185.webp" alt="Configure a Static IP Address"></p>

<p align="center"><strong>Figure 4-15 Configure a Static IP Address</strong></p>

#### 4.2.3 Wired Connection (PPPoE)

PPPoE: Configure broadband dial-up service. The configuration parameters are provided by the ISP. After configuration, the router can access the network via PPPoE.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770348912706-1e4512b8-a560-42f0-ae3b-014c3cf262f5-958422.webp" alt="Configure Broadband Dial-Up Service"></p>

<p align="center"><strong>Figure 4-16 Configure Broadband Dial-Up Service</strong></p>

#### 4.2.4 Uplink List

In "Internet > Uplink List", WAN1–WAN4 interfaces can be edited. The "Priority" icon can be dragged to adjust interface priority. Interfaces are arranged from top to bottom by priority; higher-priority interfaces are preferred as the current uplink.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770349022132-df056af6-e2bf-47f3-844b-1094774377b4-167853.webp" alt="Uplink List"></p>

<p align="center"><strong>Figure 4-17 Uplink List</strong></p>

#### 4.2.5 Uplink Settings

In "Internet > Uplink Settings", link detection and the coordination mode among different uplink interfaces can be configured.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770349157872-14dfe97e-13d3-4298-9841-d0fcc2553d4a-229360.webp" alt="Uplink Settings"></p>

<p align="center"><strong>Figure 4-18 Uplink Settings</strong></p>

- Link Probe Switch: When enabled, probes connectivity for all uplink interfaces. Enabled by default.
- Probe Address: Enter a specific probe target address.
  - a. After it is set, all uplinks probe only this address. If the specified address is unreachable, Internet access may be affected.
  - b. If not set, the device selects an available address from the uplink DNS address and alternative probe addresses for probing.
  - c. By default, it probes the uplink DNS address and alternative addresses 119.29.29.29 and 223.5.5.5.
- Link Switching Based on Probe Items: In Link Backup mode, users can enable probe items to trigger uplink switching. The following conditions must all be met:
  - a. Link switch is enabled.
  - b. Probe items are enabled.
  - c. The device is in "Link Backup" mode and not set to "No Switching".

**Notes:**

- Changes under the Internet menu may interrupt Internet access. Proceed with caution.
- When the probe address is empty, the device probes the DNS address obtained by the uplink interface by default. After a probe address is set, all uplinks probe only the specified address.
- In Link Backup mode, users can customize probe parameters. The device performs uplink switching based on enabled probe items. If no probe item is enabled, uplink switching is triggered only by priority and link connectivity.
- In Load Balancing mode, all uplinks that are operating normally will forward business traffic.

### 4.3 Local Network

In [Local Network], local subnets can be customized, including LAN address range, VLAN ID, DHCP service, etc. After configuration, go to [Services → Interface Management] and apply the network to the connected port. Local Network serves as the device's subnet resource pool; create subnets as needed. By default, all LAN interfaces use the "Default" subnet (192.168.100.1/24).

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770349438131-966e51bc-086e-446e-bf33-2896b7ecfb3e-737281.webp" alt="Local Subnet List"></p>

<p align="center"><strong>Figure 4-19 Local Subnet List</strong></p>

Click "Add/Edit" to add a new local network or edit an existing one.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770349500245-1b098788-92c6-47e7-9014-a3ac452b9da1-221563.webp" alt="Add Local Network"></p>

<p align="center"><strong>Figure 4-20 Add Local Network</strong></p>

| Parameter | Description |
|-----------|-------------|
| Name | Used to identify the network. This name can be selected in "Wi-Fi" and "Interface Management". |
| Mode | Select whether the subnet is Layer-2 transparent mode or Layer-3 IP mode. Default: "IP Mode". |
| VLAN | Split the LAN into different virtual logical networks. By default, all interfaces and Wi-Fi use the default (VLAN1) network. |
| IP Address/Mask | Gateway address for accessing the router via LAN or Wi-Fi. Default: "192.168.100.1". |
| DHCP Server | Clients connected to the router will obtain IP addresses via this feature. Enabled by default; the address pool range is generated automatically based on "IP Address/Mask". |

**Notes:**

- The default local network cannot be deleted and only supports modifying IP Address/Mask and DHCP Server settings.
- The mode of an added local network cannot be changed.
- VLAN Only mode is for Layer-2 passthrough; IP Address/Mask and DHCP Server do not need to be configured.

### 4.4 VPN

A Virtual Private Network (VPN) is an encryption technology used to create secure, private network connections over the public Internet. It allows users to securely access private network resources regardless of location. By encrypting communication data, VPN ensures confidentiality and security and prevents unauthorized access. This technology is useful for connecting to corporate networks, maintaining online privacy, and accessing restricted content. VPN is widely used in enterprise, personal, and mobile device scenarios and is one of the key tools for protecting privacy and data security.

#### 4.4.1 IPsec VPN

IPsec (Internet Protocol Security) VPN is a protocol suite designed to enhance network communication security by protecting data transmission through encryption and authentication. It is widely used for secure remote access, site-to-site connections, and VPNs. In this scenario, ER2000 is typically used as the server side, providing stable and reliable network access for IPsec clients.

Click "Add" under "VPN → IPsec VPN" to add a new IPsec VPN.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770349645803-172c631d-8a65-4b79-a7ca-aacc21013118-109547.webp" alt="IPSec VPN Edit/Create Entry"></p>

<p align="center"><strong>Figure 4-21 IPSec VPN Edit/Create Entry</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770349701483-1d7c0ab0-682a-43d6-ae18-935a1fbc0b1c-275287.webp" alt="Configure IPSec Server"></p>

<p align="center"><strong>Figure 4-22 Configure IPSec Server</strong></p>

After both sides are configured, the tunnel can be established. The tunnel status can be viewed under [Status → VPN]. Only some required fields are explained below:

| Parameter | Description |
|-----------|-------------|
| Name | Identifier for the IPsec VPN created on the router; mainly used for local management. |
| IKE Version | Select IKEv1 or IKEv2. |
| Negotiation Mode | Configure Main Mode / Aggressive Mode for IPsec establishment. |
| Pre-shared Key | Both peers must configure the same authentication key for IKE negotiation. |
| Internet Interface | Uplink interface used locally to establish the IPsec VPN. |
| Tunnel Mode | Encapsulation mode for IP packets; supports Tunnel Mode and Transport Mode. |
| Local Subnet | The subnet that needs to communicate through the IPsec tunnel via ER2000. |
| Remote Subnet | The subnet on the other end that needs to communicate through the IPsec tunnel. |
| Local ID | Field used to identify the local side; supports IP, FQDN, User FQDN. |
| Remote ID | Field used to identify the peer; supports IP, FQDN, User FQDN. |
| IKE Policy | Configure IKE parameters. |
| Encryption | IKE encryption algorithm. Range: DES, 3DES, AES128, AES192, AES256. Default: AES128. |
| Authentication | IKE authentication algorithm. Range: MD5, SHA1, SHA2-256, SHA2-384, SHA2-512. Default: SHA1. |
| DH Group | DH parameters used in IKE phase key negotiation. Range: 1, 2, 5, 14, 15, 16, 19, 20. |
| Lifetime | IKE SA lifetime. Default: 86400 seconds. |
| Peer DPD | Switch for detecting whether the IPsec tunnel is alive. |
| DPD Interval | Heartbeat interval. Default: 30 seconds. |
| DPD Timeout | Timeout. Default: 180 seconds. |
| IPsec Policy | Configure IPsec SA parameters. |
| Security Protocol | Security protocol used by ESP. Range: DES, 3DES, AES128, AES192, AES256. Default: AES128. |
| Encryption/Integrity | ESP algorithm settings. Range: MD5, SHA1, SHA2-256, SHA2-384, SHA2-512. Default: SHA1. |
| Authentication | Used for IPsec protocol authentication. |
| PFS Group | Additional key exchange in Phase 2 to improve security. Range: 1, 2, 5, 14, 15, 16, 19, 20. |
| Lifetime | IPsec SA lifetime. Default: 86400 seconds. |

**Example:**

Branch device ER815 and central device ER2000 in different regions need to access each other via an IPsec tunnel.

- ER2000: WAN IP 10.1.1.1, Local subnet 192.168.100.0/24, Remote subnet 192.168.2.0/24
- ER815: WAN IP 10.1.1.2, Local subnet 192.168.2.0/24, Remote subnet 192.168.100.0/24

At least five parameters must be filled in: Name, Pre-shared Key, Uplink Interface, Local Subnet, Remote Subnet. Other items can keep defaults.

**Notes:**

- The pre-shared key must be identical on server and client.
- Select the interface whose IP/public IP can be reached by the IPsec client. In this example, WAN2 IP is 10.1.1.1.
- Local subnet: the local subnet that communicates with the remote subnet; configure carefully to match.
- Remote subnet: the peer subnet that communicates with the server; configure carefully to match.

#### 4.4.2 L2TP VPN

Layer 2 Tunneling Protocol (L2TP) is a Layer-2 VPN protocol designed to provide secure point-to-point or site-to-site VPN connections. It is commonly used for remote access and branch interconnection, creating simple and flexible VPN tunnels between users or networks.

**L2TP VPN Server**

The L2TP server is typically deployed at the enterprise headquarters to provide remote access services for mobile offices or branches. Click "VPN → L2TP VPN → Server" to enter the L2TP server edit page.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770356874457-454be215-3a8d-4351-9dd0-3d55fbc06f72-753225.webp" alt="Configure L2TP VPN Server"></p>

<p align="center"><strong>Figure 4-23 Configure L2TP VPN Server</strong></p>

| Parameter | Description |
|-----------|-------------|
| Name | L2TP server name; cannot be modified. |
| Status | L2TP server enable switch; disabled by default. |
| Uplink Interface | Uplink interface used when L2TP acts as a server. |
| VPN Communication Address | Gateway address for L2TP clients; clients will be assigned addresses from the pool. The uplink interface IP must not be the same as the VPN communication address. |
| Address Pool | Address pool used for communication when L2TP clients connect. |
| Username/Password | Both peers must configure the same username/password for L2TP negotiation. |
| Authentication Mode | Set L2TP authentication mode. |
| Enable Tunnel Authentication | When enabled, the tunnel authentication username/password must match on both ends. |

**L2TP VPN Client**

ER2000 can act as an L2TP client to establish a tunnel with a remote L2TP server. In typical deployments, the branch side uses ER605 as the client and the server side uses ER2000. Click "Add" under "L2TP VPN → Client" to add an L2TP client. The client address is assigned by the server.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770356858281-2cabe11d-b548-4e0a-89d8-e1231264eb10-147402.webp" alt="Add L2TP Client"></p>

<p align="center"><strong>Figure 4-24 Add L2TP Client</strong></p>

| Parameter | Description |
|-----------|-------------|
| Name | L2TP client name identifier. |
| Status | Enable/disable switch for the L2TP client tunnel. |
| NAT | NAT switch for client forwarding. |
| Uplink Interface | Uplink interface used for communication with the server. |
| Server Address | Communication address of the remote L2TP server. |
| Username/Password | Must match on both ends. |
| Authentication Mode | Set L2TP authentication mode. |
| Enable Tunnel Authentication | When enabled, tunnel authentication username/password must match on both ends. |

#### 4.4.3 VXLAN VPN

VXLAN (Virtual Extensible LAN) is essentially a tunneling technology. It builds a logical tunnel over an IP network between source and destination devices and encapsulates customer packets for transmission and forwarding.

Click "Add" under "VPN → VXLAN VPN" to add a VXLAN VPN. VXLAN VPN cannot be enabled together with other VPNs or IP Passthrough.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770358052313-c9d8d6dd-6351-45bb-b704-82343d4bd60a-494166.webp" alt="Add VXLAN VPN"></p>

<p align="center"><strong>Figure 4-25 Add VXLAN VPN</strong></p>

| Parameter | Description |
|-----------|-------------|
| Name | Name of the VXLAN VPN network. |
| Uplink Interface | Egress interface used to establish VXLAN tunnels with other devices. |
| Remote Address | Peer device IP address for building the VXLAN VPN network. |
| VNI | VXLAN Network Identifier; one VNI represents one tenant. |
| Local Subnet | Address range assigned to local client devices. |

### 4.5 Security

Under [Security], advanced features can be configured as needed, including firewall, policy routing, and traffic shaping.

#### 4.5.1 Firewall

The firewall currently includes: Inbound Rules, Outbound Rules, Port Forwarding, MAC Address Filtering, etc. Configure according to business needs.

**Inbound/Outbound Rules**

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770358178754-21097b0d-1a52-4323-bca8-3fc8f9fd8d82-846554.webp" alt="Inbound/Outbound Rules"></p>

<p align="center"><strong>Figure 4-26 Inbound/Outbound Rules</strong></p>

In "Security → Firewall → Outbound Rules / Inbound Rules", interface-based traffic control can be implemented. For example, if under heavy attack from a specific source IP, inbound rules can be used to restrict traffic from that IP.

IT can also use outbound rules to restrict certain users' access to external networks. Inbound and outbound rules have the same configurable fields; the only difference is the default rule. Below is an example of adding an inbound rule.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770358196133-b43f2e91-e36e-42f9-bcc3-ebe27f85ea12-576675.webp" alt="Add Inbound Rule"></p>

<p align="center"><strong>Figure 4-27 Add Inbound Rule</strong></p>

| Parameter | Description |
|-----------|-------------|
| Name | Name of the inbound rule for local identification. |
| Status | Rule enable switch. |
| Interface | For outbound rules, the uplink interface where traffic exits the router; for inbound rules, the uplink interface where traffic enters the router. |
| Protocol | Protocol to match. Supports Any, TCP, UDP, ICMP, Custom. |
| Source | Source address to match; customizable. Default Any. |
| Destination | Destination address to match; customizable. Default Any. |
| Action | Allow or Deny for matched traffic. |

- Inbound rules: Management rules for external traffic accessing the router. Default: deny all.
- Outbound rules: Management rules for traffic from the router to the outside. Default: allow all.
- Supports adjusting priority by dragging the icon in the "Priority" column.

**Port Forwarding**

Port forwarding (also called port mapping/port redirection) redirects packets from one network port (or address) to another. Configure port forwarding rules under "Security → Firewall → Port Forwarding". When external traffic accesses a specific port on the router, the device forwards it to the corresponding port on an internal client, enabling access to internal services from outside.

Example: To access port 1024 of internal client 192.168.2.10 from outside, map that client port to port 1024 on WAN1. External users can access it by entering `https://<WAN1 address>:1024` in a browser, where `<WAN1 address>` is the WAN1 interface IP.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770358334094-623d8417-fcb4-4afe-a3d0-3a9647030b11-254570.webp" alt="Add Port Forwarding Rule"></p>

<p align="center"><strong>Figure 4-28 Add Port Forwarding Rule</strong></p>

| Parameter | Description |
|-----------|-------------|
| Name | Port forwarding rule name for local identification. |
| Status | Enable switch. |
| Interface | Uplink interface providing mapping; the uplink must have public IP support. |
| Protocol | TCP, UDP, or TCP&UDP. |
| Public Port | Port number on the uplink interface; must match the local port input range. |
| Local Address | Target device address behind the router. |
| Local Port | Target service port; must match the public port input range. |

**Network Address Translation**

Network Address Translation (NAT) rewrites the source or destination IP address in packets as they pass through the router, converting private addresses to routable addresses. Configure source/destination address translation under "Security → Firewall → NAT".

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770358413061-9daeccdb-b1ba-479b-a06d-ed0961131984-384569.webp" alt="Add NAT Rule"></p>

<p align="center"><strong>Figure 4-29 Add NAT Rule</strong></p>

| Parameter | Description |
|-----------|-------------|
| Name | Identifier for the rule. |
| Status | Enable/disable the rule. |
| Type | Select translation type. a) SNAT: Source address translation; rewrites the source IP field. b) DNAT: Destination address translation; rewrites the destination IP field. |
| Protocol | Select packet type. a) TCP b) UDP c) TCP&UDP |
| Source | Source IP address. |
| Destination | Destination IP address. |
| Translated Address | Value to translate to based on the selected type. |

**MAC Address Filtering**

MAC address filtering blocks (or allows) devices in the MAC list from accessing the Internet by controlling LAN device access requests. Configure rules under "Security → Firewall → MAC Address Filtering".

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770358496582-55bc7893-4ef9-45f2-a178-15db3bdf4b30-190351.webp" alt="Add MAC Filtering Rule"></p>

<p align="center"><strong>Figure 4-30 Add MAC Filtering Rule</strong></p>

Multiple MAC entries with descriptions can be created, and the list can be set to allow only listed MAC addresses (whitelist) or block listed MAC addresses (blacklist).

**Domain Name Filtering**

Domain name filtering blocks (or allows) clients from accessing domain names configured in the list. Configure rules under "Security → Firewall → Domain Name Filtering". Multiple rules can be added and allow access to listed domains (whitelist) or block access (blacklist).

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770358524458-11976654-4610-4bc4-9736-d351c95efa23-594299.webp" alt="Add Domain Filtering Rule"></p>

<p align="center"><strong>Figure 4-31 Add Domain Filtering Rule</strong></p>

#### 4.5.2 Policy Routing

Policy routing allows defining forwarding policies based on actual needs, forwarding different traffic flows via different links. This improves routing flexibility and controllability, increases link utilization efficiency, and reduces enterprise cost. Click "Add" under "Security → Policy Routing" to add a rule. Both source and destination cannot be set to "Any" at the same time.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770358553876-d53ce68e-b476-4484-8c91-95d9ae24676c-432342.webp" alt="Configure Policy Routing"></p>

<p align="center"><strong>Figure 4-32 Configure Policy Routing</strong></p>

#### 4.5.3 Traffic Shaping

Create shaping policies to control bandwidth per protocol to optimize network performance. This function can reduce bandwidth for entertainment traffic and prioritize bandwidth for critical business traffic. Configure traffic shaping rules under "Security → Traffic Shaping → Add/Edit".

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770358646101-11566f7d-d469-4a14-9bd5-7ca3c04fbb04-993358.webp" alt="Traffic Shaping Entry"></p>

<p align="center"><strong>Figure 4-33 Traffic Shaping Entry</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770358703869-87ac1ec7-159a-46cf-809c-d158f2fe26ed-847279.webp" alt="Configure Traffic Shaping Rules"></p>

<p align="center"><strong>Figure 4-34 Configure Traffic Shaping Rules</strong></p>

Traffic shaping policies consist of a series of rules executed in order, similar to custom firewall rules. Each rule has two main parts: the traffic type to limit/shape and how it should be limited/shaped.

**Notes:**

- Traffic that does not match any rule is forwarded with Medium priority.
- When "Limit Bandwidth" is set to 0, the system does not limit bandwidth.
- Reserved bandwidth must not be greater than limited bandwidth.

### 4.6 Services

#### 4.6.1 Interface Management

In "Services → Interface Management", which local network is allowed on a specific interface can be set, and the interface rate can be configured.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770358963931-85f451c1-767a-4ab6-92ee-963e88de9f82-772061.webp" alt="Interface Management Page"></p>

<p align="center"><strong>Figure 4-35 Interface Management Page</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770359000798-ee21b633-76f5-4edb-85e9-8d5879e87a0a-642160.webp" alt="Modify Interface Configuration"></p>

<p align="center"><strong>Figure 4-36 Modify Interface Configuration</strong></p>

**Note:** Only interfaces in LAN mode can apply local subnets.

#### 4.6.2 DHCP Server

DHCP uses a client/server model: the client requests an address and the server assigns an IP address for dynamic IP allocation. Configure DHCP address pools under "Services → DHCP Server".

Default local subnet on ER2000: 192.168.100.1/24

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770359373874-05bb365f-91fb-4c46-9e00-e4fcef7b9b73-217137.webp" alt="Configure DHCP Address Pool"></p>

<p align="center"><strong>Figure 4-37 Configure DHCP Address Pool</strong></p>

**Notes:**

- DHCP services are generated based on local network information. After deleting a local subnet in the "Local Network List", its DHCP Server will also be deleted.
- DHCP Server takes effect only when the local network entry is in IP Mode. Networks in VLAN Only mode are not selectable.

#### 4.6.3 DNS Server

DNS (Domain Name System) servers translate human-readable domain names (e.g., www.example.com) into IP addresses (e.g., 192.168.1.1). DNS servers act as the Internet's address book, helping devices locate each other and ensuring information is delivered correctly.

If DNS server addresses are not configured under "Services → DNS Server", the device uses the DNS addresses obtained by the uplink interface for resolution. After DNS server addresses are configured, the configured DNS addresses will be used for domain name resolution.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770359444900-e3d75dfa-114c-4b97-bd65-a470534bcaa5-168552.webp" alt="Configure DNS Server"></p>

<p align="center"><strong>Figure 4-38 Configure DNS Server</strong></p>

#### 4.6.4 Fixed Address List

In "Services → Fixed Address List", a fixed IP address can be assigned to a device based on its MAC address. Each time the device connects to ER2000, it will obtain the same IP address.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770359475221-901bc305-28c9-4aad-874f-929be896af92-074292.webp" alt="Assign a Fixed IP Address to a Specific MAC Address"></p>

<p align="center"><strong>Figure 4-39 Assign a Fixed IP Address to a Specific MAC Address</strong></p>

**Notes:**

- The assignable address must be within the address range of a local network in IP Mode; otherwise the configuration will not take effect.
- When a local network is deleted, all fixed address assignment rules within that address range will be deleted.

#### 4.6.5 Static Routing

In "Services → Static Routing", static routing entries can be manually configured to forward data via specified paths and interfaces. All items in the static routing table are created manually. Routes automatically generated by other services (e.g., VPN) are not displayed here.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770359524144-a27fa6bf-2a22-40fc-9b4b-016ad749b4c0-502736.webp" alt="Configure Static Routing Entry"></p>

<p align="center"><strong>Figure 4-40 Configure Static Routing Entry</strong></p>

**Notes:**

- For static routes with the same destination address/network, the next-hop address, interface, or priority cannot be the same; otherwise the route will be invalid.
- After WAN2, Wi-Fi (STA), or L2TP Client VPN is deleted, static routes using the corresponding interface will also be deleted.

#### 4.6.6 Dynamic DNS

Dynamic DNS (DDNS) automatically updates name server records in DNS. Domain names usually need to be associated with a fixed IP address. DDNS provides a fixed hostname for users with dynamic IP addresses so that external users can connect by periodically updated records.

Configure DDNS under "Services → Dynamic DNS".

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770359565613-e433526b-a281-408b-9e00-f1a0dc2fd2a0-233441.webp" alt="Configure Dynamic DNS Service"></p>

<p align="center"><strong>Figure 4-41 Configure Dynamic DNS Service</strong></p>

| Parameter | Description |
|-----------|-------------|
| Service Provider | Provided by the DDNS provider. Choices: dyndns, 3322, oray, no-ip, or Custom (URL required). |
| Hostname | Register via the URL under the service provider to obtain a hostname. |
| Username | Register via the URL under the service provider to obtain a username. |
| Password | Password set during registration. |

### 4.7 System

Under [System], cloud management, remote access control, clock, device options, configuration management, device alerts, tools, log server, and more can be configured.

#### 4.7.1 Cloud Management

InCloud Manager (star.inhandcloud.cn) is a cloud platform built by InHand Networks to address slow deployment, complex O&M, and poor business experience in enterprise networks. Centered on user needs, it integrates zero-touch deployment, intelligent O&M, security protection, and excellent business experience. Once the device connects to the cloud platform, users can perform remote management, batch configuration, traffic monitoring, etc., enabling more convenient and efficient network device management.

In "System → Cloud Management", the cloud platform address can be selected. ER2000 connects to InCloud Manager automatically after it is online by default. If cloud management is not desired, it can be disabled manually.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770359737270-e28b033e-eb17-480b-9a02-e5c8530fdefd-932285.webp" alt="Enable InCloud Manager Service"></p>

<p align="center"><strong>Figure 4-42 Enable InCloud Manager Service</strong></p>

#### 4.7.2 Remote Access Control

In "System → Remote Access Control", access to the router's Web UI from the Internet can be enabled/disabled and service ports can be set.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770359831564-c4fbab68-80f0-40ca-b129-8dc041f89a0f-911540.webp" alt="Configure Remote Access Protocols"></p>

<p align="center"><strong>Figure 4-43 Configure Remote Access Protocols</strong></p>

| Parameter | Description |
|-----------|-------------|
| HTTPS | When enabled, enter the uplink public address & port in a browser to remotely access the router Web UI. |
| SSH | When enabled, use a remote tool (e.g., CRT) and enter the uplink public address & port, username, and password to remotely log in to the router backend. |
| Ping | When enabled, the uplink interface address allows external networks to initiate Ping requests. |

**Notes:**

- LAN interfaces are not affected by this configuration.
- Firewall rules do not restrict remote access.

#### 4.7.3 System Clock

In networking, the clock function coordinates and synchronizes time between network devices. It is important for data transmission, logging, security, coordination, and troubleshooting. In "System → Clock", select the local time zone and configure the NTP server address to synchronize the device system time.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770360338678-11ce93b9-c2c8-44b3-97ae-a1e71a01d38a-650901.webp" alt="Select Time Zone and Configure NTP Server Address"></p>

<p align="center"><strong>Figure 4-44 Select Time Zone and Configure NTP Server Address</strong></p>

#### 4.7.4 Device Options

In "System → Device Options", the device can be rebooted, firmware can be upgraded, and factory settings can be restored.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770360424922-814e4ea6-d02a-4ea5-9fb3-36fbb35b90f1-529493.webp" alt="Reboot/Upgrade/Restore Factory Settings"></p>

<p align="center"><strong>Figure 4-45 Reboot/Upgrade/Restore Factory Settings</strong></p>

**Notes:**

- For local firmware upgrades, ensure the firmware is obtained from official channels to avoid device unavailability caused by incorrect firmware.
- After the device connects to the cloud platform, due to the cloud configuration synchronization mechanism, the platform may push the pre-reset configuration back to the device; the device only clears historical data.

#### 4.7.5 Configuration Management

Configuration backup and restore are key network management tasks. In "System → Configuration Management", device configuration can be exported locally. When configuration is lost or needs to be overwritten, import the backup configuration to restore it.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770360485807-d44440da-e88a-45d6-b9c4-02b79bcef35d-041465.webp" alt="Manage Device Configuration Files"></p>

<p align="center"><strong>Figure 4-46 Manage Device Configuration Files</strong></p>

#### 4.7.6 Device Alerts

If special attention to certain events is desired, select the corresponding alert events and set the email address to receive alerts. When an alert event occurs, the device automatically sends an email notification. Events not selected will still be recorded in local logs. Configure alert event types and alert email address in "System → Device Alerts".

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770360524429-7059091e-ba83-4614-a974-c55acb394a39-030743.webp" alt="Select Alert Events"></p>

<p align="center"><strong>Figure 4-47 Select Alert Events</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770360550417-826cd721-5ea4-41b8-843d-d068ba697327-398598.webp" alt="Configure Alert Email Recipient"></p>

<p align="center"><strong>Figure 4-48 Configure Alert Email Recipient</strong></p>

#### 4.7.7 Tools

**Ping**

Uses ICMP to test network connectivity. Enter any domain name or IP address in "Target" and click Start to test connectivity.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770360721414-d306ff81-f329-481e-b775-b155fdbf0e95-082243.webp" alt="Ping Test Tool"></p>

<p align="center"><strong>Figure 4-49 Ping Test Tool</strong></p>

**Traceroute**

Traceroute is a network diagnostic tool used to determine the path packets take from source to destination and each intermediate hop/router. In "System → Tools → Traceroute", enter the target host IP address, select the egress interface, and click Start to test routing connectivity.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770360756693-dcb08d80-e12a-4edd-98da-239adb8f1a03-654176.webp" alt="Traceroute Tool"></p>

<p align="center"><strong>Figure 4-50 Traceroute Tool</strong></p>

**Capture**

Packet capture is a network monitoring and analysis technique that captures and records packets transmitted over a network. It is commonly used for troubleshooting, performance analysis, security audits, and protocol analysis. In "System → Tools → Capture", packets can be captured on a specific interface. Under "Output", captured data can be displayed in the UI or exported locally.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770360774108-370fa28c-c349-4c89-bbec-8c9533de4004-637510.webp" alt="Packet Capture Tool"></p>

<p align="center"><strong>Figure 4-51 Packet Capture Tool</strong></p>

**Iperf**

Iperf is a TCP/UDP network performance testing tool that measures bandwidth and network quality and provides statistics such as latency jitter, packet loss rate, and MTU. Administrators can use these statistics to locate bottlenecks and troubleshoot network issues.

In "System → Tools → Iperf", traffic generation can be configured as server or client to test network performance.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770361045198-7864d542-3b28-43b0-b331-ce2134585755-360969.webp" alt="Traffic Test Tool (Iperf)"></p>

<p align="center"><strong>Figure 4-52 Traffic Test Tool (Iperf)</strong></p>

#### 4.7.8 Scheduled Reboot

Scheduled reboot is a device management strategy that automatically reboots the device at specific times or conditions to ensure stable operation and performance. In "System → Scheduled Reboot", the reboot time can be set. The device supports rebooting at fixed times daily, weekly, or monthly.

For monthly schedules, if the selected reboot day is greater than the actual days of that month, the device reboots on the last day of the month. For example, if rebooting on the 31st is selected, in a 30-day month the device will reboot on the 30th.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770361185701-a737900f-d5cc-4b1c-bef5-8389581a60e7-807742.webp" alt="Set Reboot Time"></p>

<p align="center"><strong>Figure 4-53 Set Reboot Time</strong></p>

#### 4.7.9 Log Server

A log server is a dedicated server or software application used to collect, store, and manage logs generated by network devices, applications, and operating systems. Logs include events, warnings, errors, activities, and other information important for monitoring, troubleshooting, and performance optimization.

After enabling the log server function in "System → Log Server", the device periodically uploads log files to the specified log server.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770361207016-3a5ce7df-b354-44c2-9f18-66e7073184f1-558514.webp" alt="Specify Log Server Address"></p>

<p align="center"><strong>Figure 4-54 Specify Log Server Address</strong></p>

#### 4.7.10 Account Management

In "Services → Account Management", the username and password for logging in to the device Web page can be set. Keep the password secure to avoid leakage.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770361229987-ad1f5e7c-15be-4819-9c87-6258f1ce2da4-259045.webp" alt="Modify Web Login Account/Password"></p>

<p align="center"><strong>Figure 4-55 Modify Web Login Account/Password</strong></p>

#### 4.7.11 Other Settings

**Web Login Management**

If the Web session remains online for a certain period, the system will automatically log out or disconnect to protect privacy and security. Set the logout time under "System → Other Settings → Web Login Management". Once a single session exceeds the configured time, the system logs out and login is required again.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770361275483-2fe985f3-d9b3-49c2-8cec-c3cfa79fd330-663902.webp" alt="Set Web Login Timeout"></p>

<p align="center"><strong>Figure 4-56 Set Web Login Timeout</strong></p>

**SIP ALG**

SIP ALG combines Session Initiation Protocol (SIP) and Application Layer Gateway (ALG). It is used to help manage and process SIP communications (used to establish and manage real-time sessions such as voice/video calls). Enable this feature under "System → Other Settings → SIP ALG". If there are VoIP devices on the network, disable this feature.

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770361288327-a51781a0-0878-4ce7-a348-442d8b519aab-857864.webp" alt="Enable SIP ALG"></p>

<p align="center"><strong>Figure 4-57 Enable SIP ALG</strong></p>

---

## Chapter 5 Typical Applications

### Case 1: IPsec VPN Networking

**Scenario Description**: A branch office (ER815) and a central site (ER2000) in different regions need to securely access each other over the Internet.

**Network Topology**:

(Details not provided in original draft; to be supplemented)

**Device Role**: ER2000 acts as the IPsec VPN server, providing stable and reliable network access for the branch IPsec client.

**Configuration Steps**:
1. On ER2000, go to "VPN → IPsec VPN", click "Add" to create a new IPsec VPN entry.
2. Fill in Name, Pre-shared Key, Internet Interface (WAN2, IP 10.1.1.1), Local Subnet (192.168.100.0/24), and Remote Subnet (192.168.2.0/24).
3. On ER815 (client side), go to "VPN → IPsec VPN", click "Add" to create the client entry. Fill in the same Pre-shared Key, select the uplink interface (WAN1, IP 10.1.1.2), set Local Subnet (192.168.2.0/24), Remote Subnet (192.168.100.0/24), and Remote Address (10.1.1.1).
4. Save the configurations on both devices and check the tunnel status under [Status → VPN].

**Reference Chapters**:
- [IPsec VPN](#441-ipsec-vpn)
- [VPN Status](#4242-vpn)

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770356292972-fc45cf37-c245-4e7d-907e-a80c112b0451-070897.webp" alt="IPsec Server-side Configuration"></p>

<p align="center"><strong>Figure 5-1 IPsec Server-side Configuration</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770356461685-49b56602-558e-4acc-a74d-2fff3bbbc2ab-767994.webp" alt="IPsec Client-side Configuration"></p>

<p align="center"><strong>Figure 5-2 IPsec Client-side Configuration</strong></p>

### Case 2: L2TP VPN Networking

**Scenario Description**: A branch office (ER815) and a central site (ER2000) need to access each other via an L2TP VPN tunnel.

**Network Topology**:

(Details not provided in original draft; to be supplemented)

**Device Role**: ER2000 acts as the L2TP VPN server, providing remote access services for the branch L2TP client.

**Configuration Steps**:
1. On ER2000, go to "VPN → L2TP VPN → Server". Enable the server, select WAN1 (10.5.3.1) as the uplink interface, and set the VPN communication address to 10.11.12.11. The address pool will auto-fill to 10.11.12.1–10.11.12.254. Set the Username and Password.
2. On ER815 (client side), go to "VPN → L2TP VPN → Client", click "Add". Enter the server address, and set the same Username and Password as the server.
3. Save the configurations on both devices and check the tunnel status under [Status → VPN].

**Reference Chapters**:
- [L2TP VPN](#442-l2tp-vpn)
- [VPN Status](#4242-vpn)

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770357579483-19fb88e2-9e09-434f-87ef-fa6359a7a946-229747.webp" alt="L2TP Server-side Configuration"></p>

<p align="center"><strong>Figure 5-3 L2TP Server-side Configuration</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770357936279-ed59ea0f-a8fb-4c05-8274-203aab093c57-187925.webp" alt="L2TP Client-side Configuration"></p>

<p align="center"><strong>Figure 5-4 L2TP Client-side Configuration</strong></p>

### Case 3: SD-WAN Deployment

**Scenario Description**: Enterprise branches need to communicate for business data transfer and video conferencing. Traditional VPN configuration is complex and troubleshooting can be challenging. SD-WAN is used to quickly create connections between branches through a user-friendly interface.

**Network Topology**:

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770361534057-c9913a26-9bdd-43e3-8584-66ad8a7e9d70-935983.webp" alt="SD-WAN Application Scenario"></p>

<p align="center"><strong>Figure 5-5 SD-WAN Application Scenario</strong></p>

**Device Role**: ER2000 can act as the Hub (central) device in an SD-WAN network, managing tunnels to all Spoke (branch) devices.

**Prerequisites**:

- All devices used for SD-WAN networking must have the Branch Professional Edition license.
- All devices can access the Internet, and the subnets that need to communicate within the SD-WAN network have been planned and configured.

**Configuration Steps**:
1. In InCloud Manager under "Network", select "SD-WAN" and click "Add". The SD-WAN network creation page will open.
2. The SD-WAN network currently supports a hub-and-spoke topology. Select ER2000 as the Hub device and add branch devices as Spokes.
3. When adding the Hub device, the public address must be set to the actual mapped public IP. If the Hub has no public IP address, the upstream router can map via NAT to ER2000.
4. After adding, click "Edit" to customize subnets and static routes in the SD-WAN network.
5. Save the network. All devices and selected subnets will interconnect. Within a single network, the local networks of the Hub and Spokes must not be the same, otherwise communication may be affected.

**Verification Method**:
1. After adding the network, the system automatically directs to the topology page. Alternatively, go to the "SD-WAN Networks" list and click the network name to open the topology details page.
2. In the network, all branch devices create connections to the Hub device. Verify that all tunnel statuses are normal.

**Reference Chapters**:
- [Cloud Management](#471-cloud-management)
- [Uplink Settings](#425-uplink-settings)

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770361616594-b5e1290e-72a3-4cc3-bb25-a0834b0b03f5-205310.webp" alt="SD-WAN Network Entry"></p>

<p align="center"><strong>Figure 5-6 SD-WAN Network Entry</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770361665587-a2b72df9-c248-4b9b-88c3-412b6f4b2379-834878.webp" alt="Edit SD-WAN Network"></p>

<p align="center"><strong>Figure 5-7 Edit SD-WAN Network</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770362465306-d595355c-5468-4004-b6e2-e1376af0f552-182153.webp" alt="Add Hub Device"></p>

<p align="center"><strong>Figure 5-8 Add Hub Device</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770362550199-2a4e6981-530b-42fb-b599-92832099952f-201735.webp" alt="Add Static Routes"></p>

<p align="center"><strong>Figure 5-9 Add Static Routes</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770362668389-af4efed4-2fc9-454c-b19e-98a3729ed44c-471788.webp" alt="Add Branch Site Device"></p>

<p align="center"><strong>Figure 5-10 Add Branch Site Device</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770362720760-760b0284-9401-4438-aed5-43d83ed78dae-431499.webp" alt="View SD-WAN Network Topology"></p>

<p align="center"><strong>Figure 5-11 View SD-WAN Network Topology</strong></p>

<p align="center"><img src="./img/rSGDpl_1ChZVcaEv/1770362813859-cf92b905-8724-4ee0-9fb5-14f45b2e5d4b-995155.webp" alt="Branch SD-WAN Scenario"></p>

<p align="center"><strong>Figure 5-12 Branch SD-WAN Scenario</strong></p>

---

## Appendix: Troubleshooting

### A.1 Network Connection Issues

| Symptom | Possible Cause | Troubleshooting Steps | Related Chapter |
|-----------|----------------|----------------------|-----------------|
| No Internet access | WAN cable not connected or upstream fault | 1. Check the WAN cable connection.<br>2. Verify the upstream network is functional. | [Wired Connection (DHCP)](#421-wired-connection-dhcp) |
| No Internet access | Incorrect connection method (PPPoE/Static IP required) | 1. Confirm with the ISP whether PPPoE credentials or a static IP are required.<br>2. Reconfigure the WAN interface accordingly. | [Wired Connection (Static IP)](#422-wired-connection-static-ip) |
| Cannot obtain an IP address on LAN | PC not in the same subnet | 1. Verify the PC is set to obtain an IP automatically.<br>2. Check the LAN subnet configuration. | [Local Network](#43-local-network) |
| Device remains offline on cloud platform | Incorrect serial number or MAC address | 1. Re-check the serial number and MAC address on the device label.<br>2. Verify the device has Internet access. | [Connect to InCloud Manager Platform](#scenario-2-connect-to-incloud-manager-platform) |
| VPN tunnel not established | Pre-shared key mismatch | 1. Verify the pre-shared key is identical on both ends.<br>2. Check the local and remote subnet configuration. | [IPsec VPN](#441-ipsec-vpn) |
| VPN tunnel not established | Incorrect server address or unreachable | 1. Confirm the server IP address is correct.<br>2. Verify that the server-side uplink interface is reachable. | [L2TP VPN](#442-l2tp-vpn) |

### A.2 Web Access Issues

| Symptom | Possible Cause | Troubleshooting Steps | Related Chapter |
|-----------|----------------|----------------------|-----------------|
| Cannot open Web interface | PC IP address not in the same subnet | 1. Confirm the PC is in the 192.168.100.0/24 subnet.<br>2. Check the default gateway is set to 192.168.100.1. | [Installation Guide](#22-installation-guide) |
| Cannot open Web interface | Browser compatibility issue | 1. Use Google Chrome.<br>2. Clear the browser cache and retry. | [Installation Guide](#22-installation-guide) |

### A.3 Device Hardware Issues

| Symptom | Possible Cause | Troubleshooting Steps | Related Chapter |
|-----------|----------------|----------------------|-----------------|
| SYS LED is off | Power adapter not connected or faulty | 1. Check the power adapter connection.<br>2. Replace the power adapter if necessary. | [Installation Guide](#22-installation-guide) |
| SYS LED blinking red | System fault | 1. Wait for the system to recover.<br>2. If the issue persists, restore factory settings. | [Restore to Factory Defaults](#15-restore-to-factory-defaults) |

---

## Appendix: Safety Precautions

1. Use the original power adapter to avoid device damage caused by mismatch.
2. Do not install the device in environments with strong electromagnetic interference or too close to high-power equipment. After installation, ensure the device is stable to avoid damage from falling.
3. Ensure the operating environment meets the temperature and humidity requirements in the specification sheet.
4. Regularly check cables, including Ethernet cables and power adapter cables. Keep them clean and replace promptly if damaged.
5. When cleaning, avoid spraying chemical agents directly on the device surface to prevent damage to the enclosure or internal components. Use a soft cloth.
6. Do not disassemble, repair, or modify the device without authorization. This may cause safety issues and void the warranty.

---

## FAQ

### Q1: Is the cloud platform free?

InHand Networks is committed to providing high-quality network services for SMB chain organizations. To use cloud platform services, licenses must be purchased per device to access rich cloud features.

### Q2: How do I add the device to the cloud platform?

Register an InCloud Manager login account at [https://star.inhandcloud.com/](https://star.inhandcloud.com/).

Log in with the registered account, go to the Devices menu, click "Add", and follow the prompts to enter the device serial number and MAC address. After the device is added for the first time, a one-year free Basic license is granted by default. Users can renew as needed.

### Q3: Can the device be used without the cloud platform?

Yes. Most configuration functions can be completed locally. However, batch configuration delivery, upgrades, SD-WAN, Connector, and other functions must be used together with the cloud platform.

If the problem cannot be solved using the answers above or other issues are encountered, please contact Beijing InHand Networks Technology Co., Ltd. for technical support.
