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

st.title("📈 Report Analysis")

st.info(
    f"Logged in as: {user_name} ({role})"
)

conn = get_connection()

# =========================
# COUNTS
# =========================

patients = pd.read_sql_query(
    "SELECT COUNT(*) as total FROM patients",
    conn
).iloc[0]["total"]

doctors = pd.read_sql_query(
    "SELECT COUNT(*) as total FROM doctors",
    conn
).iloc[0]["total"]

appointments = pd.read_sql_query(
    "SELECT COUNT(*) as total FROM appointments",
    conn
).iloc[0]["total"]

ehr_records = pd.read_sql_query(
    "SELECT COUNT(*) as total FROM ehr",
    conn
).iloc[0]["total"]

conn.close()

# =========================
# SUMMARY
# =========================

st.subheader("Hospital Summary")

st.write(f"Total Patients : {patients}")
st.write(f"Total Doctors : {doctors}")
st.write(f"Total Appointments : {appointments}")
st.write(f"Total EHR Records : {ehr_records}")

# =========================
# AI INSIGHTS
# =========================

st.subheader("AI Insights")

if patients == 0:
    st.warning(
        "No patient records available."
    )

if doctors == 0:
    st.warning(
        "No doctors registered."
    )

if doctors > 0:

    ratio = patients / doctors

    st.write(
        f"Patient-Doctor Ratio : {ratio:.2f}"
    )

    if ratio > 20:

        st.error(
            "High patient load detected. Consider adding more doctors."
        )

    elif ratio > 10:

        st.warning(
            "Patient load is increasing."
        )

    else:

        st.success(
            "Doctor availability looks healthy."
        )

if appointments > 50:

    st.warning(
        "Large number of appointments detected."
    )

elif appointments > 20:

    st.info(
        "Appointment volume is moderate."
    )

else:

    st.success(
        "Appointment workload is manageable."
    )

if ehr_records < patients:

    st.warning(
        "Some patients may not have EHR records."
    )

else:

    st.success(
        "EHR coverage is good."
    )

# =========================
# FINAL RECOMMENDATION
# =========================

st.subheader("Recommendation")

if doctors > 0 and patients/doctors > 20:

    st.error(
        "Recommendation: Recruit additional doctors."
    )

else:

    st.success(
        "Current hospital resources appear sufficient."
    )