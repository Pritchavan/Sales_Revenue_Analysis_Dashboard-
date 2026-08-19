# 📊 Sales & Revenue Analysis Dashboard

## 📌 Project Overview

This project is a **Sales & Revenue Analysis Dashboard** developed as part of the **ApexPlanet Data Analytics Internship**.

The project focuses on analyzing sales data to understand revenue performance, order trends, product performance, category performance, and regional sales distribution. An interactive dashboard was created using **Power BI**, along with a simple **Python automation pipeline** for data processing and KPI reporting.

---

## 🎯 Project Objectives

* Analyze overall sales and revenue performance.
* Track important business KPIs.
* Identify top-performing categories and products.
* Analyze sales performance across different regions.
* Understand monthly sales trends.
* Automate basic data cleaning and KPI reporting using Python.
* Generate an Excel report from the processed data.

---

## 🛠️ Tools & Technologies

* **Power BI** – Dashboard and data visualization
* **Python** – Data processing and automation
* **Pandas** – Data cleaning and analysis
* **Excel** – KPI and processed-data reporting
* **GitHub** – Project version control and documentation

---

## 📊 Key KPIs

| KPI                 |     Value |
| ------------------- | --------: |
| Total Revenue       |    ₹5.57M |
| Total Orders        |       650 |
| Total Units Sold    |     2,823 |
| Average Order Value | ₹8,571.80 |

---

## 📈 Dashboard Analysis

The Power BI dashboard provides insights into:

* Revenue performance
* Sales by category
* Sales by region
* Monthly revenue trends
* Top-performing products
* Overall business performance

The dashboard is designed to make the sales data easier to understand and support data-driven business decisions.

---

## 🔍 Key Business Insights

1. **Overall Sales Performance**
   The business generated approximately **₹5.57M in total revenue**, showing strong overall sales performance.

2. **Category Performance**
   The dashboard highlights the strongest-performing product categories and helps identify areas with opportunities for improvement.

3. **Regional Performance**
   Regional analysis helps identify high-performing and low-performing regions and provides opportunities for targeted business strategies.

4. **Product Performance**
   Top-performing products contribute significantly to overall revenue and should receive continued inventory and marketing support.

5. **Sales Trend**
   Monthly analysis shows variations in revenue over time and helps identify periods of stronger and weaker sales performance.

---

## 💡 Business Recommendations

* Focus marketing and promotional activities on high-performing categories.
* Maintain sufficient inventory for top-selling products.
* Improve performance in lower-performing regions through targeted promotions.
* Use sales trends to plan inventory and marketing activities.
* Explore cross-selling and product-bundling opportunities for high-performing products.

---

# 🤖 Data Automation Pipeline

As part of Day 28–29, a simple Python automation pipeline was created.

### Pipeline Process

```text
Raw Sales Data
      ↓
Load Data using Pandas
      ↓
Clean Data
      ↓
Remove Duplicates
      ↓
Handle Missing Values
      ↓
Save Processed Data
      ↓
Calculate KPIs
      ↓
Export KPI Report to Excel
```

### Automation Tasks

The Python script performs the following:

1. Loads the raw sales dataset.
2. Removes duplicate records.
3. Handles missing values.
4. Saves the processed dataset.
5. Calculates important KPIs.
6. Exports the results into an Excel report.

---

## 📁 Project Structure

```text
Sales-Revenue-Analysis/
│
├── data/
│   ├── sales_data.csv
│   └── processed_sales_data.csv
│
├── reports/
│   └── Sales_Report.xlsx
│
├── automation.py
├── requirements.txt
├── README.md
└── Dashboard_Screenshot.png
```

---

## ▶️ How to Run the Automation

### 1. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 2. Run the Python Script

```bash
python automation.py
```

### 3. Generated Outputs

After successful execution:

* Processed sales data is saved in the `data` folder.
* KPI report is generated in the `reports` folder.

---

## 📋 Requirements

The project uses the following Python libraries:

```text
pandas
openpyxl
```

---

## 📊 Dashboard

The Power BI dashboard provides an interactive view of the sales and revenue analysis.

**Dashboard includes:**

* KPI cards
* Revenue analysis
* Category analysis
* Regional analysis
* Sales trends
* Product performance

---

## 🎓 Internship

**ApexPlanet Data Analytics Internship**

This project demonstrates practical skills in:

* Data Cleaning
* Data Analysis
* Data Visualization
* Power BI
* Python Automation
* KPI Analysis
* Business Intelligence
* GitHub

---

## 👩‍💻 Author

**Priti Chavan**

Data Analytics Internship Project
ApexPlanet
