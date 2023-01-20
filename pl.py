import pandas as pd
import streamlit as st
import polars as pl

#Full Data Caching
url = "https://redfin-public-data.s3.us-west-2.amazonaws.com/redfin_market_tracker/zip_code_market_tracker.tsv000.gz"
df = pd.read_csv(url)
df = df.head()
# @st.cache
# def get_data() -> pd.DataFrame:
#     return pd.read_csv(url, compression='gzip', sep='\t')
# df = get_data()

uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
#read csv
    df1=pd.read_csv(uploaded_file)


# st.dataframe(df.head())
