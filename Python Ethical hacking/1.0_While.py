pass_obs = input("Ingresa tu contraseña: ")
contador = 0 

while pass_obs != "xyz" and contador < 2:
    contador += 1
    print(f"numero de intentos  {contador} limite tres")
    print("la contraseña es incorrrecta")
    pass_obs = input("ingresa la contraseña: ")

if pass_obs == "xyz":
    print("acceso permitido")
else:
    print("no se permite el acceso")