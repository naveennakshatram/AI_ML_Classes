import streamlit as st

def login():
    st.title("HR Portal Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        if username == "Naveen" and password == "kumar":
            st.session_state.logged_in = True
            st.session_state.user = username
            st.rerun()
        else:
            st.error("Invalid credentials")


def logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.rerun()