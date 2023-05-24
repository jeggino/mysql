import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy 
from sklearn.neighbors import NearestNeighbors
import pyodbc
import pymysql


#creating connection
engine = sqlalchemy.create_engine(
    "mssql+pyodbc://username:passowrd@DB_server/database?driver=ODBC+Driver+17+for+SQL+Server", 
    )

@st.cache(allow_output_mutation=True)
def get_connection():
    return create_engine("mssql+pyodbc://username:passowrd@DB_server/database?driver=ODBC+Driver+17+for+SQL+Server", 
    fast_executemany = True
    )
  
q1 = 'SELECT * FROM df'

@st.cache
def read_df1():
  df1 = pd.read_sql_query(q1, get_connection())
  return df1

st.write(read_df1)
