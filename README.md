## Deskripsi

Project ini adalah aplikasi analisis sentimen terhadap opini pengguna mengenai layanan Gojek dan Grab. Aplikasi ini dibangun menggunakan Streamlit dan model Machine Learning (Naive Bayes) yang telah dilatih melalui preprocessing Bahasa Indonesia serta TF-IDF vectorization.

Aplikasi ini menyediakan fitur prediksi sentimen real-time, analisis CSV, visualisasi wordcloud, grafik tren waktu mingguan, serta dukungan mode tampilan Light dan Dark. Model tidak disimpan di repository untuk alasan keamanan, namun aplikasi telah disiapkan agar dapat memuat model secara otomatis ketika dijalankan.

---

# Cara Menjalankan Aplikasi Streamlit

## 1. Ekstrak Proyek

Pastikan folder proyek memiliki struktur berikut:

```
sentiment-analysis-streamlit/
│── app.py
│── flask_api.py
│── utils/
│     └── preprocess.py
│── assets/
│     └── logo.png
│── model/
│── requirements.txt
│── README.md
```

Folder model dibiarkan kosong karena file model akan diunduh atau dimuat secara otomatis.

---

# 2. Instal Dependensi

Buka terminal pada folder proyek, lalu jalankan:

Windows:

```
pip install -r requirements.txt
```

MacOS atau Linux:

```
pip3 install -r requirements.txt
```

---

# 3. Menjalankan Aplikasi Streamlit

Jalankan perintah berikut:

```
streamlit run app.py
```

Setelah perintah dijalankan, Streamlit akan menampilkan alamat lokal seperti berikut:

```
Local URL: http://localhost:8501
```

Buka alamat tersebut di browser untuk mengakses aplikasi.

---

# Fitur Utama Aplikasi

## Prediksi Sentimen Real-Time

Pengguna dapat memasukkan kalimat dan aplikasi akan menampilkan prediksi sentimen beserta probability score.

## Analisis CSV

Aplikasi dapat menerima file CSV dengan minimal kolom tweet. Jika kolom tanggal tersedia, aplikasi juga menampilkan grafik tren mingguan. Hasil analisis dapat diunduh dalam bentuk CSV baru.

## Wordcloud

Menampilkan visualisasi kata paling sering muncul berdasarkan tweet yang telah diproses.

## Tren Waktu Mingguan

Jika data memiliki kolom tanggal, aplikasi akan menampilkan grafik tren jumlah sentimen per minggu.

## Light Mode dan Dark Mode

Aplikasi menyediakan pilihan tampilan Light dan Dark yang dapat diganti melalui sidebar.

## Sidebar Logo

Terdapat logo aplikasi pada bagian sidebar jika file logo tersedia dalam folder assets.

## Dukungan Model Lokal dan API

Aplikasi dapat memuat model secara lokal atau menggunakan endpoint API Flask yang tersedia dalam project.

---

# Menjalankan API Flask (Opsional)

API ini tidak wajib dijalankan untuk menggunakan Streamlit, namun disediakan apabila diperlukan.

Jalankan:

```
python flask_api.py
```

Endpoint tersedia:

```
POST /predict
```

Contoh request JSON:

```
{"text": "driver gojeknya ramah"}
```

---

# Persyaratan CSV

File CSV untuk analisis harus memiliki minimal kolom berikut:

1. tweet
2. tanggal (opsional, digunakan untuk grafik tren mingguan)

Format tanggal harus dapat diparsing oleh pandas, misalnya yyyy-mm-dd.

---

# Pertanyaan Umum

Aplikasi tidak berjalan
Pastikan Streamlit terinstal dan pastikan file depoendensi sudah terpasang dengan benar.

Model tidak ditemukan
Folder model dibiarkan kosong karena file model akan diunduh atau dimuat otomatis.

CSV tidak terbaca
Pastikan kolom tweet tersedia dalam file CSV.

---

# Penutup

Aplikasi Streamlit ini dibuat untuk memudahkan analisis sentimen media sosial secara interaktif dan mudah dipahami. Aplikasi dapat dijalankan oleh siapa saja tanpa konfigurasi tambahan yang kompleks, sehingga cocok untuk keperluan penilaian tugas maupun demonstrasi proyek.

---

