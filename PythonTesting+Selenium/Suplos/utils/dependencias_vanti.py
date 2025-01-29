from datetime import datetime


USER = ["maria_azuaje@suplos.com", #tipo 2
        "mgarcia_auditor@vanti.com", #Auditor 
        "mgarcia_profesional_abastecimiento_lider_categoria@vanti.com", #Profesional compras 
        "mgarcia_coordinador_categorias@vanti.com", #Coordinador categorías 
        "gerente_gestion_vanti@suplos.com", #Gerente gestión por categorias 
        "RolesYPerfiles_abastecimiento@vanti.com", #Director abastecimiento
        "mcuartas_profesiona_areausuaria@vanti.com", #Profesional Area Usuaria 
        "profesional_prov27@suplos.com", #Profesional proveedores Vanti 
        "mgarcia_oficial_de_cumplimiento@vanti.com", #Oficial de cumplimiento 
        "RepresentanteLegalVanti@suplos.com", #Representante Legal Vanti 
        "mgarcia_gerente_director_usuario@vanti.com", #Gerente / Director Usuario 
        "vicepresidencia_rep_27@suplos.com" #Vicepresidente 
        "GerenteDirectorUsuarioRepresentanteLegal@suplos.com", #Gerente / Director Usuario / Representante Legal 
        "vicepresidencia_rep_27@suplos.com", #Vicepresidente / Representante Legal 
        "Profesional_planificacion@suplos.com", #Profesional planificación 
        "Usuario_coordinador_planificacion@suplos.com", #Coordinador planificación 
        "Proveedor@suplos.com" #Proveedor
]

PASSWORD = "Vanti123*"

TEXTO = "Oferta de prueba Automatizada 12"

fecha_actual = datetime.now()
Dia_actual =  fecha_actual.date().strftime('%d')