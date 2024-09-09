# hasheable = va tener un valor unico
#* no permiten satos duplicados
# mutable 
# no Ordenada 

lista_numeros = [1,2,3,4,5]
set1 = set(lista_numeros)

set1.add(1)
set1.add(2)
set1.add(3)
set1.add(3)
set1.add(6)

print(set1)

pertenece = 1 in set1

print(pertenece)

frutas = {
    'manzana',
    'banano',
    'pera',
    'uva'
}

