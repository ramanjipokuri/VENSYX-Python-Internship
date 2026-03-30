# 🏠 Real Estate Customer Funnel Analytics Project

---

## 📌 Project Overview

This project simulates a **real-world real estate platform** where customers interact with properties through multiple stages:

```
Search → Wishlist → Visit → Contact → Conversion
```

The goal of this project is to:

* Analyze **customer behavior**
* Understand **conversion funnel drop-offs**
* Identify **high-performing properties and builders**
* Build a **foundation for recommendation systems and ML models**

---

## 🎯 Key Objectives

* Track customer journey across different stages
* Identify high-intent customers
* Analyze property and builder performance
* Perform funnel analysis (conversion rates)
* Prepare data for machine learning models

---

## 🧱 Project Architecture

```
CSV Files
   ↓
load_data.py (Data Upload)
   ↓
MySQL Database
   ↓
queries.py (SQL Logic)
   ↓
data_loader.py (Execute Queries)
   ↓
insights.py (Business Logic)
   ↓
run_project.py (Final Output)
```

---

## 📂 Project Files & Their Purpose

---

### 1️⃣ `config.py`

**Purpose:**
Stores database configuration details.

**Why used:**

* Avoid hardcoding credentials
* Easy to update DB settings in one place

**Key Variables:**

* DB_HOST → Database location
* DB_USER → Username
* DB_PASSWORD → Password
* DB_NAME → Database name

---

### 2️⃣ `db_connection.py`

**Purpose:**
Creates a reusable database connection.

**Why used:**

* Avoid repeating connection code
* Centralized DB connection logic

**Key Function:**

* `get_engine()` → Returns SQLAlchemy engine

**Special Handling:**

* Encodes password using `quote_plus` to handle special characters

---

### 3️⃣ `load_data.py`

**Purpose:**
Loads CSV datasets into MySQL tables.

**Why used:**

* Converts raw CSV data into structured database tables
* One-time data loading process

**How it works:**

* Reads CSV using pandas
* Uploads data using `.to_sql()`

**Important Parameter:**

* `if_exists="replace"` → replaces old table with new data

---

### 4️⃣ `queries.py`

**Purpose:**
Stores all SQL queries (business logic layer).

**Why used:**

* Keeps SQL separate from Python code
* Improves readability and reusability

**Insights Covered:**

| Insight             | Description                  |
| ------------------- | ---------------------------- |
| INSIGHT_1           | Customer profile (WHO)       |
| INSIGHT_2           | Search behavior (WHAT)       |
| INSIGHT_3           | Location activity (WHERE)    |
| INSIGHT_4           | Property performance (WHICH) |
| INSIGHT_5           | Funnel analysis              |
| INSIGHT_CITY_FUNNEL | City-level funnel            |

---

### 5️⃣ `data_loader.py`

**Purpose:**
Executes SQL queries and returns results.

**Why used:**

* Acts as a bridge between SQL and Python
* Converts SQL results into pandas DataFrame

**Key Function:**

* `run_query(query)` → Executes query and returns data

---

### 6️⃣ `insights.py`

**Purpose:**
Applies business logic and calculates insights.

**Why used:**

* Keeps analytical logic separate
* Improves modularity

**Key Features:**

* Calls SQL queries
* Calculates conversion rates:

  * wishlist_rate
  * visit_rate
  * contact_rate

---

### 7️⃣ `run_project.py`

**Purpose:**
Main execution file.

**Why used:**

* Runs all insights in one place
* Displays results

---

## 🧰 Libraries Used & Why

---

### 1️⃣ `pandas`

**Purpose:**
Data manipulation and analysis

**Why used:**

* Read CSV files
* Convert SQL results into DataFrames
* Perform calculations easily

---

### 2️⃣ `sqlalchemy`

**Purpose:**
Database connection and ORM tool

**Why used:**

* Connect Python to MySQL
* Handle database operations efficiently

---

### 3️⃣ `mysql-connector-python`

**Purpose:**
MySQL driver

**Why used:**

* Enables communication between Python and MySQL

---

### 4️⃣ `urllib.parse (quote_plus)`

**Purpose:**
Encode special characters in password

**Why used:**

* Prevent connection errors due to symbols like `@`, `$`, `#`

---

## 📊 Key Insights Generated

---

### 🔹 Customer Profile (WHO)

* Identifies customer distribution by occupation
* <img width="594" height="258" alt="image" src="https://github.com/user-attachments/assets/6acf8b42-4b86-4827-a2ae-d17955f4995d" />


---

### 🔹 Search Behavior (WHAT)

* Shows what type of properties users search for
* <img width="455" height="174" alt="image" src="https://github.com/user-attachments/assets/82db9faf-502f-4042-b7c0-b85c14e558fd" />


---

### 🔹 Location Activity (WHERE)

* Identifies cities with highest engagement
* <img width="624" height="341" alt="image" src="https://github.com/user-attachments/assets/bf533679-ebe2-4486-978f-e90989ae59f9" />


---

### 🔹 Property Performance (WHICH)

* Finds properties with highest customer interest
* <img width="597" height="365" alt="image" src="https://github.com/user-attachments/assets/e8a50788-4469-4a2f-91d2-834466ba7fc8" />


---

### 🔹 Funnel Analysis

Measures:

* Search → Wishlist conversion
* Wishlist → Visit conversion
* Visit → Contact conversion
* <img width="1067" height="566" alt="image" src="https://github.com/user-attachments/assets/68214f7a-ff9b-41ca-8746-5275aea4ee0a" />


---

## 🚀 How to Run the Project

---

### Step 1: Install Dependencies

```bash
pip install pandas sqlalchemy pymysql mysql-connector-python
```

---

### Step 2: Start MySQL Server

Ensure MySQL is running on:

```
localhost:3306
```

---

### Step 3: Create Database

```sql
CREATE DATABASE real_estate_db;
```

---

### Step 4: Load Data

```bash
python load_data.py
```

---

### Step 5: Run Insights

```bash
python run_project.py
```

---

## ⚠️ Important Notes

* Ensure MySQL server is running before executing code
* Verify database credentials in `config.py`
* Use correct file paths for CSV files
* Avoid data leakage when building ML models

---

## 🧠 Future Enhancements

* Add machine learning model for conversion prediction
* Build dashboard using Power BI / Tableau
* Implement recommendation system
* Add time-based analysis

---

## ⭐ Final Summary

This project demonstrates:

* Real-world data architecture
* SQL + Python integration
* Customer funnel analytics
* Scalable and reusable code design

---
