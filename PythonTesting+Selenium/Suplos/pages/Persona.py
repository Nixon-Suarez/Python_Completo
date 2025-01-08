from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class Persona(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

#! Probar con los valores de las variables y despues probar con otros valores 
    value = "Documentación jurídica"
    id_seleccion_tr = '//tr[@class="vertical-middle"]'
    numero_columna = 6
    def Write_iterable_objects(self, value, id_seleccion_tr, numero_columna): #?escribe en el option con el valor "value" cuando un elemento "element" se va a repetir N veces, selecciona este elemento las veces que parezca
        # Esperar a que los elementos estén presentes (opcional, si la página tarda en cargar)
        self.driver.implicitly_wait(10)

        # Encuentra todas las filas que contienen el `<tr>` con la clase 'vertical-middle'
        filas = self.driver.find_elements(By.XPATH, id_seleccion_tr)

        # Iterar sobre cada fila y seleccionar "value" en el segundo `<select>`
        for fila in filas:
            try:
                # Localizar el segundo `<select>` dentro de esta fila
                select_element = fila.find_element(By.XPATH, f'.//td[{numero_columna}]//select')  # `td[6]` es la columna que contiene el `<select>`
                
                # Convertir el elemento en un objeto de tipo Select para manipularlo
                select = Select(select_element)
                
                # Seleccionar la opción "value" por su texto visible
                select.select_by_visible_text(value)
                
                # O, alternativamente, selecciona por el valor del atributo ("value"="30")
                # select.select_by_value("30")
                
            except Exception as e:
                print(f"No se pudo seleccionar en una fila: {e}")