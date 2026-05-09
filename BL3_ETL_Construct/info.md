Absolutely. Below is a **fully step-by-step, beginner-friendly procedure** for **Assignment 3: ETL process to construct the database in SQL Server / Power BI**, based on your uploaded practical. The document’s main implementation flow uses **Power BI Query Editor** with **Products**, **Orders**, and **Order_Details**, then verifies the relationship view at the end. 

---

# BI Lab Assignment 3

# ETL Process in Power BI / SQL Server

## Goal

You will:

1. Extract data from a source table/feed.
2. Transform the data in Power Query.
3. Load the cleaned data into Power BI.
4. Confirm that the relationship between tables exists.

The assignment pages 5–11 show the exact Power BI workflow: removing unnecessary columns, expanding `Order_Details`, creating `LineTotal`, loading the model, and checking relationships. 

---

# Part A — What You Need Before Starting

## Software required

* Power BI Desktop
* A sample data source such as **Northwind OData feed** or SQL Server tables
* Internet connection if using OData feed

The assignment specifically mentions Power BI ETL steps and uses the Northwind OData feed for importing order data. 

---

# Part B — Exact Steps in Power BI

## Step 1: Open Power BI Desktop

1. Install and open **Power BI Desktop**.
2. On the start screen, wait for the home window to load.

The assignment begins by opening the Business Intelligence tool and creating a project in it. 

---

## Step 2: Get Data from the Source

For the easiest lab demonstration, use the **Northwind OData feed** shown in the practical.

### OData URL

```text
http://services.odata.org/V3/Northwind/Northwind.svc/
```

### Steps

1. Click **Home** tab.
2. Click **Get Data**.
3. Select **OData Feed**.
4. Paste the URL above.
5. Click **OK**.
6. When the **Navigator** window opens, select:

   * **Products**
   * **Orders**
   * and later the related **Order_Details** data
7. Click **Transform Data** or **Edit** to open **Power Query Editor**.

The assignment pages 4, 8, and 9 specifically show connecting to the Northwind feed and loading the model from Query Editor into Power BI Desktop. 

---

## Step 3: Keep Only the Columns You Need from Products

In Query Editor, you will clean the **Products** table.

### What to do

1. Open the **Products** query.
2. Select only these columns:

   * `ProductID`
   * `ProductName`
   * `QuantityPerUnit`
   * `UnitsInStock`
3. Right-click any selected column header.
4. Choose **Remove Other Columns**.

This exact step is written in the practical under “Remove other columns to only display columns of interest.” 

---

## Step 4: Expand the Order_Details Table

The document shows that `Order_Details` is nested inside `Orders` and must be expanded.

### What to do

1. Open the **Orders** query.
2. Find the `Order_Details` column.
3. Click the **expand icon** on that column.
4. In the expand dialog:

   * uncheck all columns first
   * select:

     * `ProductID`
     * `UnitPrice`
     * `Quantity`
5. Click **OK**.

The screenshots and instructions on pages 6–7 show the expand process very clearly. 

---

## Step 5: Create the LineTotal Column

Now calculate the value of each order line.

### What to do

1. Stay in **Query Editor**.
2. Go to the **Add Column** tab.
3. Click **Custom Column**.
4. In the formula box, type:

```powerquery
[Order_Details.UnitPrice] * [Order_Details.Quantity]
```

5. Set the new column name as:

```text
LineTotal
```

6. Click **OK**.

The assignment on page 7 shows this exact formula for the custom column. 

---

## Step 6: Rename and Reorder Columns

Now make the model easier to use.

### What to do

1. Drag the `LineTotal` column near `ShipCountry` or the desired position.
2. Remove the prefix `Order_Details.` from:

   * `Order_Details.ProductID`
   * `Order_Details.UnitPrice`
   * `Order_Details.Quantity`
3. Rename them to:

   * `ProductID`
   * `UnitPrice`
   * `Quantity`

This renaming and reordering step appears on pages 7–8 of the practical. 

---

## Step 7: Load the Data into Power BI

After cleaning is complete, load the data.

### What to do

1. Click **Home** tab in Query Editor.
2. Click **Close & Load**.

This loads the transformed data into the Power BI model, exactly as shown on page 8. 

---

## Step 8: Check the Relationship

The assignment asks you to confirm the relationship between **Products** and **Total Sales / Orders** tables.

### What to do

1. In Power BI Desktop, go to **Home** tab.
2. Click **Manage Relationships**.
3. Click **New**.
4. Select:

   * From table: `Orders`
   * From column: `ProductID`
   * To table: `Products`
   * To column: `ProductID`
5. Click **OK**.

The practical shows that Power BI may already detect this relationship automatically, and the dialog says a relationship already exists. 

---

## Step 9: Verify in Relationship View

### What to do

1. Close the relationship dialog.
2. On the left side of Power BI, click **Relationship View**.
3. You should see a line between the tables showing the relationship.

Pages 9–10 show the relationship window and the visual relationship diagram. 

---

## Step 10: Save the File

1. Click **File** → **Save As**
2. Save the report as:

```text
ETL_PowerBI_Assignment3.pbix
```

---

