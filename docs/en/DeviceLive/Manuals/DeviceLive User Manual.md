# **About the Platform**  

DeviceLive platform is designed for the industrial IoT field to quickly build intelligent edge networks paired with InHand edge intelligent hardware. It has four major capabilities: device management, remote monitoring, edge computing app management, and remote access to on-site machines. Collaborating with edge hardware, DeviceLive helps you deploy and upgrade edge APPs, implement edge data collection and pre-processing, and enable status visual monitoring.  

# 1.Quick Guide  

**Definition of Terms**  

1.  Company/Enterprise: When you successfully register with your email in the system, it creates an company/enterprise for you. Data between different company/enterprises is completely separate.

1.  Organization: After successfully registering your company/enterprise, it defaults to being a top-level organization. Depending on your business needs, you can create other organizations within this top-level organization. The top-level organization has the highest data permissions and can access all data within the current organization. Lower-level organization can only see data from their own organization and any subgroups, without access to data from higher-level organization.

1.  Internal Users: Users belonging to the current company/enterprise.

1.  External Users: Individuals outside the current company/enterprise cannot access its data by default. However, based on specific business needs, such as providing technical support, these individuals can be invited to access the company/enterprise data.

### 1.1 Organization Management  

In the InHand Cloud Service, the "User" page allows control over your organization's structure and users. This service supports multiple levels of organization. When managing business by regions or locations, you can create several subgroups for independent management. At the same level, organizations' data is separate; however, higher-level organizations can view data from lower-level ones.![](images/img_e35f489c.png)

1.1 Add Organization  

Click "Add ", enter the organization name, choose the parent organization, and then click "OK" to create an organization. Each institution can create up to five levels of organizations.![](images/img_fe4cb329.png)

  

| Field Name | Description |
| --- | --- |
| Organization Name | Custom organization names. |
| Parent Organization | The current organization's parent within the hierarchy. Higher-level organizations have access to all data within their suborganizations. |
| Contact Phone | Organization's contact phone number. |
| Contact Email | Organization's contact email. |
| Notes | Organization's description. |

  

1.2 Add User  

In the user list, click "Add" and input user details. After successful addition, users can log in to the platform using their account and password. Page permissions for users are determined by their assigned roles. Users can only access data authorized for their current organization. For instance, if a user is in Suborganization A at the tertiary level, they can solely view data within Suborganization A and its lower-level suborganizations, without access to data from primary, secondary organizations, or other tertiary organizations.  

![](images/img_6073f5b5.png)  

| Field Name | Description |
| --- | --- |
| User Name | User's name. |
| Login Email | User's email information, used for platform login and receiving platform notifications. |
| Organization | For the organization associated with the current account. Users can view resources such as devices within their current organization and its subordinate organizations. |
| Application | All applications provided by InHand Cloud Service, including InCloud Manager, DeviceLive, and others. |
| User Role | According to your selected application, corresponding roles will be displayed. InCloud Manager comprises four roles—refer to the roles section. |
| Login Password | The password used for logging in. To ensure your account's security, please set a login password according to system requirements. Safeguard your account credentials and periodically update your password for security reasons. |

  

1.3 Organization Data Management  

Administrators from higher-level organizations can allocate authorized resources to lower-level organizations, including devices, groups, networks, users, and more.

1.3.1 Device Transfer  

You can transfer devices within the organization to a lower-level organization or a specific group by following these steps:  

1.  Go to the "Devices" page in DeviceLive.  
    
2.  Select the device(s) you want to transfer.  
    
3.  Click "Move," select the target organization, and then click "Save."  
    

![](images/img_96d3828b.png)

  

1.3.2 Network Transfer（Connector）  

You can transfer networks within the organization to a lower-level organization by following these steps:  

1.  Go to the "Connector" page in DeviceLive.  
    
2.  Click on the "Edit" button for the network you want to transfer.  
    
3.  Choose the target organization and click "Save."  
    

![](images/img_02a67857.png)

  

1.3.3 Group Transfer  

You can transfer groups within the organization to a lower-level organization by following these steps:  

1.  Go to the "Groups" page in InCloud Manager.  
    
2.  Click on the "Edit" button for the group you want to transfer.  
    
3.  Choose the target organization and click "Save."  
    

![](images/img_c4f3c9fe.png)

  

1.3.4 User Transfer  

You can transfer users within the organization to a lower-level organization by following these steps:  

1.  Go to the "User" page in InHand Cloud Service.  
    
2.  Click on the "Edit" button for the user you want to transfer.  
    
3.  Choose the target organization and click "Save."

![](images/img_307330b8.png)

### 1.2 Cross-Organization Access  

When your management requirements are met:  

1.  Administrators can view all devices and resources.
2.  Devices across different projects require separate management.
3.  A single engineer maintains multiple projects, and there is overlap in the projects maintained by engineers.  
    

As shown below: The General Manager needs to view data from all departments, while each department manager needs to view data specific to their own unit. Engineer 01 manages Project 1 and Project 2, while Engineer 02 manages Project 3 and also needs to manage Project 2.  

![](images/img_fbb0ca78.png)  

On the InHand Cloud Service, you can add Engineer 01 to the organizations of Project 1 and Project 2, and add Engineer 02 to the organizations of Project 3 and Project 2. This fulfills the requirement for one engineer to manage multiple projects. Follow these steps:  

1\. Enter Project 1 and add Engineer 01 as an internal user.

![](images/img_3b560260.png)  

2.Enter Project 2 and add Engineer 01 as an external user.  

![](images/img_428e6f30.png)  

3.Similarly, add Engineer 02 to Project 2 and Project 3.  

4.After logging in, Engineer 01 can use the “Switch Organization” feature to switch between different projects for device management.DeviceLive

![](images/img_e3c01625.png)

![](images/img_82881ef9.png)  

### 1.3 Cross-company Access

When a company requires your technical support, besides creating another account for you or providing their account (internal user), the company's administrator can invite you to join their organization using the "external user" method if you have a registered email account in DeviceLive. This approach ensures the security of the customer's account while facilitating your support provision.

![](images/img_d1dbc319.png)  

