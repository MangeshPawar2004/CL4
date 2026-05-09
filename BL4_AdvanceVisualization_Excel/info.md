Below is a **complete, step-by-step procedure** for **Assignment 4: Data Analysis and Visualization using Advanced Excel**, based on the dataset and chart workflow shown in your uploaded document. The file uses a simple electronics-store sales dataset with **Month, TVs, Mobile Phones, Laptops, and Total** and then builds bar, column, line, pie, scatter, and waterfall charts, followed by chart formatting. 

# Assignment 4: Advanced Excel Data Analysis and Visualization

## 1) What this practical is about

You will create an Excel sheet, enter the given sales data, calculate totals, and then make multiple charts for analysis. The document specifically demonstrates basic charts first and then advanced chart formatting in Excel. 

## 2) Dataset to enter in Excel

Open Excel and enter the following data in **A1:D13**:

| Month     | TVs | Mobile Phones | Laptops |
| --------- | --: | ------------: | ------: |
| 1/1/2022  | 145 |           335 |      82 |
| 2/1/2022  | 145 |           362 |     126 |
| 3/1/2022  | 105 |           311 |      95 |
| 4/1/2022  | 171 |           259 |      93 |
| 5/1/2022  | 178 |           277 |     107 |
| 6/1/2022  | 167 |           292 |     145 |
| 7/1/2022  | 200 |           385 |      77 |
| 8/1/2022  | 181 |           388 |      78 |
| 9/1/2022  | 152 |           291 |      83 |
| 10/1/2022 | 143 |           345 |     102 |
| 11/1/2022 | 114 |           399 |      99 |
| 12/1/2022 | 109 |           250 |     101 |

This matches the example dataset from the assignment. 

---

# 3) Create the Total column

The assignment shows a **Total** column in the dataset. Add it as column **E**.

## Formula

In **E2**, enter:

```excel
=SUM(B2:D2)
```

Then drag it down up to **E13**.

### Result

Each row will now show the monthly total sales across TVs, Mobile Phones, and Laptops.

---

# 4) Add totals at the bottom

In row **14**, add summary totals:

* **A14** → `Total`
* **B14** → `=SUM(B2:B13)`
* **C14** → `=SUM(C2:C13)`
* **D14** → `=SUM(D2:D13)`
* **E14** → `=SUM(E2:E13)`

The document’s sample totals row is exactly the type of summary used for the pie chart section. 

---

# 5) Format the sheet

Before creating charts:

1. Select **A1:E14**
2. Make the header row bold
3. Center-align the values if needed
4. Adjust column width so all text is visible
5. Apply borders if you want the sheet to look neat

The document suggests formatting cells such as adjusting column width and bolding headers. 

---

# 6) Create the required charts

## A. Bar Chart

The assignment explains that bar charts are useful for comparing categorical data and shows how to choose **2-D Bar → Clustered Bar**. 

### Steps

1. Select **A1:D13**
2. Click **Insert**
3. Click the **Bar Chart** dropdown
4. Choose **2-D Bar → Clustered Bar**
5. Rename the title to something like:
   **Electronic Store Sales 2022**

### What it shows

Comparison of TVs, Mobile Phones, and Laptops across months.

---

## B. Column Chart

The file also shows **2-D Column → Clustered Column** as another basic chart type. 

### Steps

1. Select **A1:D13**
2. Click **Insert**
3. Click the **Column Chart** dropdown
4. Choose **2-D Column → Clustered Column**
5. Add a chart title

### What it shows

Monthly sales comparison in vertical bars.

---

## C. Line Chart

The assignment describes line charts as useful for showing change over time and uses **Line with Markers**. 

### Steps

1. Select **A1:D13**
2. Click **Insert**
3. Click **Line Chart**
4. Choose **2-D Line → Line with Markers**
5. Add title:
   **Electronic Store Sales 2022**

### What it shows

Trend of each product category across the months.

---

## D. Pie Chart

The document says pie charts are used to show proportions of a whole and compares total sales between categories using the totals row. 

### Steps

1. Select **B1:D1**
2. Hold **Ctrl** and select **B14:D14**
3. Click **Insert**
4. Click **Pie Chart**
5. Choose **2-D Pie → Pie**
6. Add data labels if needed

### What it shows

Share of total sales by product category.

---

## E. Scatter Plot

The assignment includes scatter plots under advanced techniques to compare two variables. 

### Steps

1. Select **A1:C13**
2. Click **Insert**
3. Click **Scatter Chart**
4. Choose **Scatter with Smooth Lines and Markers**
5. Add title:
   **TVs vs Laptops Comparison**

### What it shows

Relationship between two numeric series.

---

## F. Waterfall Chart

The practical also demonstrates a waterfall chart for monthly total sales. 

### Steps

1. Select **A2:A13**
2. Hold **Ctrl** and select **E2:E13**
3. Click **Insert**
4. Click **Waterfall Chart**
5. Choose **Waterfall**

### What it shows

Month-wise contribution to total sales.

---

# 7) Chart formatting steps

The document spends many pages on formatting options like title, legend, labels, styles, axis titles, and axis formatting. 

## A. Add chart title

1. Click the chart
2. Go to **Chart Design**
3. Click **Add Chart Element**
4. Choose **Chart Title**
5. Pick **Above Chart**
6. Type:
   **Electronic Store Sales 2022**

## B. Move legend

1. Click chart
2. Go to **Chart Design**
3. Click **Add Chart Element**
4. Select **Legend**
5. Choose **Top**

## C. Add data labels

1. Click chart
2. Go to **Chart Design**
3. Click **Add Chart Element**
4. Select **Data Labels**
5. Choose **Above** or **Center**

## D. Add axis titles

1. Click chart
2. Go to **Chart Design**
3. Click **Add Chart Element**
4. Choose **Axis Titles**
5. Add:

   * Horizontal Axis: `Month`
   * Vertical Axis: `Products Sold`

## E. Change chart style

1. Click chart
2. Go to **Chart Design**
3. Choose a style from **Chart Styles**
4. Click **Change Colors** if needed

## F. Format axis

1. Right-click the axis
2. Choose **Format Axis**
3. Change bounds, units, or number format if needed

The assignment shows these formatting operations with screenshots and examples on pages 11–17. 

---

# 8) If you want a clean lab file structure

Use this order in your Excel sheet:

* Row 1: headers
* Rows 2–13: monthly data
* Row 14: totals
* Separate chart sheets or the same sheet with charts placed below the table

---

# 9) Code if any

There is **no programming code** for this practical. It is an **Excel-based GUI assignment**. The only “code-like” part is the formula used for totals and summary values:

```excel
=SUM(B2:D2)
```

and totals at the bottom:

```excel
=SUM(B2:B13)
=SUM(C2:C13)
=SUM(D2:D13)
=SUM(E2:E13)
```

---

# 10) Simple conclusion to write in the record

**Conclusion:** Thus, Data Analysis and Visualization was successfully performed using Advanced Excel on the given sales dataset. 

If you want, I can turn this into a **ready-to-paste practical write-up** with **Aim, Objective, Procedure, Observations, Viva Q&A, and Conclusion** in proper lab format.
