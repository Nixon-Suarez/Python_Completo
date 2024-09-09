nombre = ""
correo = ""
mensaje = ""

condicion_salida = ("CONTINUAR")


while condicion_salida == "CONTINUAR":
    nombre = input("Ingresa nombre: ")
    correo = input("ingresa correo: ")
    mensaje = input("ingresa mensaje: ")
    print(F"""
        mensaje enviado a, {nombre}, 
        destinatario, {correo}, 
        Mensaje: {mensaje} 
    """)
    condicion_salida = input("en caso de querer continuar escribe CONTUNUAR")
