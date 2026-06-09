# MO-62A Single Board Computer SDK User Guide

## Document navigation

### Contents

| Section | Topic |
| ------- | ----- |
| [Section 1 Overview](#1-overview) | Platform capabilities, SDK components, top-level directory layout |
| [Section 2 Environment setup](#2-environment-setup) | Ubuntu host, dependencies, setup.sh, cross-toolchains |
| [Section 3 U-Boot](#3-u-boot) | Board-specific files, `make u-boot*`, staging outputs |
| [Section 4 Linux kernel](#4-linux-kernel) | defconfig, linux-dtbs, linux, linux_stage |
| [Section 5 Flashing the SD card](#5-flashing-the-sd-card) | Online write, offline `.img`, rootfs customization |
| [Section 6 Partition layout](#6-partition-layout) | MBR, BOOT contents, and extlinux |
| [Section 7 Hardware reference](#7-hardware-reference) | Whole-board interface notes (from schematic documentation) |

Anchor resolution depends on the renderer. If a link does not jump correctly, use the sidebar outline or search for the heading text.

### Task-oriented jumps

| Focus | Suggested reading |
| ----- | ----------------- |
| Prepare a build host | [Section 2 Environment setup](#2-environment-setup) |
| Produce R5 SPL / A53 U-Boot | [Section 3 U-Boot](#3-u-boot) |
| Produce DTBs, images, FIT | [Section 4 Linux kernel](#4-linux-kernel) |
| Write an SD card, build an Etcher package | [Section 5 Flashing the SD card](#5-flashing-the-sd-card) |
| Boot parameters and partition structure | [Section 6 Partition layout](#6-partition-layout) |
| Connectors, power, SoC and peripheral mapping | [Section 7 Hardware reference](#7-hardware-reference) |

---

MO-62A single-board computer SDK, based on the TI AM62A7 platform, with up to 2 TOPS AI inference performance.

## 1. Overview

MO-62A is a single-board computer based on the TI AM62A7 processor, designed for edge AI inference, machine vision, and industrial control applications. The AM62A7 integrates a quad-core Arm Cortex-A53 (up to 1.4 GHz), a single Cortex-R5F real-time processor, and a dedicated MMA (Matrix Multiplication Accelerator), delivering up to 2 TOPS of AI inference performance.

This SDK is built on **TI Processor SDK Linux RT EdgeAI AM62A EVM 11.01.07.05** and provides full hardware customization support for the MO-62A board. It includes the following components:

+ **U-Boot**: Bootloader customized for MO-62A, including R5 SPL and A53 U-Boot
+ **Linux kernel**: Kernel and device trees customized for MO-62A, based on the TI Linux RT kernel
+ **Build system**: Unified Makefile-based build and staging workflow
+ **Flash tool**: Supports direct SD card writes and offline balenaEtcher image creation

SDK directory structure overview:

```plain
mo-62a/
├── board-support/          # U-Boot, Kernel sources and prebuilt images
│   ├── built-images/       # Staged build artifacts (generated after staging)
│   ├── prebuilt-images/    # TI prebuilt firmware (bl31, bl32, ti-dm, etc.)
│   └── extra-applications/ # Board-specific extra applications
├── bin/                    # Helper scripts and flash tool
│   ├── mo-62a-flash.sh     # Unified flash tool
│   └── extlinux/           # U-Boot extlinux boot configuration
├── filesystem/             # rootfs tarball directory
├── linux-devkit/           # AArch64 cross-compilation toolchain
├── k3r5-devkit/            # ARMv7 R5 cross-compilation toolchain
├── makerules/              # Per-component Makefile rules
├── Makefile                # Top-level Makefile
├── Rules.make              # Global path and platform configuration
└── setup.sh                # Development host initialization script
```

---

## 2. Environment Setup

### 2.1 Host System Requirements

The following host environment has been verified for building this SDK:

| Item         | Requirement               |
| ------------ | ------------------------- |
| OS           | Ubuntu 22.04 LTS (x86_64) |
| Kernel       | 6.8.0 or later            |
| Architecture | x86_64                    |

Required host packages:

```bash
sudo apt-get install \
  xinetd tftpd nfs-kernel-server minicom \
  build-essential libncurses5-dev autoconf automake \
  dos2unix screen lrzsz lzop flex libssl-dev \
  u-boot-tools make git parted dosfstools e2fsprogs \
  pv xz-utils zip wget curl
```

### 2.2 Clone This Repository

Clone the MO-62A SDK to any directory on your host machine:

```bash
git clone https://github.com/inhandnet/mo-62a.git
cd mo-62a
```

### 2.3 Initialize the environment with setup.sh

Run `setup.sh` from the SDK root to initialize the development host:

```bash
./setup.sh
```

The script performs the following steps:

1. **Verifies** the host OS (Ubuntu 22.04 LTS)
2. **Adds** the current user to the `dialout` group (required for serial port access)
3. **Installs** required host packages — press `Y` to install, `n` to skip if already installed
4. **Writes** `TI_SDK_PATH` to `~/.bashrc` pointing to the cloned repository root, so the variable persists across terminal sessions
5. **Creates** a symlink at `/opt/ti-processor-sdk-linux-rt-edgeai-am62a-evm-11.01.07.05` pointing to the cloned repository, required because the cross-compilation toolchain binaries have a hardcoded ELF interpreter path at that location

Example output:

```plain
----------------------------------------------------------------------------
MO-62A SDK setup script
SDK root: /home/user/mo-62a
----------------------------------------------------------------------------

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

----------------------------------------------------------------------------
MO-62A SDK setup completed!
You can now build the SDK from: /home/user/mo-62a
----------------------------------------------------------------------------
```

> **Note:** After `setup.sh` completes, `TI_SDK_PATH` is active in the current shell and will be automatically set in all future terminal sessions via `~/.bashrc`. Running `setup.sh` again is safe — it will update the symlink and the `TI_SDK_PATH` entry without creating duplicates.

### 2.4 Toolchain

Two cross-compilation toolchains are included in the SDK:

**AArch64 toolchain** — used for Linux kernel and A53 U-Boot:

| Item           | Value                                    |
| -------------- | ---------------------------------------- |
| Path           | `linux-devkit/sysroots/x86_64-arago-linux/usr/bin/aarch64-oe-linux/` |
| Prefix         | `aarch64-oe-linux-`                      |
| GCC version    | 13.4.0                                   |
| Target sysroot | `linux-devkit/sysroots/aarch64-oe-linux/` |

**ARMv7 R5 toolchain** — used for R5 SPL (tiboot3):

| Item           | Value                                    |
| -------------- | ---------------------------------------- |
| Path           | `k3r5-devkit/sysroots/x86_64-arago-linux/usr/bin/arm-oe-eabi/` |
| Prefix         | `arm-oe-eabi-`                           |
| GCC version    | 13.4.0                                   |
| Target sysroot | `k3r5-devkit/sysroots/armv7at2hf-vfp-oe-eabi/` |

To verify both toolchains are available (run after `setup.sh` has completed):

```bash
# AArch64
linux-devkit/sysroots/x86_64-arago-linux/usr/bin/aarch64-oe-linux/aarch64-oe-linux-gcc --version

# ARMv7 R5
k3r5-devkit/sysroots/x86_64-arago-linux/usr/bin/arm-oe-eabi/arm-oe-eabi-gcc --version
```

Expected output:

```plain
aarch64-oe-linux-gcc (GCC) 13.4.0
Copyright (C) 2023 Free Software Foundation, Inc.

arm-oe-eabi-gcc (GCC) 13.4.0
Copyright (C) 2023 Free Software Foundation, Inc.
```

> **Note:** The toolchain binaries have a hardcoded ELF interpreter path pointing to `/opt/ti-processor-sdk-linux-rt-edgeai-am62a-evm-11.01.07.05/`. The symlink created by `setup.sh` satisfies this requirement regardless of where the repository is cloned. The toolchains are invoked automatically via `Rules.make` and do not require manual PATH export.

---

## 3. U-Boot

### 3.1 Related Files

MO-62A specific files added to the U-Boot source tree:

| File                                     | Description                     |
| ---------------------------------------- | ------------------------------- |
| `board-support/ti-u-boot-2025.01+git/configs/am62ax_mo_62a_a53_defconfig` | A53 U-Boot defconfig            |
| `board-support/ti-u-boot-2025.01+git/configs/am62ax_mo_62a_r5_defconfig` | R5 SPL defconfig                |
| `board-support/ti-u-boot-2025.01+git/dts/upstream/src/arm64/ti/k3-am62a7-mo-62a.dts` | A53 main device tree            |
| `board-support/ti-u-boot-2025.01+git/dts/upstream/src/arm64/ti/k3-am62a7-mo-62a-pinmux.dtsi` | Pin mux configuration           |
| `board-support/ti-u-boot-2025.01+git/arch/arm/dts/k3-am62a7-r5-mo-62a.dts` | R5 SPL device tree              |
| `board-support/ti-u-boot-2025.01+git/arch/arm/dts/k3-am62a7-mo-62a-u-boot.dtsi` | U-Boot specific DT additions    |
| `board-support/ti-u-boot-2025.01+git/arch/arm/dts/k3-am62a7-mo-62a-binman.dtsi` | Binman packaging configuration  |
| `board-support/ti-u-boot-2025.01+git/arch/arm/dts/k3-am62a7-mo-62a-lp4-4GB.dtsi` | LPDDR4 4GB memory configuration |

Prebuilt firmware required during the build (from TI, not modified):

| File                                     | Description                 |
| ---------------------------------------- | --------------------------- |
| `board-support/prebuilt-images/am62a-evm/bl31.bin` | Arm Trusted Firmware (TF-A) |
| `board-support/prebuilt-images/am62a-evm/bl32.bin` | OP-TEE OS                   |
| `board-support/prebuilt-images/am62a-evm/ti-dm/am62axx/dm_edgeai_mcu1_0_release_strip.out` | TI Device Manager firmware  |

### 3.2 Build U-Boot

U-Boot is built in two separate passes — R5 SPL first, then A53 U-Boot. Both are invoked via the top-level `make` from the SDK root.

**Build R5 SPL (tiboot3):**

```bash
make u-boot-r5
```

This configures the R5 build with `am62ax_mo_62a_r5_defconfig` and compiles using the ARMv7 R5 toolchain (`arm-oe-eabi-`). The output is placed in `board-support/u-boot-build/r5/`.

**Build A53 U-Boot:**

```bash
make u-boot-a53
```

This configures the A53 build with `am62ax_mo_62a_a53_defconfig` and compiles using the AArch64 toolchain (`aarch64-oe-linux-`), incorporating `bl31.bin`, `bl32.bin`, and the TI Device Manager firmware via binman. The output is placed in `board-support/u-boot-build/a53/`.

**Build both in one step:**

```bash
make u-boot
```

### 3.3 Stage Build Artifacts

After a successful build, copy the output binaries to `board-support/built-images/`:

```bash
make u-boot_stage
```

### 3.4 Build Output

After staging, the following files are available in `board-support/built-images/`:

| File                              | Size    | Source    | Description                              |
| --------------------------------- | ------- | --------- | ---------------------------------------- |
| `tiboot3-am62ax-gp-mo-62a.bin`    | ~318 KB | R5 build  | R5 SPL for GP (General Purpose) devices  |
| `tiboot3-am62ax-hs-fs-mo-62a.bin` | ~320 KB | R5 build  | R5 SPL for HS-FS (High Security, Field Securable) devices |
| `tiboot3-am62ax-hs-mo-62a.bin`    | ~320 KB | R5 build  | R5 SPL for HS (High Security) devices    |
| `tiboot3.bin`                     | ~320 KB | R5 build  | Default tiboot3 (HS-FS, used by flash tool) |
| `tispl.bin`                       | ~1.7 MB | A53 build | TI SPL — loads OP-TEE, TF-A, and A53 U-Boot |
| `u-boot.img`                      | ~1.2 MB | A53 build | A53 U-Boot FIT image                     |

> **Note:** The appropriate `tiboot3-*.bin` variant depends on the device security state. Most production MO-62A boards ship as HS-FS, which uses `tiboot3-am62ax-hs-fs-mo-62a.bin`. The flash tool uses `tiboot3.bin` (a copy of the HS-FS variant) by default.

---

## 4. Linux Kernel

### 4.1 Related Files

MO-62A specific files added to the Linux kernel source tree:

| File                                     | Description                  |
| ---------------------------------------- | ---------------------------- |
| `board-support/ti-linux-kernel-6.12.35+git-ti-rt/arch/arm64/configs/am62ax_mo_62a_defconfig` | MO-62A base kernel defconfig |
| `board-support/ti-linux-kernel-6.12.35+git-ti-rt/arch/arm64/boot/dts/ti/k3-am62a7-mo-62a.dts` | MO-62A main device tree      |
| `board-support/ti-linux-kernel-6.12.35+git-ti-rt/arch/arm64/boot/dts/ti/k3-am62a7-mo-62a-pinmux.dtsi` | Pin mux configuration        |

The following kernel config fragments are applied on top of the defconfig during the build:

| Fragment                | Location          | Purpose                                  |
| ----------------------- | ----------------- | ---------------------------------------- |
| `ti_arm64_prune.config` | `kernel/configs/` | Removes non-TI ARM64 platform support to reduce build size |
| `ti_rt.config`          | `kernel/configs/` | Enables PREEMPT_RT real-time kernel patches |

### 4.2 Build DTBs

Build all device tree blobs (62 DTBs and DTBOs in total):

```bash
make linux-dtbs
```

This configures the kernel with `am62ax_mo_62a_defconfig` + `ti_arm64_prune.config` + `ti_rt.config`, then builds all DTBs matching the prefix patterns defined in `Rules.make`:

```plain
ti/k3-am62a7  ti/k3-fpdlink  ti/k3-am62x-sk  ti/k3-v3link
```

Output is placed in `board-support/ti-linux-kernel-6.12.35+git-ti-rt/arch/arm64/boot/dts/`.

### 4.3 Build Kernel

Build the kernel image, modules, and FitImage:

```bash
make linux
```

This performs the following steps in order:

1. Builds DTBs (calls `linux-dtbs` automatically)
2. Builds U-Boot (calls `u-boot` automatically, required for FitImage signing key)
3. Compiles `Image` and `Image.gz`
4. Compiles kernel modules
5. Packages a signed `fitImage` using `mkimage` with the U-Boot signing key and the ITS template from `board-support/prebuilt-images/am62a-evm/`
6. Rebuilds U-Boot A53 (binman) to embed the MO-62A DTB into `tispl.bin`

### 4.4 Stage Build Artifacts

Copy kernel and DTB outputs to `board-support/built-images/`:

```bash
make linux_stage
```

### 4.5 Build Output

After staging, the following files are added to `board-support/built-images/`:

| File                             | Size    | Description                              |
| -------------------------------- | ------- | ---------------------------------------- |
| `Image`                          | ~18 MB  | Uncompressed kernel image                |
| `Image.gz`                       | ~7.0 MB | Compressed kernel image                  |
| `fitImage`                       | ~7.3 MB | Signed FIT image (kernel + DTBs), used for verified boot |
| `dtb/ti/*.dtb` / `dtb/ti/*.dtbo` | —       | 62 device tree blobs and overlays        |

> **Note:** `fitImage` is signed with the `custMpk` key from the U-Boot source tree. The signing step also triggers a rebuild of `tispl.bin` so it embeds the MO-62A DTB (`k3-am62a7-mo-62a.dtb`) in the A53 SPL. This means `make linux` will always update both `fitImage` and `tispl.bin` in `built-images/`.

---

## 5. Flashing the SD Card

The unified flash tool `bin/mo-62a-flash.sh` supports two output targets:

+ **Online flashing** — write directly to a physical SD card
+ **Offline image creation** — create a `.img` file for use with balenaEtcher

Both modes create identical partition layouts and content.

### 5.1 Prerequisites

Required host packages (installed by `setup.sh`):

```plain
parted  dosfstools  e2fsprogs  pv  xz-utils  zip  wget  curl
```

Ensure the following are ready before running the flash tool:

1. **Built images staged** — run `make u-boot_stage` and `make linux_stage` (or `make all_stage`) so that `board-support/built-images/` contains the required files
2. **Rootfs tarball present** — place a `.tar.xz` or `.tar.gz` rootfs tarball under `filesystem/`
3. **SD card inserted** (online mode only) — the tool automatically detects `/dev/sdX` and `/dev/mmcblkN` block devices

### 5.2 Launch the Flash Tool

The flash tool is interactive and must be run as root:

```bash
sudo bash bin/mo-62a-flash.sh
```

On launch, it prompts you to choose the output target:

```plain
=== MO-62A Flash Tool ===

Select output target:
  [1] Write directly to an SD card
  [2] Create offline image for balenaEtcher

Select target [1/2]:
```

### 5.3 Online Flashing (Write Directly to SD Card)

Select `[1]` for online mode. The tool will enumerate all detected block devices:

```plain
Detected candidate block devices:
  [1] /dev/sda  29.7G  SD Card Reader

Select target device number:
```

Then choose the operation mode:

```plain
Select operation mode:
  [1] full      - create partitions + format + copy BOOT + extract rootfs
  [2] partition - create partitions + format only
  [3] boot      - copy BOOT content only (strict checks, no repartition)
  [4] rootfs    - copy rootfs content only (strict checks, no repartition)

Select mode number (default 1):
```

| Mode        | Description                              |
| ----------- | ---------------------------------------- |
| `full`      | Full write: wipe and repartition, format, copy boot files, extract rootfs, install kernel modules |
| `partition` | Partitioning only: wipe and recreate MBR, format partitions — no content written |
| `boot`      | Overwrite BOOT partition only — re-flashes bootloader and kernel without touching rootfs |
| `rootfs`    | Overwrite rootfs partition only — re-extracts the rootfs without touching the BOOT partition |

For a fresh SD card, select `full`. The tool will ask for confirmation (`Type YES to continue`), then proceed automatically:

1. Unmounts any existing partitions on the selected device
2. Wipes the old partition table
3. Creates MBR partition table: BOOT (FAT32, 256 MiB) + rootfs (ext4, remaining space)
4. Formats both partitions
5. Copies boot artifacts to the BOOT partition: `tiboot3.bin`, `tispl.bin`, `u-boot.img`, `Image`, DTBs, `extlinux/`
6. Asks which rootfs tarball to use (if multiple are present under `filesystem/`)
7. Extracts the rootfs tarball to the rootfs partition
8. Installs kernel modules (`make modules_install`) into the rootfs
9. Builds and installs any external applications from `board-support/extra-applications/`

Example session (full mode):

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

After flashing, insert the SD card into the MO-62A board and power on. Boot messages appear on the serial console at `ttyS2` (115200 8N1).

### 5.4 Offline Image Creation (balenaEtcher)

Select `[2]` for image mode. The tool prompts for image parameters:

```plain
Available rootfs tarballs:
  [1] debian-13.2-xfce-v6.12-arm64-2026-01-13-12gb.tar.xz

Select rootfs tarball number (or 'q' to abort): 1

Output directory (default: bin/out): /path/to/output
Output image base name (default: mo-62a): mo-62a
Image size (GiB, integer) (default: 8): 8
Compression (zip|xz|none) (default: zip): zip
```

| Parameter        | Description                              |
| ---------------- | ---------------------------------------- |
| Output directory | Where to write the `.img` and checksum files |
| Image base name  | Filename prefix; output will be `<name>.img` (and `<name>.img.zip` etc.) |
| Image size (GiB) | Total image size. Must be large enough to hold the rootfs; 8 GiB is sufficient for the default rootfs |
| Compression      | `zip` (recommended for balenaEtcher), `xz` (smaller file, slower), `none` (no compression) |

The tool creates a sparse `.img` file, partitions and formats it via a loopback device, fills it with the same content as online mode, detaches the loop device, then compresses the result.

Output files:

```plain
/path/to/output/
├── mo-62a.img         # Raw disk image (8 GiB sparse file)
├── mo-62a.img.zip     # Compressed image for balenaEtcher (if compression=zip)
└── mo-62a.sha256      # SHA-256 checksums of all image files
```

To flash the image with balenaEtcher:

1. Open [balenaEtcher](https://etcher.balena.io/)
2. Click **Flash from file** and select `mo-62a.img.zip` (balenaEtcher accepts compressed images directly)
3. Select the target SD card
4. Click **Flash**

> **Note:** Image size must be at least as large as the expanded rootfs. The default `8` GiB is sufficient for the provided Debian rootfs (~6.9 GiB extracted). When using a custom rootfs, adjust the size accordingly.

### 5.5 Customising the Rootfs Tarball (Adding apt Packages)

The flash tool extracts the rootfs tarball as-is. Additional Debian packages (e.g. `frei0r-plugins` required by `imx219-preview.sh`) must be pre-installed into the tarball **before** flashing so that they are available after both online and offline flashing without network access on the target.

The standard workflow is:

1. **Install prerequisite tools on the host** (once, x86-64 Ubuntu/Debian):

```bash
sudo apt-get install -y qemu-user-static binfmt-support
sudo systemctl restart systemd-binfmt || sudo update-binfmts --enable
```

2. **Extract the tarball** to a temporary directory:

```bash
ROOTFS_DIR=/tmp/mo-62a-rootfs
mkdir -p "$ROOTFS_DIR"
sudo tar -xpf filesystem/debian-13.2-xfce-v6.12-arm64-2026-01-13-12gb.tar.xz \
    -C "$ROOTFS_DIR"
```

3. **Copy the `qemu` binary** into the extracted rootfs:

```bash
sudo cp /usr/bin/qemu-aarch64-static "$ROOTFS_DIR/usr/bin/"
```

4. **Bind-mount pseudo-filesystems** and enter the chroot:

```bash
sudo mount --bind /proc    "$ROOTFS_DIR/proc"
sudo mount --bind /sys     "$ROOTFS_DIR/sys"
sudo mount --bind /dev     "$ROOTFS_DIR/dev"
sudo mount --bind /dev/pts "$ROOTFS_DIR/dev/pts"
sudo chroot "$ROOTFS_DIR" /bin/bash
```

5. **Inside the chroot**, install the required packages:

```bash
apt-get update
apt-get install -y frei0r-plugins
apt-get clean
exit
```

6. **Clean up** bind mounts and the `qemu` binary:

```bash
sudo umount "$ROOTFS_DIR/dev/pts"
sudo umount "$ROOTFS_DIR/dev"
sudo umount "$ROOTFS_DIR/sys"
sudo umount "$ROOTFS_DIR/proc"
sudo rm -f  "$ROOTFS_DIR/usr/bin/qemu-aarch64-static"
```

7. **Repack** the tarball:

```bash
TARBALL=filesystem/debian-13.2-xfce-v6.12-arm64-2026-01-13-12gb.tar.xz
sudo tar -cpJf "$TARBALL" -C "$ROOTFS_DIR" .
sudo rm -rf "$ROOTFS_DIR"
```

**Packages pre-installed through this workflow:**

| Package          | Required by         | Purpose                                                                 |
| ---------------- | ------------------- | ----------------------------------------------------------------------- |
| `frei0r-plugins` | `imx219-preview.sh` | White balance via the `frei0r-filter-white-balance` GStreamer element |

**System configuration changes applied inside the chroot:**

1. **Disable DPMS and blanking:**

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

2. **Disable the X server screensaver via lightdm:**

```bash
sed -i 's|^# xserver-command=X$|xserver-command=X -s 0 -dpms|' \
    /etc/lightdm/lightdm.conf
```

---

## 6. Partition Layout

Both online flashing and offline image creation produce identical partition layouts:

| Partition | Number | Filesystem  | Size      | Label    | Contents                                 |
| --------- | ------ | ----------- | --------- | -------- | ---------------------------------------- |
| BOOT      | 1      | FAT32 (LBA) | 256 MiB   | `BOOT`   | Bootloader, kernel image, DTBs, extlinux config |
| rootfs    | 2      | ext4        | Remaining | `rootfs` | Root filesystem, kernel modules          |

Partition table type: **MBR** (Master Boot Record)

### 6.1 BOOT partition contents

After flashing, the BOOT partition contains:

```plain
BOOT/
├── tiboot3.bin          # R5 SPL (first-stage bootloader)
├── tispl.bin            # TI SPL (OP-TEE + TF-A + A53 U-Boot)
├── u-boot.img           # A53 U-Boot FIT image
├── Image                # Linux kernel image
├── ti/                  # Device tree blob directory
│   ├── k3-am62a7-mo-62a.dtb
│   └── ...
└── extlinux/
    └── extlinux.conf    # U-Boot extlinux boot configuration
```

### 6.2 Boot configuration

U-Boot uses the extlinux boot flow to load the kernel. Default `extlinux/extlinux.conf`:

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

Kernel command line parameters:

+ Serial console: `ttyS2`, 115200 baud
+ Root device: `/dev/mmcblk1p2` (second partition on the SD/MMC device)
+ Root filesystem type: `ext4`

To apply a device tree overlay, uncomment the `fdtoverlays` line and specify the `.dtbo` path relative to the BOOT partition root.

---

## 7. Hardware Reference

### 7.1 Block Diagram Overview

The MO-62A is built around the **TI AM62A74** SoC. The top-level block diagram connects the following subsystems:

| Subsystem               | Key IC                            | SoC Interface                         |
| ----------------------- | --------------------------------- | ------------------------------------- |
| Power Management        | TPS65931211 (PMIC)                | SOC_I2C0                              |
| eMMC Storage            | —                                 | MMC0                                  |
| LPDDR4 Memory           | MT53E1G32D2FW-046                 | DDR32 (32-bit)                        |
| Micro SD Card           | —                                 | MMC1                                  |
| RGB-to-HDMI Transmitter | SiI9022ACNU                       | RGB888 + MCASP0 + SOC_I2C1            |
| Gigabit Ethernet PHY    | DP83867IR                         | RGMII1 + MDIO                         |
| USB Hub (4-port)        | USB2514                           | USB1                                  |
| Wi-Fi / BT              | FG6221ASRC-0L                     | MMC2 (SDIO) + SOC_UART6               |
| RTC                     | PCF85263ATL                       | SOC_I2C0                              |
| Audio Codec             | TLV320AIC3106                     | MCASP1 + SOC_I2C1                     |
| EEPROM                  | BL24C02 (M24M02E)                 | SOC_I2C1                              |
| CSI Camera              | —                                 | CSI0 (4-lane MIPI) + SOC_I2C2         |
| 40-Pin Expansion        | —                                 | GPIO / I2C / SPI / UART / PWM / MCASP |
| Fan Controller          | TXB0104RUTR (voltage translation) | PWM + TIMER                           |
| Debug UART              | SN74LVC2G24DCUR (isolation)       | SOC_UART0                             |

---

### 7.2 Power System

**Input:** USB Type-C, 5 V, maximum 6.38 A total.

**Power rails and distribution:**

| Rail          | Source                     | Typical Current | Consumers                                |
| ------------- | -------------------------- | --------------- | ---------------------------------------- |
| VCC_3V3_MAIN  | DCDC 6 A (TPS62A63RLR)     | 6 A max         | System 3.3 V backbone                    |
| VCC_3V3_SYS   | LDSW 4 A (TPS22965)        | 957 mA          | USB Hub, Wi-Fi/BT, Audio Codec, Ethernet PHY, HDMI TX, RTC |
| VSYS_3V3_EXP  | Load Switch 4 A (TPS22965) | —               | 40-pin, CSI FPC, Micro SD                |
| VDD_CORE      | PMIC Buck (3.5 A)          | —               | SoC core                                 |
| VDD_LPDDR4    | PMIC Buck (3.5 A)          | —               | LPDDR4                                   |
| SOC_DVDD1V8   | PMIC Buck (4 A)            | —               | SoC 1.8 V I/O                            |
| VCC1V8_SYS_SW | PMIC Buck (2 A)            | 200 mA          | LPDDR4 auxiliary                         |
| VDD_2V5       | LDO (TPS74801DRCR, 1.5 A)  | 325 mA          | Ethernet PHY VDDA2P5                     |
| VDD_1V0       | LDO (TLV75510PDQN)         | 108 mA          | Ethernet PHY VDD1P0                      |
| VDD_1V2       | LDO (TLV75512PDQN)         | 80 mA           | HDMI TX VDD1P2                           |
| VDD_CANUART   | LDO (FLV70S07SYP)          | 10 mA           | CAN / UART I/O                           |

**Status LEDs (driven by MCU GPIO):**

| LED    | Color | GPIO Signal                 |
| ------ | ----- | --------------------------- |
| POWER  | Red   | B9 / MCU_GPIO0_16 / PWR_LED |
| STATUS | Green | D7 / MCU_GPIO0_15 / ACT_LED |

---

### 7.3 I2C Device Map

| SoC Bus  | Device                    | Address(es)               |
| -------- | ------------------------- | ------------------------- |
| SOC_I2C0 | PMIC TPS65931211          | 0x48 / 0x49 / 0x5A / 0x5B |
| SOC_I2C0 | RTC PCF85263ATL           | 0x51                      |
| SOC_I2C1 | Audio Codec TLV320AIC3106 | 0x1B                      |
| SOC_I2C1 | HDMI TX SiI9022ACNU       | 0x3B / 0x3F / 0x62        |
| SOC_I2C1 | EEPROM BL24C02            | 0x50                      |
| SOC_I2C2 | CSI FPC                   | —                         |
| SOC_I2C2 | EXP 40-Pin (SDA1/SCL1)    | —                         |
| MCU_I2C0 | PMIC (secondary I2C)      | —                         |

---

### 7.4 Memory

**LPDDR4 (MT53E1G32D2FW-046)**

| Item            | Value                           |
| --------------- | ------------------------------- |
| Bus width       | 32-bit                          |
| Configuration   | Single channel, 32-bit          |
| SoC interface   | DDR0 (full 32-bit data bus)     |
| Power           | VDD_LPDDR4 (1.1 V), SOC_DVDD1V8 |
| Reset pull-down | R120, 10 kΩ (populated)         |

**EEPROM (BL24C02F)**

| Item          | Value                     |
| ------------- | ------------------------- |
| Package       | SOT23-5                   |
| Interface     | I2C (SOC_I2C1)            |
| Address       | 0x50                      |
| Write protect | GPIO: C19/GPIO0_17/EEP_WC |

---

### 7.5 Storage

**eMMC**

- Interface: MMC0 (8-bit, JEDEC eMMC electrical standard v5.1 / JESD84-B51)
- I/O voltage: 1.8 V (VDDSHV4)

**Micro SD Card**

- Interface: MMC1 (4-bit, UHS-I capable with 3.3 V / 1.8 V switching)
- I/O voltage: 3.3 V (VDDSHV5) / 1.8 V switched
- Load switch with reset logic for UHS-I voltage switching
- Connector: Micro SD (MUF-MB4)

---

### 7.6 Display — Micro HDMI

**RGB-to-HDMI Transmitter: SiI9022ACNU**

| Item                | Value                                    |
| ------------------- | ---------------------------------------- |
| SoC video interface | VOUT0_DATA[0..15], VOUT0_PCLK, VSYNC, HSYNC, DE (parallel RGB) |
| SoC audio interface | MCASP0 (ACLKX, AFSX, AXR2)               |
| I2C control         | SOC_I2C1 (0x3B / 0x3F / 0x62)            |
| Reset GPIO          | AA19/GPIO0_89/HDMI_RSTn                  |
| Output connector    | Micro HDMI (J7)                          |
| ESD protection      | ESD7304D (×2 groups)                     |
| Power               | VDD_1V2 (1.2 V), VCC_3V3_SYS             |

---

### 7.7 Networking — Gigabit Ethernet

**Ethernet PHY: DP83867CSRGZR**

| Item             | Value                                    |
| ---------------- | ---------------------------------------- |
| Interface        | RGMII1 (1 Gbps)                          |
| PHY address      | 0x00                                     |
| Auto-negotiation | Enabled, Auto-MDI-X                      |
| TX clock skew    | 0 ns                                     |
| RX clock skew    | 2 ns                                     |
| MDIO             | SoC_RGMII_MDC / MDO                      |
| Crystal          | Y8, 25 MHz / 2016 / 30 ppm / 12 pF       |
| Power            | VDDA2P5 = 2.5 V, VDD1P0 = 1.0 V, VDD1P2 = 1.2 V |
| Connector        | RJ45 with integrated magnetics (LPJG4928HENL) |
| PoE header       | J5 (2×2, 2.54 mm pitch)                  |
| Link LED         | Left (green)                             |
| Activity LED     | Right (yellow)                           |

---

### 7.8 USB

**USB Hub: USB2514 (USB2514BQFN36)**

| Item             | Value                                    |
| ---------------- | ---------------------------------------- |
| Upstream port    | 1× USB 2.0 (from SoC USB1)               |
| Downstream ports | 4× USB 2.0 Type-A                        |
| Power switch     | TPS2561DRC, Ilimit = 2800 mA             |
| VBUS supply      | VBUS_5V0_TYPEA (from 5 V input via SW 2 A) |
| Current per port | Up to 2 A total for all 4 ports          |

**USB Type-C (J31)**

- USB 2.0 only (USB0)
- Powers the board (VIN-5V)
- ESD protection: TVS05000RV

---

### 7.9 Wireless — Wi-Fi / Bluetooth

**Module: FG6221ASRC-0L (6221A-SRC)**

| Item              | Value                                    |
| ----------------- | ---------------------------------------- |
| Wi-Fi interface   | MMC2 (SDIO 4-bit, 1.8 V)                 |
| BT interface      | SOC_UART6 (with CTS/RTS, 1.8 V)          |
| Enable — Wi-Fi    | EN_WLAN (F22/GPIO0_71/WLAN_EN/1V8)       |
| Enable — BT       | EN_BT (K22/GPIO0_1/BT_EN/1V8)            |
| Interrupt         | INT_WLAN (E21/GPIO0_72/WLAN_IRQ/1V8)     |
| Antenna connector | U.FL × 1 (CON1)                          |
| Supply            | SOC_DVDD1V8 (1.8 V), VCC_3V3_SYS (3.3 V) |

---

### 7.10 Audio

**Audio Codec: TLV320AIC3106IRGZ**

| Item             | Value                                    |
| ---------------- | ---------------------------------------- |
| I2S interface    | MCASP1 (ACLKX_BUF, AFSX_BUF, AXR0_BUF, AXR2_BUF) |
| I2C control      | SOC_I2C1, address 0x1B                   |
| MCLK             | 12.288 MHz crystal oscillator (25 ppm, 3.3 V) |
| Reset GPIO       | W18/GPIO0_1/AUD_RSTn                     |
| Headphone output | HPLOUT / HPROUT (stereo)                 |
| Microphone input | MIC_IN (LINE IN)                         |
| 3.5 mm jack (J8) | Pin 1: L — Pin 2: MIC — Pin 3: GND — Pin 4/5: HPROUT/HPLOUT |
| Wiring standard  | National standard (CTIA): L / R / GND / MIC |

---

### 7.11 RTC

**RTC IC: PCF85263ATL**

| Item              | Value                                    |
| ----------------- | ---------------------------------------- |
| Interface         | SOC_I2C0, I2C 7-bit address 0x51 (0b0101001) |
| Crystal           | Y1, SSP-T7-F, 32.768 kHz, 20 ppm, 12.5 pF load |
| Battery connector | J2 (SH1.0-2p, 3 V button cell)           |

---

### 7.12 Expansion Interfaces

#### 7.12.1 40-Pin Header (J9 — USER EXPN)

The 40-pin expansion header (silk: USER EXPN) exposes the following SoC signals:

| Function   | SoC Signal(s)                            |
| ---------- | ---------------------------------------- |
| GPIO       | GPIO0..21 (multiple)                     |
| I2C        | SOC_I2C2 (SDA/SCL) — also accessible as EXP40 pin 3/6 |
| UART       | SOC_UART5 × 2 (TX/RX)                    |
| SPI        | SOC_SPI0 (CLK/D0/D1/CS0/CS1)             |
| PWM        | PWM × 3                                  |
| I2S        | MCASP2 (ACLKX, AFSX, AXR)                |
| WAKEUP I2C | WKUP_I2C0                             |

#### 7.12.2 FPC 22-Pin CSI Camera (JP1)

| Item                | Value                                    |
| ------------------- | ---------------------------------------- |
| Connector           | FPC22 / 0.5 mm pitch (JP1)               |
| Standard            | Raspberry Pi Camera connector, 4-lane MIPI CSI-2 |
| Lanes               | CSI0_RXP/N[0..3] + CSI0_RXCLKP/N         |
| I2C                 | CSI_I2C2_SDA/SCL (from SOC_I2C2)         |
| Power               | VSYS_3V3_EXP                             |
| Enable / Power-down | CSI0_PWDN (Y19/GPIO0_87)                 |
| Calibration         | CSI0_RXRCALIB (499 Ω to GND)             |

#### 7.12.3 Fan Connector (J6)

| Item          | Value                                    |
| ------------- | ---------------------------------------- |
| Connector     | SH1.0-4p                                 |
| PWM control   | FAN_PWM (via TXB0104RUTR voltage translation) |
| Tach feedback | FAN_TACH                                 |
| SoC signals   | PWM (D18/TIMER_IO7), TACH (D1/ID1_10/EHRPWM1_B) |

---

### 7.13 Debug Interface

**Debug UART (J4 — SH1.0-3p)**

UART0 is the MPU debug UART. A SN74LVC2G24DCUR provides voltage isolation.

| Pin  | Signal    |
| ---- | --------- |
| 1    | UART0_RXD |
| 2    | GND       |
| 3    | UART0_TXD |

Baud rate: 115200 8N1 (matches kernel console on `ttyS2`).

---

### 7.14 Boot Configuration

The MO-62A uses a fixed resistor boot mode configuration (BOOTMODE[15:0]).

**Configured boot modes:**

| Priority | Mode           | Description            |
| -------- | -------------- | ---------------------- |
| Primary  | SD CARD (MMC1) | 4-bit MMC SD card boot |
| Backup   | Ethernet       | Network boot fallback  |

**BOOTMODE register settings (as configured by resistors):**

| Bits                | Value      | Meaning                        |
| ------------------- | ---------- | ------------------------------ |
| BOOTMODE[2:0]       | 011        | 25 MHz PLL input frequency     |
| MCU_BOOTMODE[6:3]   | 1000       | Primary boot = MMCSD (SD Card) |
| MCU_BOOTMODE[9:7]   | B8=1, B7=0 | MMC Port 1, 4-bit width        |
| MCU_BOOTMODE[12:10] | 100        | Backup boot = Ethernet         |

**All supported boot modes (per silicon):**

1. OSPI
2. MMC1 — SD Card
3. UART
4. eMMC
5. Ethernet
6. USB0 DFU
7. USB0 MS

---

### 7.15 JTAG Interface

| Signal              | Description      |
| ------------------- | ---------------- |
| SoC_EMU0 / SoC_EMU1 | Emulation pins   |
| SoC_TCK             | JTAG clock       |
| SoC_TMS             | JTAG mode select |
| SoC_TDI             | JTAG data in     |
| SoC_TDO             | JTAG data out    |
| SoC_TRSTN           | JTAG reset       |

Pull-up resistors: 4.7 kΩ to VCC_3V3_SYS.

---

### 7.16 Hardware Revision Straps

Three hardware revision pins (HW_REV0, HW_REV1, HW_REV2) are routed to the OSPI interface page (sheet 9). These PCB strap resistors (DNF by default) allow encoding the PCB revision and DDR model in hardware for software detection.