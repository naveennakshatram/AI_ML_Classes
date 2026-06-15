# app/dashboard.py

import streamlit as st

def show_dashboard():
    st.title("Employee Dashboard")
    st.write("Welcome to the Employee Dashboard!")

    col1, col2, col3 = st.columns(3)

    col1.metric("Employees", 3)
    col2.metric("Departments", 3)
    col3.metric("Avg Salary", "₹55K")