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

sheet_data = [
            {'Timestamp': "d", 'User_Input': "d", 'User_Output': "ddd"}
]

conn.update(worksheet="df_observations", data=sheet_data)
