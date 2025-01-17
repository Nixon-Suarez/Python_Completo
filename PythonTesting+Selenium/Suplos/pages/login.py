# from utils.dependencias_ODL import *
from utils.dependencias_ocensa import *

class login(): 
    def loginSuplos(self, mainPage):
        try:
            N=29
            mainPage.write(USER[N], "NAME", 'vUsuario')
            mainPage.write(PASSWORD, "NAME", 'vClave')
            # Seleccion suplos
            #                                                ⬇️ Como el Xpath es variable sele puso el Value para seleccionar suplos 
            mainPage.click("XPATH", '//*[@id="inpSelectEmpresaLogin"]/option[@value="0fhb"]')
            # hace lo mismo☝️👇
            # mainPage.click('//*[@id="inpSelectEmpresaLogin"]/option[text()="SUPLOS"]', "XPATH")
            mainPage.click("NAME", 'vEntrada')
            print(f"login con usuarios {USER[N]}")

        except Exception as e:
                print(f"Error en loginSuplos: {e}")