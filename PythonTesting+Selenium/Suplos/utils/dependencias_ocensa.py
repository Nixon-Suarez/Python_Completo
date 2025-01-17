from datetime import datetime, timedelta
import os

USER = ["oleon@intelcost.com", #Tipo2
        "Administrador_planeacion@suplos.com", #*Administrador Planeación
        "Seguimiento_abastecimiento@suplos.com", #*Seguimiento abastecimiento
        "Usuarios_areas_ocensa@suplos.com", #*Usuarios Áreas Ocensa
        "gerente_directores@suplos.com", #*Gerente / Directores
        "profesional_abastecimiento@suplos.com", #*Profesional Abastecimiento / Líder Categoría
        "gabriel.caicedo@ocensa.com.co", #?Responsable HSE
        "legalocensa@gmail.com", #*Responsable Legal
        "Responsable_financiero@suplos.com", #*Responsable Financiero
        "Profesional_soporte_abastecimiento@suplos.com", #*Profesional Soporte Abastecimiento
        "Subgerente_gestion@suplos.com", #*Subgerente de Gestión (antes Jefe Oficina)
        "Desarrollo_proveedores@suplos.com", #*Desarrollo proveedores
        "Soporte_adm_contrato@suplos.com", #*Soporte administradores de contrato
        "diana.mendez@oocensa.com.co", #*Profesional Abastecimiento convenios
        "Profesionales_areas_soporte@suplos.com", #*Profesionales areas soporte
        "Responsable_HSE_Campos@suplos.com", #*Responsable HSE Campos
        "gerente_directores@suplos.com", #*Director Servicios Corporativos
        "Corredor_seguros@suplos.com", #* no tiene los permisos para ver el detalle
        "Responsable_PQR@suplos.com", #*
        "Profesional_logistica_ocensa@suplos.com", #*
        "Responsable_agente_nacionalizacion@suplos.com", #*
        "Responsable_transportador@suplos.com", #*
        "Almacenista20@suplos.com", #*
        "Responsable_soporte_proyectos@suplos.com", #*
        "Responsable_expediting@suplos.com", #*
        "Reponsable_relaciones_laborales@suplos.com", #*
        "Responsable_impuestos@suplos.com", #*
        "Responsable_outsourcing_impuestos@suplos.com", #* no tiene los permisos para ver el detalle
        "Responsable_excelencia_abastecimiento@suplos.com", #*
        "Responsable_legal_externo@suplos.com" #*  no tiene los permisos para ver el detalle
        ]


PASSWORD = "Ocensa123*"
TEXTO = "Oferta de prueba Automatizada"

fecha_actual = datetime.now()
Fecha_contacto =  fecha_actual.date().strftime('%d/%m/%Y')

Archivo = os.path.abspath("C:\\Users\\Nixon\\Downloads\\Programacion\\All of python\\PythonTesting+Selenium\\Suplos\\utils\\Captura de pantalla 2024-12-23 085325.png")