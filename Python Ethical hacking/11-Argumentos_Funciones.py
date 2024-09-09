
from time import sleep #bien
def h1(titulo):
    titulo = titulo.upper()
    titulo = "<h1>"+titulo+"</h1>"
    return titulo
#bien

def h2(subtitulo):
    subtitulo = subtitulo.title()
    subtitulo = f"<h2> {subtitulo} </h2>"
    return subtitulo

#bien

def p(parrafo):
    texto = parrafo.lower()
    texto = "<p>{}</p>".format(texto)
    return texto
#bien

def main():
    index = open("index.html", "a")
    index.write("<html><head> </head><body>")
    while True:
        titulo = input("Ingrese un titulo\n>>")
        index.write(h1(titulo))
        for _ in range(2):
            subtitulo = input("Ingrese el Subtitulo\n>>")
            index.write(h2(subtitulo))
            parrafo = input("Ingrese un parrafo \n>>")
            index.write(p(parrafo))
        continuar = input("¿Desea Continuar? Y = Yes N = No\n")
        continuar = continuar.upper()
        if continuar == 'N':
            print("Saliendo...")
            break
    index.write("</body></html>")
    index.close()
#bien
#? __main__ es el nombre del entorno en el cual se ejecuta el código de máximo nivel.
#? «Código de máximo nivel» es el primer módulo de Python especificado por el usuario que empieza a ejecutarse. 
#?Es «de máximo nivel» porque importa todos los demás módulos que necesita el programa.
if __name__ == '__main__':
    try:
        main()
    except  KeyboardInterrupt:
        sleep(1)
        exit()