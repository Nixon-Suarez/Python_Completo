
def reporte(texto):
    archivo  = open("datosPruebaVanti.txt", "a", encoding= 'latin-1')
    archivo.write(f"{texto}")
    archivo.close()