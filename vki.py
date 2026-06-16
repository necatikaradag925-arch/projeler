kilo = float(input("kaç kilo olduğunuzu giriniz:")) 
boy = float(input("boyunuzu metre cinsinden giriniz :"))        

  

 

vki = kilo / (boy * boy)
        


print(f"vücut kitle indeksinizs: {vki:.2f}")     

    
if vki < 18.5:
    print("zayıf")

elif vki >= 18.5 and vki < 25:
    print("normal")

elif vki >= 25 and vki < 29.9:  
    print("kilolu")

else:
    print("obez")   