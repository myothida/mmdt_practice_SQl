# Tutorial: Create a SQL Server Database from CSV Files

This tutorial will guide you through creating a SQL Server database and populating it using data from five CSV files. Follow these steps to install, configure, and load data into the database.

---

#### Step 1: Prepare Your Environment

##### Prerequisites
1. **SQL Server**: Ensure you have SQL Server installed. Refer to [How to Install SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver16).
2. **SQL Server Management Studio (SSMS)**: Install SSMS to manage your database. Download it from [SSMS Download Page](https://aka.ms/ssmsfullsetup).
3. **CSV Files**: Gather your five CSV files. For example, files could include `Customers.csv`, `Orders.csv`, `Products.csv`, `OrderDetails.csv`, and `Categories.csv`.
4. **File Format**: Ensure the CSV files are properly formatted with headers matching the desired database table schema.

---

#### Step 2: Create a New Database

1. Open **SQL Server Management Studio (SSMS)** and connect to your SQL Server instance.
2. Right-click on **Databases** in the Object Explorer pane and select **New Database**.
3. In the **New Database** dialog:
   - Provide a name for your database (e.g., `SalesDB`).
   - Click **OK** to create the database.

---

#### Step 3: Create Tables for the CSV Files

##### Using SSMS
1. Expand your newly created database in the Object Explorer.
2. Right-click on **Tables** and select **New Table**.
3. Define the schema for each table based on your CSV files. For example:

######## Table: Customers
```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName NVARCHAR(100),
    ContactNumber NVARCHAR(15),
    Email NVARCHAR(100),
    Country NVARCHAR(50)
);
```

######## Table: Orders
```sql
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
```

(Repeat for other tables based on the structure of your CSV files.)

---

#### Step 4: Load Data from CSV Files

##### Using SSMS Import Wizard
1. Right-click on your database (e.g., `SalesDB`) in the Object Explorer and select **Tasks > Import Flat File**.
2. In the Import Flat File Wizard:
   - Select your CSV file (e.g., `Customers.csv`).
   - Click **Next** and follow the prompts to map the file columns to the table columns.
3. Repeat this process for each CSV file.

##### Using `BULK INSERT`
Alternatively, use the `BULK INSERT` statement to load data directly. For example:

######## Load Customers
```sql
BULK INSERT Customers
FROM 'C:\path\to\Customers.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    TABLOCK
);
```

(Repeat for each CSV file, adjusting the file path and table name.)

---

#### Step 5: Verify the Data

1. Run queries to confirm the data was loaded successfully.

######## Query Example: Retrieve All Customers
```sql
SELECT * FROM Customers;
```

######## Query Example: Count Rows in Orders
```sql
SELECT COUNT(*) AS TotalOrders FROM Orders;
```

---

#### Step 6: Establish Relationships Between Tables

Ensure foreign key relationships are defined in the database schema.

######## Example: Create Foreign Key in `Orders`
```sql
ALTER TABLE Orders
ADD CONSTRAINT FK_Customer_Order FOREIGN KEY (CustomerID)
REFERENCES Customers(CustomerID);
```

---

#### Step 7: Create Views or Queries for Analysis

You can create views or complex queries to analyze the data.

######## Example: Create a View for Order Details
```sql
CREATE VIEW OrderDetailsView AS
SELECT
    o.OrderID, c.CustomerName, o.OrderDate, o.TotalAmount
FROM
    Orders o
JOIN
    Customers c ON o.CustomerID = c.CustomerID;
```

---

#### Step 8: Save and Backup the Database

1. Right-click on the database in SSMS and select **Tasks > Back Up...**.
2. Follow the prompts to create a backup file for your database.

---

#### Conclusion
You have successfully created a SQL Server database from CSV files. You can now run queries, create reports, or integrate this database into applications. Expand on this foundation by adding indexes, stored procedures, or additional data as needed.

