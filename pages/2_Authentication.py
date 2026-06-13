import streamlit as st
import sqlite3
import bcrypt
# Session Initialization

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if "user_name" not in st.session_state:
    st.session_state.user_name = None

st.title("🔐 Authentication System")

conn = sqlite3.connect(
    "healthcare.db",
    check_same_thread=False
)

cursor = conn.cursor()

tab1, tab2 = st.tabs(
    ["Login", "Register"]
)

# ======================
# REGISTER
# ======================

with tab2:

    st.subheader("Register User")

    name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    role = st.selectbox(
        "Role",
        [
            "Patient",
            "Doctor",
            "Admin",
            "Hospital Staff"
        ]
    )

    if st.button("Register"):

        hashed = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        try:

            cursor.execute(
                """
                INSERT INTO users
                (name,email,password,role)
                VALUES(?,?,?,?)
                """,
                (
                    name,
                    email,
                    hashed,
                    role
                )
            )

            conn.commit()

            st.success(
                "Registration Successful"
            )

        except:
            st.error(
                "Email Already Exists"
            )

# ======================
# LOGIN
# ======================

with tab1:

    st.subheader("User Login")

    email = st.text_input(
        "Email",
        key="login_email"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_pass"
    )

    if st.button("Login"):

        cursor.execute(
    """
    SELECT name,password,role
    FROM users
    WHERE email=?
    """,
    (email,)
)

        user = cursor.fetchone()

        if user:

            user_name = user[0]
            stored_password = user[1]
            stored_role = user[2]

            if bcrypt.checkpw(
                password.encode(),
                stored_password
):

              st.session_state.logged_in = True
              st.session_state.role = stored_role
              st.session_state.user_name = user_name

              st.success(
                 f"Welcome {user_name} ({stored_role})"
    )

            else:
                st.error(
                    "Invalid Password"
                )

        else:
            st.error(
                "User Not Found"
            )
            # =========================
# LOGGED IN USER
# =========================

if st.session_state.logged_in:

    st.sidebar.success(
        f"👤 {st.session_state.user_name}"
    )

    st.sidebar.info(
        f"Role: {st.session_state.role}"
    )

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.user_name = None

        st.rerun()