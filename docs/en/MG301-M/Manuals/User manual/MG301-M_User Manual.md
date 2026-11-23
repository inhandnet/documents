# MG301-M Series Modular Modem User Manual

Version V1.0, August 2026

www.inhand.com.cn

<p align="center"><img src="images/cover_logo.png" alt="InHand logo" width="30%"></p>

The software described in this manual is provided under a license agreement and may only be used in accordance with the terms of that agreement.

**Copyright Notice**

© 2026 InHand Networks. All rights reserved.

**Trademarks**

The InHand logo is a registered trademark of InHand Networks.

All other trademarks or registered trademarks in this manual are the property of their respective manufacturers.

**Disclaimer**

The company reserves the right to make changes to this manual without prior notice in connection with subsequent product changes. The company assumes no responsibility for any direct, indirect, intentional or unintentional damage and hazards caused by improper installation or use.

---

## 1 Product Overview

### 1.1 Product Introduction

The MG301-M is a modular modem designed for smart metering applications in power distribution networks. It is used in conjunction with TEDA standard modular smart meters and belongs to the terminal communication unit of the MASS national smart metering system, enabling two-way remote data exchange between the meter and the distribution master station (Head-End).

The product supports 2G/4G LTE and NB-IoT cellular communication, scheduled meter reading, real-time alarms, remote firmware upgrade, digital input/relay output control, and can connect to various on-site devices to enable a wide range of applications.

### 1.2 Core Applications

- Collects meter energy data, events, open-cover alarms, and parameter data, and uploads them to the distribution master station;
- Receives commands issued by the master station: scheduled meter reading, parameter modification, firmware upgrade, relay on/off control;
- Proactively reports alarms for events such as power failure/restoration, low battery, network interruption, and unauthorized access;
- Caches metering data offline and automatically re-uploads it after the network is restored;
- Supports connection of external sensors and pulse acquisition devices (RS485 expansion interface).

## 2 Hardware Specifications and Structural Dimensions

### 2.1 Overall Dimensions

Standard size: 114mm × 74.4mm × 45mm, matching the Modem slot size inside the terminal cover of the modular meter.

<p align="center"><img src="images/dimensions.png" alt="MG301-M structural dimensions" width="90%"></p>

### 2.2 Enclosure Structure

- Protection rating: IP40, dust-proof and protected against ingress of foreign objects; mechanical impact rating IK06, withstands light on-site impacts;
- Flame retardancy rating: V-0, no flame spread combustion at high temperature;
- Plug-and-play reverse-insertion prevention structure, eliminating reverse connection to the meter socket;
- SIM card **standard card slot** (standard, tool-free SIM insertion/removal), optional built-in eSIM (supports remote carrier profile switching);
- SMA antenna interface, standard external GSM antenna included; a high-gain antenna can be fitted for weak-signal scenarios.

<p align="center"><img src="images/product_photo.png" alt="MG301-M product photo" width="70%"></p>

### 2.3 Basic Electrical Parameters

| Parameter | Specification |
|-----------|---------------|
| Supply voltage | 12VDC ±10%, supplied by the meter's isolated power supply |
| Maximum operating current | 500mA |
| Maximum power consumption | 6W |
| Electrical protection rating | Class II insulation |
| Overcurrent protection | Built-in resettable fuse, prevents large currents from damaging the meter |

### 2.4 Operating Environment Specifications

| Parameter | Specification |
|-----------|---------------|
| Operating temperature | -30°C ~ +70°C |
| Relative humidity | 0% ~ 93%, non-condensing |
| Pollution degree | 3 |
| Overvoltage category | III |

## 3 Interface and Indicator Descriptions

### 3.1 Front Panel LED Status Indicators

