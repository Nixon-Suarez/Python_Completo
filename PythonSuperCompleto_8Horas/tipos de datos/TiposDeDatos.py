# Datos simples

texto = "string" #str
enteros = 1 #int 
flotante = 1.5 #float
booleanos = False, True #bool

# Datos Compuestos
# --------------------
lista = ["ffff", True, 3, "popo"] #list
        #  0        1  2     4
lista[0] = "armando"
print(lista[0])
# ---------------------
tupla = ("a", 1, True) #tuple = inmutable
       #  0    1   2   
print(tupla[2])
# ---------------------
sets = {"a", 1, True, "a", "a", "a"} #set = inmutable-desordenada-No repetidos-no se accede por el indice accede por bucle
print(sets)
# ---------------------
diccionario = {"nombre": "armando", "edad": 30, "activo":True} #dict = Key : Value - accede por la llave
print(diccionario["activo"])
