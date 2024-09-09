 
class Auto:
    marca = 'Nisan'
    color = 'gris'
    puertas = '4'
    placa = ''

taxi = Auto() 
taxi.marca = 'susuki'
taxi.placa = 'abc-321'
taxi.color = 'Negro'
print(taxi.color)
print(taxi.placa)
print(taxi.marca)
print(taxi.puertas)

# ------------------------------------
class Persona:
    profesion = ""
    sueldo = 0

pedro = Persona()
juan = Persona()

pedro.profesion = "Doctor"
pedro.sueldo = 5000 
pedro.edad = 23
pedro.name = "Pedro"
juan.profesion = "Ingeniero"
juan.sueldo = 6000
juan.edad = 12
juan.name = "Juan"

print(f"{pedro.name} tiene {pedro.edad} años, es {pedro.profesion}")
print(f"{juan.name} tiene {juan.edad} años, es {juan.profesion}")


# asi👇 casi no se usa se usa asi ☝️
class Persona_A:
    doctor = "Pedro"
    sueldo = 7000


class Persona_B:
    ingeniero = "Juan"
    sueldo =  5000

print(Persona_B.sueldo)

