import streamlit as st

conn = st.experimental_connection("mydb", type="sql", autocommit=True)
df = conn.query("select * from df")
st.dataframe(df)
