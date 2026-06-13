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
# PAGE
# =========================

st.title("🤖 AI Healthcare Chatbot")

st.info(
    f"Logged in as: {user_name} ({role})"
)

question = st.text_input(
    "Ask a Healthcare Question"
)

# =========================
# DATABASE DATA
# =========================

conn = sqlite3.connect("healthcare.db")

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

ehr = pd.read_sql_query(
    "SELECT COUNT(*) as total FROM ehr",
    conn
).iloc[0]["total"]

conn.close()

# =========================
# CHATBOT
# =========================

if question:

    q = question.lower()

    # Database Questions

    if "patient" in q:

        st.success(
            f"Total Registered Patients: {patients}"
        )

    elif "doctor" in q:

        st.success(
            f"Total Doctors: {doctors}"
        )

    elif "appointment" in q:

        st.success(
            f"Total Appointments: {appointments}"
        )

    elif "ehr" in q or "record" in q:

        st.success(
            f"Total EHR Records: {ehr}"
        )

    # Medical Questions

    elif "diabetes" in q:

        st.success("""
Diabetes is a chronic disease that affects blood sugar levels.

Common Symptoms:
• Frequent urination
• Increased thirst
• Fatigue

Recommendation:
Maintain healthy diet and monitor blood sugar regularly.
""")

    elif "fever" in q:

        st.success("""
Fever is usually caused by infection.

Recommendations:
• Drink plenty of fluids
• Take proper rest
• Monitor temperature

Consult a doctor if fever persists.
""")

    elif "heart" in q:

        st.success("""
Heart disease affects the heart and blood vessels.

Prevention:
• Exercise regularly
• Avoid smoking
• Maintain healthy diet
""")

    elif "covid" in q:

        st.success("""
COVID-19 is a respiratory illness.

Prevention:
• Wash hands frequently
• Wear masks when necessary
• Stay updated with vaccinations
""")

    elif "blood pressure" in q:

        st.success("""
High blood pressure can increase risk of heart disease.

Recommendations:
• Reduce salt intake
• Exercise regularly
• Monitor BP frequently
""")

    else:

        st.info("""
I don't have a specific answer for that question.

Please consult a qualified healthcare professional for medical advice.
""")