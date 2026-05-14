baliklar = {
    "japon": 22,
    "beta": 26,
    "levrek": 30,
    "lepistes": 24,
    "neon tetra": 28,
    "melek balığı": 26,
    "vatoz": 25,
}   

secim = input("Hangi balık türünü besliyorsunuz? ").lower().strip() 

if secim in baliklar:
    print(f"{secim} balığı için önerilen su sıcaklığı: {baliklar[secim]}°C" )   

else:    print("Üzgünüm, bu balık türü için bilgi bulunmamaktadır.")    

sıcaklık = float(input("Akvaryumunuz kaç derece? "))  

if sıcaklık in baliklar.values():
    print("Akvaryumunuzun sıcaklığı önerilen aralıkta.")
elif sıcaklık < min(baliklar.values()):
    print("Akvaryumunuzun sıcaklığı önerilen aralığın altındadır.")
else:
    print("Akvaryumunuzun sıcaklığı önerilen aralığın üstündedir.") 