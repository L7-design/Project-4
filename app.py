import streamlit as st 
import pandas as pd


st.header('Title')

#Load dataset
data = pd.read_csv('vehicles_us.csv')