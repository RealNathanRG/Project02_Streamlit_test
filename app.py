import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("Credit_Data.csv")
fig1 = px.histogram(df, x="Income", y="Balance", color="Married")
fig2 = px.pie(df, values="Income", names="Ethnicity", title="Total income split of each ethnicity")
st.header("Income vs Balance for for married and non-married", divider="green")
st.plotly_chart(fig1)
st.plotly_chart(fig2)
