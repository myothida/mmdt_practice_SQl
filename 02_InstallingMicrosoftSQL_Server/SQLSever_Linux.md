# How to Install Microsoft SQL Server on Linux

This tutorial will guide you through the process of installing Microsoft SQL Server on a Linux machine.

---

#### References

1. [What is SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver16)
2. [Install SQL Server on Linux](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-red-hat?view=sql-server-ver16)

---

#### Prerequisites

Before you begin, ensure that your system meets the following requirements:

- **Operating System**: A supported Linux distribution (Ubuntu, Red Hat Enterprise Linux, SUSE Linux Enterprise Server, etc.).
- **Disk Space**: At least 6 GB of free space.
- **RAM**: Minimum 2 GB (4 GB recommended; 8 GB for optimal performance).
- **Network Access**: Ensure the machine can connect to the internet.
- **Superuser Privileges**: You need `sudo` access.

---

#### Step 1: Install the SQL Server Repository

1. Open a terminal and run the appropriate command for your Linux distribution to add the Microsoft SQL Server repository.
   - **Ubuntu**:

     ```bash
     wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
     sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/20.04/mssql-server-2019.list)"
     ```

   - **Red Hat**:

     ```bash
     sudo curl -o /etc/yum.repos.d/mssql-server.repo https://packages.microsoft.com/config/rhel/8/mssql-server-2019.repo
     ```

   - **SUSE**:

     ```bash
     sudo zypper addrepo -f https://packages.microsoft.com/config/sles/15/mssql-server-2019.repo
     ```

---

#### Step 2: Install SQL Server

1. Update your package list:

   - **Ubuntu**:
     ```bash
     sudo apt-get update
     ```
   - **Red Hat** or **SUSE**:
     ```bash
     sudo yum update
     ```

2. Install the SQL Server package:

   ```bash
   sudo apt-get install -y mssql-server  # For Ubuntu
   sudo yum install -y mssql-server     # For Red Hat
   sudo zypper install -y mssql-server # For SUSE
   ```

---

#### Step 3: Configure SQL Server

1. Run the setup script to configure the SQL Server instance:

   ```bash
   sudo /opt/mssql/bin/mssql-conf setup
   ```

2. Follow the prompts to:

   - Select the edition (Developer, Evaluation, etc.).
   - Accept the license terms.
   - Set a strong password for the `sa` (System Administrator) account.

3. Verify that the SQL Server service is running:

   ```bash
   systemctl status mssql-server
   ```

   - To start the service manually:
     ```bash
     sudo systemctl start mssql-server
     ```

---

#### Step 4: Install SQL Server Command-Line Tools (Optional)

1. Add the tools repository:

   - **Ubuntu**:
     ```bash
     sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/20.04/prod.list)"
     ```
   - **Red Hat**:
     ```bash
     sudo curl -o /etc/yum.repos.d/msprod.repo https://packages.microsoft.com/config/rhel/8/prod.repo
     ```

2. Install the tools:

   ```bash
   sudo apt-get install -y mssql-tools unixodbc-dev  # For Ubuntu
   sudo yum install -y mssql-tools unixODBC-devel   # For Red Hat
   ```

3. Add the tools to your PATH:

   ```bash
   echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
   source ~/.bashrc
   ```

---

#### Step 5: Connect to SQL Server

1. Open a terminal and connect to the server using the `sqlcmd` tool:

   ```bash
   sqlcmd -S localhost -U sa -P '<YourPassword>'
   ```

2. Test the connection by running a simple query:

   ```sql
   SELECT @@VERSION;
   GO
   ```

---

#### Step 6: Enable Firewall Rules (Optional)

If the SQL Server instance needs to be accessed remotely:

1. Open the necessary ports (default: 1433):
   ```bash
   sudo ufw allow 1433/tcp  # For Ubuntu
   sudo firewall-cmd --add-port=1433/tcp --permanent  # For Red Hat/SUSE
   sudo firewall-cmd --reload
   ```

---

#### Troubleshooting

- **Service Not Starting**:
  - Ensure you have sufficient permissions.
  - Check the logs at `/var/opt/mssql/log/`.
- **Connection Issues**:
  - Verify that port 1433 is open and accessible.
  - Check your firewall and SELinux settings.
- For further assistance, refer to the official [SQL Server on Linux Documentation](https://learn.microsoft.com/en-us/sql/linux/overview-sql-server-on-linux).

---

