import google.generativeai as genai
from config import Config
from datetime import datetime, timedelta
from collections import deque
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NutrisiChatbot:
    """Chatbot nutrisi berbasis Google Gemini dengan fitur riwayat dan rate limiting."""
    
    def __init__(self):
        """Inisialisasi chatbot dengan validasi dan konfigurasi."""
        Config.validate()
        
        # Konfigurasi Gemini
        genai.configure(api_key=Config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(Config.get_model())
        
        # Riwayat chat
        self.chat_history = deque(maxlen=Config.MAX_HISTORY)
        self.conversation_context = []
        
        # Rate limiting
        self.request_timestamps = deque(maxlen=Config.MAX_REQUESTS_PER_MINUTE)
        
        # System prompt untuk nutrisi
        self.system_prompt = """Anda adalah ahli gizi profesional yang membantu pengguna memahami 
        kebutuhan gizi mereka. Jawab pertanyaan tentang nutrisi, makanan sehat, dan pola makan 
        dengan cara yang mudah dipahami. Selalu berikan informasi yang akurat berdasarkan ilmu gizi. 
        Jika ditanya hal di luar nutrisi, kembalikan topik ke nutrisi dan kesehatan."""
    
    def _check_rate_limit(self) -> bool:
        """Cek apakah pengguna melebihi rate limit."""
        now = datetime.now()
        minute_ago = now - timedelta(minutes=1)
        
        # Hapus timestamp yang lebih tua dari 1 menit
        while self.request_timestamps and self.request_timestamps[0] < minute_ago:
            self.request_timestamps.popleft()
        
        if len(self.request_timestamps) >= Config.MAX_REQUESTS_PER_MINUTE:
            return False
        
        self.request_timestamps.append(now)
        return True
    
    def _validate_input(self, pertanyaan: str) -> tuple[bool, str]:
        """Validasi input pengguna."""
        if not pertanyaan or not isinstance(pertanyaan, str):
            return False, "⚠️ Silakan masukkan pertanyaan yang valid."
        
        pertanyaan = pertanyaan.strip()
        if len(pertanyaan) < 3:
            return False, "⚠️ Pertanyaan terlalu pendek. Silakan jelaskan lebih detail."
        
        if len(pertanyaan) > 2000:
            return False, "⚠️ Pertanyaan terlalu panjang. Maksimal 2000 karakter."
        
        return True, pertanyaan
    
    def tanya(self, pertanyaan: str) -> str:
        """Mengirim pertanyaan ke model dan mengembalikan jawaban dengan konteks percakapan."""
        # Validasi input
        is_valid, result = self._validate_input(pertanyaan)
        if not is_valid:
            return result
        
        pertanyaan = result
        
        # Cek rate limit
        if not self._check_rate_limit():
            return f"⏱️ Anda telah mencapai batas permintaan ({Config.MAX_REQUESTS_PER_MINUTE} per menit). Silakan tunggu sebentar."
        
        try:
            # Build conversation context
            messages = f"{self.system_prompt}\n\n"
            
            # Tambahkan riwayat chat
            for msg in self.chat_history:
                messages += f"Pengguna: {msg['pertanyaan']}\nAssistant: {msg['jawaban']}\n\n"
            
            messages += f"Pengguna: {pertanyaan}"
            
            # Generate response
            response = self.model.generate_content(messages)
            jawaban = response.text.strip()
            
            # Simpan ke riwayat
            self.chat_history.append({
                'pertanyaan': pertanyaan,
                'jawaban': jawaban,
                'timestamp': datetime.now()
            })
            
            logger.info(f"Pertanyaan diproses: {pertanyaan[:50]}...")
            return jawaban
            
        except genai.types.HarmBlockedError as e:
            logger.warning(f"Konten diblokir: {str(e)}")
            return "⚠️ Pertanyaan Anda tidak sesuai dengan kebijakan. Silakan ajukan pertanyaan yang berbeda."
        
        except genai.types.GenerativeAIError as e:
            logger.error(f"API Error: {str(e)}")
            return f"❌ Terjadi kesalahan pada API: {str(e)}"
        
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return f"❌ Maaf, terjadi kesalahan yang tidak terduga: {str(e)}"
    
    def get_history(self) -> list:
        """Mendapatkan riwayat chat."""
        return list(self.chat_history)
    
    def clear_history(self):
        """Menghapus riwayat chat."""
        self.chat_history.clear()
        logger.info("Riwayat chat dihapus")
    
    def analyze_nutrition(self, makanan: str) -> str:
        """Analisis kandungan gizi makanan."""
        prompt = f"""Berikan analisis gizi untuk '{makanan}' dalam format:
        - Kalori (per 100g)
        - Protein
        - Lemak
        - Karbohidrat
        - Vitamin dan mineral utama
        - Manfaat kesehatan
        
        Jawab dalam bahasa Indonesia."""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            logger.error(f"Error analyzing nutrition: {str(e)}")
            return f"❌ Tidak dapat menganalisis gizi: {str(e)}"
