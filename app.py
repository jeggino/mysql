import streamlit as st
import numpy as np
import pandas as pd
import sqlalchemy 
from sklearn.neighbors import NearestNeighbors
import pyodbc
import pymysql


#creating connection
engine = sqlalchemy.create_engine(
    "mssql+pyodbc://username:passowrd@DB_server/database?driver=ODBC+Driver+17+for+SQL+Server", 
    )

@st.cache(allow_output_mutation=True)
def get_connection():
    return sqlalchemy.create_engine("mssql+pyodbc://username:passowrd@DB_server/database?driver=ODBC+Driver+17+for+SQL+Server", 
    fast_executemany = True
    )
  
q1 = 'SELECT * FROM df'

df = pd.read_sql(q1, get_connection())


st.dataframe(df)
