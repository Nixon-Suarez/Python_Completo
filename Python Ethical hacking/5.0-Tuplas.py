# es como una lista inmutable se declara con ()

tupla = ("Jorge", "Javier", "Roberto")

# tupla[0] = "pedro"   # No se puede porque las tuplas son inmutables.

print(tupla.count("Javier")) # de igual forma que en las listas sirve para ver cuantas veces aparece un valor
print(len(tupla)) # ver tamaño de la tupla
print(tupla.index("Javier")) # index = posicion 

for i in range(len(tupla)):
    print(tupla[i])