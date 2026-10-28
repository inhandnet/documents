MO-62A 单板计算机 SDK，基于 TI AM62A7 平台，提供高达 2 TOPS AI 推理性能。

---

## 目录
+ [1. 概述](#1-概述)
+ [2. 环境搭建](#2-环境搭建)
    - [2.1 主机系统要求](#21-主机系统要求)
    - [2.2 克隆仓库](#22-克隆仓库)
    - [2.3 使用 setup.sh 初始化环境](#23-使用-setupsh-初始化环境)
    - [2.4 工具链](#24-工具链)
+ [3. U-Boot](#3-u-boot)
    - [3.1 相关文件](#31-相关文件)
    - [3.2 编译 U-Boot](#32-编译-u-boot)
    - [3.3 归档编译产物](#33-归档编译产物)
    - [3.4 编译输出](#34-编译输出)
+ [4. Linux 内核](#4-linux-内核)
    - [4.1 相关文件](#41-相关文件)
    - [4.2 编译 DTB](#42-编译-dtb)
    - [4.3 编译内核](#43-编译内核)
    - [4.4 归档编译产物](#44-归档编译产物)
    - [4.5 编译输出](#45-编译输出)
+ [5. 烧录 SD 卡](#5-烧录-sd-卡)
    - [5.1 前提条件](#51-前提条件)
    - [5.2 启动烧录工具](#52-启动烧录工具)
    - [5.3 在线烧录（直接写入 SD 卡）](#53-在线烧录直接写入-sd-卡)
    - [5.4 离线镜像制作（balenaEtcher）](#54-离线镜像制作balenaetcher)
    - [5.5 自定义 Rootfs 压缩包（添加 apt 软件包）](#55-自定义-rootfs-压缩包添加-apt-软件包)
+ [6. 分区布局](#6-分区布局)
    - [6.1 BOOT 分区内容](#61-boot-分区内容)
    - [6.2 启动配置](#62-启动配置)
+ [7. 硬件参考](#7-硬件参考)
    - [7.1 整体框图](#71-整体框图)
    - [7.2 供电系统](#72-供电系统)
    - [7.3 I2C 设备地址映射](#73-i2c-设备地址映射)
    - [7.4 内存](#74-内存)
    - [7.5 存储](#75-存储)
    - [7.6 显示——Micro HDMI](#76-显示micro-hdmi)
    - [7.7 网络——千兆以太网](#77-网络千兆以太网)
    - [7.8 USB](#78-usb)
    - [7.9 无线——Wi-Fi / 蓝牙](#79-无线wi-fi--蓝牙)
    - [7.10 音频](#710-音频)
    - [7.11 RTC](#711-rtc)
    - [7.12 扩展接口](#712-扩展接口)
    - [7.13 调试接口](#713-调试接口)
    - [7.14 启动配置](#714-启动配置)
    - [7.15 JTAG 接口](#715-jtag-接口)
    - [7.16 硬件版本识别引脚](#716-硬件版本识别引脚)

---

## 1. 概述
MO-62A 是一款基于 TI AM62A7 处理器的单板计算机，专为边缘 AI 推理、机器视觉和工业控制应用设计。AM62A7 集成了四核 Arm Cortex-A53（最高 1.4 GHz）、一个 Cortex-R5F 实时处理器，以及专用 MMA（矩阵乘法加速器），AI 推理性能高达 2 TOPS。

本 SDK 基于 **TI Processor SDK Linux RT EdgeAI AM62A EVM 11.01.07.05** 构建，为 MO-62A 板卡提供完整的硬件定制支持，包含以下组件：

+ **U-Boot**：为 MO-62A 定制的引导加载程序，包含 R5 SPL 和 A53 U-Boot
+ **Linux 内核**：基于 TI Linux RT 内核，为 MO-62A 定制的内核和设备树
+ **构建系统**：统一的基于 Makefile 的编译与归档工作流
+ **烧录工具**：支持直接写入 SD 卡和创建离线 balenaEtcher 镜像

SDK 目录结构概览：

```plain
mo-62a/
├── board-support/          # U-Boot、内核源码及预编译镜像
│   ├── built-images/       # 归档编译产物（归档后生成）
│   ├── prebuilt-images/    # TI 预编译固件（bl31、bl32、ti-dm 等）
│   └── extra-applications/ # 板卡专用附加应用
├── bin/                    # 辅助脚本及烧录工具
│   ├── mo-62a-flash.sh     # 统一烧录工具
│   └── extlinux/           # U-Boot extlinux 启动配置
├── filesystem/             # rootfs 压缩包目录
├── linux-devkit/           # AArch64 交叉编译工具链
├── k3r5-devkit/            # ARMv7 R5 交叉编译工具链
├── makerules/              # 各组件 Makefile 规则
├── Makefile                # 顶层 Makefile
├── Rules.make              # 全局路径与平台配置
└── setup.sh                # 开发主机初始化脚本
```

---

## 2. 环境搭建
### 2.1 主机系统要求
以下主机环境已经过编译验证：

| 项目 | 要求 |
| --- | --- |
| 操作系统 | Ubuntu 22.04 LTS（x86_64） |
| 内核版本 | 6.8.0 或更高 |
| 架构 | x86_64 |


所需主机软件包：

```bash
sudo apt-get install \
  xinetd tftpd nfs-kernel-server minicom \
  build-essential libncurses5-dev autoconf automake \
  dos2unix screen lrzsz lzop flex libssl-dev \
  u-boot-tools make git parted dosfstools e2fsprogs \
  pv xz-utils zip wget curl
```

### 2.2 克隆仓库
将 MO-62A SDK 克隆到主机任意目录：

```bash
git clone https://github.com/inhandnet/mo-62a.git
cd mo-62a
```

### 2.3 使用 setup.sh 初始化环境
在 SDK 根目录执行 `setup.sh` 以初始化开发主机：

```bash
./setup.sh
```

该脚本执行以下步骤：

1. **验证**主机操作系统（Ubuntu 22.04 LTS）
2. **将**当前用户添加到 `dialout` 组（串口访问所需）
3. **安装**所需主机软件包——按 `Y` 安装，按 `n` 跳过（如已安装）
4. **写入** `TI_SDK_PATH` 到 `~/.bashrc`，指向克隆的仓库根目录，确保该变量在 shell 会话间持久有效
5. **创建**符号链接 `/opt/ti-processor-sdk-linux-rt-edgeai-am62a-evm-11.01.07.05` 指向克隆的仓库，这是因为交叉编译工具链二进制文件中硬编码了该路径作为 ELF 解释器路径

示例输出：

```plain
-------------------------------------------------------------------------------
MO-62A SDK setup script
SDK root: /home/user/mo-62a
-------------------------------------------------------------------------------

Verifying Linux host distribution
Ubuntu 22.04 LTS is being used, continuing..

User 'user' is already in the 'dialout' group.

Do you wish to install required host packages? (Y/n) n
Host package installation skipped.

TI_SDK_PATH is already set correctly in /home/user/.bashrc:
  export TI_SDK_PATH="/home/user/mo-62a"
TI_SDK_PATH is now set to: /home/user/mo-62a

Creating toolchain symlink...
  /opt/ti-processor-sdk-linux-rt-edgeai-am62a-evm-11.01.07.05 -> /home/user/mo-62a

-------------------------------------------------------------------------------
MO-62A SDK setup completed!
You can now build the SDK from: /home/user/mo-62a
-------------------------------------------------------------------------------
```

> **注意：** `setup.sh` 完成后，`TI_SDK_PATH` 在当前 shell 中立即生效，并通过 `~/.bashrc` 在所有后续 shell 会话中自动设置。重复执行 `setup.sh` 是安全的——脚本会更新符号链接和 `TI_SDK_PATH` 条目，不会产生重复项。
>

### 2.4 工具链
SDK 包含两套交叉编译工具链：

**AArch64 工具链**——用于 Linux 内核和 A53 U-Boot：

| 项目 | 值 |
| --- | --- |
| 路径 | `linux-devkit/sysroots/x86_64-arago-linux/usr/bin/aarch64-oe-linux/` |
| 前缀 | `aarch64-oe-linux-` |
| GCC 版本 | 13.4.0 |
| 目标 sysroot | `linux-devkit/sysroots/aarch64-oe-linux/` |


**ARMv7 R5 工具链**——用于 R5 SPL（tiboot3）：

| 项目 | 值 |
| --- | --- |
| 路径 | `k3r5-devkit/sysroots/x86_64-arago-linux/usr/bin/arm-oe-eabi/` |
| 前缀 | `arm-oe-eabi-` |
| GCC 版本 | 13.4.0 |
| 目标 sysroot | `k3r5-devkit/sysroots/armv7at2hf-vfp-oe-eabi/` |


验证两套工具链均可用（执行 `setup.sh` 完成后运行）：

```bash
# AArch64
linux-devkit/sysroots/x86_64-arago-linux/usr/bin/aarch64-oe-linux/aarch64-oe-linux-gcc --version

# ARMv7 R5
k3r5-devkit/sysroots/x86_64-arago-linux/usr/bin/arm-oe-eabi/arm-oe-eabi-gcc --version
```

预期输出：

```plain
aarch64-oe-linux-gcc (GCC) 13.4.0
Copyright (C) 2023 Free Software Foundation, Inc.

arm-oe-eabi-gcc (GCC) 13.4.0
Copyright (C) 2023 Free Software Foundation, Inc.
```

> **注意：** 工具链二进制文件中硬编码了 ELF 解释器路径 `/opt/ti-processor-sdk-linux-rt-edgeai-am62a-evm-11.01.07.05/`。`setup.sh` 创建的符号链接可满足此要求，无论仓库克隆到何处。工具链通过 `Rules.make` 自动调用，无需手动导出 PATH。
>

---

## 3. U-Boot
### 3.1 相关文件
添加到 U-Boot 源码树中的 MO-62A 专用文件：

| 文件 | 描述 |
| --- | --- |
| `board-support/ti-u-boot-2025.01+git/configs/am62ax_mo_62a_a53_defconfig` | A53 U-Boot defconfig |
| `board-support/ti-u-boot-2025.01+git/configs/am62ax_mo_62a_r5_defconfig` | R5 SPL defconfig |
| `board-support/ti-u-boot-2025.01+git/dts/upstream/src/arm64/ti/k3-am62a7-mo-62a.dts` | A53 主设备树 |
| `board-support/ti-u-boot-2025.01+git/dts/upstream/src/arm64/ti/k3-am62a7-mo-62a-pinmux.dtsi` | 引脚复用配置 |
| `board-support/ti-u-boot-2025.01+git/arch/arm/dts/k3-am62a7-r5-mo-62a.dts` | R5 SPL 设备树 |
| `board-support/ti-u-boot-2025.01+git/arch/arm/dts/k3-am62a7-mo-62a-u-boot.dtsi` | U-Boot 专用 DT 扩展 |
| `board-support/ti-u-boot-2025.01+git/arch/arm/dts/k3-am62a7-mo-62a-binman.dtsi` | Binman 打包配置 |
| `board-support/ti-u-boot-2025.01+git/arch/arm/dts/k3-am62a7-mo-62a-lp4-4GB.dtsi` | LPDDR4 4GB 内存配置 |


编译期间所需的预编译固件（来自 TI，未修改）：

| 文件 | 描述 |
| --- | --- |
| `board-support/prebuilt-images/am62a-evm/bl31.bin` | Arm Trusted Firmware（TF-A） |
| `board-support/prebuilt-images/am62a-evm/bl32.bin` | OP-TEE OS |
| `board-support/prebuilt-images/am62a-evm/ti-dm/am62axx/dm_edgeai_mcu1_0_release_strip.out` | TI 设备管理器固件 |


### 3.2 编译 U-Boot
U-Boot 分两步编译——先编译 R5 SPL，再编译 A53 U-Boot。两者均通过 SDK 根目录的顶层 `make` 调用。

**编译 R5 SPL（tiboot3）：**

```bash
make u-boot-r5
```

使用 `am62ax_mo_62a_r5_defconfig` 配置 R5 编译，并使用 ARMv7 R5 工具链（`arm-oe-eabi-`）进行编译。输出位于 `board-support/u-boot-build/r5/`。

**编译 A53 U-Boot：**

```bash
make u-boot-a53
```

使用 `am62ax_mo_62a_a53_defconfig` 配置 A53 编译，并使用 AArch64 工具链（`aarch64-oe-linux-`），通过 binman 集成 `bl31.bin`、`bl32.bin` 和 TI 设备管理器固件。输出位于 `board-support/u-boot-build/a53/`。

**一步编译两者：**

```bash
make u-boot
```

### 3.3 归档编译产物
编译成功后，将输出二进制文件复制到 `board-support/built-images/`：

```bash
make u-boot_stage
```

### 3.4 编译输出
归档完成后，`board-support/built-images/` 中包含以下文件：

| 文件 | 大小 | 来源 | 描述 |
| --- | --- | --- | --- |
| `tiboot3-am62ax-gp-mo-62a.bin` | ~318 KB | R5 编译 | 适用于 GP（通用）设备的 R5 SPL |
| `tiboot3-am62ax-hs-fs-mo-62a.bin` | ~320 KB | R5 编译 | 适用于 HS-FS（高安全、可量产）设备的 R5 SPL |
| `tiboot3-am62ax-hs-mo-62a.bin` | ~320 KB | R5 编译 | 适用于 HS（高安全）设备的 R5 SPL |
| `tiboot3.bin` | ~320 KB | R5 编译 | 默认 tiboot3（HS-FS，烧录工具使用） |
| `tispl.bin` | ~1.7 MB | A53 编译 | TI SPL——加载 OP-TEE、TF-A 和 A53 U-Boot |
| `u-boot.img` | ~1.2 MB | A53 编译 | A53 U-Boot FIT 镜像 |


> **注意：** 具体使用哪个 `tiboot3-*.bin` 变体取决于设备安全状态。大多数量产 MO-62A 板卡出厂为 HS-FS，使用 `tiboot3-am62ax-hs-fs-mo-62a.bin`。烧录工具默认使用 `tiboot3.bin`（即 HS-FS 变体的副本）。
>

---

## 4. Linux 内核
### 4.1 相关文件
添加到 Linux 内核源码树中的 MO-62A 专用文件：

| 文件 | 描述 |
| --- | --- |
| `board-support/ti-linux-kernel-6.12.35+git-ti-rt/arch/arm64/configs/am62ax_mo_62a_defconfig` | MO-62A 基础内核 defconfig |
| `board-support/ti-linux-kernel-6.12.35+git-ti-rt/arch/arm64/boot/dts/ti/k3-am62a7-mo-62a.dts` | MO-62A 主设备树 |
| `board-support/ti-linux-kernel-6.12.35+git-ti-rt/arch/arm64/boot/dts/ti/k3-am62a7-mo-62a-pinmux.dtsi` | 引脚复用配置 |


编译时在 defconfig 基础上叠加应用的内核配置片段：

| 片段 | 位置 | 用途 |
| --- | --- | --- |
| `ti_arm64_prune.config` | `kernel/configs/` | 移除非 TI ARM64 平台支持，减小编译体积 |
| `ti_rt.config` | `kernel/configs/` | 启用 PREEMPT_RT 实时内核补丁 |


### 4.2 编译 DTB
编译所有设备树 blob（共 62 个 DTB 和 DTBO）：

```bash
make linux-dtbs
```

该命令使用 `am62ax_mo_62a_defconfig` + `ti_arm64_prune.config` + `ti_rt.config` 配置内核，然后编译所有匹配 `Rules.make` 中定义前缀模式的 DTB：

```plain
ti/k3-am62a7  ti/k3-fpdlink  ti/k3-am62x-sk  ti/k3-v3link
```

输出位于 `board-support/ti-linux-kernel-6.12.35+git-ti-rt/arch/arm64/boot/dts/`。

### 4.3 编译内核
编译内核镜像、模块和 FitImage：

```bash
make linux
```

该命令按顺序执行以下步骤：

1. 编译 DTB（自动调用 `linux-dtbs`）
2. 编译 U-Boot（自动调用 `u-boot`，FitImage 签名密钥所需）
3. 编译 `Image` 和 `Image.gz`
4. 编译内核模块
5. 使用 `mkimage` 和 U-Boot 签名密钥，结合 `board-support/prebuilt-images/am62a-evm/` 中的 ITS 模板，打包并签名 `fitImage`
6. 重新编译 A53 U-Boot（binman），将 MO-62A DTB 嵌入 `tispl.bin`

### 4.4 归档编译产物
将内核和 DTB 输出复制到 `board-support/built-images/`：

```bash
make linux_stage
```

### 4.5 编译输出
归档完成后，`board-support/built-images/` 中新增以下文件：

| 文件 | 大小 | 描述 |
| --- | --- | --- |
| `Image` | ~18 MB | 未压缩内核镜像 |
| `Image.gz` | ~7.0 MB | 压缩内核镜像 |
| `fitImage` | ~7.3 MB | 签名 FIT 镜像（内核 + DTB），用于验证启动 |
| `dtb/ti/*.dtb` / `dtb/ti/*.dtbo` | — | 62 个设备树 blob 和覆盖层 |


> **注意：** `fitImage` 使用 U-Boot 源码树中的 `custMpk` 密钥签名。签名步骤同时触发 `tispl.bin` 的重新编译，使其嵌入 MO-62A DTB（`k3-am62a7-mo-62a.dtb`）。因此，`make linux` 始终会同时更新 `built-images/` 中的 `fitImage` 和 `tispl.bin`。
>

---

## 5. 烧录 SD 卡
统一烧录工具 `bin/mo-62a-flash.sh` 支持两种输出目标：

+ **在线烧录**——直接写入物理 SD 卡
+ **离线镜像制作**——创建 `.img` 文件供 balenaEtcher 使用

两种模式产生完全相同的分区布局和内容。

### 5.1 前提条件
所需主机软件包（由 `setup.sh` 安装）：

```plain
parted  dosfstools  e2fsprogs  pv  xz-utils  zip  wget  curl
```

运行烧录工具前，请确认以下条件：

1. **编译产物已归档**——执行 `make u-boot_stage` 和 `make linux_stage`（或 `make all_stage`），确保 `board-support/built-images/` 中包含所需文件
2. **Rootfs 压缩包已就位**——将 `.tar.xz` 或 `.tar.gz` 格式的 rootfs 压缩包放置在 `filesystem/` 目录下
3. **SD 卡已插入**（仅在线模式）——工具自动检测 `/dev/sdX` 和 `/dev/mmcblkN` 块设备

### 5.2 启动烧录工具
烧录工具为交互式，须以 root 权限运行：

```bash
sudo bash bin/mo-62a-flash.sh
```

启动后提示选择输出目标：

```plain
=== MO-62A Flash Tool ===

Select output target:
  [1] Write directly to an SD card
  [2] Create offline image for balenaEtcher

Select target [1/2]:
```

### 5.3 在线烧录（直接写入 SD 卡）
选择 `[1]` 进入在线模式。工具将列出所有检测到的块设备：

```plain
Detected candidate block devices:
  [1] /dev/sda  29.7G  SD Card Reader

Select target device number:
```

然后选择操作模式：

```plain
Select operation mode:
  [1] full      - create partitions + format + copy BOOT + extract rootfs
  [2] partition - create partitions + format only
  [3] boot      - copy BOOT content only (strict checks, no repartition)
  [4] rootfs    - copy rootfs content only (strict checks, no repartition)

Select mode number (default 1):
```

| 模式 | 描述 |
| --- | --- |
| `full` | 全量写入：擦除并重新分区、格式化、复制启动文件、解压 rootfs、安装内核模块 |
| `partition` | 仅分区：擦除并重建 MBR、格式化分区——不写入任何内容 |
| `boot` | 仅覆盖 BOOT 分区——重新烧录引导程序和内核，不影响 rootfs |
| `rootfs` | 仅覆盖 rootfs 分区——重新解压 rootfs，不影响 BOOT 分区 |


全新 SD 卡请选择 `full`。工具将要求确认（输入 `YES` 继续），然后自动执行：

1. 卸载目标设备上的所有现有分区
2. 擦除旧分区表
3. 创建 MBR 分区表：BOOT（FAT32，256 MiB）+ rootfs（ext4，剩余空间）
4. 格式化两个分区
5. 将启动产物复制到 BOOT 分区：`tiboot3.bin`、`tispl.bin`、`u-boot.img`、`Image`、DTB、`extlinux/`
6. 询问使用哪个 rootfs 压缩包（若 `filesystem/` 下有多个）
7. 将 rootfs 压缩包解压到 rootfs 分区
8. 安装内核模块（`make modules_install`）到 rootfs
9. 编译并安装 `board-support/extra-applications/` 中的外部应用

示例会话（full 模式）：

```plain
TARGET DEVICE: /dev/sda (29.7G)

MODE: full
This will ERASE ALL DATA on /dev/sda.

Destructive operation — please confirm.
Type YES to continue: YES

Checking mounts on /dev/sda ...
Wiping old partition table signatures...
Creating MBR partitions (BOOT FAT32(LBA) 256MiB + rootfs ext4 remaining)...
Formatting BOOT: /dev/sda1 (FAT32)
Formatting rootfs: /dev/sda2 (ext4)
Copying boot artifacts to BOOT partition...

Available rootfs tarballs:
  [1] debian-13.2-xfce-v6.12-arm64-2026-01-13-12gb.tar.xz

Select rootfs tarball number (or 'q' to abort): 1

Extracting rootfs to rootfs partition...
Installing kernel modules into rootfs: /tmp/mo-62a-rootfs.xxx/usr/lib/modules
...
Installed: rtk_hciattach

Done. BOOT and rootfs written successfully.
```

烧录完成后，将 SD 卡插入 MO-62A 板卡并上电。启动日志通过串口控制台 `ttyS2`（115200 8N1）输出。

### 5.4 离线镜像制作（balenaEtcher）
选择 `[2]` 进入镜像制作模式。工具提示输入镜像参数：

```plain
Available rootfs tarballs:
  [1] debian-13.2-xfce-v6.12-arm64-2026-01-13-12gb.tar.xz

Select rootfs tarball number (or 'q' to abort): 1

Output directory (default: bin/out): /path/to/output
Output image base name (default: mo-62a): mo-62a
Image size (GiB, integer) (default: 8): 8
Compression (zip|xz|none) (default: zip): zip
```

| 参数 | 描述 |
| --- | --- |
| 输出目录 | `.img` 及校验文件的写入路径 |
| 镜像基础名称 | 文件名前缀；输出为 `<name>.img`（及 `<name>.img.zip` 等） |
| 镜像大小（GiB） | 总镜像大小，须足以容纳 rootfs；默认 8 GiB 足够当前默认 rootfs |
| 压缩格式 | `zip`（推荐，balenaEtcher 支持）、`xz`（更小、更慢）、`none`（不压缩） |


工具将创建一个稀疏 `.img` 文件，通过 loopback 设备分区和格式化，填入与在线模式完全相同的内容，卸载 loop 设备后压缩输出。

输出文件：

```plain
/path/to/output/
├── mo-62a.img         # 原始磁盘镜像（8 GiB 稀疏文件）
├── mo-62a.img.zip     # 压缩镜像（compression=zip 时生成），供 balenaEtcher 使用
└── mo-62a.sha256      # 所有镜像文件的 SHA-256 校验值
```

使用 balenaEtcher 烧录镜像：

1. 打开 [balenaEtcher](https://etcher.balena.io/)
2. 点击 **Flash from file**，选择 `mo-62a.img.zip`（balenaEtcher 支持直接使用压缩镜像）
3. 选择目标 SD 卡
4. 点击 **Flash**

> **注意：** 镜像大小须至少与解压后的 rootfs 相同。默认 8 GiB 足够当前提供的 Debian rootfs（解压后约 6.9 GiB）。使用自定义 rootfs 时，请相应调整大小。
>

### 5.5 自定义 Rootfs 压缩包（添加 apt 软件包）
烧录工具直接解压 rootfs 压缩包。额外的 Debian 软件包（如 `imx219-preview.sh` 所需的 `frei0r-plugins`）必须**在烧录前**预先安装到压缩包中，确保在线和离线烧录后均可立即使用，无需目标机网络访问。

标准工作流程如下：

1. **在主机上安装前置工具**（一次性，x86-64 Ubuntu/Debian）：

```bash
sudo apt-get install -y qemu-user-static binfmt-support
sudo systemctl restart systemd-binfmt || sudo update-binfmts --enable
```

2. **将压缩包解压**到临时目录：

```bash
ROOTFS_DIR=/tmp/mo-62a-rootfs
mkdir -p "$ROOTFS_DIR"
sudo tar -xpf filesystem/debian-13.2-xfce-v6.12-arm64-2026-01-13-12gb.tar.xz \
    -C "$ROOTFS_DIR"
```

3. **将 qemu 二进制文件**复制到解压的 rootfs：

```bash
sudo cp /usr/bin/qemu-aarch64-static "$ROOTFS_DIR/usr/bin/"
```

4. **挂载伪文件系统**并进入 chroot：

```bash
sudo mount --bind /proc    "$ROOTFS_DIR/proc"
sudo mount --bind /sys     "$ROOTFS_DIR/sys"
sudo mount --bind /dev     "$ROOTFS_DIR/dev"
sudo mount --bind /dev/pts "$ROOTFS_DIR/dev/pts"
sudo chroot "$ROOTFS_DIR" /bin/bash
```

5. **在 chroot 内**安装所需软件包：

```bash
apt-get update
apt-get install -y frei0r-plugins
apt-get clean
exit
```

6. **清理**绑定挂载和 qemu 二进制文件：

```bash
sudo umount "$ROOTFS_DIR/dev/pts"
sudo umount "$ROOTFS_DIR/dev"
sudo umount "$ROOTFS_DIR/sys"
sudo umount "$ROOTFS_DIR/proc"
sudo rm -f  "$ROOTFS_DIR/usr/bin/qemu-aarch64-static"
```

7. **重新打包**压缩包：

```bash
TARBALL=filesystem/debian-13.2-xfce-v6.12-arm64-2026-01-13-12gb.tar.xz
sudo tar -cpJf "$TARBALL" -C "$ROOTFS_DIR" .
sudo rm -rf "$ROOTFS_DIR"
```

**通过此工作流程预装的软件包：**

| 软件包 | 被哪个组件依赖 | 用途 |
| --- | --- | --- |
| `frei0r-plugins` | `imx219-preview.sh` | 通过 `frei0r-filter-white-balance` GStreamer 元素实现白平衡校正 |


**在 chroot 内完成的系统配置更改：**

1. **禁用 DPMS 和屏幕消隐：**

```bash
mkdir -p /etc/X11/xorg.conf.d
cat > /etc/X11/xorg.conf.d/10-no-dpms.conf << 'EOF'
Section "ServerFlags"
    Option "BlankTime"   "0"
    Option "StandbyTime" "0"
    Option "SuspendTime" "0"
    Option "OffTime"     "0"
EndSection

Section "Monitor"
    Identifier "Monitor0"
    Option     "DPMS"    "false"
EndSection
EOF
```

2. **通过 lightdm 禁用 X server 屏幕保护程序：**

```bash
sed -i 's|^# xserver-command=X$|xserver-command=X -s 0 -dpms|' \
    /etc/lightdm/lightdm.conf
```

---

## 6. 分区布局
在线烧录和离线镜像制作均产生完全相同的分区布局：

| 分区 | 编号 | 文件系统 | 大小 | 标签 | 内容 |
| --- | --- | --- | --- | --- | --- |
| BOOT | 1 | FAT32（LBA） | 256 MiB | `BOOT` | 引导程序、内核镜像、DTB、extlinux 配置 |
| rootfs | 2 | ext4 | 剩余空间 | `rootfs` | 根文件系统、内核模块 |


分区表类型：**MBR**（主引导记录）

### 6.1 BOOT 分区内容
烧录完成后，BOOT 分区包含以下内容：

```plain
BOOT/
├── tiboot3.bin          # R5 SPL（第一级引导程序）
├── tispl.bin            # TI SPL（OP-TEE + TF-A + A53 U-Boot）
├── u-boot.img           # A53 U-Boot FIT 镜像
├── Image                # Linux 内核镜像
├── ti/                  # 设备树 blob 目录
│   ├── k3-am62a7-mo-62a.dtb
│   └── ...
└── extlinux/
    └── extlinux.conf    # U-Boot extlinux 启动配置
```

### 6.2 启动配置
U-Boot 使用 extlinux 启动流程加载内核。默认 `extlinux/extlinux.conf`：

```plain
menu title mo-62a MicroSD (extlinux.conf)

timeout 30
default microSD

label microSD
  append console=ttyS2,115200n8 earlycon=ns16550a,mmio32,0x02800000 root=/dev/mmcblk1p2 rw rootfstype=ext4 rootwait
  kernel /Image
  fdt    /ti/k3-am62a7-mo-62a.dtb
  # fdtoverlays /overlays/<file>.dtbo
  # initrd /initrd.img
```

内核命令行参数说明：

+ 串口控制台：`ttyS2`，115200 波特率
+ 根设备：`/dev/mmcblk1p2`（SD/MMC 设备的第 2 分区）
+ 根文件系统类型：`ext4`

如需应用设备树覆盖层，请取消 `fdtoverlays` 行的注释，并指定相对于 BOOT 分区根目录的 `.dtbo` 文件路径。

---

## 7. 硬件参考
> 数据来源：`doc/Mo_62a_s_mb_v10-260203.pdf`（原理图 Rev V1.0，共 22 页）
>

### 7.1 整体框图
MO-62A 以 **TI AM62A74** SoC 为核心，顶层框图连接以下子系统：

| 子系统 | 关键 IC | SoC 接口 |
| --- | --- | --- |
| 电源管理 | TPS65931211（PMIC） | SOC_I2C0 |
| eMMC 存储 | — | MMC0 |
| LPDDR4 内存 | MT53E1G32D2FW-046 | DDR32（32-bit） |
| Micro SD 卡 | — | MMC1 |
| RGB 转 HDMI 发送器 | SiI9022ACNU | RGB888 + MCASP0 + SOC_I2C1 |
| 千兆以太网 PHY | DP83867IR | RGMII1 + MDIO |
| USB Hub（4 口） | USB2514 | USB1 |
| Wi-Fi / 蓝牙 | FG6221ASRC-0L | MMC2（SDIO）+ SOC_UART6 |
| RTC | PCF85263ATL | SOC_I2C0 |
| 音频编解码器 | TLV320AIC3106 | MCASP1 + SOC_I2C1 |
| EEPROM | BL24C02（M24M02E） | SOC_I2C1 |
| CSI 摄像头 | — | CSI0（4-lane MIPI）+ SOC_I2C2 |
| 40 Pin 扩展接口 | — | GPIO / I2C / SPI / UART / PWM / MCASP |
| 风扇控制器 | TXB0104RUTR（电平转换） | PWM + TIMER |
| 调试 UART | SN74LVC2G24DCUR（隔离） | SOC_UART0 |


---

### 7.2 供电系统
**输入：** USB Type-C，5 V，最大总电流 6.38 A。

**电源轨及分配：**

| 电源轨 | 来源 | 典型电流 | 负载 |
| --- | --- | --- | --- |
| VCC_3V3_MAIN | DCDC 6 A（TPS62A63RLR） | 最大 6 A | 系统 3.3 V 主干 |
| VCC_3V3_SYS | LDSW 4 A（TPS22965） | 957 mA | USB Hub、Wi-Fi/BT、音频编解码器、以太网 PHY、HDMI TX、RTC |
| VSYS_3V3_EXP | 负载开关 4 A（TPS22965） | — | 40 Pin、CSI FPC、Micro SD |
| VDD_CORE | PMIC Buck（3.5 A） | — | SoC 核心 |
| VDD_LPDDR4 | PMIC Buck（3.5 A） | — | LPDDR4 |
| SOC_DVDD1V8 | PMIC Buck（4 A） | — | SoC 1.8 V I/O |
| VCC1V8_SYS_SW | PMIC Buck（2 A） | 200 mA | LPDDR4 辅助 |
| VDD_2V5 | LDO（TPS74801DRCR，1.5 A） | 325 mA | 以太网 PHY VDDA2P5 |
| VDD_1V0 | LDO（TLV75510PDQN） | 108 mA | 以太网 PHY VDD1P0 |
| VDD_1V2 | LDO（TLV75512PDQN） | 80 mA | HDMI TX VDD1P2 |
| VDD_CANUART | LDO（FLV70S07SYP） | 10 mA | CAN / UART I/O |


**状态指示灯（由 MCU GPIO 驱动）：**

| LED | 颜色 | GPIO 信号 |
| --- | --- | --- |
| POWER | 红色 | B9 / MCU_GPIO0_16 / PWR_LED |
| STATUS | 绿色 | D7 / MCU_GPIO0_15 / ACT_LED |


---

### 7.3 I2C 设备地址映射
| SoC 总线 | 设备 | 地址 |
| --- | --- | --- |
| SOC_I2C0 | PMIC TPS65931211 | 0x48 / 0x49 / 0x5A / 0x5B |
| SOC_I2C0 | RTC PCF85263ATL | 0x51 |
| SOC_I2C1 | 音频编解码器 TLV320AIC3106 | 0x1B |
| SOC_I2C1 | HDMI TX SiI9022ACNU | 0x3B / 0x3F / 0x62 |
| SOC_I2C1 | EEPROM BL24C02 | 0x50 |
| SOC_I2C2 | CSI FPC | — |
| SOC_I2C2 | EXP 40 Pin（SDA1/SCL1） | — |
| MCU_I2C0 | PMIC（从 I2C） | — |


---

### 7.4 内存
**LPDDR4（MT53E1G32D2FW-046）**

| 项目 | 值 |
| --- | --- |
| 总线位宽 | 32-bit |
| 配置 | 单通道，32-bit |
| SoC 接口 | DDR0（32-bit 全位宽） |
| 供电 | VDD_LPDDR4（1.1 V），SOC_DVDD1V8 |
| 复位下拉 | R120，10 kΩ（已贴装） |


**EEPROM（BL24C02F）**

| 项目 | 值 |
| --- | --- |
| 封装 | SOT23-5 |
| 接口 | I2C（SOC_I2C1） |
| 地址 | 0x50 |
| 写保护 | GPIO：C19/GPIO0_17/EEP_WC |


---

### 7.5 存储
**eMMC**

+ 接口：MMC0（8-bit，JEDEC eMMC 电气标准 v5.1 / JESD84-B51）
+ I/O 电压：1.8 V（VDDSHV4）

**Micro SD 卡**

+ 接口：MMC1（4-bit，支持 UHS-I，3.3 V / 1.8 V 电压切换）
+ I/O 电压：3.3 V（VDDSHV5）/ 1.8 V 可切换
+ 含 UHS-I 电压切换复位逻辑的负载开关
+ 连接器：Micro SD（MUF-MB4）

---

### 7.6 显示——Micro HDMI
**RGB 转 HDMI 发送器：SiI9022ACNU**

| 项目 | 值 |
| --- | --- |
| SoC 视频接口 | VOUT0_DATA[0..15]、VOUT0_PCLK、VSYNC、HSYNC、DE（并行 RGB） |
| SoC 音频接口 | MCASP0（ACLKX、AFSX、AXR2） |
| I2C 控制 | SOC_I2C1（0x3B / 0x3F / 0x62） |
| 复位 GPIO | AA19/GPIO0_89/HDMI_RSTn |
| 输出连接器 | Micro HDMI（J7） |
| ESD 保护 | ESD7304D（×2 组） |
| 供电 | VDD_1V2（1.2 V），VCC_3V3_SYS |


---

### 7.7 网络——千兆以太网
**以太网 PHY：DP83867CSRGZR**

| 项目 | 值 |
| --- | --- |
| 接口 | RGMII1（1 Gbps） |
| PHY 地址 | 0x00 |
| 自动协商 | 已启用，Auto-MDI-X |
| TX 时钟偏移 | 0 ns |
| RX 时钟偏移 | 2 ns |
| MDIO | SoC_RGMII_MDC / MDO |
| 晶振 | Y8，25 MHz / 2016 / 30 ppm / 12 pF |
| 供电 | VDDA2P5 = 2.5 V，VDD1P0 = 1.0 V，VDD1P2 = 1.2 V |
| 连接器 | RJ45（含集成磁性器件 LPJG4928HENL） |
| PoE 接头 | J5（2×2，2.54 mm 间距） |
| 链路 LED | 左侧（绿色） |
| 活动 LED | 右侧（黄色） |


---

### 7.8 USB
**USB Hub：USB2514（USB2514BQFN36）**

| 项目 | 值 |
| --- | --- |
| 上行端口 | 1× USB 2.0（来自 SoC USB1） |
| 下行端口 | 4× USB 2.0 Type-A |
| 电源开关 | TPS2561DRC，限流 2800 mA |
| VBUS 供电 | VBUS_5V0_TYPEA（5 V 输入经 SW 2 A） |
| 单端口电流 | 4 个端口合计最高 2 A |


**USB Type-C（J31）**

+ 仅 USB 2.0（USB0）
+ 为板卡供电（VIN-5V）
+ ESD 保护：TVS05000RV

---

### 7.9 无线——Wi-Fi / 蓝牙
**模块：FG6221ASRC-0L（6221A-SRC）**

| 项目 | 值 |
| --- | --- |
| Wi-Fi 接口 | MMC2（SDIO 4-bit，1.8 V） |
| 蓝牙接口 | SOC_UART6（含 CTS/RTS，1.8 V） |
| Wi-Fi 使能 | EN_WLAN（F22/GPIO0_71/WLAN_EN/1V8） |
| 蓝牙使能 | EN_BT（K22/GPIO0_1/BT_EN/1V8） |
| 中断 | INT_WLAN（E21/GPIO0_72/WLAN_IRQ/1V8） |
| 天线连接器 | U.FL × 1（CON1） |
| 供电 | SOC_DVDD1V8（1.8 V），VCC_3V3_SYS（3.3 V） |


---

### 7.10 音频
**音频编解码器：TLV320AIC3106IRGZ**

| 项目 | 值 |
| --- | --- |
| I2S 接口 | MCASP1（ACLKX_BUF、AFSX_BUF、AXR0_BUF、AXR2_BUF） |
| I2C 控制 | SOC_I2C1，地址 0x1B |
| MCLK | 12.288 MHz 晶振（25 ppm，3.3 V） |
| 复位 GPIO | W18/GPIO0_1/AUD_RSTn |
| 耳机输出 | HPLOUT / HPROUT（立体声） |
| 麦克风输入 | MIC_IN（LINE IN） |
| 3.5 mm 接口（J8） | Pin 1：L — Pin 2：MIC — Pin 3：GND — Pin 4/5：HPROUT/HPLOUT |
| 接线标准 | 国标（CTIA）：L / R / GND / MIC |


---

### 7.11 RTC
**RTC IC：PCF85263ATL**

| 项目 | 值 |
| --- | --- |
| 接口 | SOC_I2C0，I2C 7-bit 地址 0x51（0b0101001） |
| 晶振 | Y1，SSP-T7-F，32.768 kHz，20 ppm，12.5 pF 负载 |
| 电池接口 | J2（SH1.0-2p，3 V 纽扣电池） |


---

### 7.12 扩展接口
#### 7.12.1 40 Pin 接口（J9——USER EXPN）
40 Pin 扩展接口（丝印：USER EXPN）引出以下 SoC 信号：

| 功能 | SoC 信号 |
| --- | --- |
| GPIO | GPIO0..21（多个） |
| I2C | SOC_I2C2（SDA/SCL）——同时作为 EXP40 Pin 3/6 |
| UART | SOC_UART5 × 2（TX/RX） |
| SPI | SOC_SPI0（CLK/D0/D1/CS0/CS1） |
| PWM | PWM × 3 |
| I2S | MCASP2（ACLKX、AFSX、AXR） |
| 唤醒 I2C | WKUP_I2C0 |


#### 7.12.2 FPC 22 Pin CSI 摄像头（JP1）
| 项目 | 值 |
| --- | --- |
| 连接器 | FPC22 / 0.5 mm 间距（JP1） |
| 标准 | 树莓派摄像头接口，4-lane MIPI CSI-2 |
| 差分通道 | CSI0_RXP/N[0..3] + CSI0_RXCLKP/N |
| I2C | CSI_I2C2_SDA/SCL（来自 SOC_I2C2） |
| 供电 | VSYS_3V3_EXP |
| 使能 / 掉电 | CSI0_PWDN（Y19/GPIO0_87） |
| 阻抗校准 | CSI0_RXRCALIB（499 Ω 接地） |


#### 7.12.3 风扇接口（J6）
| 项目 | 值 |
| --- | --- |
| 连接器 | SH1.0-4p |
| PWM 控制 | FAN_PWM（经 TXB0104RUTR 电平转换） |
| 转速反馈 | FAN_TACH |
| SoC 信号 | PWM（D18/TIMER_IO7），TACH（D1/ID1_10/EHRPWM1_B） |


---

### 7.13 调试接口
**调试 UART（J4——SH1.0-3p）**

UART0 为 MPU 调试 UART。SN74LVC2G24DCUR 提供电压隔离。

| 引脚 | 信号 |
| --- | --- |
| 1 | UART0_RXD |
| 2 | GND |
| 3 | UART0_TXD |


波特率：115200 8N1（与内核控制台 `ttyS2` 一致）。

---

### 7.14 启动配置
MO-62A 使用固定电阻启动模式配置（BOOTMODE[15:0]）。

**已配置的启动模式：**

| 优先级 | 模式 | 描述 |
| --- | --- | --- |
| 主启动 | SD CARD（MMC1） | 4-bit MMC SD 卡启动 |
| 备用 | Ethernet | 网络启动 |


**BOOTMODE 寄存器设置（由电阻配置）：**

| 位段 | 值 | 含义 |
| --- | --- | --- |
| BOOTMODE[2:0] | 011 | PLL 输入频率 25 MHz |
| MCU_BOOTMODE[6:3] | 1000 | 主启动 = MMCSD（SD 卡） |
| MCU_BOOTMODE[9:7] | B8=1, B7=0 | MMC 端口 1，4-bit 位宽 |
| MCU_BOOTMODE[12:10] | 100 | 备用启动 = 以太网 |


**芯片支持的所有启动模式：**

1. OSPI
2. MMC1——SD 卡
3. UART
4. eMMC
5. 以太网
6. USB0 DFU
7. USB0 MS

---

### 7.15 JTAG 接口
| 信号 | 描述 |
| --- | --- |
| SoC_EMU0 / SoC_EMU1 | 仿真引脚 |
| SoC_TCK | JTAG 时钟 |
| SoC_TMS | JTAG 模式选择 |
| SoC_TDI | JTAG 数据输入 |
| SoC_TDO | JTAG 数据输出 |
| SoC_TRSTN | JTAG 复位 |


上拉电阻：4.7 kΩ 接 VCC_3V3_SYS。

---

### 7.16 硬件版本识别引脚
三个硬件版本识别引脚（HW_REV0、HW_REV1、HW_REV2）路由至原理图第 9 页 OSPI 接口部分。这些 PCB 焊接电阻（默认 DNF）用于在硬件上编码 PCB 版本和 DDR 型号，供软件检测使用。

