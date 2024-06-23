import pandas as pd
import streamlit as st
import numpy as np
import plotly as plt

df = pd.read_csv(r"Credit_Data.csv")
st.write(df)

