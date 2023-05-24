import streamlit as st

import streamlit as st
conn = st.experimental_connection("sql")
n = st.slider("Pick a number")
if st.button("Add the number!"):
    with conn.session as session:
        session.execute("select * from df")
        session.commit()
