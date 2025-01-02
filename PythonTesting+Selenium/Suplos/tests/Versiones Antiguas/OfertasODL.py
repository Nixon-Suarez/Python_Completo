from seleniumbase import Driver
from selenium.webdriver.common.by import By
import time 

USER = "diana.acuna@odl.com.co"
PASSWORD = "Odl123*"

driver = Driver(uc=True)
url = "https://uat.suplos.com/cliente"
driver.uc_open_with_reconnect(url, 4)
driver.uc_gui_click_captcha()
time.sleep(17)

#login
driver.find_element(By.NAME, 'vUsuario').send_keys(USER)
driver.find_element(By.NAME, 'vClave').send_keys(PASSWORD)
driver.find_element(By.XPATH, '//*[@id="inpSelectEmpresaLogin"]/option[3]').click()
driver.find_element(By.NAME, 'vEntrada').click()
time.sleep(10)
#Ofertas 
driver.find_element(By.XPATH, '//*[@id="divMenuModulosPrincipal"]/div[4]/div/a').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="contenedorPrincipal"]/div[3]/div/div[3]/div/a[1]').click()
time.sleep(15)
driver.quit()
# llenar la info de la ofertas
