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

st.title("🚨 Emergency Alerts")

st.info(
    f"Logged in as: {user_name} ({role})"
)

# =========================
# ADMIN / STAFF CREATE ALERT
# =========================

if role in ["Admin", "Hospital Staff"]:

    st.subheader("Create Emergency Alert")

    alert_type = st.selectbox(
        "Alert Type",
        [
            "ICU Full",
            "Emergency Ward Full",
            "Oxygen Shortage",
            "Fire Emergency",
            "System Failure"
        ]
    )

    message = st.text_area(
        "Alert Message"
    )

    if st.button("Send Alert"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO emergency_alerts(
            alert_type,
            message,
            created_by
        )
        VALUES(?,?,?)
        """,
        (
            alert_type,
            message,
            user_name
        ))

        conn.commit()
        conn.close()

        st.success(
            "Emergency Alert Sent Successfully"
        )

# =========================
# VIEW ALERTS
# =========================

st.subheader("Active Alerts")

conn = get_connection()

df = pd.read_sql_query("""
SELECT *
FROM emergency_alerts
ORDER BY alert_id DESC
""", conn)

conn.close()

if df.empty:

    st.info(
        "No Emergency Alerts Available"
    )

else:

    st.dataframe(
        df,
        use_container_width=True
    )