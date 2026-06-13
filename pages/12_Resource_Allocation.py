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
# DATABASE CONNECTION
# =========================

def get_connection():
    return sqlite3.connect(
        "healthcare.db",
        check_same_thread=False
    )

st.title("🏥 Resource Allocation")

st.info(
    f"Logged in as: {user_name} ({role})"
)

# =========================
# ADMIN / STAFF
# =========================

if role in ["Admin", "Hospital Staff"]:

    tab1, tab2 = st.tabs(
        ["Add Resource", "Manage Resources"]
    )

    # =====================
    # ADD RESOURCE
    # =====================

    with tab1:

        resource_name = st.text_input(
            "Resource Name"
        )

        total_units = st.number_input(
            "Total Units",
            min_value=0
        )

        available_units = st.number_input(
            "Available Units",
            min_value=0
        )

        if st.button("Add Resource"):

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO resources(
                    resource_name,
                    total_units,
                    available_units
                )
                VALUES(?,?,?)
                """,
                (
                    resource_name,
                    total_units,
                    available_units
                )
            )

            conn.commit()
            conn.close()

            st.success(
                "Resource Added Successfully"
            )

    # =====================
    # VIEW / UPDATE
    # =====================

    with tab2:

        conn = get_connection()

        df = pd.read_sql_query(
            """
            SELECT *
            FROM resources
            ORDER BY resource_id DESC
            """,
            conn
        )

        conn.close()

        if df.empty:

            st.info(
                "No Resources Found"
            )

        else:

            st.dataframe(
                df,
                use_container_width=True
            )

            st.subheader(
                "Update Resource Stock"
            )

            resource_id = st.selectbox(
                "Select Resource ID",
                df["resource_id"]
            )

            new_available = st.number_input(
                "New Available Units",
                min_value=0
            )

            if st.button("Update Stock"):

                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute(
                    """
                    UPDATE resources
                    SET available_units=?
                    WHERE resource_id=?
                    """,
                    (
                        new_available,
                        int(resource_id)
                    )
                )

                conn.commit()
                conn.close()

                st.success(
                    "Stock Updated Successfully"
                )

# =========================
# DOCTOR / PATIENT VIEW
# =========================

else:

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT *
        FROM resources
        ORDER BY resource_id DESC
        """,
        conn
    )

    conn.close()

    if df.empty:

        st.info(
            "No Resources Available"
        )

    else:

        st.dataframe(
            df,
            use_container_width=True
        )