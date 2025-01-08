import os
from datetime import datetime, timedelta

contador = 0
TEXTO = "Oferta de prueba Automatizada 9"

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
fecha_actual = datetime.now()
Fecha_inicio =  fecha_actual.date().strftime('%Y/%m/%d') # formato yyyy-mm-dd  se poen la fecha actual 
fecha_mas_un_dia = fecha_actual + timedelta(days=1)
Fecha_cierre = fecha_mas_un_dia.strftime('%Y/%m/%d') # formato yyyy-mm-dd  pone la fecha actual mas 1 dia

# definir_inquietudes
Definir_fecha_limite_envio_mensajes = ["No", "Sí"]
Fecha_limite = "2025-01-31" # formato yyyy-mm-dd

# programar_visita
Se_programara_Visita = ["No", "Sí"]

# documentacion_Agregar_contenido_texto
Tipo_contenido = ["Texto", "Archivo"]
Archivo = os.path.abspath("C:\\Users\\Nixon\\Downloads\\Programacion\\All of python\\PythonTesting+Selenium\\Suplos\\utils\\Captura de pantalla 2024-12-23 085325.png") # ruta del archivo 

# informacion
Tipo_entregable = ["Texto", "Archivo", "Selección múltiple", "Selección única"]
sobre = ["Documentación jurídica", "Documentación técnica", "documentación económica", "documentaciÓn financiera", "sobre capacitaciones", "Sobre económico, técnica", "administrador de desempeno", "ofertas"]