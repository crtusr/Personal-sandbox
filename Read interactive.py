import sqlite3
import pandas as pd
import os

# Connect to the database file named "mydb.db" in the current directory
db_file = os.path.join(os.getcwd(), "mydb.db")
conn = sqlite3.connect(db_file)

# Read the data from the table "users" as a pandas DataFrame
df = pd.read_sql("SELECT * FROM users", conn)

# Display the DataFrame as an interactive table
df