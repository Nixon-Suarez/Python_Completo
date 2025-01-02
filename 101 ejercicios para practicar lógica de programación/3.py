#3 LA SUCESIÓN DE FIBONACCI
#  Escribe un programa que imprima los 50 primeros números de la sucesión
#  de Fibonacci empezando en 0.
#  - La serie Fibonacci se compone por una sucesión de números en
#    la que el siguiente siempre es la suma de los dos anteriores.
#    0, 1, 1, 2, 3, 5, 8, 13...

def Fibonacci():
    a = 0 # inicia en 0
    b = 1 # le va a sumar 
    for _ in range(1, 50): # por cada iteracion con un rango de 1 a 50 numeros
        print(a) # imprime a 

        fibo = a + b # se crea una nueva variable de la suma de a y b 
        a = b # a se reasigna un nuevo valor que en este caso es b que era el numero anterior antes de que se sumaran 
        b = fibo # b se reasigna un nuevo valor el cual es fibo el cual es la suma entre a + b para que en la otra iteracion 
        # a se reasignara como 1 y b como la 1 en la siguiente seria a = 1, b = 2

Fibonacci()
# 1
# 1 + 1 
# 2 + 1
# 3 + 2
# 5 + 3
# 8 + 5
# 13 + 8
# 21 + 13

