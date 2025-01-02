# Python Selenium Tutorial #4 - ActionChains & Automating Cookie Clicker!
#? como hacer mas de un click y almacenar la cantidad en una lista paradespues usarlo

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = Driver(uc=True)
url = "https://orteil.dashnet.org/cookieclicker/"
driver.uc_open_with_reconnect(url, 4) 

driver.implicitly_wait(5)

try:
    driver.find_element(By.ID, 'langSelect-EN').click()
    time.sleep(10)

    cookie = driver.find_element(By.ID, 'bigCookie')
    cookie_count = driver.find_element(By.ID, 'cookies')
    items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]
    #☝️ este for crea str de productPrice1 y productPrice0 y pone que inicie en 1 y que no sea menor a 0

    actions = ActionChains(driver)

    for i in range(5000):
        actions.click(cookie).perform()
        count = int(cookie_count.text.split(" ")[0]) # cuenta las veces que se han precionado la galleta y se convierte en un entero 
        for item in items:
            value = int(item.text)
            if value <= count:
                upgrade_actions = ActionChains(driver) #Actualiza para saber que si vas al lugar correcto
                upgrade_actions.move_to_element(item) #mueve el cursor al elemento item
                upgrade_actions.click().perform() #le da click


except Exception as e:
    print(e)
    driver.quit()

finally:
    time.sleep(5)
    driver.quit()

#* Otra solucion para oprimir mas de una vez 
# from selenium.webdriver.common.by import By
# from seleniumbase import Driver
# import time

# Configuración del controlador
# driver = Driver(uc=True)
# url = "https://orteil.dashnet.org/cookieclicker/"
# driver.uc_open_with_reconnect(url, 4) 

# driver.implicitly_wait(5)

# try:
#     # Seleccionar idioma
#     driver.find_element(By.ID, 'langSelect-EN').click()
#     time.sleep(10)  # Esperar que cargue la página

#     # Seleccionar el botón de la cookie
#     cookie = driver.find_element(By.ID, 'bigCookie')

#     # Hacer clic en la cookie 5000 veces
#     for i in range(5000):
#         cookie.click()

# except Exception as e:
#     print(e)

# finally:
#     time.sleep(5)
#     driver.quit()





