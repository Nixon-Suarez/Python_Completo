from utils.dependenciasRegistro import *

class RegistraeseProveedores():
    def botonRegistrarse(self, mainPage):
        mainPage.click("XPATH", "/html/body/div[2]/section/section/div[2]/div[2]/div[1]/div[3]/div[2]/div/button")
        mainPage.click("XPATH", f'//option[text()="{Pais[1]}"]')
        mainPage.click("XPATH", f'//option[text()="{Tipo_persona[0]}"]')
        
        mainPage.write(CC, "ID", 'register-form-doc')
        mainPage.write(Nombre, "ID", 'register-form-name')
        mainPage.write(Indicativo[1], "ID", 'register-form-phone-ind')
        mainPage.write(TELEFONO, "ID", 'register-form-phone')
        mainPage.write(Nombre, "ID", 'register-form-contact')
        mainPage.write(email, "ID", 'register-form-email')
        mainPage.write(email, "ID", 'register-form-email2')

        mainPage.click("CSS_SELECTOR", "ins.iCheck-helper")
        mainPage.click("ID", "btnSubmitRegCol")