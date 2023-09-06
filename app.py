import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import pymysql

SQL_script = st.text_area(label='SQL Input', value='SELECT * FROM df;')

import streamlit as st

conn = st.experimental_connection("sql")
df = conn.query("select * from df")
st.dataframe(df)