| Indicator | Silkscreen Marking | Off | Blinking | Steady On |
|-----------|--------------------|-----|----------|-----------|
| Power LED | PWR | No power supply | - | Device powered on normally |
| Serial communication LED | 485-1/485-2 | No RS485 data | Meter data transmission/reception in progress | - |
| Signal quality LED | 📶 | No signal | - | Signal value <14: 1 bar lit; 14<signal value<20: 2 bars lit; Signal value >20: all 3 bars lit |
| IP address LED | IP | No carrier, IP acquired | - | IP assigned, can connect to the master station |
| 2G/4G communication LED | 2G/4G | Network registration failed | - | Network registered successfully (2G/4G) |
| Relay LED (optional) | Relay | Relay open | - | Relay closed |

<p align="center"><img src="images/led_panel.png" alt="MG301-M front panel LED indicators" width="60%"></p>

### 3.2 Hardware Interface Definitions

| Hardware Interface | Functional Description |
|--------------------|------------------------|
| RS485 primary interface (standard) | Local communication with the meter, baud rate up to 115200bps; Optional second RS485 port (cannot be selected together with the relay output), for connecting external sensors and pulse acquisition terminals |
| Type-C USB 2.0 interface (standard) | Local log retrieval, on-site parameter configuration, local firmware upgrade |
| Dry-contact digital input (1 channel standard) | External passive contact acquisition: closed = binary 1, open = binary 0; Acquisition purpose is remotely programmable |
| Relay output (optional, up to 1 channel) | Load capacity: 240VAC/5A; Retains the existing on/off state during power failure/reset (latching relay design); When the relay is selected, the second RS485 port cannot be expanded |
| SMA antenna interface | Cellular communication antenna mounting point (horizontal cable routing) |
| SIM card slot | External standard slot, supports Micro SIM; optional eSIM for remote carrier switching |

<p align="center"><img src="images/interfaces_annotated.png" alt="MG301-M hardware interfaces" width="70%"></p>

<p align="center"><img src="images/rs485_meter_port.png" alt="Pin9/Pin10 serve as primary RS485 interface for direct communication with electricity meters" width="70%"></p>

## 4 Power Supply, Battery, and Power Failure Protection

### 4.1 Primary Power Supply

The device is normally powered by the 12V isolated DC power supply built into the modular meter, with a maximum output of 500mA and built-in current limiting protection.

### 4.2 Backup Power Supply

- **RTC real-time clock battery (standard)**
  - ensures accurate log and event timestamps after a power failure.
- **System backup power supply (optional)**
  - Rechargeable lithium battery; maintains short-term cellular communication after a mains power failure, automatically sends a power-failure notification to the master station, and records timestamped power-failure events; proactively reports a low-battery alarm when the battery level falls below 20%.

### 4.3 Power Failure and Restoration Logic

- At the moment of power failure: the backup power supply supports uploading the power-failure alarm log;
- On power restoration: automatically sends a "ready status" data packet to the master station, with a power-restoration flag;
- All meter data and events are cached locally during the offline period and re-transmitted in batch once the network is restored.

## 5 Installation, Wiring, and Plug-and-Play Operation

### 5.1 Installation Steps

1. Power off: disconnect the incoming power supply of the corresponding modular meter;
2. Open the meter's terminal protective cover to expose the standard Modem slot;
3. Align the reverse-insertion prevention latch and insert the Modem vertically; a click sound from the latch indicates that it is secured (plug-and-play, no additional wiring required);
4. Insert the Micro SIM card (external card slot) and tighten the SMA antenna;
5. Restore power to the meter, observe that the front power LED is steady on, and wait 30~120 seconds for automatic network search and base station registration.

### 5.2 Optional Accessory Installation

1. High-gain antenna: replace the standard antenna when the on-site signal is weak, and tighten the SMA connector;
2. External digital input: connect passive dry contacts to the DI terminals, non-polarized;
3. Relay output: connect external controlled loads, up to 240VAC 5A;
4. Second RS485: distinguish the A/B lines and connect external sensors (this option cannot be combined with the relay).

