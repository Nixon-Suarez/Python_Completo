import random 

meta = 20 

caracol1 = 0
caracol2 = 0

while True: 
    avance_caracol_1 = random.randint(1,4)
    avance_caracol_2 = random.randint(1,4)

    caracol1 += avance_caracol_1
    caracol2 += avance_caracol_2

    print(f"el caracol uno avanza {avance_caracol_1} espacios para un tatal de {caracol1} espacios")
    print(f"el caracol dos avanza {avance_caracol_2} espacios para un tatal de {caracol2} espacios")
    print(".....................................................")

    if caracol1 >= 20 or caracol2 >=20:
        break

if caracol1 > caracol2:
    print("El ganador es caracol 1")
elif caracol2 > caracol1:
    print("caracol 2 a ganado")
else:
    print("Empate entre los caracoles")