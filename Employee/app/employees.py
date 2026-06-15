# app/employees.py

import streamlit as st
from db import load_data

def show_employees():
    st.title("Employee Dashboard")
    st.write("Welcome to the Employee Dashboard!")

    st.subheader("Employee Data")
    st.dataframe(load_data())