Invite External User Procedure (Using the example of Organization A inviting User A from Organization C to provide support in DeviceLive）:  

1.  Administrators from Organizations A navigate to the "Users" page in InHand Cloud Service.  
    
2.  In the user list, click "Add."  
    
3.  Choose the user type as "External User."  
    
4.  Enter the email login of User A in InCloud Manager.  
    
5.  Select the relevant organization where User A will provide support, for instance: Suborganization A in level three.  
    
6.  Choose the application as "DeviceLive"  
    
7.  Select the user role and save.

![](images/img_6de8bdf2.png)  

User A will receive an invitation email. After accepting the invitation, User A can switch to Organization A to provide technical support, following these steps:  

1.  Log in to DeviceLive.  
    
2.  Click on the profile icon at the top right corner of the page, then click "Switch."  
    
3.  In the organization switch popup, select Organization A, and click "Switch" to successfully switch to Organization A for providing technical support.  
    ![](images/img_19407667.png)

# **2\. Login to** DeviceLive 

## **2.1 Registration**

Type [https://device.inhandcloud.com/](https://device.inhandcloud.com/) in the web browser to go to the DeviceLive registration and login page. (Google Chrome is recommended.)  

![](images/img_13715512.png)  

## **2.2 Login**

After registration and verification, click Access under "DeviceLive" in the Console to enter DeviceLive.You can also enter [https://device.inhandcloud.com/](https://device.inhandcloud.com/) login directly to DeviceLive.

After login, go to the Security settings page to bind a mobile number. This allows you to log in to DeviceLive by typing the mobile number.

![](images/img_c519a580.png)  

![](images/img_6470b6d5.png)  

  

# **3.****Organizations & Accounts**

Click "**Users**" to enter InHand Cloud Service, and you can manage your accounts in the system.

Describe account management, user operate permissions controlled by role, user data permissions controlled by organization, and external accounts in the system. 

![](images/img_9609dd46.png)  

  

![](images/img_9abe5c46.png)  

## **3.1 Accounts**

Click **Users** at the top of DeviceLive to manage the organization and user information of the system.

### **3.1.1 Add Users**

**1.Add Users**  

![](images/img_0aa429e7.png)  

In the user list, click "**Add**," and enter the user information as follows:

| Field Name | Description |
| --- | --- |
| **User Name** | The name of the current user. |
| **Login Email** | The user's email information is used for logging into the platform and receiving messages from the platform. |
| **Organization** | Belongs to the organization associated with the current account. Users can view resources such as devices within the current organization and its subordinate organizations. |
| **Applications** | All applications provided by InHand Networks Cloud Services, including DeviceLive, InCloud Manger, and more. |
| **User Roles** | The roles available in DeviceLive may vary depending on the selected application. |
| **Login Password** | The password is used for logging in. For the security of your account, please set a login password according to the system requirements. Please keep your account password secure and change it regularly. |

**2.Invite**

Click on "**Invite**", enter organization and role information, copy the link to the user. The user can register an account using that link, and after registration, the user's account will be automatically added to the list.  

![](images/img_8961cc4f.png)  

### **3.1.2 User Roles**

The system provides four roles: system administrator, organization manager, device full access, and device read only . The functional permissions of each role are as follows:

| Role | Functionality Permission |
| --- | --- |
| system administrator | Have all the functions and data permissions of current registered account. |
| organization manager | 1.  Users of this role have all functionality permissions in DeviceLive, but only have functional permissions for Console，Users and My Profile pages in InHand Cloud Service. 2.  Users of this role can view resources from the current organization and sub-organizations, and have the permission to operate these resources. |
| device full access | 1.  Users of this role have all functionality permissions of these pages: Overview, Devices, Connector, Groups, OTA Upgrade, Alerts, Reports, Messages, Console, My Profile. 2.  Users of this role can view resources from the current organization and sub-organizations, and have the permission to operate these resources. |
| device read only | 1.  Users of this role have the "view" functionality permissions of these pages: Overview, Devices, Connector, Groups, Alerts, Reports, Messages, Console, My Profile. 2.  Users can create and download reports for authorized resources. 3.  Users of this role can view resources from the current organization and sub-organizations, but don't have the permission to operate these resources. |

### **3.1.3 Assign Roles**

Admin can assign roles to other users.Each user can only have one role in an application.A new role assignment will overwrite the current role.

If you assign a user the role of system administrator, the user has the highest permission in all applications of the InHand Cloud Service.

![](images/img_b51285e3.png)  

### **3.1.4 Delete Users**

Select the target user and click **Delete**. Confirm the delete operation to delete the user.

### **3.1.5 Lock Users**

Admin accounts can lock other accounts to prevent accounts from logging into the platform.

On the Accounts page, click the "**Lock**" button in the "Operation" column to lock the account. If you need to unlock the account, click "Unlock" and the account can resume login.

## **3.2 My Profile**

After logging into DeviceLive, click on the application switch icon in the top left corner to access the InHand Cloud Service. From there, you can navigate to the "**My Profile**" page to change your account login password, link your mobile phone number, and set up two-factor authentication. Alternatively, you can click on the account icon in the top right corner, then scroll down and select "**Security Settings**".  

![](images/img_91e8a4d0.png)  

### **3.2.1 Change Login Password**

Passwords with high security can make your account more secure. We recommend that you change your password regularly.

Click **Change**, enter the current password of your account to verify your identity. Enter the new password and **confirm** it.

### **3.2.2 Mobile Phone Binding**

After binding the mobile phone number, you can use the mobile phone number and SMS verification code to log on to DeviceLive. Or you can use this phone number to receive alert messages when configuring alerts.

### **3.2.3 Two-factor Authentication**

To enhance account security, you can set up two-factor authentication (2FA) using multiple methods. This allows you to have a backup authentication method in case you lose your device or cannot access the app for verification.

**1.SMS Verification**

1. Click on "**Settings**" and follow the prompts to bind your mobile phone number. After successfully binding your phone number, you will receive a verification code on your bound phone number during subsequent logins for two-factor authentication.

2. If you no longer wish to use SMS verification, you can click on "**Disable**" to turn off SMS verification.

**2.APP Verification**

1. Click on "**Settings**" and follow the prompts to download and install the Google Authenticator or Microsoft Authenticator app on your mobile phone.

2. Open the app and **scan the QR code** on the screen to set up your account.

3. After scanning the code, enter the **6-digit code** displayed in the app to verify your identity. Once verified, the app authentication is successfully bound to your account. You will need to enter the 6-digit code from the app for two-factor authentication during login.

4. If you no longer wish to use app authentication, you can click on "**Disable**" to turn off app authentication.

**3.Recovery Code Verification**

When setting up two-factor authentication for the first time, you will also receive a backup code. This backup code can be used in case you are unable to receive SMS codes or use the authenticator app. You can use this backup code to bypass two-factor authentication during login by selecting "Use Backup Code.

### **3.2.4 Preferences**

Set the default number of items displayed per page in the current account list.  

  

## **3.3 System Settings**

Administrators can go to the System Settings page to set login **timeouts** and **Force MFA** for the entire organization.  

![](images/img_d8c86ebe.png)  

**1.Idle Timeout**

After setting, if the idle timeout of the account in the whole organization exceeds the setting time, you will need to log in again to access it.

**2.Force MFA**

After opening，this will require Two Factor Authentication for all users in the account.  

  

## **3.4 Organizations**

DeviceLive supports multi-level organizations. Users, devices, and other resources belong to a specific organization; users of one organization can view the devices and other data of this organization and its subordinate organizations. You can use this function to realize the data access control of different users. The isolated management of multiple sub-customers can make the data management more organized and the privacy security of the account more secure.

### **3.4.1 Add organizations**

On the "**Users**" page, click "**Create**" to add a new organization, you need to select the parent organization of the organization. By default, the organization where the account is registered is the root organization.

### **3.4.2 Devices with Organizations** 

On the Devices page, adding and importing devices will assign the devices to the operator's organization by default. You can modify the device's organization.

1\. Select the device, click "**Move**", then select the organization or the group you want to move in

2\. After selection, save the changes. Then the device is moved to the new organization, and only users within the same organization can view the device on the "Devices" page.

### **3.4.3 Groups with Organizations** 

On the **Groups** page, click add and then select the organization the group is in. Only users within the same organization can view these groups on the Groups page, and the devices within these groups can also be seen by these users on the Devices page.

### **3.4.4 Networks with Organizations** 

On the Networks page, click **add** and then select the organization the network is in. Only users within the same organization can view these networks on the "Networks" page. They can operate the devices, endpoints, and accounts in the network. When a user has the permission of a network but does not have permission for the devices that are within the network, the user can only operate the devices from the network dimension and cannot view the device on the "Devices" page or operate the devices through DeviceLive.

### **3.4.5 Users with Organizations**

On the Users page, click add and then select the organization the group is in. The data resources an account can view (including devices, groups, networks, and users) are the data within the same organization that the user is in and its subordinate organizations. Particularly, users within the root organization can view all the data in the current registered account, which includes all devices, groups, networks, and users.  

  

## **3.5 Company Profile**  

Click "**Company Profile**" in InCloud Manager's top menu to handle the current organization's information in InHand Cloud Service.  

![](images/img_24d05af6.png)  

  

Company information management includes the following details：  

-   **Basic Information**: such as company name, region, and system administrator.
-   **Contacts**: the enterprise's contact information.
-   **Billing Information**: including billing dates and invoice mailing details.
-   **Shipping Information**: the details of the recipient and address for the current enterprise.
-   **Associate an MSP Account**: By inputting the MSP's email account in InCloud Manager. Once linked, MSP can transfer devices and licenses to your account.

## **3.6 External Users**  

If an external user with a registered email account in DeviceLive needs to join your organization to provide external support, you can invite them by adding them as an "**External User**" to your current organization.

1. Go to the "**Users**" page and click on "**Add**" above the user list.

2. Select the user type as "**External User**".

3. Set the external user's login email, organization, application, and role information, then click "**Save**".

4. The external user will receive an email invitation. After accepting the invitation, the user will be able to switch to your organization to provide technical support.  

![](images/img_b3498aba.png)  

  

┃**Note**：To ensure data security, it is important to carefully configure user roles and organizational relationships when creating external users. This helps control the access and operational permissions of external users within your organization.

External users switching organizations should follow these steps:

1.  External users must first **accept the email invitation** and then log in to DeviceLive.
2.  Click on the personal information at the top right corner of the page, then click "**Switch**".
3.  In the organization switch dialog box, select the organization requiring assistance, and click "**Switch**" to successfully transition and provide technical support for the corresponding organization.  
    

  
![](images/img_baed9381.png)  

  

  

┃**Note**：①The permissions after switching to another organization are determined by the roles assigned by the invite initiator when adding external users.②If you need to switch back to your own institution, use the same entry point as above.  

# **4.**Internet Connection  

After connecting to DeviceLive, devices will automatically synchronize their configurations, enabling cloud-based management. Here are the steps for devices to connect to the platform:

(1) Local Device Configuration for Cloud Management.

(2) Adding Devices to the Platform.  

## 4.1 **Configuring an Internet Connection**  

To enable cloud-based management, it is essential to ensure that the device is connected to the internet. Configuration methods may vary across different product series; please refer to the configuration steps for the specific product series you are using. Additionally, please note that interface variations may exist due to different firmware versions. For illustrative purposes, we will use the EC942 product series as an example.  

**Method 1: Ethernet connection**

Environment: Connect the PC to ETH1 (default 192.168.3.100) interface of EC942 using an Ethernet cable, and connect ETH2 (default 192.168.4.100) interface to the Internet.

configure an IP address for the PC in the 192.168.3.X network segment (such as 192.168.3.110), with a subnet mask of 255.255.255.0. Then, enter [https://192.168.3.100:9100](https://192.168.3.100:9100/) in the Google Chrome browser to access the page as follows:  

![](images/img_dc95bfc0.png)  

Go to "**Network >> Interfaces**" page and configure DHCP or a static IP for ETH2.  

![](images/img_9fc85f0e.png)  

  

After configuration, go to "Network>> Static Routes" and add the corresponding static route to establish connectivity.

![](images/img_966a111b.png)  

  

**Method 2: Cellular Connectivity**

In most cases, simply inserting a SIM card will establish a network connection. If you have custom requirements, you can configure APN parameters in the "**Network** **\>> Cellular**" popup to enable connectivity.  

![](images/img_15bf138e.png)  

**Method 3: Wi-Fi (STA) Connectivity**

Under "**Network >> WiFi**" menu, click on "Enable Wi-Fi" and configure the relevant parameters to connect to the on-site SSID for internet connectivity.

## **4.2 Adding Devices to the Platform**

Once the device is connected to the network, you can add it to the platform. After successful addition, the device will automatically synchronize with the platform, allowing for cloud-based management of the device. Here are the steps for adding a device:

(1) In the "**Devices**" menu, click on "**Add**."

(2) In the window, enter the **device name** and **serial number**, then click "**Save**."

(3) Once added, the device will appear in the list of devices.  

# **5\. Overview**  

DeviceLive offers an overview feature that allows you to easily monitor real-time information such as device status, data usage, uplink, and device distribution under your account.

![](images/img_2655f8f0.png)  

## **5****.1 Summary**

The **overview** page displays essential information including the number of devices, their online status, and upgrade status under the current account.

| Function Modules | Description |
| --- | --- |
| **The number of devices** | 1.  **Total Devices**: Displays the total number of devices on the platform and the number of devices added in the last 7 days.  1.  **Online/Offline**: Shows the number of devices that are currently online and offline on the platform.  1.  **Inactive**: Displays the number of devices that have been added to the platform but have never been online. It also supports viewing historical records of devices that were never activated. |
| **Recent Alerts** | To view the latest alert information for all devices/networks under the platform, click '**View** **More**' to navigate to the alert details. |
| **Configuration Status** | Device Configuration Synchronization Status Ratio Information, including the following configuration states:  1.  **No Status**: Indicates that the device has never online or it’s status is unknown.        2.  **Suspended**: Represents the status when the configuration synchronization between the platform and the device is paused due to a mismatch in device and group versions. It automatically resumes synchronization when the device and group versions are consistent.        3.  **Pending**: Indicates that the device and the platform are currently synchronizing configurations.        4.  **Synced**: Denotes that the device and platform configurations have successfully synchronized.        5.  **Sync** **Failed**: Indicates that the configuration synchronization between the device and the platform has failed. |
| **Firmware Status** | Firmware Upgrade Status Ratio Information for Devices, including the following firmware upgrade states:  1.  **Scheduled**: Refers to upgrade tasks that are planned but have not yet started.        2.  **Pending**: Indicates that the upgrade is pending execution.        3.  **Upgrading**: Means the upgrade is currently in progress.        4.  **Completed**: Indicates that the upgrade task has been successfully completed.        5.  **Cancelled**: Denotes that the upgrade task has been canceled.        6.  **Failed**: Represents a failed upgrade task.        7.  **No Status**: Refers to devices that have never come online or have an unknown status. |
| **Networking Method** | Device networking method include:  1.  **Unknown**: Refers to the connectivity method when the device has never come online.        2.  **Wired**: Represents connectivity through Ethernet.        3.  **Cellular**: Denotes connectivity through cellular networks.        4.  **Wireless**: Indicates connectivity via Wi-Fi (STA).        5.  **Multiple**: Refers to the simultaneous presence of two or more connectivity methods. |
| **Device Distribution** | Distribution of device models across the account. |
| **Offline Times TOP 10** | View detailed connection information for the top 10 devices with the highest number of offline occurrences on the platform. |
| **Alerts TOP 10** | 1.  **Alerts TOP 10 by Device**: Refers to the top 10 devices ranked by the number of alerts.        2.  **Alerts TOP 10 by Type**: Indicates the top 10 alert types ranked by occurrence. |

## **5.2 Data Usage**

The **Data Usage** page allows you to view the total data usage of all devices under the account and supports viewing by network connectivity type. Basic information includes:  

![](images/img_50b37c2b.png)  

  

| Function Modules | Description |
| --- | --- |
| **Summary** | Total data usage, cellular data usage, wired data usage, and wireless data usage information for all devices. |
| **Usage Trend** | Data usage trends over time for all devices. |
| **Usage TOP 10** | The top 10 devices ranked by data usage and their corresponding data usage information. |

  

## **5.3 Uplink**

Uplink for all devices, with specific details as follows:

![](images/img_9f551cd7.png)  

  

| Field Name | Description |
| --- | --- |
| **Status** | The device's uplink status include:  1.  Connected        2.  Disabled        3.  Disconnected         ┃Note: Due to the device reporting the latest link information every 30 minutes, there may be a delay in this status. |
| **Uplink** | Types of uplink include:  1.  WAN        2.  Cellular        3.  Wi-Fi（STA） |
| **Working Mode** | 1.  **Active**：Active indicates that the current link is the primary link.        2.  **Backup** |
| **Uptime** | The connection duration of the current link. |
| **Public IP** | Public IP information for the current link. |
| **Interface IP/Mask** | Interface IP/Mask information for the current link. |
| **Throughput** | Throughput information for the current link. |
| **Latency** | Latency for the current link. |
| **Jitter** | ┃**Note:** This metric is not available for cellular and Wi-Fi links. |
| **Loss** | ┃**Note:** This metric is not available for cellular and Wi-Fi links. |

  

## **5.4 Map**

You can view the actual locations of all devices and their distribution on the **Map** page.  

![](images/img_03e854c4.png)  

  

# **6.Devices**

The device page allows you to view the basic information of all devices and supports operations such as remote configuration, firmware upgrades, remote access, commands, add, delete, move, import, export, and filter.  

![](images/img_b22e6c87.png)  

## **6****.1 Device Management**

### **6.1.1 Devices List**

The information displayed in the device list is as follows:

| Field Name | Description |
| --- | --- |
| **Status** | The device online/offline status, where green represents online and gray represents offline. |
| **Device Name** | The name that you set for the device when adding the device. |
| **Serial Number** | Indicates the unique ID of a device. |
| **Organization** | The name of the organization where the device is currently located. |
| **Product** | Indicates the device model. |
| **Firmware Version** | Indicates the current firmware version of a device. |
| **Cellular Module Version** | The current cellular module version of a device. |
| **Cellular Signal** | The signal strength of a cellular card. |
| **Group** | The group to which a device belongs. |
| **IP Address** | The public address that a device uses to connect to the Internet. |
| **MAC Address** | The physical MAC address of a device. |
| **ICCID** | The unique ID of a SIM card. |
| **Config Status** | 1.  **Unknown**: Indicates that the platform has never retrieved the device's configuration synchronization status, represented by "-".        2.  **Synced**: Means that the platform and the device have completed the configuration synchronization.        3.  **Pending**: Implies that the platform has modified the device's configuration, but the device has not yet synchronized the platform's configuration.        4.  **Sync Failed**: Suggests that there is a conflict between the platform and device configurations. In this case, an "Error Details" will appear after synchronization failure. Clicking on it will open a window displaying error details, allowing users to resolve conflicts based on the error information.        5.  **Suspended**: When the device's firmware version does not match the firmware version of its group, the platform's configuration changes will not synchronize with the device. This status will persist until the device and group versions are aligned. |
| **Firmware Status** | Firmware upgrade status for devices include:  1.  **Completed**: Indicates that an upgrade task exists and that upgrade is successful.        2.  **Failed**: Indicates that an upgrade task exists and that upgrade fails.        3.  **Pending**: Indicates that an upgrade task exists and that upgrade will be performed.        4.  **Upgrading**: Indicates that an upgrade is being performed.        5.  **Cancelled**: Indicates that an upgrade task exists but is canceled. |
| **N****etworking Method** | Networking method for devices include:  1.  WAN1        2.  WAN2        3.  SIM1        4.  SIM2        5.  Wi-Fi(STA) |
| **Location** | Displays the geographic location of a device. |
| **Description** | Description information when adding a device. |
| **Actions** | 1.  **Delete**: Click the "**Delete**" button, and after a secondary confirmation, the target device will be removed from the platform.        2.  **Config Details**: Click "**Config Details**" to view the configuration details of the target device. |

### **6.1.2 Add Device**

Click '**Add**' on the **'Devices'** menu page. In the '**Add Device**' popup, enter the **device name**, **serial number**, and **MAC address**, then click '**Confirm**'.

### **6.1.3 Import Devices**

Click **'Import'** on the **'Devices'** menu page to bulk add devices to the cloud platform.

1. Click **'Import'** at the top right of the device list.

2. **Download** the import template and fill in device information according to the template.

3. Click '**Upload File**'，select the file, and then click **'Import**'.

┃**Note:** When there are errors in the imported file, the page will provide notifications of successful and failed imports, along with the row numbers where the failures occurred.

### **6.1.4 Export Devices**

Click the **'Export'** button to export the existing device asset information from the platform in table format.

### **6.1.5 Move Devices**

Click **'Move'** on the 'Devices' menu page to move devices to a specific organization or a subgroup within an organization.

1. Select the devices you want to move in the device list.

2. Click **'Move'** at the top right of the device list.

3. Choose the **target organization** or **group** and click **'Save'**.

┃**Note:** Only devices from the same product can be added to a group. When the device's firmware version does not match that of the group, the configuration changes made on the platform will not synchronize with the device.

## **6.2 Device Details**  

Clicking on the "**Device Name**" directly navigates to the device's details page, where you can view the current device overview, projects, DeviceSupervisor, cellular signal, and basic information.  

### **6.2.1 Overview**  

This menu displays basic usage information about the device, including performance status and connection history. The basic information is as follows:  

![](images/img_8a440c87.png)  

  

| Function | Description |
| --- | --- |
| Performances | The device's usage status of CPU, memory, disk, and so on. |
| Connection History | Recording the historical connection instances between the device and the platform. |

### 6.2.2 Project  

You can view and manage current project information for the device, including Container APP , Native APP, and Personalized Environmental Variables.  

![](images/img_357ed532.png)  

### 6.2.3 DeviceSupervisor  

You can view and manage current DeviceSupervisor information for the device.

![](images/img_7ed1f000.png)  

### 6.2.4 **Cellular Signal**  

Display detailed data information for various cellular signal parameters to comprehensively analyze the current and historical network conditions of the cellular network. The displayed information includes signal level, RSSI, RSCP, EC/IO, RSRP, RSRQ, SINR, SS-RSRP, SS-RSRQ, and SS-SINR.

![](images/img_c3063f04.png)  

┃**Note:** The device reports cellular signal data every 30 minutes, which means there may be a maximum delay of 30 minutes in the data.

### 6.2.5 Details  

Click the **Details** tab to view the device's basic information, license information, upgrade package information, physical location and etc.  

![](images/img_c7997e59.png)  

  

## **6.3 Remote Access**

Users can select the target device in the **'Devices'** menu, click **'Remote Access',** and achieve remote access to the device's local interface.  

![](images/img_58dce7f7.png)  

┃**Note:**  

      ① Remote access functionality cannot be used when the device is offline.  

      ② Remote access consumes data traffic, so please avoid using it for extended periods if it is not necessary.

## **6.4 Commands**  

![](images/img_31d24248.png)  

### **6.4.1 Reboot**

Users can select the target device in the **'Devices'** menu, click **'Reboot'**, and after a secondary confirmation, the device will execute the restart operation.

┃**Note**: The device cannot be rebooted remotely when it is offline.

### **6.4.2 Restore to Factory**

Users can select the target device in the **'Devices'** menu, click 'Restore to Factory', and after a secondary confirmation, the device will execute the factory reset operation.

┃**Note:**  

      ① The factory reset operation cannot be executed when the device is offline.  

      ② After a factory reset, historical data will be cleared, but upon the device coming online again on the platform, personalized configurations and group configurations will be reapplied.  

## **6.5 Firmware Configuration**  

In the device details, you can perform remote configuration operations on individual devices, including editing configuration, viewing configuration, clearing configuration,copying configuration, and more.

### **6.5.1 Edit Configuration**

The device details supports editing device configurations. After editing and submitting the configuration, the new configuration will be pushed to the device. The configuration edited here is the device's personalized configuration.

1. Click on the device name to access the **device details**.

2. Click **'Configuration'**  and choose the **'Edit'** operation.

3. Change the configuration in the editing configuration popup, and after making changes, click **'Commit Charges'**.

![](images/img_069243a0.png)  

In the editing configuration popup, the following operations are supported:

1.  **Pending**: Click the **'Pending Configuration'** button, and the configuration modified during this session will be saved in the platform backend but not yet pushed to the device.
2.  **Discard Changes**: Click **'Discard Changes'**, and the operations made during this session will be cleared.
3.  **Commit Changes**: Click **'Commit Changes'**, and the configuration changes made during this session will be applied to the device.  
    

┃**Note:**  

      ① Devices must be online on the platform, and the current firmware version must support remote configuration.  

      ② When the device's configuration synchronization status is 'Suspended', the platform's configuration will not be pushed to the device.  

### **6.5.2 Config Details**

The device details allows you to view the configuration information of the target device, including: Running Configuration, Individual Configuration, Group Configuration, Target Configuration, and Pending Configuration.

1. Click on the device name to access the **device details**.

2. Click **'Remote Configuration'** at the top of the device list and choose **'Configuration Details'.**

3. In the configuration details popup, you can view all the configuration information for the current device. Configuration information includes:

1.  **Running**: The current configuration that the device is running, including any configuration changes made by the user on the device locally or in the cloud.  
    
2.  **Individual**: Configuration information made on the individual device's editing interface or local interface. Personalized configurations take precedence over group configurations.  
    
3.  **Group**: Displays the configuration information of the device's parent group.  
    
4.  **Target**: The combination of personalized and group configurations that users expect the device to execute after making configuration changes. Target configurations can be customized to show/hide group configurations.  
    
5.  **Pending**: Configurations modified by the user on the platform but not yet synchronized with the device.  
    

![](images/img_f23750f8.png)  

### **6.5.3 Clear Configuration**

Click the **'Clear'** button, and after a secondary confirmation, the clear operation will be executed.

┃**Note:** The copy-to-devices operation copies the target configurations of a device to the individual configurations of the selected device.

### **6.5.4 Copy to Devices**

The **'Copy to Device'** operation allows you to copy the target configuration from the source device to the target device, and the copied configuration will be treated as the personalized configuration for the target device.

1. Click on the device name to access the **device details.**

2. Click **'Configuration'** at the top of the device list and choose **'Copy to Device'.**

3. In the popup, select the target device(s), you can select multiple, and then click **'Save'**.

### **6.5.5 Copy to Groups**

The **'Copy to Groups'** operation allows you to copy the target configuration from the source device to a group, and the copied configuration will become the group configuration for the selected group(s).

1. Click on the device name to access the **device details.**

2. Click **'Configuration'** at the top of the device list and choose **'Copy to Groups'**.

3. In the popup, select the target device group(s), you can select multiple, and then click **'Save'**.

  

## **6.6 Firmware Upgrade**

The device details supports individual device firmware upgrades or batch upgrades for devices of the same model.

1. Click on the device name to access the **device details.**

2. Click **'Firmware'** at the top of the device details.

3. In the firmware upgrade popup, select the **target firmware version**. If the selected device models are not consistent, you will need to select the product model for the upgrade first.

4. Choose the current firmware version that you want to upgrade.

5. Select the **upgrade time** and click **'Save'**:

1.  **Upgrade Now**: Online devices will immediately start the upgrade process, while offline devices will perform the upgrade upon their next online status.  
    
2.  **Later Date**: Devices will perform the upgrade at the specified time. If a device is still offline at the specified time, it will execute the upgrade upon its next online status.  
    

![](images/img_8d24bf8c.png)  

  

## 6.7 Pin Project Version  

The EC series products allow pinning a project version in the device details. Once a device's project version is pinned, it won't be affected by project version updates within its grouping. Upon unpinning, the device will synchronize with the group project version.  

![](images/img_3b841c7c.png)  

┃**Note:** Devices not included in any group cannot be pinned to a project version.

# **7.Connector**  

A Connector network has three types of resources: devices, endpoints, and accounts. The respective functions are as follows:

| resource | Description |
| --- | --- |
| **devices** | Networking devices such as routers and gateways. |
| **endpoints** | The business terminal connected to the router or gateway, such as PLC and IP telephone. |
| **accounts** | The account used by the engineer or administrator to establish VPN tunnels. |

**【Procedure】**  

![](images/img_eb0860c7.png)  

## **7.1 Configure Internet**

To access the **'Connector'** page, click on **'Add'**, enter network information such as the network name, and click **'Save'** to create a new cloud connection network.

## **7.2 Configure Device**

To add devices to the connector network, follow these steps:

1. Click on the **'Add'** action in the upper right corner of the device list.

2. In the **'Add Devices'** popup, select the devices you want to add to the current connector network.

3. Configure the device's subnet address to establish a VPN communication tunnel. There are two ways to assign subnet addresses:

1.  **Auto**: The system automatically assigns addresses to devices.  
    
2.  **Manual**: In cases where specific subnet addresses are required, you can define the subnet addresses yourself. The allowable range for subnet addresses is: 10.16.32.0/24-10.31.255.0/24.  
    

After devices are added, the system automatically assigns a virtual IP to each device and establishes a VPN connection tunnel. When the VPN channel for device cloud connectivity is online, users can use this virtual IP to remotely access the local web management interface of the router device.

![](images/img_9c2d40d4.png)  

┃**Note:** A maximum of 4,000 devices and accounts can be added to a connector network.

## **7.3 Configure Endpoint**

To add endpoint resources to the connector network, follow these steps:

1. Click on the **'Add'** action in the upper right corner of the endpoint list.

2. In the **'Add'** popup, enter the **endpoint name** and **LAN IP**.

3. Select the device to which the endpoint belongs.

4. Configure the endpoint's **virtual IP** to enable remote communication through the router's VPN communication tunnel. There are two ways to assign virtual IP to endpoint:

1.  **Auto**: The system automatically assigns virtual addresses to endpoints.  
    
2.  **Manual**: In cases where specific virtual IP are required for endpoints, you can define them yourself. The allowable range for virtual IP is: x.x.x.2-x.x.x.254.  
    

![](images/img_b15f57e3.png)  

┃**Note:** A maximum of 243 endpoints can be added to a connector device.

## **7.****4 Configure Account**

**1、Add an account**

When accessing the Connector network details, go to the **'Accounts'** page to add accounts to the Connector network.

1. Click on the **'Add'** action in the upper right corner of the Accounts list.

2. In the 'Add Account' popup, enter the **account name**.

3. Configure the **virtual IP** for the account to establish a VPN communication tunnel through the virtual IP and DeviceLive. There are two types of virtual IP assignment:

1.  **Float IP**: A floating IP is not pre-assigned and is dynamically allocated based on server availability when the account connects.  
    
2.  **Static IP**: In cases where specific virtual IP are required for the account, you can define them as static IP. Once defined, they will not change. The allowable range for virtual IP is: 10.16.0.2-10.16.15.255.  
    

![](images/img_c6f66e2f.png)  

┃**Note:** A maximum of 4,000 devices and accounts can be added to a connector network.  

**2、Connect the account to the client**

After the account is added, you must use the connector client to establish a VPN tunnel. The platform supports MacOS, Windows, iOS, and Android clients.Below is an example of Windows operation:

1\. **Download the Windows client:** Access the Connector Network details, go to the **'Accounts'** tab, and click on the Connector Client to **download the Windows version**.

![](images/img_ced65366.png)  

2\. **Download the client configuration file:** On the **'Accounts'** tab, select an account, and **download** the corresponding client configuration.  

![](images/img_308671b2.png)  

3\. After the client has installed well, open the client software, import the client configuration file, and then click "**CONNECT**" to establish the VPN tunnel between the account and DeviceLive. Next, you can use this VPN tunnel to remotely access your endpoints under the device or download and upload data.  

![](images/img_01e4210b.png)  

  

## **7****.5 View Connection Records**

Both devices and accounts can view the history of connector, which can assist in analyzing business trends or identifying abnormal nodes. The recorded information includes historical connection status, duration of individual connections, total VPN traffic, and uplink and downlink traffic of a single connection.

To access the connector history, go to the connector network details and click on the **'Connection History'** option in the device list and account list operations column.  

![](images/img_f84fb1e6.png)  

  

# **8.Groups**

You can add or remove groups to configure devices in bulk. If there's a conflict between group settings and individual preferences, the device follows individual preferences. If the group is for EC series products, it enables project management based on the group.

## **8.1 Overview and Device**  

### **8.1.1 Overview**  

You can view statistics for the current group, including distribution of device configuration status, firmware upgrade status, firmware versions,offline top 10, alerts top 10 by device, and alerts top 10 by type.  

![](images/img_ee4e53df.png)  

┃**Note:** If a device has a different firmware version than the group, it's marked as "suspended," meaning you can't configurate it remotely. Click the **unusual icon** in "**Firmware Distribution**" on the "**Overview**" page to upgrade devices with mismatched firmware.  

### 8.1.2 Devices  

Display current group information and easily manage device transfers as needed for your business.

-   **Add Devices**: Click "**Move Devices**" and the system will automatically filter devices that match the group's product model. You can then select multiple devices to add them to the group.
-   **Remove Devices**:After selecting the devices, click "**Remove**". After a confirmation, the devices will be removed from the group, and their group configurations will be automatically cleared.  
    

![](images/img_581548e3.png)  

  

## **8.2 Firmware Configuration**  

### **8.2.1 Edit Confirmation**

Users can go to the group details, and click the "**Edit**" button to edit the group‘s firmware configuration’. 

 ![](images/img_ad53639f.png)

In the configuration editing popup, the following operations are supported:

1.  **Pending Configuration**: Click the "Pending Configuration" button, and the configurations made during this session will be saved to the platform backend but not yet deployed to the devices within the group.
2.  **Discard Changes**: Click the **"Discard Changes"** button, and any operations made during this session will be discarded.
3.  **Commit Charges**: Click the "**Commit Charges**" button to apply the configurations made during this session to the devices within the group.  
    

┃**Note:**  

      ①Individual configurations take precedence over group configurations.  

      ②Combining individual and group configurations may lead to configuration conflicts. It is recommended to avoid individual configurations on devices before adding them to a group.  

      ③When performing local configurations or individual device editing within a group, group configurations for the corresponding functional modules may become ineffective.  

### **8.2.2 Config Details**

The group details allows you to view the configuration information for the current group.

1. Click on "**Configuration**" at the top of the group list, then choose "**Config Details**".

2. In the configuration details popup, you can view the current configuration information for the selected group.

### **8.2.3 Clear**

Click on "**Clear**" in the configuration section. After confirming the action, the group configuration will be cleared.

┃**Note:** This operation only clears the group configuration, and the individual configurations of devices within the group will still be retained.

### **8.2.4 Copy to Groups**

Click on "**Copy to Groups**" in the configuration section, to copy the group configuration and perform batch configurations for devices within the target group.  

  

## **8.3 Firmware Upgrade**

The group details supports firmware upgrade operations for individual groups.

1. Click on "**Firmware**" at the top of the group details.

2. In the firmware upgrade pop-up window, choose **the target firmware version**.

3. Select the current firmware version that needs to be upgraded.

![](images/img_6d87d247.png)  

  

┃**Note**：  

      ①Online devices within the group will immediately execute the upgrade task.  

      ②Devices that are offline will perform the upgrade operation upon their next online status.  

## **8.4** DeviceSupervisor Management  

When the product model within a group supports DeviceSupervisor, bulk management of DeviceSupervisor versions and configurations for devices within the group can be performed in the group details.  

### 8.4.1 DeviceSupervisor Upgrade  

You can click on '**DeviceSupervisor**,' select '**Upgrade**,' which will open the upgrade window. From there, you can choose the target version for the upgrade process.  

![](images/img_c779c9dd.png)  

### 8.4.2 Edit  

Clicking on "**DeviceSupervisor**," selecting "**Edit**," allows you to edit the DeviceSupervisor configurations for devices within the group.  

![](images/img_22bec7ff.png)  

In the configuration editing popup, the following operations are supported:

1.  **Pending Configuration**: Click the "Pending Configuration" button, and the configurations made during this session will be saved to the platform backend but not yet deployed to the devices within the group.  
    
2.  **Discard Changes**: Click the **"Discard Changes"** button, and any operations made during this session will be discarded.  
    
3.  **Commit Charges**: Click the "**Commit Charges**" button to apply the configurations made during this session to the devices within the group.

### 8.4.3 **Config Details**  

Click on "**DeviceSupervisor**," choose "**Config Details**," and within the configuration details pop-up, you can view the current configuration information for the group.  

![](images/img_848a3967.png)  

### 8.4.4 Clear  

Click on "**DeviceSupervisor**," select "**Clear**," confirm the action, and the DeviceSupervisor configuration for the group will be cleared.  

![](images/img_018d830f.png)  

### 8.4.5 Copy to Groups  

Click on "**DeviceSupervisor**," choose "**Copy to Groups**" to replicate the DeviceSupervisor configuration to another group and perform bulk configuration for devices within the target group.  

![](images/img_6595049d.png)  

## **8.5 Commands**  

![](images/img_1a7f8ce2.png)  

### **8.5.1 Reboot**

Click "**Reboot**" to perform a batch restart of devices within the group.  

┃Note:The restart command will only affect devices within the group that are currently online. Devices within the group that are offline will not execute this command (even when they come online later, they will not restart automatically).  

  

### **8.5.2 Restore to Factory**

In the "**Groups**" menu, select the target group, click on "**Restore to Factory**",and you can perform a batch factory reset for the devices within that group.

┃**Note:**  

      ①The factory reset command will only affect the devices within the group that are currently online. Offline devices within the group will not execute this command, even when they come online later.      

      ②After a device is restored to factory settings, all historical data will be cleared. When the device comes online again, it will reapply both its individualized configuration and the group configuration.  

## 8.6 Project Management  

You can move devices running the same business application into a group according to business needs, managing applications and their required runtime environments in bulk through "Groups >> Project" This facilitates the efficient deployment, upgrade, and environment deployment of applications.

When you need to deploy or update applications for devices within a group, you can achieve this by creating and deploying a project version. A project version includes the applications you need to deploy along with the corresponding runtime environment configuration.  

### 8.6.1 Add Project Version  

Navigate to the "Projects" tab in the group details, click the "Add" button, and enter the "Add Version" page. Here, you can configure container applications, native applications, and application dependency settings as needed.

**1.Container Application Configuration**  

Container applications support two configuration modes: Compose mode and WEB mode.

-   Compose Mode: Suitable for developers familiar with Docker Compose commands. In this mode, you can use [standard Docker Compose commands](https://docs.docker.com/compose/) to configure container applications.
-   WEB Mode: Suitable for users who are not familiar with Docker Compose commands but understand simple Docker configurations. In this mode, you can generate Docker Compose configurations conveniently through a visual interface. Note: WEB mode only supports generating Docker Compose configurations for V2.4 versions.

The method for creating services and data volumes in WEB mode is as follows:

1.  Create Service

![](images/img_32f6d6fd.png)

2.  Create Volume

![](images/img_c7915f7a.png)

**2.Native Application Configuration**  

You can use [standard systemd commands](https://systemd.io/) to configure native applications.

![](images/img_0224f363.png)

  

**3\. Application Dependency Configuration**  

Application dependencies consist of two parts: application dependency files and env incremental.

-   Application Dependency Files: This includes executable files, scripts, relevant environment variables, and other necessary files for running the application.
-   Env Incremental: This includes the runtime environment required for running the application.

![](images/img_b888b9f2.png)

### 8.6.2 Other Project Version Operations  

You can perform various operations on created project versions, including release, edit, deploy to a group, copy, and delete.

-   Release: When a project version is in the 'Unreleased' state, you can release it. After release, the project version can be deployed to the associated group.
-   Edit: You can edit a project version using a similar approach as adding a new project version. Released project versions are not editable.
-   Deploy to Group: Released project versions can be deployed to the associated group. After deployment, the platform will distribute application information of the project version to all devices under the group, excluding pinned project versions.
-   Copy: You can create a new project version based on the current version. During copying, you can adjust configuration parameters as needed.
-   Delete: Support for single/batch deletion of project versions. After deletion, devices that have deployed this project version will not clear applications and environment incrementals.

![](images/img_06f15e12.png)

### 8.6.3 Docker Registry Management  

If you need to pull images from a private Docker Registry, you must configure information about the private Docker Registry. Navigate to the "Project" tab in the group details, click the "Registry Management" button, and enter the "Registry Management" page.

Click the "Add" button, configure the Registry URL, username, and password, then click "OK." Once configured, the Docker Registry will be distributed to all devices under the group.

![](images/img_b1a9a183.png)  

  

## 8.7 Env Incremental Management  

If the application running on your device has environmental requirements for the host machine (For example, to run the application properly, the host machine must have Python 3.7 runtime environment and related Python dependencies such as pymysql and paho-mqtt), you can first complete the application's debugging and running on a test device. Afterward, remove files unrelated to the runtime environment, such as logs and application programs. Next, upload the runtime environment of the test device to the platform for subsequent deployment to other devices.  

![](images/img_2984a5cf.png)  
  

### 8.7.1 Upload Env Incremental  

Go to the group details '**Env Incremental**' tab, click the '**Upload Env Incremental**' button, and configure the name, device, and description in the popup window. After configuration, click 'OK' and wait for the completion of the env incremental upload. Once uploaded, you can associate this env incremental in the 'Application Dependency Configuration' of the project version.

![](images/img_d0416852.png)

### 8.7.2 Delete Env Incremental  

Env incrementals not associated with any project version can be deleted. Env incrementals associated with a project version need to have their association with the project version removed before deletion.  

![](images/img_c8a0004c.png)  
  

# 9.Config Tasks  

When devices require configuration updates via command-line interface, you can create configuration tasks for these devices, supporting both individual and batch configurations.  

## 9.1Create Config Task  

1\. Click "**Create Config Task**" to access the task configuration page.

2\. Choose the **product model** for which configuration needs to be deployed.

3\. Paste or import the **configuration command-line content**.

4\. **Select the devices** to which this configuration should be applied.

5\. Click "**Sure**".  

![](images/img_7e0f3915.png)  

┃**Note:**    

      ① Only certain device models support command-line configuration, as indicated by platform prompts.  

      ② For products that do not support command-line configuration, you can utilize the "Firmware Remote Configuration" feature in device details or groups, allowing configuration deployment via GUI.  

      ③ The deployed configuration can be either full or partial; if deploying a partial configuration, only the specified settings will be altered.  

## 9.2 Configuration Task Management  

The configuration task list provides information such as task status and progress.

Clicking on the "**Task ID**" allows access to detailed information about the task, including configuration content and device execution status.  

![](images/img_7dc8b13b.png)  

  

![](images/img_756557ee.png)  

# 10.OTA Upgrade  

When you need to perform firmware or DSA version upgrades for a single device or multiple devices, you can create upgrade tasks on the "OTA Upgrade" page. You can also manage upgrade tasks within this menu.  

## 10.1 Create Upgrade Task  

1.  Click on "**Create Upgrade Task**"， select the product model, upgrade package type, target version, and upgrade time.  
    
2.  Choose the upgrade method:  
    

1.  Group-based Upgrade: After creating the upgrade task, it will distribute the upgrade task to all devices in the group that can be upgraded to the target version. If devices in the group's current version cannot be upgraded to the target version, the system won't issue upgrade tasks for these devices.  
    
2.  Device-based Upgrade: You can select one or multiple devices for the upgrade. Once the upgrade task is created, it will automatically redirect to the "Upgrade History" page, where you can view the progress of the upgrade tasks.  
    

![](images/img_c74b059b.png)  

  

![](images/img_799092ed.png)  

## 10.2 Task Management  

1.  Canceling Upgrade Tasks: Only tasks in "Waiting" and "In Progress" status can be canceled.
2.  Viewing Upgrade Tasks: Access the "Upgrade History" tab to see the upgrade records for all devices.  
    

# **11\. Alerts**  

## **11.1 Alert Settings**

The platform supports multiple types of alarms, allowing you to customize the specific alert types you wish to receive and the groups for which alerts should be reported. Additionally, you can choose the notification recipients and methods for these alerts.

1. Go to the **Alerts** menu and click "**Alert Settings**" in the upper left corner of the alert list.

2. Click "**Add Rule**" in the upper right corner of the alert rule list.

3. Select the group to be monitored, alert type, notification users, and notification method, then

click "**Save**". If no notification users are set, the generated alarms will only be displayed on the platform. The platform supports two notification methods:

1.  **Email**: When an alert is triggered, an alert email will be sent to the configured notification users.  
    
2.  **SMS**: When an alert is triggered, an alert SMS will be sent to the configured notification users. Users need to bind their phone numbers to the platform.   
    

![](images/img_307aac70.png)  

The explanation for alarm types is as follows:

| Alert Type | Description |
| --- | --- |
| **Connect to the Platform** | Devices can be online on the platform for more than N minutes.Configurable time range: 5 -120 minutes. |
| **Disconnect from Platform** | Devices can be disconnected (offline) from the platform for more than N minutes. Configurable time range: 5 -120 minutes. |
| **Configuration Sync Failed** | The device failed to synchronize its configuration with the cloud platform due to network or other issues. |
| **Configuration Modified Locally** | The device configuration was modified by the user via the local interface or CLI. |
| **Reboot** | The device's system has been rebooted. |
| **Firmware Changed** | The device's local firmware has been upgraded or downgraded, including: local device execution of upgrades, platform upgrades to the device firmware version. |
| **License Expiring Soon** | The license applied to the device on the platform will expire in N days. Configurable time range: 1-30 days. |
| **License Expired** | The license applied to the device has expired, rendering the device unable to utilize the platform's functionalities. |
| **Client Online** | A client connected under the device has connected. |
| **Client Offline** | A client connected under the device has disconnected. |
| **Primary Uplink Type Switch** | The upstream link type of the device has changed, either due to manual intervention or backup link switching. |
| **SIM Switch** | The device with dual SIM cards has undergone a primary-secondary SIM card switch, such as the cellular link transitioning from SIM1 to SIM2. |
| **Wired Wan Connected** | The current upstream link for the device is wired, and it's connected. |
| **Wired Wan Disconnected** | The current upstream link for the device is wired, and it's disconnected. |
| **Cellular Wan Connected** | The current upstream link for the device is cellular, and it's connected. |
| **Cellular Wan Disconnected** | The current upstream link for the device is cellular, and it's disconnected. |
| **Wi-Fi(STA) Wan connected** | The current upstream link for the device is Wi-Fi（STA）, and it's connected. |
| **Wi-Fi(STA) Wan Disconnected** | The current upstream link for the device is Wi-Fi(STA), and it's disconnected. |

## **11.2 Alert List**

Under the "**Alerts**" menu, you can view the alert information for all devices on the platform. This information includes the time when the alert was generated, its type, device name, group, description, and more.  

# **12.Reports**  

The report page displays historical generated report information and supports adding new reports and managing report information.  

![](images/img_49bc53f7.png)  

## **12.1 Create Report**

Click "**Create New**" to create a new report by selecting report information based on your business requirements.

1. In the "**Reports**" menu, click "**Create New**" to enter the report content selection page.

2. **Choose the type of report**: Select the report content you want to include in the report.

3. **Select Devices/Groups**: Choose whether you want to include all devices, organizations, or specific groups in the report.

4. **Set the reporting period**: Define the time range for the report data, with a maximum selection of up to the last 30 days.

5. **Configure report details**: Specify whether you want to generate the report in PDF or Excel format and provide an email address for receiving the report. If you want to schedule regular report generation, you can set the time for daily, weekly, or monthly reports.

6. After submission, the platform will generate the report according to the selected configuration at the specified time. If you have set an email address to receive the report, you will receive an email notification when the report is ready.  

![](images/img_e546ef4f.png)  

![](images/img_713fb189.png)  

![](images/img_7f199bf6.png)  

![](images/img_69e5010b.png)  

## **12.2 Manage reports**

Clicking "**Manage Now**" allows you to view all the newly added reports with scheduled tasks.

1.  **Edit Report**: Click on "**Edit**" to go to the "Choose Report" page, where you can configure other information besides the report content. After saving the configuration, the platform will generate the report based on the new configuration rules.  
    
2.  **Delete Report**: Click "**Delete**" to delete a scheduled report. Once deleted, the platform will no longer generate reports for that scheduled task.

## **12.3 Report History  
**

You can view the generated reports on DeviceLive from the Report menu. You can perform the following operations:

1.  **Download Report**: You can download the generated PDF or Excel report file.  
    
2.  **Delete Report**: You can delete the report if you no longer need the report.  
    
3.  **Re-run**: After clicking "Re-run", the list will generate a new report information immediately with the original configuration.

# **13.Messages**

Click the Messages menu to receive messages from DeviceLive, including product messages, firmware messages, and service messages.

![](images/img_c02ed546.png)  

# **14.Logs**

On the page Logs, you can view **Activity Logs**, **Login Logs**.

![](images/img_84ae1d41.png)  

## **  
14.1 Activity Logs**

Click the **Activity Logs** tab to view the operations performed by all users on DeviceLive.

## **14.2 Login Logs**

Click the **Login Logs** tab to view the login records of all users on DeviceLive. Upgrade Logs, Activity Logs, Login Logs.

# **15.Licenses**

DeviceLive subscribes to each device based on licenses and charges accordingly. You can choose different types of licenses for devices based on your needs, and the service scope of each type of license is as shown on the purchase page. The platform supports online purchase of service licenses, eliminating the need for cumbersome offline communication. Upon successful online purchase and application to the device, the service is immediately activated.  

To access "InHand Cloud Service," click on "**Subscription**" to view the usage status of licenses and device permits under the current account. You can also manage and purchase licenses.  

![](images/img_820e80c1.png)  

![](images/img_a4f58c6e.png)  

  

## **15.1 Summary**

On the "**Subscriptions>> Overview**" page, you can view statistical information about the licenses under your account.

| Function Modules | Description |
| --- | --- |
| **Device Overview** | View the number of devices in different service statuses, click to apply filter conditions, and navigate to the "Devices" page:  -   **Total**: Total count of devices under the current account. -   **Available**: Devices capable of connecting to the platform and using its functionalities (determined by applied device licenses). -   **Unavailable**: Devices unable to connect to the platform due to expired or unapplied licenses. Licensing required for these devices. -   **Anomaly**: After a device license expires, the device might retain partial platform functionality, but it may lack expected features. |
| **License Overview** | To view the total number of licenses and statistics for different license statuses, click to apply filter conditions and navigate to the "Licenses" page:  -   **Total**:The total count of licenses under the current account. -   **Active Used**: Licenses in an activated state and already applied to devices. -   **Expiring Soon**: The number of licenses expiring within 30 days. You can extend the remaining duration of these licenses to reduce adverse impacts on your business due to license expiration. -   **Active Unused**: Licenses in an activated state but not yet applied to any devices. These licenses still consume remaining duration. To avoid waste, prioritize applying these licenses to devices. -   **Expired**: Number of licenses that have expired. |
| **Recent License Alerts** | View license alarm information for all devices, and click "**View More**" to jump to the alarm menu. |
| **License Distribution** | View the percentage of different types of licenses in the account. |

  

## **15.2 Licenses Information**

On the "**Subscriptions>> Licenses**" page, you can view the purchased licenses, and the license information includes the following:  

![](images/img_b61f7221.png)

| Field Name | Description |
| --- | --- |
| **License Key** | The unique ID of a license. |
| **Type** | The plan type of a license. |
| **Status** | The working status of a license:  -   **Inactive**: The initial status of a license when it has not been applied to any device. -   **Active**: When a license is first applied to a device, it becomes "Active." Active licenses start consuming their subscription period, regardless of whether they are applied to a device or not. -   **Expiring Soon**: The remaining validity period of the license is less than 30 days. -   **Expired**: When the remaining subscription period of a license reaches zero, it becomes "Expired". |
| **Order ID** | The order from which the license was generated. |
| **Added At** | The time when the license was added to this account. |
| **Duration** | The subscription duration of a license is measured in days. |
| **Activation Date** | The time when the license is activated. |
| **Expiration Date** | The time when the license expires. |
| **Time Remaining** | The remaining usable duration of a license is the time left until the license expires. Once the duration is consumed, the license status changes to "expired." |
| **Associated Device** | The device to which the license is currently applied. |

  

┃**Note:**  

①Once a license is applied to a device for the first time, it becomes activated.

②An activated license will continue to consume its remaining valid duration, whether or not it is applied to a device.

③After a license has expired, it cannot be applied to any more devices. Any devices that had the license applied will lose access to the features covered by that license once it expires.  

## **15.3 Use Licenses**

On the "**Subscriptions>> Devices**" page, you can manage the application of licenses to devices, which includes the following functions:  

![](images/img_7c8b232c.png)  

**1、License status of devices**

In the "**Subscriptions>> Devices**" section, you can view the current service status for each device. The service status can have the following states:

| Status | Description |
| --- | --- |
| **Available** | Devices capable of connecting to the platform and using its functionalities (determined by applied device licenses). |
| **Unavailable** | Devices unable to connect to the platform due to expired or unapplied licenses. Licensing required for these devices. |
| **Anomaly** | After a device license expires, the device might retain partial platform functionality, but it may lack expected features. |

**2、Assign a license to one device**

On the "**Subscriptions>> Devices**" page, you can apply a license to an individual device using the following steps:

1. Click on "**Assign License**" in the operations column of the device list (The device that have not yet applied a license).

2. In the "Assign License" pop-up window, select the **license type** and the specific license you want to use, then click "**Assign**".  

![](images/img_0d3fe68d.png)  

**3、Extend device license duration**

For a licensed device, you can extend the license period before the license expires to prevent service termination and avoid affecting service operation. InCloud Manager support extending the duration of a license by merging the duration of multiple licenses. You can only superimpose licenses of the same type to a licensed device.

1. On the "**Subscriptions****\>> Devices**" page, click on the "Assign License" option in the operations column (These devices that have already applied a license).

2. In the "**Extend License**" pop-up window, select the desired license, and then click the "**Assign**" button.

┃**Note**:  

      ①After stacking, the duration of the originally applied license to the device will be extended.  

      ②Stacking is irreversible; once licenses are stacked, they cannot be separated again.  

![](images/img_4892b6f5.png)  

**4、Assign licenses to multiple devices**

When dealing with a large number of devices, the platform supports the quick batch application of licenses to multiple devices:

1. In the "**Subscriptions****\>> Devices**" page, click on "**Assign Licenses**" above the device list.

2. Select the license types you want to apply and the devices you want to apply them to. Click "Assign Licenses", and the platform will automatically allocate the licenses.

3. Confirm the license results and click "**Assign**" to make the batch licenses effective.

To maximize the utilization of licenses under your account, the platform will prioritize the allocation of activated licenses. Other types of licenses will be randomly allocated without considering the duration.  

┃**Note**: If a device already has a similar license in use, applying it again will result in the license duration being extended. This action is irreversible, so please proceed with caution.

 ![](images/img_3ca8b8f0.png)

**5、Remove license**

When a device's business use case changes, and you need to switch to a different type of license, or if the device experiences a malfunction and needs to be replaced with another device, you can revoke the license from the original device. After revoking it, the canceled license can be applied to another device, and the original device will become "unlicensed," causing the services within the license scope to immediately terminate.

1. On the "**Subscriptions****\>> Devices**" page, click the "**Remove License**" option in the action column for the target device.

2. After confirming the action in a second dialog, the license will be removed from the device.  

![](images/img_9997ebaa.png)  

**6、Remove licenses in batches**

The platform supports quickly revoking the licenses of multiple devices. After revocation, the revoked licenses can still be applied to other devices. The original devices will become "Unlicensed," and services within the license scope will be terminated immediately.

1. On the "**Subscriptions****\>> Devices**" page, select the devices from which you want to remove licenses.

2. Click on "Remove License" at the top of the device list and confirm the action when prompted.  

┃**Note:** Devices without applied licenses cannot have their licenses canceled.

![](images/img_c49d230f.png)  

## **15.4 Upgrade License**

When the functionality of a device with a lower version of the license does not meet your business requirements, you can upgrade the license for that device.

1. On the "**Subscriptions****\>> Devices**" page, click "**Upgrade License**" at the top of the device list.

2. Select the type of license you want to upgrade. Once selected, the platform will automatically filter devices bound to this license type.

3. Choose the devices you want to upgrade the license for.

4. Select the **license type** to which you want to upgrade, then click "**Submit**".

5. Confirm the results of the license upgrade. After clicking "**Confirm**", the license upgrade will take effect, and the device's license will change to the advanced version. If you choose to cancel the license upgrade, it will not take effect.

┃**Note:** You can batch upgrade already activated licenses of the same type. After the upgrade, the remaining duration of the license will be adjusted proportionally based on the price ratio between the two license types before and after the upgrade.  

![](images/img_e2fa9f6e.png)  

## **15.5 Transfer licenses**

The platform supports users in transferring licenses to other accounts. After the transfer, the license will be removed from the original account. However, licenses that have already been applied to devices cannot be transferred.

The other account needs to bind your InCloud Manager email account:

1. The system administrator should click on "**Company**" in the page header to access the Enterprise Management page.

2. In the "**Associate an MSP Account**" section, enter your InCloud Manager email account and click "**Update**". You will see that account in the customer list.

3. In the "**Subscriptions****\>> Licenses**" page, select the license you want to transfer.

4. In the "**Transfer Licenses**" popup, confirm the license you want to transfer, select the customer, and click "**Transfer**" to complete the transfer successfully.

┃**Note**:  

      ①Transferring licenses that are currently in use or have expired is not supported.  

      ②You can transfer a maximum of 1000 licenses at a time.  

![](images/img_1b80afb1.png)  

## **15.6 Transfer Devices**  

The platform supports transferring devices and their associated licenses to another account. Before performing the transfer operation, you need to follow the same steps as described in "Transfer" to have the other account bind to your InCloud Manager account.  

1.On the "**Subscriptions>> Devices**" page, select the devices you want to transfer to the customer.  

2.Click on the "**Transfer**" button at the top of the list.  

3.In the "**Transfer Devices**" pop-up window, confirm the devices to be transferred and select the customer account to transfer to. Click "Transfer" to complete the transfer successfully.  

**┃Note:** After the transfer, the devices and the associated licenses will be removed from the current account.  

![](images/img_daacf790.png)  

  

## **15.7 License Co-Termination**

When you need to align the expiration time of equipment licensing services, you can better manage your business and unify financial reconciliation and settlement. You can do the following:

1. On the "**Subscriptions****\>> Licenses**" or "**Subscriptions****\>> Devices**" page.

2. Select the license that needs to be aligned with expiration time.

3\. Click "**Co-Termination**".

4. Confirm the result information after unification, click "**OK**", and the system will automatically unify the expiration time of the selected license to the same time.  

┃**Note:**   

       ① The system will automatically unify the expiration date of the same type of license selected to the same time. For example, if the current license is 2024-06-01 and two basic licenses with a remaining duration of 1 year and one with a remaining duration of 60 days are selected, the average remaining duration is: (2\*365+1\*60) / 3= 264. Then the expiration date of the three licenses after unification is: 2024-06-01 + 264 days = 2025-02-20.  

      ② The operation of "Co-Termination" is irreversible, please operate with caution.  

![](images/img_4a75ddef.png)  

  

## **15.8 Purchase Licenses**

The license purchase process is as follows:

1\. Go to the "**Subscriptions >> Purchase**" page.

2\. Select the type of product to purchase the license.

3\. Go to the license purchase page, select the required license type, subscription duration and quantity, and click "**Buy Now**".

4\. Confirm the order, select the payment method, and click to pay.

5\. After the payment is completed, the platform will automatically generate the license.  

**| Note:**

① The order to be paid can continue to be paid within 15 days after the order is placed. If the order is still not paid after 15 days, the order will be automatically cancelled.

② Different types of licenses cover different functions, please confirm before purchase.

③ The license does not support returns.  

④If offline payment is required, please provide your purchase order PDF file and order number and send it to [incloud@inhandnetworks.com](mailto:incloud@inhandnetworks.com).

![](images/img_1ab864da.png)  

  

If you need someone else to pay for the order, you can generate the payment link and then copy to the person who paid. The payer gets the link and can pay directly with a credit card or offline.  

![](images/img_f011308b.png)  

## **15.9 Renewal of License**  

When the device's license is about to expire, you can extend the remaining license duration in advance to avoid the impact of license expiration on your business. The operation steps are as follows:

1\. Go to the "**Devices**" or "**Licenses**" page.

2\. Select the license to be renewed and click "**License** **Renewal**".

3\. Select the renewal time and click Submit.

4\. Confirm the order information and make payment. After payment, the platform will automatically extend the validity period of the selected license.  

**| Note:** Refunds are not supported on renewed orders.

![](images/img_50e7e356.png)  

  

## **15.10 Orders**

When you purchase or renew your license, you can view the details of your order on the Order page or continue to pay for your order.

![](images/img_b68af157.png)  

  

  

  

# FAQ

**1.Why does my device remain offline on the platform even after it's been configured for connection?**

The device cannot go online after it is added to the platform. Please check:

1\. Whether the network of the device is normal.  

2.Whether the local cloud service of the device is enabled.  

3\. Confirm whether the current firmware version of the device supports connecting to the cloud platform.

4\. If the device is connected to the Internet via cellular, please check whether the whitellisted address of the iot card includes: \*.inhandcloud.com, \*.amazonaws.com.

5\. Whether the device is bound with a license? If not, you can enter "**InHand Cloud Service >> Subscriptions**" to bind the license.

**2\. Does the offline device support remote firmware upgrade?**

Firmware upgrades on the cloud platform do not distinguish between online status and can be created for offline devices. When the device next goes online on the platform, the device will receive the upgrade task from the platform to perform the upgrade operation.

After the firmware upgrade task is delivered to the offline device, the firmware upgrade status will change to "Wait". If you do not need the upgrade, you can cancel it in the task list.  

  

**3.****How can external users switch to other organizations to provide technical support?**  

1.External users must first accept the email invitation and then log in to DeviceLive.

2.Click on the personal information at the top right corner of the page, then click "**Switch**."

3.In the organization switch dialog box, select the organization requiring assistance, and click "Switch" to successfully transition and provide technical support for the corresponding organization.

![](images/img_144318d0.png)  

  

**4.How do you get someone else to pay for your license order?**

If you have already generated a license purchase/renewal order, you can:  

1\. Go to the "**Subscriptions >> Orders**" page and find the order you need to pay for.

2\. Click "**Pay**".  

![](images/img_59aeec94.png)  

3\. Confirm the order information and click "**Check Out**" .  

![](images/img_8066d000.png)  

4\. Click "**Generate Payment Link**" and "**C****opy**".  

![](images/img_0740dfb4.png)  

5\. Send the copied link to the payer.  

After receiving the link, the payer can pay directly without logging into the platform.  

  

**5.How to pay for license orders offline?**  

You need to email the order number on the platform together with your purchase order to [incloud@inhandnetworks.com](mailto:incloud@inhandnetworks.com). Our operations staff will contact you.  

Prompt information is also included in the generated payment link.  

![](images/img_5703f775.png)