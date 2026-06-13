import streamlit as st
import sqlite3
import pandas as pd

st.title("🔔 Notifications Debug")

conn = sqlite3.connect("healthcare.db")

df = pd.read_sql_query(
    "SELECT * FROM notifications",
    conn
)

conn.close()

st.write("Total Notifications:", len(df))
st.dataframe(df)