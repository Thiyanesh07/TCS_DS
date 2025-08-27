import pandas as pd
import streamlit as st

df = pd.read_csv("Retail_Transactions_2000.csv")

st.title("📊 Sales Dashboard")

st.metric("Total Revenue", f"{df['TotalAmount'].sum():,.0f}")
st.metric("Total Transactions", len(df))

st.bar_chart(df.groupby("ProductCategory")["TotalAmount"].sum())
st.line_chart(df.groupby("PurchaseDate")["TotalAmount"].sum())
