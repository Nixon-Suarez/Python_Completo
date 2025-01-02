# Python Selenium Tutorial #5 - UnitTest Framework (Part 1)
#? OOP y assert 
#! nota como no usamos como tenemos que usar la instalacion tenemos que usar la importacion de By nunca el find_element_by_name

import unittest
from selenium import webdriver
import page 
from selenium.webdriver import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class PythonOrgSearch(unittest.TestCase):

    def setUp(self): #aqui definimos lo que vamos a utilizar mas adelante Variables...
        print("setUp")
        self.service = Service(ChromeDriverManager().install())
        self.option = webdriver.ChromeOptions()
        self.driver = Chrome(service=self.service, options=self.option)
        self.driver.get("http://www.python.org")

    def test_search_python(self):
        #llamamos al metodo Main de page y si esto da verdadero continua con la siguente validacion 
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        #Con el metodo search_text_element(SearchTextElement) validamos si pycon esta 
        mainPage.search_text_element = "pycon"
        # llamamos al metodo click_go_button para dar click si el elemento existe 
        mainPage.click_go_botton()
        #validamos si el texto existe en la pagina
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found() #y si esto se ejecuta exitosamente da como bien a la prueba



    # def test_example(self):
    #     print("test")
    #     assert True #if the condition on the right side -> valida si el test se ejecuto de buena manera True se ejecuto correcto false lo contrario 

    # def test_example_2(self):
    #     print("test")
    #     assert False

    # def not_a_test(self):
    #     print("This wont work") no funciona ya que no tiene a test de primera por lo cual no se ejecuta 

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
