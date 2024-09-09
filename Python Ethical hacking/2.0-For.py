# 1
# nombres = ["elias", "javier", "juan", "david"]

# for nombre in nombres: 
#     print(f"Hola {nombre}")

# 2

# oracion = "Bienvenidos a hola mundo 🥵"

# for letra in oracion:
#     if letra.lower() not in 'aeiou ':
#         print(letra)

# 3

usuarios = ["adim", "root", "administrador"]
passwords = ["toor", "qwety", "12345", "contraseña"]

for usuario in usuarios:
    for password in passwords:
        if usuario == "administrador" and password == "12345":
            print("acceso permitido")
            print(f" {usuario}:{password}" )