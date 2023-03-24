import streamlit as st
import pandas as pd
import seaborn as sns


df = pd.read_csv('https://frenzy86.s3.eu-west-2.amazonaws.com/fav/company_sales_data.csv')
st.title('Grafico')
st.dataframe(df)

df(head)