import sqlite3
import pandas as pd
import os
from IPython.display import display # Importar la librería IPython

# Connect to the database file named "mydb.db" in the current directory
db_file = os.path.join(os.getcwd(), "mydb.db")
conn = sqlite3.connect(db_file)

# Read the data from the table "users" as a pandas DataFrame
df = pd.read_sql("SELECT * FROM users", conn)

# Display the DataFrame as an interactive table
display(df) # Usar la función display para mostrar la tabla
