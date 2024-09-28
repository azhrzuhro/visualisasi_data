import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

bike_day = pd.read_csv("new_bike_day.csv")

datetime_columns = ["dteday"]
bike_day.sort_values(by="dteday", inplace=True)
bike_day.reset_index(inplace=True)
 
for column in datetime_columns:
    bike_day[column] = pd.to_datetime(bike_day[column])

min_date = bike_day["dteday"].min()
max_date = bike_day["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )


main_df = bike_day[(bike_day["dteday"] >= str(start_date)) & 
                (bike_day["dteday"] <= str(end_date))]

st.header('Dicoding Collection Dashboard :sparkles:')

st.subheader("Rental Demographics")
 
workingday_with_cnt = bike_day.groupby('workingday')['cnt'].mean().reset_index().sort_values("cnt")

col1, col2 = st.columns(2)
 
with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
 
    sns.barplot(
        y="cnt", 
        x="workingday",
        data=workingday_with_cnt.sort_values(by="cnt", ascending=False),
        palette="Reds",
        ax=ax
    )
    ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Hari Kerja", loc="center", fontsize=50)
    ax.set_ylabel("Jumlah Sewa")
    ax.set_xlabel("Hari Kerja dan Tidak Kerja")
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2:

    holiday_with_cnt = bike_day.groupby('holiday')['cnt'].mean().reset_index().sort_values("cnt")
    fig, ax = plt.subplots(figsize=(20, 10))
 
    sns.barplot(
        y="cnt", 
        x="holiday",
        data=holiday_with_cnt.sort_values(by="cnt", ascending=False),
        palette="Greens",
        ax=ax
    )
    ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Hari Libur", loc="center", fontsize=50)
    ax.set_ylabel("Jumlah Sewa")
    ax.set_xlabel("Hari Libur dan Tidak Libur")
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)
 

 
fig, ax = plt.subplots(figsize=(20, 10))
weathersit_with_cnt =  bike_day.groupby('weathersit')['cnt'].mean().reset_index().sort_values("cnt")

sns.barplot(
    x="cnt", 
    y="weathersit",
    data=weathersit_with_cnt.sort_values(by="cnt", ascending=False),
    palette="Blues",
    ax=ax
)
ax.set_title("Jumlah Penyewaan Berdasarkan Cuaca", loc="center", fontsize=30)
ax.set_ylabel("Cuaca")
ax.set_xlabel("Jumlah Sewa")
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)