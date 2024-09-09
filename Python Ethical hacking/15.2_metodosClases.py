# un metodo es una funcion dentro de una clase 
# determina una accion o un comportamiento
# los metodos siempre tienen un self
# la funcion constructura es __init__ (la funcion constructor da un orden dentro de la clase y todo lo que este en init se va a ejecutar)


# class Matematicas:
#     def suma(self):
# #        👇 el self funciona para sacar la variable del metodo sin este no se puede utilizar ni invocar fuera
#         self.uno = 1
#         self.dos = 2
# #         👇 esta variable no se puede llamar fuera del metodo ya que no tiene el self pero este funciona dentro 
#         tres = 3
#         suma = self.dos + tres
#         return suma
    
# s = Matematicas()
# sumando  = s.suma()
# print(sumando)

# class INit:
#     def __init__(self):
#         print("ME TENGO QUE EJECUTAR PORQUE ESTOY EN EL INIT")

#objet1 = INit()

# class Ropa:
#     #     👇el constructor (init) se ejecuta al crear el objeto
#     def __init__(self):
#         self.marca = "NIKE"
#         self.talla = "M"
#         self.color = "Azul"
# #   mientras que sin el contructor se tiene que llamar a la funcion para que se pueda ejecutar
#     def propiedades(self):
#         self.marca1 = "NIKE"
#         self.talla1 = "M"
#         self.color1 = "Azul"

# objeto1 = Ropa()
# print(objeto1.marca)

# objeto2 = Ropa()
# objeto2.propiedades()
# print(objeto2.marca1) 

class Calculadora:
    def __init__(self, a, b):
        self.suma = a + b
        self.resta = a - b
        self.multiplicacion = a * b
        self.divicion =  a / b

    def sum(self, a, b):
        self.suma = a + b

#                   👇ya que este es el contructor los argumenos se ponen aqui
calc = Calculadora(5,7)
print(calc.divicion)

#        👇ya que este es un metodo los argumentos se pasan en el llamado del metodo 
calc.sum(8,9)
print(calc.suma)







        




