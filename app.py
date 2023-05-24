import streamlit as st
import numpy as np
import pandas as pd
import sqlalchemy 
import pyodbc
import pymysql



con  = sqlalchemy.create_engine("mssql+pyodbc://username:passowrd@DB_server/database?driver=ODBC+Driver+17+for+SQL+Server")
  
df = pd.read_sql( 'SELECT * FROM df', con=con)

st.dataframe(df)
