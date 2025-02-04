from pages.OfertasRFI import ofertasRFI

class testsODL():
    def test_crear_oferta_rfi(self, main_page):

        OfertaRFIPrueba = ofertasRFI()
        OfertaRFIPrueba.ir_a_Ofertas_RFI(main_page)
        OfertaRFIPrueba.info_basica(main_page)
        OfertaRFIPrueba.configurar_cronograma(main_page)
        OfertaRFIPrueba.guardar_inicial(main_page)
        OfertaRFIPrueba.definir_inquietudes(main_page)
        OfertaRFIPrueba.programar_visita(main_page) 
        OfertaRFIPrueba.documentacion(main_page)
        OfertaRFIPrueba.informacion(main_page)
        OfertaRFIPrueba.Guardado_general(main_page)
        OfertaRFIPrueba.criterios(main_page)
        OfertaRFIPrueba.cuadro_economico(main_page)
        OfertaRFIPrueba.usuarios_internos(main_page)
        OfertaRFIPrueba.Guardado_general(main_page)