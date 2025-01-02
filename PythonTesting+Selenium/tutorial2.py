from selenium.webdriver import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
import time 

def F2():
    service = Service(ChromeDriverManager().install()) 
    option = webdriver.ChromeOptions() 
    driver = Chrome(service=service, options=option)
    driver.get("https://coursecareers.com/explore/software-dev-fundamentals?a=techwithtim") 

    try:
        #* Presionamos un link text
        element = Wait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, '//*[@id="w-node-f85422c6-6945-c7e0-5abe-ce6502a2ffc1-ad11489d"]/div[2]/a')
        )
        element.click() 

    except ValueError as ve:
        print("Error en los datos proporcionados", ve)
        driver.quit()

    finally:
        time.sleep(10)
        driver.quit()

F2()