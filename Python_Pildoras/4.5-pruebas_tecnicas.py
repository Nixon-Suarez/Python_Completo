# desbes invertir una lista sin utilizar la funcion reverse 

def reverse_lista(lista):
    inicio = 0
    fin = len(lista) -1 
    while inicio < fin:
        lista[inicio], lista[fin] = lista[fin], lista[inicio]

        inicio += 1
        fin -= 1
    return lista

lista_original =[1, 2, 3, 4, 5]
print(reverse_lista(lista_original))