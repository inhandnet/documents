This document is used to explain the basic configuration operations of InGateway902 (IG902 for short) networking, software version update, etc., so that users can master the basic configuration of IG902 and the use of common functions.

# 1\. Configure IG902 Network Parameters[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#configure-ig902-network-parameters "Permalink to this headline")  

## 1.1 Access the IG902[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#access-the-ig902 "Permalink to this headline")  

-   Step 1: By default, the IP address of GE 0/1 on IG902 is 192.168.1.1; the IP address of GE 0/2 on IG902 is 192.168.2.1. This document uses the GE 0/2 port to access the IG902 as an example. Set the PC’s IP address to be on the same subnet with GE 0/2.
    
    -   Method 1: Enable the PC to obtain an IP address automatically (recommended)
        
        ![](images/img_594d3d19.png)
        
    -   Method 2: Set a fixed IP address
        
        Select Use the following IP address, enter an IP address (By default,any from 192.168.2.2 to 192.168.2.254), subnet mask (By default,255.255.255.0), default gateway (By default,192.168.2.1), and DNS server address, and click OK.
        
        ![](images/img_b89d3808.png)
        
-   Step 2: Launch the browser on the PC and access the IP address of GE 0/2. Enter the login user name and password. The default user name and password are adm and 123456 respectively.
    
    ![](images/img_3b04186d.png)
    
-   Step 3: After successful login, you can see the web page as shown below:
    
    ![](images/img_2bcecb94.png)
    
-   Step 4: To change the user name and password for logging in to the web management interface of IG902, choose System > User Management page of IG902 and set the new user name and password.
    
    ![](images/img_55e0c69c.png)
    
-   Step 5: To change the IP address of GE 0/2, choose Network > Network Interfaces > Ethernet > Gigabitethernet 0/2 page of IG902 to configure GE 0/2.
    
    ![](images/img_8e76ad7d.png)
    

## 1.2 Connect IG902 to the Internet[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#connect-ig902-to-the-internet "Permalink to this headline")  

-   Method 1: Connect to the Internet by SIM card
    
    -   Step 1: Insert the SIM card. (Note: Before inserting or removing the SIM card, unplug the power cable; otherwise, the operation may cause data loss or damage the IG902.) After inserting the SIM card, connect the 4G LTE antenna to the ANT interface and power on the IG902.
        
        ![](images/img_44a1c2e2.png)
        
    -   Step 2: Choose Network > Network Interfaces > Cellular page of IG902 and select Enable Cellular and click Submit.
        
        ![](images/img_196de994.png)
        
        When the network connection status is Connected and an IP address has been allocated, the IG902 has been connected to the Internet with the SIM card.
        
        ![](images/img_6b186e82.png)
        
-   Method 2: Connect to the Internet by Ethernet
    
    -   Step 1: Use the Ethernet cable to connect the GE 0/1 and GE 0/2 ports of the IG902 respectively, as shown below:
        
        ![](images/img_a50b04d3.png)
        
    -   Step 2: Choose Network > Network Interface > Ethernet > Gigabit Ethernet 0/1 page of IG902 to configure the IP address of the GE 0/1 port and click Submit. (When the network type is a static IP address, you need to configure the IP, subnet mask, and other information according to the site network conditions.)
        
        ![](images/img_3a613213.png)
        
        ![](images/img_08e8f3fb.png)
        
    -   Step 3: Choose Network > Static Routing > Configuration page of IG902 to add a static route for GE 0/1 port and click Submit. (Select “Gigabitethernet 0/1” for the interface item, and configure the other items according to the site network conditions.)
        
        ![](images/img_dfa0add1.png)
        
    -   Step 4: Choose System > Network Tools page of IG902 and use the Ping tool to check whether the IG902 has successfully connected to the Internet. The following figure shows that IG902 have successfully connected to the Internet:
        
        ![](images/img_100902f1.png)
        

# 2\. Update the Software[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#update-the-software "Permalink to this headline")  

