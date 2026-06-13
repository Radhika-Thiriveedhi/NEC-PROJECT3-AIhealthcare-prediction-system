import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

# =========================
# LOGIN CHECK
# =========================

if not st.session_state.get("logged_in"):
    st.error("Please Login First")
    st.stop()

role = st.session_state.get("role")
user_name = st.session_state.get("user_name")

# =========================
# DATABASE CONNECTION
# =========================

def get_connection():
    return sqlite3.connect(
        "healthcare.db",
        check_same_thread=False
    )

# =========================
# PAGE TITLE
# =========================

st.title("🩺 EHR Management Panel")

st.write("Current User:", user_name)
st.write("Current Role:", role)

# =========================
# DOCTOR / ADMIN
# =========================

if role in ["Doctor", "Admin"]:

    tab1, tab2 = st.tabs(
        ["Add Record", "View Records"]
    )

    # =====================
    # ADD RECORD
    # =====================

    with tab1:

        conn = get_connection()

        try:

            patients = pd.read_sql_query(
                """
                SELECT name
                FROM users
                WHERE role='Patient'
                """,
                conn
            )

        except:

            patients = pd.DataFrame()

        conn.close()

        if patients.empty:

            st.warning(
                "No registered patients found"
            )

        else:

            patient_name = st.selectbox(
                "Select Patient",
                patients["name"]
            )

            disease = st.selectbox(
                "Select Disease",
                [
                    "Diabetes",
                    "Heart Disease",
                    "Kidney Disease",
                    "Cancer"
                ]
            )

            if disease == "Diabetes":

                diagnosis = "Diabetes"

                treatment = "Insulin Therapy + Diet Control"

                prescription = "Metformin 500mg Twice Daily"

                vaccination = "Influenza Vaccine"

            elif disease == "Heart Disease":

                diagnosis = "Heart Disease"

                treatment = "Cardiac Rehabilitation"

                prescription = "Aspirin + Statins"

                vaccination = "Pneumococcal Vaccine"

            elif disease == "Kidney Disease":

                diagnosis = "Kidney Disease"

                treatment = "Dialysis Monitoring"

                prescription = "ACE Inhibitors"

                vaccination = "Hepatitis B Vaccine"

            else:

                diagnosis = "Cancer"

                treatment = "Chemotherapy"

                prescription = "Oncology Medication"

                vaccination = "HPV Vaccine"

            st.text_area(
                "Diagnosis",
                value=diagnosis,
                disabled=True
            )

            st.text_area(
                "Treatment",
                value=treatment,
                disabled=True
            )

            st.text_area(
                "Prescription",
                value=prescription,
                disabled=True
            )

            st.text_input(
                "Vaccination",
                value=vaccination,
                disabled=True
            )

            visit_date = st.date_input(
                "Visit Date",
                value=date.today()
            )

            if st.button("Save Record"):

                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute(
                    """
                    INSERT INTO ehr(
                        patient_name,
                        diagnosis,
                        treatment,
                        prescription,
                        vaccination,
                        doctor_name,
                        visit_date
                    )
                    VALUES(?,?,?,?,?,?,?)
                    """,
                    (
                        patient_name,
                        diagnosis,
                        treatment,
                        prescription,
                        vaccination,
                        user_name,
                        str(visit_date)
                    )
                )

                conn.commit()
                conn.close()

                st.success(
                    "EHR Record Saved Successfully"
                )

    # =====================
    # VIEW RECORDS
    # =====================

    with tab2:

        conn = get_connection()

        try:

            df = pd.read_sql_query(
                """
                SELECT *
                FROM ehr
                ORDER BY record_id DESC
                """,
                conn
            )

        except:

            df = pd.DataFrame()

        conn.close()

        if df.empty:

            st.info(
                "No EHR records found"
            )

        else:

            st.dataframe(
                df,
                use_container_width=True
            )

# =========================
# PATIENT VIEW
# =========================

elif role == "Patient":

    conn = get_connection()

    try:

        df = pd.read_sql_query(
            """
            SELECT *
            FROM ehr
            WHERE patient_name=?
            ORDER BY record_id DESC
            """,
            conn,
            params=(user_name,)
        )

    except:

        df = pd.DataFrame()

    conn.close()

    st.subheader(
        "My Medical Records"
    )

    if df.empty:

        st.info(
            "No Medical Records Found"
        )

    else:

        st.dataframe(
            df,
            use_container_width=True
        )

# =========================
# HOSPITAL STAFF
# =========================

elif role == "Hospital Staff":

    conn = get_connection()

    try:

        df = pd.read_sql_query(
            """
            SELECT *
            FROM ehr
            ORDER BY record_id DESC
            """,
            conn
        )

    except:

        df = pd.DataFrame()

    conn.close()

    if df.empty:

        st.info(
            "No EHR records found"
        )

    else:

        st.dataframe(
            df,
            use_container_width=True
        )

