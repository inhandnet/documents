# InGateway902 User Manual


## Declaration

Thank you for selecting this product. Prior to use, read this user manual carefully and observe the following statements. Compliance with these provisions helps maintain intellectual property rights and legal compliance, and ensures that the usage experience remains consistent with the latest product information. For questions or to obtain written permission, contact the technical support team.

- **Copyright Notice**

  This user manual contains copyright-protected material. All rights are reserved by Beijing InHand Networks Technology Co., Ltd. and its licensors. No part of this manual may be excerpted, reproduced, or transmitted in any form or by any means without prior written permission.

- **Disclaimer**

  Due to continuous updates in product technology and specifications, the company does not guarantee that the information in this user manual is entirely consistent with the actual product. Therefore, the company assumes no liability for disputes arising from discrepancies between actual technical parameters and the contents of this manual. Product changes may be made without prior notice. The company reserves the right of final modification and interpretation.

- **Copyright Information**

  The contents of this user manual are protected by copyright law. All rights are reserved by Beijing InHand Networks Technology Co., Ltd. and its licensors. No part of this manual may be used, copied, or distributed without prior written permission.

## GUI Conventions

The following symbols and formatting conventions are used throughout this manual:

| Symbol | Meaning | Example |
|--------|---------|---------|
| `< >` | Indicates a variable or parameter to be replaced with an actual value | `<IP address>` indicates that a specific IP address must be entered |
| `" "` | Indicates a text label on the interface | Click the "Save" button |
| `→` | Indicates a menu hierarchy or sequence of operations | **Network** → **Cellular** |
| `【 】` | Indicates a menu or page name | Navigate to the 【System Settings】page |

## Technical Support
Email: support@inhandnetworks.com

URL: www.inhand.com

## How to Use This Manual

### Reading Guide

- First-time users: It is recommended to read the chapters in the following order: "Getting to Know the Device" → "Installation and First Use" → "Common Scenario Configurations" → "Feature Descriptions and Parameter Reference"
- Existing device users: Refer directly to "Feature Descriptions and Parameter Reference" or "Appendix: Troubleshooting"
- Cloud platform management users: Refer to the device remote management platform sections in "Common Scenario Configurations" (where applicable)

### Quick Jump by Task

