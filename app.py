import streamlit as st

conn = st.experimental_connection(
    "ebird",
    type="sql",
    url="mysql://user:pass@localhost:3306/mydb"
)
df = conn.query("select * from df")
st.dataframe(df)
