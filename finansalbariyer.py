maddidurum = input( "Bu alacağın şey için bütçen var mı? ") 

if maddidurum == "hayır":
    print(" Önce para biriktirmelisin.  ")  

elif maddidurum == "evet":
    print(" O zaman alabilirsin.")

    zaman = input("Bu ürünü haftada kaç saat kullanacaksın? ")

    if zaman <= "2":
        print("Bu kadar az kullanacağın bir ürünü almana gerek yok kiralayabilirsin. " )    

    elif zaman > "2":
        print("Bu ürünü almak kiralamak daha uygun olabilir. ") 

    alternatif = input("bu ürünün daha ucuz ama aynı işi gören bir alternatifi var mı? ") 

    if alternatif == "evet":
        print("O zaman o alternatifi almak daha mantıklı olabilir. ")   

    elif alternatif == "hayır":
        print("O zaman bu ürünü almak mantıklı olabilir. ") 
