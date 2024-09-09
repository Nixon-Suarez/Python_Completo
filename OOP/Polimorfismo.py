 # dependeiendo de un objeto el metodo se va a comportar de diferente manera 


class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido())

    
gato = Gato()
perro = Perro()


# Polimorfismo mismo metodo funciona diferente para diferentes objetos 
print(gato.sonido())    
print(perro.sonido())

# Polimorfismo de finsion al cambiar el parametro cambia el resultado no cambia la funcion
hacer_sonido(gato)
hacer_sonido(perro)

#Polimorfismo de Herencia, tambien llamado subtipos o subclases  
# al hacer esto es obligatorio que el metodo provenga de una herencia para ser usado (Este es usado en lenguajes de programacio de programacion orientada a objetos (Java))

