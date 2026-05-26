kantin_fiyatlari = {
    "simit": 10,
    "poğaça": 12,
    "meyve suyu": 15,
    "gazoz": 20,
    "çikolata": 15,
    "bisküvi": 10,
    "döner": 50,
    "ayran": 20
}

print("Kantin Listesi ve Fiyatlar: ", kantin_fiyatlari)

secim = input("Almak istediğiniz ürünü yazınız: ").lower().strip()

if secim in kantin_fiyatlari:
    fiyat = kantin_fiyatlari[secim]
    print(f"Seçtiğiniz {secim} ürününün fiyatı: {fiyat} TL")
    
    bakiye = float(input("Lütfen bakiyenizi giriniz: "))
    
    if bakiye >= fiyat:
        print(f"{secim} ürününü satın alabilirsiniz. Kalan bakiyeniz: {bakiye - fiyat} TL")
    else:
        print(f"Yetersiz bakiye. {secim} ürününün fiyatı {fiyat} TL, ancak bakiyeniz sadece {bakiye} TL.")
else:
    print("Seçtiğiniz ürün kantinde bulunmamaktadır.")