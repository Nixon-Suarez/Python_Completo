import random

def atk_enemy(num):
    if num == 2:
        daño = random.randrange(0,20,5)
        return daño
    elif num == 3:
        daño = random.randrange(5,20,5)
        return daño
    else:
        daño = random.randrange(0,30,5)
        return daño
    
def atk(atk):
    if atk == 1:
        print("Elegiste el ataque mas fuerte")
        daño = random.randrange(20,70,10)
        return daño, False
    else:
        print("Elegiste el ataque normal")
        daño = random.randrange(10,40,10)
        return daño, True