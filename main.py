import streamlit as st
import pandas as pd

# Example inventory data
inventory_data = [
    {"Product ID": "P001", "Name": "Apple",
        "Category": "Fruit", "Quantity": 10, "Status": "OK"},
    {"Product ID": "P002", "Name": "Banana", "Category": "Fruit",
        "Quantity": 2, "Status": "Low Stock"},
    {"Product ID": "P003", "Name": "Milk", "Category": "Dairy",
        "Quantity": 0, "Status": "Misplaced"},
    {"Product ID": "P004", "Name": "Eggs", "Category": "Dairy",
        "Quantity": 12, "Status": "Damaged"},
    {"Product ID": "P005", "Name": "Bread",
        "Category": "Bakery", "Quantity": 5, "Status": "OK"},
]

df = pd.DataFrame(inventory_data)

# --- Dashboard Title ---
st.title("Retail AI Inventory Dashboard")

# --- KPIs ---
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total Products", len(df))
kpi2.metric("Low Stock", df[df["Status"] == "Low Stock"].shape[0])
kpi3.metric("Alerts", df[df["Status"].isin(["Damaged", "Misplaced"])].shape[0])

# --- Alerts Section ---
st.header("Alerts")

# Alert for damaged or misplaced products
for idx, row in df.iterrows():
    if row["Status"] == "Damaged":
        st.warning(
            f"Product '{row['Name']}' (ID: {row['Product ID']}) is reported as DAMAGED. Please review immediately.", icon="🚨")
    elif row["Status"] == "Misplaced":
        st.warning(
            f"Product '{row['Name']}' (ID: {row['Product ID']}) is MISPLACED. Please investigate.", icon="🕵️")

# Alert for low stock
for idx, row in df.iterrows():
    if row["Status"] == "Low Stock":
        st.warning(
            f"Product '{row['Name']}' (ID: {row['Product ID']}) is LOW on stock. Consider restocking.", icon="⚠️")

# --- Inventory Table ---
st.header("Current Inventory")
st.dataframe(df, use_container_width=True)

# Optional: Add filters, search, or product management features as needed
