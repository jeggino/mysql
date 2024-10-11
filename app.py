import streamlit as st
import mysql.connector
import pandas as pd
import requests
from streamlit_lottie import st_lottie


config = {
    'user': 'root',
    'password': 'Platinum79',
    'host': 'localhost',
    'port': 3306,  
    'database':'ebird'
}

db = mysql.connector.connect(**config)
"""Fetch all records from the 'patients' table."""
cursor = db.cursor()

# Select the database
cursor.execute("USE userdb")

# Fetch all patients
select_patients_query = "SELECT * FROM patients"
cursor.execute(select_patients_query)
patients = cursor.fetchall()

st.dataframe(patients)
