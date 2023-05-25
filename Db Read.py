import sqlite3
import os

# Connect to the database file named "mydb.db" in the current directory
db_file = os.path.join(os.getcwd(), "mydb.db")
conn = sqlite3.connect(db_file)

# Create a cursor object to execute queries
cur = conn.cursor()

# Execute a SELECT query to get all data from the table "users"
cur.execute("SELECT * FROM users")

# Fetch all rows from the query result
data = cur.fetchall()

# Print the data
for row in data:
    print(row)

# Close the connection
conn.close()