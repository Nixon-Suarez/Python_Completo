
#* se declara con {}
nombres = ["Pedro", "Jorge", "Maria", "Ana"] #lista 
informacion = {"Nombre":"Pedro",  "Edad":24, "Especialidad":["programacion", "Ciberseguridad"]} #diccionario
#               ☝️llave   ☝️valor
#                   ⬇️ siempre se debe llamar la llave no el valor
print(informacion["Nombre"])
#*         ☝️accede a un valor por medio de la llave

for info in informacion:
    print(info) # esto imprime las laves 
    print(informacion[info]) # esto imprime la llave y el valor 

#* Reasignar un valor a una llave
informacion["Edad"] = 30
print(informacion)

#------------------------
for info in informacion:
    print(f"{info}:{informacion[info]}")

#-------------------
    
# for key in informacion:
#     if isinstance(informacion[key], list):
#         for i in informacion[key]:
#             print(f"{key}:{i}")
#     else:
#         print(f"{key}:{informacion[info]}")
    
#*------------Clear = Limpiar un diccionario-----------------
# informacion.clear() 
# print(informacion)
#*--------------Items = retorna clave y el valor------
print(informacion.items())
#----------------Keys = mostrar las llaves-------
print(informacion.keys())
#--------------Values = Mostrar los valores -----------
print(informacion.values())

#---------In = buscar un elemento--------------
# Busca llave
if "Edad" in informacion:
    print("Si se encuentra")
else: 
    print("No se encuentra")

#Busca valor

if "Pedro" in informacion.values():
    print("Si se encuentra")
else: 
    print("No se encuentra")