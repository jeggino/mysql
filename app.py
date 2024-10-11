import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(
    worksheet="df_observations",
    ttl=0,
    usecols=[0, 1],
    nrows=3,
)

