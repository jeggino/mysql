import streamlit as st
import SQLAlchemy
import mysqlclient

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from df;')
st.dataframe(df)

