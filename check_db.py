import sqlite3

conn = sqlite3.connect("healthcare.db")

cursor = conn.cursor()

cursor.execute("PRAGMA table_info(ehr)")

for row in cursor.fetchall():
    print(row)

conn.close()