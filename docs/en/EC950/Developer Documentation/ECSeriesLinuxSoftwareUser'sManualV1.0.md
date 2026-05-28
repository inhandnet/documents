# EC Series Linux Software User's Manual V1.0

**Edge Computer EC Series**

**Linux Software User's Manual**

**(Applicable for Debian11 V1.1.0 and above)**

Version 1.0, December 2023

<www.inhandnetworks.com>

![1749119259744-5d95e538-b6e6-4d05-a44e-61184b61a336.png](./img/7FVBHB35v1gbWuzj/1749119259744-5d95e538-b6e6-4d05-a44e-61184b61a336-413136.png)

The software described in this manual is according to the license agreement, can only be used in accordance with the terms of the agreement.

**Copyright Notice**

© 2023 InHand Networks All rights reserved.

**Trademarks**

The InHand logo is a registered trademark of InHand Networks.

All other trademarks or registered trademarks in this manual belong to their respective manufacturers.

**Disclaimer**

The company reserves the right to change this manual, and the products are subject to subsequent changes without prior notice. We shall not be responsible for any direct, indirect, intentional or unintentional damage or hidden trouble caused by improper installation or use.

## 1.Introduction

This user manual is for the Inhand Arm-based edge computers listed below and covers instructions for all supported models. Detailed instructions for configuring advanced settings are covered in Chapters 3 and 4 of the manual. Before referring to these sections, verify that the hardware specifications for your computer model support the covered features and configurations.

**Inhand Arm-based edge computers**

●  EC312 series

**Inhand Arm-based edge computer Linux system**

The Inhand Arm-based edge computer Linux system is a Linux distribution optimized for industrial applications and users. It is released and maintained by Inhand. The system integrates several feature sets based on Debian to enhance and accelerate user application development and ensure system’s reliability of development.

## 2.Quick boot

### 2.1.Device connection

You will need another computer to connect to the ARM-based computer. Log in to the command line interface by connecting to the ARM computer via Ethernet.

The default username and password are as follows.

| Username | edge |
| :--- | :--- |
| Password | security@edge |

### 2.1.1.SSH connection

Inhand linux computers support SSH connections over Ethernet, and you can connect to Inhand linux computers using the default IP addresses listed below.

| Port | Default IP |
| :--- | :--- |
| ETH1 | 192.168.3.100 |
| ETH2 | 192.168.4.100 |

<u>NOTE                                                       </u>

Before running the ssh command, make sure to configure the IP address of your laptop/ desktop Ethernet interface in the range ETH1 192.168.3.0/24, ETH2 192.168.4.0/24.

<u>                                                                                </u>

**Connect to the Inhand linux machine using SSH command line via ETH1.**

![1749119259942-4be5f769-d927-43e2-8442-5719c2b0803a.png](./img/7FVBHB35v1gbWuzj/1749119259942-4be5f769-d927-43e2-8442-5719c2b0803a-499504.png)

**Enter yes to complete the connection.**

![1749119260266-1785366f-4e0a-4f01-a15c-b91b20e44d3b.png](./img/7FVBHB35v1gbWuzj/1749119260266-1785366f-4e0a-4f01-a15c-b91b20e44d3b-419457.png)

**Enter the default password security@edge to log in.**

![1749119260464-1f34a93c-a51f-4764-877d-cfb46ee6ec80.png](./img/7FVBHB35v1gbWuzj/1749119260464-1f34a93c-a51f-4764-877d-cfb46ee6ec80-128545.png)

**Login successfully**

![1749119260808-fa6885df-9927-40f0-958c-e2548b006482.png](./img/7FVBHB35v1gbWuzj/1749119260808-fa6885df-9927-40f0-958c-e2548b006482-721212.png)

<u>NOTE                                                       </u>

