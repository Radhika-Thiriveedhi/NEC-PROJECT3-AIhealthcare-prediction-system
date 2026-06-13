import sqlite3

conn = sqlite3.connect("healthcare.db")
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE ehr ADD COLUMN doctor_name TEXT")
    print("doctor_name added")
except Exception as e:
    print("doctor_name error:", e)

try:
    cursor.execute("ALTER TABLE ehr ADD COLUMN visit_date TEXT")
    print("visit_date added")
except Exception as e:
    print("visit_date error:", e)

conn.commit()
conn.close()

print("Finished")