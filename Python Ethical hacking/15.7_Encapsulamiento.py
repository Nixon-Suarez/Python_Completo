# esta tecnica se realiza para que los atributos y metodos de un objeto se oculten con fines de que no sean accedidos desde fuera de la clase 
#esto nos da integridad de objetos


class Cliente:
    def __init__(self):
#?------------encapsular un atributo
        self.__name  = "Pedro"
#            ☝️ __variable = esto es el encapsulaminerto solo puedo acceder a el atraves de su clase no afuera
       # print(self.__name)

    def getname(self):   # este seria el metodo para poder imprimirlo afuera pero esto es posible porque lo seguimos trabajando dentro de la clase
        return self.__name  #lo que hace es retornarlo para despues poder imprimirlo afuera
#?---------------encapsular metodos
#           👇 __namemetodo = asi se encapsula en metodo
    def __saludo(self):
        print("Bienvenidosss")
# 👇 accede a un metodo encapsulado 1
persona = Cliente()
print(persona.getname())
# 👇 accede a un metodo encapsulado 2
print(persona._Cliente__name)
# 👇 accede a un metodo encapsulado 
persona._Cliente__saludo()
