import streamlit as st
import sqlite3
import pandas as pd

st.title("👨‍⚕️ Doctor Management System")

conn = sqlite3.connect(
    "healthcare.db",
    check_same_thread=False
)

cursor = conn.cursor()

tab1, tab2, tab3 = st.tabs(
    [
        "Add Doctor",
        "View Doctors",
        "Search Doctor"
    ]
)

# ==========================
# ADD DOCTOR
# ==========================

with tab1:

    st.subheader("Register Doctor")

    name = st.text_input(
        "Doctor Name"
    )

    specialization = st.selectbox(
        "Specialization",
        [
            "Cardiology",
            "Neurology",
            "Orthopedics",
            "Oncology",
            "Pediatrics",
            "Dermatology",
            "General Medicine"
        ]
    )

    experience = st.number_input(
        "Experience (Years)",
        0,
        50
    )

    qualification = st.text_input(
        "Qualification"
    )

    slots = st.text_input(
        "Available Slots"
    )

    if st.button("Add Doctor"):

        cursor.execute("""
        INSERT INTO doctors(
        name,
        specialization,
        experience,
        qualification,
        available_slots
        )
        VALUES(?,?,?,?,?)
        """,
        (
            name,
            specialization,
            experience,
            qualification,
            slots
        ))

        conn.commit()

        st.success(
            "Doctor Added Successfully"
        )

# ==========================
# VIEW DOCTORS
# ==========================

with tab2:

    df = pd.read_sql_query(
        "SELECT * FROM doctors",
        conn
    )

    st.dataframe(
        df,
        use_container_width=True
    )

# ==========================
# SEARCH DOCTOR
# ==========================

with tab3:

    search = st.text_input(
        "Doctor Name"
    )

    if st.button("Search Doctor"):

        cursor.execute("""
        SELECT *
        FROM doctors
        WHERE name LIKE ?
        """,
        (
            f"%{search}%",
        ))

        data = cursor.fetchall()

        if data:

            df = pd.DataFrame(
                data,
                columns=[
                    "Doctor ID",
                    "Name",
                    "Specialization",
                    "Experience",
                    "Qualification",
                    "Available Slots"
                ]
            )

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.error(
                "Doctor Not Found"
            )