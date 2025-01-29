# How to Install Microsoft SQL Server

This tutorial will guide you through the process of installing Microsoft SQL Server on a Windows machine.

---

#### References

1. [What is SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver16)
2. [SQL Server Installation](https://learn.microsoft.com/en-us/sql/sql-server/install/what-s-new-in-sql-server-installation?view=sql-server-ver16)

---

#### Prerequisites

Before you begin, ensure that your system meets the following requirements:

- **Operating System**: Windows 10 or later.
- **Disk Space**: At least 6 GB of free space.
- **RAM**: Minimum 2 GB (4 GB recommended; 8 GB for optimal performance).

---

#### Step 1: Download SQL Server

1. Visit the official Microsoft SQL Server download page:\
   [Download SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads).
2. Select the edition you want to install. For most users, the **SQL Server 2022 Developer Edition** is a great choice (free for development and testing).
3. Click the **Download Now** button to start the download.

---

#### Step 2: Run the Installer

1. After downloading, open the installer `.exe` file.
2. Choose an installation type:
   - **Basic**: A simple, guided installation with default settings.
   - **Custom**: Allows you to choose specific features and configurations.
3. The installer will check for prerequisites. If everything is in order, click **Install**.

   *Note*: The installation process may take several minutes, depending on your system's performance.

---

#### Step 3: Choose the Features to Install

1. If you selected **Custom** installation, you’ll see a list of features to choose from. You can either:
   - Use the default selections.
   - Customize based on your needs. For example:
     - **SQL Server Database Engine**: Essential for database management.
     - **SQL Server Management Studio (SSMS)**: GUI tool for managing SQL Server (installed separately).
     - **SQL Server Reporting Services (SSRS)**: For reports and analysis.
     - **SQL Server Integration Services (SSIS)**: For data migration and ETL processes.
2. After selecting the features, click **Next**.

---

#### Step 4: Configure SQL Server Instance

1. Choose an instance name:
   - Use the default (`MSSQLSERVER`).
   - Specify a custom name for environments with multiple installations.
2. Select an authentication mode:
   - **Windows Authentication**: Uses your Windows login credentials.
   - **Mixed Mode**: Allows both SQL Server and Windows authentication. If selected, set a strong password for the `sa` (System Administrator) account.
3. Add SQL Server administrators (Windows users or groups).
4. Click **Next**.

---

#### Step 5: Install the Features

1. Click **Install** to begin installing the selected features.
2. If prompted by User Account Control (UAC), allow the installer to make changes to your system.
3. The process may take several minutes. Once finished, review the installation summary and click **Close**.

---

#### Step 6: Install SQL Server Management Studio (SSMS)

1. SSMS is a separate tool for managing SQL Server via a graphical user interface.
2. Download it from the following link:\
   [Download SSMS](https://aka.ms/ssmsfullsetup).
3. Run the SSMS installer and follow the prompts to complete the installation.

---

#### Step 7: Connect to SQL Server

1. Open **SQL Server Management Studio (SSMS)**.
2. In the **Connect to Server** window, provide the following details:
   - **Server Name**: `localhost` (if using the default instance) or your custom instance name.
   - **Authentication**: Choose the method you configured earlier (Windows Authentication or SQL Server Authentication).
   - If using SQL Server Authentication, enter the `sa` username and password.
3. Click **Connect**.

---

#### Step 8: If succsesful, you should see the server you just created. 

![image](https://github.com/user-attachments/assets/af18d508-d7d8-4be7-9e0c-27ee01885b23)


---

#### Troubleshooting

- **Common Issues:**
  - **Insufficient Permissions**: Run the installer as an administrator.
  - **Port Conflicts**: Ensure that port 1433 (default SQL Server port) is available.
  - **Performance Issues**: Verify that your system meets the recommended prerequisites.
- For detailed help, refer to the official [Microsoft SQL Server Documentation](https://learn.microsoft.com/en-us/sql/sql-server).

---


