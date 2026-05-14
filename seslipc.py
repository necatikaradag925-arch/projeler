import random
import os
import time
from elevenlabs.client import ElevenLabs
import pygame

# 1. API Bağlantısı
client = ElevenLabs(
    api_key="sk_f569bbf7333b9e5c57b020b12cfb7e90314d7a51904c0d52"
)

# Ses motorunu başlat (Pencere açılmaması için şart)
pygame.mixer.init()

# 2. "Sör" Ağırlıklı Cümleler

cümleler = [   
    ", sistemler etkinleştirildi. Tüm ağ protokolleri çevrimiçi.",
    " bütün fonksiyonlar normal düzeyde çalışıyor. Her şey hazır.",
    ", sistem taraması tamamlandı. Herhangi bir dış müdahale tespit edilmedi.",
    " güç seviyeleri optimize edildi. Bir sonraki talimatınızı bekliyorum.",
    " veri akışı dengelendi. Komutlarınızı bekliyorum.",
    " erişim onaylandı. Sistem merkezi kontrolü tamamen sizin yetkinizde.",
    " cihaz yapılandırması tamamlandı. Her şey yolunda görünüyor.",
    " sistem durumu kontrol ediliyor. Tüm sunucular aktif ve stabil durumda.",
]  

print("--- Jarvis Sistemi Aktif ---")
print("Yeni replik için ENTER'a bas, çıkmak için 'q' yaz.")
  
# 3. ANA DÖNGÜ
while True:
    islem = input("\nKomut bekliyorum (Enter/q): ").lower()
    
    if islem == 'q':
        by = ["Sistem, kapanıyor, görüşmek üzere efendim."]
        secilen_metin = random.choice(by)
    else:
        secilen_metin = random.choice(cümleler)

    print(f"Jarvis: {secilen_metin}")

    try:
        # Ses Oluşturma
        audio = client.text_to_speech.convert(
            text=secilen_metin,
            voice_id="mKFxb09SBPIGwSZPV1FE", 
            output_format="mp3_44100_128",
            model_id="eleven_multilingual_v2"
        )
        
        # Benzersiz isimle kaydet (Permission hatasını önler)
        dosya_adi = f"jarvis_{int(time.time())}.mp3"
        audio_bytes = b"".join(list(audio))
        
        with open(dosya_adi, "wb") as f:
            f.write(audio_bytes)
            
        # Sesi ARKA PLANDA ÇAL (Pencere açılmaz, odağı terminalde tutar)
        pygame.mixer.music.load(dosya_adi)
        pygame.mixer.music.play()
        
        if islem == 'q':
            # Sesin çalması için kısa bir süre bekle ve çık
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            break
            
    except Exception as e:
        print(f"Hata oluştu: {e}")
        if islem == 'q': break

# Kapatırken motoru durdur
pygame.mixer.quit()
