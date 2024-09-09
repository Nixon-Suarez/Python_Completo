#2 ¿ES UN ANAGRAMA?

# /*
# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS
#   las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
#  - Dos palabras exactamente iguales no son anagrama.


def sonAnagrmas(world1, world2):
    list = []
    if world1 == world2:
        return False

    elif len(world1) == len(world2):
        for char in world1:
            list.append(char)
        for char in world2:
            list.append(char)
    else:
        return False

    set1 = set(list)
    if len(set1) == len(world1):
        return True
     
world1 = "abcd"
world2 = "dcba"
if sonAnagrmas(world1, world2):
    print(f"Son anagramas: {world1} y {world2}")
else:
    print(f"No son anagramas: {world1} y {world2}")


#-------
def son_anagramas(palabra1, palabra2):
    if palabra1 == palabra2:
        return False

    if len(palabra1) != len(palabra2):
        return False

    set_palabra1 = sorted(palabra1) # sorted = funcion que ordena una lista
    set_palabra2 = sorted(palabra2)

    return set_palabra1 == set_palabra2 
   

# Ejemplo de uso
palabra1 = "abcd"
palabra2 = "dcba"

if son_anagramas(palabra1, palabra2):
    print(f"Son anagramas: {palabra1} y {palabra2}")
    
else:
    print(f"No son anagramas: {palabra1} y {palabra2}")

