import yfinance as yf
import time

def piyasa_verileri_al():
    # Verileri kütüphane üzerinden çekiyoruz
    dolar_verisi = yf.Ticker("TRY=X")
    btc_verisi = yf.Ticker("BTC-USD")
    euro_verisi = yf.Ticker("EURTRY=X")
    
    dolar = dolar_verisi.history(period="1d")['Close'].iloc[-1]
    btc = btc_verisi.history(period="1d")['Close'].iloc[-1]
    euro = euro_verisi.history(period="1d")['Close'].iloc[-1]
    
    return dolar, euro, btc

print("--- Amele bot sürünmeye başladı ---")    

while True:
    try:
        # 1. Verileri alıyoruz
        dolar, euro, btc = piyasa_verileri_al()
        
        # 2. Ekrana yazdırıyoruz
        print(f" DOLAR: {dolar:.2f} TL")
        print(f" EURO : {euro:.2f} TL")
        print(f" BTC  : {btc:.2f} USD")
        
        print("\n30 saniye kestircem moruk...")
        
        # 3. Senin o özel soruların
        cevap = input("nasılsın iyimisin bu arada? ")
        if cevap.lower() == "iyiyim":
            print("Harika! sürünmeye devam o zaman")
        else:
            print("Anladım moruk, hayat zor...")

        # 4. Bekleme süresi
        time.sleep(30)

    except Exception as e:
        # try ile tam aynı hizada olmalı!
        print(f"Hata oluştu: {e}")
        time.sleep(5)   