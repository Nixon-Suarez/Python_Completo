from pages.DesempeñoVanti import DesempeñoVanti

class testsVanti():
    def test_vantiPerfiles(self, main_page):

        DesempeñoVantiPruebas = DesempeñoVanti()

        DesempeñoVantiPruebas.ir_a_desempeño(main_page)
        DesempeñoVantiPruebas.validarver_resultados(main_page)
        DesempeñoVantiPruebas.validarevaluar_proveedores(main_page)
        DesempeñoVantiPruebas.validarConsultar_ejercicio(main_page)
        DesempeñoVantiPruebas.validarCreardesempeño(main_page)
        DesempeñoVantiPruebas.cerrarSesion(main_page) 