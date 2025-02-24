import streamlit as st
import pandas as pd

st.title("💰 Expense Tracker Dashboard")

df = pd.read_csv("data/transactions.csv")
st.write(df)

category_expense = df.groupby("Category")["Amount"].sum()
st.bar_chart(category_expense)
