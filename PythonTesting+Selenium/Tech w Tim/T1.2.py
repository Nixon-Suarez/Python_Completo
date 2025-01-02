
#? Como copiar elementos de la web 
from selenium.webdriver import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
import time 

def F1():
    service = Service(ChromeDriverManager().install()) 
    option = webdriver.ChromeOptions() 
    driver = Chrome(service=service, options=option)
    driver.get("https://webscraper.io/") 

# Este try esta hecho para evitar errores por que se ejecute muy rapido y por alguna excepcion 
    try:#             👇
        InfoImpor = Wait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "col-lg-8")) #espera hasta que se encuantra el elemento
                                                    #☝️ col-lg-8 es un div completo entonces va a tomar todo el texto que este en ese div 
        )
        for element in InfoImpor: 
            print(element.text) #imprimimos el texto de la variable InfoImpor


    except ValueError as ve:
        print("Error en los datos proporcionados", ve)
        driver.quit()

    finally:
        time.sleep(10)
        driver.quit()


F1()