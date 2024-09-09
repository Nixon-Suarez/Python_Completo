class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando en {self.grado} de bachilerato a la edad de {self.edad} 😁")
        
nombre1 = input("Ingresar nombre: ")
edad1 = int(input("Ingresar Edad: "))
grado1 = input("Ingresar Grado: ")

Estudiante1 = Estudiante(nombre1, edad1, grado1)
print(f"""
        Nombre: {nombre1}
        Edad: {edad1}
        Grado: {grado1}
    """) 

count = 0
while count < 5:
    estudiar = input("desea estudiar estudiar y/n ")
    if estudiar.lower() == "y":
        Estudiante1.estudiar()
        break
    else:
        count += 1
    

if count == 5:
    print("No quiere estudiar 😔")