| Task | Corresponding Chapter | Estimated Time |
|------|----------------------|----------------|
| Network setup | [Network Configuration](#network-configuration) | As needed |
| Cellular configuration | [Cellular Network Configuration](#cellular-network-configuration) | Approx. 10 minutes |
| Ethernet configuration | [Ethernet Configuration](#ethernet-configuration) | Approx. 5 minutes |
| Wi-Fi setup | [WLAN Configuration](#wlan-configuration) | Approx. 5 minutes |
| VPN configuration | [VPN Configuration](#vpn-configuration) | Approx. 10 minutes |
| Firmware upgrade | [Firmware Upgrade](#firmware-upgrade) | Approx. 15 minutes |
| Python/Docker deployment | [Python and Docker](#python-and-docker) | As needed |
| Device Manager connection | [Device Manager](#device-manager) | Approx. 10 minutes |

**Default Access Information for the IG902 Edge Computing Gateway**

| Item | Default Value |
|------|---------------|
| GE 0/1 IP address | 192.168.1.1 |
| GE 0/2 IP address | 192.168.2.1 |
| Username | adm |
| Password | 123456 |



# Chapter 1 Know the Device

## 1.1 Overview

The InGateway902 (IG902) series is a new-generation 4G edge computing gateway developed by InHand Networks for the Industrial IoT sector. It provides omnipresent, uninterrupted Internet access over globally deployed 3G or 4G wireless networks and various broadband services. With edge computing capability and comprehensive features such as security guarantee and wireless services, the product is able to connect a large number of devices and provide high-speed data channels for IT-based device management. The edge computing capability enables data optimization, real-time response, agile connection, and intelligent analysis at the edge of the IoT. Using IG902 gateways as edge nodes can significantly reduce data traffic between the data center and on-site devices, and prevent bottlenecks of cloud computing. In addition, the IG902 optimizes the network architecture, and provides higher security, faster response, and more intelligent services.

<p align="center"><img src="images/img_88fa1490.webp" alt="Common application scenarios of the IG902"></p>

<p align="center"><strong>Figure 1-1 Common Application Scenarios of the IG902</strong></p>

## 1.2 Packing List

Each IG902 product is delivered with standard accessories frequently used at the customer site. Check the received product against the packing list carefully. If any accessory is missing or damaged, contact the InHand sales personnel promptly. InHand provides optional accessories based on the characteristics of different sites.

### Standard Accessories

| Item | Quantity | Description |
|------|----------|-------------|
| Gateway | 1 | Edge computing gateway |
| Product document | 1 | Quick installation manual and user manual (obtained by scanning a QR code) |
| Guide rail installation accessory | 1 | Used to fix the gateway |
| Power terminal | 1 | 7-pin industrial terminal |
| Network cable | 1 | 1.5 m long |
| Antenna | 1 | 3G or 4G specification |
| Product warranty card | 1 | Warranty period: 1 year |
| Certificate of conformance | 1 | Certificate of conformance for the edge computing gateway |

### Optional Accessories

| Item | Quantity | Description |
|------|----------|-------------|
| AC power cord | 1 | Power cord for American, English, Australian, or European Standard |
| Power Adapter | 1 | 12VDC Power Adapter |
| Wi-Fi Antenna | 1 | Wi-Fi Antenna |
| GPS Antenna | 1 | GPS Antenna |
| Serial Port | 1 | Gateway serial port line for debugging |

## 1.3 Appearance and Interfaces

The IG900 series product is applicable to multiple panel appearances, as they have the same installation method. Refer to the actual product during operation.

<p align="center"><img src="images/img_4ba25f02.webp" alt="IG902 panel appearance"></p>

<p align="center"><strong>Figure 1-2 IG902 Panel Appearance</strong></p>

<p align="center"><img src="images/img_ff10e4d7.png" alt="IG902 structure and dimensions"></p>

<p align="center"><strong>Figure 1-3 IG902 Structure and Dimensions</strong></p>

(Original manuscript does not provide details, to be supplemented)

| Interface | Position | Function |
|-----------|----------|----------|
| (Original manuscript does not provide details, to be supplemented) | (Original manuscript does not provide details, to be supplemented) | (Original manuscript does not provide details, to be supplemented) |

## 1.4 Indicator Lights

### LED Indicator

<p align="center"><img src="images/img_9901c7f4.webp" alt="IG902 LED indicators"></p>

<p align="center"><strong>Figure 1-4 IG902 LED Indicators</strong></p>

<p align="center"><img src="images/img_14ee9646.png" alt="IG902 LED indicator details"></p>

<p align="center"><strong>Figure 1-5 IG902 LED Indicator Details</strong></p>

Note: Two SIM card indicators are provided. The indicator for SIM card 1 is turned on during the startup process and when startup is successful. In the last four situations, the indicator for the used SIM card is turned on. The following figure shows the indicator for SIM card 1.

(Original manuscript does not provide details, to be supplemented)

| Indicator | Status | Meaning |
|-----------|--------|---------|
| (Original manuscript does not provide details, to be supplemented) | (Original manuscript does not provide details, to be supplemented) | (Original manuscript does not provide details, to be supplemented) |

### Signal Status Indicator

<p align="center"><img src="images/img_0451941d.png" alt="Signal status indicator 1-9"></p>

<p align="center"><strong>Figure 1-6 Signal Status Indicator (1-9)</strong></p>

Signal: 1-9, there might be a signal problem. Check whether the antenna is installed properly and whether the signal quality in the operating area is good.

<p align="center"><img src="images/img_2bb7898d.png" alt="Signal status indicator 10-19"></p>

<p align="center"><strong>Figure 1-7 Signal Status Indicator (10-19)</strong></p>

Signal: 10-19, indicating that signal and device operation are normal.

<p align="center"><img src="images/img_8430e16f.png" alt="Signal status indicator 20-31"></p>

<p align="center"><strong>Figure 1-8 Signal Status Indicator (20-31)</strong></p>

Signal: 20-31, indicating good signal.

## 1.5 Factory Reset

There are two ways to restore the IG902 to factory settings: hardware factory reset and software factory reset.

### Hardware Factory Reset

1. After the device is powered on and the ERR light is off, press and hold the RESET key.
2. When the ERR light is always on, release the RESET key.
3. After the ERR light goes out, press and hold the RESET key again, and release the RESET key when the ERR light flashes. Wait for the ERR light to go out, indicating that the factory reset was successful.

### Software Factory Reset

1. Log in to the web management interface.
2. Navigate to System Management > Configuration Management.
3. Click the reset button and select OK. The IG902 will complete the factory reset operation automatically.

<p align="center"><img src="images/img_6e79f519.webp" alt="Software factory reset interface"></p>

<p align="center"><strong>Figure 1-9 Software Factory Reset Interface</strong></p>

## 1.6 Default Settings

| Parameter | Default Value |
|-----------|---------------|
| GE 0/1 IP address | 192.168.1.1 |
| GE 0/2 IP address | 192.168.2.1 |
| Web login username | adm |
| Web login password | 123456 |
| PC IP configuration (Method 1) | Obtain an IP address automatically (recommended) |
| PC IP configuration (Method 2) | Static IP: any from 192.168.2.2 to 192.168.2.254; Subnet mask: 255.255.255.0; Default gateway: 192.168.2.1 |



# Chapter 2 Installation and First Use

## 2.1 Pre-installation Preparation

Before installing the IG902 gateway, verify that the installation environment, tools, and accessories meet the following requirements.

### 2.1.1 Environment Requirements

| Item | Requirement |
|------|-------------|
| Power supply | 24 V DC (12–48 V DC range acceptable); rated current 0.6 A (range 1.2–0.3 A) |
| Operating temperature | –25°C to 75°C |
| Storage temperature | –40°C to 85°C |
| Relative humidity | 5% to 95% (non-condensing) |
| Installation surface | Industrial DIN-rail or wall with adequate load-bearing capacity |

> **Caution**: The device surface temperature may become high during operation. Install the device in a restricted access area and assess the surrounding environment before installation.

### 2.1.2 Safety Precautions

> **Caution**: Verify the voltage class before connecting power. Incorrect voltage may cause equipment damage or safety hazards.

> **Caution**: Avoid direct sunlight and keep the device away from thermal sources or areas with strong electromagnetic interference.

> **Caution**: Ensure all required cables and connectors are available and undamaged before beginning installation.

### 2.1.3 Tools and Accessories Checklist

| Item | Quantity | Status |
|------|----------|--------|
| IG902 gateway | 1 | Required |
| Power terminal block | 1 | Required |
| DIN-rail (if applicable) | 1 | Required |
| Wall mounting bracket with screws (if applicable) | 1 set | Optional |
| SIM card (if using cellular) | 1–2 | Optional |
| Cellular antenna(s) | 1–2 | Optional |
| Ethernet cable | 1+ | Required |
| Ground cable | 1 | Recommended |
| Screwdriver | 1 | Required |

---

## 2.2 Installation Guide

### 2.2.1 DIN-Rail Installation

1. Select an installation location and reserve adequate space for mounting and cable routing.
2. Insert the upper part of the DIN-rail seat onto the DIN-rail. Grasp the lower end of the device and rotate it upward in the direction indicated by arrow 2 with gentle force, to engage the DIN-rail seat onto the DIN-rail. Verify that the device is securely mounted on the DIN-rail, as shown in the following figure.

<p align="center"><img src="images/img_dbd13c1a.png" alt="DIN-rail installation"></p>

<p align="center"><strong>Figure 2-1 DIN-Rail Installation</strong></p>

### 2.2.2 DIN-Rail Uninstallation

1. Press the device downward in the direction indicated by arrow 1 in the following figure to create a gap near the lower end of the device so that the device disengages from the DIN-rail.
2. Rotate the device in the direction indicated by arrow 2, grasp the lower end of the device, and move the device outward. Lift the device when its lower end is free from the DIN-rail. Then remove the device from the DIN-rail.

<p align="center"><img src="images/img_dc825e04.png" alt="DIN-rail uninstallation"></p>

<p align="center"><strong>Figure 2-2 DIN-Rail Uninstallation</strong></p>

### 2.2.3 Wall-Mounted Installation

1. Select an installation location and reserve adequate space for mounting and cable routing.
2. Attach the wall mounting bracket to the back of the device using a screwdriver, as shown in the following figure.

<p align="center"><img src="images/img_6240508c.png" alt="Attach wall mounting bracket"></p>

<p align="center"><strong>Figure 2-3 Attach Wall Mounting Bracket</strong></p>

3. Remove the screws (packaged with the wall mounting bracket), fasten the screws at the installation positions using the screwdriver, and pull down the device to secure it, as shown in the following figure.

<p align="center"><img src="images/img_0e41e169.webp" alt="Secure device to wall"></p>

<p align="center"><strong>Figure 2-4 Secure Device to Wall</strong></p>

### 2.2.4 Wall-Mounted Uninstallation

Hold the device with one hand and unfasten the screws that secure the upper end of the device with the other hand, to remove the device from the installation location.

### 2.2.5 SIM Card Installation

The IG902 supports dual SIM cards. Unfasten the screws on the cover of the SIM card holder using a screwdriver and insert a SIM card.

<p align="center"><img src="images/img_73f941ed.webp" alt="SIM card installation"></p>

<p align="center"><strong>Figure 2-5 SIM Card Installation</strong></p>

### 2.2.6 Antenna Installation

Rotate the movable part of the metal SMA interface with gentle force until it cannot be rotated further, at which point the outer thread of the antenna connection cable is no longer visible. Do not twist the antenna with excessive force by grasping the black plastic cover.

<p align="center"><img src="images/img_65784960.webp" alt="Antenna installation"></p>

<p align="center"><strong>Figure 2-6 Antenna Installation</strong></p>

> **Caution**: The IG902 supports dual antenna configuration: ANT antenna and AUX antenna. The ANT antenna transmits and receives data. The AUX antenna only increases antenna signal strength and cannot be used independently for data transmission. In normal conditions, only the ANT antenna is used. The AUX antenna is used together with the ANT antenna only when the signal is poor and signal strength must be improved.

### 2.2.7 Power Supply Connection

1. Remove the terminal block from the gateway.
2. Unfasten the locking screw on the terminal block.
3. Connect the power cable to the terminal block and fasten the locking screw.

<p align="center"><img src="images/img_97f67394.webp" alt="Power supply connection"></p>

<p align="center"><strong>Figure 2-7 Power Supply Connection</strong></p>

> **Caution**: Verify the polarity and voltage before applying power. Incorrect connection may damage the device.

### 2.2.8 Ground Protection Connection

1. Unfasten the ground screw cap.
2. Place the ground loop of the cabinet ground cable onto the ground post.
3. Fasten the ground screw cap.

> **Caution**: Ground the gateway to improve its interference resistance. Connect the ground cable to the ground post of the gateway based on the operating environment.

### 2.2.9 Network Cable Connection

Connect the gateway to a PC directly using an Ethernet cable.

<p align="center"><img src="images/img_5d2b1fbb.webp" alt="Network cable connection"></p>

<p align="center"><strong>Figure 2-8 Network Cable Connection</strong></p>

### 2.2.10 Terminal Connection (Industrial Interface Models)

> **Caution**: This section is only applicable to IG902 models equipped with industrial interfaces.

Terminals provide RS-232 and RS-485 interface modes. Connect cables to the corresponding terminals before using the interfaces. During installation, remove the terminals from the device, unfasten the locking screws on the terminals, connect cables to the corresponding terminals, and fasten the screws. Arrange the cables in an orderly manner.

<p align="center"><img src="images/img_5ba016b9.png" alt="Terminal connection"></p>

<p align="center"><strong>Figure 2-9 Terminal Connection</strong></p>

### 2.2.11 Web Interface Login

By default, the IP address of GE 0/1 on the IG902 is 192.168.1.1; the IP address of GE 0/2 on the IG902 is 192.168.2.1. The following procedure uses the GE 0/2 port to access the IG902 as an example.

1. Configure the PC IP address to be on the same subnet as GE 0/2.
   - Method 1: Enable the PC to obtain an IP address automatically (recommended).

   <p align="center"><img src="images/img_594d3d19.png" alt="Obtain IP address automatically"></p>

   <p align="center"><strong>Figure 2-10 Obtain IP Address Automatically</strong></p>

   - Method 2: Set a fixed IP address.

     Select "Use the following IP address", enter an IP address (by default, any address from 192.168.2.2 to 192.168.2.254), subnet mask (by default, 255.255.255.0), default gateway (by default, 192.168.2.1), and DNS server address, and click OK.

   <p align="center"><img src="images/img_b89d3808.png" alt="Set fixed IP address"></p>

   <p align="center"><strong>Figure 2-11 Set Fixed IP Address</strong></p>

2. Launch the browser on the PC and access the IP address of GE 0/2. Enter the login username and password. The default username and password are `adm` and `123456` respectively.

   <p align="center"><img src="images/img_3b04186d.webp" alt="Web login page"></p>

   <p align="center"><strong>Figure 2-12 Web Login Page</strong></p>

3. After successful login, the web management interface is displayed as shown below.

   <p align="center"><img src="images/img_2bcecb94.webp" alt="Web management interface"></p>

   <p align="center"><strong>Figure 2-13 Web Management Interface</strong></p>

4. To change the username and password for logging in to the web management interface of the IG902, navigate to System > User Management and set the new username and password.

   <p align="center"><img src="images/img_55e0c69c.webp" alt="User management page"></p>

   <p align="center"><strong>Figure 2-14 User Management Page</strong></p>

5. To change the IP address of GE 0/2, navigate to Network > Network Interfaces > Ethernet > Gigabitethernet 0/2 to configure GE 0/2.

   <p align="center"><img src="images/img_8e76ad7d.webp" alt="Ethernet interface configuration"></p>

   <p align="center"><strong>Figure 2-15 Ethernet Interface Configuration</strong></p>

---

## 2.3 Quick Check

After completing the installation, verify the following items to confirm that the device is installed and operating correctly.

| No. | Check Item | Expected Result | Status |
|-----|------------|-----------------|--------|
| 1 | Device is securely mounted on the DIN-rail or wall | No looseness or vibration | |
| 2 | SIM card is properly inserted (if using cellular) | SIM card holder cover is fastened | |
| 3 | Antenna is properly connected (if using cellular) | ANT antenna is tightened; AUX antenna is connected if needed | |
| 4 | Power cable is correctly connected | Device powers on and indicators light up | |
| 5 | Ground cable is connected | Ground screw cap is fastened | |
| 6 | Ethernet cable is connected between gateway and PC | PC network interface shows connection status | |
| 7 | PC IP configuration is correct | PC is on the same subnet as the gateway interface | |
| 8 | Web interface is accessible | Login page loads successfully with default credentials | |
| 9 | Industrial terminals are connected (if applicable) | Cables are secured and arranged orderly | |

> **Caution**: If any check item does not produce the expected result, power off the device and recheck the corresponding installation step before powering on again.



# Chapter 3 Common Scenario Configurations



## Scene 1: Web Access and Login

**Goal**: Access the IG902 web management interface via a PC browser and complete login authentication.

**Prerequisites**:
- The IG902 device is powered on.
- A PC is connected to the IG902 via the GE 0/2 interface (or GE 0/1 interface).
- A web browser is available on the PC.

**Estimated Time**: About 5 minutes.

**Operation Steps**:

1. Configure the PC IP address to be on the same subnet as the IG902 interface.
   - The default IP address of GE 0/1 on the IG902 is 192.168.1.1; the default IP address of GE 0/2 is 192.168.2.1. The following steps use the GE 0/2 port as an example.
   1.1. Method 1: Enable the PC to obtain an IP address automatically (recommended).

   <p align="center"><img src="images/img_6125aad4.png" alt="PC obtain IP automatically"></p>

   <p align="center"><strong>Figure 3-1 PC Obtain IP Address Automatically</strong></p>

   1.2. Method 2: Set a fixed IP address.
   Select "Use the following IP address", enter an IP address (any value between 192.168.2.2 and 192.168.2.254 by default), subnet mask (255.255.255.0 by default), default gateway (192.168.2.1 by default), and DNS server address, and click "OK".

   <p align="center"><img src="images/img_cf831e0b.png" alt="PC set fixed IP address"></p>

   <p align="center"><strong>Figure 3-2 PC Set Fixed IP Address</strong></p>

2. Launch the browser on the PC and access the IP address of GE 0/2 (192.168.2.1 by default). Enter the login user name and password on the login page. The default user name and password are **adm** and **123456** respectively.

   <p align="center"><img src="images/img_d4da9568.webp" alt="IG902 login page"></p>

   <p align="center"><strong>Figure 3-3 IG902 Login Page</strong></p>

3. After successful login, the web management interface is displayed as shown below.

   <p align="center"><img src="images/img_eb9e1ed7.webp" alt="IG902 web management interface"></p>

   <p align="center"><strong>Figure 3-4 IG902 Web Management Interface</strong></p>

4. (Optional) To change the login user name and password, navigate to 【System】→【User Management】, and set the new user name and password.

   <p align="center"><img src="images/img_55e0c69c.webp" alt="User Management page"></p>

   <p align="center"><strong>Figure 3-5 User Management Page</strong></p>

5. (Optional) To change the IP address of GE 0/2, navigate to 【Network】→【Network Interfaces】→【Ethernet】→【Gigabitethernet 0/2】 to configure the interface.

   <p align="center"><img src="images/img_8e76ad7d.webp" alt="GE 0/2 configuration page"></p>

   <p align="center"><strong>Figure 3-6 GE 0/2 Configuration Page</strong></p>

**Verification Method**:
1. Confirm that the IG902 web management interface is accessible in the browser.
2. Confirm that login is successful and the main dashboard page is displayed.



## Scene 2: Cellular Networking

**Goal**: Connect the IG902 to the Internet via a cellular network using a SIM card.

**Prerequisites**:
- A valid SIM card is available.
- The IG902 device is powered off.
- A 4G LTE antenna is available for connection.

**Estimated Time**: About 5 minutes.

**Operation Steps**:
1. Install the SIM card and antenna.
   1.1. Power off the IG902 before inserting or removing the SIM card to avoid data loss or hardware damage.
   1.2. Insert the SIM card into the SIM card slot.
   1.3. Connect the 4G LTE antenna to the ANT interface.
   1.4. Power on the IG902.

   <p align="center"><img src="images/img_44a1c2e2.webp" alt="SIM card and antenna installation" width="50%"></p>
   <p align="center"><strong>Figure 3-7 SIM Card and Antenna Installation</strong></p>

2. Enable the cellular network connection.
   2.1. Navigate to **Network > Network Interfaces > Cellular**.
   2.2. Select the **Enable Cellular** option.
   2.3. Click **Submit** to apply the configuration.

   <p align="center"><img src="images/img_196de994.webp" alt="Enable cellular network"></p>
   <p align="center"><strong>Figure 3-8 Enable Cellular Network</strong></p>

3. Verify the connection status.
   3.1. Check the network connection status on the Cellular page.
   3.2. Confirm that the status displays as **Connected** and an IP address has been allocated.

   <p align="center"><img src="images/img_6b186e82.webp" alt="Cellular connection status"></p>
   <p align="center"><strong>Figure 3-9 Cellular Connection Status</strong></p>

**Verification Method**:
1. On the Cellular page, verify that the connection status shows **Connected**.
2. Confirm that an IP address is displayed in the status area.
3. Attempt to access an external network or the Internet to confirm data connectivity.

**Common Issues**:
- **No connection after enabling cellular**: Verify that the SIM card is correctly inserted and the antenna is securely connected to the ANT interface.
- **No IP address allocated**: Check that the SIM card is active and has sufficient data balance. Confirm APN settings with the network operator if necessary.
- **Connection drops frequently**: Check the signal strength and ensure the device is positioned in an area with adequate cellular coverage.


## Scene 3: Ethernet Networking

**Goal**: Connect the IG902 to the Internet or a local network via the Ethernet interface.

**Prerequisites**:
- The IG902 is powered on and accessible via Web interface.
- An Ethernet cable is available.
- The network parameters (IP address, subnet mask, gateway) for the target network are known (if using static IP).

**Estimated Time**: About 5 minutes.

**Operation Steps**:
1. Connect the Ethernet cable to the target port.
   1.1. Use an Ethernet cable to connect the GE 0/1 or GE 0/2 port of the IG902 to the upstream network device (such as a switch or router).

   <p align="center"><img src="images/img_a50b04d3.webp" alt="Ethernet cable connection" width="40%"></p>
   <p align="center"><strong>Figure 3-10 Ethernet Cable Connection</strong></p>

2. Configure the Ethernet interface parameters.
   2.1. Navigate to **Network > Network Interfaces > Ethernet** to open the Ethernet page.
   2.2. Click the **Gigabitethernet 0/1** tab to configure the GE 0/1 port.
   2.3. Select a **Network Type** for the interface:
   
        - **Static IP**: Manually configure the IP address, subnet mask, and other parameters according to the site network conditions.
             - **Dynamic Address (DHCP)**: The interface automatically obtains an IP address, subnet mask, and other parameters from the DHCP server.
             2.4. Enter or select values for the remaining parameters as required. For details about these parameters, see the parameter description below.
             2.5. Click **Submit** to save the configuration of GE 0/1.
             2.6. (Optional) To configure GE 0/2, click the **Gigabitethernet 0/2** tab. By default, GE 0/2 is a bridge interface; to configure this interface, remove `gigabitethernet 0/2` from the **Bridge** page first.
             2.7. Select a network type for GE 0/2 and set the parameters.
             2.8. Click **Submit** to save the configuration of GE 0/2.
   
   The following figure shows the GE 0/1 configuration with **Network Type** set to **DHCP**.
   
   <p align="center"><img src="images/img_69eac962.png" alt="GE 0/1 DHCP configuration"></p>
   <p align="center"><strong>Figure 3-11 GE 0/1 DHCP Configuration</strong></p>
   
   The following figure shows the GE 0/1 configuration with **Network Type** set to **Static IP**.
   
   <p align="center"><img src="images/img_7532441b.webp" alt="GE 0/1 Static IP configuration"></p>
   <p align="center"><strong>Figure 3-12 GE 0/1 Static IP Configuration</strong></p>
   
   The following figure shows the GE 0/2 configuration with **Network Type** set to **Static IP**.
   
   <p align="center"><img src="images/img_f11a9230.webp" alt="GE 0/2 Static IP configuration"></p>
   <p align="center"><strong>Figure 3-13 GE 0/2 Static IP Configuration</strong></p>
   
3. (Optional) Add a static route.
   3.1. If the network requires static routing, navigate to **Network > Routing > Static Routing** to open the Static Routing page.
   3.2. Click the **Add** icon to add a static route.
   3.3. Set the parameters. For details about these parameters, see the static routing parameter description below.
   3.4. Click **OK** to save the configuration, and then click **Submit** to apply the configuration.

   The following figure shows an example static route configuration.

   <p align="center"><img src="images/img_5522d5ec.webp" alt="Static route configuration"></p>
   <p align="center"><strong>Figure 3-14 Static Route Configuration</strong></p>

**Verification Method**:
1. Navigate to **System > Network Tools** and use the Ping tool to verify network connectivity.
2. Enter a target IP address or domain name (such as `8.8.8.8`) and execute the ping test.
3. If replies are received, the IG902 has successfully connected to the target network.

   The following figure shows a successful ping test result.

   <p align="center"><img src="images/img_100902f1.webp" alt="Ping test success"></p>
   <p align="center"><strong>Figure 3-15 Ping Test Result</strong></p>

**Parameter Reference**:

Ethernet parameters are described as follows:

| Parameter | Description |
|-----------|-------------|
| Network Type | Specifies how the interface obtains its network address. **Static IP** (default): uses a manually configured IP address, subnet mask, and other information. **Dynamic Address (DHCP)**: configures the interface as a DHCP client to obtain an IP address and subnet mask automatically. |
| Primary IP | Specifies the IP address of the Ethernet interface. By default, the IP address of GE 0/1 is `192.168.1.1`, and the IP address of GE 0/2 is `192.168.2.1`. |
| Netmask | Specifies the subnet mask of the Ethernet interface. |
| MTU | Specifies the maximum transmit unit, expressed in bytes. The default value is `1500`. |
| Speed/Duplex | Specifies the link speed and duplex mode. Options include: Auto Negotiation, 1000M Full Duplex, 1000M Half Duplex, 100M Full Duplex, 100M Half Duplex, 10M Full Duplex, 10M Half Duplex. |
| Track L2 State | Enables or disables tracking of the Layer 2 interface status. When enabled, the interface state is Down when not physically connected and Up when physically connected. When disabled, the interface state is displayed as Up regardless of physical connection status. |
| Shutdown | Disables the interface. |
| Description | Specifies descriptive information that identifies the Ethernet interface. |
| Secondary IP Setting | Allows setting up to 10 secondary IP addresses in addition to the primary IP address. |

Static routing parameters are described as follows:

| Parameter | Description |
|-----------|-------------|
| Destination | Specifies the destination IP address to which packets are sent. |
| Netmask | Specifies the subnet mask of the destination IP address. |
| Interface | Specifies the interface through which data packets are forwarded to the destination network. |
| Gateway | Specifies the IP address of the next router that data packets pass through before reaching the destination IP address. |
| Distance | Specifies the priority of the route. A smaller value indicates a higher priority. |
| Track ID | Specifies the track index or ID. |

**Common Issues**:
- Unable to access the Internet via Ethernet: Verify that the network type and IP parameters match the site network conditions. If using DHCP, confirm that a DHCP server is available on the network.
- Ping test fails: Check the physical cable connection, verify the IP address and gateway configuration, and confirm that the upstream network device is functioning correctly.
- GE 0/2 cannot be configured: By default, GE 0/2 is part of a bridge interface. Remove `gigabitethernet 0/2` from the **Bridge** page before configuring it independently.



## Scene 4: Software Update

**Goal**: Update the IG902 firmware, Python SDK, or Docker SDK to obtain the latest features and improvements.

**Prerequisites**:
- The IG902 device is powered on and accessible via the Web interface.
- The firmware file, Python SDK file, or Docker SDK file has been obtained from the official resource website.
- A stable network connection or local file access is available.

**Estimated Time**: About 10 minutes.

**Operation Steps**:

1. Update the IG902 firmware.
   1.1. Navigate to **System > Firmware Upgrade** to display the **Firmware Upgrade** page.
   1.2. Click **Select File** to select a firmware file for the IG902.
   1.3. Click **Starting Upgrade** and **OK** to start the firmware upgrade.
   1.4. Wait until the upgrade succeeds, and then click **Reboot** to restart the IG902.

   <p align="center"><img src="images/img_5d21c1cd.webp" alt="Firmware Upgrade page"></p>

   <p align="center"><strong>Figure 3-16 Firmware Upgrade Page</strong></p>

2. Upgrade the Python SDK of IG902.
   2.1. Navigate to **Edge Computing > Python Edge Computing**.
   2.2. Select **Python Engine**.
   2.3. Select a Python SDK file and click **Upgrade**.
   2.4. When the upgrade confirmation window pops up, click **Confirm**.
   2.5. The IG902 automatically performs the upgrade.

   <p align="center"><img src="images/img_a9323b16.webp" alt="Python SDK Upgrade"></p>

   <p align="center"><strong>Figure 3-17 Python SDK Upgrade</strong></p>

3. Upgrade the Docker SDK of IG902.
   3.1. Navigate to **Edge Computing > Docker Manager**.
   3.2. Close the Docker Manager and import the Docker SDK.

   <p align="center"><img src="images/img_dc857fcb.webp" alt="Docker Manager Import SDK"></p>

   <p align="center"><strong>Figure 3-18 Docker Manager Import SDK</strong></p>

   3.3. After importing, the IG902 automatically installs the Docker SDK. The installation process usually takes 1-2 minutes.
   3.4. After successful installation, select **Enable Docker Manager** and click **Submit**.

   <p align="center"><img src="images/img_103f6982.webp" alt="Enable Docker Manager"></p>

   <p align="center"><strong>Figure 3-19 Enable Docker Manager</strong></p>

   3.5. After enabling the Docker Manager, click the access button of the Docker Manager to access the management page.

   <p align="center"><img src="images/img_6af58d66.webp" alt="Docker Manager Access Button"></p>

   <p align="center"><strong>Figure 3-20 Docker Manager Access Button</strong></p>

   3.6. Enter the account and password set in the figure above to log in to the Docker Manager.

   <p align="center"><img src="images/img_0f84657b.webp" alt="Docker Manager Login"></p>

   <p align="center"><strong>Figure 3-21 Docker Manager Login</strong></p>

**Verification Method**:
1. After the firmware upgrade completes and the device reboots, check the firmware version on the **System > Firmware Upgrade** page to confirm it matches the updated version.
2. After the Python SDK upgrade completes, verify the Python Engine status on the **Edge Computing > Python Edge Computing** page.
3. After the Docker SDK upgrade completes, verify that the Docker Manager is enabled and accessible on the **Edge Computing > Docker Manager** page.

**Common Issues**:
- Firmware upgrade fails: Verify that the firmware file is correct for the IG902 model and that the file is not corrupted.
- Device does not reboot after upgrade: Manually power cycle the device and check the firmware version again.
- Docker Manager cannot be accessed: Verify that the Docker Manager has been enabled and that the correct account credentials are used.



## Scene 5: Python Edge Computing Application

**Goal**: Deploy and manage custom Python applications on the IG902 using the Python Edge Computing engine.

**Prerequisites**:
- The IG902 device is powered on and accessible via the Web interface.
- The Python Edge Computing engine is enabled.
- The Python SDK is installed (optional but recommended for development).
- The App package file (.tar.gz or similar) is prepared for installation.

**Estimated Time**: About 15 minutes.

**Operation Steps**:

1. Enable the Python Edge Computing engine.
   1.1. Navigate to 【Edge Computing】→【Python Edge Computing】.
   1.2. Enable the Python edge computing engine.
   1.3. Install or upgrade the Python SDK if necessary.

   <p align="center"><img src="images/img_ffbc2629.webp" alt="Python Edge Computing engine and SDK status"></p>

   <p align="center"><strong>Figure 3-22 Python Edge Computing Engine and SDK Status</strong></p>

2. Install the Python App.
   2.1. On the 【Python Edge Computing】page, click the "Add" button.
   2.2. Select the App package file to be installed.
   2.3. Click "OK" to confirm the installation.

   <p align="center"><img src="images/img_dd72bd28.webp" alt="Add Python App"></p>

   <p align="center"><strong>Figure 3-23 Add Python App</strong></p>

   2.4. After importing, the installed App appears in the App list.

   <p align="center"><img src="images/img_ed93e881.webp" alt="Imported Python Apps list"></p>

   <p align="center"><strong>Figure 3-24 Imported Python Apps List</strong></p>

3. Enable and run the App.
   3.1. In the App list, select "Enable" for the target App.
   3.2. Click "Submit" to apply the configuration.

   <p align="center"><img src="images/img_aa50e704.webp" alt="Enable and submit Python App"></p>

   <p align="center"><strong>Figure 3-25 Enable and Submit Python App</strong></p>

   3.3. Once enabled, the App automatically runs and will run every time the IG902 starts.

   <p align="center"><img src="images/img_79c7c89e.webp" alt="Python App running status"></p>

   <p align="center"><strong>Figure 3-26 Python App Running Status</strong></p>

4. Update the App configuration file (optional).
   4.1. If the installed App supports configuration file import, click the "Import Configuration" button.
   4.2. Select the configuration file to be imported, then click "Confirm".

   <p align="center"><img src="images/img_2a953439.webp" alt="Import App configuration file"></p>

   <p align="center"><strong>Figure 3-27 Import App Configuration File</strong></p>

   4.3. Restart the App after the import is successful. The App will run according to the imported configuration file.

   <p align="center"><img src="images/img_9a919bc8.webp" alt="Restart App after configuration import"></p>

   <p align="center"><strong>Figure 3-28 Restart App After Configuration Import</strong></p>

5. Update the Python App version (optional).
   5.1. To update the App version, import the new version of the App package on the 【Python Edge Computing】page.

   <p align="center"><img src="images/img_41be4c37.webp" alt="Update Python App version"></p>

   <p align="center"><strong>Figure 3-29 Update Python App Version</strong></p>

   5.2. After the update is completed, the new version is displayed in the App list.

   <p align="center"><img src="images/img_3d625e15.webp" alt="App version updated"></p>

   <p align="center"><strong>Figure 3-30 App Version Updated</strong></p>

6. Enable debug mode (optional).
   6.1. On the 【Python Edge Computing】page, select "Enable Debug Mode".
   6.2. After enabling, the IG902 starts an SSH server on LAN port 222 (default IP address: 192.168.2.1).
   6.3. The SSH username and password are displayed on the Web page. A random password is generated each time debug mode is enabled or the device restarts.
   6.4. For details on using VS Code for Python development on IG902, refer to the MobiusPi Python Development Quick Start documentation.

   <p align="center"><img src="images/img_695a16ce.webp" alt="Enable debug mode"></p>

   <p align="center"><strong>Figure 3-31 Enable Debug Mode</strong></p>

**Verification Method**:
1. On the 【Python Edge Computing】page, verify that the App status shows "Running".
2. Click "View" to check the running logs of the specified App and confirm normal operation.

   <p align="center"><img src="images/img_666fafdc.png" alt="Python development environment configuration"></p>

   <p align="center"><strong>Figure 3-32 Python Development Environment Configuration</strong></p>

   <p align="center"><img src="images/img_d095640d.webp" alt="App running status example"></p>

   <p align="center"><strong>Figure 3-33 App Running Status Example</strong></p>

**Common Issues**:
- App fails to start: Verify that the Python Edge Computing engine is enabled and the App package is compatible with the current SDK version.
- Configuration import has no effect: Ensure the App is restarted after importing the configuration file.
- Debug mode connection fails: Verify that the client device is on the same LAN as the IG902 and that port 222 is accessible.

---

**App Configuration Functions Reference**:

| Function | Description |
|----------|-------------|
| Start all | Starts all enabled apps. |
| Stop all | Stops all enabled apps. |
| Restart all | Restarts all enabled apps. |
| Download | Downloads running logs of a specified app. |
| Delete | Deletes all running logs of a specified app. |
| View | Displays running logs of a specified app. |
| Stop | Stops a specified app. |
| Restart | Restarts a specified app. |
| Enable | Enables an app so it runs automatically after each system reboot. |
| Start Parameters | Configures app start parameters. |
| Export | Exports an app configuration file. |
| Import | Imports an app configuration file. After import and restart, the app runs with the imported configuration. |
| Unload | Unloads an app. |
| Add | Adds a new app. |



## Scene 6: Device Manager Connection

**Goal**: Connect the IG902 to the InHand Device Manager cloud platform for remote monitoring, maintenance, configuration delivery, and batch upgrades.

**Prerequisites**:
- The IG902 is powered on and has network access.
- A registered account on the target Device Manager platform is available.

**Estimated Time**: About 5 minutes.

**Operation Steps**:

1. Navigate to **System** > **Device Manager** to open the **Device Manager** page.
2. Select **Enable Device Manager**.
3. Configure the parameters according to the following descriptions:
   - **Server Address**: Specify the server address of the Device Manager platform to be connected. The addresses for InHand platforms are as follows:
     - Device Manager: `iot.inhandnetworks.com`
     - InConnect: `ics.inhandnetworks.com`
   - **Registered Account**: Specify the account registered on the Device Manager platform that is associated with the IG902 device.
   - **Advanced Settings**: Contains configurations such as heartbeat interval. The default configuration can generally be used. For detailed parameter descriptions, refer to the table below.
4. Click **Submit** to apply the configuration.

The following figure shows a sample configuration connecting the IG902 to the Device Manager (`iot.inhandnetworks.com`) platform.

<p align="center"><img src="images/img_422a641f.png" alt="Device Manager configuration page"></p>

<p align="center"><strong>Figure 3-34 Device Manager Configuration</strong></p>

**Device Manager Parameters**:

| Parameter | Description |
|-----------|-------------|
| Enable Device Manager | Enables or disables the Device Manager platform connection. |
| Server Address | Specifies the server address of the Device Manager platform to be connected. |
| Registered Account | Specifies an account registered on the Device Manager platform. |
| Advanced Settings | |
| -- Location Type | Specifies the source of the location information. Options are Cellular and GPS. |
| -- LBS Information Upload | Specifies the interval for reporting LBS information. The valid value range is 60–86400 seconds. |
| -- Interval | Specifies the interval between heartbeat packets exchanged with the Device Manager platform. The valid value range is 30–86400 seconds. |
| -- Dataflow Upload Interval | Specifies the interval for reporting traffic information. The valid value range is 3600–86400 seconds. |

**Verification Method**:
1. After the configuration is submitted, verify the connection status on the Device Manager page.
2. Confirm that the status displays as **Connection Accepted**, indicating the IG902 has successfully connected to the Device Manager.

<p align="center"><img src="images/img_f2af3a47.png" alt="Device Manager connection status"></p>

<p align="center"><strong>Figure 3-35 Device Manager Connection Status</strong></p>

**Common Issues**:
- Connection status does not show "Connection Accepted": Verify that the server address and registered account are correct, and ensure the IG902 has network access to the Internet.
- Unable to register an account: Access the Device Manager platform website to complete account registration before configuring the device.



## Scene 7: I/O Module Configuration

**Goal**: Configure the I/O module to support digital input, pulse counting, digital output, and pulse output functions, and enable remote I/O status reading via Modbus TCP.

**Prerequisites**:
- The IG902 device is equipped with an I/O module (as shown in Figure 3-1).
- The device has been powered on and the Web management interface is accessible.
- The physical I/O wiring has been completed according to the connection mode diagrams.

**Estimated Time**: About 15 minutes.

**Operation Steps**:

1. Navigate to the I/O configuration page.
   1.1. Log in to the device Web interface.
   1.2. Go to 【Edge Computing】→【IO Module】→【Configuration】.

2. Configure the I/O functions based on site requirements.
   2.1. **Digital input**: Set the digital input mode. The IG902 supports 4 channels of digital input. Dry contacts and wet contacts are determined based on actual connections.
      - Dry contact: 0 indicates open circuit; 1 indicates close to DICOM.
      - Wet contact: 0 indicates 0 V DC to 3 V DC / -3 V DC to 0 V DC; 1 indicates 10 V DC to 30 V DC / -30 V DC to -10 V DC (4 mA minimum).
      - Isolation: 3000 Vrms.

      <p align="center"><img src="images/img_58baad1f.webp" alt="IG902 I/O module" width="20%"></p>
      <p align="center"><strong>Figure 3-36 IG902 I/O Module</strong></p>

      <p align="center"><img src="images/img_87a49f9f.webp" alt="Digital input connection modes" width="50%"></p>
      <p align="center"><strong>Figure 3-37 Digital Input Connection Modes</strong></p>

   2.2. **Pulse counting**: Set the pulse counting parameters. The IG902 supports 4 channels with a maximum input frequency of 50 kHz and a maximum count of 4294967296 (32-bit). The starting value is 0, and the counted value is retained after power down.

      <p align="center"><img src="images/img_f4ba8eef.webp" alt="Pulse counting connection modes" width="50%"></p>
      <p align="center"><strong>Figure 3-38 Pulse Counting Connection Modes</strong></p>

      <p align="center"><img src="images/img_fa88dcc1.webp" alt="Pulse counting configuration"></p>
      <p align="center"><strong>Figure 3-39 Pulse Counting Configuration</strong></p>

   2.3. **Digital output**: Set the digital output parameters. The IG902 supports 4 channels. 0 indicates OFF; 1 indicates ON. Open collector to 30 V, 500 mA maximum per channel for resistance load. Isolation: 3000 Vrms.

      <p align="center"><img src="images/img_0899b4cf.webp" alt="Digital output connection modes" width="50%"></p>
      <p align="center"><strong>Figure 3-40 Digital Output Connection Modes</strong></p>

      <p align="center"><img src="images/img_5146c650.webp" alt="Digital output configuration"></p>
      <p align="center"><strong>Figure 3-41 Digital Output Configuration</strong></p>

   2.4. **Pulse output**: Set the pulse output parameters. A maximum of 5000 Hz pulse signal output is supported. The duty cycle is 50% for the pulse output at 5000 Hz frequency.

      <p align="center"><img src="images/img_c27f1101.webp" alt="Pulse output connection modes"></p>
      <p align="center"><strong>Figure 3-42 Pulse Output Connection Modes</strong></p>

      <p align="center"><img src="images/img_a81a0fc9.webp" alt="Pulse output configuration"></p>
      <p align="center"><strong>Figure 3-43 Pulse Output Configuration</strong></p>

3. Control pulse counting and pulse output (optional).
   3.1. After setting DI to pulse counting mode, click **Start** to begin counting the pulses received by the DI. Click **Reset** to reset the count value to the starting value.

      <p align="center"><img src="images/img_ca451e4b.png" alt="Pulse counting control"></p>
      <p align="center"><strong>Figure 3-44 Pulse Counting Control</strong></p>

   3.2. After setting DO to pulse output mode, click **Start** to output pulses based on the specified output frequency.

      <p align="center"><img src="images/img_442dc407.png" alt="Pulse output control"></p>
      <p align="center"><strong>Figure 3-45 Pulse Output Control</strong></p>

4. Configure Modbus TCP Slave.
   4.1. Go to the Modbus TCP Slave settings page.
   4.2. Turn on the **Enable** switch to enable the Modbus TCP Slave function. This function allows the Modbus TCP Master to read the I/O status of the IG902.
   4.3. Turn on the **External Access** switch to allow the Modbus TCP Master outside the gateway to read the I/O status of the IG902 (such as SCADA software).
   4.4. Set other parameters based on site requirements.

      <p align="center"><img src="images/img_409a2327.webp" alt="Modbus TCP Slave configuration"></p>
      <p align="center"><strong>Figure 3-46 Modbus TCP Slave Configuration</strong></p>

5. Read the I/O status through Modbus TCP.
   5.1. Use Device Supervisor to read the I/O status. First, add a Modbus TCP controller and set the controller communication parameters based on the Modbus TCP Slave configuration.

      <p align="center"><img src="images/img_7472f4ae.webp" alt="Modbus TCP controller configuration"></p>
      <p align="center"><strong>Figure 3-47 Modbus TCP Controller Configuration</strong></p>

   5.2. Configure the data to be collected according to the Modbus mapping table. For example, to read **DI0 Counter Value**:

      <p align="center"><img src="images/img_6b53f01b.png" alt="Data collection configuration step 1"></p>
      <p align="center"><strong>Figure 3-48 Data Collection Configuration (Step 1)</strong></p>

      <p align="center"><img src="images/img_45444eb4.webp" alt="Data collection configuration step 2"></p>
      <p align="center"><strong>Figure 3-49 Data Collection Configuration (Step 2)</strong></p>

   5.3. After the configuration is completed, the **DI0 Counter Value** can be obtained.

      <p align="center"><img src="images/img_f3986c36.webp" alt="DI0 Counter Value result"></p>
      <p align="center"><strong>Figure 3-50 DI0 Counter Value Reading Result</strong></p>

**Verification Method**:
1. Verify that the I/O configuration page reflects the configured modes and parameters.
2. For pulse counting, verify that the counter increments when input pulses are applied.
3. For digital output, verify that the output state changes according to the configured value.
4. For Modbus TCP, verify that the Modbus TCP Master can successfully read the I/O status registers.

**Common Issues**:
- Modbus TCP Master cannot read I/O status: Verify that the Modbus TCP Slave function is enabled and the communication parameters (IP address, port, unit ID) match between the master and slave.
- External Modbus TCP Master cannot access I/O status: Verify that the **External Access** switch is turned on.
- Pulse counting does not increment: Verify that the DI channel is set to pulse counting mode and the **Start** button has been clicked.



# Chapter 4 Feature Descriptions and Parameter Reference



## 4.1 Overview

The **Overview** page displays the IG902 running status, including network connection status, system information, and data usage. After logging in to the IG902 web interface, the **Overview** page appears by default. The **Overview** menu can also be clicked to display this page.

This page contains the following information sections:

** Network Connection Status**

The Network Connection Status area shows the IG902 network connection status and network configuration.

- External network status: Clicking **Set UP** navigates to the Static Routing page (see 4.4.2 Static Routing).
- Network status of GE 0/1: Clicking **Set UP** navigates to the Ethernet page (see 4.2.2 Ethernet).
- Network status of GE 0/2: Clicking **Set UP** navigates to the Ethernet page (see 4.2.2 Ethernet).

<p align="center"><img src="images/img_cb6f087a.webp" alt="Network Connection Status"></p>

<p align="center"><strong>Figure 4-1 Network Connection Status</strong></p>

**Edge Computing**

The Edge Computing area shows the status of Python edge computing.

<p align="center"><img src="images/img_fa01ebeb.png" alt="Edge Computing Status"></p>

<p align="center"><strong>Figure 4-2 Edge Computing Status</strong></p>

**Data Usage Monitoring**

The Data Usage Monitoring area shows the data traffic usage in the last 24 hours. One data record is produced every hour.

<p align="center"><img src="images/img_6771fc24.webp" alt="Data Usage Monitoring"></p>

<p align="center"><strong>Figure 4-3 Data Usage Monitoring</strong></p>

**CPU Load**

The CPU Load area shows the CPU usage in the last 1 minute, 5 minutes, and 15 minutes.

<p align="center"><img src="images/img_ae357be0.webp" alt="CPU Load"></p>

<p align="center"><strong>Figure 4-4 CPU Load</strong></p>

**Memory**

The Memory area shows the current memory usage.

<p align="center"><img src="images/img_97374bd6.png" alt="Memory Usage"></p>

<p align="center"><strong>Figure 4-5 Memory Usage</strong></p>

**System Information**

The System Information area displays device system information. The Edit icon can be clicked to change the name of the IG902.

<p align="center"><img src="images/img_b6092178.png" alt="System Information"></p>

<p align="center"><strong>Figure 4-6 System Information</strong></p>


## 4.2 Network

### 4.2.1 Network Interfaces

#### 4.2.1.1 Cellular

The **Cellular** page displays the configuration and status of the IG902 dial-up interface. The dial-up interface parameters can be configured to connect the IG902 to a cellular network, or details about the dial-up interface can be viewed on this page.

**Configuration steps:**

1. Navigate to **Network > Network Interfaces > Cellular** to display the **Cellular** page.
2. Select **Enable Cellular**.
3. Set the parameters (default settings are recommended). For details about these parameters, see the cellular network parameter description below.
4. Click **Submit** to complete the configuration of the dial-up interface.

The cellular network parameters are described as follows:

- **Enable Cellular**: enables or disables the cellular network connection.

- **Profile**
  - **Network Type**: specifies the type of the mobile network to which the gateway is connected, which can be GSM or CDMA.
  - **APN**: specifies the access point name (APN) that identifies the service type of a WCDMA/LTE network. A WCDMA/LTE system provides services based on the APN of the connected WCDMA/LTE network. (This parameter does not need to be set for the CDMA2000 series.)
  - **Access Number**: specifies the dial string provided by the network operator. Obtain this dial string from the network operator.
    - If the 3G/LTE data card supports WCDMA or LTE, the default dial string is `*99***1#`.
    - If the 3G data card supports CDMA 2000, the default dial string is `#777`.
  - **Auth Method**
    - **Auto**: selects an authentication method automatically.
    - **PAP**: specifies the Password Authentication Protocol, a simple plain-text authentication method implemented through two-way handshakes.
    - **CHAP**: specifies the Challenge Handshake Authentication Protocol, a security authentication method that verifies message digests through three-way handshakes.
    - **MS-CHAP**: specifies the CHAP standard defined by Microsoft.
    - **MS-CHAPv2**: specifies the upgraded version of MS-CHAP, which requires two-way authentication.
  - **Username**: specifies the user name used for connection to the public data network (PDN). It is provided by the network operator. The default value is `gprs`.
  - **Password**: specifies the password of the PDN user. It is provided by the network operator. The default value is `gprs`.

- **Dual SIM Enable**: enables or disables the dual-SIM card mode.
  - **Main SIM**: specifies the main SIM card used. Options are SIM1, SIM2, Random, and Sequential.
  - **Max Number Of Dial**: specifies the maximum number of dial-up attempts on SIM1. When the number of dial-up failures reaches this number, the gateway switches to SIM2.
  - **Min Connected Time**: specifies the minimum network connection duration after the gateway dials up successfully. Within this duration, the number of dial-up attempts is counted. When the connection duration exceeds the set value, the number of dial-up attempts is reset. When the value is set to 0, this function is disabled.
  - **Backup SIM Timeout**: specifies the timeout period of the backup SIM card used currently. The gateway switches to the main SIM card when the timeout period of the backup SIM card is reached.

- **Network Type**: specifies a network type for the SIM card. Options are Auto, 3G, 4G, and 2G. A specific network type suitable for the gateway and SIM card can be selected, or the auto mode can be chosen, in which the gateway automatically registers to the suitable network.

- **Profile**: specifies the index of the dial-up parameter set.

- **Roaming**: enables the roaming function to allow the gateway to dial up in roaming state or disables the roaming function to prevent the gateway from dialing up in roaming state. When a local SIM card is used, its dial-up capability is not affected whether this option is selected or deselected.

- **PIN code**: specifies the personal identification number of the SIM card. If PIN code is enabled but not set or set incorrectly, the gateway cannot dial up. A valid PIN code enables the gateway to dial up to a network.

- **Static IP**: enables or disables the use of a static IP address. If this option is selected, an IP address must be specified manually. Then, the gateway obtains the specified static IP address every time it dials up to a network.

- **Connection Mode**
  - **Always Online**: indicates that the gateway stays online when it is running properly and will be disconnected and redial up only if the dial-up interface does not transmit any traffic in 30 minutes. This is the default connection mode of the system.
  - **On-demand Dial**
    - **Data Trigger**: indicates that the gateway is offline by default and will dial up automatically when data is sent to the Internet.
  - **Manual Dial**: indicates that the network connection can be established or terminated by clicking **Connect** or **Disconnect** in the **Status** area.

- **Redial Interval**: specifies the period that the gateway waits before dialing up again.

- **ICMP Probes**
  - **ICMP Detection Server**: specifies the IP address or domain name of the remote ICMP server to be probed. (If two ICMP servers are enabled, it is recommended to enter the IP addresses or domain names of both servers here.) The gateway supports two ICMP servers: a primary server and a backup server. After two servers are configured, the gateway probes the primary server first. It probes the secondary server only when the number of probe retries on the primary server reaches the maximum value. If both servers fail to be detected, the gateway dials up again and starts a new round of ICMP probe.
  - **ICMP Detection Interval**: specifies the interval between ICMP probe packets sent from the gateway.
  - **ICMP Detection Timeout**: specifies the timeout period of an ICMP probe. If the gateway does not receive any ICMP Reply packet within this period, it considers that the ICMP probe times out.
  - **ICMP Detection Max Retries**: specifies the maximum number of retries after an ICMP probe failure. (The gateway dials up again when the number of retries reaches this value.)
  - **ICMP Detection Strict**: enables or disables the strict ICMP probe mode. In this mode, the gateway does not send ICMP probe packets when its dial-up interface is transmitting data traffic. It sends ICMP probe packets only when the dial-up interface is idle.

- **Advanced Settings**
  - **Initial Commands**: specifies some AT commands used to check the module status.
  - **RSSI Poll Interval**: specifies the interval at which the gateway checks the signal status after dialing up successfully. For example, the interval is set to 60s. If the antennas are removed after the gateway dials up successfully, the signal strength will remain unchanged in 60s and decrease 60s later. If the interval is set to 0, RSSI polling is disabled.
  - **Dial Timeout**: specifies the dial-up timeout period. If the gateway fails to dial up to a network within the timeout period, the dial-up times out. In this case, the gateway checks the module status and dials up to the network again.
  - **MRU**: specifies the maximum receive unit, which is expressed in bytes.
  - **MTU**: specifies the maximum transmit unit, which is expressed in bytes.
  - **Use Default Asyncmap**: enables or disables the default Asyncmap.
  - **Use Peer DNS**: enables or disables the use of the DNS server assigned in the connected network.
  - **LCP Interval**: specifies the interval at which the gateway checks whether the cellular connection is normal.
  - **LCP Max Retries**: specifies the maximum number of dial-up retries after the link connection is interrupted.
  - **Infinitely Dial Retry**: enables the gateway to retry unlimited times upon a dial-up failure.
  - **Debug**: enables display of more detailed system logs.
  - **Expert Options**: allows command parameters to be set.

#### 4.2.1.2 Ethernet

The **Ethernet** page displays the configuration and status of Ethernet interfaces on the IG902. Ethernet interface parameters can be set, or details about the Ethernet interfaces can be viewed on this page.

**Configuration steps:**

1. Navigate to **Network > Network Interfaces > Ethernet** to display the **Ethernet** page and click the **Gigabitethernet 0/1** tab.
2. Select a network type for interface GE 0/1.
3. Select options or enter values for the parameters. For details about these parameters, see the Ethernet parameter description below.
4. Click **Submit** to complete the configuration of GE 0/1.
5. Navigate to **Network > Network Interfaces > Ethernet** to display the **Ethernet** page and click the **Gigabitethernet 0/2** tab. (By default, GE 0/2 is a bridge interface. To configure this interface, `gigabitethernet 0/2` must be removed from the **Bridge** page first.)
6. Select a network type for interface GE 0/2.
7. Select options or enter values for the parameters. For details about these parameters, see the Ethernet parameter description below.
8. Click **Submit** to complete the configuration of GE 0/2.

The following figure shows the configuration of GE 0/1, with **Network Type** set to **DHCP**.

<p align="center"><img src="images/img_69eac962.png" alt="GE 0/1 DHCP Configuration"></p>

<p align="center"><strong>Figure 4-7 GE 0/1 DHCP Configuration</strong></p>

The following figure shows the configuration of GE 0/1, with **Network Type** set to **Static IP**.

<p align="center"><img src="images/img_7532441b.webp" alt="GE 0/1 Static IP Configuration"></p>

<p align="center"><strong>Figure 4-8 GE 0/1 Static IP Configuration</strong></p>

The following figure shows the configuration of GE 0/2, with **Network Type** set to **Static IP**.

<p align="center"><img src="images/img_f11a9230.webp" alt="GE 0/2 Static IP Configuration"></p>

<p align="center"><strong>Figure 4-9 GE 0/2 Static IP Configuration</strong></p>

The Ethernet parameters are described as follows:

- **Network Type** (Static IP by default)
  - **Static IP**: uses a manually configured IP address, matching subnet mask, and other information for the Ethernet interface.
  - **Dynamic Address (DHCP)**: configures the interface as a DHCP client to obtain an IP address, the matching subnet mask, and other information through DHCP.

- **Static IP mode**
  - **Primary IP**: specifies the IP address of the Ethernet interface. By default, the IP address of GE 0/1 is 192.168.1.1, and the IP address of GE 0/2 is 192.168.2.1.
  - **Netmask**: specifies the subnet mask of the Ethernet interface.
  - **MTU**: specifies the maximum transmit unit, which is expressed in bytes. The default value is 1500.
  - **Speed/Duplex**, including:
    - Auto Negotiation
    - 1000M Full Duplex
    - 1000M Half Duplex
    - 100M Full Duplex
    - 100M Half Duplex
    - 10M Full Duplex
    - 10M Half Duplex
  - **Track L2 State**: enables or disables tracking of L2 interface status. After this feature is enabled, the interface is Down when it is not physically connected and is Up when it is physically connected. After this feature is disabled, the interface state is displayed as UP regardless of whether the interface is physically connected.
  - **Shutdown**: disables the interface.
  - **Description**: specifies the descriptive information that identifies the Ethernet interface.
  - **Secondary IP Setting**: allows up to 10 secondary IP addresses to be set in addition to the primary IP address.

- **DHCP mode**
  - **Description**: specifies the descriptive information that identifies the Ethernet interface.

#### 4.2.1.3 WLAN

The **WLAN** page displays the WLAN configuration and status on the IG902. WLAN parameters can be set, or detailed WLAN status information can be viewed on this page.

**Configuration steps:**

1. Navigate to **Network > Network Interfaces > WLAN** to display the **WLAN** page.
2. Select **Enable Wi-Fi**, and then select options or enter values for the parameters. For details about these parameters, see the WLAN parameter description below.
3. Click **Submit** to complete the WLAN configuration.

The following figure shows the configuration of the gateway as a wireless access point (AP).

<p align="center"><img src="images/img_ab3187d0.webp" alt="WLAN AP Mode Configuration"></p>

<p align="center"><strong>Figure 4-10 WLAN AP Mode Configuration</strong></p>

The following figure shows the configuration of the gateway as a wireless client.

<p align="center"><img src="images/img_970a7eef.png" alt="WLAN Client Mode Configuration"></p>

<p align="center"><strong>Figure 4-11 WLAN Client Mode Configuration</strong></p>

The WLAN parameters are described as follows:

- **Enable Wi-Fi**: enables or disables the Wi-Fi service. After enabling the Wi-Fi service, the basic parameters and security authentication options for the wireless network can be set, so that users can connect to the Internet wirelessly.

- **Station Role**: specifies the working mode of the gateway, which can be client or AP.

- **Client mode**
  - **Default Route**: uses the default route. After this option is selected, a wireless route is added automatically.
  - **Client SSID**: specifies the SSID (Service Set Identifier, can be understood as: the "name" of a WiFi network, used to identify and distinguish different wireless networks) of the network to be connected.
  - **Auth Method**: same as the authentication method used on the network to be connected.
  - **Encrypt Mode**: same as the encryption method used on the network to be connected.
  - **WPA/WPA2 PSK Key**: same as the key used on the network to be connected.
  - **Network Type**: same as the type of the network to be connected.

- **AP mode**
  - **SSID Broadcast**: enables SSID broadcasting to allow wireless clients to discover this SSID or disables SSID broadcasting to hide this SSID. When the SSID is hidden, beacon frames sent from the AP do not contain the SSID. In this case, a wireless client can connect to the AP only after the SSID is manually specified on the client.
  - **AP Isolate**: enables or disables client isolation on the AP. After this feature is enabled, the AP does not forward L2 packets between the clients connected to it.
  - **Bridge**: enables or disables bridging of the radio interface to the bridge interface.
  - **Band**: specifies the frequency band used by the AP. The gateway supports 2.4 GHz and 5 GHz bands.
  - **Radio Type**: specifies the radio type of the AP. The AP supports six radio types: 802.11g/n, 802.11g, 802.11n, 802.11b, 802.11b/g, and 802.11b/g/n.
    - 802.11b: works at the 2.4 GHz band, with the maximum rate of 11 Mbit/s.
    - 802.11g: works at the 2.4 GHz band, with the maximum rate of 54 Mbit/s.
    - 802.11n: works at the 2.4 GHz or 5 GHz band, with the maximum theoretical rate of 300 Mbit/s.
  - **Channel**: specifies a data transmission channel that uses wireless signals as the transmission medium. The AP provides 13 channels with different carrier frequencies.
    - The center frequency of channel 1 is 2.412 GHz.
    - The center frequency of channel 2 is 2.417 GHz.
    - The center frequency of channel 3 is 2.422 GHz.
    - The center frequency of channel 4 is 2.427 GHz.
    - The center frequency of channel 5 is 2.432 GHz.
    - The center frequency of channel 6 is 2.437 GHz.
    - The center frequency of channel 7 is 2.442 GHz.
    - The center frequency of channel 8 is 2.447 GHz.
    - The center frequency of channel 9 is 2.452 GHz.
    - The center frequency of channel 10 is 2.457 GHz.
    - The center frequency of channel 11 is 2.462 GHz.
    - The center frequency of channel 12 is 2.467 GHz.
    - The center frequency of channel 13 is 2.472 GHz.
  - **SSID**: specifies the service set identifier of the AP. The SSID technology allows a WLAN to be divided into multiple sub-networks that require separate identity authentication. Users can connect to a sub-network only after passing the identity authentication of the sub-network. This prevents access from unauthorized users.
  - **Auth Method**: specifies the authentication method used by the AP. The AP supports five authentication methods: open authentication, shared key authentication, WPA-PSK, WPA2-PSK, and WPAPSK/WPA2PSK. The last three authentication methods are implemented by using encrypted data.
  - **Encrypt Mode**: specifies the encryption mode used for authentication. The AP supports TKIP and AES encryption modes.
  - **WPA/WPA2 PSK Key**: specifies the authentication key, which contains 8-63 characters.
  - **Bandwidth**: specifies the channel bandwidth on the working band of the AP. Options are 20MHz and 40MHz.
  - **Stations Limit**: specifies the maximum number of clients supported by the AP (a maximum of 128).
  - **IP Address**: specifies the IP address of the radio interface. (This parameter is unavailable after the bridge interface is enabled.)
  - **Netmask**: specifies the subnet mask of the radio interface. (This parameter is unavailable after the bridge interface is enabled.)

#### 4.2.1.4 Bridge

The bridge interface is a logical, virtual interface on the IG902. The radio interface can be bridged with interface GE 0/2. (If `Station Role` is set to `client` on the **WLAN** page, the radio interface cannot be selected as a bridge member.)

**Configuration steps:**

1. Select members of the bridge interface.
2. Set parameters for the bridge interface. For details about these parameters, see the bridge interface parameter description below.
3. Click **Submit** to save the configuration.

As shown in the following figure, the radio interface is bridged with interface GE 0/2.

<p align="center"><img src="images/img_73aa71a6.webp" alt="Bridge Interface Configuration"></p>

<p align="center"><strong>Figure 4-12 Bridge Interface Configuration</strong></p>

The bridge interface parameters are described as follows:

- **Primary IP**: specifies the primary IP address of the bridge interface.
- **Netmask**: specifies the subnet mask of the bridge interface.
- **Secondary IP Setting**: allows up to 10 secondary IP addresses to be set in addition to the primary IP address.
- **Bridge Member**
  - **dot11radio 1**: specifies the radio interface.
  - **gigabitethernet 0/2**: specifies interface GE 0/2.

#### 4.2.1.5 Loopback

The loopback interface is a logical, virtual interface on the IG902. After the loopback interface is created and configured, its IP address can be pinged or a Telnet connection can be set up to it to test the network connectivity. Loopback interface parameters can be set or viewed on the **Loopback** page.

**Configuration steps:**

1. Navigate to **Network > Network Interfaces > Loopback** to display the **Loopback** page. Loopback interface parameters can be set or viewed on this page.
2. Click the Add icon in the table under **Secondary IP Setting** to add a secondary IP address for the loopback interface. (The default IP address is 127.0.0.1.)
3. Enter the secondary IP address and subnet mask.
4. Click **Submit** to complete the configuration of the loopback interface.

As shown in the following figure, a secondary IP address 127.0.0.2 is set for the loopback interface.

<p align="center"><img src="images/img_5758e76f.webp" alt="Loopback Interface Configuration"></p>

<p align="center"><strong>Figure 4-13 Loopback Interface Configuration</strong></p>

> **Caution**: A maximum of 10 secondary IP addresses can be set for the loopback interface.



### 4.2.2 Network Services

#### 4.2.2.1 DHCP Server

DHCP (Dynamic Host Configuration Protocol, can be understood as: the network's "automatic allocator," automatically assigning IP addresses and other network parameters to connected devices) uses a client/server communication model. The client sends a configuration request to the server, and the server replies with the IP address allocated to the client and other configuration information. In this way, the client IP address and other configuration parameters are assigned dynamically.

To configure a DHCP server, follow these steps:

1. Navigate to **Network > Network Services > DHCP > DHCP Server** to display the **DHCP Server** page.
2. Click the **Add** or **Edit** icon to configure the DHCP server.
3. Set the parameters. For details about these parameters, see the DHCP server parameter description below.
4. Click **OK** to save the configuration, and then click **Submit** to apply the configuration.

<p align="center"><img src="images/img_95e923f4.webp" alt="DHCP Server configuration"></p>

<p align="center"><strong>Figure 4-14 DHCP Server Configuration</strong></p>

The DHCP server parameters are described as follows:

- **Enable DHCP Service**: enables or disables the DHCP service. The DHCP server and DHCP relay features cannot be enabled at the same time.
- **Interface**: specifies the interface on which the DHCP service is enabled. Options include Gigabitethernet 0/1, Gigabitethernet 0/2, Bridge 1, or Dot11radio 1. Interfaces Bridge 1 and Dot11radio 1 are available only on the Wi-Fi-capable IG902.
- **Starting Address**: specifies the start IP address of the IP address pool for address allocation to DHCP clients.
- **Ending Address**: specifies the end IP address of the IP address pool for address allocation to DHCP clients.
- **Lease**: specifies the validity period of allocated IP addresses. The DHCP server reclaims expired IP addresses for reallocation. This field cannot be left blank.
- **Windows Name Server (WINS)**: specifies the IP address of the WINS server.
- **Static IP Setting**: allows binding a fixed IP address to a MAC address.

<p align="center"><img src="images/img_15155a32.webp" alt="Static IP Setting"></p>

<p align="center"><strong>Figure 4-15 Static IP Setting</strong></p>

#### 4.2.2.2 DHCP Relay

A DHCP relay (or DHCP relay agent) can process and forward DHCP information between subnets and physical network segments.

To configure a DHCP relay, follow these steps:

1. Navigate to **Network > Network Services > DHCP > DHCP Relay** to display the **DHCP Relay** page.
2. Enable the DHCP relay feature. The DHCP server must be disabled before this operation.
3. Specify the DHCP server addresses and relay interface. For details about these parameters, see the DHCP relay parameter description below.
4. Click **Submit** to apply the configuration.

<p align="center"><img src="images/img_9a279870.png" alt="DHCP Relay configuration"></p>

<p align="center"><strong>Figure 4-16 DHCP Relay Configuration</strong></p>

The DHCP relay parameters are described as follows:

- **Enable DHCP Relay**: enables or disables the DHCP relay feature. The DHCP relay and DHCP server features cannot be enabled at the same time.
- **DHCP Server**: specifies the IP address of the DHCP server.
- **Relay Interface**: specifies the network interface that serves as the DHCP relay.

#### 4.2.2.3 DNS

DNS (Domain Name System, can be understood as: the internet's "phone book," translating website domain names into IP addresses that computers can recognize) is a distributed database used for TCP/IP applications and provides translation between domain names and IP addresses. DNS allows users to access applications by using easy-to-remember, meaningful domain names, which are then translated into the correct IP addresses by a DNS server on the network.

**DNS Server Configuration**

To configure a DNS server, follow these steps:

1. Navigate to **Network > Network Services > DNS** to display the **DNS** page.
2. Enter the IP address of the DNS server.
3. Click **Submit** to apply the configuration.

<p align="center"><img src="images/img_4ea78e2a.png" alt="DNS server configuration"></p>

<p align="center"><strong>Figure 4-17 DNS Server Configuration</strong></p>

**DNS Relay Service Configuration**

To configure the DNS relay service, follow these steps:

1. Navigate to **Network > Network Services > DNS** to display the **DNS** page.
2. Enable the DNS relay service. The DNS relay service cannot be disabled when the DHCP server feature is enabled.
3. Click the **Add** icon to add a **[domain name <=> IP address] pair**.
4. Enter the domain name or IP address of a host and specify the matching IP address.
5. Click **OK** to save the configuration, and then click **Submit** to apply the configuration.

<p align="center"><img src="images/img_90768db8.png" alt="DNS relay service configuration"></p>

<p align="center"><strong>Figure 4-18 DNS Relay Service Configuration</strong></p>

#### 4.2.2.4 GPS

On the **GPS** page, the GPS service can be enabled or disabled, the IG902 location information can be viewed, and IP forwarding and serial forwarding for GPS can be configured. The IG902 can act as a GPS client or server for IP forwarding.

Navigate to **Network > Network Services > GPS** to display the **GPS** page.

<p align="center"><img src="images/img_a32f4f9a.webp" alt="GPS configuration page"></p>

<p align="center"><strong>Figure 4-19 GPS Configuration Page</strong></p>

To configure GPS forwarding, follow these steps:

1. In the **Configure** area, select **Enable GPS**.
2. Select **Enable** under **GPS IP Forwarding** or **GPS Serial Forwarding**.
3. Configure the parameters. For details about these parameters, see the GPS IP forwarding parameter description and GPS serial forwarding parameter description below. The GPS serial forwarding and DTU features cannot be used at the same time. Therefore, DTU must be disabled before enabling GPS serial forwarding.
4. Click **Submit** to save the configuration.

<p align="center"><img src="images/img_b0afeb23.webp" alt="GPS IP forwarding configuration"></p>

<p align="center"><strong>Figure 4-20 GPS IP Forwarding Configuration</strong></p>

<p align="center"><img src="images/img_a3fe9822.webp" alt="GPS serial forwarding configuration"></p>

<p align="center"><strong>Figure 4-21 GPS Serial Forwarding Configuration</strong></p>

The parameters of GPS IP forwarding are described as follows:

- **Enable**: enables or disables GPS IP forwarding.
- **Type**: specifies the type of GPS IP forwarding.
  - **Client**
    - **Transmit Protocol**: specifies the transmission protocol used. Options are TCP and UDP.
    - **Connection Type**: specifies the type of the transmission connection. Options are Long-Lived and Short-Lived. The setting must be the same as that on the server.
    - **Keepalive Interval**: specifies the interval at which the gateway sends heartbeat packets over the TCP connection established.
    - **Keepalive Retry**: specifies the number of heartbeat packet retransmissions upon a heartbeat timeout. If the heartbeat does not resume after heartbeat packets are retransmitted for the specified number of times, the gateway terminates the TCP connection.
    - **Min Reconnect Interval**: specifies the connection interval at the beginning of TCP connection setup. The interval increases every 30 seconds until it reaches the maximum value.
    - **Max Reconnect Interval**: specifies the maximum retry interval for TCP connection setup.
    - **Source Interface**: specifies the interface of which the IP address is used by the gateway to establish a TCP connection to the server.
    - **Reporting Interval**: specifies the interval at which the gateway reports GPS data.
    - **Include RMC**: specifies whether the GPS data sent from the gateway includes RMC data.
    - **Include GSA**: specifies whether the GPS data sent from the gateway includes GSA data.
    - **Include GGA**: specifies whether the GPS data sent from the gateway includes GGA data.
    - **Include GSV**: specifies whether the GPS data sent from the gateway includes GSV data.
    - **Message Prefix**: specifies the user-defined content in the headers of GPS messages sent from the gateway.
    - **Message Suffix**: specifies the user-defined content at the end of GPS messages sent from the gateway.
  - **Server**
    - **Connection Type**: specifies the type of the transmission connection. Options are Long-Lived and Short-Lived. The connection type must be the same as that on the client.
    - **Keepalive Interval**: specifies the interval at which the gateway sends heartbeat packets over the TCP connection established.
    - **Keepalive Retry**: specifies the number of heartbeat packet retransmissions upon a heartbeat timeout. If the heartbeat does not resume after heartbeat packets are retransmitted for the specified number of times, the gateway terminates the TCP connection.
    - **Local Port**: specifies the service port number used by the gateway when it serves as a TCP server.
    - **Reporting Interval**: specifies the interval at which the gateway reports GPS data.
    - **Include RMC**: specifies whether the GPS data sent from the gateway includes RMC data.
    - **Include GSA**: specifies whether the GPS data sent from the gateway includes GSA data.
    - **Include GGA**: specifies whether the GPS data sent from the gateway includes GGA data.
    - **Include GSV**: specifies whether the GPS data sent from the gateway includes GSV data.
    - **Message Prefix**: specifies the user-defined content in the headers of GPS messages sent from the gateway.
    - **Message Suffix**: specifies the user-defined content at the end of GPS messages sent from the gateway.

Parameters of GPS serial forwarding are described as follows:

- **Enable**: enables or disables GPS serial forwarding.
- **Serial Type**: same as that on the remote end (RS232 or RS485).
- **Baudrate**: same as that on the remote end.
- **Data Bits**: same as that on the remote end.
- **Parity**: same as that on the remote end.
- **Stop Bit**: same as that on the remote end.
- **Software Flow Control**: enables or disables software flow control.
- **Include RMC**: specifies whether the GPS data sent from the gateway includes RMC data.
- **Include GSA**: specifies whether the GPS data sent from the gateway includes GSA data.
- **Include GGA**: specifies whether the GPS data sent from the gateway includes GGA data.
- **Include GSV**: specifies whether the GPS data sent from the gateway includes GSV data.

#### 4.2.2.5 Host List

Information about hosts connected to the IG902 can be viewed on the **Host List** page.

Navigate to **Network > Network Services > Host List** to display the **Host List** page.

<p align="center"><img src="images/img_793491be.png" alt="Host List page"></p>

<p align="center"><strong>Figure 4-22 Host List</strong></p>



### 4.2.3 Routing

#### 4.2.3.1 Routing Status

Navigate to **Network > Routing > Routing Status** to open the **Routing Status** page. This page displays information about static routes configured on the IG902.

<p align="center"><img src="images/img_ecdeec4f.png" alt="Routing Status page"></p>

<p align="center"><strong>Figure 4-23 Routing Status</strong></p>

### 4.2.3.2 Static Routing

Static routes can be configured on the **Static Routing** page. After configuration, packets sent to a specific destination are forwarded through the specified route. (Generally, static routes do not need to be configured.)

The configuration steps are as follows:

1. Navigate to **Network > Routing > Static Routing** to open the **Static Routing** page.
2. Click the **Add** icon to add a static route.
3. Set the parameters. For details about these parameters, see the static routing parameter description below.
4. Click **OK** to save the configuration, and then click **Submit** to apply the configuration.

The following figure shows the configuration of a static route.

<p align="center"><img src="images/img_5522d5ec.webp" alt="Static Routing configuration page"></p>

<p align="center"><strong>Figure 4-24 Static Routing Configuration</strong></p>

Parameters of a static route are described as follows:

| Parameter | Description |
|-----------|-------------|
| Destination | Specifies the destination IP address to which packets are sent. |
| Netmask | Specifies the subnet mask (can be understood as: a "ruler" used to divide network ranges, helping the device determine whether the target IP is within the same local area network) of the destination IP address. |
| Interface | Specifies the interface through which data packets are forwarded to the destination network. |
| Gateway | Specifies the IP address of the next router (can be understood as: the "gate" between networks, through which the device accesses other networks or the Internet) that data packets pass through before reaching the destination IP address. |
| Distance | Specifies the priority of the route. A smaller value indicates a higher priority. |
| Track ID | Specifies the track index or ID. |



### 4.2.4 Firewall

#### 4.2.4.1 ACL

An access control list (ACL) permits or denies specified data flows (such as the data flow from a specified source IP address or account) based on a series of matching rules to filter the data reaching a network interface. A data filtering policy for a network interface can be configured on the **ACL** page.

**Configuration procedure:**

1. Choose **Network > Firewall > ACL** to display the **ACL** page.
2. Click the Add icon under **Access Control Policy** to add an access control policy.
3. Set the parameters. For details about these parameters, see [access control policy parameter description](#access-control-policy-parameter-description).
4. Click the Add or Edit icon under **ACL** to add an access control list on a specified interface.
5. Set the parameters. For details about these parameters, see [access control list parameter description](#access-control-list-parameter-description).
6. Click **OK** to save the configuration, and then click **Submit** to apply the configuration.

The following figure shows the configuration of a standard access control policy.

<p align="center"><img src="images/img_4cbedf30.webp" alt="Standard access control policy configuration"></p>

<p align="center"><strong>Figure 4-25 Standard Access Control Policy Configuration</strong></p>

The following figure shows the configuration of an extended access control policy.

<p align="center"><img src="images/img_accec351.webp" alt="Extended access control policy configuration"></p>

<p align="center"><strong>Figure 4-26 Extended Access Control Policy Configuration</strong></p>

The following figure shows the configuration of an access control list.

<p align="center"><img src="images/img_c1dfb3cb.webp" alt="Access control list configuration"></p>

<p align="center"><strong>Figure 4-27 Access Control List Configuration</strong></p>

**Access Control Policy Parameter Description**

Parameters of a standard access control policy are described as follows:

| Parameter | Description |
|-----------|-------------|
| ID | Specifies the ID of an ACL rule, in the range of 1-99. A smaller value indicates a higher priority of the rule. |
| Sequence Number | Specifies the sequence number of the ACL rule. A smaller value indicates a higher priority of the rule. |
| Action | Permits or denies forwarding of matching packets. |
| Source IP | Specifies the source IP address of packets in the ACL rule. If this field is kept blank, the rule matches packets from all networks. |
| Source Wildcard | Specifies the wildcard mask of the source IP address in the ACL rule. |
| Log | Enables or disables recording of access control logs. |
| Description | Records meanings of access control parameters. |

Parameters of an extended access control policy are described as follows:

| Parameter | Description |
|-----------|-------------|
| ID | Specifies the ID of an ACL rule, in the range of 100-199. A smaller value indicates a higher priority of the rule. |
| Sequence Number | Specifies the sequence number of the ACL rule. A smaller value indicates a higher priority of the rule. |
| Action | Permits or denies forwarding of matching packets. |
| Protocol | Specifies the access control protocol. |
| Source IP | Specifies the source IP address of packets in the ACL rule. If this field is kept blank, the rule matches packets from all networks. |
| Source Wildcard | Specifies the wildcard mask of the source IP address in the ACL rule. |
| Source Port | Specifies the source port number of packets. The value **any** indicates that TCP/UDP packets with any source ports match the rule. This parameter is available only when the TCP or UDP protocol is selected. |
| Destination IP | Specifies the destination IP address of packets in the ACL rule. If this field is kept blank, the rule matches packets destined for all networks. |
| Destination Wildcard | Specifies the wildcard mask of the destination IP address in the ACL rule. |
| Destination Port | Specifies the destination port number of packets. The value **any** indicates that TCP/UDP packets with any destination ports match the rule. This parameter is available only when the TCP or UDP protocol is selected. |
| Established Connection | Specifies the range of TCP packets controlled. If this option is selected, the system controls TCP packets on established connections and does not control those on unestablished connections. If this option is deselected, the system controls TCP packets on both established and unestablished connections. This parameter is available only when the TCP protocol is selected. |
| Fragments | Enables or disables control of fragmented data packets sent from the interface. |
| Log | Enables or disables recording of access control logs. |
| Description | Records meanings of access control parameters. |

**Access Control List Parameter Description**

Parameters of an access control list are described as follows:

| Parameter | Description |
|-----------|-------------|
| Interface | Specifies the name of the interface on which the access control policy is configured. |
| Rule | Specifies the inbound, outbound, and administrative rules. |

#### 4.2.4.2 NAT

Network address translation (NAT) allows multiple hosts in a LAN to connect to the Internet by using one or multiple public IP addresses. This feature maps a few public IP addresses to many private IP addresses to conserve public IP addresses. NAT rules can be viewed and configured on the **NAT** page.

**Configuration procedure:**

1. Choose **Network > Firewall > NAT** to display the **NAT** page.
2. Select an interface from the **Interface** drop-down list.
3. Click the Add icon under **Network Address Translation (NAT) Rules** to add an NAT rule and set parameters for the rule. For details about these parameters, see [NAT rule parameter description](#nat-rule-parameter-description).
4. Click **OK** to save the configuration, and then click **Submit** to apply the configuration.

As shown in the following figure, the NAT rule allows hosts connected to the IG902 to connect to the Internet by using the IP address of interface GE 0/2.

<p align="center"><img src="images/img_a692f450.png" alt="NAT rule configuration"></p>

<p align="center"><strong>Figure 4-28 NAT Rule Configuration</strong></p>

**NAT Rule Parameter Description**

Parameters of the NAT rule are described as follows:

| Parameter | Description |
|-----------|-------------|
| Action | SNAT: uses the source network address translation feature that translates source IP addresses of data packets into another IP address. Generally, this feature is used for data packets sent to the Internet through the router.<br>DNAT: uses the destination network address translation feature that translates destination IP addresses of data packets into another IP address. Generally, this feature is used for data packets sent to the private network through the router.<br>1:1NAT: uses one-to-one IP address translation. |
| Source Network (available when the action is set to SNAT or DNAT) | Inside: translates private IP addresses.<br>Outside: translates public IP addresses. |
| Translation Type | IP to IP<br>IP to INTERFACE<br>IP PORT to IP PORT<br>ACL to INTERFACE<br>ACL to IP |
| Access Control List (unavailable for 1:1 NAT) | Specifies the ACL rule used to match the packets of which the IP addresses are translated. |
| Translated Address (unavailable for 1:1 NAT) | Specifies the IP address or interface translated from the source address. |
| Description | Specifies the description of the NAT rule. |



## 4.3 Edge Computing

### 4.3.1 Python Edge Computing

The **Python Edge Computing** page displays information about the Python secondary development environment on the IG902, as well as the configuration and running status of Python apps on the IG902. The secondary development environment can be used to develop custom Python apps, and set or view app status.

**Configuration of the Python secondary development environment:**

1. Navigate to **Edge Computing > Python Edge Computing** to display the **Python Edge Computing** page.
2. Enable the Python edge computing engine.
3. Install or upgrade the Python SDK (optional).
4. Enable the debugging mode. For details about Python secondary development, refer to [Python Development Quick Start](http://sdk.ig.inhandnetworks.com/en/latest/MobiusPi-Python-QuickStart-EN.html).

**Configuration of a Python app:**

1. Navigate to **Edge Computing > Python Edge Computing** to display the **Python Edge Computing** page.
2. Enable the Python edge computing engine.
3. Install or upgrade the Python SDK (optional).
4. In the **Configure** area, import the app package and select **Enable**. For details about the configuration, refer to the app configuration function description.
5. Click **Submit** to apply the configuration.

The following figure shows the configuration of the Python development environment on the IG902.

<p align="center"><img src="images/img_666fafdc.png" alt="Python development environment configuration"></p>

<p align="center"><strong>Figure 4-29 Python Development Environment Configuration</strong></p>

The following figure shows the app running status (HelloWorld as an example).

<p align="center"><img src="images/img_d095640d.webp" alt="App running status"></p>

<p align="center"><strong>Figure 4-30 App Running Status</strong></p>

The app configuration functions are described as follows:

- App status

  - Start all: starts all the enabled apps.
  - Stop all: stops all the enabled apps.
  - Restart all: restarts all the enabled apps.
  - Download: downloads running logs of a specified app.
  - Delete: deletes all running logs of a specified app.
  - View: displays running logs of a specified app.
  - Stop: stops a specified app.
  - Restart: restarts a specified app.

- App List

  - Enable: enables an app so that it will run automatically after each system reboot.
  - Start Parameters: allows configuration of app start parameters.
  - Export: allows export of an app configuration file.
  - Import: allows import of an app configuration file. After a configuration file is imported and the app is restarted, the app runs with the imported configuration file.
  - Unload: allows unloading of an app.
  - Add: allows addition of an app.

### 4.3.2 Docker Manager

The IG902 supports hosting of Docker images. Docker images can be released on the IG902 to deploy and run self-developed applications quickly.

**Configuration of the Docker environment:**

1. Install the Docker SDK.
2. Enable the Docker manager.
3. Configure Docker images and containers on the Docker management page (Portianer).

The following figure shows the Docker manager enabled.

<p align="center"><img src="images/img_3f14d586.png" alt="Docker manager enabled"></p>

<p align="center"><strong>Figure 4-31 Docker Manager Enabled</strong></p>

Parameters on the Docker management page are described as follows:

- Enable Docker Manager: enables or disables the Docker Manager.
- Docker Version: allows installation or upgrade of a Docker version.
- User Name: specifies the user name used to log in to the Portianer.
- Password: specifies the password used to log in to the Portianer.
- Port: specifies the port number used to access the Portianer. The default port number is 9000.
- Docker Image: allows import of a Docker image.


## 4.4 System Management

### 4.4.1 System Time

To enable the IG902 to cooperate with other devices properly, an accurate system time may need to be configured. The system time is set on the **System Time** page, and the NTP (Network Time Protocol, can be understood as: a protocol used to synchronize clocks between computer systems over a network) protocol can be enabled to implement clock synchronization among all clock-supporting devices on the network. In this way, all devices maintain the same clock to provide applications based on the consistent time.

The system time can be set using the following methods.

**Method 1: Select a time zone.**

1. Navigate to **System > System Time** to display the **System Time** page.
2. Select the time zone where the IG902 is located from the **Time Zone** drop-down list.
3. Click **Apply**.

**Method 2: Set the system time manually.**

1. Navigate to **System > System Time** to display the **System Time** page.
2. Set a specific time in the **Set Time** field.
3. Click **Apply**.

**Method 3: Use the local time of the PC.**

1. Navigate to **System > System Time** to display the **System Time** page.
2. The IG902 can obtain the time of the PC as its local time.
3. Click **Sync** next to the **Device Time** field.

**Method 4: Enable SNTP (Simple Network Time Protocol, can be understood as: a simplified version of NTP for time synchronization) clients.**

1. Navigate to **System > System Time** to display the **System Time** page.
2. Select **Enable SNTP Clients**.
3. Set the parameters. For details about these parameters, see [SNTP Client Parameter Description](#sntp-client-parameter-description).
4. Click **Submit** to apply the configuration.

To enable the NTP server to synchronize time to other devices, follow these steps.

1. Navigate to **System > System Time** to display the **System Time** page.
2. Select **Enable SNTP Server**.
3. Set the parameters. For details about these parameters, see [NTP Server Parameter Description](#ntp-server-parameter-description).
4. Click **Submit** to apply the configuration.

<p align="center"><img src="images/img_b24855d7.png" alt="System Time - Time Zone and Manual Setting"></p>

<p align="center"><strong>Figure 4-32 System Time - Time Zone and Manual Setting</strong></p>

<p align="center"><img src="images/img_47e77155.webp" alt="System Time - SNTP Client Configuration"></p>

<p align="center"><strong>Figure 4-33 System Time - SNTP Client Configuration</strong></p>

<p align="center"><img src="images/img_8509e81b.webp" alt="System Time - NTP Server Configuration"></p>

<p align="center"><strong>Figure 4-34 System Time - NTP Server Configuration</strong></p>

**SNTP Client Parameter Description**

| Parameter | Description |
|-----------|-------------|
| Enable SNTP Clients | Enables or disables SNTP clients. If the cellular interface is selected as the source interface, the SNTP service will not be enabled when the gateway fails to dial up to a network. |
| Update Interval | Specifies the interval at which the SNTP clients synchronize time with the IG902. |
| Source Interface | Specifies the interface through which the IG902 sends SNTP packets. The source interface and source address cannot be used at the same time. |
| Source Address | Specifies the source address of the SNTP packets sent from the IG902. The source interface and source address cannot be used at the same time. |
| SNTP Servers List | |
| Server Address | Specifies the domain name or IP address of an SNTP server. A maximum of 10 servers can be added to the list. If multiple SNTP servers are set, the system polls all the SNTP servers to find an available one. |
| Port | Specifies the SNTP port number used by an SNTP server. |

**NTP Server Parameter Description**

| Parameter | Description |
|-----------|-------------|
| Enable NTP Server | Enables or disables the NTP server feature. |
| Update Interval | Specifies the time synchronization interval. The NTP protocol uses the multi-stratum synchronization model. Generally, stratum-n+1 clocks synchronize with a stratum-n clock source. NTP supports synchronization of up to 16 strata of clocks, namely, stratum 0 to stratum 15. Synchronization cannot be implemented for more than 16 strata of clocks. |
| Source Interface | Specifies the interface through which the IG902 sends NTP packets. The source interface and source address cannot be used at the same time. |
| Source Address | Specifies the source address of the SNTP packets sent from the IG902. The source interface and source address cannot be used at the same time. |
| NTP Servers List | |
| Primary NTP Server | Specifies the primary NTP server from which the IG902 synchronizes time. If multiple primary NTP servers are selected, the IG902 polls all the selected servers to find an available one. |
| Server Address | Specifies the domain name or IP address of an NTP server. A maximum of 10 servers can be added to the list. |

---

### 4.4.2 System Logs

Navigate to **System > Log** to display the **Log** page. This page displays a large amount of information about the network and IG902, such as its running status and changes of configuration. On the **Configure** page, a remote log server can be set. Then, the IG902 will synchronize all system logs to the remote log server. The host used as the remote log server must run a remote log program (for example, `Kiwi Syslog Daemon`).

(Original manuscript does not provide details, to be supplemented)

---

### 4.4.3 Configuration Management

Navigate to **System > Configuration Management** to display the **Configuration Management** page. On this page, configuration parameters can be backed up, parameter settings can be imported, and factory settings of the IG902 can be restored.

**Configuration Management Parameters**

| Parameter | Description |
|-----------|-------------|
| Auto Save | Enables or disables automatic saving of modified configuration in the startup configuration file. |
| Encrypted | Enables or disables password encryption. After this option is selected, all passwords configured on the IG902 web system are displayed in encrypted text. This feature improves the security of passwords. |

**Configuration Files Operations**

| Operation | Description |
|-----------|-------------|
| Import Startup Config | Allows importing a configuration file as the startup configuration of the IG902. The IG902 will load the imported configuration file upon a reboot. The validity and correct order of commands in the imported configuration file must be ensured. The IG902 filters out invalid commands in the imported configuration file, and then saves the valid commands as the startup configuration. The system will execute these commands sequentially after a reboot. If commands in the imported configuration file are not listed in a valid order, the system cannot enter the expected state after a reboot. |
| Export Startup Config | Allows backing up the startup configuration on a host. The startup configuration is the configuration that the IG902 loads after it starts. |
| Export Running Config | Allows backing up the running configuration on a host. The running configuration is the configuration that the IG902 is running. |
| Restore Factory Configuration | Allows restoring the factory settings of the IG902. This operation restores all parameters on the IG902 to the default settings. The factory settings are restored after a reboot of the IG902. |

---

### 4.4.4 Device Manager

The Device Manager developed by InHand Networks allows monitoring the status of IG902 gateways, maintaining on-site devices remotely, configuring and upgrading a batch of IG902 gateways at the same time remotely, and performing other management operations to manage IG902 gateways and on-site devices more conveniently and efficiently. An IG902 can be connected to the Device Manager on the **Device Manager** page to use the functions and services of the platform.

Follow these steps to connect to the Device Manager.

1. Navigate to **System > Device Manager** to display the **Device Manager** page.
2. Select **Enable Device Manager**.
3. Set the parameters. For details about these parameters, see [Device Manager Parameter Description](#device-manager-parameter-description).
4. Click **Submit** to apply the configuration.

The following figure shows the configuration that connects the IG902 to the `iot.inhandnetworks.com` (DM) platform.

<p align="center"><img src="images/img_422a641f.png" alt="Device Manager Configuration"></p>

<p align="center"><strong>Figure 4-35 Device Manager Configuration</strong></p>

**Device Manager Parameter Description**

| Parameter | Description |
|-----------|-------------|
| Enable Device Manager | Enables or disables the DM platform. |
| Server Address | Specifies the server address of the DM platform to be connected. |
| Registered Account | Specifies an account registered on the DM platform. |
| Advanced Settings | |
| Location Type | Specifies the source of the location information. Options are Cellular and GPS. |
| LBS Information Upload | Specifies the interval for reporting LBS (Location Based Service, can be understood as: services that use geographic location data to provide information or functionality) information. The valid value range is 60-86400. |
| Interval | Specifies the interval between heartbeat packets exchanged with the DM platform. The valid value range is 30-86400. |
| Dataflow Upload Interval | Specifies the interval for reporting traffic information. The valid value range is 3600-86400. |

---

### 4.4.5 Firmware Upgrade

The firmware version for the IG902 can be upgraded on the **Firmware Upgrade** page, so that the IG902 can provide new functions or better user experiences.

Follow these steps to upgrade the firmware version.

1. Navigate to **System > Firmware Upgrade** to display the **Firmware Upgrade** page.
2. Click **Select File** to select a firmware file for the IG902.
3. Click **Starting Upgrade** and **OK** to start the firmware upgrade.
4. Wait until the upgrade succeeds, and then click **Reboot** to restart the IG902.

(Original manuscript does not provide details, to be supplemented)

---

### 4.4.6 Access Tools

To facilitate IG902 management and configuration, the IG902 management and access methods can be configured on the **Access Tools** page.

**Configure HTTPS**

1. Navigate to **System > Access Tools** to display the **Access Tools** page.
2. Select **Enable HTTPS** and set the parameters. For details about these parameters, see [HTTPS Parameter Description](#https-parameter-description).
3. Click **Submit** to apply the configuration.

**Configure Telnet**

1. Navigate to **System > Access Tools** to display the **Access Tools** page.
2. Select **Enable TELNET** and set the parameters. For details about these parameters, see [Telnet Parameter Description](#telnet-parameter-description).
3. Click **Submit** to apply the configuration.

**Configure SSH**

1. Navigate to **System > Access Tools** to display the **Access Tools** page.
2. Select **Enable SSH** and set the parameters. For details about these parameters, see [SSH Parameter Description](#ssh-parameter-description).
3. Click **Submit** to apply the configuration.

<p align="center"><img src="images/img_19ffea58.png" alt="Access Tools - HTTPS Configuration"></p>

<p align="center"><strong>Figure 4-36 Access Tools - HTTPS Configuration</strong></p>

<p align="center"><img src="images/img_cb59d886.png" alt="Access Tools - Telnet Configuration"></p>

<p align="center"><strong>Figure 4-37 Access Tools - Telnet Configuration</strong></p>

<p align="center"><img src="images/img_36635663.webp" alt="Access Tools - SSH Configuration"></p>

<p align="center"><strong>Figure 4-38 Access Tools - SSH Configuration</strong></p>

**HTTPS Parameter Description**

| Parameter | Description |
|-----------|-------------|
| Listen IP Address | Specifies the listening IP address. Options include Any, 127.0.0.1, and other IP addresses. |
| Port | Specifies the listening port number of HTTPS. |
| Web Login Timeout | Specifies the timeout period of web page login. The valid value range is 0-3600. |
| Remote Control | Enables or disables remote access to the IG902 through HTTPS. If no remote control network is specified, the IG902 can be remotely controlled through any network. |

**Telnet Parameter Description**

| Parameter | Description |
|-----------|-------------|
| Listen IP Address | Specifies the listening IP address. Options include Any, 127.0.0.1, and other IP addresses. |
| Port | Specifies the listening port number of Telnet. |
| Remote Control | Enables or disables remote access to the IG902 through Telnet. If no remote control network is specified, the IG902 can be remotely controlled through any network. |

**SSH Parameter Description**

| Parameter | Description |
|-----------|-------------|
| Listen IP Address | Specifies the listening IP address. Options include Any, 127.0.0.1, and other IP addresses. |
| Port | Specifies the listening port number of SSH. |
| Timeout | Specifies the SSH timeout period. The valid value range is 0-120. |
| Key Mode | Fixed as RSA. |
| Key Length | Specifies the length of the key used. Options are 512, 1024, 2048, and 4096. |
| Remote Control | Enables or disables remote access to the IG902 through SSH. If no remote control network is specified, the IG902 can be remotely controlled through any network. |

---

### 4.4.7 User Management

On the **User Management** page, user accounts can be added and the password and access rights of each account can be managed. These accounts allow multiple users to access and manage the IG902.

Follow these steps to add a user.

1. Navigate to **System > User Management** to display the **User Management** page.
2. Click the **Add** icon to add a user.
3. Set the parameters.
4. Click **OK** to save the configuration.

(Original manuscript does not provide details, to be supplemented)

---

### 4.4.8 Reboot

Navigate to **System > Reboot** to display the **Reboot** page, and then reboot the IG902 or set a scheduled reboot plan for it. The following figure shows the IG902 configured to reboot at 0:00 every day.

<p align="center"><img src="images/img_70e32b55.webp" alt="Reboot Configuration"></p>

<p align="center"><strong>Figure 4-39 Reboot Configuration</strong></p>

(Original manuscript does not provide details, to be supplemented)

---

### 4.4.9 Network Tools

Navigate to **System > Network Tools** to display the **Network Tools** page. Network problems of the IG902 can be diagnosed on this page. Extension options can be entered in the **Expert Options** area. For example, expert option `-t` for the ping tool enables the IG902 to ping a specified host continuously until the ping is stopped.

**Ping Tool**

The ping tool can be used to check whether a network is reachable.

<p align="center"><img src="images/img_e6fac575.png" alt="Network Tools - Ping Test Configuration"></p>

<p align="center"><strong>Figure 4-40 Network Tools - Ping Test Configuration</strong></p>

**Traceroute Tool**

The traceroute tool can be used to determine the route used to transmit IP datagrams to a destination.

<p align="center"><img src="images/img_af3af2c3.png" alt="Network Tools - Traceroute Test Configuration"></p>

<p align="center"><strong>Figure 4-41 Network Tools - Traceroute Test Configuration</strong></p>

**Tcpdump Tool**

The Tcpdump tool can be used to capture packets transmitted on a specified interface.

<p align="center"><img src="images/img_fe687a2b.png" alt="Network Tools - Tcpdump Configuration"></p>

<p align="center"><strong>Figure 4-42 Network Tools - Tcpdump Configuration</strong></p>

(Original manuscript does not provide details, to be supplemented)

---

### 4.4.10 3rd Party Notification

Navigate to **System > 3rd Party Notification** to display the **3rd Party Notification** page. The statement about the third-party software used for the IG902 can be viewed on this page.

(Original manuscript does not provide details, to be supplemented)



## 4.5 Navigation Bar Operations

### 4.5.1 Returning to the Homepage

Click the InGateway logo in the upper left corner of any web page of the IG902 to return to the **Overview** page.

<p align="center"><img src="images/img_b782794a.webp" alt="InGateway logo for returning to homepage"></p>

<p align="center"><strong>Figure 4-43 InGateway Logo</strong></p>

### 4.5.2 Logging Out

To log out from the IG902, click the user name in the upper right corner.

<p align="center"><img src="images/img_b45de36d.webp" alt="User name for logging out"></p>

<p align="center"><strong>Figure 4-44 User Name Dropdown</strong></p>

### 4.5.3 Changing the Language

Click the globe icon in the upper right corner to change the language of web pages. The IG902 supports simplified Chinese and English.

<p align="center"><img src="images/img_319b3f0f.webp" alt="Globe icon for changing language"></p>

<p align="center"><strong>Figure 4-45 Language Selection Icon</strong></p>



## 4.6 Advanced Functions

### 4.6.1 Administration

#### 4.6.1.1 System Status

The System Status page displays the current operating status of the gateway, including system information and network information.

**System Information** includes the firmware version, MAC address, system time, and start time of the gateway.

**Network Information** displays the status of network interfaces. In the Network Information area, click **Settings** next to Cellular1, Gigabitethernet 0/1, Gigabitethernet 0/2, or Bridge 1 to enter the corresponding interface configuration page.

The language of the web pages and the host name of the gateway can also be configured on this page.

(Original manuscript does not provide details, to be supplemented)

#### 4.6.1.2 AAA

AAA (Authentication, Authorization, and Accounting, can be understood as: a unified security framework that controls who can access the device, what services they can use, and records their resource usage) is a method to determine who can access a server and what services they can use on the server. It is a structure used to configure three independent security functions in the same way. This structure provides the following service modules:

- **Authentication**: verifies whether a user has the right to access the network.
- **Authorization**: authorizes the user to use certain services.
- **Accounting**: records the usage of network resources by the user.

> **Note**: When RADIUS, TACACS+, and local modes are all configured, they are used following the preference order of 1 > 2 > 3.

**RADIUS**

The RADIUS (Remote Authentication Dial-In User Service, can be understood as: a centralized user authentication protocol that verifies user identity before granting network access) protocol uses the client/server (C/S) model. A network access server (NAS) (can be understood as: a device that acts as a gateway between users and the network, forwarding authentication requests to a central server) is a RADIUS client that transmits user authentication information to a specified RADIUS server and processes the response packets received from the RADIUS server. The RADIUS server receives users' access requests, authenticates their identities, and sends the required configuration information for users to the client. All data transmitted between the server and client is verified using a shared key. The client and server encrypt user passwords before transmitting them to each other, ensuring the security of passwords. The RADIUS service uses UDP as the transmission protocol and is often used in network environments that require high security and allow remote access.

The RADIUS parameters are described as follows:

| Parameter | Description |
|-----------|-------------|
| Server | Specifies the domain name or IP address of a RADIUS server. A maximum of 10 RADIUS servers can be set. |
| Port | Specifies the service port number of the RADIUS server. |
| Key | Specifies the authentication key to be verified before a connection can be established to the RADIUS server. A client can establish a connection to the RADIUS server only if its authentication key is the same as that set on the RADIUS server. |
| Source Interface | Specifies the source interface of RADIUS packets. |

**TACACS+**

The Terminal Access Controller Access Control System Plus (TACACS+) protocol is a security protocol that enhances functions of the TACACS protocol. This protocol provides functions similarly to RADIUS and uses the client/server model for communication between the NAS and TACACS+ server. TACACS+ supports independent authentication, authorization, and accounting.

The TACACS+ parameters are described as follows:

| Parameter | Description |
|-----------|-------------|
| Server | Specifies the domain name or IP address of a TACACS+ server. A maximum of 10 TACACS+ servers can be set. |
| Port | Specifies the service port number of the TACACS+ server. |
| Key | Specifies the authentication key to be verified before a connection can be established to the TACACS+ server. A client can establish a connection to the TACACS+ server only if its authentication key is the same as that set on the TACACS+ server. |

**LDAP**

The Lightweight Directory Access Protocol (LDAP) is based on the X.500 standard but is much simpler and is customizable. Unlike X.500, LDAP supports TCP/IP. In simple words, LDAP provides centralized management of user access, authentication, and authorization. This protocol is easy to customize and supports centralized management of users and user groups, centralized information storage, setting of security and access control policies, security delegation reading, change of user rights, and other related functions.

The LDAP parameters are described as follows:

| Parameter | Description |
|-----------|-------------|
| Name | Specifies the name of a user-defined server list. |
| Server | Specifies the domain name or IP address of an LDAP server. A maximum of 10 LDAP servers can be set. |
| Port | Specifies the port number of the LDAP server. |
| Base DN | Specifies the top of the LDAP directory tree. |
| Username | Specifies the user name used to access the LDAP server. |
| Password | Specifies the password used to access the LDAP server. |
| Security | Specifies the encryption mode. Three options are available: None, SSL, and StartTLS. |
| Verify Peer | Enables or disables peer authentication. |

** AAA Settings**

The IG902 supports the following authentication methods:

| Method | Description |
|--------|-------------|
| Non-authentication (none) | Users are fully trusted, and their identities are not verified. Generally, this method is not used. |
| Local authentication (local) | User information is configured on an NAS. Local authentication is fast and reduces the operation cost, but the amount of user information stored is limited by the hardware capacity. |
| Remote authentication (LDAP) | User information is configured on an authentication server. Remote authentication can be implemented by using the RADIUS, TACACS+, or LDAP. |

The IG902 supports the following authorization methods:

| Method | Description |
|--------|-------------|
| Non-authorization (none) | Authorization is not performed for users. |
| Local authorization (local) | Users are authorized based on the attributes of local accounts configured on the NAS. |
| TACACS+ authorization | Users are authorized by a TACACS+ server. |
| Authorization after RADIUS authentication | Authentication and authorization are bound together, and RADIUS authentication cannot be performed separately. |
| LDAP authorization | Users are authorized by an LDAP server. |

> **Caution**: Authentication method 1 must be consistent with authorization method 1. Authentication method 2 must be consistent with authorization method 2. Authentication method 3 must be consistent with authorization method 3.

#### 4.6.1.3 Alarm

The alarm function allows discovery of exceptions on the gateway in real time, so that the exceptions can be fixed quickly. When an exception occurs, the gateway raises an alarm. Types of exceptions defined in the system can be selected, and an appropriate alarm reporting way can be chosen to obtain exception information. All alarms are recorded in alarm logs to facilitate troubleshooting.

Alarms are classified into system alarms and port alarms:

- **System alarms**: raised upon system or environment exceptions, including hot start, cold start, and memory shortage alarms.
- **Port alarms**: raised upon exceptions on network interfaces, including LINK-UP and LINK-DOWN alarms.

Alarms have the following states:

| State | Description |
|-------|-------------|
| Raise | Indicates that an alarm has been generated but not been confirmed. |
| Confirm | Indicates that an alarm cannot be solved currently. |
| All | Indicates all alarms generated. |

Alarms are classified into the following levels:

| Level | Description |
|-------|-------------|
| EMERG | The gateway undergoes a serious error that may cause a system reboot. |
| CRIT | The gateway undergoes an unrecoverable error. |
| WARN | The gateway undergoes an error that affects system functionality. |
| NOTICE | The gateway undergoes an error that affects system performance. |
| INFO | A normal event has occurred. |

On the **Alarm** page, the following operations can be performed:

- Click the **Status** tab to view all alarms generated in the system since power-on.
- Click the **Alarm Input** tab to select the types of alarms to monitor.
- Click the **Alarm Output** tab to set the alarm notification method. By default, alarms are recorded in logs. After alarm output is configured, the system reports generated alarms by sending notification emails from the specified source email address to the specified destination email address. Generally, this function is not used.
- Click the **Alarm Map** tab to map a specified alarm type to one or multiple alarm notification methods. Two alarm mapping modes are supported: CLI (console interface) and email. To use the email mapping mode, enable email notification and specify related email addresses on the **Alarm Output** tab page.

(Original manuscript does not provide details, to be supplemented)



### 4.6.2 Link Backup

Backup connections are often used between devices in a network environment to improve the network robustness and stability. These backup connections are also called backup links or redundant links.

#### 4.6.2.1 SLA

InHand SLA (Service Level Agreement, can be understood as: a network performance monitoring mechanism that uses probe packets to detect link quality and availability) is implemented in the following way:

1. Object tracking: This module traces the reachability of a specified object.
2. SLA probe: The object tracking module uses the InHand SLA function to send different types of probes to the specified object.
3. Policy-based routing using a route mapping table: This module associates tracking results with routing processes.
4. Static routing and tracking options.

Follow these steps to configure InHand SLA:

1. Define one or multiple SLA entries (probes).
2. Define one or multiple tracked objects to track the status of the SLA entries.
3. Specify the action taken for the tracked object.

The SLA parameters are described as follows:

| Parameter | Description |
|-----------|-------------|
| Index | Specifies the index or ID of an SLA entry, which can be manually set or automatically generated. A maximum of 10 SLA entries can be added. |
| Type | Specifies the type of an SLA entry. The value defaults to icmp-echo and cannot be changed. ICMP-Echo datagrams are used to check whether a host address is alive. The gateway sends an ICMP-Echo (Type 8) datagram to the destination host. If the gateway receives an ICMP-Echo-Reply (Type 0) datagram from the host, it considers the host alive. |
| Destination Address | Specifies the IP address to which the probe is sent. |
| Data size | Specifies the user-defined size of data. The valid value range is 0-1000. |
| Interval (s) | Specifies the interval at which the gateway sends ICMP probes. The valid value range is 1-608400. |
| Timeout (ms) | Specifies the timeout period of an ICMP probe. If the gateway does not receive the reply to an ICMP probe within the timeout period, it considers that the probe fails and sends another probe. The valid value range is 1-300000. |
| Consecutive | Specifies the number of probe failures for determining a link failure. If the gateway does not receive any reply after sending the specified number of probes, the SLA probe fails and the SLA state changes to DOWN. The valid value range is 1-1000. |
| Life | Defaults to forever (always effective after configured) and cannot be changed. |

#### 4.6.2.2 Track Module

The track module implements the association function together with application modules and monitoring modules. Located between application and monitoring modules, the track module shields the difference in monitoring modules and provides the same interface for application modules.

Parameters of the track module are described as follows:

| Parameter | Description |
|-----------|-------------|
| Index | Specifies the index or ID of a tracked object, which can be manually set or automatically generated. A maximum of 10 tracked objects can be added. |
| Type | Specifies the type of the tracked object. Options are sla and interface. |
| SLA ID | Specifies the index or ID of an existing SLA entry. This parameter is unavailable when the track type is set to interface. |
| Interface | Specifies the tracked interface. This parameter is unavailable when the track type is set to sla. |
| Negative Delay | Specifies the amount of time before the tracked object is displayed as abnormal after the interface or SLA state changes to DOWN. The value 0 indicates that the abnormal state is displayed immediately. The unit of the value is second. |
| Positive Delay | Specifies the amount of time before the tracked object switches to the normal state after fault recovery. The value 0 indicates that the tracked object switches to the normal state immediately. |

#### 4.6.2.3 VRRP

The Virtual Router Redundancy Protocol (VRRP, can be understood as: a protocol that allows multiple physical routers to work together as one virtual router, ensuring gateway redundancy and failover) enables multiple routers on a LAN to function as one virtual router. A router can be virtualized into multiple virtual routers based on IP addresses of VLAN interfaces on different network segments. Each virtual router is identified by an ID. A router can be virtualized into up to 255 virtual routers.

The interface tracking capability of VRRP extends the backup function, providing backup for not only interfaces on other routers but also other interfaces on the local router (such as an upstream interface) when these interfaces are faulty. When an upstream interface is in Down or Removed state, the local router lowers its own priority to enable another router with a higher priority in the VRRP group to become the gateway for traffic forwarding.

The VRRP parameters are described as follows:

| Parameter | Description |
|-----------|-------------|
| Enable | Enables or disables VRRP. |
| Virtual Router ID | Specifies the ID of a virtual router. The valid value range is 1-255. |
| Interface | Specifies the interface on which the virtual router is configured. |
| Virtual IP | Specifies the IP address of the virtual router. |
| Priority | Specifies the priority of the local router in the VRRP group. The value ranges from 0 to 255 (a larger value indicates a higher priority). A router with a higher priority is more likely to become the gateway. |
| Advertisement Interval | Specifies the interval for heartbeat packet exchange between routers in the VRRP group. |
| Preemption Mode | Enables the router to send VRRP Advertisement packets immediately when it finds its priority higher than the current gateway. As a result, a new round of gateway election is triggered, and the router replaces the previous gateway. Correspondingly, the previous gateway becomes a backup router. |
| Track ID | Specifies the index or ID of an existing tracked object. |

#### 4.6.2.4 Interface Backup

Interface backup refers to master-backup bindings between interfaces on the same device. When the main interface in a binding cannot transmit service traffic properly due to an interface failure or insufficient bandwidth, traffic can be quickly switched to the backup interface. The backup interface then transmits all traffic or shares a part of traffic. This feature improves the reliability of data communication between devices.

The interface backup parameters are described as follows:

| Parameter | Description |
|-----------|-------------|
| Main Interface | Specifies the interface currently used for traffic forwarding. |
| Backup Interface | Specifies the interface waiting for traffic switching. |
| Startup Delay | Specifies the amount of time before an interface probe is triggered. The valid value range is 0-300. |
| Up Delay | Specifies the amount of time before the main interface turns Up when the probe state changes from failed to successful. The value 0 indicates that the main interface turns Up immediately. The valid value range is 0-180. |
| Down Delay | Specifies the amount of time before the main interface turns Down when the probe state changes from successful to failed. The value 0 indicates that the main interface turns Down immediately. The valid value range is 0-180. |
| Track id | Specifies the index or ID of an existing tracked object. (If interface backup is used with the track module, the main interface does not turn Down when a probe fails.) |



### 4.6.3 Routing

Routing is a process that determines the end-to-end route of packets sent from a source to a destination. Routing works on data packet forwarding devices on Layer 3 of the OSI reference model. A router connects networks by forwarding data packets between them. When the router receives a data packet, it determines the outbound interface and next-hop IP address by searching for the destination IP address of the data packet in its routing table, and then rewrites the link-layer header of the data packet for forwarding. The router dynamically maintains a routing table to record the current network topology and updates routing information based on link information received from other routers on the network.

#### 4.6.3.1 Static Routing

Static routes are manually configured. After a static route to a destination address is configured, packets destined for this address will be forwarded along this route. Generally, static routes do not need to be configured.

The parameters of a static route are described as follows:

- **Destination**: specifies the destination IP address to which packets are sent.
- **Netmask**: specifies the subnet mask of the destination IP address.
- **Interface**: specifies the interface through which data packets are forwarded to the destination network.
- **Gateway**: specifies the IP address of the next router that data packets pass through before reaching the destination IP address.
- **Distance**: specifies the priority of the route. A smaller value indicates a higher priority.

#### 4.6.3.2 Dynamic Routing

The interior gateway protocol used in an autonomous system (AS) can be the Open Shortest Path First (OSPF) protocol or Routing Information Protocol (RIP).

**RIP**

The RIP (Routing Information Protocol, can be understood as: a distance-vector routing protocol that measures path quality by hop count) is applicable to small-sized networks. It measures the distance to a destination by hop count, which is called metric. The number of hops from a router to a directly connected network is 0, and the number of hops to a network reachable through another router is 1. That is, the hop count increases with the number of intermediate routers. To limit the convergence time, RIP defines a metric range of 0-15. A hop count of 16 or larger is considered infinite, indicating that the destination network or host is unreachable. To improve the routing performance and prevent routing loops, RIP provides the split horizon feature. RIP can also import routing information learned by other routing protocols.

The RIP parameters are described as follows:

- **Enable**: enables or disables RIP.
- **Update Timer**: specifies the interval at which the router sends route updates. The valid value range is 5-2147483647, and the unit is second.
- **Timeout Timer**: specifies the aging time of a route. If the router does not receive any Update packet for a route within the aging time, it sets the metric of this route to 16 in the routing table. The valid value range is 5-2147483647, and the unit is second.
- **Garbage Collection Timer**: specifies the amount of time before a route is removed from the routing table after its metric is set to 16. Within the garbage collection period, RIP sends Update packets for this route with the metric of 16. If the route is not updated when the garbage collection timer expires, the route is permanently removed from the routing table. The valid value range is 5-2147483647.
- **Version**: specifies the version of the RIP protocol. Options are Default, v1, and v2.
- **Network**: specifies the first IP address in a network segment and the matching subnet mask.
- **Advanced Options**
  - **Default-Information Originate**: enables or disables advertisement of default routing information.
  - **Default Metric**: specifies the default cost from the local router to the destination. The valid value range is 1-16. The value 16 indicates that the destination is unreachable.
  - **Redistribute Connected**: enables or disables direct route redistribution to RIP.
    - **Metric**: specifies the metric of the redistributed direct route after direct route redistribution is enabled. The valid value range is 0-16.
  - **Redistribute Static**: enables or disables static route redistribution to RIP.
    - **Metric**: specifies the metric of the redistributed static route after static route redistribution is enabled. The valid value range is 0-16.
  - **Redistribute OSPF**: enables or disables OSPF route redistribution to RIP.
    - **Metric**: specifies the metric of redistributed OSPF routes after OSPF route redistribution is enabled. The valid value range is 0-16.
  - **Distance/Metric Management**
    - **Distance**: specifies the administrative distance of a route learned by RIP.
    - **IP Address**: specifies the destination IP address of the RIP route.
    - **Netmask**: specifies the subnet mask of the RIP route.
    - **ACL Name**: specifies an access control list used for route redistribution.
    - **Metric**: changes the metric of the route sent from or received on an interface.
    - **Policy In/Out**: specifies the direction to which the route filtering policy is applied. Options are In and Out.
      - **In**: applies the access control list to incoming traffic.
      - **Out**: applies the access control list to outgoing traffic.
    - **Interface**: specifies the interface to which the route filtering policy is applied.
    - **ACL Name**: specifies the name of the access control list referenced in the route filtering policy.
  - **Filter Policy**
    - **Policy Type**: specifies the type of the route filtering policy. Options are access-list and prefix-list.
    - **Policy Name**: specifies the name of the prefix list.
    - **Policy In/Out**: specifies the direction to which the route filtering policy is applied. Options are In and Out.
    - **Interface**: specifies the interface to which the route filtering policy is applied.
    - **Filter Out (Permit Default Route-Interface)**: allows only transmission to the default router interface.
  - **Passive Interface**: specifies an interface as the passive interface.
  - **Interface**
    - **Interface**: specifies an interface.
    - **Send Version**: specifies the RIP version of packets sent from the interface. Options are Default, v1, and v2.
    - **Receive Version**: specifies the RIP version of packets accepted on the interface. Options are Default, v1, and v2.
    - **Split Horizon & Poisoned Reverse**: Options are split-horizon and disabled.
    - **Authentication Mode**: specifies the authentication method used on the interface. Options are text and md5.
    - **Key**: specifies the authentication key used for RIPv2 packet exchange.
  - **Neighbor**: specifies the IP address of a RIP neighbor.
- **Network**
  - **IP Address**: specifies the interface's IP address to be advertised by RIP.
  - **Netmask**: specifies the interface's subnet mask to be advertised by RIP.

**OSPF**

The OSPF (Open Shortest Path First, can be understood as: a link-state routing protocol that calculates the shortest path based on network topology) protocol is a link state-based interior gateway protocol developed by the IETF.

The OSPF parameters are described as follows:

- **Enable**: enables or disables OSPF.
- **Router ID**: specifies the ID of the LSA-originating router.
- **Route Advanced Options**
  - **ABR Type**: specifies the type of the area border router. Options are cisco, ibm, standard, and shortcut.
  - **RFC1583 Compatibility**: enables or disables compatibility with RFC1583.
  - **OSPF Opaque-LSA**: enables or disables OSPF Opaque LSAs.
  - **SPF Delay Time**: specifies the delay before OSPF SPF computation. The valid value range is 0-600000, and the unit is millisecond.
  - **SPF Initial-holdtime**: specifies the initial SPF holding time. The valid value range is 0-600000, and the unit is millisecond.
  - **SPF Max-holdtime**: specifies the maximum SPF holding time. The valid value range is 0-600000, and the unit is millisecond.
  - **Reference Bandwidth**: The valid value range is 1-4294967, and the unit is Mbit.
- **Interface**
  - **Interface**: specifies the interface on which the OSPF parameters are configured.
  - **Network**: specifies the type of the OSPF network. Options are Broadcast, NBMA, Point-to-Multipoint, and Point-to-Point.
  - **Hello Interval**: specifies the interval between Hello packets sent from the interface. Two neighboring routers cannot establish a neighbor relationship if they send Hello packets at different intervals. The valid value range is 1-65535.
  - **Dead Interval**: specifies the timeout period of a neighbor. If the router does not receive any Hello packet from a neighbor within this period, it considers the neighbor invalid. Two neighboring routers cannot establish a neighbor relationship if they have different Dead intervals. The valid value range is 1-65535.
  - **Retransmit Interval**: specifies the LSA retransmission interval. After the router advertises an LSA to a neighbor, it waits for the Ack packet from the neighbor. If the router does not receive an Ack packet from the neighbor within the retransmission interval, it retransmits the LSA. The valid value range is 3-65535.
  - **Transmit Delay**: specifies the delay time added to the LSA aging time (Age field) before the LSA is sent. This time is added because it takes some time to transmit OSPF packets on a link. This parameter is especially significant on a low-speed link. The valid value range is 1-65535.
  - **Interface Advanced Options**
    - **Interface**: specifies an interface.
    - **Passive Interface**: allows the interface to receive OSPF packets only and disables it from sending OSPF packets.
    - **Cost**: specifies the cost of OSPF on the interface. By default, the OSPF cost is calculated automatically based on the interface bandwidth.
    - **Priority**: specifies the priority of OSPF on the interface.
    - **Authentication**: specifies the authentication method used in the OSPF area. If simple authentication is selected, a password for simple authentication needs to be set and confirmed. If MD5 authentication is selected, an MD5 key and a password need to be set and confirmed.
    - **Key ID**: specifies the ID of the key for MD5 authentication. This parameter takes effect only for MD5 authentication. The valid value range is 1-255.
    - **Key**: specifies the authentication key used for OSPF packet exchange.
- **Network**
  - **IP Address**: specifies the IP address of the local network.
  - **Netmask**: specifies the subnet mask of the local network address.
  - **Area ID**: specifies the ID of the area where the LSA originating router is located.
- **Area**
  - **Area ID**: specifies the ID of an OSPF area.
  - **Area**: configures the OSPF area as a stub or NSSA area. The backbone area (with the ID of 0.0.0.0) cannot be configured as a stub or NSSA area.
  - **No Summary**: disables the route summarization function that aggregates multiple routes into one broadcast LSA. The result and biggest advantage of route summarization is a smaller routing table.
  - **Authentication**: specifies the authentication method used for OSPF packets. Options are simple, password, and md5.
  - **Area Advanced Options - Area Range**
    - **Area ID**: specifies the ID of the area where the OSPF-enabled interface is located.
    - **IP Address**: specifies the network segment where the interface is located.
    - **Netmask**: specifies the subnet mask of the network segment where the interface is located.
    - **Not Advertise**: disables advertisement of intra-area routing information to other areas.
    - **Cost**: specifies the OSPF cost on the interface. The valid value range is 0-16777215.
  - **Area Advanced Options - Area Filter**
    - **Area ID**: specifies the ID of the OSPF area to which the filtering policy is applied.
    - **Filter Type**: specifies the mode of route filtering. Options are import, export, filter-in, and filter-out.
    - **ACL Name**: specifies the name of the access control list used to filter routes. Only the routes allowed by the access control list can take effect.
  - **Area Advanced Options - Area Virtual Link**
    - **Area ID**: specifies the ID of an OSPF area.
    - **ABR Address**: specifies the interface address that the ABR uses to connect to the area. An ABR (Area Border Router, can be understood as: a router that connects the backbone area with other OSPF areas) is a router that connects multiple areas.
    - **Authentication**: specifies the authentication method used for OSPF packets. Options are simple, password, and md5.
    - **Key ID**: specifies the ID of the key for MD5 authentication. This parameter takes effect only for MD5 authentication. The valid value range is 1-255.
    - **Key**: specifies the authentication key used for OSPF packet exchange.
    - **Hello Interval**: specifies the interval between Hello packets sent from the interface. The valid value range is 1-65535.
    - **Dead Interval**: specifies the timeout period of a neighbor. If the router does not receive any Hello packet from a neighbor within this period, it considers the neighbor invalid. The valid value range is 1-65535.
    - **Retransmit Interval**: specifies the interval at which the router retransmits an SLA after the LSA fails to get a response. The valid value range is 1-65535.
    - **Transmit Delay**: specifies the delay time before LSA transmission. The valid value range is 1-65535.
- **Redistribution**
  - **Redistribution Type**: specifies the type of redistributed routes. Options are connected, static, and rip.
  - **Metric**: specifies the metric of the redistributed route advertised by the router.
  - **Metric Type**: specifies the type of external routes imported to the OSPF routing table.
    - **1**: indicates Type-1 external routes that are highly reliable. For OSPF, cost of a calculated external route is equivalent to the cost of an intra-AS route and is comparable with the cost of an OSPF route. That is, the cost of a Type-1 external route is the sum of the cost from the local router to the corresponding autonomous system boundary router (ASBR) and the cost from the ASBR to the destination address of the external route.
    - **2**: indicates Type-2 external routes that are less reliable. For OSPF, the cost of a route from the ASBR to outside the AS is much larger than the cost of an intra-AS route to the ASBR. Therefore, in OSPF route cost calculation, only the cost from the ASBR to outside the AS is considered. That is, the cost of a Type-2 external route is equal to the cost from the ASBR to the destination IP address of the external route.
  - **Route Map**: This parameter is not configurable currently.
  - **Redistribution Advanced Options**
    - **Always Redistribute Default Route**: enables the router to advertise the redistributed default route after startup.
    - **Redistribute Default Route Metric**: specifies the metric of the redistributed default route advertised by the router.
    - **Redistribute Default Route Metric Type**: 1 or 2.
    - **Default Metric**: specifies the default metric used for route redistribution.
    - **Distance Management**
      - **Area Type**: specifies the route type. Options are inter-area or external.
      - **Distance**: specifies the distance of OSPF routes that can be learned in the area.

**Filtering Route**

The parameters of a route filtering policy are described as follows:

- **Access Control List**
  - **ACL Name**: specifies the name of an access control list.
  - **Action**: specifies the action taken on matching packets. Options are permit and deny.
  - **Any Address**: removes the need to match IP addresses and subnet masks.
  - **IP Address**: specifies a destination IP address.
  - **Netmask**: specifies the subnet mask of the IP address.
- **IP Prefix-list**
  - **Prefix-list Name**: specifies the name of a prefix list.
  - **Sequence Number**: specifies the sequence number of a rule in the prefix list. A prefix list can contain multiple rules.
  - **Action**: specifies the action taken on matching packets. Options are permit and deny.
  - **Any Address**: removes the need to set the IP address, subnet masks, grand equal prefix length, and less equal prefix length.
  - **IP Address**: specifies a destination IP address.
  - **Netmask**: specifies the subnet mask of the IP address.
  - **Grand Equal Prefix Length**: specifies the network portion length in the subnet mask that determines the minimum IP address in the subnet. The valid value range is 0-32.
  - **Less Equal Prefix Length**: specifies the network portion length in the subnet mask that determines the maximum IP address in the subnet. The valid value range is 0-32.

#### 4.6.3.3 Multicast Routing

Multicast routing establishes loop-free transmission paths from a data source to multiple receivers. These paths form a multicast distribution tree. A multicast routing protocol establishes and maintains a multicast routing table, and forwards multicast data packets correctly and efficiently based on the multicast routing table.

** Basic Settings**

On the Basic tab page, a multicast data source can be specified. The basic parameters are described as follows:

- **Enable**: enables or disables multicast routing.
- **Source**: specifies the IP address of the data source.
- **Netmask**: specifies the subnet mask of the source IP address.
- **Interface**: specifies the interface connected to the data source.

**IGMP**

The IGMP (Internet Group Management Protocol, can be understood as: a protocol that allows IP hosts to report their multicast group memberships to neighboring routers) is a multicast protocol in the IP protocol suite, and is used by IP hosts to report their group membership to any immediately neighboring router. This protocol defines the model of multicast communication between hosts on different network segments. Routers on these network segments must support multicast communication. IGMP establishes and maintains multicast group memberships between IP hosts and immediately neighboring multicast routers. It defines how the group memberships of hosts on a network segment are maintained on a multicast router.

The IGMP parameters are described as follows:

- **Upstream Interface**: specifies the interface connected to the upstream network device.
- **Downstream Interface List**
  - **Downstream Interface**: specifies the interface connected to a downstream terminal.
  - **Upstream Interface**: specifies the interface connected to the upstream network device.



### 4.6.4 VPN

VPN (Virtual Private Network, can be understood as: a "dedicated secure tunnel" built over a public network, allowing remote devices to access an internal network securely) is a virtual private communication network established over the Internet depending on an Internet service provider (ISP) and a network service provider (NSP). A virtual network refers to a logical network.

#### 4.6.4.1 IPsec

IPsec (Internet Protocol Security, can be understood as: a network-layer "encryption guard" that provides security and authentication protection for IP communications) is a group of open network security protocols formulated by the IETF, which provide data source authentication, data encryption, data integrity check, and anti-replay on the IP layer to ensure the security of data transmission over the Internet. IPsec lowers the risk of data leakage and interception, ensures data integrity and confidentiality, and protects security of service data transmission.

The IPsec parameters are described as follows:

- IKEv1 Policy

  - ID: specifies the ID of an IKEv1 policy.

  - Encryption: specifies the algorithm used to encrypt plain text. Options are 3DES, DES, AES128, AES192, and AES256.

    - 3DES: uses three 64-bit DES keys to encrypt plain text.
    - DES: uses a 64-bit key to encrypt a 64-bit plain-text block.
    - AES: uses a 128-bit, 192-bit, or 256-bit key to encrypt plain text.

  - Hash: specifies the hash algorithm used in the policy. Options are MD5, SHA1, SHA2-256, SHA2-384, and SHA2-512.

    - MD5: generates a 128-bit message digest for a message of any length.
    - SHA1: generates a 160-bit message digest for a message of a length less than 128 bits.
    - SHA2-256: generates a 256-bit message digest.
    - SHA2-384: generates a 384-bit message digest.
    - SHA2-512: generates a 512-bit message digest.

  - Diffie-Hellman Group: specifies the Diffie-Hellman algorithm, an open key algorithm. Two parties calculate a shared key based on the data exchanged between them, without transmitting the key to each other. To encrypt data sent to each other, the two parties must have a shared key. The essence of Internet Key Exchange (IKE) is that the communication parties never transmit the key over an insecure network. Instead, they exchange a series of data to calculate a shared key. Other parties (such as hackers) cannot calculate the key even if they intercept all the data exchanged for key calculation.

  - Lifetime: specifies the lifetime of the IKE security association (SA). The two parties negotiate another SA to replace the old one before the lifetime expires.

- IKEv2 Policy

  - ID: specifies the ID of an IKEv2 policy.

  - Encryption: specifies the algorithm used to encrypt plain text. Options are 3DES, DES, AES128, AES192, and AES256.

    - 3DES: uses three 64-bit DES keys to encrypt plain text.
    - DES: uses a 64-bit key to encrypt a 64-bit plain-text block.
    - AES: uses a 128-bit, 192-bit, or 256-bit key to encrypt plain text.

  - Integrity: specifies the algorithm used to check data integrity. Options are MD5, SHA1, SHA2-256, SHA2-384, and SHA2-512.

    - MD5: generates a 128-bit message digest for a message of any length.
    - SHA1: generates a 160-bit message digest for a message of a length less than 128 bits.
    - SHA2-256: generates a 256-bit message digest.
    - SHA2-384: generates a 384-bit message digest.
    - SHA2-512: generates a 512-bit message digest.

  - Diffie-Hellman Group: specifies the Diffie-Hellman algorithm, an open key algorithm. Two parties calculate a shared key based on the data exchanged between them, without transmitting the key to each other. To encrypt data sent to each other, the two parties must have a shared key. The essence of IKE is that the communication parties never transmit the key over an insecure network. Instead, they exchange a series of data to calculate a shared key. Other parties (such as hackers) cannot calculate the key even if they intercept all the data exchanged for key calculation.

  - Lifetime: specifies the lifetime of the IKE SA. The two parties negotiate another SA to replace the old one before the lifetime expires.

- IPsec Policy

  - Name: specifies the name of the IPsec policy. This parameter cannot be changed after the IPsec policy is configured successfully.

  - Encapsulation: specifies the encapsulation protocol used for IP packets. The Authentication Header (AH) protocol defines an authentication method to authenticate data sources and ensure data integrity. The Encapsulating Security Payload (ESP) protocol defines encryption and authentication (optional) methods to ensure data reliability.

    - AH: provides data source authentication, data integrity check, and packet anti-replay. The sender uses a hash algorithm to calculate a digest field for an IP packet based on the fixed fields in the IP header and the IP payload. The receiver calculates the digest for the received IP packet and compares it with the digest field carried in the packet to determine whether the packet has been tampered with during transmission on the network.
    - ESP: provides all functions of the AH protocol and encrypts payload of IP packets. The ESP protocol can protect data in IP headers of IP packets.

  - Authentication: specifies the algorithm used for authentication. Options are MD5, SHA1, SHA2-256, SHA2-384, and SHA2-512.

    - MD5: generates a 128-bit message digest for a message of any length.
    - SHA1: generates a 160-bit message digest for a message of a length less than 128 bits.
    - SHA2-256: generates a 256-bit message digest.
    - SHA2-384: generates a 384-bit message digest.
    - SHA2-512: generates a 512-bit message digest.

  - IPsec Mode: specifies the IPsec encapsulation mode.

    - Tunnel Mode: adds an IPsec header (AH or ESP) outside the original IP header and adds a new IP header at the outermost layer. Then, the original IP packet is protected by IPsec as a part of payload. The tunnel mode is generally used between two security gateways. The packets encrypted by one security gateway can only be decrypted by the peer security gateway.
    - Transport Mode: inserts an IPsec header (AH or ESP) between the IP header and upper-layer protocol header. This mode retains the original IP header but changes the IP protocol field to AH or ESP, and calculates a new checksum for the IP header. The transport mode is applicable to communication between two hosts or between a host and a security gateway.

- IPsec Tunnels

  - Basic Parameters

    - Destination Address: specifies the IP address or domain name of the IKE peer. (Set this parameter to 0.0.0.0 when the IG902 acts as a server.)

    - Map Interface: specifies the interface to which the IPsec policy is applied.

    - IKE Version: specifies the version of the IKE protocol. Options are IKEv1 and IKEv2.

    - IKEv1 Policy: specifies a policy ID defined in the IKEv1 policy list.

    - IKEv2 Policy: specifies a policy ID defined in the IKEv2 policy list.

    - IPsec Policy: specifies a policy ID defined in the IPsec policy list.

    - Authentication Type: specifies the authentication method used for the IPsec tunnel. Shared key authentication and digital certificate authentication are supported.

      - Shared Key: specifies the shared key used for authentication.
      - Digital Certificate: specifies the digital certificate used for authentication. A valid certificate needs to be imported on the certificate management page.

    - Negotiation Mode: specifies the mode of IKEv1 negotiation.

      - Main Mode: separates key exchange information from the identity information. This mode protects identity information to enhance the security.
      - Aggressive Mode: does not provide identity authentication but meets requirements of some special network environments. The aggressive mode can be used when the address of the tunnel initiator cannot be obtained in advance or keeps changing, but both parties want to establish an IKE SA by using a pre-shared key.

    - Local Subnet: specifies the source network of the interested flow defined for the IPsec tunnel.

    - Remote Subnet: specifies the destination network of the interested flow defined for the IPsec tunnel.

  - IKE Advance (Phase 1)

    - Local ID: specifies the type of the local device's identifier for IKE negotiation.

      - IP Address: specifies the peer IP address used to establish the IPsec interface.
      - FQDN: specifies the character string used as the identifier of the local device.
      - User FQDN: specifies the fully qualified domain name used as the identifier of the local device.

    - Remote ID: specifies the type of the peer device's identifier for IKE negotiation.

      - IP Address: specifies the interface IP address that the local device uses to complete IKE negotiation and exchange identity information with the peer device.
      - FQDN: specifies the identifier string that the peer devices used for IKE negotiation. The value must be the same as that set on the peer device.
      - User FQDN: specifies the fully qualified domain name used as the identifier of the peer device. The value must be the same as that set on the peer device.

    - IKE Keepalive (DPD): enables or disables dead peer detection (DPD).

      - DPD Timeout: specifies the timeout period of a DPD probe. After the receiving end triggers a DPD probe by sending a DPD request to the peer, it waits for a DPD response. If no DPD response is received from the peer, it deletes the IPsec SA. The valid value range is 10-3600, and the unit is second.
      - DPD Interval: specifies the IPsec neighbor detection interval. After DPD is enabled, the receiving end can trigger a DPD probe if it does not receive any IPsec-encrypted packets from the peer within the DPD interval. In this case, the receiving end sends a DPD request to check whether the IKE peer is available. The valid value range is 10-3600, and the unit is second.

    - XAUTH: specifies the XAUTH user name and password.

  - IPsec Advance (Phase 2)

    - PFS: enables or disables Perfect Forward Secrecy (PFS), a feature that ensures security of other keys when a key is encrypted, because these keys are not derived from one another. The key used in phase-2 IPsec negotiation is derived from the key generated in phase 1. If the phase-1 key for IKE negotiation is intercepted by an attacker, the attacker may collect sufficient information to derive the phase-2 key for IPsec SA negotiation. The PFS feature prevents this problem by performing an additional DH exchange, ensuring security of the phase-2 key.
    - IPsec SA Lifetime: specifies the duration in which the IPsec SA is alive. When the two ends perform IPsec negotiation to establish an SA, the smaller value between the lifetime values set on the local and peer devices takes effect.
    - IPsec SA Idletime: specifies the maximum idle duration of an IPsec SA. If no data is transmitted within this duration after the IPsec SA is established, the IPsec SA becomes invalid. When the current IPsec SA is about to expire, IPsec negotiation is triggered to establish a new SA, so that the new SA is ready before the old SA becomes invalid.

  - Tunnel Advance

    - Tunnel Start Mode: specifies how the IPsec tunnel is initiated.

      - Automatically: indicates that the local device completes IKE negotiation automatically to set up an IPsec tunnel after the IPsec policy is applied. This mode is often used on a client.
      - Respond Only: indicates that local device only receives IPsec requests and does not initiate a connection. This mode is often used on a server.
      - On-demand: indicates that the local device completes IKE negotiation to set up an IPsec tunnel only when detecting IPsec packets on the interface.

    - Local/Remote Send Cert Mode: specifies when to send the certificate. Options are Send cert always, Send cert on request, and Not send cert.

      - Send cert always: Some IPsec services do not send certificate requests but need to receive the certificate from the peer because they do not save the certificate. For these IPsec services, this option must be selected on the peer to enable the IPsec tunnel to be established.
      - Send cert on request: The local device sends the certificate to the peer only when receiving a request from the peer.
      - Not send cert: The local device sends the certificate to the peer regardless of whether the peer sends a request.

    - ICMP Detect

      - ICMP Detection Server: specifies the address of the peer host to be detected.
      - ICMP Detection Local IP: specifies the source address of the traffic to be protected by IPsec.
      - ICMP Detection Interval: specifies the interval between ICMP probe packets sent from the local device.
      - ICMP Detection Timeout: specifies the timeout period of an ICMP probe. If the local device does not receive any ICMP Reply packet within this period, it considers that the ICMP probe times out.
      - ICMP Detection Max Retries: specifies the maximum number of retries after an ICMP probe failure. (The local device restarts the IPsec service when the number of retries reaches this value.)

**IPsec Extension Setting**

The IPsec extension parameters are described as follows:

- Basic Parameters

  - Name: specifies the name of an IPsec profile.

  - IKE Version: specifies the version of the IKE protocol. Options are IKEv1 and IKEv2.

  - IKEv1 Policy: specifies a policy ID defined in the IKEv1 policy list.

  - IKEv2 Policy: specifies a policy ID defined in the IKEv2 policy list.

  - IPsec Policy: specifies a policy ID defined in the IPsec policy list.

  - Authentication Type: specifies the authentication method used for the IPsec tunnel. Shared key authentication and digital certificate authentication are supported.

    - Shared Key: specifies the shared key used for authentication.
    - Digital Certificate: specifies the digital certificate used for authentication. A valid certificate needs to be imported on the certificate management page.

  - Negotiation Mode: specifies the mode of IKEv1 negotiation.

    - Main Mode: separates key exchange information from the identity information. This mode protects identity information to enhance the security.
    - Aggressive Mode: does not provide identity authentication but meets requirements of some special network environments. The aggressive mode can be used when the address of the tunnel initiator cannot be obtained in advance or keeps changing, but both parties want to establish an IKE SA by using a pre-shared key.

- IKE Advance (Phase 1)

  - Local ID: specifies the local ID of the specified type.

  - Remote ID: specifies the peer ID of the specified type.

  - IKE Keepalive (DPD): enables or disables dead peer detection (DPD).

    - DPD Timeout: specifies the timeout period of a DPD probe. After the receiving end triggers a DPD probe by sending a DPD request to the peer, it waits for a DPD response. If no IPsec-encrypted packet is received from the peer, it deletes the ISAKMP profile. The valid value range is 10-3600, and the unit is second.
    - DPD Interval: specifies the IPsec neighbor detection interval. After DPD is enabled, the receiving end can trigger a DPD probe if it does not receive any IPsec-encrypted packets from the peer within the DPD interval. In this case, the receiving end sends a DPD request to check whether the IKE peer is available. The valid value range is 10-3600, and the unit is second.

- IPsec Advance (Phase 2)

  - PFS: enables or disables Perfect Forward Secrecy (PFS), a feature that ensures security of other keys when a key is encrypted, because these keys are not derived from one another. The key used in phase-2 IPsec negotiation is derived from the key generated in phase 1. If the phase-1 key for IKE negotiation is intercepted by an attacker, the attacker may collect sufficient information to derive the phase-2 key for IPsec SA negotiation. The PFS feature prevents this problem by performing an additional DH exchange, ensuring security of the phase-2 key.
  - IPsec SA Lifetime: specifies the duration in which the IPsec SA is alive. When the two ends perform IPsec negotiation to establish an SA, the smaller value between the lifetime values set on the local and peer devices takes effect.

Note:

- Encryption algorithms used for IPsec are AES, 3DES, and DES, listed in descending order of security. The encryption algorithms with higher security are more complex and slower in calculation. Therefore, the DES algorithm can be used to meet ordinary security requirements.
- When the IG902 acts as an IPsec server, set the remote address to 0.0.0.0. Generally, this setting is used when one end uses a public IP address and the other end uses a variable address for dial-up.
- IPsec extensions are often combined with GRE to establish a DMVPN or GRE over IPsec network.


#### 4.6.4.2 GRE

Generic Routing Encapsulation (GRE) is a protocol that encapsulates packets of any network-layer protocol within another network-layer protocol. GRE can be used as a Layer 3 tunneling protocol to provide a transparent transmission channel for VPN data. In essence, GRE is a tunneling technology that provides a channel for transmitting encapsulated data packets. Data packets are encapsulated at one end of the tunnel and decapsulated at the other end.

The GRE parameters are described as follows:

- **Enable**: enables or disables GRE.
- **Index**: specifies a GRE tunnel ID. The valid range is 1-100.
- **Network Type**: specifies the GRE network type.
- **Local Virtual IP**: specifies the virtual IP address of the local device.
- **Peer Virtual IP**: specifies the virtual IP address of the peer device. If the network type is set to subnet, enter a subnet mask in this field.
- **Source Type**: specifies the type of the source address. It can be an IP address or interface name.
- **Local Interface**: specifies the source interface of the GRE tunnel.
- **Local IP**: specifies the source IP address of the GRE tunnel.
- **Peer IP**: specifies the destination address of the GRE tunnel.
- **Key**: specifies the authentication key of the GRE tunnel. The same key must be set on both ends of the tunnel.
- **MTU**: specifies the maximum transmit unit allowed on the GRE tunnel, which is expressed in bytes.
- **NHRP Enable**: enables or disables the Next Hop Resolution Protocol (NHRP). This protocol is used by a source station (host or router) connected to a non-broadcast multiple access (NBMA) subnet to determine the next-hop IP address and NBMA subnet address toward the destination station.
  - **NHS IP Address**: specifies the next-hop server address.
  - **Authentication Key**: specifies the NHRP authentication key.
  - **Hold Time**: The valid value range is 1-65535.
  - **Purge Forbid**: disables or enables transmission of NHRP Purge messages.
- **IPsec Profile**: enables or disables the IPsec profile. It is used together with IPsec extensions.
- **Description**: specifies the description of the GRE tunnel.

**Note:**

- NHRP is applicable only to dynamic multipoint virtual private networks (DMVPNs) and does not need to be enabled for GRE.
- GRE is usually used when both ends use a fixed public IP address.

#### 4.6.4.3 L2TP

The Layer 2 Tunneling Protocol (L2TP) is a virtual private dial-up network (VPDN) tunneling protocol that extends Point-to-Point Protocol (PPP) applications. It is an important VPN technology that enables users to dial up to headquarters networks of their enterprises remotely.

**L2TP Client**

The parameters of an L2TP client are described as follows:

- **L2TP Class**
  - **Name**: specifies the name of an L2TP class.
  - **Authentication**: enables or disables peer authentication before network connection setup.
  - **Hostname**: specifies the host name of the local device. This parameter can be left blank.
  - **Challenge Secret**: specifies the authentication key used on the tunnel. This parameter is required when authentication is enabled. It does not need to be set if authentication is disabled.

- **Pseudowire Class**
  - **Name**: specifies the name of a pseudowire class.
  - **L2TP Class**: specifies the name of an existing L2TP class.
  - **Source Interface**: specifies the source interface of the tunnel.
  - **Data Encapsulation Method**: L2TPV2 or L2TPV3.
  - **Tunnel Management Protocol**: L2TPV2, L2TPV3, or NONE.

- **L2TPv2 Tunnel**
  - **Enable**: enables or disables the L2TP tunnel.
  - **ID**: specifies the ID of the L2TP virtual interface.
  - **L2TP Server**: specifies the IP address or domain name of the L2TP server.
  - **Pseudowire Class**: specifies the name of an existing pseudowire class.
  - **Authentication Type**: specifies the authentication method used on the tunnel. Options are Auto, PAP, and CHAP.
  - **Username**: specifies the valid user name specified for the remote server.
  - **Password**: specifies the valid password specified for the remote server.
  - **Local IP Address**: specifies the IP address of the L2TP virtual interface. This field can be left blank and the IP address allocated by the L2TP server can be used.
  - **Remote IP Address**: specifies the gateway of the L2TP address pool on the server. This field can be left blank.

- **L2TPv3 Tunnel**
  - **Enable**: enables or disables the L2TPv3 tunnel.
  - **ID**: specifies the ID of the L2TPV3 virtual interface.
  - **L2TP Server**: specifies the IP address or domain name of the L2TPv3 server.
  - **Pseudowire Class**: specifies the name of an existing pseudowire class.
  - **Protocol**: specifies the packet encapsulation protocol used on the tunnel. Options are IP and UDP.
  - **Source Port**: specifies the source port used to establish the L2TP tunnel when UDP is used.
  - **Destination Port**: specifies the destination port used to establish the L2TP tunnel when UDP is used.
  - **Xconnect interface**: specifies the L2TPv3 bridge interface.

- **L2TPv3 Session**
  - **Local Session ID**: specifies the local tunnel ID specified in static L2TPv3 tunnel configuration. The valid value range is 1-65535.
  - **Remote Session ID**: specifies the remote tunnel ID specified in static L2TPv3 tunnel configuration. The valid value range is 1-65535.
  - **Local Tunnel ID**: specifies the L2TPv3 tunnel ID set in the **L2TPv3 Tunnel** area.
  - **Local Session IP Address**: specifies the IP address of the static L2TPv3 virtual interface.

**L2TP Server**

Parameters of an L2TP server are described as follows:

- **Enable**: enables or disables the L2TP server.
- **Username**: specifies the user name used to access the L2TP server.
- **Password**: specifies the password used to access the L2TP server.
- **Authentication Type**: specifies the authentication method used by the L2TP server. Options are Auto, PAP, and CHAP.
- **Local IP Address**: specifies the virtual address of the L2TP server interface.
- **Client Start IP Address**: specifies the start IP address of the IP address pool on the L2TP server.
- **Client End IP Address**: specifies the end IP address of the IP address pool on the L2TP server.
- **Link Detection Interval**: specifies the interval at which the L2TP server sends link detection packets after an L2TP tunnel is established. The valid value range is 0-32767, and the unit is second.
- **Max Retries for Link Detection**: specifies the maximum number of L2TP link detection failures. The L2TP establishes a new connection after link detection fails for the maximum number of times. The valid value range is 0-100.
- **Enable MPPE**: enables or disables Microsoft Point-to-Point Encryption (MPPE).
- **Enable Tunnel Authentication**
  - **Challenge Secrets**: specifies the key used for authentication during L2TP tunnel setup. The same key must be set on both ends of the tunnel.
  - **Server Name**: specifies the name of the L2TP server.
  - **Client Name**: specifies the name of the L2TP client connected to the server.
- **Expert Options** (recommended: kept blank): specify the parameters used for L2TP debugging.

#### 4.6.4.4 OpenVPN

In the OpenVPN architecture, when a user accesses a remote virtual address (an address of a virtual NIC, not a real address), the operating system uses the routing mechanism to send the datagrams (TUN mode) or data frames (TAP mode) to the virtual NIC. When the service program receives the data, it processes the data and sends the data to the external network through the socket. When the remote service program receives the data from the external network through its socket, it processes the data and sends the data to the virtual NIC. The application software then receives the data. At this time, a unidirectional transmission process is completed. The reverse transmission process is similar.

**OpenVPN Client**

The parameters of an OpenVPN client are described as follows:

- **Enable**: enables or disables the OpenVPN client.
- **Index**: specifies a tunnel ID.
- **OpenVPN Server**: specifies the IP address or domain name of an OpenVPN server.
- **Port**: specifies the port number used to establish an OpenVPN tunnel.
- **Protocol Type**: specifies the protocol used for data transmission. Options are UDP and TCP.
- **Authentication Type**: Select an authentication type and set parameters for the authentication type.
- **Description**: specifies the description of the OpenVPN tunnel.
- **Advanced Options**
  - **Source Interface**: specifies the interface used to establish the OpenVPN tunnel.
  - **Interface Type**: specifies the type of data sent from the interface.
    - **Tun**: mostly used for IP-based communication.
    - **Tap**: allows complete Ethernet frames to pass through the OpenVPN tunnel and provides support for non-IP protocols.
  - **Network Type**: Options are net30, p2p, and subnet.
    - **net30**: Four IP addresses with a 30-bit mask are selected from the IP address pool. The larger one between the two intermediate IP addresses is used as the IP address of the client's virtual NIC, and the smaller one is used as the peer IP address.
    - **p2p**: An IP address is selected from the IP address pool as the IP address of the client's virtual NIC, and the actual IP address of the virtual NIC is used as the peer IP address.
    - **subnet**: An IP address is selected from the IP address pool as the IP address of the client's virtual NIC, and the subnet mask of the virtual NIC is used as the peer IP address.
  - **Cipher**: specifies the protocol used to encrypt the data transmitted over the OpenVPN tunnel. The setting must be the same on the client and server.
  - **HMAC**: specifies the authentication method used for data transmitted over the OpenVPN tunnel. Data cannot be transmitted if the authentication fails. The setting must be the same on the client and server.
  - **Compression LZO**: specifies the compression format of data transmitted over the OpenVPN tunnel.
  - **Redirect-Gateway**: enables the OpenVPN interface to act as the default gateway for the client, so that all traffic of the client is forwarded through the OpenVPN interface.
  - **Remote Float**: allows the remote device to change its IP address or port.
  - **Link Detection Interval**: specifies the interval for sending link detection packets after an OpenVPN tunnel is established. The valid value range is 10-1800, and the unit is second.
  - **Link Detection Timeout**: specifies the timeout period of OpenVPN link detection. After the number of link detection failures reaches the maximum value, the local device initiates a new L2TP connection. The valid value range is 60-3600.
  - **MTU**: specifies the maximum transmit unit on the OpenVPN interface, which is expressed in bytes.
  - **Enable Debug**: enables or disables debugging logs.
  - **Expert Configuration**: specifies OpenVPN extension parameters.
  - **Import Configuration**: Select the OpenVPN configuration file to import.

**OpenVPN Server**

The parameters of an OpenVPN server are described as follows:

- **Enable**: enables or disables the OpenVPN server.
- **Config Mode**: specifies whether to complete the configuration manually or import a configuration file.
  - **Manual Config**
    - **Authentication Type**: specifies the authentication method used.
    - **Local IP Address**: specifies the virtual IP address of the OpenVPN server interface.
    - **Remote IP Address**: specifies the virtual IP address of the OpenVPN client.
    - **Description**: specifies the description of the OpenVPN tunnel.
    - **Show Advanced Options**: enables or disables display of advanced options.
      - **Source Interface**: specifies the interface used to establish the OpenVPN tunnel.
      - **Interface Type**: specifies the type of data sent from the interface.
        - **Tun**: mostly used for IP-based communication.
        - **Tap**: allows complete Ethernet frames to pass through the OpenVPN tunnel and provides support for non-IP protocols.
      - **Network Type**: Options are net30, p2p, and subnet.
      - **Protocol Type**: specifies the communication protocol used between the client and server. The setting must be the same on the client and server.
      - **Port**: specifies the port number of the OpenVPN service.
      - **Cipher**: specifies the protocol used to encrypt the data transmitted over the OpenVPN tunnel. The setting must be the same on the client and server.
      - **HMAC**: specifies the authentication method used for data transmitted over the OpenVPN tunnel. Data cannot be transmitted if the authentication fails. The setting must be the same on the client and server.
      - **Compression LZO**: specifies the compression format of data transmitted over the OpenVPN tunnel. The setting must be the same as that on the client.
      - **Link Detection Interval**: specifies the interval for sending link detection packets after an OpenVPN tunnel is established. The valid value range is 10-1800, and the unit is second.
      - **Link Detection Timeout**: specifies the timeout period of OpenVPN link detection. If the local device does not receive a response to the link detection packet within this period, link detection fails. The valid value range is 60-3600.
      - **MTU**: specifies the maximum transmit unit on the OpenVPN interface, which is expressed in bytes.
      - **Enable Debug**: enables or disables debugging logs.
      - **Expert Configuration**: specifies OpenVPN extension parameters.
      - **Username/Password**: specifies the user name and password used for server access when password authentication is used.
      - **Local Subnet**: specifies the route from the OpenVPN server to the client. Enter the subnet address on which the client is located.
      - **Client Subnet**: specifies the static route that the OpenVPN server sends to the client.
      - **Client ID**: specifies the attribute ID of the client, generally the certificate name or user name of the client.

#### 4.6.4.5 Certificate Management

The Simple Certificate Enrollment Protocol (SCEP) is a certificate management protocol formulated jointly by Cisco and Verisign. This protocol combines PKCS#7 and PKCS#10 standards, and supports extensive clients and certification authorities (CAs).

The certificate management parameters are described as follows:

- **Enable SCEP**: enables or disables the Simple Certificate Enrollment Protocol.
- **Force to re-enroll**: restarts the certificate enrollment service every time without checking the status of the current certificate.
- **Status**: displays the current certificate enrollment status on the device, which can be Initiation, Enrolling, Re-Enrolling, or Complete.
- **Protect Key**: specifies the key set during certificate enrollment for encryption of the digital certificate. A certificate can be imported or exported only after entering the protection key set during certificate enrollment.
- **Protect Key Confirm**: Enter the protection key again to confirm the key.
- **Strict CA**: sets the ID of a trusted CA. The certificate of a device is enrolled and issued by a trusted CA. Therefore, the ID of a trusted CA must be specified to bind the device to the CA. Then, the device completes certificate application, acquisition, revocation, and query through this CA.
- **Server URL**: specifies the URL of the CA server. A CA server URL must be specified beforehand, so that the device can apply to this server for a certificate through SCEP, for example, `http://100.17.145.158:8080/certsrv/mscep/mscep.dll`.
- **Common Name**: specifies the general name of the certificate required.
- **FQDN**: specifies the fully qualified domain name (FQDN) of the certificate. FQDN is the unique identifier of an entity on a network and is composed of a host name and a domain name. It can be resolved into an IP address. For example, host name `www` and domain name `whatever.com` form an FQDN `www.whatever.com`.
- **Unit 1**: specifies the name of the first organization of the certificate.
- **Unit 2**: specifies the name of the second organization of the certificate.
- **Domain**: specifies the qualified domain name of the certificate.
- **Serial Number**: specifies the serial number of the certificate.
- **Challenge**: specifies the challenge code of the certificate, which is required for certificate revocation (optional).
- **Challenge Confirm**: Enter the challenge code again to confirm the setting.
- **Unstructured address**: specifies the IP address of the certificate.
- **RSA Key Length**: specifies the length of the RSA key. The valid value range is 128-2048, and the unit is bit.
- **Poll Interval**: specifies the interval at which the device queries the current certificate status from the server. The valid value range is 30-3600, and the unit is second.
- **Poll Timeout**: specifies the maximum duration for querying the certificate status. The device considers the certificate application fails when the timeout period expires. The valid value range is 30-86400, and the unit is second.
- **Revocation**: enables or disables certificate revocation.
  - **CRL URL**: specifies the URL of the certificate revocation list (CRL) distribution point.
  - **OCSP URL**: specifies the URL of the Online Certificate Status Protocol (OCSP) server. Generally, it is the same as the URL of the CA server.

**Note:** When using a certificate, ensure that the system time is consistent with the actual time.



### 4.6.5 Industrial Interfaces

The IG902 provides industrial interfaces to connect to terminals with industrial interfaces. The IG902 forwards data from these terminals to the upstream device wirelessly through the gateway, implementing wireless communication between the terminals and the upstream device. Industrial interfaces of the IG902 include serial interfaces and I/O interfaces. Serial interfaces include RS232 and RS485 interfaces. I/O interfaces include digital input, relay output, and analog input interfaces.

#### 4.6.5.1 DTU

DTU (Data Transfer Unit, can be understood as: a "data mover" that converts serial port data into network data for transmission) forwards data from serial port terminals to the upstream device wirelessly through the gateway.

**Serial Port**

To ensure proper communication between the IG902 and terminals, the serial port parameters of the IG902 must be configured based on the serial port settings of the terminals. The serial port parameters are described as follows:

| Parameter | Description |
|-----------|-------------|
| Serial Type | The type of serial port 1 is RS232, and the type of serial port 2 is RS485, which cannot be changed. |
| Baudrate | Specifies the symbol transmission speed measured by the number of symbols transmitted per second. |
| Data Bits | Specifies the number of data bits in communication. |
| Parity | Specifies the error check method used in serial communication. Generally, parity check or no check is performed. |
| Stop Bit | Specifies the last bit of a packet. Typical values are 1, 1.5, and 2. |
| Software Flow Control | Enables or disables software flow control on the serial port. It is a mechanism to block flows when communication fails for some reason. This mechanism enables a data receiving device to instruct the sender to stop sending data when it cannot receive data. |
| Description | Specifies the description of the serial port. |

> **Caution**
>
> - Serial port settings on the IG902 must be the same as those on the terminals connected to it.
> - DTU and GPS serial forwarding cannot be enabled at the same time.

**DTU1**

The parameters of DTU1 are described as follows:

| Parameter | Description |
|-----------|-------------|
| Enable | Enables or disables DTU1. |
| DTU Protocol | Specifies the communication protocol used on DTU1. Options are Transparent, TCP Server, RFC2217 Mode, IEC101 to 104, Modbus Bridge, and DC Protocol. |
| | - Transparent and TCP Server: In transparent transmission mode, the IG902 acts as a client. In TCP server mode, the IG902 acts as a server. |
| | - RFC2217 Mode: removes the need to configure serial port settings. |
| | - IEC101 to 104: provides similar functions to TCP. This mode is applicable to the electric power industry. |
| Transmit Protocol | Specifies the transmission protocol used. Options are TCP and UDP. |
| Connection Type | Specifies the type of the TCP connection. Options are Long-lived and Short-lived. |
| | - Long-lived: indicates that the TCP client retains the TCP connection to the TCP server. |
| | - Short-lived: indicates that the TCP client terminates the TCP connection to the TCP server if no data is transmitted over the connection within the idle timeout period. |
| Keepalive Interval | Specifies the interval at which the TCP client sends TCP keepalive packets after establishing a connection to the TCP server. The valid value range is 1-3600, and the unit is second. |
| Keepalive Retry | Specifies the maximum number of TCP keepalive packet retransmissions. The device retransmits TCP keepalive packets when a TCP keepalive probe times out. If the device does not receive any response after retransmitting TCP keepalive packets for the specified number of times, it initiates a TCP connection again. The valid value range is 1-100. |
| Serial Buffer Frame | Specifies the buffer size on the serial port. The default value is 4K. |
| Packet Size | Specifies the size of each frame sent from the serial port. The serial port starts frame transmission when the frame size reaches this value. The valid value range is 1-1024, and the unit is byte. |
| Force Transmit Timer | Specifies the maximum data transmission interval. If the data transmission interval exceeds the specified value, the device sends the data in multiple frames. The valid value range is 10-65535, and the unit is millisecond. |
| Min Reconnect Interval | Specifies the minimum interval for reestablishing a TCP connection. When a connection fails to be established, the device attempts to reestablish a connection at the specified minimum interval. It retries continuously until the specified maximum reconnection interval is reached. The valid value range is 15-60, and the unit is second. |
| Max Reconnect Interval | Specifies the maximum interval for reestablishing a TCP connection. When the reconnection period reaches the maximum interval, the device attempts to reestablish a connection at this interval (maximum reconnection interval). The valid value range is 60-3600, and the unit is second. |
| Multi-server Policy | Specifies the policy used when multiple servers are available. Options are parallel and polling. |
| | - Parallel: connects to all the servers specified in the destination IP address list concurrently. |
| | - Polling: connects to the servers in the list sequentially. If the first server is connected successfully, the device does not connect to other servers. If the first server cannot be connected, the device tries the other servers in the listed order until a server is connected successfully. |
| Source Interface | Generally, this parameter does not need to be set. |
| Local IP Address | Specifies the IP address of the interface. Set this parameter when IP is selected for the Source Interface field. This field can be left blank. |
| DTU ID | Specifies the DTU ID that the device sends to the server after connecting to the server. This field can be left blank. |
| Enable Debug | Enables or disables debugging logs. |
| Enable Report ID | Enables or disables ID reporting. |
| Keepalive Interval (ID Report) | This parameter needs to be set only when Enable Report ID is selected. The valid value range is 1-65535, and the unit is second. |
| Keepalive Content | This parameter needs to be set only when Enable Report ID is selected. |
| Destination IP Address | |
| - Server Address | Specifies the IP address of a server to be connected. |
| - Server Port | Specifies the port number of the server to be connected. |

> **Note**: A maximum of 10 destination IP addresses can be specified.

**DTU2**

The parameters of DTU2 are the same as those of DTU1.

#### 4.6.5.2  I/O Interfaces

I/O (Input/Output, can be understood as: the "senses and limbs" of the device, used to receive external signal input or control external device output) interfaces include digital input, analog input, and relay output interfaces.

The relay output is ON by default. The relay output status can be set to OFF or ON, or the OFF timer can be set to enable the relay output to turn on automatically.

States of I/O interfaces are as follows:

| Interface | State | Description |
|-----------|-------|-------------|
| Digital Input | Wet contact, voltage +10 V to +30 V | Maps to state 1 |
| Digital Input | Wet contact, voltage 0 V to +3 V | Maps to state 0 |
| Digital Input | Dry contact, terminal connected | State is 1 |
| Digital Input | Dry contact, terminal disconnected | State is 0 |
| Analog Input | - | The analog input status is determined based on the current or voltage obtained from the analog input interface. |
| Relay Output | Default | The default status is ON. The status of a relay output interface can be changed manually. The relay output interface stays ON if its status is not changed in the Action field. |

Action options for Relay Output:

| Action | Description |
|--------|-------------|
| OFF | Turns off relay output. |
| ON | Turns on relay output. |
| OFF -> ON | Specifies the duration after which the relay output interface turns ON. |
| ON -> OFF | Specifies the duration after which the relay output interface turns OFF. |

The I/O interface parameters are described as follows:

**Digital Input**

| Parameter | Description |
|-----------|-------------|
| Mode | Options are Shutdown, Dry Connect, and Wet Connect. |
| | - Shutdown: disables the I/O interface. |
| | - Dry Connect: determines the I/O interface status based on whether the input is on or off. |
| | - Wet Connect: determines the I/O interface status based on the input voltage. |

**Analog Input**

| Parameter | Description |
|-----------|-------------|
| Mode | Options are Shutdown, 0-20mA, 4-20mA, 0-5V, and 0-10V. |
| | - Shutdown: disables the I/O interface. |
| | - 0-20mA: indicates that the range of current is 0-20 mA. |
| | - 4-20mA: indicates that the range of current is 4-20 mA. |
| | - 0-5V: indicates that the range of voltage is 0-5 V. |
| | - 0-10V: indicates that the range of voltage is 0-10 V. |
| Collect Interval | Specifies the interval at which the device reads the voltage or current value on the I/O interface. The value 0 indicates that the device does not read the voltage or current value on the I/O interface. |



### 4.6.6 Wizards

The Wizards page provides simplified configuration of general settings to help users complete basic configuration of the IG902 quickly. The configuration result is not displayed on the Wizards page, but can be viewed on the page of the corresponding feature.

#### 4.6.6.1 New LAN

The parameters on the New LAN page are described as follows:

- Interface: specifies the interface on which the LAN is created.

- Primary IP: specifies the primary IP address of the interface. Set or change the primary IP address as required.

- Netmask: specifies the subnet mask of the interface. (It can be automatically generated.)

- DHCP Server: enables or disables the DHCP (Dynamic Host Configuration Protocol, can be understood as: the "automatic allocator" in the network that automatically assigns IP addresses and other network parameters to connected devices) server feature.

  - Starting Address: specifies the start IP address of the IP address pool for dynamic address allocation.
  - Ending Address: specifies the end IP address of the IP address pool for dynamic address allocation.
  - Lease: specifies the validity period of a dynamically allocated IP address. The valid value range is 30-10080, and the unit is minute.

#### 4.6.6.2 New WAN

The parameters on the New WAN page are described as follows:

- Interface: specifies the interface on which the WAN is created.
- Type: specifies the type of the IP address assigned to the WAN interface. Options are Static IP, Dynamic Address (DHCP), and ADSL Dialup (PPPoE) (Point-to-Point Protocol over Ethernet, can be understood as: the "handshake protocol" for broadband dial-up, used to verify account credentials and establish a network connection).
- Primary IP: specifies the primary IP address of the interface. Set or change the primary IP address as required.
- Netmask: specifies the subnet mask of the interface. (It can be automatically generated.)
- Gateway: specifies the gateway IP address for the interface.
- Primary DNS: specifies the address of the DNS (Domain Name System, can be understood as: the "phone book" of the Internet, translating website domain names into IP addresses that computers can recognize) server.
- NAT: enables or disables NAT (Network Address Translation, can be understood as: the "translator" in the network that converts private IP addresses of internal devices into public IP addresses). After enabled, this feature can translate private IP addresses into public IP addresses.

#### 4.6.6.3 New Cellular

The parameters on the New Cellular page are described as follows:

- Dial-up parameters: Auto or Custom.

  - Auto

  - Custom

    - APN: specifies the access point name.
    - Access Number: specifies the dial string provided by the mobile network operator. (Enter the number provided by the local operator.)
    - Username: specifies the user name provided by the mobile network operator. (Enter the user name provided by the local operator.)
    - Password: specifies the password provided by the mobile network operator. (Enter the password provided by the local operator.)

  - NAT: enables or disables network address translation. After enabled, this feature can translate private IP addresses into public IP addresses.

#### 4.6.6.4 New IPsec Tunnel

The parameters on the New IPsec Tunnel page are described as follows:

- Basic Parameters

  - Tunnel ID: specifies the sequence number of the new tunnel.
  - Map Interface: specifies the source interface of the tunnel.
  - Destination Address: specifies the destination IP address of the tunnel.
  - Negotiation Mode: specifies the tunnel negotiation mode. Options are Main Mode and Aggressive Mode. The main mode is used generally.
  - Local Subnet: specifies the source subnet address of the flow protected by IPsec (Internet Protocol Security, can be understood as: the "encryption bodyguard" at the network layer, providing security and authentication protection for IP communications).
  - Local Netmask: specifies the source subnet mask of the flow protected by IPsec.
  - Remote Subnet: specifies the destination subnet address of the flow protected by IPsec.
  - Remote Netmask: specifies the destination subnet mask of the flow protected by IPsec.

- Phase 1 Parameters

  - IKE Policy: specifies the policy used for IKE negotiation, such as 3DES-MD5-DH1 or 3DES-MD5-DH2.
  - IKE Lifetime: specifies the lifetime of the IKE SA.
  - Local ID Type: specifies the type of the local end's identifier. Options are FQDN, User FQDN, and IP Address.
  - Local ID: specifies the ID of the local end. This parameter needs to be set only when the local ID type is set to FQDN or user FQDN. Enter an ID of the specified type. (A user FQDN must be a standard email address.)
  - Remote ID Type: specifies the type of the remote end's identifier. Options are FQDN, User FQDN, and IP Address.
  - Remote ID: specifies the ID of the remote end. This parameter needs to be set only when the remote ID type is set to FQDN or user FQDN. Enter an ID of the specified type. (A user FQDN must be a standard email address.)
  - Authentication Method: specifies the authentication method used for the IPsec tunnel. Shared key authentication and digital certificate authentication are supported.
  - Key: specifies the key used for IPsec negotiation. Set this parameter when shared key authentication is used.

- Phase 2 Parameters

  - IPsec Policy: specifies the policy used for IPsec negotiation, such as 3DES-MD5-96 or 3DES-SHA1-96.
  - IPsec Lifetime: specifies the lifetime of the IPsec SA.

> **Caution**: Inbound and outbound rules must be created for each tunnel. A filtering policy will not be applied if it contains only the rule for one direction.



# Chapter 5 Typical Applications

The original document does not contain explicit typical application cases with network topology diagrams. No typical application cases are provided in this chapter.



## Appendix Troubleshooting

This appendix organizes common fault phenomena and troubleshooting methods for the IG902 gateway. When an abnormality is observed during operation, locate the corresponding phenomenon in the table below and perform the troubleshooting steps in sequence.

### 1 Device Startup and Indicator Issues

| Phenomenon | Possible Cause | Troubleshooting Steps | Related Chapter |
|------------|---------------|----------------------|-----------------|
| ERR indicator stays red after power-on | System startup error or hardware fault | 1. Power off the device and verify that the power supply voltage is within the acceptable range (12–48 V DC).<br>2. Check that the power cable and terminal block are securely connected.<br>3. Remove all non-essential cables and antennas, then power on again.<br>4. If the ERR indicator remains red, perform a hardware factory reset. | [Factory Reset](#factory-reset) |
| ERR indicator does not respond to RESET button during factory reset | RESET button timing is incorrect | 1. Ensure the RESET button is pressed within 10 seconds after the device is powered on.<br>2. Wait for the ERR indicator to turn solid red, then release the button.<br>3. Wait for the ERR indicator to turn off, then press and hold the RESET button again.<br>4. Release the RESET button when the ERR indicator blinks. | [Factory Reset](#factory-reset) |
| Signal status indicator shows value 1–9 | Antenna not installed properly or weak signal in the operating area | 1. Verify that the ANT antenna is securely tightened.<br>2. If signal strength is insufficient, connect the AUX antenna in addition to the ANT antenna.<br>3. Relocate the device to an area with better cellular coverage. | [Antenna Installation](#antenna-installation) |

### 2 Network Connection Issues

| Phenomenon | Possible Cause | Troubleshooting Steps | Related Chapter |
|------------|---------------|----------------------|-----------------|
| Unable to access the web management interface | PC IP address is not on the same subnet as the gateway | 1. Verify that the PC is connected to GE 0/1 or GE 0/2 via an Ethernet cable.<br>2. Check that the PC IP configuration matches the gateway subnet (GE 0/1: 192.168.1.x; GE 0/2: 192.168.2.x).<br>3. Alternatively, set the PC to obtain an IP address automatically. | [Web Interface Login](#web-interface-login) |
| Unable to access the web management interface | Incorrect username or password | 1. Verify that the username is `adm` and the password is `123456` (default values).<br>2. If the password was changed and forgotten, perform a hardware factory reset to restore default credentials. | [Default Settings](#default-settings) |
| Cellular dial-up fails | SIM card is not inserted or is improperly seated | 1. Power off the device.<br>2. Unfasten the screws on the SIM card holder cover and verify that the SIM card is correctly inserted.<br>3. Fasten the cover screws and power on the device again. | [SIM Card Installation](#sim-card-installation) |
| Cellular dial-up fails | APN parameters are incorrect | 1. Navigate to **Network > Network Interfaces > Cellular**.<br>2. Verify that the APN, access number, username, and password match the values provided by the network operator.<br>3. Click **Submit** to apply the corrected parameters. | [Cellular](#cellular) |
| Cellular dial-up fails | PIN code is enabled but incorrect or unset | 1. Navigate to **Network > Network Interfaces > Cellular**.<br>2. Verify that the PIN code matches the SIM card PIN.<br>3. If the PIN code is unknown, contact the network operator. | [Cellular](#cellular) |
| Cellular dial-up fails | Roaming is disabled while the SIM card is in roaming state | 1. Navigate to **Network > Network Interfaces > Cellular**.<br>2. Enable the **Roaming** option if the device is operating outside the home network.<br>3. Click **Submit** to apply the configuration. | [Cellular](#cellular) |
| Cellular connection drops frequently | Weak signal or antenna issue | 1. Check the signal status indicator value; if it is 1–9, improve antenna installation.<br>2. Ensure the ANT antenna is connected; add the AUX antenna if signal strength is poor.<br>3. Verify that the ICMP detection server is reachable and detection parameters are properly set. | [Cellular](#cellular) |
| Ethernet interface is down | Physical link is disconnected | 1. Verify that the Ethernet cable is securely connected to both the gateway and the peer device.<br>2. Check that the cable is not damaged.<br>3. Verify that **Track L2 State** is enabled if the interface state needs to reflect physical connectivity. | [Ethernet](#ethernet) |
| WLAN client mode fails to connect | Incorrect SSID or authentication parameters | 1. Navigate to **Network > Network Interfaces > WLAN**.<br>2. Verify that the **Client SSID** matches the target wireless network name.<br>3. Ensure that **Auth Method**, **Encrypt Mode**, and **WPA/WPA2 PSK Key** match the target network settings.<br>4. Click **Submit** to apply the configuration. | [WLAN](#wlan) |

### 3 Data Transmission Issues

| Phenomenon | Possible Cause | Troubleshooting Steps | Related Chapter |
|------------|---------------|----------------------|-----------------|
| DTU data forwarding fails | Serial port parameters do not match the terminal settings | 1. Navigate to **Industrial > DTU > Serial Port**.<br>2. Verify that baudrate, data bits, parity, and stop bit settings match those of the connected terminal.<br>3. Click **Submit** to apply the corrected parameters. | [DTU](#dtu) |
| DTU data forwarding fails | DTU and GPS serial forwarding are both enabled | 1. Navigate to **Industrial > DTU**.<br>2. Disable either DTU or GPS serial forwarding, as these two features cannot be enabled simultaneously.<br>3. Click **Submit** to apply the configuration. | [DTU](#dtu) |
| DTU cannot connect to the server | Incorrect destination IP address or port | 1. Navigate to **Industrial > DTU > DTU1** (or **DTU2**).<br>2. Verify that the **Server Address** and **Server Port** are correctly configured.<br>3. Verify that the gateway has a valid network connection (cellular or Ethernet).<br>4. Click **Submit** to apply the configuration. | [DTU](#dtu) |
| GPS serial forwarding does not work | DTU is enabled simultaneously | 1. Navigate to **Industrial > DTU**.<br>2. Disable DTU before enabling GPS serial forwarding.<br>3. Click **Submit** to apply the configuration. | [GPS](#gps) |

### 4 Configuration and System Issues

| Phenomenon | Possible Cause | Troubleshooting Steps | Related Chapter |
|------------|---------------|----------------------|-----------------|
| Configuration changes do not take effect | Changes were saved but not submitted | 1. After modifying parameters, click **OK** or **Save** to save the configuration.<br>2. Click **Submit** to apply the configuration to the system.<br>3. If necessary, reboot the device to ensure all changes take effect. | (Original draft lacks detail, pending supplementation) |
| System time is incorrect | NTP/SNTP is not configured | 1. Navigate to **System > System Time**.<br>2. Select the correct time zone or set the time manually.<br>3. Alternatively, enable **SNTP Clients** and configure a valid NTP server address.<br>4. Click **Apply** or **Submit** to apply the configuration. | [System Time](#system-time) |
| Forgotten web login password | Password was changed from the default | 1. Perform a hardware factory reset to restore the default username (`adm`) and password (`123456`).<br>2. After resetting, log in and navigate to **System > User Management** to set a new password. | [Factory Reset](#factory-reset) |
| DHCP clients cannot obtain IP addresses | DHCP server is disabled or misconfigured | 1. Navigate to **Network > Network Services > DHCP > DHCP Server**.<br>2. Verify that **Enable DHCP Service** is selected.<br>3. Verify that the interface, starting address, and ending address are correctly configured.<br>4. Click **Submit** to apply the configuration. | [DHCP Server](#dhcp-server) |
| DHCP relay does not work | DHCP relay is enabled while DHCP server is also enabled | 1. Navigate to **Network > Network Services > DHCP > DHCP Relay**.<br>2. Verify that the DHCP server is disabled before enabling the DHCP relay.<br>3. Verify that the DHCP server address and relay interface are correctly configured.<br>4. Click **Submit** to apply the configuration. | [DHCP Relay](#dhcp-relay) |

### 5 Hardware and Installation Issues

| Phenomenon | Possible Cause | Troubleshooting Steps | Related Chapter |
|------------|---------------|----------------------|-----------------|
| Device does not power on | Incorrect power supply or polarity | 1. Verify that the power supply voltage is 24 V DC (acceptable range: 12–48 V DC).<br>2. Check that the power cable polarity matches the terminal block markings.<br>3. Verify that the locking screw on the terminal block is fastened securely. | [Power Supply Connection](#power-supply-connection) |
| Device is loose on DIN-rail | Improper installation | 1. Press the device downward to disengage the lower end from the DIN-rail.<br>2. Reinstall by engaging the upper part of the DIN-rail seat first, then rotating the lower end upward until it locks securely.<br>3. Verify that the device does not move when gently pulled. | [DIN-Rail Installation](#din-rail-installation) |
| Antenna cannot be tightened | Excessive force applied to the plastic cover | 1. Rotate only the movable metal part of the SMA interface.<br>2. Do not twist the antenna by grasping the black plastic cover.<br>3. Tighten until the outer thread of the antenna connection cable is no longer visible. | [Antenna Installation](#antenna-installation) |



## Appendix Safety Precautions

1. The device requires a DC power supply of 24 V DC (12–48 V DC). The voltage class must be verified before connection. The rated current is 0.6 A (1.2–0.3 A).
2. The operating temperature range is –25°C to 75°C. The storage temperature range is –40°C to 85°C. The relative humidity range is 5% to 95% (non-condensing). The surface temperature of the device may be elevated during operation. The device must be installed in a restricted access area, and the surrounding environment must be assessed for suitability.
3. The device must not be exposed to direct sunlight and must be kept away from heat sources and areas with strong electromagnetic interference.
4. The gateway must be installed on an industrial DIN-rail.
5. All required cables and connectors must be verified as properly installed before operation.

> **Warning**: Verify the power supply voltage and current ratings before connecting power to avoid equipment damage.



## FAQ

### Question 1: How to Restore Factory Settings Through Hardware?

1. Locate the RESET button on the operation panel.
2. Press and hold the RESET button within 10 seconds after the device is powered on.
3. Release the RESET button when the ERR indicator turns red.
4. After a few seconds, when the ERR indicator turns off, press and hold the RESET button again.
5. Release the RESET button when the ERR indicator blinks. After a while, the ERR indicator turns off, indicating that the factory settings have been restored.

