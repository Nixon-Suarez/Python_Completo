from time import sleep

def salida():
    print("Saliendo...")
    sleep(1)
    exit()

try:
    saludo = "hola"
    print(int(saludo))
except KeyboardInterrupt: #KeyboardInterrupt =  se genera cuando el usuario presiona Ctrl+C para interrumpir el programa.
    salida()
except NameError: #NameError = ocurre cuando el intérprete CPython no reconoce un nombre de objeto local o global que se haya proporcionado en el código fuente de Python.
    salida()
except ZeroDivisionError: # ZeroDivisionError = la división entre cero es una operación que matemáticamente no está definida
    salida()
except TypeError: #TypeError = "Error de tipo" Que sale cuando usamos un tipo de dato incorrecto. 
    salida()
except ValueError: #excepción incorporada (definida por Python) que es lanzada cuando una función espera un valor determinado pero recibe otro.
    print("Hola")
    salida()
except: #Cualquier otro error que no sea alguno de los anteriores 
    salida()

#existen muchas mas excepciones o errores dependiendo de cada modulo 
    