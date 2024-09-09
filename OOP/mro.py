# mro = Method resolution order
# esto es el orden en que se ejecutan los metodos y atributos en caso de que ellos se llamen de la misma manera pero en diferentes clases y estos se hereden 
# cuales tendrian prioridad 

class A:
    def hablar(self):
        print("hola soy A")

class B(A):
    # def hablar(self):
    #     print("hola soy B")
    pass

class C(A):
    # def hablar(self):
    #     print("hola soy C")
    pass

class D(B,C):
    # def hablar(self):
    #     print("hola soy D")
        pass

d = D()

d.hablar()

# para hacer esto☝️ sin necesidad de probar podemos hacer esto⬇️
print(D.mro())


A.hablar(d)
# ☝️ llamar el metodo hablar de la clase A por medio de un objeto que instacia de una clase que hereda de A