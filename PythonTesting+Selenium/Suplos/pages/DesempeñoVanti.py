import time
from utils.dependencias_vanti import *
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

class DesempeñoVanti():
    #! ya que todos funcionan igual hacer una clase para ir a los modulos con un codigo similar a este 
    def ir_a_desempeño(self, mainPage):
        # Busaca en el beinvenidos 
        try:
            mainPage.click("XPATH", '//div[.//p[text()="Desempeño"]]/a')
        except:
            print(f"Error al buscar el elemento: intentando DESDE EL MENU ")
            mainPage.click("XPATH", "//a[span[text()='Desempeño']]")
        
    def Consultar_ejercicio(self, mainPage):
        mainPage.click("XPATH", "//a[contains(text(),'Consultar')]")
        mainPage.click("XPATH", "//td/i[@title='Detalle']", index=0)
        mainPage.click("XPATH", "//a[.//span[@data-original-title='Ver/Evaluar']]", index=0)
        time.sleep(2)
        mainPage.ValidarElementoExistente("XPATH", "//a[.//span[@data-original-title='Ver/Evaluar']]")
        
    def crear_ejercicio_desempeño(self, mainPage):
        mainPage.click("XPATH", "//a[contains(text(),'Crear ejercicio de evaluación')]")
        mainPage.write(TEXTO, "XPATH", '//div[contains(@class, "form-group") and .//label[text()="Periodo a evaluar (*)"]]/input')
        mainPage.write(TEXTO, "XPATH", '//div[contains(@class, "col-md-6") and .//label[text()="Nombre / Número (*)"]]/input')
        mainPage.click("XPATH", '//*[@id="start_date_evaluation_exercise"]/span/button')
        mainPage.click("XPATH", f"//td[contains(@class, 'today') and text()='{Dia_actual}']")
        mainPage.click("XPATH", '//*[@id="date_end_evaluation_exercise"]/span/button')
        mainPage.click("XPATH", f"//td[contains(@class, 'today') and text()='{Dia_actual}']")
        mainPage.click("XPATH", '//*[@id="divCreateExerciseDesempeno"]/div/div[2]/div/button')
        mainPage.click("XPATH", '//*[@id="divCreateExerciseDesempeno"]/div/div[2]/div/button[2]')
        mainPage.click("XPATH", '//*[@id="divExerciseDesempeno"]/div/div[1]/div/div/div/div[2]/div/div/div/div/button[3]')
        mainPage.ENTER_GENERAL()
        mainPage.ENTER_GENERAL()

    def ver_resultados(self, mainPage):
        mainPage.click("XPATH", "//a[contains(text(),'Aprobar')]")
        mainPage.ValidarElementoExistente("XPATH", "//td/i[@title='Detalle']")

    def evaluar_proveedores(self, mainPage):
        mainPage.click("XPATH", "//a[contains(text(),'Evaluar proveedor')]")
        mainPage.ValidarElementoExistente("XPATH", "//td/i[@title='Detalle']")

    def nueva_evaluacion(self, mianPage):
        pass