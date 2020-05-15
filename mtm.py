import math
import itertools

from helpers import best


dict_mtm = {'poner_cg': 2.59, 'extraer_cg':1.26, 'poner_cm': 3.18, 'extraer_cm': 1.35, 'poner_cp': 3.62, 'extraer_cp': 1.73, 'poner_inter': 4.24, 'extraer_inter': 1.73, 'junta_redonda': 4.73, 'junta_plana': 9.15, 'en_d>1_<100': 2.70, 'en_d>1_100-300':3.20, 'en_d>1_300-500': 3.85, 'en_d>1_500-750':4.71, 'en_d>1_750-1000': 5.47, 'en_d=0,5-1_<100': 3.20, 'en_d=0,5-1_100-300': 3.70, 'en_d=0,5-1_300-500': 4.35, 'en_d=0,5-1_500-750': 5.21, 'en_d=0,5-1_750-1000': 5.97, 'en_d<0,5_<100': 4.47, 'en_d<0,5_100-300': 4.96, 'en_d<0,5_300-500': 5.61, 'en_d<0,5_500-750': 6.47, 'en_d<0,5_750-1000': 7.24, 'en_inter_<100': 5.52, 'en_inter_100-300': 5.92, 'en_inter_>300': 6.24, 'poner_brida_simple': 5.43, 'cortar_brida_simple': 4.14, 'poner_brida_compleja': 6.79, 'orientar_cortar_brida': 5.18, 'colocar_lampara_giratoria':6.49, 'colocar_lampara_lengueta': 6.05, 'colocar_retenedor': 3.20, 'cierre_seguridad': 4.50, 'cerrar_tapa_automatica':5.66, 'cerrar_tapa_libro':3.15, 'cerrar_integrado':1.73, 'cerrar_independiete': 4.15, 'encintado_manual': 9.42, 'encintado_manual_posicion': 10.81, 'encintado_automatico': 6.02, 'encintado_automatico_posicion': 7.32, 'embalar_cable_caja': 2.04, 'embalar_cable_plastico-caja':10.36}

mtm = ['conectores grandes', 'conectores medianos', 'conectores pequeños', ]

class operario(object):
    def __init__(self,tiempo,actividades):
        self.tiempo = tiempo
        self.actividades = actividades

    def getTiempo(self):
         return self.tiempo

    def getActividades(self):
        return self.actividades

class elemento(object):
    def __init__(self,complejo=False,)

for actv in dict_mtm:
    print(actv)

def habilitarActv(pendientes):
""" toma las actividades pendientesy revisa se pueden realizar o todavia no """
