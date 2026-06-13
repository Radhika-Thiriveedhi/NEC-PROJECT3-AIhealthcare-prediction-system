import streamlit as st
import sqlite3
import pandas as pd

if not st.session_state.get("logged_in"):

    st.error("Please Login First")

    st.stop()

if st.session_state.get("role") != "Admin":

    st.error(
        "Only Admin Can Access Doctor Management"
    )

    st.stop()


st.title("👨‍⚕️ Doctor Management System")

conn = sqlite3.connect(
    "healthcare.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Create table if missing
cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors(
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    specialization TEXT,
    experience INTEGER,
    qualification TEXT,
    available_slots TEXT
)
""")

conn.commit()

tab1, tab2, tab3 = st.tabs(
    [
        "Add Doctor",
        "View Doctors",
        "Search Doctor"
    ]
)

# ====================================
# ADD DOCTOR
# ====================================

with tab1:

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
        "Experience",
        min_value=0,
        max_value=50
    )

    qualification = st.text_input(
        "Qualification"
    )

    slots = st.text_input(
        "Available Slots"
    )

    if st.button("Add Doctor"):

        cursor.execute(
            """
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
            )
        )

        conn.commit()

        st.success(
            "Doctor Added Successfully"
        )

# ====================================
# VIEW DOCTORS
# ====================================

with tab2:

    df = pd.read_sql_query(
        "SELECT * FROM doctors",
        conn
    )

    st.dataframe(
        df,
        use_container_width=True
    )

# ====================================
# SEARCH DOCTOR
# ====================================

with tab3:

    search_name = st.text_input(
        "Doctor Name To Search"
    )

    if st.button("Search Doctor"):

        result = pd.read_sql_query(
            f"""
            SELECT *
            FROM doctors
            WHERE name LIKE '%{search_name}%'
            """,
            conn
        )

        if len(result) > 0:

            st.dataframe(
                result,
                use_container_width=True
            )

        else:

            st.error(
                "Doctor Not Found"
            )