import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r"C:\Users\Nathan\Downloads\bankloans.csv")
X = df.drop("default", axis=1)
y = df["default"].fillna(0)

print(X.columns)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
log_reg = LogisticRegression(random_state=0).fit(X_train_scaled, y_train)

print(log_reg.score(X_train_scaled, y_train))

fig, ax = plt.subplots()
ax.scatter(X_test['creddebt'].sort_values(), y_test, alpha=0.5)
ax.scatter(X_test['creddebt'].sort_values(), log_reg.predict(X_test_scaled), alpha=0.5)
st.header("Logistic Regression", divider="green")
st.pyplot(fig)

# fig1 = px.histogram(df, x="Income", y="Balance", color="Married")
# fig2 = px.pie(df, values="Income", names="Ethnicity", title="Total income split of each ethnicity")

# st.plotly_chart(fig1)
# st.plotly_chart(fig2)
