
#* crea archivo
nombre = input("Ingrese su nombre ha almacenar \n ")
#?      ⬇️open abre el archivo o lo crea si esta con Append 
file = open("nombres.txt", "a")
#                          ☝️a = Append (crea un archivo guarda los datos en el o si ya existe el archivo solo lo guarda), 
#                             r = Read (solo permite leer y solo se abre si ya existe), 
#                             w = write (crea un archivo o guarda en el, el dato y lo elimana al recargarlo)
file.write(nombre + "\n")
file.close()
#☝️ esto crea un archivo de texto (nombres.txt) el cual almacena los datos

 #* ⬇️elimina archivos 
from os import remove # importa remove 
remove ("nombres.txt") # remove elimina el archivo 
print("\nSe ha eliminado el archivo")

#⬇️ abre el archivo ya existente Tuplas.py solo para leer (r) y este es almacenado en una variable
archivo = open("Tuplas.py","r")
archivo = archivo.read() #  Lee todo el contenido del archivo y lo pasa a la variable archivo
print(archivo) # imprime todo el contenido del archivo

#⬇️ otra forma de hacer lo mismo 

#      nombre archivo ha abrir
#           ⬇️           ⬇️read      ⬇️nombre de la variable que va a tomar el valor del archivo
with open ("Tuplas.py", "r") as  archivo:
    arc =  archivo.read() #  read Lee todo el contenido del archivo y lo pasa a la variable arc
                          #  readline lee lineas del archivo y los guarda en una lista con el /n tambien dentro de la lista
    print(arc) 