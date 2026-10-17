import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. KONFIGURASI HALAMAN & DATA
# ==========================================
st.set_page_config(page_title="Dashboard Analisis Data", layout="wide")

# Judul Utama
st.title("🔬 Visualisasi Ilmiah & Statistik")
st.markdown("""
Dashboard ini mendemonstrasikan integrasi **Matplotlib (OO Style)** dan **Seaborn** ke
dalam aplikasi web interaktif menggunakan Streamlit.
""")

# Mengatur tema visual agar konsisten
sns.set_theme(style="whitegrid")

# Sidebar untuk Kontrol Global
st.sidebar.header("Parameter Global")
sampel_data = st.sidebar.slider("Jumlah Sampel Data", 50, 1000, 100)

# ==========================================
# 2. MATPLOTLIB: OBJECT ORIENTED STYLE
# ==========================================
st.header("A. Visualisasi Matematika (Matplotlib OO)")
st.caption("Mendemonstrasikan penggunaan `plt.subplots()` untuk kontrol penuh.")

# Layout Kolom
col1, col2 = st.columns([2, 1])

with col1:
    # Generate Data Dummy
    x = np.linspace(0, 10, sampel_data)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # Langkah 1: Buat Figure & Axes
    fig_mpl, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Langkah 2: Plotting pada Axes 1 (Line Chart)
    ax1.plot(x, y_sin, label="Sinus", color="#1f77b4", linewidth=2)
    ax1.plot(x, y_cos, label="Cosinus", color="#ff7f0e", linestyle="--")
    ax1.set_title("Gelombang Trigonometri")
    ax1.set_xlabel("Waktu (t)")
    ax1.set_ylabel("Amplitudo")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Langkah 3: Plotting pada Axes 2 (Scatter Plot)
    rng = np.random.RandomState(42)
    x_scatter = rng.rand(50)
    y_scatter = rng.rand(50)
    colors = rng.rand(50)
    area = (30 * rng.rand(50)) ** 2

    ax2.scatter(x_scatter, y_scatter, s=area, c=colors, alpha=0.5, cmap="viridis")
    ax2.set_title("Sebaran Data Acak")

    fig_mpl.tight_layout()

    # RENDER KE WEB
    st.pyplot(fig_mpl)
    plt.close(fig_mpl)

with col2:
    st.info("""
    **Konsep OO Style:**
    Berbeda dengan `plt.plot()` biasa, di sini kita mendefinisikan `fig` dan `ax` secara eksplisit.
    Ini memudahkan pengaturan layout multi-grafik (subplots).
    """)

# ==========================================
# 3. SEABORN: STATISTICAL EDA
# ==========================================
st.divider()
st.header("B. Analisis Statistik (Seaborn)")
st.caption("Visualisasi distribusi dan korelasi menggunakan dataset 'Tips'.")

# Load Dataset (butuh internet saat pertama kali)
df_tips = sns.load_dataset("tips")

# Checkbox untuk melihat data mentah
if st.checkbox("Tampilkan Dataset (Head)"):
    st.dataframe(df_tips.head())

row2_col1, row2_col2 = st.columns(2)

# --- Grafik 1: Distribusi (Histogram) ---
with row2_col1:
    st.subheader("1. Distribusi Tagihan")

    fig_sb1, ax_sb1 = plt.subplots(figsize=(6, 4))
    sns.histplot(data=df_tips, x="total_bill", kde=True, hue="time",
                 palette="magma", ax=ax_sb1)

    st.pyplot(fig_sb1)
    plt.close(fig_sb1)
    st.markdown("**Insight:** Membandingkan distribusi tagihan saat Lunch vs Dinner.")

# --- Grafik 2: Relasi Multivariat (Scatter) ---
with row2_col2:
    st.subheader("2. Hubungan Tagihan & Tip")

    # Interaksi: Filter Gender
    filter_gender = st.radio("Pilih Gender:", ["Male", "Female"], horizontal=True)

    # Filter Data
    subset_data = df_tips[df_tips["sex"] == filter_gender]

    fig_sb2, ax_sb2 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(
        data=subset_data,
        x="total_bill",
        y="tip",
        hue="smoker",
        style="day",
        s=100,
        ax=ax_sb2,
    )
    ax_sb2.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    fig_sb2.tight_layout()

    st.pyplot(fig_sb2)
    plt.close(fig_sb2)

# ==========================================
# 4. KORELASI (HEATMAP)
# ==========================================
st.subheader("3. Matriks Korelasi")

col_corr1, col_corr2 = st.columns([1, 2])

with col_corr1:
    st.markdown("""
    Heatmap digunakan untuk melihat seberapa kuat hubungan antar variabel numerik.
    * **1.0:** Korelasi positif kuat
    * **-1.0:** Korelasi negatif kuat
    """)

with col_corr2:
    fig_corr, ax_corr = plt.subplots(figsize=(8, 3))
    # Menghitung korelasi hanya untuk kolom numerik
    sns.heatmap(df_tips.corr(numeric_only=True), annot=True, cmap="coolwarm",
                fmt=".2f", ax=ax_corr)
    st.pyplot(fig_corr)
    plt.close(fig_corr)

# Footer
st.caption("Modul Praktikum Visualisasi Data | Informatika")
