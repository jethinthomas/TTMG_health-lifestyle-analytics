import pandas as pd
import streamlit as st
import plotly.figure_factory as ff
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

# print(df.head())
# st.set_page_config(layout="wide")

st.title("Analysis based on people's lifestyle and health dataset")
st.write("Source: https://www.numbeo.com")

# st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)
st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)

# file_name = "/home/jethin/Desktop/PYTHON_PRACTICE/bs4_code/health-lifestyle-analytics/health.csv"
file_name = "health.csv"

df = pd.read_csv(file_name,index_col=False)
print(df)
# st.title("Hello world!")
st.write(df)
rankings = 10
rankings = st.selectbox('Rankings to be disaplayed ?',(5,10,15,20,25,30),1)

bg_select = "quality_of_life"
bg_option = df.columns[2:]
# bg_option = ('quality_of_life','purchasing_power_index','safety_index','health_care_index','cost_of_living_index','property_price_to_income_ratio','traffic_commute_time_index','pollution_index','climate_index')
bg_select = st.selectbox('Rankings to be disaplayed ?',bg_option,0)

df = df.sort_values(by=[bg_select], ascending=False)
y_label = ' '.join(bg_select.split('_')).title()
val_count  = df[bg_select][:rankings]
fig = plt.figure(figsize=(10,5))
sns.barplot(df.loc[val_count.index,"country"], val_count.values)
plt.xticks(rotation=70)
plt.tight_layout()
plt.title(f"TOP {rankings} rankings According to {y_label}")
plt.xlabel('Country')
plt.ylabel(y_label)
st.pyplot(fig)

df = df.sort_values(by=[bg_select], ascending=True)
val_count  = df[bg_select][:rankings]
fig = plt.figure(figsize=(10,5))
sns.barplot(df.loc[val_count.index,"country"], val_count.values)
plt.xticks(rotation=70)
plt.tight_layout()
plt.title(f"BOTTOM {rankings} rankings According to {y_label}")
plt.xlabel('Country')
plt.ylabel(y_label)
st.pyplot(fig)

df = df.sort_values(by=[bg_select], ascending=False)
clist = df["country"].tolist()
countries = st.selectbox("Select country", clist, 0)
st.write(f"You selected: {countries}")
country_index = df.loc[df['country'] == countries].index[0]
st.line_chart(df.iloc[country_index, 2:])
