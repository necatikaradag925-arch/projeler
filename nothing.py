import time
import keyboard
zaman = int(input("kaçtan geriye sayılsın: " ))


while zaman > 0:
    print(zaman)
    interrupted = False    
   
    for _ in range(10): 
        time.sleep(0.1)
        if keyboard.is_pressed("j"):
            interrupted = True
            break 
    
    if interrupted: 
        print("sayaç durduruldu") 
        break       
       
    zaman -= 1 