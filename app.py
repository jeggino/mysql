import mysql.connector
import streamlit as st

# Establish a connection to MySQL Server

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Platinum79",
    database="ebird"


)
mycursor=mydb.cursor()
print("Connection Established")

st.subheader("Read Records")
mycursor.execute("select * from df")
result = mycursor.fetchall()
for row in result:
    st.write(row)

