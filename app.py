import streamlit as st
import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:Platinum79@localhost/ebird")

query = "SELECT * FROM df"

df = pd.read_sql(query, engine)

df
