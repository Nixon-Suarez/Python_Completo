import unittest
from seleniumbase import Driver
from pages.Persona import Persona
from pages.OfertasRFI import ofertasRFI
from pages.login import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCrearOfertaRFI(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para cada prueba"""
        print("Iniciando configuración")
        self.driver = Driver(uc=True)
        self.url = "https://uat.suplos.com/cliente"
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def test_crear_oferta_rfi(self):
        main_page = Persona(self.driver)

        Login = login()
        Login.loginSuplos(main_page)

        OfertaRFIPrueba = ofertasRFI()
        OfertaRFIPrueba.ir_a_Ofertas_RFI(main_page)
        OfertaRFIPrueba.info_basica(main_page)
        OfertaRFIPrueba.configurar_cronograma(main_page)
        OfertaRFIPrueba.guardar(main_page)
        OfertaRFIPrueba.definir_inquietudes(main_page)
        OfertaRFIPrueba.programar_visita(main_page)
        OfertaRFIPrueba.documentacion(main_page)
        OfertaRFIPrueba.informacion(main_page)

    def tearDown(self):
        """Cierre del driver al finalizar cada prueba"""
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