<p align="center"><img src="images/modem_socket.png" alt="Standard Modem Socket" width="70%"></p>

### 5.3 Removal

Disconnect power from the meter, press the latches on both sides and pull the Modem out vertically; to replace the SIM, simply pull out the external card slot.

## 6 Getting Started

### 6.1 Accessing the MG301-M

Connect the PC and the MG301-M using the Type-C USB 2.0 interface.

<p align="center"><img src="images/com_ports.png" alt="COM ports in device manager" width="60%"></p>

**Step 1**: Install the local configuration tool MG3XXTool_Installer.exe

<p align="center"><img src="images/tool_main_window.png" alt="InHand MG3XX Configuration Tool main window" width="70%"></p>

**Step 2**: Open the configuration tool, click "Connect" and select the corresponding COM port; leave the other parameters at their defaults, then click "Connect"

<p align="center"><img src="images/connect_dialog.png" alt="Connect to MG dialog" width="70%"></p>

Username: **admin**

Password: **admin@123**

**Step 3**: After successful login, the system status of the device can be viewed, as shown in the figure below

<p align="center"><img src="images/login_success.png" alt="Login success" width="70%"></p>

<p align="center"><img src="images/config_read_success.png" alt="Configuration read succeeded" width="70%"></p>

<p align="center"><img src="images/status_summary.png" alt="Status summary page" width="70%"></p>

On the **Physical layer** tab, the module status, signal quality (CSQ), SIM status and other cellular information can be viewed:

<p align="center"><img src="images/status_physical_layer.png" alt="Status physical layer page" width="70%"></p>

On the **Network layer** tab, the authentication mode, cellular IP, and data transmission statistics can be viewed:

<p align="center"><img src="images/status_network_layer.png" alt="Status network layer page" width="70%"></p>

If the password is forgotten and the device cannot be accessed, click "Forgot password?". The device will then be restored to factory defaults, and the username and password revert to admin/admin@123.

<p align="center"><img src="images/forgot_password.png" alt="Forgot password button" width="70%"></p>

<p align="center"><img src="images/forgot_password_confirm.png" alt="Forgot password confirmation" width="70%"></p>

### 6.2 System Settings

#### 6.2.1 System Time

For better coordination between the MG301-M and other devices, the system time must be configured accurately. The configuration methods and steps are as follows:

- **Method 1: Use the PC's local time to configure the system time**

  After logging into the local configuration tool, the MG301-M automatically obtains the PC's local time.

  <p align="center"><img src="images/time_pc_sync.png" alt="MG time synced from PC" width="70%"></p>

- **Method 2: Use the time zone to configure the system time**

  In the Configurations→Advanced configuration→Extended configuration→Time Settings page, customize the time zone, then click "Save configurations" and reboot the device.

  <p align="center"><img src="images/time_settings.png" alt="Time Settings page" width="70%"></p>

- **Method 3: Use an SNTP server to configure the system time**

  In the Configurations→Advanced configuration→Extended configuration→SNTP page, configure the SNTP server parameters, then click "Save configurations" and reboot the device.

  <p align="center"><img src="images/sntp_settings.png" alt="SNTP settings page" width="70%"></p>

  The SNTP server parameters are described as follows:

  - SNTP service: SNTP enable/disable switch
    - Open: enables the SNTP service
    - Close: disables the SNTP service
  - SNTP server: the address of the SNTP server (domain name or IP address)
  - SNTP Port: the port of the SNTP server
  - SNTP Sync Period(min): synchronizes the device time to the server at the specified update interval

#### 6.2.2 System Logs

##### 6.2.2.1 Real-time Log

In Maintenance→Real-time log, click "Start receive" to view the device's real-time log.

<p align="center"><img src="images/realtime_log_start.png" alt="Start receiving real-time log" width="70%"></p>

**Step 1**: Click "Stop receive" to stop real-time log output.

