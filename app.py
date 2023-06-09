import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import pymysql

SQL_script = st.text_area(label='SQL Input', value='SELECT * FROM df;')

@st.cache(allow_output_mutation=True)
def get_connection():
    return create_engine("mysql+pymysql://root:Platinum79@localhost/ebird")

@st.cache
def load_data(SQL_script):
    df = pd.read_sql_query(SQL_script, get_connection())
    return df

raw_data = load_data(SQL_script)
raw_data

