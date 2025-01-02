#Va con el main
#? tiene la funcion de comparar el titulo y darle click a un elemento
from locator import*
from element import BasePageElement


class SearchTextElement(BasePageElement):
    locator = "q"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver 

class MainPage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title #valida si Python esta en el titulo de la pagina 
    
    def click_go_botton(self): #busca elemento y llama a la funcion go botton del archivo locator de la clase MainPageLocator 
        element = self.driver.find_element(*MainPageLocator.GO_BUTTON)
        element.click() 

class SearchResultPage(BasePage):  # Correctly inherit from BasePage

    def is_result_found(self):
        return "No results found." not in self.driver.page_source # Validate if there are results