import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("ecommerce.db")

# Load tables
customers = pd.read_sql_query("SELECT * FROM customers", conn)
products = pd.read_sql_query("SELECT * FROM products", conn)
orders = pd.read_sql_query("SELECT * FROM orders", conn)
order_items = pd.read_sql_query("SELECT * FROM order_items", conn)

# Join data
query = """
SELECT
    c.name AS customer_name,
    c.city,
    o.order_id,
    o.order_date,
    p.product_name,
    p.category,
    oi.quantity,
    oi.price,
    o.total_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
"""
combined = pd.read_sql_query(query, conn)

# Title
st.title("🛒 E-Commerce Dashboard")

# Summary Metrics
total_revenue = combined["total_amount"].sum()
total_customers = customers["customer_id"].nunique()
total_orders = orders["order_id"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Customers", total_customers)
col3.metric("Total Orders", total_orders)

# Category-wise Sales
st.subheader("Sales by Category")
category_sales = combined.groupby("category")["total_amount"].sum()

fig, ax = plt.subplots()
category_sales.plot(kind="bar", ax=ax)
st.pyplot(fig)

# Top Selling Products
st.subheader("Top Selling Products")
top_products = combined.groupby("product_name")["quantity"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_products)

# Full joined table
st.subheader("Full Joined Dataset")
st.dataframe(combined)

conn.close()
