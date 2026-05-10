from random_word import RandomWords
from googletrans import Translator
r = RandomWords()
kelime = RandomWords()

trans = Translator()
while True:
    ingkelime = r.get_random_word() 

    ceviri = trans.translate(ingkelime, dest='tr')  

    print("İngilizce Kelime: ", ingkelime)

    cevap = input("Türkçe Çevirisi: ")  

    if cevap == ceviri.text.lower():
        print("Tebrikler! Doğru cevap.")

    else:
        print("Maalesef, yanlış cevap. Doğru cevap: ", ceviri.text)