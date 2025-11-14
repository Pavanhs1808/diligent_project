import sqlite3
import pandas as pd

# File paths
files = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "reviews": "reviews.csv"
}

# Connect to SQLite
conn = sqlite3.connect("ecommerce.db")

# Enable foreign keys
conn.execute("PRAGMA foreign_keys = ON;")

# --- Create tables ---
create_tables_sql = """
CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    gender TEXT,
    age INTEGER,
    city TEXT,
    state TEXT,
    signup_date TEXT
);

CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL,
    stock INTEGER
);

CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT,
    order_date TEXT,
    total_amount REAL,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE IF NOT EXISTS order_items (
    order_item_id TEXT PRIMARY KEY,
    order_id TEXT,
    product_id TEXT,
    quantity INTEGER,
    price REAL,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);

CREATE TABLE IF NOT EXISTS reviews (
    review_id TEXT PRIMARY KEY,
    customer_id TEXT,
    product_id TEXT,
    rating INTEGER,
    review_text TEXT,
    review_date TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);
"""

conn.executescript(create_tables_sql)
print("Tables created successfully!")

# --- Insert data from CSVs ---
for table, file in files.items():
    df = pd.read_csv(file)
    df.to_sql(table, conn, if_exists="append", index=False)
    print(f"Loaded {file} → {table}")

conn.close()
print("Data ingestion completed.")
