# MO68A User Guide

**Version 1.0 · Beijing InHand Networks Technology Co., Ltd.**

## Task-based navigation

| Concern | Where to read |
| ------- | ------------- |
| Fastest path (flash SD, wiring, first login) | [MO68A Quick Start Guide](MO68A_Quick_Start_Guide_V1.0.md) |
| Connector pinouts, electrical and mechanical specs | [MO68A Hardware Reference Manual](MO68A_Hardware_Reference_Manual_V1.0.md) |
| Hostname, timezone, locale, apt after the wizard | [§3 Getting Started](#3-getting-started) |
| Software install and upgrade | [§4 Software Management](#4-software-management) |
| SD partitioning and free space | [§5 Micro SD Card](#5-micro-sd-card) |
| Serial troubleshooting and early boot log | [§6 Debug Serial Console](#6-debug-serial-console) |
| No display or DisplayPort compatibility | [§7 Mini DisplayPort](#7-mini-displayport), [§19.5 Display No Signal](#195-display-no-signal) |
| Ethernet and SSH | [§8 Network and Remote Access](#8-network-and-remote-access) |
| Fan required and thermal control | [§9 Fan and Thermal Management](#9-fan-and-thermal-management) |
| Sensors / RTC / EEPROM on I2C | [§10 I2C](#10-i2c), [§11 RTC](#11-rtc) |
| USB audio / storage / HID | [§12 USB](#12-usb) |
| NVMe / PCIe expansion | [§13 PCIe](#13-pcie) |
| Raspberry Pi HAT, GPIO / SPI / UART | [§14 40-pin GPIO Header](#14-40-pin-gpio-header) |
| MIPI CSI camera or DSI display | [§15 MIPI FPC Ports](#15-mipi-fpc-ports), [§16 MIPI DSI Display](#16-mipi-dsi-display), [§17 Camera Input](#17-camera-input) |
| AI inference / MMA | [§18 AI Inference Acceleration](#18-ai-inference-acceleration) |
| Boot failure, network, NVMe, display | [§19 Troubleshooting](#19-troubleshooting) |

---

## 1. Introduction

### 1.1 Product Overview

MO68A is a single-board computer built around the TDA4VE / AM68A SoC (TI J721S2 family). It features dual Cortex-A72 application cores, up to six Cortex-R5F MCU cores, and an 8 TOPS AI accelerator, all in a Raspberry Pi 40-pin HAT-compatible form factor.

The board runs Armbian Linux (Debian 13 Trixie) and is suited for AI edge inference, machine vision, embedded Linux development, and industrial computing applications.

### 1.2 Key Specifications

| Parameter      | Value                                     |
|:-------------- |:----------------------------------------- |
| SoC            | TDA4VE / AM68A (TI J721S2)                |
| CPU            | 2× ARM Cortex-A72, up to 2.0 GHz          |
| AI Accelerator | 8 TOPS (MMA)                              |
| RAM            | 8 GB LPDDR4                               |
| Storage        | Micro SD (primary); PCIe NVMe (expansion) |
| OS             | Armbian (Debian 13 Trixie)                |
| Networking     | Gigabit Ethernet                          |
| USB            | 4× USB 3.0 Type-A                         |
| Display        | Mini DisplayPort                          |
| Camera/Display | 2× MIPI 22-pin FPC (CSI-2 / DSI)          |
| Expansion      | 40-pin GPIO header (RPi HAT compatible)   |
| Power input    | USB-C, 5 V / 5 A (27 W)                   |

### 1.3 Document Scope

| Document | Covers |
| --- | --- |
| [MO68A Quick Start Guide](MO68A_Quick_Start_Guide_V1.0.md) | Shortest path: flash SD, wiring, power-on, first login, and network access |
| **MO68A User Guide (this document)** | Interface usage, peripheral configuration, system administration, troubleshooting |
| [MO68A Hardware Reference Manual](MO68A_Hardware_Reference_Manual_V1.0.md) | Circuit and connector definitions, key components, mechanical reference |

This guide assumes you have completed SD image flashing and first-time initialization from the Quick Start Guide. If not, read the [Shortest path](MO68A_Quick_Start_Guide_V1.0.md#shortest-path) section in the [MO68A Quick Start Guide](MO68A_Quick_Start_Guide_V1.0.md) first.

---

## 2. Accessories and Requirements

| Item                   | Specification             | Notes                           |
|:---------------------- |:------------------------- |:------------------------------- |
| USB-C power adapter    | 5 V / 5 A (25 W minimum)  | Required                        |
| Micro SD card          | ≥ 16 GB, Class 10 / UHS-I | Required                        |
| PWM fan (4-pin)        | 5 V                       | Required for thermal management |
| RJ45 Ethernet cable    | —                         | Required                        |
| Mini DisplayPort cable | —                         | Desktop use                     |
| DisplayPort monitor    | DisplayPort input         | Desktop use                     |
| USB keyboard and mouse | —                         | Desktop use                     |
| USB-to-UART adapter    | 3.3 V logic               | Serial debug console            |
| RTC battery            | CR2032, 2-pin JST-SH      | Optional; required for RTC      |

---

## 3. Getting Started

### 3.1 Initial Setup

Follow the [MO68A Quick Start Guide](MO68A_Quick_Start_Guide_V1.0.md) to:

1. Flash the Armbian image to a Micro SD card
2. Connect all peripherals (fan, display, Ethernet, power — in that order)
3. Complete the first-login initialization wizard (locale, timezone, user account)

The board is ready for use when the green LED (D1) is solid.

### 3.2 Verify System Status

After login, confirm the system is running correctly:

```bash
# Kernel version
uname -r

# OS information
cat /etc/os-release

# Storage layout
lsblk

# Memory
free -h

# Network
ip addr show eth0
```

Expected output: root filesystem on `/dev/mmcblk1p2`, `eth0` with an assigned IP address. If an NVMe SSD is installed, `/dev/nvme0n1` will also appear in the `lsblk` output.

### 3.3 Recommended Initial Configuration

**Set hostname:**

```bash
hostnamectl set-hostname mo68a
```

**Set timezone** (replace with your local timezone):

```bash
timedatectl set-timezone Asia/Shanghai
timedatectl status
```

**Update package list:**

```bash
apt update
```

**Set locale:**

```bash
dpkg-reconfigure locales
```

---

## 4. Software Management

MO68A runs Armbian Linux (Debian 13 Trixie). Package management uses `apt`, the standard Debian package manager. All commands below should be run as root or with `sudo`.

**Update package index** (run before installing or upgrading):

```bash
apt update
```

**Install a package:**

```bash
apt install <package>
```

**Remove a package:**

```bash
# Keep configuration files
apt remove <package>

# Remove package and its configuration files
apt purge <package>
```

**Remove unused dependencies:**

```bash
apt autoremove
```

**Upgrade all installed packages:**

```bash
apt upgrade
```

**Search for packages by keyword:**

```bash
apt search <keyword>
```

**Show package details:**

```bash
apt show <package>
```

---

## 5. Micro SD Card

The Micro SD card is the primary boot medium and root filesystem storage. It contains two partitions:

| Partition   | Size      | Mount point | Purpose                       |
|:----------- |:--------- |:----------- |:----------------------------- |
| `mmcblk1p1` | 256 MB    | `/boot`     | Kernel, device tree, overlays |
| `mmcblk1p2` | Remaining | `/`         | Root filesystem               |

**View partition layout:**

```bash
lsblk /dev/mmcblk1
```

Example output:

```
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
mmcblk1     179:0    0 29.7G  0 disk
├─mmcblk1p1 179:1    0  256M  0 part /boot
└─mmcblk1p2 179:2    0 29.2G  0 part /var/log.hdd
                                     /
```

> `mmcblk1p2` shows two mount points: `/` (root filesystem) and `/var/log.hdd`. Armbian mounts `/var/log` as a tmpfs at runtime to reduce SD card wear; `/var/log.hdd` is the persistent log directory on the SD card.

**Check available space:**

```bash
df -h /
```

> On first boot, Armbian automatically expands the root partition to fill the SD card. This triggers one automatic reboot and takes 1–2 minutes.

---

## 6. Debug Serial Console

The board provides a hardware serial console on connector J6 (SH1.0 3-pin). This console outputs the full boot log and provides a login prompt independent of the display or network — making it essential for headless setup, kernel debugging, and recovery.

### 6.1 Hardware Connection

Connect a 3.3 V USB-to-UART adapter to J6:

| Pin | Signal |
|:--- |:------ |
| 1   | RXD    |
| 2   | GND    |
| 3   | TXD    |

> **Warning:** Use a **3.3 V logic** adapter only. A 5 V adapter will damage the board.

Connect the adapter **before** applying power to capture the full boot log from the start.

### 6.2 Terminal Setup

Settings: **115200 baud, 8N1, no flow control**

```bash
# Linux
minicom -D /dev/ttyUSB0 -b 115200
```

On Windows, use PuTTY or Tera Term and select the correct COM port.

The console device on the board is `/dev/ttyS2` (UART8). This port is dedicated to the debug console — do not use it for general-purpose UART communication.

---

## 7. Mini DisplayPort

Connect a DisplayPort monitor to J9 (Mini DisplayPort). The board outputs video after the desktop environment loads.

> The display must have a native DisplayPort input. A passive Mini DP to HDMI adapter will not work; use an active adapter or a DP-native monitor.

**Check display detection:**

```bash
cat /sys/class/drm/card*/card*-DP-*/status
```

---

## 8. Network and Remote Access

### 8.1 Wired Ethernet

The board uses NetworkManager. The Ethernet interface is `eth0` and uses DHCP by default.

**Check connection status:**

```bash
nmcli device status
```

**View assigned IP address:**

```bash
ip addr show eth0
```

**Configure a static IP address:**

```bash
nmcli con mod "Wired connection 1" \
  ipv4.method manual \
  ipv4.addresses 192.168.1.100/24 \
  ipv4.gateway 192.168.1.1 \
  ipv4.dns "8.8.8.8 8.8.4.4"
nmcli con up "Wired connection 1"
```

**Revert to DHCP:**

```bash
nmcli con mod "Wired connection 1" ipv4.method auto
nmcli con up "Wired connection 1"
```

### 8.2 SSH Access

SSH server is enabled by default. Connect from a host computer:

```bash
ssh <username>@<board-ip>
```

---

## 9. Fan and Thermal Management

### 9.1 Fan Connector

Connect a 5 V 4-pin PWM fan to J7 (SH1.0, 1.0 mm pitch):

| Pin | Signal | Direction      |
|:--- |:------ |:-------------- |
| 1   | 5 V    | Power out      |
| 2   | PWM    | Output to fan  |
| 3   | GND    | Ground         |
| 4   | TACH   | Input from fan |

### 9.2 Automatic Speed Control

Fan speed is controlled automatically by the kernel thermal governor based on the SoC temperature. The fan always runs at a minimum of 20% speed; it ramps up as temperature rises.

| Temperature (main0-thermal) | Fan speed  |
|:--------------------------- |:---------- |
| Below 60 °C                 | 20 %       |
| 60 – 70 °C                  | 40 – 60 %  |
| 70 – 80 °C                  | 60 – 80 %  |
| Above 80 °C                 | 80 – 100 % |

The PWM signal runs at 25 kHz. Speed transitions are stepped by the governor on each 1-second polling cycle.

### 9.3 Monitoring

**Fan speed (RPM):**

```bash
cat /sys/class/hwmon/hwmon0/fan1_input
```

Example output:

```
5742
```

RPM is measured from the TACH signal: the driver counts falling edges on the tachometer input and samples once per second. Accuracy depends on the fan's pulses-per-revolution specification (2 pulses/rev assumed, standard for most 4-pin PWM fans).

**PWM output state:**

```bash
cat /sys/kernel/debug/pwm
```

Example output (idle, 20 % duty cycle):

```
0: platform/3010000.pwm, 2 PWM devices
 pwm-0   ((null)   ): period: 0 ns duty: 0 ns polarity: normal
 pwm-1   (pwm-fan  ): requested enabled period: 40000 ns duty: 8000 ns polarity: normal usage_power
```

The `duty` value divided by `period` gives the current duty cycle (8000 / 40000 = 20 %).

**Current cooling level:**

```bash
cat /sys/class/thermal/cooling_device0/cur_state   # 0–4
cat /sys/class/thermal/cooling_device0/max_state   # 4
```

**All zone temperatures:**

```bash
for z in /sys/class/thermal/thermal_zone*/; do
  printf '%-20s %d °C\n' "$(cat ${z}type)" "$(($(cat ${z}temp) / 1000))"
done
```

Example output:

```
wkup0-thermal        50 °C
wkup1-thermal        50 °C
main0-thermal        50 °C
main1-thermal        51 °C
main2-thermal        51 °C
main3-thermal        51 °C
main4-thermal        50 °C
```

The fan is controlled by **main0-thermal** (thermal_zone2). To monitor it continuously:

```bash
watch -n 2 cat /sys/class/thermal/thermal_zone2/temp
```

---

## 10. I2C

The SoC exposes five I2C buses. Use `i2cdetect -l` to list them:

```bash
i2cdetect -l
```

Example output:

```
i2c-0   i2c             OMAP I2C adapter                        I2C adapter
i2c-1   i2c             OMAP I2C adapter                        I2C adapter
i2c-2   i2c             OMAP I2C adapter                        I2C adapter
i2c-3   i2c             OMAP I2C adapter                        I2C adapter
i2c-4   i2c             a000000.dp-bridge                       I2C adapter
```

| Device node  | SoC bus   | Connected to                    | 40-pin pins                               |
|:------------ |:--------- |:------------------------------- |:----------------------------------------- |
| `/dev/i2c-0` | WKUP I2C0 | PMIC and power ICs              | 27, 28 (shared with PMIC — use with care) |
| `/dev/i2c-1` | SOC I2C0  | 40-pin header (user)            | 3, 5                                      |
| `/dev/i2c-2` | SOC I2C1  | Board EEPROM (0x50), RTC (0x51) | —                                         |
| `/dev/i2c-3` | SOC I2C5  | MIPI FPC (internal)             | —                                         |
| `/dev/i2c-4` | DP AUX    | Mini DisplayPort (AUX channel)  | —                                         |

> **Caution:** `/dev/i2c-0` (pins 27, 28) is shared with the PMIC. Incorrect transactions on this bus can affect system power rails. Scan or access it only if you understand the consequences.

> **Caution:** `/dev/i2c-4` is the DisplayPort AUX channel I2C adapter, used internally by the display subsystem. Do not scan or access this bus.

**Scan an I2C bus:**

```bash
i2cdetect -y -r <bus>
```

The `-r` flag uses read-mode probing, which is safer than the default Quick Write mode.

Example — scan the 40-pin user I2C bus (SOC I2C0, pins 3 and 5):

```bash
i2cdetect -y -r 1
```

**Read a register:**

```bash
i2cget -y <bus> <addr> <reg>
```

**Dump all registers of a device:**

```bash
i2cdump -y <bus> <addr>
```

**Write a register:**

```bash
i2cset -y <bus> <addr> <reg> <value>
```

> **Warning:** `i2cset` writes directly to device registers and takes effect immediately. Writing incorrect values to the wrong device — especially on bus 0 (PMIC) — can cause system instability or hardware damage. Only use `i2cset` on known devices with a register map you understand.

---

## 11. RTC

### 11.1 Battery Installation

The RTC (PCF85263ATL) is backed by a CR2032 battery connected via J8 (SH1.0, 2-pin, 1.0 mm pitch). Install the battery before setting the time to preserve the clock across power cycles.

Use a CR2032 coin cell with a pre-fitted 2-pin JST-SH (1.0 mm pitch) connector. Do not insert a bare coin cell; the JST connector is required.

### 11.2 Time Configuration

Armbian uses `systemd-timesyncd` to synchronize the system clock from NTP. When network is available, the system time is kept accurate automatically. systemd also writes the system time to the RTC periodically and on shutdown, so the RTC stays in sync without manual intervention.

**Verify the RTC driver is loaded:**

```bash
ls /dev/rtc*
```

**Check the current time and RTC status:**

```bash
timedatectl status
```

The output includes both `Local time` (system clock) and `RTC time` (hardware clock).

To verify the RTC works correctly, disable NTP, set a known time manually, then reboot and confirm the time is preserved.

**Disable automatic time synchronization:**

```bash
timedatectl set-ntp false
```

**Set the system time manually:**

```bash
timedatectl set-time "2026-05-08 12:00:00"
```

systemd automatically writes the new time to the RTC. Verify both clocks are updated:

```bash
timedatectl status
```

**Reboot, then confirm the time is preserved:**

```bash
reboot
# After reboot:
timedatectl status
```

---

## 12. USB

The four USB 3.0 Type-A ports provide peripheral expansion. Common scenarios covered in this section include keyboard and mouse input, audio output, and portable storage.

### 12.1 USB 3.0 Type-A Ports

Four USB 3.0 ports are provided via the TUSB8041 hub: two on J2 and two on J3.

**List all connected USB devices:**

```bash
lsusb
```

Example output with a mouse and keyboard connected:

```
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0451:8142 Texas Instruments, Inc. TUSB8041 4-Port Hub
Bus 001 Device 003: ID 046d:c077 Logitech, Inc. Mouse
Bus 001 Device 004: ID 046d:c31d Logitech, Inc. Media Keyboard K200
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
```

The TUSB8041 hub always appears on Bus 001. Devices connected to the Type-A ports appear as additional entries under Bus 001 or Bus 002.

### 12.2 Keyboard and Mouse

USB keyboards and mice are supported out of the box via the USB HID driver. Connect to any Type-A port (J2 or J3) and the device is immediately available — no configuration required.

On the desktop, input is handled by the graphical environment. In headless mode, a USB keyboard is available on a local terminal session.

### 12.3 USB Audio

USB audio devices (speakers, headsets, USB sound cards) are plug-and-play. The kernel's built-in USB Audio Class (UAC) driver requires no configuration — connect the device and it is immediately available as an ALSA sound card.

**Step 1 — Verify detection:**

```bash
lsusb
```

Example output (USB speaker appears as a new entry under Bus 001):

```
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0451:8142 Texas Instruments, Inc. TUSB8041 4-Port Hub
Bus 001 Device 003: ID 046d:c077 Logitech, Inc. Mouse
Bus 001 Device 004: ID 046d:c31d Logitech, Inc. Media Keyboard K200
Bus 001 Device 008: ID 4c4a:4155 Jieli Technology UACDemoV1.0
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
```

Confirm ALSA has registered it as a sound card and find the card number:

```bash
aplay -l
```

Example output when an I2S audio HAT is also installed (WM8960 takes card 0; USB audio is assigned card 1):

```
card 0: WM8960Audio [WM8960-Audio], device 0: davinci-mcasp.0-wm8960-hifi wm8960-hifi-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: UACDemoV10 [UACDemoV1.0], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

> Card numbers are assigned in probe order. I2S devices probe before USB, so a USB audio device is card 0 only when no I2S sound card is present.

To find the USB audio card number directly:

```bash
aplay -l | grep -i "USB Audio"
```

Example output:

```
card 1: UACDemoV10 [UACDemoV1.0], device 0: USB Audio [USB Audio]
```

The card number and device number both appear in the output (e.g. `card 1:`, `device 0:`). Use those values in all subsequent commands (shown as `<C>` and `<D>` below).

**Step 2 — Adjust volume:**

Query mixer controls and volume range (values are device-specific):

```bash
amixer -c <C> contents
```

Example output for a USB speaker:

```
numid=2,iface=MIXER,name='PCM Playback Switch'
  ; type=BOOLEAN,access=rw------,values=1
  : values=on

numid=3,iface=MIXER,name='PCM Playback Volume'
  ; type=INTEGER,access=rw---R--,values=2,min=0,max=147,step=0
  : values=44,44
  | dBminmax-min=-28.37dB,max=-0.94dB
```

Set playback volume (control name and value range vary by device; check `amixer contents` output):

```bash
amixer -c <C> cset name='PCM Playback Volume' 60,60
```

Mute / unmute:

```bash
# Mute
amixer -c <C> cset name='PCM Playback Switch' off

# Unmute
amixer -c <C> cset name='PCM Playback Switch' on
```

**Step 3 — Test playback:**

Sine-wave test tone (clearly audible on any speaker):

```bash
speaker-test -c 2 -t sine -f 1000 -l 3 -D plughw:<C>,<D>
```

Play an audio file (`plughw` handles sample rate and channel conversion automatically):

```bash
aplay -D plughw:<C>,<D> audio.wav
```

USB audio requires no device tree changes and works immediately. The 40-pin I2S interface (§14.5) is an alternative for designs that require an on-board codec.

### 12.4 USB Drive

USB storage is mounted automatically by the desktop environment. In headless mode:

```bash
# List block devices
lsblk

# Mount USB storage
mkdir -p /mnt/usb
mount /dev/sda1 /mnt/usb

# Unmount safely before removal
umount /mnt/usb
```

---

## 13. PCIe

The PCIe Gen3 FPC connector (J10) provides a high-speed expansion interface for attaching devices such as NVMe SSDs, compute accelerators, or custom PCIe peripherals via an adapter board.

Verified compatible device: **KIOXIA KEG60ZNS1T02**.

**After connecting and booting, verify detection:**

```bash
lsblk
ls /dev/nvme*
```

**Mount an existing partition:**

```bash
mkdir -p /mnt/nvme
mount /dev/nvme0n1p1 /mnt/nvme
```

**Mount automatically on boot** — add to `/etc/fstab`:

```
/dev/nvme0n1p1  /mnt/nvme  ext4  defaults  0  2
```

---

## 14. 40-pin GPIO Header

The 40-pin header (J11) follows the Raspberry Pi HAT mechanical footprint and pin numbering. For full signal assignments and ball numbers, see **HRM** [§40-pin GPIO header (J11)](MO68A_Hardware_Reference_Manual_V1.0.md#40-pin-gpio-header-j11).

> IO voltage is 3.3 V. Do not connect 5 V signals to any GPIO pin.

### 14.1 Pin Reference

| Function (odd pin)         | Pin |     | Pin | Function (even pin)   |
| --------------------------:|:---:|:---:|:---:|:--------------------- |
| 3.3 V                      | 1   |     | 2   | 5.0 V                 |
| I2C0_SDA (AE24)            | 3   |     | 4   | 5.0 V                 |
| I2C0_SCL (AH25)            | 5   |     | 6   | GND                   |
| AUDIO_CLK / GPIO0_30 (Y25) | 7   |     | 8   | UART5_TXD (W25)       |
| GND                        | 9   |     | 10  | UART5_RXD (AC24)      |
| WKUP_GPIO0_60 (E27) †      | 11  |     | 12  | I2S_CLK (AB28)        |
| GPIO0_0 (AG24)             | 13  |     | 14  | GND                   |
| WKUP_GPIO0_61 (E28) †      | 15  |     | 16  | GPIO0_27 (V26)        |
| 3.3 V                      | 17  |     | 18  | GPIO0_51 (AE27)       |
| SPI5_MOSI (R27)            | 19  |     | 20  | GND                   |
| SPI5_MISO (AD27)           | 21  |     | 22  | WKUP_GPIO0_70 (B26) † |
| SPI5_CLK (T27)             | 23  |     | 24  | SPI5_CS0 (U28)        |
| GND                        | 25  |     | 26  | SPI5_CS1 (W28)        |
| WKUP_I2C0_SDA (H27) †      | 27  |     | 28  | WKUP_I2C0_SCL (H24) † |
| GPIO0_18 (AB27)            | 29  |     | 30  | GND                   |
| GPIO0_33 (AA28)            | 31  |     | 32  | PWM / ECAP0 (AB26)    |
| PWM5_B / GPIO0_32 (U26)    | 33  |     | 34  | GND                   |
| I2S_FS (U27)               | 35  |     | 36  | GPIO0_10 (AB24)       |
| GPIO0_9 (Y28)              | 37  |     | 38  | I2S_DIN (AC28)        |
| GND                        | 39  |     | 40  | I2S_DOUT (Y26)        |

† WKUP-domain GPIO (gpiochip0); all others are main-domain GPIO (gpiochip1).

> For I2C commands and bus assignment, see §10. I2C pins on the 40-pin header: pins 3 and 5 (SOC I2C0, `/dev/i2c-1`), pins 27 and 28 (WKUP I2C0, `/dev/i2c-0`).

### 14.2 GPIO

Multiple GPIO lines are available on the 40-pin header. The board uses the Linux GPIO character device interface. Tools from the `gpiod` package (`gpiodetect`, `gpioinfo`, `gpioget`, `gpioset`) are pre-installed.

**List GPIO chips:**

```bash
gpiodetect
```

```
gpiochip0 [42110000.gpio] (89 lines)   # WKUP domain GPIO (WKUP_GPIO0_X)
gpiochip1 [600000.gpio]   (66 lines)   # Main domain GPIO0 (GPIO0_X)
gpiochip2 [0-0048]        (11 lines)   # Internal system controller (not for user access)
gpiochip3 [7inch-touchscreen-p] (2 lines)   # RPi 7-inch panel (present when panel is connected)
```

**List lines of a GPIO chip** (example: gpiochip2):

```bash
gpioinfo -c gpiochip2
```

```
gpiochip2 - 11 lines:
        line   0:       unnamed                 input
        line   1:       unnamed                 input
        line   2:       unnamed                 input
        line   3:       unnamed                 input
        line   4:       unnamed                 output
        line   5:       unnamed                 output
        line   6:       unnamed                 input
        line   7:       unnamed                 input
        line   8:       unnamed                 output
        line   9:       unnamed                 input
        line  10:       unnamed                 output
```

**Read a GPIO input** (example: GPIO0_0, pin 13):

```bash
gpioget -c gpiochip1 0
```

Output: `"0"=active` (active = high, inactive = low)

**Set a GPIO output** (example: GPIO0_0 high, then low):

```bash
gpioset -c gpiochip1 0=1
gpioset -c gpiochip1 0=0
```

> **Note:** `gpioset` blocks until the process is terminated — the GPIO line is held in the set state until you press Ctrl+C, after which it is released. Only operate lines exposed on the 40-pin header.

> **Note:** Some pins have a non-GPIO default pinmux (for example, pin 7 defaults to `AUDIO_CLK`). If `gpioset` has no effect, the pin requires a device tree overlay to switch its pinmux to GPIO mode.

**Read a WKUP-domain GPIO** (example: WKUP_GPIO0_60, pin 11):

```bash
gpioget -c gpiochip0 60
```

**40-pin GPIO line mapping:**

| Header Pin | Signal        | Chip      | Line |
|:----------:|:------------- |:--------- |:----:|
| 7          | GPIO0_30      | gpiochip1 | 30   |
| 11         | WKUP_GPIO0_60 | gpiochip0 | 60   |
| 13         | GPIO0_0       | gpiochip1 | 0    |
| 15         | WKUP_GPIO0_61 | gpiochip0 | 61   |
| 16         | GPIO0_27      | gpiochip1 | 27   |
| 18         | GPIO0_51      | gpiochip1 | 51   |
| 22         | WKUP_GPIO0_70 | gpiochip0 | 70   |
| 29         | GPIO0_18      | gpiochip1 | 18   |
| 31         | GPIO0_33      | gpiochip1 | 33   |
| 33         | GPIO0_32      | gpiochip1 | 32   |
| 36         | GPIO0_10      | gpiochip1 | 10   |
| 37         | GPIO0_9       | gpiochip1 | 9    |

### 14.3 SPI

SPI5 is available on the 40-pin header and enabled by default. The bus can be used in two ways:

- **Userspace access via `spidev`**: No overlay required. `/dev/spidev1.0` (CS0) is available immediately after boot. Sensors, ADCs, and other peripherals can be driven from userspace using standard SPI libraries (e.g., Python `spidev`).
- **Kernel-driver peripherals** (e.g., SPI displays): A device tree overlay is required to register the peripheral — specifying its `compatible` string, chip-select, and maximum clock frequency — so the kernel can bind the appropriate driver.

| Pin | Signal    | SoC Ball |
|:--- |:--------- |:-------- |
| 19  | SPI5_MOSI | R27      |
| 21  | SPI5_MISO | AD27     |
| 23  | SPI5_CLK  | T27      |
| 24  | SPI5_CS0  | U28      |
| 26  | SPI5_CS1  | W28      |

The device node is `/dev/spidev1.0` (CS0).

**Verify SPI device node:**

```bash
ls /dev/spidev*
```

**Check SPI configuration:**

```bash
spi-config -d /dev/spidev1.0 -q
```

**Loopback test** (connect pin 19 to pin 21 with a jumper wire):

```bash
echo -ne '\x55\xAA\x12\x34' | spi-pipe -d /dev/spidev1.0 -s 1000000 | xxd
```

Expected output:

```
00000000: 55aa 1234                                U..4
```

### 14.4 UART

UART5 is available on the 40-pin header, exposed as `/dev/ttyS0`, and enabled by default.

| Pin | Signal    | SoC Ball | Direction |
|:--- |:--------- |:-------- |:--------- |
| 8   | UART5_TXD | W25      | Output    |
| 10  | UART5_RXD | AC24     | Input     |

> The serial debug console (J6, UART8) uses `/dev/ttyS2`. Do not use `/dev/ttyS2` for general-purpose UART communication.

**Identifying which ttyS is which:**

```bash
# Show MMIO address for each ttyS — match against SoC datasheet or DTS reg values
cat /proc/tty/driver/serial
```

The console device can also be identified by its file permissions — it is owned by group `tty` rather than `dialout`:

```
crw------- root tty     ttyS2   ← debug console (J6), for system administration
crw-rw---- root dialout ttyS0   ← general-purpose UART (40-pin header)
```

**Loopback test:**

Short pin 8 (TXD) to pin 10 (RXD) on the 40-pin header, then:

```bash
# Configure port: 115200 baud, raw mode, no local echo
stty -F /dev/ttyS0 115200 raw -echo

# Start receiver in background
cat /dev/ttyS0 &

# Send test string — should be echoed back immediately
echo "loopback" > /dev/ttyS0

# Stop receiver: bring to foreground then press Ctrl+C
fg
```

### 14.5 I2S / Audio

The I2S interface (MCASP0) is available on the 40-pin header. Audio devices are managed through ALSA.

| Pin | Signal              | SoC Ball | Direction             |
|:--- |:------------------- |:-------- |:--------------------- |
| 12  | BCLK (MCASP0_ACLKX) | AB28     | Output (clock master) |
| 35  | LRCLK (MCASP0_AFSX) | U27      | Output (clock master) |
| 38  | DIN  (MCASP0_AXR0)  | AC28     | Input                 |
| 40  | DOUT (MCASP0_AXR1)  | Y26      | Output                |

Using I2S requires an external I2S audio codec IC wired to the 40-pin header and a device tree overlay that registers the codec and MCASP0 as an ALSA sound card. Without the overlay, `aplay -l` returns "no soundcards found".

The WM8960 Audio HAT is a supported I2S codec HAT that connects to the 40-pin header. The procedure below applies to that HAT. The clock source is the internal MCASP auxiliary clock (196.608 MHz), which divides exactly to 48 kHz family rates; 44.1 kHz playback is possible but runs approximately 4860 PPM off-rate.

**Step 1 — Load the overlay:**

Edit `/boot/uEnv.txt` and add (or uncomment) the following line (comment out any other `name_overlays` lines):

```
name_overlays=ti/k3-j721s2-panda-wm8960-audio-hat.dtbo
```

To combine with a camera overlay, list them space-separated on a single line, e.g.:

```
name_overlays=ti/k3-j721s2-panda-wm8960-audio-hat.dtbo ti/k3-j721s2-panda-csi2-imx219-mipi0.dtbo
```

Reboot after editing.

**Step 2 — Verify the sound card is registered:**

```bash
aplay -l
```

Expected output:

```
card 0: WM8960Audio [WM8960-Audio], device 0: davinci-mcasp.0-wm8960-hifi wm8960-hifi-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

The card number and device number both appear in the output (e.g. `card 0:`, `device 0:`). Use those values in all subsequent commands (shown as `<C>` and `<D>` below).

Query available mixer controls:

```bash
amixer -c <C> scontrols
```

**Step 3 — Initialize mixer controls** (the default state may produce no output):

```bash
amixer -c <C> sset 'Left Output Mixer PCM' on
amixer -c <C> sset 'Right Output Mixer PCM' on
amixer -c <C> sset Headphone 80%
amixer -c <C> sset Speaker 80%
amixer -c <C> sset Playback 80%
```

**Step 4 — Test playback:**

All playback commands use `plughw:<C>,<D>`, which enables the ALSA plug layer to handle sample-rate conversion, channel mapping, and format adaptation automatically — any audio file can be played regardless of its original sample rate.

Sine-wave test (both channels, 3 loops):

```bash
speaker-test -c 2 -t sine -f 1000 -l 3 -D plughw:<C>,<D>
```

Play an audio file:

```bash
aplay -D plughw:<C>,<D> audio.wav
```

> **Note:** If a USB audio device is also connected it will appear as a separate card. The WM8960 HAT is always card 0 when the overlay is loaded; verify with `aplay -l` if unsure.

> **Tip:** For most use cases, a USB audio device (§12.3) is simpler — plug-and-play with no hardware wiring or device tree changes required.

**Step 5 — Test capture (recording):**

> The following procedure uses the WM8960 Audio HAT as an example. Control names and gain ranges are specific to this device; other I2S codecs may differ.

**Step 5.1 — Confirm the capture device is available:**

Lists all hardware devices that support capture. If the list is empty, the sound card has not registered a capture interface.

```bash
arecord -l
```

Example output:

```
**** List of CAPTURE Hardware Devices ****
card 0: WM8960Audio [WM8960-Audio], device 0: davinci-mcasp.0-wm8960-hifi wm8960-hifi-0 [davinci-mcasp.0-wm8960-hifi wm8960-hifi-0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

**Step 5.2 — Query current capture configuration:**

Query the PGA (Programmable Gain Amplifier) gain and mute state. Confirm the output shows `[on]` (not muted) and gain is non-zero.

```bash
amixer -c <C> sget 'Capture'
```

Example output:

```
Simple mixer control 'Capture',0
  Capabilities: cvolume cswitch
  Capture channels: Front Left - Front Right
  Limits: Capture 0 - 63
  Front Left: Capture 46 [73%] [17.25dB] [on]
  Front Right: Capture 46 [73%] [17.25dB] [on]
```

Query whether the Boost amplifier output is connected to the PGA. Confirm both show `[on]` (Boost path open).

```bash
amixer -c <C> sget 'Left Input Mixer Boost'
amixer -c <C> sget 'Right Input Mixer Boost'
```

Example output:

```
Simple mixer control 'Left Input Mixer Boost',0
  Capabilities: pswitch pswitch-joined
  Playback channels: Mono
  Mono: Playback [on]
```

Query the current Boost gain value and its available range. Note the `Limits` line in the output for use in Step 5.3.

```bash
amixer -c <C> sget 'Left Input Boost Mixer LINPUT1'
amixer -c <C> sget 'Right Input Boost Mixer RINPUT1'
```

Example output:

```
Simple mixer control 'Left Input Boost Mixer LINPUT1',0
  Capabilities: volume volume-joined
  Playback channels: Mono
  Capture channels: Mono
  Limits: 0 - 3
  Mono: 1 [33%] [13.00dB]
```

**Step 5.3 — Set capture configuration:**

If Step 5.2 shows values that differ from the recommended settings, apply the following commands.

Open the Boost amplifier output path to the PGA, allowing the microphone signal to reach the ADC:

```bash
amixer -c <C> sset 'Left Input Mixer Boost' on
amixer -c <C> sset 'Right Input Mixer Boost' on
```

Set the Boost gain (range from Step 5.2: 0–3, corresponding to 0 / +13 / +20 / +29 dB). Recommended starting value: `1` (+13 dB):

```bash
amixer -c <C> sset 'Left Input Boost Mixer LINPUT1' 1
amixer -c <C> sset 'Right Input Boost Mixer RINPUT1' 1
```

Set the PGA gain for left and right channels (range from Step 5.2: 0–63, corresponding to −17 dB to +30 dB). Recommended starting value: `46` (+17 dB):

```bash
amixer -c <C> sset 'Capture' 46,46
```

Total capture gain: Boost +13 dB + PGA +17 dB = **+30 dB**. If the recording sounds distorted, reduce the gain; if it is too quiet, increase it.

**Step 5.4 — Query hardware-supported capture parameters:**

Query the formats, sample rates, and channel counts supported by the hardware. Use these values to select parameters for the recording command in Step 5.5.

```bash
arecord -D hw:<C>,<D> --dump-hw-params -d 1 /dev/null
```

Example output:

```
FORMAT:   S16_LE S32_LE
CHANNELS: [1 2]
RATE:     [8000 48000]
```

**Step 5.5 — Record:**

Record audio using parameters derived from Step 5.4:

```bash
arecord -D hw:<C>,<D> -f S16_LE -r 48000 -c 2 -d 10 rec.wav
```

| Parameter       | Value                       | Source                                                                               |
|:--------------- |:--------------------------- |:------------------------------------------------------------------------------------ |
| `-D hw:<C>,<D>` | Direct hardware access      | Card and device numbers from Step 5.1                                                |
| `-f S16_LE`     | 16-bit signed little-endian | Step 5.4: FORMAT S16_LE S32_LE                                                       |
| `-r 48000`      | 48 kHz                      | Step 5.4: RATE [8000 48000]; 48 kHz divides exactly from the 196.608 MHz MCASP clock |
| `-c 2`          | Stereo                      | Step 5.4: CHANNELS [1 2]                                                             |
| `-d 10`         | 10 seconds                  | Test duration; adjust as needed                                                      |

**Step 5.6 — Verify by playback:**

Play back the recording using the ALSA plug layer (`plughw`), which handles format and sample-rate conversion automatically. If the recorded content is audible, capture is working correctly.

```bash
aplay -D plughw:<C>,<D> rec.wav
```

### 14.6 PWM

Two PWM outputs are available on the 40-pin header:

| Pin | Signal                   | Driver                   | Device address | Channel |
|:---:|:------------------------ |:------------------------ |:--------------:|:-------:|
| 32  | ECAP0_IN_APWM_OUT (AB26) | `pwm-tiecap` (ECAP0)     | `3100000.pwm`  | 0       |
| 33  | PWM5_B / GPIO0_32 (U26)  | `pwm-ehrpwm` (EHRPWM5_B) | `3050000.pwm`  | 1       |

> `pwmchip` numbers are assigned dynamically at boot and may differ between boards. Always look up the chip by device address before use. `3010000.pwm` (EHRPWM1) is reserved for fan speed control.

Show all pwmchip-to-device mappings:

```bash
for c in /sys/class/pwm/pwmchip*; do echo "$c -> $(readlink -f $c/device)"; done
```

Look up the chip number for a specific output:

```bash
# ECAP0 (pin 32)
grep -rl 3100000 /sys/class/pwm/pwmchip*/device/uevent | grep -o 'pwmchip[0-9]*'

# EHRPWM5 (pin 33)
grep -rl 3050000 /sys/class/pwm/pwmchip*/device/uevent | grep -o 'pwmchip[0-9]*'
```

#### Pin 32 — ECAP0 APWM output

Pin 32 uses the SoC's Enhanced Capture (ECAP) module in Asymmetric PWM (APWM) output mode, channel 0:

```bash
# Look up chip number
CHIP=$(grep -rl 3100000 /sys/class/pwm/pwmchip*/device/uevent | grep -o 'pwmchip[0-9]*')

# Register channel 0 — creates the pwm0/ control directory
echo 0 > /sys/class/pwm/$CHIP/export

# Set period in nanoseconds (1 000 000 ns = 1 kHz)
echo 1000000 > /sys/class/pwm/$CHIP/pwm0/period

# Set duty cycle in nanoseconds (500 000 ns = 50%)
echo 500000 > /sys/class/pwm/$CHIP/pwm0/duty_cycle

# Start output
echo 1 > /sys/class/pwm/$CHIP/pwm0/enable
```

To stop the output:

```bash
CHIP=$(grep -rl 3100000 /sys/class/pwm/pwmchip*/device/uevent | grep -o 'pwmchip[0-9]*')

# Stop output
echo 0 > /sys/class/pwm/$CHIP/pwm0/enable

# Release channel 0 — removes the pwm0/ directory
echo 0 > /sys/class/pwm/$CHIP/unexport
```

#### Pin 33 — EHRPWM5_B output

Pin 33 uses EHRPWM5 channel B, channel 1:

```bash
# Look up chip number
CHIP=$(grep -rl 3050000 /sys/class/pwm/pwmchip*/device/uevent | grep -o 'pwmchip[0-9]*')

# Register channel 1 (B) — creates the pwm1/ control directory
echo 1 > /sys/class/pwm/$CHIP/export

# Set period in nanoseconds (1 000 000 ns = 1 kHz)
echo 1000000 > /sys/class/pwm/$CHIP/pwm1/period

# Set duty cycle in nanoseconds (500 000 ns = 50%)
echo 500000 > /sys/class/pwm/$CHIP/pwm1/duty_cycle

# Start output
echo 1 > /sys/class/pwm/$CHIP/pwm1/enable
```

To stop the output:

```bash
CHIP=$(grep -rl 3050000 /sys/class/pwm/pwmchip*/device/uevent | grep -o 'pwmchip[0-9]*')

# Stop output
echo 0 > /sys/class/pwm/$CHIP/pwm1/enable

# Release channel 1 (B) — removes the pwm1/ directory
echo 1 > /sys/class/pwm/$CHIP/unexport
```

---

## 15. MIPI FPC Ports

### 15.1 Overview

J24 (MIPI0) and J25 (MIPI1) are 22-pin FPC connectors with a MIPI D-PHY interface. Each port can be configured as either CSI-2 camera input or DSI display output via device tree overlay — but not both simultaneously on the same port.

Verified compatible devices:

- **Camera:** Sony IMX219 (e.g., Raspberry Pi Camera Module 2)
- **Display:** Raspberry Pi 7-inch DSI panel (J24 only; see §16)

### 15.2 Configuration

Mode selection is controlled by the `name_overlays` line in `/boot/uEnv.txt`. Three scenarios are supported:

| Scenario | J24 (MIPI0) | J25 (MIPI1) | `name_overlays`                                                                         |
|:-------- |:----------- |:----------- |:--------------------------------------------------------------------------------------- |
| A        | CSI camera  | —           | `ti/k3-j721s2-panda-csi2-imx219-mipi0.dtbo`                                             |
| B        | —           | CSI camera  | `ti/k3-j721s2-panda-csi2-imx219-mipi1.dtbo`                                             |
| C        | DSI display | CSI camera  | `ti/k3-j721s2-panda-dsi-rpi-7inch-panel.dtbo ti/k3-j721s2-panda-csi2-imx219-mipi1.dtbo` |

`name_overlays` rules:

- Each value is a path to a `.dtbo` file relative to `/boot/dtb/`

- Only the last uncommented `name_overlays` line takes effect — comment out all others

- To load multiple overlays, list them space-separated on a single `name_overlays` line, e.g. Scenario C:
  
  ```
  name_overlays=ti/k3-j721s2-panda-dsi-rpi-7inch-panel.dtbo ti/k3-j721s2-panda-csi2-imx219-mipi1.dtbo
  ```

---

## 16. MIPI DSI Display

J24 (MIPI0) supports DSI display output. For overlay configuration see §15.2; for combined DSI + camera use see §17.3 (Scenario C).

> J25 (MIPI1) DSI support is not currently available.

> **Warning:** The DSI panel must be physically connected to J24 before boot. If the panel is absent, the DSS display subsystem fails to initialize and Mini DisplayPort (J9) will also be unavailable.

---

## 17. Camera Input

For port hardware overview and overlay configuration rules, see §15.

### 17.1 Scenario A — J24 Camera

Edit `/boot/uEnv.txt` and uncomment the following line (comment out any other `name_overlays` lines):

```
name_overlays=ti/k3-j721s2-panda-csi2-imx219-mipi0.dtbo
```

Connect the IMX219 to J24 and verify detection:

```bash
v4l2-ctl --list-devices
```

**Configure sensor parameters:**

```bash
v4l2-ctl -d /dev/v4l-subdev0 --set-ctrl=analogue_gain=200
v4l2-ctl -d /dev/v4l-subdev0 --set-ctrl=exposure=3000
```

**Configure the media pipeline:**

```bash
media-ctl -d /dev/media0 -V '"imx219 5-0010":0 [fmt:SRGGB8_1X8/1920x1080]'
media-ctl -d /dev/media0 -V '"cdns_csi2rx.4500000.csi-bridge":0 [fmt:SRGGB8_1X8/1920x1080]'
media-ctl -d /dev/media0 -V '"cdns_csi2rx.4500000.csi-bridge":1 [fmt:SRGGB8_1X8/1920x1080]'
media-ctl -d /dev/media0 -V '"4504000.ticsi2rx":0 [fmt:SRGGB8_1X8/1920x1080]'
```

**Capture a JPEG frame:**

```bash
gst-launch-1.0 v4l2src device=/dev/video0 num-buffers=1 \
  ! "video/x-bayer,width=1920,height=1080,format=rggb,framerate=30/1" \
  ! bayer2rgb ! videoconvert ! jpegenc ! filesink location=cam.jpg
```

### 17.2 Scenario B — J25 Camera

Edit `/boot/uEnv.txt` and uncomment the following line (comment out any other `name_overlays` lines):

```
name_overlays=ti/k3-j721s2-panda-csi2-imx219-mipi1.dtbo
```

Connect the IMX219 to J25 and verify detection:

```bash
v4l2-ctl --list-devices
```

**Configure sensor parameters:**

```bash
v4l2-ctl -d /dev/v4l-subdev2 --set-ctrl=analogue_gain=200
v4l2-ctl -d /dev/v4l-subdev2 --set-ctrl=exposure=3000
```

**Configure the media pipeline:**

```bash
media-ctl -d /dev/media0 -V '"imx219 3-0010":0 [fmt:SRGGB8_1X8/1920x1080]'
media-ctl -d /dev/media0 -V '"cdns_csi2rx.4514000.csi-bridge":0 [fmt:SRGGB8_1X8/1920x1080]'
media-ctl -d /dev/media0 -V '"cdns_csi2rx.4514000.csi-bridge":1 [fmt:SRGGB8_1X8/1920x1080]'
media-ctl -d /dev/media0 -V '"4510000.ticsi2rx":0 [fmt:SRGGB8_1X8/1920x1080]'
```

**Capture a JPEG frame:**

```bash
gst-launch-1.0 v4l2src device=/dev/video2 num-buffers=1 \
  ! "video/x-bayer,width=1920,height=1080,format=rggb,framerate=30/1" \
  ! bayer2rgb ! videoconvert ! jpegenc ! filesink location=cam.jpg
```

### 17.3 Scenario C — J24 DSI Display + J25 Camera

Edit `/boot/uEnv.txt` and uncomment the following line (comment out any other `name_overlays` lines):

```
name_overlays=ti/k3-j721s2-panda-dsi-rpi-7inch-panel.dtbo ti/k3-j721s2-panda-csi2-imx219-mipi1.dtbo
```

For DSI display setup refer to §16. For camera capture commands refer to §17.2.

> **Warning:** The DSI panel must be physically connected to J24 before boot. If the panel is absent, the DSS display subsystem fails to initialize and Mini DisplayPort (J9) will also be unavailable.

---

## 18. AI Inference Acceleration

The TDA4VE / AM68A SoC includes an 8 TOPS Matrix Multiply Accelerator (MMA). TI provides the TIDL (TI Deep Learning) runtime and model inference tools as part of the Edge AI SDK.

> **Note:** AI inference toolchain documentation and usage examples will be added in a future revision of this guide. Refer to the TI Edge AI documentation and EdgeAI-Studio resources for current information.

Key components:

- **MMA (Matrix Multiply Accelerator)**: 8 TOPS, supports INT8 quantized inference
- **C7x DSP cores**: used for pre/post processing in TIDL pipelines
- **R5F MCU cores**: real-time control and sensor management
- **TIDL runtime**: model conversion, inference API, GStreamer integration

---

## 19. Troubleshooting

### 19.1 Board Does Not Boot

- Confirm the SD card is fully inserted into J23 (it clicks into place).
- Re-flash the image using Armbian Imager and wait for *Write Successful* before ejecting.
- On first boot, the system expands the filesystem and reboots automatically — allow 3–4 minutes total.
- LED indicator: red = powered, OS not running; solid green = OS running.

### 19.2 No Serial Console Output

- Verify the adapter is connected to J6, not J5 (USB-C power).
- Use a **3.3 V logic** USB-to-UART adapter — 5 V signals will damage the board.
- Settings: **115200 baud, 8N1, no flow control**.
- The debug console is on `/dev/ttyS2` (UART8).
- Open the serial terminal **before** applying power to capture the full boot log.

### 19.3 No Network

- Confirm the RJ45 cable is connected to J1 (Ethernet port).
- Check link LED on the Ethernet port.
- Verify interface state: `nmcli device status`
- Check assigned IP: `ip addr show eth0`

### 19.4 NVMe Not Detected

- Confirm the FPC cable is fully seated at J10 and the NVMe adapter.
- Check kernel messages: `dmesg | grep -i nvme`
- List PCI devices: `lspci`

### 19.5 Display No Signal

- Use a monitor with native DisplayPort input. Passive Mini DP to HDMI adapters do not work.
- Confirm the cable is firmly seated in J9.
- Check DRM status: `cat /sys/class/drm/card*/card*-DP-*/status`

---

## Appendix A — Quick Specification Reference

| Item        | Value                                           |
|:----------- |:----------------------------------------------- |
| SoC         | TDA4VE / AM68A (J721S2)                         |
| CPU         | 2× Cortex-A72, up to 2.0 GHz                    |
| AI          | 8 TOPS                                          |
| RAM         | 8 GB LPDDR4                                     |
| Storage     | Micro SD (boot + rootfs); PCIe NVMe (expansion) |
| OS          | Armbian (Debian 13 Trixie)                      |
| Network     | Gigabit Ethernet (eth0), DHCP by default        |
| USB         | 4× USB 3.0 (TUSB8041 hub)                       |
| Display     | Mini DisplayPort (J9)                           |
| Camera      | 2× MIPI CSI-2 / DSI FPC (J24, J25)              |
| GPIO header | 40-pin, RPi HAT compatible, 3.3 V IO            |
| Debug UART  | J6, /dev/ttyS2, 115200 8N1                      |
| Power       | USB-C (J5), 5 V / 5 A                           |

## Appendix B — Related Documents and Resources

| Document / Resource | Description |
| --- | --- |
| [MO68A Quick Start Guide](MO68A_Quick_Start_Guide_V1.0.md) | Initial setup, flashing, first login |
| [MO68A Hardware Reference Manual](MO68A_Hardware_Reference_Manual_V1.0.md) | Connector pinouts, signal assignments, electrical specifications |

---

## Revision History

| Version | Date       | Description     |
|:------- |:---------- |:--------------- |
| 1.0     | 2026-04-28 | Initial release |
