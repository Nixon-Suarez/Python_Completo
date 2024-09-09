
#?⬇️ HACER UNA FUNCION SIN PARAMETROS NI ARGUMENTOS
#def saludar_usuario():
#     print(""" 
# Hola comom estas 
# este canal trata de programacion 
# sigueme en ...............
#     """)

# saludar_usuario()
 
#? ⬇️Hacer una funcion con parametros definidos
def suma(numero1, numero2):
    resultado = numero1 + numero2
    print(f"las Suma entre {numero1} + {numero2} es: {resultado}")

def multi(numero1, numero2):
    resultado = numero1 * numero2
    print(f"las multiplicacion entre {numero1} y {numero2} es: {resultado}")

def resta(numero1, numero2):
    resultado = numero1 - numero2
    print(f"las resta entre {numero1} y {numero2} es: {resultado}")


def div(numero1, numero2):
    resultado = numero1 / numero2
    print(f"la divicion entre {numero1} y {numero2} es: {resultado}")

continuar = True
while continuar:
    primer_numero = float(input("ingrese el primer numero: "))
    segundo_numero = float(input("ingrese el segundo numero: "))
    operacion = input("operacion que desea ejecutar: suma➕, multi✖️, resta➖, div➗: ").lower


    if operacion == "suma":
        suma(primer_numero, segundo_numero)
    elif operacion == "multi":
        multi(primer_numero, segundo_numero)    
    elif operacion == "resta":
        resta(primer_numero, segundo_numero)
    elif operacion == "div":
        div(primer_numero, segundo_numero)
    else:
        print("esa operacion no existe 😠")

    desea_continuar = input("desea realizar otra operacion y/n: ")
    if desea_continuar.lower() != 'y':
        continuar = False
        print("gracias por usar la calculadora! 👋")
    
