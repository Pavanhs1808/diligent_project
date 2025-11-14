📘 E-Commerce Analytics Dashboard – README
📌 Overview

This project simulates a complete end-to-end data analytics pipeline for an e-commerce system.
It includes:

Synthetic data generation (Customers, Products, Orders, Order Items, Reviews)

Ingestion into a SQLite database

SQL joins for analytics

Interactive Streamlit Dashboard

Weekly CRM Report (sales, customers, revenue trends)

This project mirrors a real-world analytics setup used by companies like Amazon, Flipkart, Meesho, etc.

📂 Project Structure
ecommerce_project/
│
├── customers.csv
├── products.csv
├── orders.csv
├── order_items.csv
├── reviews.csv
│
├── ecommerce.db
│
├── load_to_sqlite.py
├── dashboard.py
├── queries.sql
│
└── README.md

🚀 Features
✔️ Synthetic e-commerce dataset (100+ rows each)
✔️ SQLite database with relationships
✔️ SQL join queries
✔️ Interactive Streamlit dashboard
✔️ Weekly CRM analytics report
✔️ Charts & tables
✔️ Easy to extend with more KPIs
📊 Data Model (5 Tables)
1. customers

customer_id

name

email

gender

age

city

signup_date

2. products

product_id

product_name

category

price

stock

3. orders

order_id

customer_id

order_date

total_amount

4. order_items

order_item_id

order_id

product_id

quantity

price

5. reviews

review_id

customer_id

product_id

rating

review_text

review_date

🛠️ 1. Load CSV Data Into SQLite

Run the ingestion script:

python load_to_sqlite.py


This will:

Create a DB named ecommerce.db

Create all 5 tables

Load each CSV into the respective table

🧪 2. Run SQL Queries

Write any SQL query in queries.sql.

Example (join query used in dashboard):

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
JOIN products p ON oi.product_id = p.product_id;

📈 3. Run the Dashboard

Install dependencies:

pip install streamlit pandas matplotlib


Run the dashboard:

streamlit run dashboard.py


Dashboard opens at:

http://localhost:8501

📅 Weekly CRM Report (Included in Dashboard)

The Weekly CRM Report section includes:

Weekly revenue

Weekly orders

Weekly new customers

Average order value

Weekly revenue trend chart

CRM metrics table

This helps analyze:

User activity

Sales spikes

Customer growth

Engagement patterns

🔮 Use Cases

This project demonstrates:

🔹 Data engineering (ETL)
🔹 Relational database modeling
🔹 SQL analytics
🔹 Dashboard design
🔹 CRM weekly reporting
🔹 Synthetic data generation
🔹 Business intelligence workflows

Useful for:

Analysts

Data engineers

ML engineers

Backend developers

Students building portfolio projects
