import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    print("loading csv data...")
    df = pd.read_csv("app/datasets/employee.csv")  # runs every time
    return df