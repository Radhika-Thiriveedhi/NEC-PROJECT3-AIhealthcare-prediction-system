import streamlit as st
import sqlite3
import pandas as pd

# =========================
# LOGIN CHECK
# =========================

if not st.session_state.get("logged_in"):
    st.error("Please Login First")
    st.stop()

role = st.session_state.get("role")
user_name = st.session_state.get("user_name")

# =========================
# DATABASE
# =========================

def get_connection():
    return sqlite3.connect(
        "healthcare.db",
        check_same_thread=False
    )

# =========================
# PAGE TITLE
# =========================

st.title("📑 Reports")

st.info(
    f"Logged in as: {user_name} ({role})"
)

# =========================
# REPORT SELECTION
# =========================

report_type = st.selectbox(
    "Select Report",
    [
        "Patients",
        "Doctors",
        "Appointments",
        "EHR"
    ]
)

conn = get_connection()

# =========================
# LOAD REPORT
# =========================

if report_type == "Patients":

    df = pd.read_sql_query(
        "SELECT * FROM patients",
        conn
    )

elif report_type == "Doctors":

    df = pd.read_sql_query(
        "SELECT * FROM doctors",
        conn
    )

elif report_type == "Appointments":

    df = pd.read_sql_query(
        "SELECT * FROM appointments",
        conn
    )

else:

    df = pd.read_sql_query(
        "SELECT * FROM ehr",
        conn
    )

# =========================
# SHOW REPORT
# =========================

st.dataframe(
    df,
    use_container_width=True
)

# =========================
# DOWNLOAD CSV
# =========================

csv = df.to_csv(
    index=False
)

st.download_button(
    label="Download CSV Report",
    data=csv,
    file_name=f"{report_type}.csv",
    mime="text/csv"
)

conn.close()