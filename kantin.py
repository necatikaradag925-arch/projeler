kantin_fiyatlari = {
    "simit": 10,
    "poğaça": 12,
    "meyve suyu": 15,
    "gazoz": 20,
    "çikolata": 15,
    "bisküvi": 10,
    "döner": 50,
    "ayran": 15
}

print("Kantin Listesi ve Fiyatlar: ", kantin_fiyatlari)

secim = input("Almak istediğiniz ürünü yazınız: ").lower().strip()

if secim in kantin_fiyatlari:
    fiyat = kantin_fiyatlari[secim]
    print(f"Seçtiğiniz {secim} ürününü alabilirsiniz. Fiyatı: {fiyat} TL")
else:
    print("Seçtiğiniz ürün kantinde bulunmamaktadır.")

    
