from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

class BasePage():
    def __init__(self, driver): 
        self.driver = driver  # Llama al constructor de BasePage
        
    #escribe en la pagina
    #tambien sube un archivo -> en esta caso object tiene que ser la direccion del archivo
    def write(self, obj, tipoId, id): 
        by_attribute = getattr(By, tipoId)
        element = Wait(self.driver, 10).until(
            EC.element_to_be_clickable((by_attribute, id)) 
        ) 
        element.send_keys(obj)

    #lee la pagina
    def read(self, tipoId, id):
        by_attribute = getattr(By, tipoId)
        InfoImpor = Wait(self.driver, 10).until(
            EC.presence_of_all_elements_located((by_attribute, id)) #espera hasta que se encuantra el elemento
        )
        for element in InfoImpor: 
            print(element.text)

    #clickea en la pagina
    def click(self, tipoId, id):
        by_attribute = getattr(By, tipoId)
        element = Wait(self.driver, 10).until(
            EC.element_to_be_clickable((by_attribute, id))
        )
        element.click()

    def Upload(self, obj, tipoId, id):
        if not os.path.exists(obj):
            raise FileNotFoundError(f"El archivo '{obj}' no existe.")
        
        by_attribute = getattr(By, tipoId)
        element = Wait(self.driver, 20).until(
            EC.visibility_of_element_located((by_attribute, id)) 
        )
        element.send_keys(obj)

#id -> el identificador ejemplo "Botton1" o el expath que seria la direccion 
#tipoId -> el tipo de identificador que se va a usar ejemplo By.ID o By.XPATH
#obj -> el objeto que se va a usar en el send key ejemplo "hola" o "C:/Users/Usuario/Desktop/imagen.jpg" 