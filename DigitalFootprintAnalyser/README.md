# Digital Footprint Analyzer (Privacy‑Focused)

An **offline analytics engine** that analyzes personal digital activity logs and generates **privacy & productivity insights**, without sending data anywhere.

This project is designed with **clean architecture**, **OOP principles**, **generators**, **caching**, and **scalability** in mind.

---

## 🔍 Problem Statement

In today’s digital world, users generate large amounts of personal data through screen usage, applications, and browsing activity. Analyzing this data can provide meaningful insights, but sending it to external services can compromise privacy.

**Goal:**
Build a **privacy‑first, offline system** that analyzes weekly digital activity data and generates clear insights about screen time, productivity, and risky browsing behavior.

---

## 🧠 Solution Approach

We designed an offline analytics pipeline that:

* Works entirely on **local files**
* Supports **multiple weeks of data**
* Auto‑detects available datasets
* Produces clean, human‑readable insights
* Avoids hardcoding and supports scalability

Overall flow:

```
Data Files → Processing → Analysis → Insights → Output
```

---

## 📁 Project Structure

```
digital_footprint_analyzer/
│
├── data/
│   ├── week1/
│   │   ├── screen_time.csv
│   │   ├── app_usage.csv
│   │   └── browsing.txt
│   ├── week2/
│   │   ├── screen_time.csv
│   │   ├── app_usage.csv
│   │   └── browsing.txt
│
├── core/
│   ├── analyzer.py
│   ├── insights.py
│   ├── cache.py
│   ├── models.py
│   └── exceptions.py
│
├── utils/
│   ├── file_readers.py
│   └── docstream.py
│
└── main.py
```

---

## 📊 Dataset Design

Each week contains **three files**:

### 1️⃣ `screen_time.csv`

Tracks daily screen usage.

**Columns:**

* `date` – Date of usage
* `minutes` – Total screen time for the day

Used to calculate:

* **Average daily screen time**

---

### 2️⃣ `app_usage.csv`

Tracks application usage.

**Columns:**

* `app` – Application name
* `category` – Usage category (Productivity, Social, Entertainment, etc.)
* `minutes` – Time spent

Used to determine:

* **Dominant usage category**

---

### 3️⃣ `browsing.txt`

Tracks visited websites.

* One domain per line

Used to calculate:

* **Risky site visits** (based on a predefined risky list)

---

## 🧩 Module‑wise Explanation

### 🔹 `utils/file_readers.py`

Responsible for:

* Reading CSV files
* Cleaning headers
* Handling Excel BOM (`utf‑8‑sig`) issues

Keeps file I/O logic separate from analysis logic.

---

### 🔹 `utils/docstream.py`

Responsible for:

* Streaming browsing data using **generators**

Benefits:

* Memory efficient
* Scales well for large files

---

### 🔹 `core/analyzer.py`

The **core analytics engine**.

Handles:

* Average screen time calculation
* Dominant category identification
* Risky site count

---

### 🔹 `core/insights.py`

Responsible for:

* Converting raw analytics results into readable insights

Keeps **presentation logic separate** from computation.

---

### 🔹 `core/cache.py`

Responsible for:

* Caching weekly reports
* Avoiding recomputation for repeated runs

Improves performance and demonstrates optimization thinking.

---

### 🔹 `core/models.py`

Defines basic data models.

Used to:

* Represent structured data
* Improve code readability and extensibility

---

### 🔹 `core/exceptions.py`

Placeholder for:

* Custom, user‑defined exceptions

Shows readiness for production‑grade error handling.

---

### 🔹 `main.py`

The **entry point** of the application.

Responsibilities:

* Auto‑detect all week folders inside `data/`
* Accept optional command‑line week arguments
* Coordinate reading, analysis, caching, and output

---

## ▶️ How to Run

### 🔹 Analyze all weeks (Auto‑detect)

```bash
python main_2weeks.py
```
### 🔹 Analyze for week1
```bash
python main.py
```
### 🔹 Analyze specific weeks

```bash
python main_2weeks.py week1 week2
```

---

## 📈 Sample Output

```
--- Digital Footprint Insights ---
 Average daily screen time: 354.3 minutes
 High Productivity usage
 Risky site visits: 3
```

---

## ⚙️ Key Features

* ✔️ Offline & privacy‑focused
* ✔️ Modular and scalable architecture
* ✔️ Multi‑week analysis support
* ✔️ Auto‑detection of datasets
* ✔️ Generator‑based file streaming
* ✔️ Caching for performance
* ✔️ Robust CSV handling (Excel‑safe)

---

## 🧠 Learning Outcomes

* Designing clean Python project structures
* Applying OOP principles in real projects
* Handling real‑world CSV issues
* Building scalable CLI‑based applications
* Writing production‑ready, maintainable code

---
#### Pokuri Venkata Ramanajaneyulu
