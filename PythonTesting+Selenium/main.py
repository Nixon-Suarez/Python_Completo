from selenium.webdriver import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
import time 

USER =  [
"standard_user",
"locked_out_user",
"problem_user",
"performance_glitch_user",
"error_user",
"visual_user"]

PASSWORD = "secret_sauce"

def main():
    service = Service(ChromeDriverManager().install()) # aqui instalamos chromeDriver
    option = webdriver.ChromeOptions() # con esto se habilita el paso de parametros al navegador 
    # option.add_argument("--headless") #esto hace que se ejecute sin abrir la ventana 
    option.add_argument("--window-size=1920, 1080") # aqui se pone el tamaño de la ventana del navegador
    driver = Chrome(service=service, options=option)
    driver.get("https://www.saucedemo.com/") # aqui se abre la pagina que queremos

    #*login
    #                                   👇esto dice que va buscar el por el ID 
    user_input = driver.find_element(By.ID, "user-name") # accede al elemento del HTML con el ID user-name y lo almacenamos un una variable 
    user_input.send_keys(USER[0]) #escribimos en el user-name el usuario 1
    #Mas corto 
    driver.find_element(By.ID, "password").send_keys(PASSWORD) #lo mismo de arriba pero con la contraseña y en una misma linea
    driver.find_element(By.ID, "login-button").click() # lo mismo accedemos al boton que tiene el Id login-button y le hacemos click

    #*Compras
    #                                        👇esto dice que va buscar el por el Name
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()

    #*Carrito
    #Asi se selecciona cuando no tiene ni id ni name 
    # se preciona en click derecho sobre el elemento html y le damos copy -> copy full XPath
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click()

    #*Pagar
    # Asi se selecciona con Class
    driver.find_element(By.ID, "checkout").click()

    #*Ingresar datos pago
    Fname_input = driver.find_element(By.ID, "first-name").send_keys("En este caso") 
    Lname_input = driver.find_element(By.ID, "last-name").send_keys("Algo Aleatorio") 
    Postal_input = driver.find_element(By.ID, "postal-code").send_keys("1234") 
    driver.find_element(By.ID, "continue").click() 

    #*Finalizamos la compra
    driver.find_element(By.ID, "finish").click()

    time.sleep(10)
    driver.quit()# aqui cerramos el driver
    

if __name__ == "__main__":
    main()

