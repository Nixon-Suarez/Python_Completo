from utils.dependencias import *

class login():
    def loginSuplos(self, mainPage):
        mainPage.write(USER , "NAME", 'vUsuario')
        mainPage.write(PASSWORD, "NAME", 'vClave')
        # Seleccion suplos
        #                                                ⬇️ Como el Xpath es variable sele puso el Value para seleccionar suplos 
        mainPage.click("XPATH", '//*[@id="inpSelectEmpresaLogin"]/option[@value="0fhb"]')
        # hace lo mismo☝️👇
        # mainPage.click('//*[@id="inpSelectEmpresaLogin"]/option[text()="SUPLOS"]', "XPATH")
        mainPage.click("NAME", 'vEntrada')