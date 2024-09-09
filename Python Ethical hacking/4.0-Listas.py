# se declaran con []
nombres = ["jorge", "maria", "Pedro", "Ana", "Juan"]
# edades = [25, 23, 22]
# booleano = [True, False]
# lista = [["jorge", "maria", "Pedro"], [25, 23, 22]]

# for i in lista:
#     for j in i:
#         print(j)

#-------------
# lista_2d = [[["Jorge", 24],["Daniel", 25]],[["Ana", 21],["Maria",22]]]


# for i in lista_2d:
#     for j in i:
#         print(j)

#--------------------------

# mix = ["jorge", 24, True, 3.5, ["Adios", "Hola"]]

# for valor in mix:
#?     if isinstance(valor, list):#La función isinstance recibe como argumentos un objeto y una clase y devuelve True si el objeto es una instancia de dicha clase o de una subclase de ella.
#         for j in valor:
#             print(j)
#     else:
#         print(valor)

#----------------
# print(len(nombres))
# print(nombres[:-1])
# print(nombres.count("jorge")) # busca cuantas veces aparece un valor
# nombres.append("Rodrigo") #append sirve para agragar al final de la lista 
# nombres.insert(2,"Rodrigo") # insert te permite agragar un valor en cualquier parte especifica de la lista
# print(nombres.pop())#imprime el ultimo valor
# nombres.append("rodrigo")
# nombres.remove("rodrigo") #remove elimina el valor deseado pero siempre la primera aparicion del valor 

print(nombres.index("Rodrigo")) # index permite ver la posicion del valor

#---------------------------

# for i in nombres:
#     print(nombres[nombres.index(i)])
#     continue

#--------------------------

print(nombres) 
nombres.reverse() #reverse voltea la lista
nombres.sort() #sort Ordena en de manera alfabetica
print(nombres)