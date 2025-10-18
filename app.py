# --- Streamlit App: Mutabaah Yaumiyah ---

import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

st.set_page_config(page_title="Mutabaah Yaumiyah", page_icon="🕌", layout="centered")

st.title("🕌 Mutabaah Yaumiyah Harian")

st.write("Pantau ibadah wajib dan sunnahmu setiap hari untuk meningkatkan kedekatan dengan Allah 🤍")

# --- Input Data Harian ---
st.subheader("🌅 Ibadah Wajib")
today = datetime.date.today()

data = {
    "Tanggal": [today],
    "Subuh": [st.time_input("Subuh", key="subuh")],
    "Dzuhur": [st.time_input("Dzuhur", key="dzuhur")],
    "Ashar": [st.time_input("Ashar", key="ashar")],
    "Maghrib": [st.time_input("Maghrib", key="maghrib")],
    "Isya": [st.time_input("Isya", key="isya")]
}

st.subheader("🌙 Ibadah Sunnah")
rawatib = st.checkbox("Shalat Rawatib")
duha = st.checkbox("Shalat Dhuha")
tahajud = st.checkbox("Shalat Tahajud")
puasa = st.multiselect("Puasa Sunnah", ["Senin", "Kamis", "Yaumul Bidh"])
quran = st.number_input("Baca Al-Qur'an (ayat)", 0)
murojaah = st.text_input("Murojaah (surat/ayat)")
ziyadah = st.text_input("Ziyadah (surat/ayat)")

# --- Simpan Data ---
if st.button("💾 Simpan Hari Ini"):
    df = pd.DataFrame(data)
    df["Rawatib"] = rawatib
    df["Duha"] = duha
    df["Tahajud"] = tahajud
    df["Puasa"] = ",".join(puasa)
    df["Quran"] = quran
    df["Murojaah"] = murojaah
    df["Ziyadah"] = ziyadah
    df.to_csv("mutabaah.csv", mode="a", header=False, index=False)
    st.success("Data berhasil disimpan! 🌸")

# --- Visualisasi Progress ---
st.subheader("📈 Progress Ibadah Harian")
try:
    df_all = pd.read_csv("mutabaah.csv", names=list(data.keys()) + ["Rawatib","Duha","Tahajud","Puasa","Quran","Murojaah","Ziyadah"])
    chart = px.line(df_all, x="Tanggal", y="Quran", title="Progress Bacaan Al-Qur'an", markers=True)
    st.plotly_chart(chart, use_container_width=True)
except FileNotFoundError:
    st.info("Belum ada data yang tersimpan. Mulai isi mutabaah hari ini!")
