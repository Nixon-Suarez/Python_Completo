#numero par o impar menores al numero puesto
# todos los numeros pares o impares anteriores imprimirlos 
#par es true impar es false

numero = 0
pares = ""
impares = ""

while numero < 1:
    numero = int(input("Ingrese un numero entero positivo: "))

if numero % 2 == 0:
    for i in range(1, numero+1):
        if i % 2 == 0:
            pares += str(i) + ","
    print(pares[:-1])
else:
    for i in range(1, numero+1):
        if i % 2 == 1:
            impares  += str(i) + ","
    print(impares[:-1])