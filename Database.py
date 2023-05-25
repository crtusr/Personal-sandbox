import sqlite3
import os

# Create a database file named "mydb.db" in the current directory
db_file = os.path.join(os.getcwd(), "mydb.db")

# Connect to the database
conn = sqlite3.connect(db_file)

# Create a cursor object to execute queries
cur = conn.cursor()

# Create a table named "users" with two columns: "name" and "age"
cur.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)")

# Insert some data into the table
cur.execute("INSERT INTO users VALUES ('Alice', 25)")
cur.execute("INSERT INTO users VALUES ('Bob', 30)")

# Commit the changes and close the connection
conn.commit()
conn.close()
