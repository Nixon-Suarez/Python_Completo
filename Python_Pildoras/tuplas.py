mi_tupla = (1, False, "Edward", 0.123)
#           0     1      2       3
print(mi_tupla[3]) # accede a un valor 

def retornar_estudiante():
    return "Edward", 12, True

nombre, edad, activo = retornar_estudiante()
# ☝️esto es lo mismo que hacer esto 👇
# pero peor mas largo 
# tuplaEstudiante = retornar_estudiante()
# print(tuplaEstudiante)

# nombre = tuplaEstudiante[0]
# edad = tuplaEstudiante[1]
# activo = tuplaEstudiante[2]

#?----------one-line swapping 
# reasignar nuevos valores al de la variable_1 darle 2.0 y a la variable_2 1.0
variable_1 = 1.0
variable_2 = 2.0

# variabletemporal = variable_1
# variable_1 = variable_2
# variable_2 = variabletemporal
# 👇ahora utilizando one-line swapping 
variable_1, variable_2 = variable_2, variable_1

print(variable_1, variable_2)


