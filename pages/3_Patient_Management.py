import streamlit as st

# ====================================
# LOGIN CHECK
# ====================================

if not st.session_state.get("logged_in"):

    st.error("Please Login First")

    st.stop()

current_role = st.session_state.get("role")

# ====================================
# PAGE TITLE
# ====================================

st.title("👨‍⚕️ Patient Management")

st.info(
    f"Logged In Role: {current_role}"
)

# ====================================
# ACCESS CONTROL
# ====================================

if current_role not in [
    "Admin",
    "Doctor",
    "Hospital Staff"
]:

    st.error(
        "Patients cannot access Patient Management Module"
    )

    st.stop()

# ====================================
# PATIENT FORM
# ====================================

name = st.text_input("Patient Name")

age = st.number_input(
    "Age",
    1,
    120
)

gender = st.selectbox(
    "Gender",
    [
        "Male",
        "Female",
        "Other"
    ]
)

weight = st.number_input("Weight")

height = st.number_input("Height")

blood = st.selectbox(
    "Blood Group",
    [
        "A+","A-",
        "B+","B-",
        "AB+","AB-",
        "O+","O-"
    ]
)

medical = st.text_area(
    "Medical Conditions"
)

family = st.text_area(
    "Family History"
)

allergies = st.text_area(
    "Allergies"
)

insurance = st.text_area(
    "Insurance Details"
)

# ====================================
# ROLE RESTRICTIONS
# ====================================

if current_role in [
    "Admin",
    "Hospital Staff"
]:

    if st.button(
        "Register Patient"
    ):

        st.success(
            "Patient Registered Successfully"
        )

else:

    st.warning(
        "Doctors can only view patient information. They cannot register patients."
    )