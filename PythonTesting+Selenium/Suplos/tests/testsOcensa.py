from pages.comentarios_proveedores_Ocensa import comentarios_proveedores_Ocensa
import time

class testsOcensa():
    def test_ocensa_cometario_proveedor(self, main_page):
        PruebaCrearComentario = comentarios_proveedores_Ocensa()

        PruebaCrearComentario.ir_a_proveedores(main_page)
        PruebaCrearComentario.ver_detalle_proveedor(main_page)
        PruebaCrearComentario.ir_pestaña_gestion_profecionales(main_page)
        for _ in range(1):
            PruebaCrearComentario.precionar_agregar_gestion(main_page)
            PruebaCrearComentario.gestion_profecionales(main_page)
            time.sleep(2)
        PruebaCrearComentario.cerrarSesion(main_page)