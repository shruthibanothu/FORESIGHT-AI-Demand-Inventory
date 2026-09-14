# FORESIGHT – AI-Powered Demand & Inventory Intelligence

FORESIGHT is an AI-powered demand forecasting and inventory intelligence platform designed to help businesses predict product demand, identify inventory risks, and make better stock replenishment decisions.

## 🚀 Live Demo

[Open FORESIGHT Live App](https://foresight-ai-demand-inventory-omhe.onrender.com/)

## 📌 Project Overview

Managing inventory is challenging because businesses need to maintain enough stock to meet customer demand while avoiding overstocking.

FORESIGHT combines **machine learning-based demand forecasting** with **inventory analysis** to provide actionable insights at the SKU level.

The platform analyzes historical sales, product information, calendar events, and inventory data to:

* Forecast daily product demand
* Identify products at risk of stockout
* Detect excess inventory
* Calculate stock coverage
* Recommend reorder quantities
* Provide interactive sales and inventory analytics

## 🧠 Machine Learning

The demand forecasting model uses **Random Forest Regression**.

### Features Used

The model uses historical demand patterns and relevant business information, including:

* Lag features: 1, 7, 14 and 28 days
* Rolling mean: 7, 14 and 28 days
* Rolling standard deviation
* Promotion information
* Calendar-related information

The model was selected after evaluating the forecasting performance and removing features that could cause data leakage.

### Model Performance

| Metric |  Value |
| ------ | -----: |
| MAE    |   2.81 |
| RMSE   |   3.67 |
| MAPE   | 33.84% |

## 📊 Dashboard Features

### 1. Sales Analytics

Provides an overview of historical sales through:

* Total units sold
* Total revenue
* Average selling price
* Sales trend over time
* Sales by category
* Top 10 products by sales

### 2. Inventory Risk Analysis

Identifies products based on their inventory condition and highlights high-risk and medium-risk SKUs.

### 3. Reorder Recommendations

Provides recommended order quantities based on forecasted demand, available inventory, safety stock and lead time.

### 4. Demand Forecast

Displays forecasted daily demand for products at the SKU level.

### 5. Risk Distribution

Provides a visual summary of inventory risk levels across products.

### 6. SKU Details

Allows users to select an individual SKU and view its inventory and forecasting information.

## 📂 Dataset

The project uses four datasets:

| Dataset                   | Description                                                |
| ------------------------- | ---------------------------------------------------------- |
| `calendar.csv`            | Calendar, weekend, holiday and promotion information       |
| `sales_daily.csv`         | Daily sales, revenue, price and promotion data             |
| `sku_master.csv`          | Product, category and pricing information                  |
| `inventory_snapshots.csv` | Stock, orders, lead time, safety stock and inventory value |

The datasets are stored inside the `data/` folder.

## 🗂️ Project Structure

```text
FORESIGHT-AI-Demand-Inventory/
│
├── app.py
├── foresight_model.ipynb
├── foresight_output.csv
├── requirements.txt
├── README.md
│
└── data/
    ├── calendar.csv
    ├── sales_daily.csv
    ├── sku_master.csv
    └── inventory_snapshots.csv
```

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Random Forest**
* **Streamlit**
* **GitHub**
* **Render**

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/shruthibanothu/FORESIGHT-AI-Demand-Inventory.git
cd FORESIGHT-AI-Demand-Inventory
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎯 Key Outcomes

FORESIGHT provides a single dashboard for understanding both **demand and inventory conditions**.

It helps users:

* Understand historical sales patterns
* Forecast future demand
* Identify potential stockout risks
* Detect excess inventory
* Make data-driven replenishment decisions

## 👩‍💻 Project

**FORESIGHT – AI-Powered Demand & Inventory Intelligence**

Built using machine learning, data analytics and Streamlit.


