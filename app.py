import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import joblib
from utils.preprocess import clean_text

# -------------------------------
# Load Model
# -------------------------------
model = joblib.load("model/sentiment_model.pkl")
tfidf = joblib.load("model/tfidf_vectorizer.pkl")

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(
    page_title="Sentiment Analysis Gojek/Grab",
    layout="wide"
)

st.title("📊 Sentiment Analysis Dashboard – Gojek & Grab")
st.write("Dashboard interaktif berbasis Streamlit untuk analisis sentimen media sosial.")

# -------------------------------
# Sidebar Menu
# -------------------------------
menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Prediksi Kalimat", "Analisis CSV", "Wordcloud", "Tren Waktu"]
)

# -----------------------------------------------------
# 1. Prediksi Kalimat
# -----------------------------------------------------
if menu == "Prediksi Kalimat":
    st.header("🔍 Prediksi Sentimen Real-Time")

    text = st.text_area("Masukkan kalimat", height=150)

    if st.button("Prediksi"):
        if text.strip() == "":
            st.warning("Masukkan teks terlebih dahulu!")
        else:
            clean = clean_text(text)
            vec = tfidf.transform([clean])
            pred = model.predict(vec)[0]

            st.success(f"Prediksi Sentimen: **{pred.upper()}**")

# -----------------------------------------------------
# 2. Analisis CSV
# -----------------------------------------------------
elif menu == "Analisis CSV":
    st.header("📁 Analisis Sentimen dari File CSV")

    uploaded = st.file_uploader("Upload file CSV (kolom: tweet, tanggal)", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
        
        # Pastikan kolom wajib
        if "tweet" not in df.columns:
            st.error("CSV wajib memiliki kolom 'tweet'")
        else:
            # Preprocessing
            df["clean_tweet"] = df["tweet"].apply(clean_text)
            X = tfidf.transform(df["clean_tweet"]).toarray()

            df["sentimen"] = model.predict(X)

            st.dataframe(df)

            # Chart
            st.subheader("Distribusi Sentimen")
            fig, ax = plt.subplots()
            df["sentimen"].value_counts().plot(kind='bar', ax=ax)
            st.pyplot(fig)

            # Download hasil
            csv_out = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Hasil CSV", csv_out, "hasil_sentimen.csv")

# -----------------------------------------------------
# 3. Wordcloud
# -----------------------------------------------------
elif menu == "Wordcloud":
    st.header("☁️ Wordcloud Sentimen")

    uploaded = st.file_uploader("Upload file CSV (kolom: tweet)", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)

        df["clean_tweet"] = df["tweet"].apply(clean_text)
        text = " ".join(df["clean_tweet"])

        wc = WordCloud(width=800, height=400, background_color="white").generate(text)

        fig, ax = plt.subplots(figsize=(15, 7))
        ax.imshow(wc, interpolation='bilinear')
        ax.axis("off")

        st.pyplot(fig)

# -----------------------------------------------------
# 4. Tren Waktu Mingguan
# -----------------------------------------------------
elif menu == "Tren Waktu":
    st.header("📈 Analisis Tren Waktu")

    uploaded = st.file_uploader("Upload file CSV (wajib ada kolom tanggal & tweet)", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)

        if "tanggal" not in df.columns:
            st.error("CSV wajib memiliki kolom 'tanggal'")
        else:
            df["tanggal"] = pd.to_datetime(df["tanggal"], errors="coerce")
            df["clean_tweet"] = df["tweet"].apply(clean_text)

            X = tfidf.transform(df["clean_tweet"])
            df["sentimen"] = model.predict(X)

            df["minggu"] = df["tanggal"].dt.isocalendar().week

            trend = df.groupby(["minggu", "sentimen"]).size().unstack(fill_value=0)

            st.subheader("Tren Sentimen Mingguan")
            st.line_chart(trend)
