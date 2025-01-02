# Python Selenium Tutorial #2 - Locating Elements From HTML 
#? escribir y hacer click en elementos
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

#ir al login 
driver.find_element(By.XPATH, '//*[@id="styleguideheader"]/div/div/div[2]/div[7]/button').click()
time.sleep(5)
# login
email = driver.find_element(By.ID, 'username')
email.send_keys(USER) #pone el usuario
email.send_keys(Keys.RETURN) # le da enter 
time.sleep(3)
contrasena = driver.find_element(By.ID, 'password')
contrasena.send_keys(PASSWORD) #pone la contraseña
time.sleep(3)
contrasena.send_keys(Keys.RETURN) # le da enter
time.sleep(10)
driver.quit()

