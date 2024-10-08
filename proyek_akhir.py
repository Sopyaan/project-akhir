# -*- coding: utf-8 -*-
"""Proyek_Akhir.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y0kFeOGw45SKHYPrtXxx3Izz2_-tcTkZ

# Proyek Analisis Data: Bike Sharing Analysis
- Nama:Sopyan
- Email:sopyanwae60@gmail.com
- Id Dicoding:sopyan_wae

## Menentukan Pertanyaan Bisnis

- pertanyaan 1 : Bagaimana variasi ketersediaan sepeda berdasarkan kondisi cuaca (weathersit) pada hari-hari tertentu? Apakah cuaca yang baik memengaruhi peningkatan penyewaan?
- Pertanyaan 2 : Bagaimana tren jumlah penyewaan sepeda per bulan dari Januari 2011 hingga Desember 2012?
- pertanyaan 3 : Bagaimana hubungan antara suhu (temp) dan jumlah penyewaan sepeda harian? Apakah terdapat tren atau pola tertentu?
- pertanyaan 4 : Apakah ada perbedaan antara distribusi penyewaan sepeda antara weekend dan weekdays?
- pertanyaan 5 : Bagaimana kontribusi pengguna casual dan registered terhadap total penyewaan sepeda?
- Pertanyaan 6 : Bagaimana performa atau tren peminjaman dalam periode satu tahun terakhir?

## Menyiapkan semua library yang dibuthkan
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Uploading the dataset
all_df = pd.read_csv("all_data.csv")

# Convert 'dteday' to datetime type
all_df['dteday'] = pd.to_datetime(all_df['dteday'])

# Question 1: Variation in bike availability based on weather conditions
plt.figure(figsize=(10, 5))
sns.barplot(
    y="cnt",
    x="weathersit",
    data=all_df,
    hue="weathersit",  # `hue` assigned to categorize based on 'weathersit'
    palette="viridis"
)
plt.title("Variasi Ketersediaan Sepeda Berdasarkan Kondisi Cuaca", fontsize=15)
plt.ylabel("Jumlah Penyewaan")
plt.xlabel("Kondisi Cuaca")
plt.tick_params(axis='x', labelsize=12)
st.pyplot(plt)  # Use st.pyplot() for Streamlit

# Question 2: Monthly rental trends from January 2011 to December 2012
bulanan = all_df.groupby(pd.Grouper(key='dteday', freq='ME')).sum()
plt.figure(figsize=(10, 3))
plt.plot(bulanan.index, bulanan['cnt'], marker='o', linestyle='-')
plt.title('Total Peminjaman Sepeda Bulanan (Tahun 2011 - Tahun 2012)')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewaan')
plt.grid(True)
st.pyplot(plt)  # Streamlit plotting

# Question 3: Relationship between temperature and bike rentals
plt.figure(figsize=(10, 5))
sns.scatterplot(
    y="cnt",
    x="temp",
    data=all_df
)
plt.title("Hubungan Antara Suhu dan Jumlah Penyewaan Sepeda Harian", fontsize=15)
plt.ylabel("Jumlah Penyewaan")
plt.xlabel("Suhu")
plt.tick_params(axis='x', labelsize=12)
st.pyplot(plt)  # Streamlit plotting

# Question 4: Bike rental distribution between weekends and weekdays
plt.figure(figsize=(10, 5))
sns.barplot(
    x="holiday",
    y="cnt",
    data=all_df,
    hue="holiday",  # `hue` for weekend vs weekday comparison
    dodge=True,
    palette="viridis"
)
plt.title("Distribusi Penyewaan Sepeda pada Weekend dan Weekdays", fontsize=15)
plt.ylabel("Jumlah Penyewaan")
plt.xlabel("Weekend (1: Ya, 0: Tidak)")
plt.legend(title="Status Hari Libur")
st.pyplot(plt)

# Question 5: Casual and registered user contributions
plt.figure(figsize=(10, 5))
sns.barplot(
    data=all_df,
    x='weekday',
    y='cnt',
    hue='yr',
    palette='viridis'
)
plt.title('Kontribusi Pengguna Casual dan Registered Terhadap Total Penyewaan per Tahun')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

# Question 6: Performance in the last year
data = all_df[all_df['yr'] == 1]
bulan = data.groupby(pd.Grouper(key='dteday', freq='ME')).sum()
plt.figure(figsize=(11, 4))
plt.plot(bulan.index, bulan['cnt'], marker='o', linestyle='-')
plt.xticks(bulan.index, bulan.index.strftime('%b'))
plt.title('Performa Peminjaman Sepeda Setahun Terakhir')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewaan')
plt.grid(True)
st.pyplot(plt)


"""## Conclusion

**Conclution pertanyaan 1**: Berdasarkan barplot kondisi cuaca terhadap jumlah penyewaan dapat saya simpulkan menjadi:
- weathersit 1 : pada kondisi ini cuaca baik yang berpengaruh pada tingginya penyewaan sepeda.
-weathersit 2 dan 3 : pada kondisi ini cuaca lebih buruk sehingga terjadi penurunan penyewaan sepeda

**Conclution pertanyaan 2**: Grafik tersebut menunjukkan tren peminjaman sepeda bulanan dari Januari 2011 hingga Januari 2013. Jumlah peminjaman meningkat pesat pada awal 2011, mencapai puncak tertinggi di pertengahan tahun, sekitar Juli 2011. Setelah itu, peminjaman cenderung stabil hingga akhir 2011, sebelum menurun tajam di awal 2012. Namun, pada pertengahan 2012, jumlahnya kembali naik dan mencapai puncak baru, tetapi kemudian menurun lagi menjelang akhir tahun 2012 hingga Januari 2013. Ini menunjukkan adanya pola musiman, dengan peningkatan peminjaman di pertengahan tahun dan penurunan di awal tahun.


**Conclution pertanyaan 3**: berdasarkan visualisasi berdasarkan scatterplot dapat disimpulkan bahwa semakin tinggi cuaca maka semakin tinggi pula jumlah penyewaan sepeda. Hal ini sejalan dengan conlusin pertanyaan 1.

**Conclution pertanyaan 4**: berdasrakan barplot menunujukan hasil bahwa tingkat penyewaan pada *weekdays* lebih tinggi dari pada *weekend*. Hal ini terjadi karena pada saat cuaca yang baik kecenderungan dari orang-orang untuk keluar rumah untuk menikmati keindahan alam.

**Conclution pertanyaan 5**: berdasarkan barplot dapat ditarik kesimpulan bahwa:
- pada tahun 2011 dan 2012 terlihat pengguna casual dan registered terhadap penyewaan sepeda cukup seragam.
- pengguna registered memberikan kontribusi lebih tinggi dibandingkan casual dalam penyewaan sepeda.
- karena tingginya pengguna registered dalam penyewaan sepeda, maka bisnis bisa meningkatkan jumlah pengguna registerednya untuk meningkatkan volume penyewaan ini.

**Conclution pertanyaan 6**: Grafik tersebut menunjukkan tren peminjaman sepeda selama setahun terakhir. Peminjaman sepeda meningkat secara bertahap dari Januari hingga mencapai puncaknya pada bulan Mei. Setelah itu, peminjaman tetap tinggi dan stabil hingga Agustus, sebelum mulai menurun secara bertahap dari September hingga Desember, dengan penurunan paling tajam terjadi di bulan terakhir. Ini menunjukkan bahwa peminjaman sepeda cenderung tinggi di pertengahan tahun dan menurun menjelang akhir tahun.
"""
