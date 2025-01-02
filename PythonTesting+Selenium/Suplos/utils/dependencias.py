import os

contador = 0
def TEXTO ():
    global contador
    contador += 1
    print (f"Oferta de prueba Automatizada {contador}")

# login
USER = "diana.acuna@odl.com.co"
PASSWORD = "Odl123*"

# info_basica
Tipo_de_necesidad = "Planeada" # o No planeada
Clase = ["Bien", "Servicio", "Bien y servicio"]
Incoterm = ["DDP", "Abierto", "FAC", "DAP", "DPU", "DPU", "DPU", "CIP", "CPT", "EXW1", "CIF", "CFR", "FOB", "FAS", "FCA", "EXW"]
Aplica_AIU = ["Sí", "No"]
Moneda_cotizacion = ["COP", "USD", "EUR", "GBP", "Abierto"]
Moneda_presupuesto = ["COP", "USD", "EUR", "GBP"]
Presupuesto = 1000000 # numerico
Tipo_contratacion = ["Contratación directa", "Proceso competitivo"]
Direccion = ["Presidencia", "Soporte a la operación", "Operaciones", "Legal y asuntos corporativos", "Gestión activos", "Estrategias y finanzas", "Cumplimiento"]
Compania = ["ODL", "OBC", "Conjunto"]

# configurar_cronograma
Fecha_inicio = "2025-01-02" # formato yyyy-mm-dd  Poner un la fecha actual 
Fecha_cierre = "2025-01-03" # formato yyyy-mm-dd  Poner un la fecha actual mas 1 dia

# definir_inquietudes
Definir_fecha_limite_envio_mensajes = ["No", "Sí"]
Fecha_limite = "2025-01-31" # formato yyyy-mm-dd

# programar_visita
Se_programara_Visita = ["No", "Sí"]

# documentacion_Agregar_contenido_texto
Tipo_contenido = ["Texto", "Archivo"]
Archivo = os.path.abspath("C:\\Users\\Nixon\\Downloads\\Programacion\\All of python\\PythonTesting+Selenium\\Suplos\\OfertasODLV2.py\\Archivos\\carga1.png") # ruta del archivo 

# informacion
Tipo_entregable = ["Texto", "Selección única", "Selección múltiple", "Archivo"]