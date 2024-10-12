# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# url = "https://docs.google.com/spreadsheets/d/1mkF1s_hsoX7GfCdbb_RtaxssqYfLO-kpsJncbqc5Wpw/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=st.secrets["spreadsheet"],ttl=0)
data[data['project']=='Badhoevedorp']
