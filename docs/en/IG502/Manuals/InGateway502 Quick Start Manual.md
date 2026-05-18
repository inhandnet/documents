## 1. Access and connect IG502 to the Internet  

1.  Step 1: By default, the IP address of WAN on IG502 is 192.168.1.1; the IP address of LAN on IG502 is 192.168.2.1. This document uses the LAN port to access the IG502 as an example. Set the PC’s IP address to be on the same subnet with LAN.  
    

### [](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#access-the-ig502 "Permalink to this headline")

-   Step 1: By default, the IP address of WAN on IG502 is 192.168.1.1; the IP address of LAN on IG502 is 192.168.2.1. This document uses the LAN port to access the IG502 as an example. Set the PC’s IP address to be on the same subnet with LAN.
    
    -   Method 1: Enable the PC to obtain an IP address automatically (recommended)
        
        ![](images/img_0816f13c.png)
        
    -   Method 2: Set a fixed IP address
        
        Select Use the following IP address, enter an IP address (By default,any from 192.168.2.2 to 192.168.2.254), subnet mask (By default,255.255.255.0), default gateway (By default,192.168.2.1), and DNS server address, and click OK.
        
        ![](images/img_b8bd7b26.png)
        
-   Networking Method 1: Connect to the Internet by SIM card
    
    -   Step 2: Insert the SIM card. (Note: Before inserting or removing the SIM card, unplug the power cable; otherwise, the operation may cause data loss or damage the IG502.) After inserting the SIM card, connect the 4G LTE antenna to the ANT interface and power on the IG502.
        
        ![](images/img_fff06c91.png)  
        
    -   Step 3: Launch the browser on the PC and access the IP address of LAN. Enter the login user name and password. The default user name and password are adm and 123456 respectively.
        
        ![](images/img_9dfac9bb.png)
        
          
        
    -   Step 4: After successful login, you can see the web page as shown below:![](images/img_f37bbd1b.png)  
        
    -   Step 5: Choose Network > Network Interfaces > Cellular page of IG502 and select Enable Cellular and click Submit.  
        
        ![](images/img_5517cef2.png)
        
        When the network connection status is Connected and an IP address has been allocated, the IG502 has been connected to the Internet with the SIM card.
        
        ![](images/img_08b5f07a.png)
        
-   Networking Method 2: Connect to the Internet by Ethernet
    
    -   Step 2: Use the Ethernet cable to connect the WAN and LAN ports of the IG502 respectively, as shown below:
        
        ![](images/img_a61060b6.png)  
        
    -   Step 3: Launch the browser on the PC and access the IP address of LAN. Enter the login user name and password. The default user name and password are adm and 123456 respectively.![](images/img_a3b3a70d.png)  
        
    -   Step 4: After successful login, you can see the web page as shown below:![](images/img_c3e30d98.png)  
        
    -   Step 5: Choose Network > Network Interface > WAN page of IG502 to configure the IP address of the WAN port and click Submit. (When the network type is a static IP address, you need to configure the IP, subnet mask, and other information according to the site network conditions.)![](images/img_5a86045c.png)![](images/img_d43d5c69.png)  
        
    -   Step 6: Choose Network > Routing > Static Routing page of IG502 to add a static route for WAN port and click Submit. (Select “WAN” for the interface item, and configure the other items according to the site network conditions.)![](images/img_c5ddb89f.png)  
        
    -   Step 7: Choose System > Network Tools page of IG502 and use the Ping tool to check whether the IG502 has successfully connected to the Internet. The following figure shows that IG502 have successfully connected to the Internet:![](images/img_cdafc7cb.png)  
        

### [](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#connect-ig502-to-the-internet "Permalink to this headline")

-   To change the IP address of LAN, choose Network > Network Interfaces > LAN page of IG502 to configure LAN.![](images/img_5c99783b.png)  
    
-   To change the user name and password for logging in to the web management interface of IG502, choose System > User Management page of IG502 and set the new user name and password.![](images/img_e4ee2c8b.png)
    

## 2\. Update the Software[](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#update-the-software "Permalink to this headline")

