import sqlite3

conn = sqlite3.connect("logs.db")
cursor = conn.cursor()

# Show first 5 rows
rows = cursor.execute("SELECT * FROM logs LIMIT 5").fetchall()
for row in rows:
    print(row)

conn.close()
