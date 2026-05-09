# Business Intelligence Practical 1

# Import Data from Different Sources into Power BI

I analyzed your uploaded assignment document. 

---

# Aim

Import data from different sources such as:

* Excel
* SQL Server
* Oracle
* OData Feed

and load it into Power BI.

---

# Software Requirements

## Required Software

### 1. Power BI Desktop

Download:

[Power BI Desktop](https://powerbi.microsoft.com/desktop/?utm_source=chatgpt.com)

---

# Installation Steps

## Step 1: Install Power BI

1. Download Power BI Desktop
2. Run installer
3. Click:

```text id="q6y7ax"
Next → Install → Finish
```

---

# PART A — Import Excel Data into Power BI

---

# Step 1: Create Excel File

Create a file:

```text id="5r1a91"
Products.xlsx
```

---

# Sample Data

| ProductID | ProductName | Category    | Price |
| --------- | ----------- | ----------- | ----- |
| 1         | Laptop      | Electronics | 65000 |
| 2         | Mouse       | Accessories | 700   |
| 3         | Keyboard    | Accessories | 1200  |
| 4         | Mobile      | Electronics | 25000 |

Save the file.

---

# Step 2: Open Power BI

Open:

```text id="a5p93n"
Power BI Desktop
```

---

# Step 3: Import Excel Data

## Steps

1. Click:

```text id="w0wk1i"
Home → Get Data
```

2. Select:

```text id="b5qm4h"
Excel Workbook
```

3. Click:

```text id="2d2hzg"
Connect
```

4. Select:

```text id="gx6qmi"
Products.xlsx
```

5. Click:

```text id="j8j8f1"
Open
```

---

# Step 4: Select Table

In Navigator window:

* Select:

```text id="h1ehc9"
Products
```

* Click:

```text id="1y3wo4"
Load
```

---

# Expected Output

Table data will appear in Power BI Fields section.

---

# PART B — Import CSV File

---

# Step 1: Create CSV File

## students.csv

```csv id="dvlr6v"
RollNo,Name,Department,Marks
101,John,AI&DS,90
102,Alice,Computer,85
103,Bob,IT,78
```

---

# Step 2: Import CSV

## Steps

1. Click:

```text id="u9i9k3"
Home → Get Data
```

2. Select:

```text id="gmc8b7"
Text/CSV
```

3. Select:

```text id="10h5r2"
students.csv
```

4. Click:

```text id="d6lvrm"
Load
```

---

# PART C — Import Data from SQL Server

---

# Install SQL Server

Download:

[SQL Server Express](https://www.microsoft.com/en-us/sql-server/sql-server-downloads?utm_source=chatgpt.com)

---

# Sample SQL Database

## Create Database

```sql id="wo0j1m"
CREATE DATABASE CollegeDB;
```

---

## Create Table

```sql id="m1gvj2"
USE CollegeDB;

CREATE TABLE Students (
    RollNo INT,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Marks INT
);
```

---

## Insert Data

```sql id="dxb1kk"
INSERT INTO Students VALUES
(101, 'John', 'AI&DS', 90),
(102, 'Alice', 'Computer', 85),
(103, 'Bob', 'IT', 78);
```

---

# Import SQL Data into Power BI

## Steps

1. Open Power BI
2. Click:

```text id="fv1r6v"
Get Data
```

3. Select:

```text id="2tqg6r"
SQL Server
```

4. Enter:

```text id="2rjtw5"
Server Name
```

Example:

```text id="ln8y1e"
localhost
```

5. Select database:

```text id="x7tvw8"
CollegeDB
```

6. Click:

```text id="vyrg8y"
Load
```

---

# PART D — Import Data from OData Feed

Assignment document uses Northwind OData Feed. 

---

# OData URL

```text id="ob9u0n"
http://services.odata.org/V3/Northwind/Northwind.svc/
```

---

# Steps

1. Open Power BI
2. Click:

```text id="w6z9xy"
Home → Get Data
```

3. Select:

```text id="ck1w8g"
OData Feed
```

4. Paste URL:

```text id="7u8x6n"
http://services.odata.org/V3/Northwind/Northwind.svc/
```

5. Click:

```text id="r8rjdi"
OK
```

6. Select:

```text id="rqm3tp"
Orders Table
```

7. Click:

```text id="7d6p7h"
Load
```

---

# PART E — Import Oracle Database

---

# Install Oracle Database

Download:

[Oracle Database XE](https://www.oracle.com/database/technologies/xe-downloads.html?utm_source=chatgpt.com)

---

# Oracle SQL Example

```sql id="fwlmsx"
CREATE TABLE EMPLOYEE (
    ID NUMBER,
    NAME VARCHAR2(50),
    SALARY NUMBER
);
```

---

## Insert Data

```sql id="hr6qwx"
INSERT INTO EMPLOYEE VALUES (1, 'John', 50000);
INSERT INTO EMPLOYEE VALUES (2, 'Alice', 60000);
```

---

# Connect Oracle to Power BI

## Steps

1. Open Power BI
2. Click:

```text id="x5h4w6"
Get Data
```

3. Select:

```text id="n5hpkz"
Oracle Database
```

4. Enter:

```text id="0ibg4k"
Server Name
```

5. Click:

```text id="66d7rw"
Connect
```

---

# Data Transformation (Optional)

Use:

```text id="5l1h5x"
Transform Data
```

You can:

* Remove columns
* Rename columns
* Filter rows
* Change data types

---

# Important Power BI Components

| Component          | Purpose              |
| ------------------ | -------------------- |
| Get Data           | Import data          |
| Power Query Editor | Transform data       |
| Fields Pane        | Show tables          |
| Report View        | Create charts        |
| Model View         | Manage relationships |

---

# Viva Questions with Answers

## Q1. What is Power BI?

Power BI is a business intelligence and data visualization tool by Microsoft.

---

## Q2. What is OData Feed?

OData is a protocol used to share and access data over the web.

---

## Q3. What is ETL?

ETL stands for:

* Extract
* Transform
* Load

---

## Q4. What is Power Query?

Power Query is used for data cleaning and transformation.

---

## Q5. Which sources can Power BI connect to?

* Excel
* CSV
* SQL Server
* Oracle
* Web APIs
* OData
* MySQL

---

## Q6. Difference between Load and Transform Data?

| Load                  | Transform                      |
| --------------------- | ------------------------------ |
| Directly imports data | Modifies data before importing |

---

## Q7. What is legacy data?

Old data stored in outdated systems or formats.

---

# Conclusion

Successfully imported data from:

* Excel
* CSV
* SQL Server
* Oracle
* OData Feed

into Power BI and loaded it into the target system.
