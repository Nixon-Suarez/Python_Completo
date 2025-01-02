#4 ES UN NÚMERO PRIMO?
# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.
# Los números primos son aquellos que solo son divisibles por ellos mismos. 
# tomar el numero por ejemplo el 7 y dividirlo del 1 hasta su numero, y si ninguno es entero excepto el 1 o el 7 entonces si es numero primo.
# 1 < y < x 

def primos(numero):
    if numero < 2: 
        return False

    for y in range (2, numero):
        if numero % y == 0:
            return False 
        
        return True

while True:

    x = int(input("ingrese un numero: "))

    if x == -1:
        break
    
    if primos(x):
        print(f"El número {x} es primo")
    else:
        print(f"El número {x} no es primo")

