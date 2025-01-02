
#! si esquiba el cloudflare pero no puede precionar botones ni meter info
from selenium.webdriver import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
import time 

USER = "diana.acuna@odl.com.co"
PASSWORD = "Odl123*"

option = webdriver.ChromeOptions() 
option.add_experimental_option("detach", True) #Para que no se cierre
option.add_experimental_option("excludeSwitches", ["enable-automation"]) #Quita el modo desarrollador 
option.add_experimental_option("useAutomationExtension", False) 
option.add_argument('--disable-blink-features=AutomationControlled') #Elimina lo que dice que es un navegador controlado 
option.add_argument('--disable-extensions') # elimina las extensiones 
option.add_argument('--no-sandbox') # elimina modo dev  
option.add_argument('--disable-infobars')  #elimina barra de informacion 
option.add_argument('--disable-dev-shm-usage')  #elimina el manejo de memoria 
option.add_argument('--disable-browser-side-navigation')  #elimina la navegacion 
option.add_argument('--disable-gpu')  #desactivar graficos 

option.add_argument("auto-open-devtools-for-tabs") #abre la consola

driver = Chrome(options=option)


driver.execute_script("window.open('https://uat.suplos.com/cliente', '_blank')") #en vez de abrir de una la pagina abre una ventana con dos paginas una con el sitio necestado y uno en blanco 
#☝️esto con el fin de que nos permita continuar como si fueramos personas  
wait = Wait(driver, 20) 

driver.switch_to.window(driver.window_handles[1]) #entramos a la pagina 1 ya que se abre primero la blanca 

driver.refresh()  #* esto refresca la pagina 

time.sleep(15)

# while True:
#     try:
#         # Verificar si el div "success" está visible
#         success_div = wait.until(EC.visibility_of_element_located((By.ID, "success")))
#         if success_div.is_displayed():
#             print("¡Operación exitosa!")
#             # Esperar los elementos antes de interactuar
#             user_field = wait.until(EC.visibility_of_element_located((By.NAME, "vUsuario")))
#             user_field.send_keys(USER)

#             password_field = wait.until(EC.visibility_of_element_located((By.ID, "contrasena")))
#             password_field.send_keys(PASSWORD)

#             login_button = wait.until(EC.element_to_be_clickable((By.ID, "vEntrada")))
#             login_button.click()
#             break
#     except:
#         print("Esperando el estado success...")

#     try:
#         # Verificar si el div "fail" está visible
#         fail_div = driver.find_element(By.ID, "fail")
#         if fail_div.is_displayed():
#             print("¡Error detectado! Reintentando...")
#             driver.refresh()
#     except:
#         pass  # Si no encuentra el div "fail", continúa esperando