To obtain the latest software version of IG502 and updated functions, please visit the [Resource](https://www.inhandnetworks.com/downlist/cid-148/). To update the IG502 software version, do as follows.

### 2.1 Update the IG502 firmware.[](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#update-the-ig502-firmware "Permalink to this headline")  

Choose System > Firmware Upgrade. Select a firmware file and click Start Upgrading. After the update is completed, you are prompted to restart the system to Apply the new firmware.

![](images/img_3fe99b5c.png)

### 2.2 Upgrade the Python SDK of IG502.[](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#upgrade-the-python-sdk-of-ig502 "Permalink to this headline")  

Choose Edge Computing > Python Edge Computing. Select Python Engine, select an Python SDK file, and click Upgrade; when the upgrade confirmation window pops up, click Confirm. Then the IG502 automatically performs the upgrade.

![](images/img_aeadade7.png)

## 3\. Python Edge Computing[](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#python-edge-computing "Permalink to this headline")

### 3.1 Install and run Python App[](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#install-and-run-python-app "Permalink to this headline")

To install and run Python App (App for short) in IG502, please refer to the following process, this document takes **Device Supervisor** as an example:

-   Step 1: Install the App
    
    Before installing the App, you need to ensure that the Python Edge Computing Engine is enabled and the Python SDK is installed, as shown in the following figure:
    
    ![](images/img_74354f2a.png)
    
    Choose Edge Computing > Python Edge Computing. click the Add button and select the App package file to be installed, then click Confirm.
    
    ![](images/img_dcc4709f.png)
    
    After importing, you can view the imported Apps, as shown in the following figure:
    
    ![](images/img_bb4e287e.png)
    
-   Step 2: Run the App
    
    Select enable App and click Submit.
    
    ![](images/img_435cde5d.png)
    
    Once enabled, the App automatically runs and will run every time the IG502 is started.
    
    ![](images/img_2b535130.png)
    

### 3.2 Update Configuration File for App[](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#update-configuration-file-for-app "Permalink to this headline")

If the installed App supports importing configuration files to modify the running mode, you can update the App running configuration by referring to the following process:

-   Step 1: Choose Edge Computing > Python Edge Computing, click the Import Configuration button and select the configuration file to be imported, then click Confirm.
    
    ![](images/img_9cc7c317.png)
    
-   Step 2: Restart the App after the import is successful. After the App restarts, it will runing according to the imported configuration file.
    
    ![](images/img_118847ab.png)
    

### 3.3 Update Python App version[](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#update-python-app-version "Permalink to this headline")

Generally, if you need to update the Python App version, you only need to import the new version of the App on the Edge Computing > Python Edge Computing page.

![](images/img_9faef70d.png)

After the update is completed, as shown below：

![](images/img_22a6da6f.png)

### 3.4 Enable the Debug Mode[](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#enable-the-debug-mode "Permalink to this headline")

To run and debug Python code on IG502, you need to enable IG502’s debug mode. Choose Edge Computing > Python Edge Computing, select Enable Debug Mode. After enabling, you can develop IG502 through VS Code. How to use VS Code for Python development of IG502, please refer to [Quick Start for MobiusPi Python Development](http://sdk.ig.inhandnetworks.com/en/latest/MobiusPi-Python-QuickStart-EN.html).

![](images/img_4cffd1b1.png)

After the debugging mode is enabled, IG502 will start an SSH server to listen on port 222 of LAN (default IP address being 192.168.2.1). The user name and password of the SSH server are displayed on the previous web page. A random password is generated every time the debugging mode is enabled or the IG502 is restarted to ensure security.

## 4\. InHand Cloud[](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#inhand-cloud "Permalink to this headline")

The InHand Cloud developed by InHand supports functions such as monitoring IG502 status, remote maintenance of equipment, remote batch delivery of IG502 configuration, and IG502 batch upgrade, helping users to conveniently and efficiently manage IG502 and field devices. In order to enable the InHand Cloud to remotely manage the IG502 and field devices, the IG502 needs to be connected to the cloud platform. The connection method is as follows:Choose System Management > InHand Cloud, tick Enable InHand Cloud and configure the corresponding server address and registered account, and click Submit after the configuration is complete. The **InHand Connect Service** platform mainly provides users with remote maintenance channels, and the **InHand Device Manager** platform mainly provides users with gateway management services (such as batch remote upgrades, etc.).

-   Server address: the address of the InHand Cloud.
-   Registered account: the InHand Cloud account associated with the IG502 device (if you have not registered an account, you need to register an account first)
-   Advanced settings: Contains configurations such as heartbeat interval. Generally, you can use the default configuration.

![](images/img_75921418.png)

After the IG502 is successfully connected to the InHand Device Manager, the status is described as Connection Accepted.

![](images/img_14a3249b.png)

## 5\. Data Collection And Upload To The Cloud[](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#data-collection-and-upload-to-the-cloud "Permalink to this headline")

-   Step 1: Connect PLC
    
    Use Ethernet or serial cable to connect IG502 and PLC, the following figure describes how to connect serial port terminals of IG502:
    
    ![](images/img_3417df96.png)
    
-   Step 2: Install and run Device Supervisor
    
    Please refer to 3.1 Install and Run Python App for how to install and run Device Supervisor.
    
-   Step 3: Add a PLC
    
    Choose **Edge Computing > Device Supervisor > Device List**, and click **Add**. On the device adding page, select the PLC protocol and configure the PLC communication parameters. The following figure is an example of adding S7-1200 PLC:
    
    ![](images/img_f68e9e59.png)
    
-   Step 4: Add variable
    
    On the **Device List** page, click **Add** variable, and configure the variable parameters in the pop-up box.
    
    ![](images/img_b5802c27.png)
    
-   Step 5: Configure a cloud service to report and receive data
    
    Choose Edge Computing > Device Supervisor > Cloud. Select Enable Cloud Service, configure the MQTT connection parameters and publish and subscribe messages (this document takes the configuration of publish messages as an example), and then click Submit. After the above configuration is correctly completed, the collected data can be monitored in the gateway and cloud platform.
    
    ![](images/img_caf1e8b0.png)
    
    ![](images/img_da578111.png)
    

## 6\. I/O Module[](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#i-o-module "Permalink to this headline")

IG502 supports the digital input, pulse counting, digital output, and pulse output functions. In addition, IG502 can remotely read I/O status data or report it to the cloud platform through Modbus TCP. I/O in each mode is defined as follows:

-   Digital input (Dry contacts and wet contacts are specified based on actual connections.)
    
    -   Dry contacts
        
        0: disconnected
        
        1: connected
        
        The following figure shows the connection modes.
        
        ![](images/img_ccb80461.png)
        
    -   Wet contacts
        
        0: 0 V DC to 3 V DC/-3 V DC to 0 V DC
        
        1: 10 V DC to 30 V DC/-30 V DC to -10 V DC (4 mA min)
        
        The following figure shows the connection modes.
        
        ![](images/img_031b4544.png)
        
-   Pulse counting
    
    A maximum of 3000 Hz pulse signal counting is supported, up to 4294967296. The following figure shows the connection modes.
    
    ![](images/img_d4457bb0.png)
    
-   Digital output
    
    0: Low level
    
    1: High level. According to the external power output voltage, if no external power supply is connected, no voltage is output. The maximum voltage output is 30 V, 500 mA.
    
    The following figure shows the connection modes.
    
    ![](images/img_d046abe3.png)
    
-   Pulse output
    
    A maximum of 5000 Hz pulse signal output is supported. The following figure shows the connection modes.
    
    ![](images/img_f5145b16.png)
    

The procedure for configuring I/O and obtaining I/O status data is as follows:

-   Step 1: Choose “Edge Computing > IO Module > Configuration”, and configure the I/O functions based on the site requirements. The following figures show a configuration example.
    
    -   Digital input
        
        ![](images/img_15f96398.png)
        
    -   Pulse counting
        
        The starting value is 0. After power down, the value counted by the power down is retained.
        
        ![](images/img_adf31287.png)
        
    -   Digital output
        
        ![](images/img_b904d25c.png)
        
    -   Pulse output
        
        According to the frequency of 5000 Hz, the duty cycle is 50% for the pulse output.
        
        ![](images/img_9f23a02e.png)
        
-   Step 2 (optional): Set the pulse counting and pulse output.
    
    After setting DI to the pulse counting, click Start to count the pulses received by the DI. Otherwise, do not count it. Click Reset to reset the count value to the starting value.
    
    ![](images/img_4e50ef2c.png)
    
    After setting DO to the pulse counting, click Start to output pulses based on the specified output frequency. Otherwise, do not output pulses.
    
    ![](images/img_54a8c434.png)
    
-   Step 3: Set Modbus TCP Slave.
    
    Turn on the **Enable** switch to enable the Modbus TCP Slave function. This function allows Modbus TCP Master to read the I/O status of IG502. After you turn on the **External Access** switch, Modbus TCP Master outside the gateway can read the I/O status of IG502, such as the SCADA software. Set other parameters based on the site requirements. The following figure shows a configuration example.
    
    ![](images/img_077971ab.png)
    
-   Step 4: Read the I/O status through Modbus TCP.
    
    Use Device Supervisor to read the I/O status of IG502 in Step 3 as an example. First, add a Modbus TCP controller and set the controller communication parameters based on Modbus TCP Slave.
    
    ![](images/img_f113e81e.png)
    
    Then, configure the data to be collected according to the Modbus mapping table. For example, read **DI0 Counter Value** as an example.
    
    ![](images/img_c5c3479c.png)
    
    ![](images/img_36046157.png)
    
    After the configuration is completed, you can obtain **DI0 Counter Value**.
    
    ![](images/img_b4e9a303.png)
    

## Appendix[](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#appendix "Permalink to this headline")

### Factory reset[](http://manual.ig.inhandnetworks.com/en/latest/IG502-Quick-Start-Manual.html#factory-reset "Permalink to this headline")

There are two ways to restore the IG502 to factory settings: hardware factory reset and software factory reset.

-   Hardware factory reset
    
    -   Step 1: After the device is powered on and the ERR light is off, press and hold the RESET key;
    -   Step 2: When the ERR light is always on, release the RESET key;
    -   Step 3: After the ERR light goes out, press and hold the RESET key again, and release the RESET key when the ERR light flashes; wait for the ERR light to go out, indicating that the factory reset was successful.
-   Software factory reset
    
    Choose System Management > Configuration Management, click the reset button and select OK. IG502 will complete the factory reset operation by itself.
    
    ![](images/img_eb89eb15.png)