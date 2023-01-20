import pandas as pd
import streamlit as st

@st.cache
def get_az_xlsx() -> pd.DataFrame:
    file = r'C:\Users\Dan\Desktop\Coding\Datasets\Redfin_Data\Redfin_Zip_Realtor_CA_2022-10.csv'
    return(pd.read_csv(file))
df = get_az_xlsx()

st.dataframe(df)
