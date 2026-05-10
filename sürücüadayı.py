yaş = int(input("Yaşınızı giriniz: ")) 
  
if yaş >= 18: 
    print("Ehliyet alabilirsiniz.")

puani = float(input("sınav puanınızı giriniz: "))  

if  puani < 70:
        print("ehliyet alamazsınız.")

elif puani >= 70:
        print("ehliyet alabilirsiniz.")
        parankaç = float(input("kaç paranız var: "))
                        
        parankaç = float(input("kaç paranız var: "))
                        
        if parankaç >= 500000:
                print("arabanız ve ehliyetiniz hayırlı olsun.")

        elif parankaç < 500000:
                print("arabaya  elveda et ama ehliyeti kaptın.")

 
elif yaş < 18: 
    print("Ehliyet alamazsınız.")
    
    