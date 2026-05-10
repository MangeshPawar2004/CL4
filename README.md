# Business Intelligence and Business Data Analytics Practicals

This repository contains implementation of Business Intelligence (BI) and Business Data Analytics (BDA) practical assignments using:

- Hadoop
- MapReduce
- MongoDB
- Power BI
- Advanced Excel
- Machine Learning
- Classification
- Clustering
- Python
- SQL Server

---

# Repository Structure

```text
Assignments/
│
├── Assignment1_Hadoop_Setup/
├── Assignment2_WordCount_MapReduce/
├── Assignment3_Student_Grades_MapReduce/
├── Assignment4_MongoDB_CRUD/
├── Assignment5_PowerBI_Data_Import/
├── Assignment6_ETL_Visualization/
├── Assignment7_ETL_Superstore_PowerBI/
├── Assignment8_Advanced_Excel/
├── Assignment9_Classification/
└── Assignment10_Clustering/
```

---

# Software Requirements

## Common Requirements

- Python 3.10+
- Jupyter Notebook
- Power BI Desktop
- MongoDB
- Java JDK 8+
- Hadoop
- Git

---

# Windows Installation Guide

## 1. Install Python

Download:
https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

---

## 2. Install Jupyter Notebook

```bash
pip install notebook
```

Run:

```bash
jupyter notebook
```

---

## 3. Install Java JDK

Download:
https://www.oracle.com/java/technologies/downloads/

Verify:

```bash
java -version
javac -version
```

---

## 4. Install Hadoop

Download:
https://hadoop.apache.org/releases.html

Set environment variables:

```text
HADOOP_HOME=C:\hadoop
JAVA_HOME=C:\Program Files\Java\jdk-17
```

Add to PATH:

```text
%HADOOP_HOME%\bin
```

Verify:

```bash
hadoop version
```

---

## 5. Install MongoDB

Download:
https://www.mongodb.com/try/download/community

Create DB directory:

```bash
mkdir C:\data
mkdir C:\data\db
```

Start MongoDB:

```bash
mongod
```

Open Mongo Shell:

```bash
mongosh
```

---

## 6. Install Power BI

Download:
https://powerbi.microsoft.com/desktop/

---

# Ubuntu Installation Guide

## 1. Update System

```bash
sudo apt update
sudo apt upgrade
```

---

## 2. Install Python

```bash
sudo apt install python3 python3-pip -y
```

Verify:

```bash
python3 --version
```

---

## 3. Install Jupyter

```bash
pip3 install notebook
```

Run:

```bash
jupyter notebook
```

---

## 4. Install Java

```bash
sudo apt install openjdk-17-jdk -y
```

Verify:

```bash
java -version
javac -version
```

---

## 5. Install Hadoop

```bash
sudo apt install ssh rsync -y
```

Download Hadoop:

```bash
wget https://downloads.apache.org/hadoop/common/hadoop-3.4.0/hadoop-3.4.0.tar.gz
```

Extract:

```bash
tar -xvzf hadoop-3.4.0.tar.gz
```

Verify:

```bash
hadoop version
```

---

## 6. Install MongoDB

```bash
sudo apt install mongodb -y
```

Start MongoDB:

```bash
sudo systemctl start mongodb
```

Open shell:

```bash
mongosh
```

---

# Python Libraries Installation

Install all required libraries:

## Windows

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

## Ubuntu

```bash
pip3 install numpy pandas matplotlib seaborn scikit-learn
```

---

# Assignment 1
# Hadoop / BigQuery / Databricks / Snowflake / Redshift Setup

## Objective

- Configure Hadoop
- Setup BigQuery
- Setup Databricks
- Setup Snowflake
- Setup Redshift

## Hadoop Commands

### Windows

```bash
hdfs namenode -format
start-dfs.cmd
start-yarn.cmd
```

### Ubuntu

```bash
hdfs namenode -format
start-dfs.sh
start-yarn.sh
```

Verify:

```bash
jps
```

Open:

```text
http://localhost:9870
```

---

# Assignment 2
# Word Count MapReduce

## Compile

### Windows

```bash
javac -classpath %HADOOP_HOME%\share\hadoop\common\*;^
%HADOOP_HOME%\share\hadoop\mapreduce\*;^
%HADOOP_HOME%\share\hadoop\hdfs\* -d . *.java
```

### Ubuntu