# Part C — If Your Teacher Wants SQL Server Version Too

If your lab strictly needs the database in **SQL Server**, use this simpler structure.

## Step 1: Create Database

```sql
CREATE DATABASE ETL_Demo;
GO
USE ETL_Demo;
GO
```

## Step 2: Create Staging Table

```sql
CREATE TABLE StagingProducts (
    ProductID INT,
    ProductName VARCHAR(100),
    QuantityPerUnit VARCHAR(100),
    UnitsInStock INT
);
```

## Step 3: Create Final Table

```sql
CREATE TABLE FinalProducts (
    ProductID INT,
    ProductName VARCHAR(100),
    QuantityPerUnit VARCHAR(100),
    UnitsInStock INT
);
```

## Step 4: Insert Raw Data into Staging

```sql
INSERT INTO StagingProducts VALUES
(1, 'Laptop', '1 pc', 10),
(2, 'Mouse', '1 box', 50),
(3, 'Keyboard', '1 box', 30);
```

## Step 5: Transform and Load

```sql
INSERT INTO FinalProducts
SELECT ProductID, ProductName, QuantityPerUnit, UnitsInStock
FROM StagingProducts;
```

This matches the ETL idea described in the theory section: extract from source, transform in staging, then load into the final table. 

---

# Part D — What to Write in Your Record

You can write this in your notebook:

## Title

**Perform the Extraction, Transformation and Loading (ETL) process to construct the database in SQL Server / Power BI**

## Procedure

1. Open Power BI Desktop.
2. Import source data using OData Feed / SQL Server.
3. Open Query Editor.
4. Remove unwanted columns.
5. Expand nested `Order_Details`.
6. Create `LineTotal` using custom column.
7. Rename and reorder columns.
8. Close and load the model.
9. Verify relationships in Relationship View.

---

# Part E — Viva / Oral Questions with Simple Answers

## 1. What is ETL?

ETL stands for **Extract, Transform, Load**.

## 2. What is extraction?

Extraction means taking data from the source system.

## 3. What is transformation?

Transformation means cleaning, converting, and preparing data.

## 4. What is loading?

Loading means storing the transformed data into the target system.

## 5. Why is Power Query used?

Power Query is used to clean and shape data before loading.

## 6. What is the use of relationship view?

It shows how tables are connected in the Power BI model.

## 7. Why do we create `LineTotal`?

To calculate the total value of each order line.

## 8. What is the purpose of removing extra columns?

It keeps only useful data and makes the model simpler.

---

# Part F — Very Short Conclusion

In this practical, data is extracted from the source, transformed in Power BI Query Editor, loaded into the model, and the relationship between tables is verified. The assignment pages 5–11 show this complete ETL flow step by step. 

If you upload Assignment 4, I’ll format it the same way: exact steps, code if needed, and viva answers.
===================================================================================================================================================



Yes — I will use the provided **Sample - Superstore.csv** dataset for the ETL practical. It has **9,994 rows and 21 columns**, including fields like **Order Date, Ship Date, Category, Sub-Category, Sales, Quantity, Discount, and Profit**.

# BI Lab Assignment 3

# ETL Process using the provided Superstore dataset

## Goal

Take the provided dataset, clean it, transform it, load it into Power BI, and build visuals from it.

---

# 1) What to install first

Install:

* **Power BI Desktop**
* **Python** only if you want to preprocess outside Power BI, but it is not required

For this practical, **Power BI Desktop alone is enough**.

---

# 2) Place the dataset correctly

Save the file as:

```text
Sample - Superstore.csv
```

Keep it in a folder that you can easily find, for example:

```text
D:\BI_Lab\
```

---

# 3) Open Power BI Desktop

1. Start **Power BI Desktop**
2. On the home screen, click **Get Data**
3. Select **Text/CSV**
4. Browse and choose the file **Sample - Superstore.csv**
5. Click **Open**

If the preview does not look correct, change the file encoding to **Latin1 / 1252** during import. This is useful because the dataset contains special characters in some environments.

---

# 4) Extract the data

Extraction means bringing data from the source file into Power BI.

### Steps

1. After selecting the CSV file, check the preview window.
2. Verify the columns:

   * Row ID
   * Order ID
   * Order Date
   * Ship Date
   * Ship Mode
   * Customer ID
   * Customer Name
   * Segment
   * Country
   * City
   * State
   * Postal Code
   * Region
   * Product ID
   * Category
   * Sub-Category
   * Product Name
   * Sales
   * Quantity
   * Discount
   * Profit
3. Click **Transform Data**

---

# 5) Transform the data in Power Query

This is the most important part of the ETL process.

## Step 5.1: Set correct data types

In **Power Query Editor**:

* `Order Date` → **Date**
* `Ship Date` → **Date**
* `Sales` → **Decimal Number**
* `Discount` → **Decimal Number**
* `Profit` → **Decimal Number**
* `Quantity` → **Whole Number**
* `Postal Code` → **Text** or **Whole Number**

### How to change type

1. Click the column
2. Go to **Transform**
3. Choose **Data Type**
4. Select the correct type

---

## Step 5.2: Remove unwanted rows if any

This dataset is already clean, but still check:

