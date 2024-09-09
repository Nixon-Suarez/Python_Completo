
#  Crea una única función (importante que sólo sea una) que sea capaz
#  de calcular y retornar el área de un polígono.
#   - La función recibirá por parámetro sólo UN polígono a la vez.
#  - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

# Area de un cuadrado es Lado x Lado 
# Area de un Triangulo es Base x Altura / 2
# Area de un rectángulo es Base x Altura

#! aun hay errores debe aparecer el mensaje antes de pedir altura..
#! agregar un bucle para que funcione mas de una vez 

class Poligono:
    def __init__(self, nombre, base, altura):
        self.nombre = nombre
        self.base = base
        self.altura = altura

    def calcular_area(self):
        if self.nombre == "cuadrado" or self.nombre == "c":
            return self.base * self.base
        elif self.nombre == "rectángulo" or self.nombre == "r":
            return self.base * self.altura
        elif self.nombre == "triangulo" or self.nombre == "t":
            return (self.base * self.altura) / 2
        else:
            return None

figura = input("Ingresa la figura (nombre completo o su inicial: cuadrado, rectángulo, triangulo): ").lower()
alturas = int(input("Ingrese la altura: "))
bases = int(input("Ingrese la base: "))

poli = Poligono(figura, bases, alturas)

area = poli.calcular_area()

if area is not None:
    print(f"El área del {figura} es: {area}")
else:
    print("No se reconoce el polígono.")
