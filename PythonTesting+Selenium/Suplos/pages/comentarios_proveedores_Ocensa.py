from utils.dependencias_ocensa import *
class comentarios_proveedores_Ocensa():
    def ir_a_proveedores(self, mainPage):
        
        mainPage.click("XPATH", '//div[.//p[text()="Proveedores"]]/a')
        mainPage.click("XPATH", "//a[contains(@class, 'btn btn-app') and contains(., 'Consultar')]") 
    
    def ver_detalle_proveedor(self, mainPage):
        
        mainPage.click("XPATH", "//td/i[@title='Detalle']", index=0)

    def ir_pestaña_gestion_profecionales(self, mainPage):
        
        mainPage.click("XPATH", '//*[@id="infoDetalleProov"]/div[3]/div/ul/li[13]/a')

    def precionar_agregar_gestion(self, mainPage):
        
        mainPage.click("XPATH", '//*[@id="29a"]/div/div/button')
            

    def gestion_profecionales(self, mainPage):
        
        mainPage.write(TEXTO, "ID", "comentarioGp")
        mainPage.write(Fecha_contacto, "ID", "fechaContactoGp")
        mainPage.write(TEXTO, "ID", "repuestaProveedorGp")
        mainPage.write(TEXTO, "ID", "soporteTextGp")
        mainPage.write(TEXTO, "ID", "observacionesAdicionalesGp")
        mainPage.Upload(Archivo, "ID", 'soporteGp')
        mainPage.click("XPATH", '//*[@id="modalGestionProfesionalesOcensa"]/div/div/div[3]/button[1]')
        mainPage.handle_popup("CLASS_NAME", "swal2-popup", "swal2-title", "swal2-content")


    def cerrarSesion(self, mainPage):
        mainPage.click("XPATH", "//a[img[contains(@src, 'noimage.png')]]")
        mainPage.click("XPATH", "//a[text()='Cerrar Sesion']")