1. Go to **Home**
2. Click **Remove Rows**
3. Use:

   * **Remove Blank Rows** if needed
   * **Remove Duplicates** on `Row ID` if required

In the provided dataset, there are no null values and no duplicate rows, so this is mostly a verification step.

---

## Step 5.3: Trim text fields

To clean text data:

1. Select all text columns such as:

   * Customer Name
   * Segment
   * Country
   * City
   * State
   * Region
   * Category
   * Sub-Category
   * Product Name
2. Click **Transform**
3. Choose **Format → Trim**

This removes extra spaces from text values.

---

## Step 5.4: Create new calculated columns

Now add useful derived columns.

### A. Profit Margin

1. Go to **Add Column**
2. Click **Custom Column**
3. Name it:

```text
Profit Margin
```

4. Use this formula:

```powerquery
if [Sales] = 0 then null else ([Profit] / [Sales]) * 100
```

This gives profit margin in percentage.

---

### B. Shipping Days

Create a column to calculate shipping time.

1. Add another **Custom Column**
2. Name it:

```text
Shipping Days
```

3. Use this formula:

```powerquery
Duration.Days([Ship Date] - [Order Date])
```

This shows how many days the order took to ship.

---

### C. Order Year

1. Add another **Custom Column**
2. Name it:

```text
Order Year
```

3. Use:

```powerquery
Date.Year([Order Date])
```

---

### D. Order Month

1. Add another **Custom Column**
2. Name it:

```text
Order Month
```

3. Use:

```powerquery
Date.ToText([Order Date], "MMM")
```

---

# 6) Load the transformed data

After all changes are done:

1. Click **Home**
2. Click **Close & Apply**

Now Power BI loads the transformed dataset into the model.

---

# 7) Create at least 5 visualizations

Use the loaded dataset and create these 5 visuals.

## Visualization 1: Sales by Category

### Steps

1. In **Report View**, choose **Clustered Column Chart**
2. Drag:

   * `Category` to Axis
   * `Sales` to Values

### What it shows

Total sales for Furniture, Office Supplies, and Technology.

---

## Visualization 2: Profit by Region

### Steps

1. Add a **Bar Chart**
2. Drag:

   * `Region` to Axis
   * `Profit` to Values

### What it shows

Which region gives the highest profit.

---

## Visualization 3: Sales by Segment

### Steps

1. Add a **Donut Chart**
2. Drag:

   * `Segment` to Legend
   * `Sales` to Values

### What it shows

Sales contribution of Consumer, Corporate, and Home Office segments.

---

## Visualization 4: Monthly Sales Trend

### Steps

1. Add a **Line Chart**
2. Drag:

   * `Order Date` to Axis
   * `Sales` to Values

If needed, use the date hierarchy or month column.

### What it shows

How sales change over time.

---

## Visualization 5: Profit by Sub-Category

### Steps

1. Add a **Bar Chart** or **Treemap**
2. Drag:

   * `Sub-Category` to Axis
   * `Profit` to Values

### What it shows

Which sub-category is most profitable.

---

# 8) Optional extra visuals for a stronger lab file

You can also add:

* **Sales by State**
* **Quantity by Ship Mode**
* **Profit Margin by Category**
* **Sales vs Profit scatter plot**
* **Top 10 Product Names by Sales**

These make the report look stronger.

---

# 9) Save the report

1. Click **File**
2. Click **Save As**
3. Save as:

```text
Superstore_ETL_Assignment3.pbix
```

---

# 10) What to write in your practical record

## Title

**Perform the Extraction, Transformation and Loading (ETL) process to construct the database in Power BI using Sample - Superstore dataset**

## Procedure

1. Open Power BI Desktop.
2. Import the provided Superstore CSV file.
3. Open Power Query Editor.
4. Set correct data types.
5. Remove duplicates and clean text fields.
6. Create calculated columns like Profit Margin, Shipping Days, Order Year, and Order Month.
7. Close and apply the changes.
8. Create five visuals from the transformed data.
9. Save the Power BI file.

## Conclusion

The ETL process was successfully completed using the provided Superstore dataset, and the cleaned data was loaded into Power BI for analysis and visualization.

---

# 11) Viva questions and simple answers

## Q1. What is ETL?

ETL stands for **Extract, Transform, Load**.

## Q2. What is extraction?

Extraction means taking data from the source file or system.

## Q3. What is transformation?

Transformation means cleaning, converting, and preparing data.

## Q4. What is loading?

Loading means sending the final cleaned data into the target system.

## Q5. Why is Power Query used?

Power Query is used to clean, filter, and transform data before loading.

## Q6. Why do we create Profit Margin?

To understand how much profit is earned from sales.

## Q7. Why is Shipping Days useful?

It helps measure delivery efficiency.

## Q8. What is the benefit of visualizations?

They make trends, comparisons, and patterns easy to understand.

---

# 12) Best way to present this in lab

Use this order in your notebook or viva:

1. Explain dataset source
2. Explain extraction
3. Show transformations
4. Show 5 visuals
5. Give conclusion

If you upload Assignment 4, I will do the same with this dataset style and give you a ready-to-write practical file.
