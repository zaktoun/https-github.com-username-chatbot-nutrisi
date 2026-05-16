````markdown
# 🚀 Cara Menjalankan Chatbot Nutrisi Sehat

## ⚡ Quick Start (5 menit)

### 1. Setup Environment
```bash
# Buat virtual environment
python3 -m venv venv

# Aktivasi (Linux/Mac)
source venv/bin/activate

# Aktivasi (Windows)
venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup API Key
```bash
# Copy template
cp .env.example .env

# Edit dengan API key Anda
# Dapatkan di: https://makersuite.google.com/app/apikey
nano .env
```

**Isi .env:**
```env
GOOGLE_API_KEY=your_api_key_here
```

### 4. Jalankan Aplikasi
```bash
streamlit run app.py
```

Aplikasi akan membuka di: **http://localhost:8501** 🎉

---

## 📋 Prasyarat

- ✅ Python 3.8+
- ✅ pip (Python Package Manager)
- ✅ Koneksi internet
- ✅ Google Gemini API Key (gratis)

---

## 🔐 Dapatkan API Key (Gratis)

### Langkah-Langkah:
1. Buka [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Klik **"Create API Key"**
3. Pilih **"Create API key in new Google Cloud project"**
4. Copy key Anda
5. Paste ke file `.env`

> ⚠️ **Jangan share API key Anda!**

---

## 🐛 Common Issues

### Streamlit tidak ditemukan?
```bash
pip install streamlit==1.32.2
```

### Module not found error?
```bash
pip install -r requirements.txt --force-reinstall
```

### API key not valid?
```bash
# Cek .env file ada
ls -la | grep .env

# Cek isi .env
cat .env

# Reset: dapatkan key baru dari https://makersuite.google.com/app/apikey
```

---

## 📚 Dokumentasi Lengkap

Lihat [README.md](README.md) untuk dokumentasi komprehensif!

````
