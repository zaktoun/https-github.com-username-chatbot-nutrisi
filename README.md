````markdown
# 🥦 Chatbot Nutrisi Sehat

> **"Asisten AI untuk edukasi gizi sehat berbasis Gemini"** - Chatbot yang membantu Anda memahami nutrisi dengan mudah dan akurat.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 📑 Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Teknologi](#teknologi)
- [Instalasi](#instalasi)
- [Konfigurasi](#konfigurasi)
- [Cara Menjalankan](#cara-menjalankan)
- [Penggunaan](#penggunaan)
- [Struktur Proyek](#struktur-proyek)
- [Troubleshooting](#troubleshooting)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

---

## ✨ Fitur Utama

### 💬 **Chat Interaktif**
- Tanya jawab seputar nutrisi, gizi seimbang, dan pola makan sehat
- Percakapan dengan konteks (riwayat chat tersimpan)
- Rate limiting untuk keamanan API

### 📊 **Analisis Gizi**
- Lihat kandungan nutrisi makanan (kalori, protein, lemak, karbo)
- Manfaat kesehatan dan vitamin
- Rekomendasi pola makan

### 🎯 **AI Berkualitas**
- Powered by **Google Gemini 2.5 Flash** API
- Natural Language Processing (NLP) canggih
- Jawaban akurat berbasis ilmu gizi

### 🛡️ **Keamanan**
- Manajemen API key via `.env`
- Input validation dan error handling
- Rate limiting per pengguna

### 🎨 **UI/UX Friendly**
- Interface interaktif dengan Streamlit
- Sidebar dengan fitur tambahan
- Chat history yang terorganisir
- Tips gizi harian

---

## 🛠️ Teknologi

| Komponen | Teknologi |
|----------|-----------|
| **Framework** | Streamlit 1.32.2 |
| **AI/LLM** | Google Generative AI (Gemini 2.5 Flash) |
| **Bahasa** | Python 3.8+ |
| **Environment** | python-dotenv |
| **Logging** | Python Built-in Logging |

---

## 📦 Instalasi

### Prasyarat
- **Python 3.8+**
- **pip** (Package Manager)
- **Git** (untuk clone repository)

### Langkah-Langkah

#### 1️⃣ Clone Repository
```bash
git clone https://github.com/zaktoun/https-github.com-username-chatbot-nutrisi.git
cd https-github.com-username-chatbot-nutrisi
```

#### 2️⃣ Buat Virtual Environment
```bash
# Untuk Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Untuk Windows
python -m venv venv
venv\Scripts\activate
```

#### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ Konfigurasi Environment
```bash
# Copy file .env.example ke .env
cp .env.example .env

# Edit .env dan tambahkan API key Anda
nano .env
# atau gunakan editor favorit Anda
```

---

## 🔐 Konfigurasi

### 1. Dapatkan Google Gemini API Key

#### 🌐 Langkah-Langkah:
1. Buka [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Klik **"Create API Key"**
3. Pilih **"Create API key in new Google Cloud project"** atau gunakan project existing
4. Copy API key Anda

#### ⚙️ Update File `.env`
```env
# Google Gemini API Configuration
GOOGLE_API_KEY=your_api_key_here

# Optional: Model Configuration
MODEL=gemini-2.5-flash
TEMPERATURE=0.6
MAX_TOKENS=500

# Rate Limiting
MAX_REQUESTS_PER_MINUTE=10
```

### Parameter Konfigurasi

| Parameter | Default | Deskripsi |
|-----------|---------|-----------|
| `GOOGLE_API_KEY` | - | **[Required]** API key dari Google Gemini |
| `MODEL` | `gemini-2.5-flash` | Model AI yang digunakan |
| `TEMPERATURE` | `0.6` | Kreativitas respons (0.0-1.0) |
| `MAX_TOKENS` | `500` | Panjang maksimal respons |
| `MAX_REQUESTS_PER_MINUTE` | `10` | Batasan permintaan per menit |

---

## 🚀 Cara Menjalankan

### Local Development
```bash
# Pastikan virtual environment aktif
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate     # Windows

# Jalankan aplikasi
streamlit run app.py
```

Aplikasi akan terbuka di: **`http://localhost:8501`**

### Production Deployment

#### Deploy ke Streamlit Cloud
```bash
# Push ke GitHub
git add .
git commit -m "Deploy chatbot"
git push origin main

# 1. Buka https://share.streamlit.io
# 2. Klik "New app"
# 3. Connect repository Anda
# 4. Set GOOGLE_API_KEY di Secrets
```

#### Deploy ke Hugging Face Spaces
1. Buat repository di [Hugging Face](https://huggingface.co/spaces)
2. Push code Anda
3. Add secret `GOOGLE_API_KEY` di Settings

---

## 💻 Penggunaan

### Interface Utama

#### **Tab 1: Chat**
```
1. Ketik pertanyaan Anda di text area
2. Klik tombol "Tanyakan"
3. Tunggu respons dari AI
4. Lihat riwayat chat di atas
```

**Contoh pertanyaan:**
- "Apa manfaat protein untuk tubuh?"
- "Berapa kebutuhan kalori harian saya?"
- "Bagaimana cara diet sehat?"
- "Makanan apa yang kaya vitamin C?"

#### **Tab 2: Analisis Gizi**
```
1. Masukkan nama makanan
2. Klik "Analisis"
3. Lihat detail kandungan gizi
```

**Contoh:**
- Telur
- Nasi Merah
- Ayam Goreng
- Brokoli

### Advanced Usage

#### Menggunakan Class Chatbot Secara Langsung
```python
from chatbot_nutrisi import NutrisiChatbot

# Inisialisasi
bot = NutrisiChatbot()

# Tanya
jawaban = bot.tanya("Apa itu kalori?")
print(jawaban)

# Analisis gizi
analisis = bot.analyze_nutrition("Telur")
print(analisis)

# Lihat riwayat
history = bot.get_history()
print(history)

# Hapus riwayat
bot.clear_history()
```

---

## 📂 Struktur Proyek

```
https-github.com-username-chatbot-nutrisi/
├── app.py                    # Main Streamlit application
├── chatbot_nutrisi.py        # Chatbot core logic
├── config.py                 # Configuration & settings
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore file
├── README.md                # Documentation (file ini)
└── cara menjalankan.md      # Quick start guide (Indonesian)
```

### File Descriptions

| File | Deskripsi |
|------|-----------|
| **app.py** | Interface Streamlit utama dengan UI/UX interaktif |
| **chatbot_nutrisi.py** | Logic chatbot, chat history, rate limiting, validation |
| **config.py** | Konfigurasi API, model, rate limiting |
| **requirements.txt** | Semua dependencies yang diperlukan |
| **.env.example** | Template environment variables |
| **.gitignore** | Exclude file sensitif dari Git |

---

## 🐛 Troubleshooting

### ❌ Error: "GOOGLE_API_KEY belum diatur"
**Solusi:**
```bash
# Pastikan .env file ada di root directory
ls -la | grep .env

# Cek isi .env
cat .env

# Jika tidak ada, buat dari .env.example
cp .env.example .env
nano .env  # Edit dengan API key Anda
```

### ❌ Error: "ModuleNotFoundError: No module named 'streamlit'"
**Solusi:**
```bash
# Install dependencies
pip install -r requirements.txt

# Atau install individual
pip install streamlit google-generativeai python-dotenv
```

### ❌ Error: "Connection refused" / API tidak merespons
**Solusi:**
```bash
# Cek koneksi internet Anda
ping google.com

# Cek API key valid
# Buka https://makersuite.google.com/app/apikey

# Cek rate limiting
# Default: 10 requests per menit
```

### ⚠️ Aplikasi sangat lambat
**Solusi:**
```python
# Kurangi MAX_TOKENS di .env
MAX_TOKENS=300  # Default 500

# Atau ubah TEMPERATURE
TEMPERATURE=0.3  # Lebih rendah = lebih cepat
```

### 🔄 Riwayat chat hilang saat reload
**Catatan:** Ini normal karena Streamlit melakukan refresh. Untuk persistent storage, perlu database (sudah direncanakan di v2).

---

## 📈 Roadmap Pengembangan

### ✅ v1.0 (Current)
- [x] Chat interface
- [x] Chat history (session)
- [x] Nutrition analysis
- [x] Rate limiting
- [x] Input validation
- [x] Improved UI/UX

### 🔄 v1.1 (Planned)
- [ ] Persistent chat history (database)
- [ ] User profiles & personalization
- [ ] Export results to PDF
- [ ] Multi-language support
- [ ] Chatbot personality customization

### 🚀 v2.0 (Future)
- [ ] Integration dengan nutrition API
- [ ] Mobile app version
- [ ] Voice input/output
- [ ] Real-time nutrition database
- [ ] Community features

---

## 💡 Tips & Best Practices

### ✅ Do's
```python
✓ Gunakan pertanyaan yang spesifik
✓ Ketik dengan grammar yang baik
✓ Tambahkan konteks jika perlu (umur, aktivitas, kondisi)
✓ Scroll up untuk melihat riwayat chat
✓ Gunakan analisis gizi untuk detail makanan
```

### ❌ Don'ts
```python
✗ Jangan berisi informasi kesehatan serius tanpa konsultasi dokter
✗ Jangan abuse rate limit (farming API)
✗ Jangan commit .env ke repository
✗ Jangan share API key Anda
✗ Jangan gunakan untuk diagnosis medis
```

---

## 🤝 Kontribusi

Kami terbuka untuk kontribusi! 🎉

### Cara Berkontribusi:
1. **Fork** repository ini
2. **Buat branch** fitur baru (`git checkout -b feature/AmazingFeature`)
3. **Commit** perubahan (`git commit -m 'Add AmazingFeature'`)
4. **Push** ke branch (`git push origin feature/AmazingFeature`)
5. **Buat Pull Request**

### Kontribusi yang Diterima:
- 🐛 Bug fixes
- ✨ Fitur baru
- 📖 Dokumentasi
- 🎨 UI/UX improvements
- 🧪 Test cases
- 🌍 Translations

---

## 📄 Lisensi

Project ini berlisensi di bawah [MIT License](LICENSE) - silakan lihat file LICENSE untuk detail lengkap.

---

## 👥 Tim Pengembang

- **Author:** [zaktoun](https://github.com/zaktoun)
- **Project:** Hacktiv8 Final Project
- **Dibuat:** Oktober 2025

---

## 🔗 Links & Resources

- 📚 [Google Gemini API Docs](https://ai.google.dev/)
- 📦 [Streamlit Documentation](https://docs.streamlit.io/)
- 🥗 [Nutrition Information](https://www.fatsecret.com/)
- 🔐 [Python dotenv](https://github.com/theskumar/python-dotenv)

---

## 📞 Support & Feedback

Jika Anda mengalami masalah atau punya saran:

1. **GitHub Issues:** [Create an Issue](https://github.com/zaktoun/https-github.com-username-chatbot-nutrisi/issues)
2. **Email:** Buka issue di repository
3. **Discussions:** Forum diskusi di GitHub

---

## 🙏 Terima Kasih

Terima kasih telah menggunakan **Chatbot Nutrisi Sehat**! Semoga aplikasi ini membantu Anda menjalani gaya hidup yang lebih sehat. 🥗💪

---

**⭐ Jika project ini bermanfaat, silakan beri bintang!**

````
