lista_numeros = [1, 2, 3, 4]
lista_nombres = ["Edward", "Carlos", "Juan"]
lista_bool = [True, False]

print(lista_numeros[2])
lista_numeros[2] = 100
print(lista_numeros)

#--------list funcion que tranforma a lista 
tupla = (1, 2, 3)
lista_n = list(tupla)
print(type(lista_n))

#-------append = agrgar elementos alfinal de la lista
lista_numeros.append(5)
lista_numeros.append(5)
print(lista_numeros)

#--------count = cuanta cuantos elementos del mismo vaor se encuentran en la lista
print(lista_numeros.count(5))

#-----exetnd = extiende la lista con elementos que se pasan como argumento
lista_extendida = [100, 101]
                        #⬇️se pasa como argumento la lista extendida 
lista_numeros.extend(lista_extendida)
print(lista_numeros)

#-----index = busca un elemento y retorna su indice 
print(lista_numeros.index(5))

#----insert = inserta elementos en cualquier lugar de la lista 
print(lista_numeros)
#                    ⬇️ubicacion, nuevo valor ha agregar 
lista_numeros.insert(0, 300)

#--- pop = extrae elementos de la lista y los retorna
#                      ⬇️ si esta vacio extrae el ultimo valor de la lista sino el valor con la localizacion adentro
print(lista_numeros.pop())
print(lista_numeros)

#--- remove = elimina los elementos por el valor indicado en el argumento
lista_numeros.remove(100)
print(lista_numeros)

#--- reverse = reversa la lista
lista_numeros.reverse()
print(lista_numeros)

# -- sort = organiza los elementos 
lista_numeros.sort()
print(lista_numeros)

#-- clear = limpia toda la lista
lista_numeros.clear()
print(lista_numeros)
