import unittest
from seleniumbase import Driver
from pages.Persona import Persona
from pages.OfertasRFI import ofertasRFI
from pages.login import login
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.comentarios_proveedores_Ocensa import comentarios_proveedores_Ocensa
from pages.RegistraeseProveedores import RegistraeseProveedores
from pages.DesempeñoVanti import DesempeñoVanti
import time
from pages.reporte import reporte
# from utils.dependencias_ocensa import *
from utils.dependencias_vanti import *

class Tests(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para cada prueba"""
        print("Iniciando configuración")
        self.driver  = Driver(uc=True)
        self.url = "https://uat.suplos.com/cliente" #"https://capacitacion.suplos.com/proveedores/" 
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    # !implementar esta logica para todos los test meterlo en una funcion 

    def test_vantiPerfiles(self): 
        N = 0
        for _ in USER:
            intentos = 5  # Número máximo de reintentos
            intento_actual = 0
            login_exitoso = False
            reporte(f"{N}----\n")

            while intento_actual < intentos and not login_exitoso:
                main_page = Persona(self.driver)
                print("paso 1")
                Login = login()
                print("paso 2")
                time.sleep(2)

                login_exitoso = Login.loginSuplos(main_page, N)
                print("paso 3")

                if login_exitoso:
                    time.sleep(2)

                    DesempeñoVantiPruebas = DesempeñoVanti()
                    print("paso 4") 
                    Persona.ejecutar_seguro(DesempeñoVantiPruebas.ir_a_desempeño, main_page)
                    Verresultados = Persona.ejecutar_seguro(DesempeñoVantiPruebas.validarver_resultados, main_page)
                    Verevaluar = Persona.ejecutar_seguro(DesempeñoVantiPruebas.validarevaluar_proveedores, main_page)
                    Vervalidar = Persona.ejecutar_seguro(DesempeñoVantiPruebas.validarConsultar_ejercicio, main_page)
                    Vercrear = Persona.ejecutar_seguro(DesempeñoVantiPruebas.validarCreardesempeño, main_page)

                    # # DesempeñoVantiPruebas.crear_ejercicio_desempeño(main_page)
                    # # DesempeñoVantiPruebas.ir_a_desempeño(main_page)
                    # Persona.ejecutar_seguro(DesempeñoVantiPruebas.validarCreardesempeño, main_page)
                    # Persona.ejecutar_seguro(DesempeñoVantiPruebas.Consultar_ejercicio, main_page)
                    # Persona.ejecutar_seguro(DesempeñoVantiPruebas.ir_a_desempeño, main_page)
                    # Persona.ejecutar_seguro(DesempeñoVantiPruebas.evaluar_proveedores, main_page)
                    # Persona.ejecutar_seguro(DesempeñoVantiPruebas.ir_a_desempeño, main_page)
                    # Persona.ejecutar_seguro(DesempeñoVantiPruebas.ver_resultados, main_page)
                    # Persona.ejecutar_seguro(DesempeñoVantiPruebas.ir_a_desempeño, main_page)
                    
                    Persona.ejecutar_seguro(DesempeñoVantiPruebas.cerrarSesion, main_page)
                    exito = (""" paso 5 - se ejecuto exitosamente
                            ---------------------------\n""")
                    reporte(exito)
                    N += 1  # Incrementar solo si el login fue exitoso
                    time.sleep(5)
                else:
                    intento_actual += 1  # 🔹 Incrementar intentos solo si falla
                    print("paso 6 (entro al else)")
                    print(f"Intento {intento_actual} fallido para {USER[N]}. Reintentando...")

                    if intento_actual < intentos:
                        time.sleep(2)
                        self.tearDown()
                        self.setUp()
                    else:
                        intentos = (f"Se alcanzó el máximo de intentos para {USER[N]}. Saltando al siguiente usuario. \n")
                        print(intentos)
                        reporte(intentos)
                        N += 1
            
        reporte("Finalizado-------------------------------------")

    # def test_crear_oferta_rfi(self):
    #     main_page = Persona(self.driver)

    #     Login = login()
    #     Login.loginSuplos(main_page, 0)

    #     OfertaRFIPrueba = ofertasRFI()
    #     OfertaRFIPrueba.ir_a_Ofertas_RFI(main_page)
    #     OfertaRFIPrueba.info_basica(main_page)
    #     OfertaRFIPrueba.configurar_cronograma(main_page)
    #     OfertaRFIPrueba.guardar_inicial(main_page)
    #     OfertaRFIPrueba.definir_inquietudes(main_page)
    #     OfertaRFIPrueba.programar_visita(main_page)
    #     OfertaRFIPrueba.documentacion(main_page) 
    #     OfertaRFIPrueba.informacion(main_page)
    #     OfertaRFIPrueba.Guardado_general(main_page)
    #     OfertaRFIPrueba.criterios(main_page)
    #     OfertaRFIPrueba.cuadro_economico(main_page)
    #     OfertaRFIPrueba.usuarios_internos(main_page)
    #     OfertaRFIPrueba.Guardado_general(main_page)

    # def tests_ocensa_cometario_proveedor(self):
    #     main_page = Persona(self.driver)
    #     N = 0
    #     time.sleep(2)
    #     Login = login()
    #     Login.loginSuplos(main_page, N)
    #     PruebaCrearComentario = comentarios_proveedores_Ocensa()
    #     PruebaCrearComentario.ir_a_proveedores(main_page)
    #     PruebaCrearComentario.ver_detalle_proveedor(main_page)
    #     PruebaCrearComentario.ir_pestaña_gestion_profecionales(main_page)
    #     for _ in range(1):
    #         PruebaCrearComentario.precionar_agregar_gestion(main_page)
    #         PruebaCrearComentario.gestion_profecionales(main_page)
    #         time.sleep(2)

    # def test_registro(self):
    #     main_page = Persona(self.driver)
    #     time.sleep(2)
    #     PruebaRegistro = RegistraeseProveedores()
    #     PruebaRegistro.botonRegistrarse(main_page)

    def tearDown(self):
        """Cierre del driver al finalizar cada prueba"""
        if self.driver:
            time.sleep(5) 
            self.driver.quit()

if __name__ == "__main__":
    unittest.main() 
