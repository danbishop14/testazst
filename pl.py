import pandas as pd
import streamlit as st

# @st.cache
# def get_az_xlsx() -> pd.DataFrame:
#     file = 'Redfin_Zip_Realtor_CA_2022-10.csv'
#     return(pd.read_csv(file))
# df = get_az_xlsx()

uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
#read csv
    df1=pd.read_csv(uploaded_file)