To obtain the latest software version of IG902 and updated functions, please visit the [](http://www.inhand.com) [Resource](http://www.inhand.com). To update the IG902 software version, do as follows.

## 2.1 Update the IG902 firmware.[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#update-the-ig902-firmware "Permalink to this headline")

Choose System > Firmware Upgrade. Select a firmware file and click Start Upgrading. After the update is completed, you are prompted to restart the system to Apply the new firmware.

![](images/img_5d21c1cd.png)

## 2.2 Upgrade the Python SDK of IG902.[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#upgrade-the-python-sdk-of-ig902 "Permalink to this headline")

Choose Edge Computing > Python Edge Computing. Select Python Engine, select an Python SDK file, and click Upgrade; when the upgrade confirmation window pops up, click Confirm. Then the IG902 automatically performs the upgrade.

![](images/img_a9323b16.png)

## 2.3 Upgrade the Docker SDK of IG902.[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#upgrade-the-docker-sdk-of-ig902 "Permalink to this headline")

Choose Edge Computing > Docker Manager, close the Docker Manager and import the Docker SDK.

![](images/img_dc857fcb.png)

After importing, IG902 will automatically install the Docker SDK. The installation process usually takes 1-2 minutes. Please be patient. After successful installation, select Enable Docker Manager and click Submit.

![](images/img_103f6982.png)

After enabling the Docker Manager, you can click the access button of the Docker Manager to access the management page.

![](images/img_6af58d66.png)

Enter the account and password set in the figure above to log in to the Docker Manager.

![](images/img_0f84657b.png)

# 3\. Python Edge Computing[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#python-edge-computing "Permalink to this headline")  

### 3.1 Install and run Python App[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#install-and-run-python-app "Permalink to this headline")

To install and run Python App (App for short) in IG902, please refer to the following process:

-   Step 1: Install the App
    
    Before installing the App, you need to ensure that the Python Edge Computing Engine is enabled and the Python SDK is installed, as shown in the following figure:
    
    ![](images/img_ffbc2629.png)
    
    Choose Edge Computing > Python Edge Computing. click the Add button and select the App package file to be installed, then click OK.
    
    ![](images/img_dd72bd28.png)
    
    After importing, you can view the imported Apps, as shown in the following figure:
    
    ![](images/img_ed93e881.png)
    
-   Step 2: Run the App
    
    Select enable App and click Submit.
    
    ![](images/img_aa50e704.png)
    
    Once enabled, the App automatically runs and will run every time the IG902 is started.
    
    ![](images/img_79c7c89e.png)
    

### 3.2 Update Configuration File for App[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#update-configuration-file-for-app "Permalink to this headline")

If the installed App supports importing configuration files to modify the running mode, you can update the App running configuration by referring to the following process:

-   Step 1: Choose Edge Computing > Python Edge Computing, click the Import Configuration button and select the configuration file to be imported, then click Confirm.
    
    ![](images/img_2a953439.png)
    
-   Step 2: Restart the App after the import is successful. After the App restarts, it will runing according to the imported configuration file.
    
    ![](images/img_9a919bc8.png)
    

### 3.3 Update Python App version[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#update-python-app-version "Permalink to this headline")

Generally, if you need to update the Python App version, you only need to import the new version of the App on the Edge Computing > Python Edge Computing page.

![](images/img_41be4c37.png)

After the update is completed, as shown below：

![](images/img_3d625e15.png)

### 3.4 Enable the Debug Mode[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#enable-the-debug-mode "Permalink to this headline")

To run and debug Python code on IG902, you need to enable IG902’s debug mode. Choose Edge Computing > Python Edge Computing, select Enable Debug Mode. After enabling, you can develop IG902 through VS Code. How to use VS Code for Python development of IG902, please refer to [Quick Start for MobiusPi Python Development](http://sdk.ig.inhandnetworks.com/en/latest/MobiusPi-Python-QuickStart-EN.html).

![](images/img_695a16ce.png)

After the debugging mode is enabled, IG902 will start an SSH server to listen on port 222 of LAN (default IP address being 192.168.2.1). The user name and password of the SSH server are displayed on the previous web page. A random password is generated every time the debugging mode is enabled or the IG902 is restarted to ensure security.

# 4\. Device Manager[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#device-manager "Permalink to this headline")  

The Device Manager developed by InHand supports functions such as monitoring IG902 status, remote maintenance of equipment, remote batch delivery of IG902 configuration, and IG902 batch upgrade, helping users to conveniently and efficiently manage IG902 and field devices. In order to enable the Device Manager to remotely manage the IG902 and field devices, the IG902 needs to be connected to the cloud platform. The connection method is as follows:Choose System Management > Device Manager, tick Enable Device Manager and configure the corresponding server address and registered account, and click Submit after the configuration is complete.

-   Server address: the address of the Device Manager. The address of the Device Manager developed by InHand is as follows:
    
    -   Device Manager：`iot.inhandnetworks.com`
    -   InConnect：`ics.inhandnetworks.com`
-   Registered account: the Device Manager account associated with the IG902 device (if you have not registered an account, you need to register an account first)
-   Advanced settings: Contains configurations such as heartbeat interval. Generally, you can use the default configuration.

![](images/img_f2af3a47.png)

After the IG902 is successfully connected to the Device Manager, the status is described as Connection Accepted.

![](images/img_9be34ab1.png)

# 5\. I/O Module[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#i-o-module "Permalink to this headline")  

Note: The following information is only for the IG902 with IO module shown in the figure below

![](images/img_58baad1f.png)

IG902 supports the digital input, pulse counting, digital output, and pulse output functions. In addition, IG902 can remotely read I/O status data or report it to the cloud platform through Modbus TCP. I/O in each mode is defined as follows:

-   Digital input (Dry contacts and wet contacts are specified based on actual connections.)
    
    -   Channels: 4
        
    -   Dry contacts  
        
        0: Open
        
        1: Close to DlCOM
        
        The following figure shows the connection modes.
        
    -   Wet contacts
        
        0: 0 V DC to 3 V DC/-3 V DC to 0 V DC
        
        1: 10 V DC to 30 V DC/-30 V DC to -10 V DC (4 mA min.)  
        
    -   Isolation: 3000 Vrms
        
        The following figure shows the connection modes.
        
        ![](images/img_87a49f9f.png)
        
-   Pulse counting  
    

-   Channels: 4
    
-   Input Frequency: 50 kHz max.  
    
-   Maximum Count: 4294967296(32 bit)  
    

     The following figure shows the connection modes.  

![](images/img_f4ba8eef.png)  

-   Digital output  
    

1.  Channels: 4  
    
2.  0: OFF  
    
3.  1: ON. Open collector to 30 V, 500 mA max.(per channel) for resistance load.  
    
4.  Isolation: 3000 Vrms

     The following figure shows the connection modes.  

![](images/img_0899b4cf.png)  

-   Pulse output
    
    A maximum of 5000 Hz pulse signal output is supported. The following figure shows the connection modes.
    
    ![](images/img_c27f1101.png)
    

The procedure for configuring I/O and obtaining I/O status data is as follows:

-   Step 1: Choose “Edge Computing > IO Module > Configuration”, and configure the I/O functions based on the site requirements. The following figures show a configuration example.
    
    -   Digital input
        
        ![](images/img_45c38d7f.png)
        
    -   Pulse counting
        
        The starting value is 0. After power down, the value counted by the power down is retained.
        
        ![](images/img_fa88dcc1.png)
        
    -   Digital output
        
        ![](images/img_5146c650.png)
        
    -   Pulse output
        
        According to the frequency of 5000 Hz, the duty cycle is 50% for the pulse output.
        
        ![](images/img_a81a0fc9.png)
        
-   Step 2 (optional): Set the pulse counting and pulse output.
    
    After setting DI to the pulse counting, click Start to count the pulses received by the DI. Otherwise, do not count it. Click Reset to reset the count value to the starting value.
    
    ![](images/img_ca451e4b.png)
    
    After setting DO to the pulse counting, click Start to output pulses based on the specified output frequency. Otherwise, do not output pulses.
    
    ![](images/img_442dc407.png)
    
-   Step 3: Set Modbus TCP Slave.
    
    Turn on the **Enable** switch to enable the Modbus TCP Slave function. This function allows Modbus TCP Master to read the I/O status of IG902. After you turn on the **External Access** switch, Modbus TCP Master outside the gateway can read the I/O status of IG902, such as the SCADA software. Set other parameters based on the site requirements. The following figure shows a configuration example.
    
    ![](images/img_409a2327.png)
    
-   Step 4: Read the I/O status through Modbus TCP.
    
    Use Device Supervisor to read the I/O status of IG902 in Step 3 as an example. First, add a Modbus TCP controller and set the controller communication parameters based on Modbus TCP Slave.
    
    ![](images/img_7472f4ae.png)
    
    Then, configure the data to be collected according to the Modbus mapping table. For example, read **DI0 Counter Value** as an example.
    
    ![](images/img_6b53f01b.png)
    
    ![](images/img_45444eb4.png)
    
    After the configuration is completed, you can obtain **DI0 Counter Value**.
    
    ![](images/img_f3986c36.png)  
    

# Appendix[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#appendix "Permalink to this headline")  

## Factory reset[](http://manual.ig.inhandnetworks.com/en/latest/IG902-Quick-Start-Manual.html#factory-reset "Permalink to this headline")  

There are two ways to restore the IG902 to factory settings: hardware factory reset and software factory reset.

-   Hardware factory reset
    
    -   Step 1: After the device is powered on and the ERR light is off, press and hold the RESET key;
    -   Step 2: When the ERR light is always on, release the RESET key;
    -   Step 3: After the ERR light goes out, press and hold the RESET key again, and release the RESET key when the ERR light flashes; wait for the ERR light to go out, indicating that the factory reset was successful.
-   Software factory reset
    
    Choose System Management > Configuration Management, click the reset button and select OK. IG902 will complete the factory reset operation by itself.
    
    ![](images/img_6e79f519.png)  
    

[Next](http://manual.ig.inhandnetworks.com/en/latest/IG902-User-Manual-EN.html "InGateway902 User Manual")  [Previous](http://manual.ig.inhandnetworks.com/en/latest/index.html "InGateway User Manual")