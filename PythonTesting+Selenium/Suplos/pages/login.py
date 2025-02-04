# from utils.dependencias_ODL import *
from utils.dependencias_vanti import *
# from utils.dependencias_ocensa import *
from pages.reporte import reporte
import time

class login():
    def loginSuplos(self, mainPage, N):
        try:
            mainPage.write(USER[N], "NAME", 'vUsuario')
            mainPage.write(PASSWORD, "NAME", 'vClave')
            # Seleccion suplos
            #                                                ⬇️ Como el Xpath es variable sele puso el Value para seleccionar suplos 
            mainPage.click("XPATH", '//*[@id="inpSelectEmpresaLogin"]/option[@value="0fhb"]')
            # hace lo mismo☝️👇
            # mainPage.click('//*[@id="inpSelectEmpresaLogin"]/option[text()="SUPLOS"]', "XPATH")
            mainPage.click("NAME", 'vEntrada')
            mainPage.handle_popup("CLASS_NAME", "swal2-popup", "swal2-title", "swal2-content")
            usuariologin = (f"login con usuarios {USER[N]}\n")
            print(usuariologin)
            reporte(usuariologin)
            time.sleep(2)
            return True

        except Exception as e:
                error = (f"Error en loginSuplos: {e} \n")
                print(error)
                reporte(error)
                return False
