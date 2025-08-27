# 🛒 Retail Transactions Data Cleaning & Visualization


##  📌 Project Overview

This project focuses on cleaning, preprocessing, and visualizing a retail transactions dataset. The dataset contains 10,000+ transactions (a sample of 2000 is provided) with details about customers, purchases, and payment modes.

The objective is to create a clean, analysis-ready dataset and generate visual dashboards that uncover customer demographics, sales insights, and spending patterns.

## 📂 Dataset Details

File: RETAIL_TRANSACTIONS_2000.csv


| Column | Description |
|--------|-------------|
| TransactionID | Unique ID for each transaction |
| CustomerID | Unique ID for customers |
| Gender | Male / Female / Other |
| Age | Age of customer |
| City | City where purchase happened |
| ProductCategory | Electronics, Fashion, Groceries, Furniture, etc. |
| Quantity | Units purchased |
| Price | Price per unit (₹) |
| TotalAmount | Derived column (Quantity × Price) |
| PurchaseDate | Date of purchase |
| PaymentMode | Cash, Card, UPI, Wallet |

---

##⚡ Part A: Data Preprocessing

### 🔍 1. Data Inspection

- Load dataset and check size, structure, and column details.

- Identify missing values, duplicates, and inconsistent data.

### 🛠️ 2. Handling Missing Data

- Replace missing Age with mean/median.

- Replace missing City with most frequent value.

- Drop rows where critical fields (TransactionID, ProductCategory) are missing.

### 🧹 3. Data Cleaning

- Remove duplicate transactions.

- Correct negative/zero values in Quantity and Price.

### ⚙️ 4. Feature Engineering

- Recalculate TotalAmount if missing.

- Extract Month and DayOfWeek from PurchaseDate.

- Create AgeGroup (18–25, 26–40, 41–60, 60+).



### ✅ 5. Final Verification

- Ensure no missing/invalid values remain.

- Save cleaned dataset as:

- Retail_Cleaned.csv

## 📊 Part B: Data Visualization

### 👥 1. Customer Demographics

- Age distribution (histogram).
  <img width="695" height="470" alt="image" src="https://github.com/user-attachments/assets/05fd4512-5254-48aa-8ad6-472124ed3759" />


- Gender distribution (pie/bar chart).
  <img width="405" height="427" alt="image" src="https://github.com/user-attachments/assets/3029e9a8-5d31-4645-9869-83a8ef446e3d" />


- Customers by city (Top 10).
  <img width="1005" height="602" alt="image" src="https://github.com/user-attachments/assets/0f6398ba-15fd-455a-85a5-cbe3648a5377" />


### 💰 2. Sales Insights

- Total sales by product category (bar chart).
  <img width="846" height="596" alt="image" src="https://github.com/user-attachments/assets/56669229-0647-4adb-a5c7-72e5fabc83a0" />


- Monthly sales trend (line chart).
  <img width="1001" height="597" alt="image" src="https://github.com/user-attachments/assets/221c69c6-d547-4795-a9eb-eaea89501a02" />


- Payment mode usage (pie chart).
  <img width="558" height="581" alt="image" src="https://github.com/user-attachments/assets/3ddf2af6-2e19-40c9-a9c4-fcd7c5528dbf" />


### 📈 3. Advanced Insights

- Average spend per customer by age group (bar chart).
  <img width="704" height="470" alt="image" src="https://github.com/user-attachments/assets/9adefb4a-2e57-46ba-b3d7-b2acdb3971e2" />


- City-wise revenue contribution (bar chart).
  <img width="908" height="547" alt="image" src="https://github.com/user-attachments/assets/20003559-c219-431e-a87c-6ffa89aebe85" />


- Heatmap: Product Category vs Payment Mode.

## 🛠️ Tools & Libraries

- Python (Pandas, NumPy) – Data preprocessing

- Matplotlib & Seaborn – Visualizations

- Plotly / Power BI / Tableau – Interactive dashboards (optional)

## 🚀 How to Run

1.Clone this repository:
```
git clone https://https://github.com/Thiyanesh07/TCS_DS
cd retail-analysis
```

2. Install dependencies  
```bash
pip install -r requirements.txt
```

3. Run preprocessing  & visualization
```bash
jupyter notebook tcs.ipynb
```



Explore cleaned dataset:

Retail_Cleaned.csv


Run visualization notebook:

visualization.ipynb


## 📌 Deliverables

✅ Clean dataset → Retail_Cleaned.csv

✅ Jupyter Notebook → Preprocessing + Visualizations

## EXPECTED LEARNING OUTCOMES

- Understand real-world challenges in raw data.
- Learn step-by-step data preprocessing techniques (cleaning, handling missing values, encoding, feature
engineering).
- Gain hands-on skills in data visualization for storytelling.
- Build confidence in creating business-ready datasets for analysis
