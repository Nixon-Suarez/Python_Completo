from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
class Persona(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click(self, tipoId, id, index=None):
        """
        Método para hacer clic en un elemento específico, con manejo de elementos ocultos o no encontrados.
        """
        by_attribute = getattr(By, tipoId)

        try:
            # Si no se especifica índice
            if index is None:
                element = Wait(self.driver, 10).until(
                    EC.element_to_be_clickable((by_attribute, id))
                )
                element.click()  # Intentar hacer clic

            else:
                # Si se especifica índice
                elements = Wait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((by_attribute, id))
                )
                if len(elements) > index:
                    element = elements[index]
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                    self.driver.execute_script("arguments[0].focus();", element)
                    Wait(self.driver, 10).until(EC.element_to_be_clickable(element)).click()
                else:
                    raise IndexError(f"No hay suficientes elementos para el índice {index}. Total elementos: {len(elements)}")

        except (TimeoutException, NoSuchElementException) as e:
            # Si el elemento no está visible o no se encuentra, intentar forzar visibilidad y clic por JS
            print(f"Elemento no encontrado o no clickeable: {id}. Intentando con JavaScript...")
            try:
                element = self.driver.find_element(by_attribute, id)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                self.driver.execute_script("arguments[0].style.display = 'block';", element)
                self.driver.execute_script("arguments[0].click();", element)
            except Exception as js_exception:
                raise Exception(f"No se pudo hacer clic con JavaScript: {js_exception}") from e

        except ElementClickInterceptedException:
            # Manejar caso donde el clic está bloqueado por otro elemento
            print(f"El clic fue interceptado por otro elemento. Intentando forzar...")
            self.driver.execute_script("arguments[0].click();", element)

        except Exception as e:
            # Captura cualquier otro error no específico
            raise Exception(f"Error al intentar hacer clic en el elemento: {e}")

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

    def handle_popup(self, tipoId, id, id_tituloPOPUP, id_contenidoPOPUP):
        """
        Detecta si un popup de SweetAlert2 aparece y extrae el mensaje.
        """

        by_attribute = getattr(By, tipoId)
        try:
            # Espera hasta que el popup sea visible (máximo 5 segundos)
            popup = Wait(self.driver, 5).until(
                EC.visibility_of_element_located((by_attribute, id))
            )
            
            # Extrae el título y contenido del mensaje
            title = popup.find_element(By.ID, id_tituloPOPUP).text
            content = popup.find_element(By.ID, id_contenidoPOPUP).text

            print(f"Popup detectado: {title} - {content}")

            # O lanza una excepción para detener la prueba
            raise Exception(f"Popup detectado: {title} - {content}")

        except TimeoutException:
            # Si el popup no aparece, simplemente continúa
            print("No se detectó ningún popup.")

        except NoSuchElementException as e:
            # Si algo falla en el manejo del popup
            print(f"Error al procesar el popup: {e}")
            raise

    def limpiarcache(self):
        # Borra todas las cookies
        self.driver.delete_all_cookies()
        # Recargar la página
        self.driver.refresh()

