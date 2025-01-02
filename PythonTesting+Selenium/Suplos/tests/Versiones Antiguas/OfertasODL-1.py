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
driver.find_element(By.XPATH, '//*[@id="divMenuModulosPrincipal"]/div[7]/div/a').click()
time.sleep(5)
#! cambiar el XPATH
driver.find_element(By.XPATH, '//*[@id="contenedorPrincipal"]/div[3]/div/div[3]/div/a[1]').click()
time.sleep(15)
# llenar la info de la ofertas
driver.find_element(By.XPATH, '//*[@id="tab_informacion_basica"]/div/div[1]/div[2]/div[2]/div/div/textarea').send_keys("Oferta de prueba Automatizada")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="tab_informacion_basica"]/div/div[1]/div[2]/div[3]/div/div/textarea').send_keys("Oferta de prueba Automatizada")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="tab_informacion_basica"]/div/div[1]/div[2]/div[4]/div[1]/div/select/option[3]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="tab_informacion_basica"]/div/div[1]/div[2]/div[4]/div[2]/div/select/option[2]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="tab_informacion_basica"]/div/div[1]/div[2]/div[4]/div[5]/div/select/option[2]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="tab_informacion_basica"]/div/div[1]/div[2]/div[4]/div[6]/div/input').send_keys("1000000")
time.sleep(5)
driver.find_element(By.XPATH, '').send_keys("1000000")
time.sleep(5)
# Tipo de contratación (*):
driver.find_element(By.XPATH, '//*[@id="tab_informacion_basica"]/div/div[1]/div[2]/div[4]/div[7]/div/select/option[2]').click()
time.sleep(5)
# Dirección (*):
driver.find_element(By.XPATH, '//*[@id="tab_informacion_basica"]/div/div[1]/div[2]/div[4]/div[8]/div/select/option[4]').click()
time.sleep(5)
# Compañía (*):
driver.find_element(By.XPATH, '//*[@id="tab_informacion_basica"]/div/div[1]/div[2]/div[4]/div[9]/div/select/option[2]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="divSolicitarRegistroOfertas"]/div/div/div/div/div/div/div/div[3]/div/div/button').click()