```bash
javac -classpath `hadoop classpath` -d . *.java
```

---

## Create JAR

```bash
jar -cvf wordcount.jar *.class
```

---

## Run Program

```bash
hadoop jar wordcount.jar WCDriver input output
```

---

## View Output

```bash
hdfs dfs -cat output/part-r-00000
```

---

# Assignment 3
# Student Grade MapReduce

## Compile

### Windows

```bash
javac -classpath %HADOOP_HOME%\share\hadoop\common\*;^
%HADOOP_HOME%\share\hadoop\mapreduce\*;^
%HADOOP_HOME%\share\hadoop\hdfs\* -d . *.java
```

### Ubuntu

```bash
javac -classpath `hadoop classpath` -d . *.java
```

---

## Create JAR

```bash
jar -cvf grades.jar *.class
```

---

## Run

```bash
hadoop jar grades.jar GradeDriver input output
```

---

## View Output

```bash
hdfs dfs -cat output/part-r-00000
```

---

# Assignment 4
# MongoDB CRUD Operations

## Start MongoDB

### Windows

```bash
mongod
```

### Ubuntu

```bash
sudo systemctl start mongodb
```

---

## Open Shell

```bash
mongosh
```

---

## MongoDB Commands

### Create Database

```javascript
use collegeDB
```

### Insert Document

```javascript
db.students.insertOne({
    name:"Mangesh",
    rollNo:101,
    department:"AI&DS",
    year:4
})
```

### Find Data

```javascript
db.students.find()
```

### Update Data

```javascript
db.students.updateOne(
    {rollNo:101},
    {$set:{year:5}}
)
```

### Delete Data

```javascript
db.students.deleteOne({rollNo:101})
```

---

# Assignment 5
# Power BI Data Import

## Steps

1. Open Power BI Desktop
2. Click Get Data
3. Select:
   - Excel
   - CSV
   - SQL Server
   - OData Feed
4. Load data
5. Transform using Power Query

---

# Assignment 6
# ETL Visualization using Titanic Dataset

## Install Libraries

```bash
pip install pandas matplotlib seaborn
```

---

## Run Program

```bash
python titanic_etl.py
```

### Ubuntu

```bash
python3 titanic_etl.py
```

---

# Assignment 7
# ETL using Superstore Dataset in Power BI

## Steps

1. Open Power BI
2. Import Sample-Superstore.csv
3. Open Power Query
4. Transform data
5. Create calculated columns
6. Load data
7. Create visualizations

---

# Assignment 8
# Advanced Excel Visualization

## Charts Used

- Bar Chart
- Column Chart
- Line Chart
- Pie Chart
- Scatter Plot
- Waterfall Chart

## Excel Formula

```excel
=SUM(B2:D2)
```

---

# Assignment 9
# Classification using Machine Learning

## Install Libraries

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

## Run Program

### Windows

```bash
python classification.py
```

### Ubuntu

```bash
python3 classification.py
```

---

# Assignment 10
# K-Means Clustering

## Install Libraries

```bash
pip install numpy matplotlib scikit-learn
```

---

## Run Program

### Windows

```bash
python clustering.py
```

### Ubuntu

```bash
python3 clustering.py
```

---

# Git Commands

## Clone Repository

```bash
git clone <repository-url>
```

---

## Initialize Git

```bash
git init
```

---

## Add Files

```bash
git add .
```

---

## Commit Changes

```bash
git commit -m "Added BI and BDA practical assignments"
```

---

## Push to GitHub

```bash
git branch -M main
git remote add origin <repository-url>
git push -u origin main
```

---

# Common Errors and Solutions

## javac not recognized

### Solution

Add Java bin folder to PATH:

```text
C:\Program Files\Java\jdk-17\bin
```

---

## mongosh command not found

Add MongoDB bin folder to PATH:

```text
C:\Program Files\MongoDB\Server\8.0\bin
```

---

## Hadoop command not found

Add Hadoop bin directory to PATH:

```text
C:\hadoop\bin
```

---

# Technologies Used

- Hadoop
- HDFS
- MapReduce
- MongoDB
- Power BI
- Python
- SQL Server
- Excel
- Scikit-learn
- Jupyter Notebook

---

# Author

Mangesh Pawar  
Fourth Year Artificial Intelligence and Data Science

---

# License

This repository is created for educational and academic purposes.