More SSH information can be found at [https://wiki.debian.org/SSH](https://wiki.debian.org/SSH)

<u>                                                                                 </u>

### 2.2.User Management

### 2.2.1.Switch to Root user

You can use sudo -i (or sudo su) command switches to the root user . For security reasons, do not use the root user to operate all commands.

**sudo -i Enter the default password security@edge to switch to the root user.**

![1749119261457-f80f2922-91be-4555-95a3-92c790a2d6bb.png](./img/7FVBHB35v1gbWuzj/1749119261457-f80f2922-91be-4555-95a3-92c790a2d6bb-445353.png)

<u>NOTE                                                       </u>

When the ARM computer returns a permission denied message after executing the command, you need to use sudo to elevate the permissions.

You must use "sudo su –c" to run the command instead of using >, <, >>, <<, etc., the command needs to be enclosed inside ''

For more sudo information, visit [https://wiki.debian.org/sudo](https://wiki.debian.org/sudo)

<u>                                                                                </u>

### 2.2.2.Create and delete users

You can create and delete users using the _**useradd**_ and _**userdel**_ commands, see the **Linux man pages** for these commands to use. The following example shows how to create a test1 user in the sudo group whose default login shell is bash and has a home directory of home/test1.

**To create the test1 user, use the **_**useradd** _**command.**

![1749119261609-8ccfe9b4-e149-4299-af58-e225c3302467.png](./img/7FVBHB35v1gbWuzj/1749119261609-8ccfe9b4-e149-4299-af58-e225c3302467-589813.png)

**To change the password for test1, use the **_**passwd** _**command to enter and confirm the password .**

![1749119261784-4863024a-92b5-4156-95bd-b1c5741c4434.png](./img/7FVBHB35v1gbWuzj/1749119261784-4863024a-92b5-4156-95bd-b1c5741c4434-611704.png)

**To delete user test1, use the **_**userdel** _**command .**

![1749119261945-202da61d-5d6c-4676-838a-626169f7f207.png](./img/7FVBHB35v1gbWuzj/1749119261945-202da61d-5d6c-4676-838a-626169f7f207-878951.png)

### 2.2.3.Disable default user

**Use the **_** passwd -l**_**command to lock the default user so that edge users cannot log in.**

![1749119262116-dac8f453-624b-41b5-b2d2-e148cd94432a.png](./img/7FVBHB35v1gbWuzj/1749119262116-dac8f453-624b-41b5-b2d2-e148cd94432a-309338.png)

**Use the **_** passwd -u**_**command to unlock the default user so that edge users can log in.**

![1749119262308-1b65f25d-1975-428c-966b-7543352d1942.png](./img/7FVBHB35v1gbWuzj/1749119262308-1b65f25d-1975-428c-966b-7543352d1942-471652.png)

<u>NOTE                                                       </u>

Before disabling the default user, please create other users and ensure that other users can access the ARM computer through SSH.

<u>                                                                                 </u>

### 2.3.Network settings

### 2.3.1.Ethernet settings

After logging in for the first time, you can configure your ARM-based computer network settings to suit your application.

<u>NOTE                                                      </u>

After updating the network configuration, changes in the Ethernet IP address will cause the SSH connection to be interrupted and the SSH connection needs to be re-established.

<u>                                                                                      </u>

**Ethernet configuration file path.**

![1749119262570-faf43587-df22-427c-a12f-59aaeddeb0c8.png](./img/7FVBHB35v1gbWuzj/1749119262570-faf43587-df22-427c-a12f-59aaeddeb0c8-074388.png)

**Ethernet ETH1 and ETH2 configuration files.**

![1749119262749-8e4391d0-fedf-4c3f-985d-942b823a1b1c.png](./img/7FVBHB35v1gbWuzj/1749119262749-8e4391d0-fedf-4c3f-985d-942b823a1b1c-569243.png)

**Configure Ethernet ETH1 as a static IP**

To set a static IP address for an ARM-based computer, use the_**iface**_ command to modify the gateway address, IP address, network address, netmask, and broadcast parameters of the Ethernet interface.

![1749119262895-851aef69-1171-4936-8d23-a5af49b21e50.png](./img/7FVBHB35v1gbWuzj/1749119262895-851aef69-1171-4936-8d23-a5af49b21e50-258033.png)

![1749119263091-6a3403d1-503d-4e64-af31-f3bcb1779da3.png](./img/7FVBHB35v1gbWuzj/1749119263091-6a3403d1-503d-4e64-af31-f3bcb1779da3-916313.png)

**Configure Ethernet ETH1 as a dynamic IP address**

To configure one or two Ethernet ports to request IP addresses dynamically, use the **dhcp **option in place of static in the_** iface**_ command, as shown below .

| Default Setting for ETH1 | Dynamic Setting using DHCP |
| :--- | :--- |
| auto eth1<br/>iface eth1 inet static<br/>address 192.168.3.100/24 | auto eth1<br/>iface eth1 inet dhcp |

![1749119263284-84b62e84-4fb0-4b3c-86bf-47a0b0f3ce2f.png](./img/7FVBHB35v1gbWuzj/1749119263284-84b62e84-4fb0-4b3c-86bf-47a0b0f3ce2f-432405.png)

**Enable Ethernet configuration to take effect**

After updating the Ethernet configuration file, use the ***ifdown** _ and***ifup**_ commands to make the configuration take effect.

![1749119263508-7c2cd6f0-5e27-4895-8a8d-f4695dff6034.png](./img/7FVBHB35v1gbWuzj/1749119263508-7c2cd6f0-5e27-4895-8a8d-f4695dff6034-435228.png)

<u>NOTE                                                       </u>

For more vim usage, please refer to [https://manpages.org/vim](https://manpages.org/vim)

For more Ethernet configuration, please refer to [https://www.baeldung.com/linux/network-interface-configure](https://www.baeldung.com/linux/network-interface-configure)

<u>                                                                                  </u>

### 2.4.System Management

### 2.4.1.system version

Use the _**ecversion**_ command to check the system image version of your ARM-based computer.

**To check the firmware version of your ARM-based computer, enter **_**ecversion** _

![1749119263700-db4f98a8-a5f4-4010-aca9-efb0e86660b7.png](./img/7FVBHB35v1gbWuzj/1749119263700-db4f98a8-a5f4-4010-aca9-efb0e86660b7-485028.png)

**Add the **_**–a** _**option to output complete version information**

![1749119263863-e02a48a0-af2c-44dc-a48d-a8c1147f3aee.png](./img/7FVBHB35v1gbWuzj/1749119263863-e02a48a0-af2c-44dc-a48d-a8c1147f3aee-696063.png)

### 2.4.2.Adjust the time

ARM-based computers have two time settings. One is the system time, and the other is the time maintained by the**RTC** (Real time clock ) ARM-based computer hardware. Use the _**date**_ command to query the current system time or set a new system time. Use the _**hwclock**_ command to query the current RTC time or set a new RTC time.

Use the date MMDDhhmmYYYY command to set the system time:

| MM | month |
| :--- | :--- |
| DD | date |
| hh | Hour |
| mm | minute |
| YYYY | Year |

**Get system time**

![1749119264084-d9231447-7134-464d-a9ff-fb07eb68a989.png](./img/7FVBHB35v1gbWuzj/1749119264084-d9231447-7134-464d-a9ff-fb07eb68a989-501182.png)

**Set system time**

![1749119264309-aa83b604-69f4-47de-a030-ea71279e7e5f.png](./img/7FVBHB35v1gbWuzj/1749119264309-aa83b604-69f4-47de-a030-ea71279e7e5f-081631.png)

**Get RTC time**

![1749119264530-8f0f5ea8-ad07-4745-917b-66a9b602f20f.png](./img/7FVBHB35v1gbWuzj/1749119264530-8f0f5ea8-ad07-4745-917b-66a9b602f20f-047151.png)

**Write system time to RTC**

![1749119264826-8a7ac266-3818-4ce1-ac11-d19c2ef09400.png](./img/7FVBHB35v1gbWuzj/1749119264826-8a7ac266-3818-4ce1-ac11-d19c2ef09400-656365.png)

<u>NOTE                                                       </u>

For more date and time information, please refer to [https://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html](https://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html)

[https://wiki.debian.org/DateTime](https://wiki.debian.org/DateTime)

<u>                                                                                             </u>

### 2.4.3.Adjust time zone

There are two ways to configure ARM's computer time zone. One is to use the TZ variable and the other is to use the /etc/localtime file.

**Use TZ variable**

The format of the TZ environment variable is as follows:

TZ=`<value>`HH[:MM[:SS]][summer[HH[:MM[:SS]][, start date[/starttime], end date[/endtime]]

Here are some possible settings for the North American Eastern Time Zone:

(1)TZ=EST5EDT

(2)TZ=EST0EDT

(3)TZ=EST0

In the first case, the reference time is GMT and the stored time value is correct worldwide. A simple change to the TZ variable prints local time correctly in any time zone.

In the second case, the reference time is Eastern Standard Time and the only conversion performed is to Daylight Savings Time. Therefore, there is no need to adjust the hardware clock twice a year for daylight saving time.

In the third case, the reference time is always the reported time. You can use this option if the hardware clock on the machine automatically adjusts to daylight saving time, or if you wish to manually adjust the hardware time twice a year.

![1749119265074-94447559-b59b-4e10-bafa-32d2c45eefc5.png](./img/7FVBHB35v1gbWuzj/1749119265074-94447559-b59b-4e10-bafa-32d2c45eefc5-894575.png)

You must include the TZ settings in the /etc/rc.local file. When you restart your computer, the time zone setting will be activated.

The following table lists other possible values for the TZ environment variable:

| Hours From Greenwich Mean Time (GMT) | Value | Description |
| :--- | :--- | :--- |
| 0 | GMT | Greenwich Mean Time |
| +1 | ECT | European Central Time |
| +2 | EET | European Eastern Time |
| +2 | ART | |
| +3 | EAT | Saudi Arabia |
| +3.5 | MET | Iran |
| +4 | NET | |
| +5 | PLT | West Asia |
| +5.5 | IST | India |
| +6 | BST | Central Asia |
| +7 | VST | Bangkok |
| +8 | CTT | China |
| +9 | JST | Japan |
| +9.5 | ACT | Central Australia |
| +10 | AET | Eastern Australia |
| +11 | SST | Central Pacific |
| +12 | NST | New Zealand |
| -11 | MIT | Samoa |
| -10 | HST | Hawaii |
| -9 | AST | Alaska |
| -8 | PST | Pacific Standard Time |
| -7 | PNT | Arizona |
| -7 | MST | Mountain Standard Time |
| -6 | CST | Central Standard Time |
| -5 | EST | Eastern Standard Time |
| -5 | IET | Indiana East |
| -4 | PRT | Atlantic Standard Time |
| -3.5 | CNT | Newfoundland |
| -3 | AGT | Eastern South America |
| -3 | BET | Eastern South America |
| -1 | CAT | Azores |

**Use the /etc/localtime file**

The local time zone is stored in /etc/localtime and is used by the GNU Library for C (glibc) if no value is set for the TZ environment variable. This file is either a copy of the /usr/share/zoneinfo/ file or a symbolic link to it. ARM - based computers do not provide the /usr/share/zoneinfo/ file. You should find a suitable time zone information file and overwrite the original local time file in the ARM based machine.

<u>NOTE                                                      </u>

To change the time zone through localtime, please refer to [https://linuxize.com/post/how-to-set-or-change-timezone-in-linux/](https://linuxize.com/post/how-to-set-or-change-timezone-in-linux/)

<u>                                                                               </u>

### 2.5.Determine disk space

To determine the amount of free disk space, use the _**df**_ command with the _**–h**_ option. The system returns the amount of disk space divided by file system. Here is an example:

![1749119265351-a6118cd2-268e-4001-9375-632d5274ffed.png](./img/7FVBHB35v1gbWuzj/1749119265351-a6118cd2-268e-4001-9375-632d5274ffed-216925.png)

### 2.6.Install system image

### 2.6.1.Prepare a bootable SD card

(1)Prepare a Micro SD card with a capacity of at least 16GB and a USB card reader

(2)Insert the SD card into the corresponding USB slot on your Windows system

(3)Download win32diskimager from the link address

[http://sourceforge.net/projects/win32diskimager/](http://sourceforge.net/projects/win32diskimager/)

(4)Save the attachment linux-PE.img to your local Windows computer

(5)Confirm that the Device device is the SD card drive letter, and select linux-PE.img as the Image File.

![1749119265598-f0243cae-0ca6-4b2d-b2a7-e240e21aa365.png](./img/7FVBHB35v1gbWuzj/1749119265598-f0243cae-0ca6-4b2d-b2a7-e240e21aa365-748227.png)

(6)Click the Write button and select Yes

![1749119265761-e08a7865-6b0f-446a-9b63-9b6b554f8ba2.png](./img/7FVBHB35v1gbWuzj/1749119265761-e08a7865-6b0f-446a-9b63-9b6b554f8ba2-344402.png)

(7)Waiting for production to be completed

![1749119265940-80a92bf1-01a7-4ee0-859b-7180c7387e6b.png](./img/7FVBHB35v1gbWuzj/1749119265940-80a92bf1-01a7-4ee0-859b-7180c7387e6b-892848.png)

(8)Format the SD card and select FAT32 as the file system.

![1749119266114-abb13326-d8cd-4cec-8acf-7802d857ced2.png](./img/7FVBHB35v1gbWuzj/1749119266114-abb13326-d8cd-4cec-8acf-7802d857ced2-773628.png)

### 2.6.2.Copy system image to SD card

(1)Create a flash-image folder in the root directory of the SD card

![1749119266317-78c50abb-7c21-4785-ae21-7cf99fb97126.png](./img/7FVBHB35v1gbWuzj/1749119266317-78c50abb-7c21-4785-ae21-7cf99fb97126-151935.png)

(2)Copy the system image and image MD5 file to the flash-image folder

![1749119266526-cc7f6d7f-4e83-4b09-9904-ef37218f1fb8.png](./img/7FVBHB35v1gbWuzj/1749119266526-cc7f6d7f-4e83-4b09-9904-ef37218f1fb8-414411.png)

(3)Download the Dos2Unix tool from the link address

[https://dos2unix.sourceforge.io/](https://dos2unix.sourceforge.io/)

(4)Use the dos2nuix program to convert Windows format line breaks in MD5 files to Unix format

![1749119266700-c41f1d75-80a0-4a1a-9ff2-315ad6f7e987.png](./img/7FVBHB35v1gbWuzj/1749119266700-c41f1d75-80a0-4a1a-9ff2-315ad6f7e987-546666.png)

![1749119266853-ca48e1b3-934b-44b2-9515-9e5fbc62793d.png](./img/7FVBHB35v1gbWuzj/1749119266853-ca48e1b3-934b-44b2-9515-9e5fbc62793d-697948.png)

(5)Remove SD card

### 2.6.3.ARM computer configured in mirror installation mode

(1)Power off the device and remove the 4 fixing screws on the upper cover.

![1749119267123-5e1550f3-c5e2-46a8-85f2-374c59922d62.png](./img/7FVBHB35v1gbWuzj/1749119267123-5e1550f3-c5e2-46a8-85f2-374c59922d62-228955.png)

(2)bootable SD card with the system image into the SD slot

![1749119267578-2b5b797c-0be7-4969-9a71-bcfaf4619b57.png](./img/7FVBHB35v1gbWuzj/1749119267578-2b5b797c-0be7-4969-9a71-bcfaf4619b57-022968.png)

(3)Short circuit J16 terminal

![1749119267975-54026b93-5705-487e-84de-94789997f2aa.png](./img/7FVBHB35v1gbWuzj/1749119267975-54026b93-5705-487e-84de-94789997f2aa-903483.png)

(4)The device is powered on and waits for the status light to flash.

(5)Connect the device through ETH1 and use telnet to connect to 192.168.3.100. The user name is root and there is no password.

![1749119268304-90b9fcfa-50f0-4e63-bde5-7bba1940b779.png](./img/7FVBHB35v1gbWuzj/1749119268304-90b9fcfa-50f0-4e63-bde5-7bba1940b779-018513.png)

![1749119268507-78ddcd7e-4d4f-416c-b63a-525b2abe5f0f.png](./img/7FVBHB35v1gbWuzj/1749119268507-78ddcd7e-4d4f-416c-b63a-525b2abe5f0f-688567.png)

(6)Install the system using flash command

![1749119268730-3d5f2536-921f-4aa9-a527-5bbf54771842.png](./img/7FVBHB35v1gbWuzj/1749119268730-3d5f2536-921f-4aa9-a527-5bbf54771842-622407.png)

(7)Enter the system name that appears available for installation

![1749119268891-52f08042-c270-4382-b844-f5083038808f.png](./img/7FVBHB35v1gbWuzj/1749119268891-52f08042-c270-4382-b844-f5083038808f-878320.png)

(8)Wait for flashing complete

![1749119269045-dd9210df-4600-4991-976b-fd5326df2408.png](./img/7FVBHB35v1gbWuzj/1749119269045-dd9210df-4600-4991-976b-fd5326df2408-945942.png)

(9)Disconnect the power, remove the J16 short-circuit terminal and SD card, restore the upper cover and power on again

<u>NOTE                                                       </u>

Updating the system through the flash command will not clear user data and device manufacturer solidified information (such as device model/SN number/Ethernet MAC address, etc.)

If you want to clear user data and device manufacturer firmware information, please use the flash -f command with caution.

<u>                                                                                </u>

## 3.Peripheral configuration

### 3.1.serial port

The ARM computer's serial port supports RS-232 and RS-485 with flexible baud rate settings. Each port is independent of each other. Please refer to the hardware description section in the product manual for corresponding connection and use.

The _**stty**_ command is used to view and modify serial terminal settings, as detailed below.

**Show settings details**

![1749119269218-8ee716fe-f688-4f69-8552-f6718fe55d5b.png](./img/7FVBHB35v1gbWuzj/1749119269218-8ee716fe-f688-4f69-8552-f6718fe55d5b-931521.png)

**Set the serial port baud rate to 115200**

![1749119269385-d521d310-9215-4c4e-9f10-05c5f027ae1a.png](./img/7FVBHB35v1gbWuzj/1749119269385-d521d310-9215-4c4e-9f10-05c5f027ae1a-444634.png)

**Verify setting results**

![1749119269554-f205ee93-542c-40ff-8707-a1e1bdd7d863.png](./img/7FVBHB35v1gbWuzj/1749119269554-f205ee93-542c-40ff-8707-a1e1bdd7d863-932272.png)

<u>NOTE                                                       </u>

For more ways to use stty, please refer to

[http://www.gnu.org/software/coreutils/manual/coreutils.html](http://www.gnu.org/software/coreutils/manual/coreutils.html)

<u>                                                                               </u>

### 3.2.USB and SD card

ARM-based computers offer a USB port for storage expansion . You can use the _**mkdir**_ command to create a storage mount point, use the mount command to mount a storage partition, and use the _**mkfs**_command to format the partition.

**View USB memory**

![1749119269725-8cb9d0a6-2057-4921-aa31-147a2b8d280f.png](./img/7FVBHB35v1gbWuzj/1749119269725-8cb9d0a6-2057-4921-aa31-147a2b8d280f-092549.png)

**Create USB storage mount point**

![1749119269909-80c0962f-e485-41bc-95f5-4a704283c11a.png](./img/7FVBHB35v1gbWuzj/1749119269909-80c0962f-e485-41bc-95f5-4a704283c11a-149134.png)

**Mount USB storage partition 1 to the mount point**

![1749119270077-8898c491-23c0-4098-9b94-ed1f4fe530d7.png](./img/7FVBHB35v1gbWuzj/1749119270077-8898c491-23c0-4098-9b94-ed1f4fe530d7-992908.png)

**Check the mounting status**

![1749119270253-10b94817-a621-48ed-9229-054f53ff7d4c.png](./img/7FVBHB35v1gbWuzj/1749119270253-10b94817-a621-48ed-9229-054f53ff7d4c-408445.png)

**View SD card memory**

![1749119270429-80fd11fc-1868-4723-8db6-9476159e7186.png](./img/7FVBHB35v1gbWuzj/1749119270429-80fd11fc-1868-4723-8db6-9476159e7186-989209.png)

**Create SD card storage mount point**

![1749119270598-30441b77-f682-4462-8c91-1aa9e1aec1dc.png](./img/7FVBHB35v1gbWuzj/1749119270598-30441b77-f682-4462-8c91-1aa9e1aec1dc-843538.png)

**Mount SD card memory partition 1 to the mount point**

![1749119270793-778d8a79-08dd-47d0-9e37-69f3d3692844.png](./img/7FVBHB35v1gbWuzj/1749119270793-778d8a79-08dd-47d0-9e37-69f3d3692844-365004.png)

**Check the mounting status**

![1749119270999-7abf86b1-8a34-4941-b551-689dcdee0909.png](./img/7FVBHB35v1gbWuzj/1749119270999-7abf86b1-8a34-4941-b551-689dcdee0909-070818.png)

**Unmount and format USB partition 1 as ext4 file system**

![1749119271202-8248d665-e392-486d-a674-25a3974f9365.png](./img/7FVBHB35v1gbWuzj/1749119271202-8248d665-e392-486d-a674-25a3974f9365-589927.png)

<u>NOTE                                                       </u>

Before formatting the storage, make sure the storage is not mounted to the device.

For more information on how to use the mkdir command, please refer to

[https://linuxize.com/post/how-to-create-directories-in-linux-with-the-mkdir-command/](https://linuxize.com/post/how-to-create-directories-in-linux-with-the-mkdir-command/)

For more information on how to use the mount command, please refer to

[https://www.man7.org/linux/man-pages/man8/mount.8.html](https://www.man7.org/linux/man-pages/man8/mount.8.html)

For more information on how to use the mkfs command, please refer to

[https://linuxsimply.com/mkfs-command-in-linux/](https://linuxsimply.com/mkfs-command-in-linux/)

<u>                                                                               </u>

### 3.3.CAN bus

The CAN port on the ARM computer supports CAN 2.0A/B and CAN FD standards, and the maximum data baud rate can reach 5Mbps.

### 3.3.1.Configure Socket CAN

By default, the CAN port is in the down state without initialization . If you need to configure the CAN port , please use the ip link command.

**Configure CAN port**

![1749119271406-f82163b6-e062-4bf6-932d-6f9714cd80cf.png](./img/7FVBHB35v1gbWuzj/1749119271406-f82163b6-e062-4bf6-932d-6f9714cd80cf-091449.png)

**Enable CAN port**

![1749119271606-f98a0c3b-ce5b-4f2a-8f69-020ae774beae.png](./img/7FVBHB35v1gbWuzj/1749119271606-f98a0c3b-ce5b-4f2a-8f69-020ae774beae-586546.png)

The following code is an example of the SocketCAN API, which uses the raw interface to receive and send packets .

**Send example**

```cpp
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <string.h> 
#include <net/if.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <sys/ioctl.h> 
#include <linux/can.h> 
#include <linux/can/raw.h> 
int main(void) 
{ 
    int s; 
    int nbytes; 
    struct sockaddr_can addr; 
    struct can_frame frame; 
    struct ifreq ifr; 
    char *ifname = "can1"; 
    if((s = socket(PF_CAN, SOCK_RAW, CAN_RAW)) < 0) { 
    perror("Error while opening socket");
    return -1; 
    } 
    strcpy(ifr.ifr_name, ifname); 
    ioctl(s, SIOCGIFINDEX, &ifr); 
    addr.can_family = AF_CAN; 
    addr.can_ifindex = ifr.ifr_ifindex; 
    printf("%s at index %d\n", ifname, ifr.ifr_ifindex); 
    if(bind(s, (struct sockaddr *)&addr, sizeof(addr)) < 0) { 
    perror("Error in socket bind"); 
    return -2; 
    } 
    frame.can_id = 0x123; 
    frame.can_dlc = 2; 
    frame.data[0] = 0x11; 
    frame.data[1] = 0x22; 
    nbytes = write(s, &frame, sizeof(struct can_frame)); 
    printf("Wrote %d bytes\n", nbytes); 
    return 0; 
}
```

**receive examples**

```cpp
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <string.h> 
#include <net/if.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <sys/ioctl.h> 
#include <linux/can.h> 
#include <linux/can/raw.h> 
int main(void) 
{ 
    int i; 
    int s; 
    int nbytes; 
    struct sockaddr_can addr; 
    struct can_frame frame; 
    struct ifreq ifr; 
    char *ifname = "can0"; 
    if((s = socket(PF_CAN, SOCK_RAW, CAN_RAW)) < 0) { 
    perror("Error while opening socket"); 
    return -1; 
    } 
    strcpy(ifr.ifr_name, ifname); 
    ioctl(s, SIOCGIFINDEX, &ifr); 
    addr.can_family = AF_CAN; 
    addr.can_ifindex = ifr.ifr_ifindex; 
    printf("%s at index %d\n", ifname, ifr.ifr_ifindex); 
    if(bind(s, (struct sockaddr *)&addr, sizeof(addr)) < 0) { 
    perror("Error in socket bind"); 
    return -2; 
    } 
    nbytes = read(s, &frame, sizeof(struct can_frame)); 
    if (nbytes < 0) { 
    perror("Error in can raw socket read"); 
    return 1; 
    } 
    if (nbytes < sizeof(struct can_frame)) { 
    fprintf(stderr, "read: incomplete CAN frame\n");
    return 1; 
    } 
    printf(" %5s %03x [%d] ", ifname, frame.can_id, frame.can_dlc); 
    for (i = 0; i < frame.can_dlc; i++) 
    printf(" %02x", frame.data[i]); 
    printf("\n"); 
    return 0; 
}
```

SocketCAN information will be written to the paths / proc/sys/net/ipv4/conf/can*and /proc/sys/net/ipv4/neigh/can*

<u>NOTE                                                       </u>

Before configuring the CAN interface, please ensure that the CAN interface is in down state.

For more information on how to use the CAN bus, please refer to

[https://www.kernel.org/doc/html/latest/networking/can.html](https://www.kernel.org/doc/html/latest/networking/can.html)

<u>                                                                               </u>

### 3.4.Analog input detection

The analog input port on the ARM computer supports 4-20mA current signal detection, and the current value can be read using the cat command.

![1749119271824-28a9299a-6cd8-40ee-9f39-e952c4631348.png](./img/7FVBHB35v1gbWuzj/1749119271824-28a9299a-6cd8-40ee-9f39-e952c4631348-400745.png)

<u>NOTE                                                       </u>

The unit of current value obtained by analog input detection is microampere.

<u>                                                                               </u>

### 3.5.Digital input and output

ARM computers have multiple channels of digital input detection and digital output control. You can use the cat command to query the GPIO information corresponding to the digital interface.

**Query digital input and output through cat command**

![1749119271996-4337a396-7d48-49a5-8a5b-c9a25dfadd48.png](./img/7FVBHB35v1gbWuzj/1749119271996-4337a396-7d48-49a5-8a5b-c9a25dfadd48-540955.png)

| Digital input and output channels | device node |
| :--- | :--- |
| DI0 | /sys/class/gpio/gpio454 |
| DI1 | /sys/class/gpio/gpio455 |
| DI2 | /sys/class/gpio/gpio456 |
| DI3 | /sys/class/gpio/gpio457 |
| DO0 | /sys/class/gpio/gpio323 |
| DO1 | /sys/class/gpio/gpio453 |
| DO2 | /sys/class/gpio/gpio465 |
| DO3 | /sys/class/gpio/gpio461 |

**Read digital input status through **_**cat** _**command**

![1749119272229-85887b7b-3224-4c6b-ab23-28e64116c043.png](./img/7FVBHB35v1gbWuzj/1749119272229-85887b7b-3224-4c6b-ab23-28e64116c043-623575.png)

**Control digital output status through **_**echo** _**command**

![1749119272433-e0b616a2-1e50-4ccc-a004-067165f7f3c6.png](./img/7FVBHB35v1gbWuzj/1749119272433-e0b616a2-1e50-4ccc-a004-067165f7f3c6-673313.png)

<u>NOTE                                                       </u>

Avoid **'Permission denied'** when **'sudo echo x >'**, because the redirection symbol ">" is also a _**bash**_ command. Sudo only allows the**echo **command to have **root permissions**, but **does not allow** the ">" command to also have root permissions, so _**bash** _ will think that this command does not have the permission to write information. At this time, you need to use ***sudo su -c***  command to handle it.

<u>                                                                               </u>

### 3.6.User programmable keys

ARM computers provide programmable buttons, which are provided to users for development and use using the **event** event process. The event corresponding to the button is /dev/input/event0.

**Reference example**

```cpp
#include <stdio.h>
#include <linux/input.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
 
#define DEV_PATH "/dev/input/event0"

int main()
{
    int keys_fd;
    char ret[2];
    struct input_event t;
    keys_fd = open(DEV_PATH, O_RDONLY);
    if(keys_fd <= 0)
    {
        printf("open /dev/input/event0 device error!\n");
        return -1;
    }
    while(1)
    {
        if(read(keys_fd, &t, sizeof(t)) == sizeof(t))
        {
            if(t.type == EV_KEY)
                if(t.value==0 || t.value==1)
                {
                    printf("key %d %s\n", t.code, (t.value) ? "Pressed" : "Released");
                    if(t.code == KEY_ESC)
                        break;
                }
        }
    }
    close(keys_fd);
    return 0;
}
```

<u>NOTE                                                       </u>

For more information on **how to use events**, please refer to

[https://askubuntu.com/questions/826719/decoding-key-values-from-dev-input-eventx-in-c](https://askubuntu.com/questions/826719/decoding-key-values-from-dev-input-eventx-in-c)

<u>                                                                               </u>

### 3.7.LED

There are multiple user-programmable LEDs on the ARM computer. You can use the _**ls**_ command to view the LED nodes and the _**echo**_ command to control the LEDs.

![1749119272583-84e9a650-e4de-495c-bbb4-3b36ada6d904.png](./img/7FVBHB35v1gbWuzj/1749119272583-84e9a650-e4de-495c-bbb4-3b36ada6d904-266057.png)

**Light up USER LED**

![1749119272770-a5f01702-65cf-4bf9-bf54-56be431fa5af.png](./img/7FVBHB35v1gbWuzj/1749119272770-a5f01702-65cf-4bf9-bf54-56be431fa5af-216511.png)

**Make USER LED blink**

![1749119272960-bdf605c1-666d-4f3b-bc3a-907b627f3eec.png](./img/7FVBHB35v1gbWuzj/1749119272960-bdf605c1-666d-4f3b-bc3a-907b627f3eec-940813.png)

<u>NOTE                                                       </u>

For more LED usage methods, please refer to

[https://www.kernel.org/doc/html/latest/leds/leds-class.html](https://www.kernel.org/doc/html/latest/leds/leds-class.html)

[https://raspberrypi.stackexchange.com/questions/697/how-do-i-control-the-system-leds-using-my-software](https://raspberrypi.stackexchange.com/questions/697/how-do-i-control-the-system-leds-using-my-software)

<u>                                                                               </u>

### 3.8.TPM

ARM computers provide **TPM2.0** hardware support and are pre-installed with the **tpm2-tools tool**, which can be used to test and verify **TPM2.0**.

**Generate random numbers**

![1749119273175-3ab27bb3-de71-43b4-9b50-244d98d46ea0.png](./img/7FVBHB35v1gbWuzj/1749119273175-3ab27bb3-de71-43b4-9b50-244d98d46ea0-040600.png)

<u>NOTE                                                       </u>

For more information on how to use tpm2-tools, please refer to

[https://tpm2-tools.readthedocs.io/en/latest/](https://tpm2-tools.readthedocs.io/en/latest/)

<u>                                                                               </u>

## 4.Wireless connections

The instructions in this chapter cover all wireless features supported by Inhand ARM-based computers. Before referring to sections in this chapter, please make sure that those sections apply to the hardware specifications of the ARM computer platform.

### 4.1.Cellular settings

In cellular control based on ARM computers, it is necessary to control the cellular power switch and dual-card switching switch. Both switches are switched and enabled through GPIO.

| | device node | value | state | default |
| --- | :--- | :--- | :--- | :--- |
| cellular power control | /sys/class/gpio/gpio401/value | 1 | enable | |
| | | 0 | disable | ✔ |
| SIM card switch | /sys/class/gpio/gpio405/value | 1 | SIM card 2 | |
| | | 0 | SIM card 1 | ✔ |

<u>NOTE                                                       </u>

When using cellular, you need to confirm which card slot the current SIM card is in or which SIM card slot you want to use for dialing. You need to switch to the required SIM card before enabling cellular power, otherwise the cellular module will fail to check the card.

<u>                                                                               </u>

**Switch SIM to SIM card 1**

![1749119273323-7c025a45-70c3-47a8-b078-d8a8b9c61f67.png](./img/7FVBHB35v1gbWuzj/1749119273323-7c025a45-70c3-47a8-b078-d8a8b9c61f67-245076.png)

**Enable cellular module**

![1749119273495-e0e718f7-bd19-4b7e-b378-1deadb55458f.png](./img/7FVBHB35v1gbWuzj/1749119273495-e0e718f7-bd19-4b7e-b378-1deadb55458f-952237.png)

**Query module model**

![1749119273677-e89f48fa-23e3-436c-b13c-c7b4a6c36e52.png](./img/7FVBHB35v1gbWuzj/1749119273677-e89f48fa-23e3-436c-b13c-c7b4a6c36e52-836690.png)

You can query the cellular module used by the current hardware device through the _**envtools**_ command, where _**cell-***_ represents the module model (the current device uses the FQ53 module)

**Dial using PPPD**

ARM-based computers support the PPPD dial-up function. PPPD dial-up scripts are different for different types of cellular modules. The detailed dial-up scripts and module correspondences are as follows.

| cellular module | PPPD chat script |
| :--- | :--- |
| LQA3 | quectel-ppp-ttyUSB2 |
| MOD1 | quectel-ppp-ttyUSB4 |
| FQ73 | quectel-ppp-ttyUSB5 |
| FQ53 | quectel-ppp-ttyUSB5 |
| FQ33 | quectel-ppp-ttyUSB3 |

![1749119273841-374af37d-9df8-4068-bf48-c43167a7abcb.png](./img/7FVBHB35v1gbWuzj/1749119273841-374af37d-9df8-4068-bf48-c43167a7abcb-685659.png)

![1749119274023-d92f1bf6-27eb-4ba4-862d-3c666a19d47b.png](./img/7FVBHB35v1gbWuzj/1749119274023-d92f1bf6-27eb-4ba4-862d-3c666a19d47b-165020.png)

![1749119274197-d247ce8c-3a00-4b46-8f93-5a0c78a62fc5.png](./img/7FVBHB35v1gbWuzj/1749119274197-d247ce8c-3a00-4b46-8f93-5a0c78a62fc5-232242.png)

<u>NOTE                                                       </u>

The PPPD dial-up script configured by the device by default is the most basic dial-up implementation and does not configure APN and other information. If you need to configure APN or use richer module functions, you need to change /etc/ppp/peers/quectel-ppp-ttyUSB* script

<u>                                                                               </u>

### 4.2.Wi-Fi settings

ARM computers support Wi-Fi configuration, and you can use the wpa_supplicant tool to configure and use Wi-Fi .

**Enable Wi-Fi**

![1749119274412-be7ea7c1-529d-49f9-8f19-730704effc96.png](./img/7FVBHB35v1gbWuzj/1749119274412-be7ea7c1-529d-49f9-8f19-730704effc96-204039.png)

**Add wpa_supplicant.conf configuration file**

![1749119274601-32c223ce-dede-43c2-a0e9-a2578e30db87.png](./img/7FVBHB35v1gbWuzj/1749119274601-32c223ce-dede-43c2-a0e9-a2578e30db87-238264.png)

![1749119274792-798f21f3-c3c6-44bc-bdcc-53211cda68d6.png](./img/7FVBHB35v1gbWuzj/1749119274792-798f21f3-c3c6-44bc-bdcc-53211cda68d6-854455.png)

![1749119274975-1490ceec-d6b1-437a-b065-352e14b0d4a1.png](./img/7FVBHB35v1gbWuzj/1749119274975-1490ceec-d6b1-437a-b065-352e14b0d4a1-406504.png)

**Start wpa_supplicant service**

![1749119275220-4cac6348-bfa2-4834-9af4-189b97dabdf8.png](./img/7FVBHB35v1gbWuzj/1749119275220-4cac6348-bfa2-4834-9af4-189b97dabdf8-753219.png)

**Scan for hotspots**

![1749119275412-903a966c-fd04-4185-accc-431ab1b1a165.png](./img/7FVBHB35v1gbWuzj/1749119275412-903a966c-fd04-4185-accc-431ab1b1a165-128103.png)

**Query scan results**

![1749119275653-8e2d11cd-f924-44f7-b4ff-5a627c8f812a.png](./img/7FVBHB35v1gbWuzj/1749119275653-8e2d11cd-f924-44f7-b4ff-5a627c8f812a-505843.png)

**Add new connection**

![1749119275831-8ceaf720-6d23-4158-93aa-7093579bb92c.png](./img/7FVBHB35v1gbWuzj/1749119275831-8ceaf720-6d23-4158-93aa-7093579bb92c-949554.png)

**save connection**

![1749119276021-61c34bf9-bafa-451a-b074-b74c7c37cfd7.png](./img/7FVBHB35v1gbWuzj/1749119276021-61c34bf9-bafa-451a-b074-b74c7c37cfd7-088130.png)

**Enable connection**![1749119276235-7cc71d6e-a4ed-453b-bf43-2c2730fa7e66.png](./img/7FVBHB35v1gbWuzj/1749119276235-7cc71d6e-a4ed-453b-bf43-2c2730fa7e66-201781.png)

**Enable DHCP**

![1749119276422-d728394d-1f6d-432e-b63b-65a1c73e8ef4.png](./img/7FVBHB35v1gbWuzj/1749119276422-d728394d-1f6d-432e-b63b-65a1c73e8ef4-121403.png)

**Disconnect**

![1749119276611-dd0627df-d1a1-4638-a20c-d5f37a82db8f.png](./img/7FVBHB35v1gbWuzj/1749119276611-dd0627df-d1a1-4638-a20c-d5f37a82db8f-948517.png)

**List saved connections**

![1749119276800-1c8602fd-f8f5-4d1b-a7c5-717e89727392.png](./img/7FVBHB35v1gbWuzj/1749119276800-1c8602fd-f8f5-4d1b-a7c5-717e89727392-969356.png)

<u>NOTE                                                       </u>

For more information on how to use wpa_supplicant, please refer to

[https://wiki.archlinux.org/title/Wpa_supplicant](https://wiki.archlinux.org/title/Wpa_supplicant)

<u>                                                                                 </u>

## 5.Safety

SSH connections for the root account are disabled for increased security . sudo is a program designed to allow users permitted by the system administrator to execute programs as root. The goal is to grant as few privileges as possible but still allow the user to gain appropriate root privileges . Using sudo is better (or safer) than opening a session as root for many reasons, including:

1. No one needs to know the root password (sudo prompts for the current user's password). Additional privileges can be granted temporarily to individual users and then no password changes are required.
2. It's easy to run only the commands that require special permissions via sudo; the remaining commands are executed as an unprivileged user, reducing the damage caused by errors.
3. As the example shows, some system-level commands are not directly available to user edge

The output is as follows:

![1749119276981-b1b8f948-2045-4ce9-9590-104ede86b05f.png](./img/7FVBHB35v1gbWuzj/1749119276981-b1b8f948-2045-4ce9-9590-104ede86b05f-244216.png)

## 6.Start, recover and update

### 6.1.recover

ARM computers provide two system reset mechanisms, one is based on the **update** command method, and the other is based on the **reset** button mechanism.

**Based on update command mode**

Enter ***sudo update reset*** and then enter_**yes**_ according to the prompts. The ARM computer will automatically restart and reset the system.

![1749119277168-e7833e3c-0db5-4215-84d1-70b1aa0561a6.png](./img/7FVBHB35v1gbWuzj/1749119277168-e7833e3c-0db5-4215-84d1-70b1aa0561a6-786256.png)

**Based on reset button mechanism**

The reset button mechanism relies on the **reset_monitor.service**. This service is not added to the boot list by default and is not enabled.

**To add it to the boot auto-start list, please use **_** sudo systemctl enable reset_monitor**_

![1749119277337-9027e717-c665-476e-a014-11fb0abb2104.png](./img/7FVBHB35v1gbWuzj/1749119277337-9027e717-c665-476e-a014-11fb0abb2104-483944.png)

**To delete from the boot auto-start list, use **_** sudo systemctl disable reset_monitor**_**.**

![1749119277504-e153516a-ba90-4471-89af-0d498e77f1d5.png](./img/7FVBHB35v1gbWuzj/1749119277504-e153516a-ba90-4471-89af-0d498e77f1d5-920864.png)

**To start the reset_monitor service, please use **_** sudu systemctl start reset_monitor**_

![1749119277705-21a05fdb-c0b8-4242-b731-a0841172dacb.png](./img/7FVBHB35v1gbWuzj/1749119277705-21a05fdb-c0b8-4242-b731-a0841172dacb-575323.png)

**To query the reset_monitor service status, please use **_** sudu systemctl status reset_monitor**_

![1749119277903-7ef8532c-2671-4905-98ff-f5b46195f9d9.png](./img/7FVBHB35v1gbWuzj/1749119277903-7ef8532c-2671-4905-98ff-f5b46195f9d9-550790.png)

**Use the reset button to reset the system**

After the reset_monitor.service service is started, the system can be reset by pressing the reset button. When pressed for more than 10 seconds, the warn LED will light up. After pressing for more than 20s, the warn LED will turn off. Release the reset button when the warn LED is on, and the ARM computer will automatically restart and reset the system.

<u>NOTE                                                       </u>

System reset is an important function for ARM computers. After system reset, ARM computers will be restored to the default state. At this time, all user data and configurations will be lost.

Before performing a system reset on an ARM computer, please ensure that critical data is effectively backed up and transferred to external storage media such as removable disks.

After the system is reset, the reset_monitor service will be deleted from the auto-start list. If you want to reset the system through the reset button again, please reconfigure it according to the reset button mechanism mentioned above.

<u>                                                                                 </u>

### 6.2.Update

### 6.2.1.App update, installation and download

ARM computer provides a complete application update strategy based on the distribution Linux system (Debian 11). You can use the apt command to update and install applications online, and the _**dpkg**_ command to install offline application packages.

**Update and install applications online using apt command**

The first and most important step is to synchronize the package index file in the ARM. This file will be updated synchronously from the source repository specified in /etc/apt/sources.list. When a synchronization is performed, package-related information, including versions and dependencies, are also downloaded from the repository. To perform a sync, make sure your network can connect to the apt repository, then run the_**apt-get update**_ command with root privileges.

![1749119278083-e477809a-ef8e-4e26-a717-2308eec353ae.png](./img/7FVBHB35v1gbWuzj/1749119278083-e477809a-ef8e-4e26-a717-2308eec353ae-229884.png)

Next, you can use ***sudo apt-get install <packages name>*** to download and install new applications and use_**sudo apt-get upgrade <packages name>**_to update installed applications, such as installing cron applications.

![1749119278275-ef939a66-ec66-4256-8446-ad66518f2d20.png](./img/7FVBHB35v1gbWuzj/1749119278275-ef939a66-ec66-4256-8446-ad66518f2d20-424920.png)

**Use **_** dpkg -l**_**to display the list of installed applications**

![1749119278472-678cfdf0-2b01-4295-8e06-06cace5d161f.png](./img/7FVBHB35v1gbWuzj/1749119278472-678cfdf0-2b01-4295-8e06-06cace5d161f-372447.png)

**Install offline using **_** dpkg -i <packages-name.deb>**_

![1749119278677-c7689437-4c7b-4d06-bd46-b51778d30aad.png](./img/7FVBHB35v1gbWuzj/1749119278677-c7689437-4c7b-4d06-bd46-b51778d30aad-113733.png)

<u>NOTE                                                       </u>

For more information on how to use the apt command, please refer to

[https://linuxize.com/post/how-to-use-apt-command/](https://linuxize.com/post/how-to-use-apt-command/)

For more information on how to use the dpkg command, please refer to

[https://linuxize.com/post/how-to-use-apt-command/](https://linuxize.com/post/how-to-use-apt-command/)

Dependency issues may occur when using dpkg to install offline software

dpkg: error processing package bcron (--install):

dependency problems - leaving unconfigured

At this time, you need to install the dependent software according to the prompts and try

<u>                                                                                 </u>

### 6.2.2.ARM computer version update

**Prepare a removable USB memory or SD card for version updates**

(1)Format removable USB memory or SD card to FAT32 file system

![1749119278869-0e89a107-c6a9-47d6-a6a4-8d30060cb342.png](./img/7FVBHB35v1gbWuzj/1749119278869-0e89a107-c6a9-47d6-a6a4-8d30060cb342-001151.png)

(2)Create the ec300_img folder in the root directory of the file system

![1749119279014-f8a63cad-ba23-4a81-b33c-6f73c1eea0e7.png](./img/7FVBHB35v1gbWuzj/1749119279014-f8a63cad-ba23-4a81-b33c-6f73c1eea0e7-114679.png)

(3)Copy the mirroring and image MD5 files that need to be updated on the ARM computer to the ec300_img directory

![1749119279212-17430ebd-edb7-43fb-b250-8af82b159502.png](./img/7FVBHB35v1gbWuzj/1749119279212-17430ebd-edb7-43fb-b250-8af82b159502-291461.png)

(4)Use the dos2nuix program to convert Windows format line breaks in MD5 files to Unix format

![1749119279422-c951c370-262f-4df2-a1e0-d57f2685a6f3.png](./img/7FVBHB35v1gbWuzj/1749119279422-c951c370-262f-4df2-a1e0-d57f2685a6f3-133102.png)

(5)Insert the removable USB memory or SD card into the ARM computer, enter sudo update, and enter yes when prompted.

![1749119279576-18391446-b7fa-437e-bc78-b3e9ef90ec7c.png](./img/7FVBHB35v1gbWuzj/1749119279576-18391446-b7fa-437e-bc78-b3e9ef90ec7c-796613.png)

(6)The system will automatically restart and update the system. During the system update process, the warn LED will flash. After the update is completed, the ARM computer will automatically restart.

(7)After the update is complete, you can use the ***sudo ecversion*** command to check the current ARM computer version

<u>NOTE                                                       </u>

When a removable USB memory and an SD card are connected at the same time, the ARM computer will determine whether there is an updateable image in the two memories. If there is an updateable image in both memories, the image in the removable USB memory will be started by default for update.

<u>                                                                                 </u>

## 7.Programming instructions

ARM computer supports application natively compilating and cross-compilation. Native compilation is simpler because all the coding and compilation can be done directly on the device. However, the ARM architecture is less powerful and therefore compiles slower. To overcome it, you can use a toolchain to compile the code on a Linux machine, which will compile much faster.

### 7.1.Native compilation environment

Follow these steps to update the program:

(1)Make sure the network connection is available

(2)Use ***apt-get update*** command to update the Debian package list

![1749119279767-d9b47cc4-670c-4179-8b8e-65ca0f0e9cfb.png](./img/7FVBHB35v1gbWuzj/1749119279767-d9b47cc4-670c-4179-8b8e-65ca0f0e9cfb-181270.png)

(3)Install local compilation toolchain

![1749119279941-e29c7e2b-3e98-471a-ae27-7eb4ca789448.png](./img/7FVBHB35v1gbWuzj/1749119279941-e29c7e2b-3e98-471a-ae27-7eb4ca789448-542709.png)

### 7.2.Cross-compilation environment

Cross-compilation is a method of using a cross-compilation tool chain to compile a program that can be recognized and executed by an ARM computer on an x86 platform computer. Before cross-compiling an ARM computer executable program, you need to prepare an x86_64 Ubuntu operating system version 18.04 or above platform computer.

**Download the cross-compilation toolchain on your local computer**

wget [**https://developer.ARM.com/-/media/Files/downloads/gnu-a/9.2-2019.12/binrel/gcc-ARM-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz**](https://developer.arm.com/-/media/Files/downloads/gnu-a/9.2-2019.12/binrel/gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz)

![1749119280189-bd87bc1a-fb55-4c4a-b618-713b1631f355.png](./img/7FVBHB35v1gbWuzj/1749119280189-bd87bc1a-fb55-4c4a-b618-713b1631f355-970155.png)

### 7.3.Sample program

Use vim to compile the hello.c file locally and use gcc to compile it into a hello executable program.

**Sample code**

![1749119280334-e06a5eb2-77ac-4df9-9784-ea4fff96ed2b.png](./img/7FVBHB35v1gbWuzj/1749119280334-e06a5eb2-77ac-4df9-9784-ea4fff96ed2b-263873.png)

**Compile using gcc**

![1749119280570-f732ce9b-62e3-4347-aed4-777f5d67cf2d.png](./img/7FVBHB35v1gbWuzj/1749119280570-f732ce9b-62e3-4347-aed4-777f5d67cf2d-870583.png)

**Give hello executable permissions**

![1749119280779-2090797b-e00c-4a87-b691-58f87ecfba48.png](./img/7FVBHB35v1gbWuzj/1749119280779-2090797b-e00c-4a87-b691-58f87ecfba48-791515.png)

**Execute hello program**

![1749119280955-31ec9f98-2907-4b05-b88d-33c4994e1acf.png](./img/7FVBHB35v1gbWuzj/1749119280955-31ec9f98-2907-4b05-b88d-33c4994e1acf-063081.png)

<u>NOTE                                                       </u>

Please refer to the compilation method based on make and makefile.

[https://linuxhandbook.com/using-make/](https://linuxhandbook.com/using-make/)

For Linux development based on C language, please refer to

[https://linuxconfig.org/c-development-on-linux-introduction-i](https://linuxconfig.org/c-development-on-linux-introduction-i)

<u>                                                                                 </u>
