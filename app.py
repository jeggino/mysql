import streamlit as st
import mysql.connector
import pandas as pd



config = {
    'user': 'root',
    'password': 'Platinum79',
    'host' : "localhost"
    'port': 3306,  
    'database':'ebird'
}


db = mysql.connector.connect(**config)
"""Fetch all records from the 'patients' table."""
cursor = db.cursor()

# Select the database
cursor.execute("USE ebird")

# Fetch all patients
select_patients_query = "SELECT * FROM df"
cursor.execute(select_patients_query)
patients = cursor.fetchall()

st.dataframe(patients)
