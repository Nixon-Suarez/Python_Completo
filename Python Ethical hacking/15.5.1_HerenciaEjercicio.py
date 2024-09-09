class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresar_datos(self):
        self.datos = [int(input("Ingrese el Valor " + str(i + 1) + "= ")) for i in range(self.n)]

class Operaciones(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
        
    def suma(self):
        a,b = self.datos
        s = a + b
        print("La Suma de los numeros es {}".format(s))

    def resta(self):
        a,b = self.datos
        r = a - b
        print("La Resta de los numeros es {}".format(r))

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def cuadrada(self):
        import math
        a = self.datos[0]
        print("La Raiz es {}".format(math.sqrt(a)))


ejemplo = Operaciones()
ejemplo.ingresar_datos()
ejemplo.suma()

ejemplo2 = Raiz()
ejemplo2.ingresar_datos()
ejemplo2.cuadrada()