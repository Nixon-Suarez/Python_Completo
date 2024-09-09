#append

archivo  = open("mis_datos_append.txt", "a", encoding= 'latin-1')
cantidad = int(input("¿Cuantas personas registraras?\n"))

for  i in range (cantidad):
    nombre = input("Ingrese su nombre: \n")
    apellido = input("Ingresar su apellido: \n")
    edad = int(input("Ingrese  su edad: \n "))
    sexo = str(input("Ingrese su sexo: \n [H]. Hombre \n [M].mujer \n")).upper()
    carrera = input("Ingrese su carrera: \n")

    while sexo != "H" and sexo != "M":
        sexo = str(input("Ingrese su sexo: \n [H]. Hombre \n [M]. mujer \n")).upper()

    if edad >= 30 and sexo == "H":
        archivo.write(f" HOla Señor{nombre} {apellido} \n")
        archivo.write(f" tiene {edad} años \n")
        archivo.write(f" estudio la carrera de {carrera} \n")

    elif edad < 30 and sexo == "H":
        archivo.write(f"Hola joven {nombre} {apellido}")
        archivo.write(f" tiene {edad} años \n")
        archivo.write(f" estudio la carrera de {carrera} \n")

    elif edad >= 30 and sexo == "M":
        archivo.write(f"Hola Señora {nombre} {apellido}")
        archivo.write(f" tiene {edad} años \n")
        archivo.write(f" estudio la carrera de {carrera} \n")
    elif edad < 30 and sexo == "M":
        archivo.write(f"Hola señorita {nombre} {apellido}")
        archivo.write(f" tienes {edad} años \n")
        archivo.write(f" estudio la carrera de {carrera} \n")
    else:
        pass

    archivo.write("*"*10)
    archivo.write("\n")

archivo.close()
