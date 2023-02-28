import pandas as pd
import streamlit as st

st.title("This is the excel file data")
excel_file='Survey_Results.xlsx'
sheet_name='DATA'

df=pd.read_excel(excel_file, sheet_name=sheet_name,usecols='B:D',header=3)

df_participants=pd.read_excel(excel_file,sheet_name=sheet_name, usecols='F:G',header=3)

st.dataframe(df)
st.dataframe(df_participants)