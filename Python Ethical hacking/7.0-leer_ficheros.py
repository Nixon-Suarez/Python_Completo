# read solo permite  leer un archivo de texto y mostrar su contenido en la consola si ya existen 
#            ⬇️➡️ abre el archivo o lo llama
#            ⬇️                            ⬇️detecta el mayor tipo de datos 
file_user = open("7.2-user.txt","r",encoding= 'latin-1')
#                                  ☝️se encarga de la deteccion de caracteres  
usuarios = file_user.read().split("\n") #?la funcion read llama la informacion en archivo user.txt el cualo esta almacenado en la variable file_user
print(usuarios)#             ☝️split separa cadenas de texto dependiendo del parametro que se le coloque (\n) y los almacena en listas

file_pass = open("7.1-pass.txt","r", encoding= 'latin-1')
passwords = file_pass.read().split("\n")
print(passwords)

for usuario in usuarios:
    for password in passwords: 
        if usuario == "admin" and password == "qwerty":
            print(f"Se encontraron las credenciales {usuario}:{password}")
            break
        else:
            print(f"intento fallodo {usuario}:{password}....")

file_user.close() # cierra el archivo 
file_pass.close()


