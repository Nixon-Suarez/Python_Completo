# Python Selenium Tutorial #3 - Page Navigating and Clicking Elements
#? control de excepciones, back y forward

from selenium.webdriver import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time 
 
USER = "nyamidsuarez@ucompensar.edu.co"
PASSWORD = "Pggnn010202.2006"

driver = Driver(uc=True)
url = "https://www.netacad.com/"
driver.uc_open_with_reconnect(url, 4)

# Metemos la ligica del T1 en un try y utilizamos wait en vez de time 
try:
    botonLogin = Wait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="styleguideheader"]/div/div/div[2]/div[7]/button'))
    )
    botonLogin.click()
    
    email = Wait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'username')) 
    )
    email.send_keys(USER)#pone el user name 
    # email.clear() # esto limpia el texto lo deja en blanco
    email.send_keys(Keys.RETURN) # le da enter 

    contrasena = Wait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    contrasena.send_keys(PASSWORD)
    contrasena.send_keys(Keys.RETURN) 

    menu = Wait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="marketplace-container"]/div[1]/div/div/div/div/div[1]/div/div[2]/div[3]/div/div/div/div[1]/div/button'))
    )
    menu.click()

    time.sleep(10)

    driver.back() # hace que vuelvas a la pagina anterior ⬅️
    driver.back()
    driver.forward() # hace que vuelvas a la pagina que estabas hace la funcionalidad de este boton en el navegador ➡️

    time.sleep(10)
except Exception as e:
    print(e)
    driver.quit()

finally:
    time.sleep(5)
    driver.quit()
