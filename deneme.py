yaş = int(input("Yaşınızı Giriniz: "))
okul =  int(input("Okula gidiyor musunuz? (evet: 1 ve hayır: 0) "))

if yaş >= 18 and okul == 0:
    print("Askere gelme yaşınız geldi")

elif yaş >= 18 and okul == 1:
     print("okulunuz Bittiğinde askere Geleceksiniz!")
    
elif yaş == 18 or yaş < 18 and okul == 0: 
     print("askere gelme yaşınız gelmedi")

elif yaş == 18 or yaş < 18 and okul == 1:
     print("askere gelme yaşınız gelmedi")

else: 
     print("Hatalı giriş yaptınız")