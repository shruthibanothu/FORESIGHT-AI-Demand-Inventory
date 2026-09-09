
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="FORESIGHT",
    page_icon="📦",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("/content/foresight_output.csv")

# -----------------------------
# Header
# -----------------------------
st.title("📦 FORESIGHT")
st.subheader("AI-Powered Demand & Inventory Intelligence Platform")

st.markdown(
    "Demand forecasting, inventory risk detection and intelligent reorder recommendations."
)

# -----------------------------
# KPIs
# -----------------------------
total_skus = len(df)
high_risk = (df["Risk_Level"] == "HIGH").sum()
medium_risk = (df["Risk_Level"] == "MEDIUM").sum()
low_risk = (df["Risk_Level"] == "LOW").sum()
total_reorder = df["Recommended_Order_Qty"].sum()
total_excess = df["Excess_Stock"].sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total SKUs", total_skus)
c2.metric("🔴 High Risk", high_risk)
c3.metric("🟡 Medium Risk", medium_risk)
c4.metric("📦 Reorder Qty", int(total_reorder))

st.divider()

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🔎 Filters")

categories = ["All"] + sorted(
    df["Category"].dropna().unique().tolist()
)

selected_category = st.sidebar.selectbox(
    "Category",
    categories
)

risk_levels = ["All", "HIGH", "MEDIUM", "LOW"]

selected_risk = st.sidebar.selectbox(
    "Risk Level",
    risk_levels
)

filtered = df.copy()

if selected_category != "All":
    filtered = filtered[
        filtered["Category"] == selected_category
    ]

if selected_risk != "All":
    filtered = filtered[
        filtered["Risk_Level"] == selected_risk
    ]

# -----------------------------
# Inventory Risk
# -----------------------------
st.header("🚨 Inventory Risk Analysis")

display_cols = [
    "SKU",
    "Product_Name",
    "Category",
    "Current_Stock",
    "On_Order",
    "Forecast_Daily_Demand",
    "Stock_Coverage_Days",
    "Risk_Level",
    "Recommended_Order_Qty",
    "Recommended_Action"
]

st.dataframe(
    filtered[display_cols],
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# Reorder Recommendations
# -----------------------------
st.header("📦 Reorder Recommendations")

reorder = filtered[
    filtered["Recommended_Order_Qty"] > 0
].sort_values(
    "Recommended_Order_Qty",
    ascending=False
)

if len(reorder) > 0:
    st.dataframe(
        reorder[display_cols],
        use_container_width=True,
        hide_index=True
    )
else:
    st.success("✅ No immediate reorder recommendations.")

# -----------------------------
# Demand Forecast
# -----------------------------
st.header("📈 Forecasted Daily Demand")

forecast_chart = (
    filtered[
        ["SKU", "Forecast_Daily_Demand"]
    ]
    .set_index("SKU")
)

st.bar_chart(forecast_chart)

# -----------------------------
# Risk Distribution
# -----------------------------
st.header("📊 Risk Distribution")

risk_counts = (
    filtered["Risk_Level"]
    .value_counts()
)

st.bar_chart(risk_counts)

# -----------------------------
# Inventory Summary
# -----------------------------
st.header("📋 Inventory Summary")

s1, s2, s3 = st.columns(3)

s1.metric(
    "High Risk SKUs",
    int(high_risk)
)

s2.metric(
    "Excess Stock Units",
    int(total_excess)
)

s3.metric(
    "Recommended Order Units",
    int(total_reorder)
)

# -----------------------------
# SKU Search
# -----------------------------
st.header("🔍 SKU Details")

sku_list = sorted(df["SKU"].unique())

selected_sku = st.selectbox(
    "Select SKU",
    sku_list
)

sku_data = df[df["SKU"] == selected_sku]

st.dataframe(
    sku_data,
    use_container_width=True,
    hide_index=True
)

st.success(
    "FORESIGHT analysis completed successfully 🚀"
)
