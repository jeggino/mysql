import streamlit as st
import numpy as np
import pandas as pd
import sqlalchemy 
import pyodbc
import pymysql



# con  = sqlalchemy.create_engine("mssql+pyodbc://username:passowrd@DB_server/database?driver=ODBC+Driver+17+for+SQL+Server")
engine = sqlalchemy.create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="Platinum79",
                               db="ebird"))
  
df = pd.read_sql( 'SELECT * FROM df', con=engine)

st.dataframe(df)
