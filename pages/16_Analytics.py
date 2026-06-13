import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

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

st.title("📊 Healthcare Analytics Dashboard")

st.info(
    f"Logged in as: {user_name} ({role})"
)

conn = get_connection()

# =========================
# COUNTS
# =========================

patients = pd.read_sql_query(
    "SELECT COUNT(*) as count FROM patients",
    conn
).iloc[0]["count"]

doctors = pd.read_sql_query(
    "SELECT COUNT(*) as count FROM doctors",
    conn
).iloc[0]["count"]

appointments = pd.read_sql_query(
    "SELECT COUNT(*) as count FROM appointments",
    conn
).iloc[0]["count"]

ehr = pd.read_sql_query(
    "SELECT COUNT(*) as count FROM ehr",
    conn
).iloc[0]["count"]

# =========================
# METRICS
# =========================

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Patients",
        patients
    )

    st.metric(
        "Total Doctors",
        doctors
    )

with col2:
    st.metric(
        "Appointments",
        appointments
    )

    st.metric(
        "EHR Records",
        ehr
    )

# =========================
# APPOINTMENT STATUS
# =========================

try:

    status_df = pd.read_sql_query(
        """
        SELECT status,
        COUNT(*) as total
        FROM appointments
        GROUP BY status
        """,
        conn
    )

    if not status_df.empty:

        fig = px.pie(
            status_df,
            names="status",
            values="total",
            title="Appointment Status"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

except:
    pass

# =========================
# RESOURCE UTILIZATION
# =========================

try:

    resource_df = pd.read_sql_query(
        """
        SELECT resource_name,
        available_units
        FROM resources
        """,
        conn
    )

    if not resource_df.empty:

        fig2 = px.bar(
            resource_df,
            x="resource_name",
            y="available_units",
            title="Available Resources"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

except:
    pass

conn.close()