import streamlit as st
from auth import login
from auth import logout
from dashboard import show_dashboard
from employees import show_employees
from salary import show_salary

# init session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# login page
if not st.session_state.logged_in:
    login()

st.sidebar.title(f"Welcome, {st.session_state.user}!")
page = st.sidebar.radio("Go to", ["Dashboard", "Employees", "Salary"])

if st.sidebar.button("Logout",logout):
    logout()

# ---------------- ROUTING ----------------
if page == "Dashboard":
    show_dashboard()

elif page == "Employees":
    show_employees()

elif page == "Salary":
    show_salary()
    