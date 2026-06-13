import sqlite3

conn = sqlite3.connect("healthcare.db")

cursor = conn.cursor()

# ==================================
# USERS TABLE
# ==================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(

    user_id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    email TEXT UNIQUE,

    password BLOB,

    role TEXT

)
""")

# ==================================
# PATIENTS TABLE
# ==================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(

    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    age INTEGER,

    gender TEXT,

    weight REAL,

    height REAL,

    blood_group TEXT,

    medical_conditions TEXT,

    family_history TEXT,

    allergies TEXT,

    insurance TEXT

)
""")

# ==================================
# DOCTORS TABLE
# ==================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors(

    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    specialization TEXT,

    qualification TEXT,

    experience INTEGER,

    available_slots TEXT

)
""")

# ==================================
# APPOINTMENTS TABLE
# ==================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments(

    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_name TEXT,

    doctor_name TEXT,

    appointment_date TEXT,

    appointment_time TEXT,

    status TEXT DEFAULT 'Pending'

)
""")

# ==================================
# EHR TABLE
# ==================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS ehr(

    record_id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_name TEXT,

    diagnosis TEXT,

    treatment TEXT,

    prescription TEXT,

    vaccination TEXT,

    doctor_name TEXT,

    visit_date TEXT

)
""")

# ==================================
# NOTIFICATIONS TABLE
# ==================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS notifications(

    notification_id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_name TEXT,

    message TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

# ==================================
# BED MANAGEMENT TABLE
# ==================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS beds(

    bed_id INTEGER PRIMARY KEY AUTOINCREMENT,

    ward_name TEXT,

    total_beds INTEGER,

    occupied_beds INTEGER,

    available_beds INTEGER,

    icu_beds INTEGER,

    emergency_beds INTEGER

)
""")

# ==================================
# STAFF TABLE
# ==================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS staff(

    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,

    staff_name TEXT,

    role TEXT,

    shift TEXT,

    department TEXT

)
""")

# ==================================
# RESOURCES TABLE
# ==================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS resources(

    resource_id INTEGER PRIMARY KEY AUTOINCREMENT,

    resource_name TEXT,

    total_units INTEGER,

    available_units INTEGER

)
""")

# ==================================
# EMERGENCY ALERTS TABLE
# ==================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS emergency_alerts(

    alert_id INTEGER PRIMARY KEY AUTOINCREMENT,

    alert_type TEXT,

    message TEXT,

    created_by TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")
conn.commit()

conn.close()

print("Database Ready Successfully")