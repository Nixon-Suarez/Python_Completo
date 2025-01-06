from utils.dependencias import *
import time

class ofertasRFI(): 
    def ir_a_Ofertas_RFI(self, mainPage):
        #👇 Valida si dentro el div que tenga adentro un p que tenga el texto Materialización - Proceso / Eventos y preciona el a
        mainPage.click("XPATH", '//div[.//p[text()="Materialización - Proceso / Eventos"]]/a')
        #👇crear oferta RFI validando el a que tenga el onclick argarCrearOfertasAraru 'RFI', 'cerrada'
        mainPage.click("XPATH", '//a[@onclick="cargarCrearOfertasAraru(\'RFI\', \'cerrada\')"]')

    def info_basica(self, mainPage):
        #* info basica                
        mainPage.write(TEXTO, "XPATH", '//*[@id="tab_informacion_basica"]/div/div[1]/div[2]/div[2]/div/div/textarea') #!Xpath real del textarea de objeto - puede dar error en ele futuro
        mainPage.write(TEXTO, "XPATH", '//*[@id="tab_informacion_basica"]/div/div[1]/div[2]/div[3]/div/div/textarea') #!Xpath real del textarea de objeto - puede dar error en ele futuro
        mainPage.click("XPATH", f'//option[text()="{Tipo_de_necesidad}"]')

        mainPage.click("XPATH", f'//option[text()="{Clase[0]}"]')
        if Clase[0] == "Bien":
            mainPage.click("XPATH", f'//option[text()="{Incoterm[0]}"]') 

        mainPage.click("XPATH", f'//option[text()="{Aplica_AIU[0]}"]')
        mainPage.click("XPATH", f'//option[text()="{Moneda_cotizacion[0]}"]')
        mainPage.click("XPATH", f'(//select[@class="form-control"]/option[text()="{Moneda_presupuesto[0]}"])[2]') # se hace asi ya que tiene las mismas opciones que la moneda de cotizacion
        mainPage.click("XPATH", f'//option[text()="{Tipo_contratacion[0]}"]')
        mainPage.click("XPATH", f'//option[text()="{Direccion[0]}"]')
        mainPage.click("XPATH", f'//option[text()="{Compania[0]}"]')
        mainPage.write(Presupuesto, "XPATH", '//input[@class="form-control numero"]') 

    def configurar_cronograma(self, mainPage):
        #*cronograma
        mainPage.click("CSS_SELECTOR", 'a[href="#tab_cronograma"]') #seleccion con el CSS_SELECTOR mejor forma de seleccionar un a
        mainPage.write(Fecha_inicio, "ID", 'datepickerFechaInicio')
        mainPage.write(Fecha_cierre, "ID", 'datepickerFechaCierre')
        mainPage.click("XPATH", '//input[@class="form-control timepicker timepickerHoraInicio"]') 
        time.sleep(2)
        mainPage.click("CSS_SELECTOR", 'a[data-action="incrementHour"]')
        time.sleep(2)

    def guardar(self, mainPage):
        #*Guardar
        mainPage.click("XPATH", '//*[@id="divSolicitarRegistroOfertas"]/div/div/div/div/div/div/div/div[3]/div/div/button') #!Xpath real del textarea de objeto - puede dar error en ele futuro
        time.sleep(5)
        mainPage.click("CSS_SELECTOR", 'button.swal2-confirm.swal2-styled')
        time.sleep(3)

    def definir_inquietudes(self, mainPage):
        #* Limite de inquitudes
        mainPage.click("CSS_SELECTOR", 'a[href="#tab_inquietudes"]')
        time.sleep(3)

        mainPage.click("XPATH", f'//label[text()="¿Definir fecha límite de envío de mensajes?:"]/following-sibling::div/select/option[text()="{Definir_fecha_limite_envio_mensajes[0]}"]') #! corregir cuando se haga el input
        if Definir_fecha_limite_envio_mensajes[0] == "Sí":
            mainPage.write(Fecha_limite, "ID", 'datepickerFechaLimiteMsgFecha')
            mainPage.write(TEXTO, "XPATH", '//*[@id="tab_inquietudes"]/div/div/div[2]/div[2]/div[4]/div/textarea') #!Xpath real del textarea de objeto - puede dar error en ele futuro

    def programar_visita(self, mainPage):
        #*Visita de obra / Reunión aclaratoria
        # llenarlo con si si quiere que aparezca no solo no se usa la funcion (Arreglar)
        mainPage.click("CSS_SELECTOR", 'a[href="#tab_visita_obras"]')
        time.sleep(3)
        mainPage.click("XPATH", f'//label[text()="¿Se programará Visita / Reunión aclaratoria?:"]/following-sibling::div/select/option[text()="{Se_programara_Visita[0]}"]')
        # terminar de llenar campos
            # mainPage.click("XPATH", '//button[contains(@class, "btn btn-primary") and contains(text(), "Adicionar")]')
            # mainPage.click("CSS_SELECTOR", 'a[href="#divRegistroVisitae643b208-a5f9-4e91-bf56-4b2b9a726eef"]')

    #?----------------------------
    def documentacion(self, mainPage):
        #*Contenido - Documentación petición de ofertas / Términos y condiciones del proceso
        mainPage.click("CSS_SELECTOR", 'a[href="#tab_contenido_documentacion"]')
        mainPage.click("XPATH", '//button[contains(@class, "btn btn-primary") and contains(text(), " Agregar contenido")]')
        self.documentacion_Agregar_contenido_Archivo(mainPage)
        self.documentacion_Agregar_contenido_texto(mainPage)
        mainPage.click("XPATH", '//*[@id="tab_contenido_documentacion"]/div/div[2]/div/div/div[3]/button[2]') #!XPATH real cerrar

    def documentacion_Agregar_contenido_texto(self, mainPage):
        mainPage.click("XPATH", f'//option[text()="{Tipo_contenido[0]}"]')
        mainPage.write(TEXTO, "XPATH", '//div[contains(@class, "form-group") and .//p[text()="Título del contenido (*):"]]/input')
        mainPage.write(TEXTO, "XPATH", '//div[contains(@class, "form-group") and .//p[text()="Descripción del contenido:"]]/textarea')
        mainPage.write(TEXTO, "ID", 'mce_0_ifr')
        self.agregarDucumentacion(mainPage)

    def documentacion_Agregar_contenido_Archivo(self, mainPage):
        mainPage.click("XPATH", f'//option[text()="{Tipo_contenido[1]}"]')
        mainPage.write(TEXTO, "XPATH", '//div[contains(@class, "form-group") and .//p[text()="Nombre del archivo (*):"]]/input')
        mainPage.write(TEXTO, "XPATH", '//div[contains(@class, "form-group") and .//p[text()="Descripción del archivo:"]]/textarea')
        mainPage.Upload(Archivo, "ID", 'rutaContenidoArchivo')
        mainPage.click("CSS_SELECTOR", 'a[href="../ic_controladores/ctrl_uploadfiles.php"]')
        time.sleep(5)
        mainPage.click("CSS_SELECTOR", 'button.swal2-confirm.swal2-styled')
        self.agregarDucumentacion(mainPage)

    def agregarDucumentacion(self, mainPage):
        mainPage.click("XPATH", "//button[contains(@class, 'btn-success') and contains(text(), 'Agregar')]")
    #?------------------------------

    #*--------------------------------
    def informacion(self, mainPage):
        # Información - Entregables de la oferta por parte de los oferentes
        mainPage.click("CSS_SELECTOR", 'a[href="#tab_entregables"]')
        mainPage.click("XPATH", "//button[contains(@class, 'btn-primary') and contains(text(), 'Agregar entregable')]")
        self.informacion_agregar_texto(mainPage)
        self.informacion_agregar_archivo(mainPage)
        self.informacion_agregar_seleccion_multiple(mainPage)

        mainPage.click("XPATH", '//*[@id="tab_entregables"]/div[1]/div[2]/div[1]/div[1]/div[3]/button[2]')

    def informacion_agregar_texto(self, mainPage):
        mainPage.click("XPATH", f'//div[label[contains(text(),"Tipo de entregable (*)")]]/select/option[text()="{Tipo_entregable[0]}"]')
        mainPage.write(TEXTO, "XPATH", '//*[@id="tab_entregables"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/input')
        mainPage.write(TEXTO, "ID", 'mce_2_ifr')
        self.agregraInformacion(mainPage)
    
    def informacion_agregar_archivo(self, mainPage):
        mainPage.click("XPATH", f'//div[label[contains(text(),"Tipo de entregable (*)")]]/select/option[text()="{Tipo_entregable[1]}"]')
        mainPage.write(TEXTO, "XPATH", '//div[contains(@class, "form-group") and .//p[text()="Título del archivo a solicitar (*):"]]/input')
        mainPage.write(TEXTO, "XPATH", '//div[contains(@class, "form-group") and .//p[text()="Descripción del archivo a solicitar:"]]/textarea')
        self.agregraInformacion(mainPage)
    
    def informacion_agregar_seleccion_multiple(self, mainPage):
        mainPage.click("XPATH", f'//div[label[contains(text(),"Tipo de entregable (*)")]]/select/option[text()="{Tipo_entregable[2]}"]')
        mainPage.write(TEXTO, "XPATH", '//div[contains(@class, "form-group") and .//p[text()="Pregunta contenido (*):"]]/input')
        mainPage.click("XPATH", '//*[@id="tab_entregables"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[4]/div[2]/div/div/button')
        mainPage.write(TEXTO, "XPATH", '//*[@id="tab_entregables"]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[4]/div[2]/div[1]/div/div/input')
        self.agregraInformacion(mainPage)
    
    def informacion_agregar_seleccion_unica(self, mainPage):
        mainPage.click("XPATH", f'//div[label[contains(text(),"Tipo de entregable (*)")]]/select/option[text()="{Tipo_entregable[3]}"]')
    #agregar los demas campos 

    def agregraInformacion(self, mainPage):
        mainPage.click("XPATH", '(//button[contains(@class, "btn-success") and contains(text(), "Agregar")])[2]')
    #*---------------------------------