<p align="center"><img src="images/realtime_log_stop.png" alt="Stop receiving real-time log" width="70%"></p>

**Step 2**: After stopping real-time log output, click "Export log" to save the real-time log currently displayed on the interface to the local PC.

<p align="center"><img src="images/realtime_log_export.png" alt="Export real-time log" width="70%"></p>

**Step 3**: Click "Clear screen" to clear the real-time log currently displayed on the interface.

<p align="center"><img src="images/realtime_log_clear.png" alt="Clear real-time log screen" width="70%"></p>

##### 6.2.2.2 Historical Log

In Maintenance→History log, click "Read log" to view the device's historical log.

<p align="center"><img src="images/history_log_read.png" alt="Read historical log" width="70%"></p>

**Step 1**: Click "Stop reading" to stop historical log output.

<p align="center"><img src="images/history_log_stop.png" alt="Stop reading historical log" width="70%"></p>

**Step 2**: After stopping historical log output, click "Export log" to save the historical log currently displayed on the interface to the local PC.

<p align="center"><img src="images/history_log_export.png" alt="Export historical log" width="70%"></p>

**Step 3**: Click "Erase log" to clear the historical logs stored in the device.

<p align="center"><img src="images/history_log_erase.png" alt="Erase historical log" width="70%"></p>

#### 6.2.3 Configuration Management

In the Configurations interface, click "Read configurations" to read the device's current configuration.

<p align="center"><img src="images/config_read.png" alt="Read configurations" width="70%"></p>

**Step 1**: Click "Export configurations" to export the device's current configuration and generate a configuration file saved to the local PC.

<p align="center"><img src="images/config_export.png" alt="Export configurations" width="70%"></p>

**Step 2**: Click "Import configurations" to import the configuration file from the local PC to the device.

<p align="center"><img src="images/config_import.png" alt="Import configurations" width="70%"></p>

**Step 3**: After modifying the configuration, click "Save configurations" to save it, then reboot the device for the changes to take effect.

<p align="center"><img src="images/config_save_reboot.png" alt="Save configurations and reboot" width="70%"></p>

#### 6.2.4 Rebooting the Device

In the Status interface, click "Reboot" to reboot the device.

<p align="center"><img src="images/reboot.png" alt="Reboot button" width="70%"></p>

Click "Factory reset" to restore the device configuration to factory defaults.

<p align="center"><img src="images/factory_reset.png" alt="Factory reset button" width="70%"></p>

#### 6.2.5 Firmware Upgrade

In Maintenance→Upgrade firmware, click "Browse file" to select the file to upgrade, then click "Upgrade" to complete the firmware version upgrade.

<p align="center"><img src="images/firmware_upgrade.png" alt="Upgrade firmware page" width="70%"></p>

#### 6.2.6 Log Out

Click "Disconnect" to log out of the current account.

<p align="center"><img src="images/logout.png" alt="Disconnect button" width="70%"></p>

### 6.3 Network Settings

#### 6.3.1 Cellular Network

Configure the MG301-M's redial rules in the Configurations→Basic configuration→Dial parameters page.

<p align="center"><img src="images/dial_parameters.png" alt="Dial parameters page" width="70%"></p>

Configure the MG301-M's cellular network parameters in the SIM card 1 page.

<p align="center"><img src="images/sim_card1.png" alt="SIM card 1 page" width="70%"></p>

The cellular network parameters are described as follows:

- Auto dial: the MG301-M automatically registers to the network and dials after startup
- Redial interval: the time interval for the device to retry the connection after a dial failure
- Max redial times: when the MG301-M's consecutive redial attempts exceed this count, a reboot is triggered
- Network dialing number: the dialing string used for dialing; the dialing string is provided by the carrier, please obtain it from the carrier
- APN: (Access Point Name) identifies the service type of the WCDMA/LTE network. The WCDMA/LTE system provides corresponding services based on the APN used by the user to connect to the WCDMA/LTE network; it is provided by the carrier
- Network dial username: specifies the username for accessing the external PDN network; provided by the carrier
- Network dial password: specifies the password for accessing the external PDN network
- Authentication mode:
  - Auto: automatically selects an authentication method
  - PAP: Password Authentication Protocol; provides a simple plaintext authentication method via a two-way handshake
  - CHAP: Challenge Handshake Authentication Protocol; performs secure authentication by confirming digest information via a three-way handshake
