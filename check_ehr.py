import sqlite3

conn = sqlite3.connect("healthcare.db")

cursor = conn.cursor()

cursor.execute("PRAGMA table_info(ehr)")

columns = cursor.fetchall()

for col in columns:
    print(col)

conn.close()