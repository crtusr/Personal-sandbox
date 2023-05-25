import sqlite3

conn = sqlite3.connect('my_database.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS comments
             (id INTEGER PRIMARY KEY, content TEXT)''')

c.execute("INSERT INTO comments (content) VALUES ('Hello, World!')")

conn.commit()
conn.close()