- Network mode: networks such as Auto, Only 2G, and Only 4G can be selected. According to the device in use and the SIM card conditions, users can select a specific network mode or use the automatic mode, in which the device registers to the network mode most suitable for the current network conditions
- Local number: sets the number of the SIM card in use (if the number has already been written to the SIM card, this configuration will not take effect!)

<p align="center"><img src="images/sim_card1_params.png" alt="SIM card 1 parameters" width="70%"></p>

### 6.4 Communication Protocols

#### 6.4.1 MASS

Configure the MASS protocol parameters in the Configurations→Basic configuration→MASS Protocol Setting page.

When Protocol is set to MQTT, the interface displays the MQTT parameter configuration items.

When Protocol is set to TCP, the interface displays the TCP parameter configuration items.

<p align="center"><img src="images/mass_tcp.png" alt="MASS protocol TCP settings" width="70%"></p>

Configure the basic MASS protocol parameters in the Other Setting page.

<p align="center"><img src="images/mass_other_setting.png" alt="MASS protocol Other Setting page" width="70%"></p>

The MASS protocol parameters are described as follows:

- Protocol: select the protocol
  - disable: disables the MASS protocol
  - MQTT: communicate using MQTT
  - TCP: communicate using TCP
- MQTT Topic Prefix: MQTT topic prefix
- MQTT Username: the username used to connect to the MQTT server
- MQTT Password: the password used to connect to the MQTT server
- MQTT Broker Address: the MQTT server address
- MQTT Broker Port: the MQTT server listening port
- TCP IP: the TCP server address
- TCP Port: the TCP server listening port
- MASS Heartbeat Period(min): the MG301-M's heartbeat transmission period, in minutes
- MASS Auto Restart Period(h): the MG301-M's automatic restart period, in hours. A value of 0 disables this function
- MASS Data Lifespan(h): the duration for which the MG301-M stores read data, in hours. A value of 0 disables this function
- MASS Retry Interval(min): the retry interval for the MG301-M to resend messages to the server, in minutes
- MASS Retry Count: the number of retries for the MG301-M to resend messages to the server

### 6.5 User Settings

Configure the username and password for logging into/managing the MG301-M in the Configurations→Advanced configuration→Administrator setting page.

<p align="center"><img src="images/user_settings.png" alt="Administrator setting page" width="70%"></p>

The user parameters are described as follows:

- Administrator account: the username for logging into the MG301-M
- Administrator password: the password for logging into the MG301-M

Note: The username and password must be set together!

### 6.6 ICMP Detection

Configure the ICMP detection parameters in the Configurations→Advanced configuration→ICMP setting page.

<p align="center"><img src="images/icmp_setting.png" alt="ICMP setting page" width="70%"></p>

The ICMP parameters are described as follows:

- ICMP host: ICMP detection target address
- Max lost packets: the number of detection failures. A redial is triggered when the cumulative count reaches this value
- ICMP detect interval: the time interval for sending ICMP detection packets
- ICMP timeout: if no ICMP response packet is received within the configured ICMP detection timeout, the ICMP detection is considered timed out

## 7 Package Contents

**Standard Accessories**

| Accessory | Quantity | Description |
|-----------|----------|-------------|
| Modem module | 1 unit | MG301-M |
| Antenna | 1 pcs | 1× cellular antenna |
| Wiring terminals | 1 set | Industrial terminals for connecting power supply, serial port, I/O, and relay |
