sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: ")) 

print("Yapmak istediğiniz işlemi seçiniz:")
print("+. Toplama")
print("-. Çıkarma")
print("*. Çarpma")
print("/. Bölme")

işlem = input("İşlemi seçiniz: ")

if işlem == "+":
    sonuç = sayi1 + sayi2
    print("Sonuç: ", sonuç)
elif işlem == "-":
    sonuç = sayi1 - sayi2
    print("Sonuç: ", sonuç)
elif işlem == "*":
    sonuç = sayi1 * sayi2
    print("Sonuç: ", sonuç)
elif işlem == "/":
    if sayi2 != 0:
        sonuç = sayi1 / sayi2
        print("Sonuç: ", sonuç)
    else:
        print("Hata: Bir sayı sıfıra bölünemez.")
 
