import sqlalchemy.create_engine
import streamlit as st

# Establish a connection to MySQL Server

mydb =create_engine(
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

