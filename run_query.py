import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

query = open("queries.sql").read()
df = pd.read_sql_query(query, conn)

print(df.head(100))

conn.close()
