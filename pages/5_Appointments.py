import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

# =========================
# LOGIN CHECK
# =========================

if not st.session_state.get("logged_in"):
    st.error("Please login first")
    st.stop()

role = st.session_state.get("role")
user_name = st.session_state.get("user_name")

# =========================
# DB CONNECTION
# =========================

def get_connection():
    return sqlite3.connect(
        "healthcare.db",
        timeout=10,
        check_same_thread=False
    )

st.title("📅 Appointment Management")
st.info(f"Logged in as: {user_name} ({role})")

# =========================
# PATIENT
# =========================

if role == "Patient":

    st.subheader("Book Appointment")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM users
        WHERE role='Doctor'
    """)

    doctors = [row[0] for row in cursor.fetchall()]
    conn.close()

    if not doctors:

        st.warning("No doctors available")

    else:

        doctor_name = st.selectbox(
            "Select Doctor",
            doctors
        )

        appointment_date = st.date_input(
            "Appointment Date",
            value=date.today()
        )

        appointment_time = st.time_input(
            "Appointment Time"
        )

        if st.button("Book Appointment"):

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO appointments(
                    patient_name,
                    doctor_name,
                    appointment_date,
                    appointment_time,
                    status
                )
                VALUES(?,?,?,?,?)
            """, (
                user_name,
                doctor_name,
                str(appointment_date),
                str(appointment_time),
                "Pending"
            ))

            cursor.execute("""
                INSERT INTO notifications(
                    user_name,
                    message
                )
                VALUES(?,?)
            """, (
                doctor_name,
                f"New appointment request from {user_name}"
            ))

            conn.commit()
            conn.close()

            st.success(
                "Appointment Booked Successfully"
            )

            st.rerun()

    st.subheader("My Appointments")

    conn = get_connection()

    df = pd.read_sql_query("""
        SELECT *
        FROM appointments
        WHERE patient_name=?
        ORDER BY appointment_id DESC
    """, conn, params=(user_name,))

    conn.close()

    st.dataframe(
        df,
        use_container_width=True
    )

# =========================
# DOCTOR / ADMIN
# =========================

elif role in ["Doctor", "Admin"]:

    st.subheader("All Appointments")

    conn = get_connection()

    df = pd.read_sql_query("""
        SELECT *
        FROM appointments
        ORDER BY appointment_id DESC
    """, conn)

    conn.close()

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader(
        "Approve / Reject Appointments"
    )

    conn = get_connection()

    pending = pd.read_sql_query("""
        SELECT *
        FROM appointments
        WHERE status='Pending'
        ORDER BY appointment_id DESC
    """, conn)

    conn.close()

    if pending.empty:

        st.info(
            "No Pending Appointments"
        )

    else:

        for _, row in pending.iterrows():

            appointment_id = int(
                row["appointment_id"]
            )

            st.write("---")

            st.write(
                f"Patient: {row['patient_name']}"
            )

            st.write(
                f"Doctor: {row['doctor_name']}"
            )

            st.write(
                f"Date: {row['appointment_date']}"
            )

            st.write(
                f"Time: {row['appointment_time']}"
            )

            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "Approve",
                    key=f"approve_{appointment_id}"
                ):

                    conn = get_connection()
                    cursor = conn.cursor()

                    cursor.execute("""
                        UPDATE appointments
                        SET status='Approved'
                        WHERE appointment_id=?
                    """, (appointment_id,))

                    cursor.execute("""
                        INSERT INTO notifications(
                            user_name,
                            message
                        )
                        VALUES(?,?)
                    """, (
                        row["patient_name"],
                        f"Your appointment with Dr. {row['doctor_name']} has been approved."
                    ))

                    conn.commit()
                    conn.close()

                    st.success(
                        "Appointment Approved"
                    )

                    st.rerun()

            with col2:

                if st.button(
                    "Reject",
                    key=f"reject_{appointment_id}"
                ):

                    conn = get_connection()
                    cursor = conn.cursor()

                    cursor.execute("""
                        UPDATE appointments
                        SET status='Rejected'
                        WHERE appointment_id=?
                    """, (appointment_id,))

                    cursor.execute("""
                        INSERT INTO notifications(
                            user_name,
                            message
                        )
                        VALUES(?,?)
                    """, (
                        row["patient_name"],
                        f"Your appointment with Dr. {row['doctor_name']} has been rejected."
                    ))

                    conn.commit()
                    conn.close()

                    st.warning(
                        "Appointment Rejected"
                    )

                    st.rerun()

