import math
import itertools

from helpers import best

def shareOut(elements, takt_time):

    dict_mtm = {'poner_cg': 2.59, 'extraer_cg':1.26, 'poner_cm': 3.18, 'extraer_cm': 1.35, 'poner_cp': 3.62, 'extraer_cp': 1.73, 'poner_inter': 4.24, 'extraer_inter': 1.73, 'junta_redonda': 4.73, 'junta_plana': 9.15, 'en_d>1_<100': 2.70, 'en_d>1_100-300':3.20, 'en_d>1_300-500': 3.85, 'en_d>1_500-750':4.71, 'en_d>1_750-1000': 5.47, 'en_d=0,5-1_<100': 3.20, 'en_d=0,5-1_100-300': 3.70, 'en_d=0,5-1_300-500': 4.35, 'en_d=0,5-1_500-750': 5.21, 'en_d=0,5-1_750-1000': 5.97, 'en_d<0,5_<100': 4.47, 'en_d<0,5_100-300': 4.96, 'en_d<0,5_300-500': 5.61, 'en_d<0,5_500-750': 6.47, 'en_d<0,5_750-1000': 7.24, 'en_inter_<100': 5.52, 'en_inter_100-300': 5.92, 'en_inter_>300': 6.24, 'poner_brida_simple': 5.43, 'cortar_brida_simple': 4.14, 'poner_brida_compleja': 6.79, 'orientar_cortar_brida': 5.18, 'colocar_lampara_giratoria':6.49, 'colocar_lampara_lengueta': 6.05, 'colocar_retenedor': 3.20, 'cierre_seguridad': 4.50, 'cerrar_tapa_automatica':5.66, 'cerrar_tapa_libro':3.15, 'cerrar_integrado':1.73, 'cerrar_independiete': 4.15, 'encintado_manual': 9.42, 'encintado_manual_posicion': 10.81, 'encintado_automatico': 6.02, 'encintado_automatico_posicion': 7.32, 'embalar_cable_caja': 2.04, 'embalar_cable_plastico-caja':10.36}

    dp1 = {'poner_cg': 2.59, 'poner_cm': 3.18, 'poner_cp': 3.62,'poner_inter': 4.24}
    dp2 = {'junta_redonda': 4.73, 'junta_plana': 9.15,}
    dp3 = {'en_d>1_<100': 2.70, 'en_d>1_100-300':3.20, 'en_d>1_300-500': 3.85, 'en_d>1_500-750':4.71, 'en_d>1_750-1000': 5.47, 'en_d=0,5-1_<100': 3.20, 'en_d=0,5-1_100-300': 3.70, 'en_d=0,5-1_300-500': 4.35, 'en_d=0,5-1_500-750': 5.21, 'en_d=0,5-1_750-1000': 5.97, 'en_d<0,5_<100': 4.47, 'en_d<0,5_100-300': 4.96, 'en_d<0,5_300-500': 5.61, 'en_d<0,5_500-750': 6.47, 'en_d<0,5_750-1000': 7.24, 'en_inter_<100': 5.52, 'en_inter_100-300': 5.92, 'en_inter_>300': 6.24}
    dp4 = {'poner_brida_simple': 5.43, 'poner_brida_compleja': 6.79, 'colocar_lampara_giratoria':6.49, 'colocar_lampara_lengueta': 6.05, 'colocar_retenedor': 3.20, 'cierre_seguridad': 4.50, 'cerrar_tapa_automatica':5.66, 'cerrar_tapa_libro':3.15, 'cerrar_integrado':1.73, 'cerrar_independiete': 4.15, 'encintado_manual': 9.42, 'encintado_manual_posicion': 10.81, 'encintado_automatico': 6.02, 'encintado_automatico_posicion': 7.32}
    dp5 = {'cortar_brida_simple': 4.14, 'orientar_cortar_brida': 5.18}
    dp6 = { 'extraer_cg': 1.26, 'extraer_cm': 1.35, 'extraer_cp': 1.73 }
    dp7 = {}
    dp8 = {'embalar_cable_caja': 2.04, 'embalar_cable_plastico-caja':10.36}

    #p1 = ['poner_cg', 'poner_cm', 'poner_cm']
    p1 = []
    #p2 = ['junta_redonda']
    p2 = []
    #p3 = ['en_d>1_<100', 'en_d>1_<100', 'en_d=0,5-1_<100', 'en_d=0,5-1_<100']
    p3 = []
    #p4 = ['poner_brida_simple', 'poner_brida_compleja','poner_brida_compleja', 'colocar_retenedor', 'colocar_retenedor', 'encintado_automatico_posicion', 'encintado_automatico_posicion']
    p4 = []
    #p5 = ['cortar_brida_simple', 'orientar_cortar_brida', 'orientar_cortar_brida']
    p5 = []
    #p6 = []
    p6 = []
    #p7 = ['embalar_cable_plastico-caja']
    p7 = []

    p8 = []


    #def por_ahora():
    #takt_time = float(input("takt time: "))
    cg = elements[0] #int(input("conectores grandes: "))
    for i in range(cg):
        p1.append('poner_cg')
        p6.append('extraer_cg')

    cm = elements[1] #int(input("conectores medianos: "))
    for i in range(cm):
        p1.append('poner_cm')
        p6.append('extraer_cm')
    ch = elements[2] #int(input("conectores pequeños: "))
    for i in range(ch):
        p1.append('poner_cp')
        p6.append('extraer_cp')
    jun = elements[3] #int(input('junta_redonda: '))
    for i in range(jun):
        p2.append('junta_redonda')

    jun_p = elements[4] #int(input('junta_plana: '))
    for i in range(jun_p):
        p2.append('junta_plana')

    en1 = elements[5] #int(input("en_d>1_<100: "))
    for i in range(en1):
        p3.append('en_d>1_<100')

    en2 = elements[6] #int(input('en_d>1_100-300: '))
    for i in range(en2):
        p3.append('en_d>1_<100')
    en3 = elements[7] #int(input('en_d>1_300-500: '))
    for i in range(en3):
        p3.append('en_d>1_100-300')
    en4 = elements[8] #int(input('en_d>1_500-750: '))
    for i in range(en4):
        p3.append('en_d>1_500-750')
    en5 = elements[9] #int(input('en_d>1_750-1000: '))
    for i in range(en5):
        p3.append('en_d>1_750-1000')
    en6 = elements[10] #int(input('en_d=0,5-1_<100: '))
    for i in range(en6):
        p3.append('en_d=0,5-1_<100')
    en7 = elements[11] #int(input('en_d=0,5-1_100-300: '))
    for i in range(en7):
        p3.append('en_d=0,5-1_100-300')
    en8 = elements[12] #int(input('en_d=0,5-1_300-500: '))
    for i in range(en8):
        p3.append('en_d=0,5-1_300-500')
    en9 = elements[13] #int(input('en_d=0,5-1_500-750: '))
    for i in range(en9):
        p3.append('en_d=0,5-1_500-750')
    en10 = elements[14] #int(input('en_d=0,5-1_750-1000: '))
    for i in range(en10):
        p3.append('en_d=0,5-1_750-1000')
    en11 = elements[15] #int(input('en_d<0,5_<100: '))
    for i in range(en11):
        p3.append('en_d<0,5_<100')
    en12 = elements[16] #int(input('en_d<0,5_100-300: '))
    for i in range(en12):
        p3.append('en_d<0,5_100-300')
    en13 = elements[17] #int(input('en_d<0,5_300-500: '))
    for i in range(en13):
        p3.append('en_d<0,5_300-500')
    en14 = elements[18] #int(input('en_d<0,5_500-750: '))
    for i in range(en14):
        p3.append('en_d<0,5_500-750')
    en15 = elements[19] #int(input('en_d<0,5_750-1000: '))
    for i in range(en15):
        p3.append('en_d<0,5_750-1000')
    en16 = elements[20] #int(input('en_inter_<100: '))
    for i in range(en16):
        p3.append('en_inter_<100')
    en17 = elements[21] #int(input('en_inter_100-300: '))
    for i in range(en17):
        p3.append('en_inter_100-300')
    en18 = elements[22] #int(input('en_inter_>300: '))
    for i in range(en18):
        p3.append('en_inter_>300')
    brs = elements[23] #int(input('bridas simples: '))
    for i in range(brs):
        p4.append('poner_brida_simple')
        p5.append('cortar_brida_simple')
    brc = elements[24] #int(input('bridas complejas: '))
    for i in range(brc):
        p4.append('poner_brida_compleja')
        p5.append('orientar_cortar_brida')
    lamp_gr = elements[25] #int(input('lamparas giratorias: '))
    for i in range(lamp_gr):
        p4.append('colocar_lampara_giratoria')
    lamp_len = elements[26] #int(input('lamparas de lengueta: '))
    for i in range(lamp_len):
        p4.append('colocar_lampara_lengueta')
    el_s1 = elements[27] #int(input('Retenedores: '))
    for i in range(el_s1):
        p4.append('colocar_retenedor')
    el_s2 = elements[28] #int(input('cierre_seguridad: '))
    for i in range(el_s2):
        p4.append('cierre_seguridad')
    el_s3 = elements[29] #int(input('Tapas automaticas: '))
    for i in range(el_s3):
        p4.append('cerrar_tapa_automatica')
    el_s4 = elements[30] #int(input('Tapas de libro: '))
    for i in range(el_s4):
        p4.append('cerrar_tapa_libro')
    el_s5 = elements[31] #int(input('integrados: '))
    for i in range(el_s5):
        p4.append('cerrar_integrado')
    el_s6 = elements[32] #int(input('Independientes: '))
    for i in range(el_s6):
        p4.append('cerrar_independiete')
    encintado_manual = elements[33] #int(input('Encintados manuales: '))
    for i in range(encintado_manual):
        p4.appent('encintado_manual')
    encintado_manual_posicion = elements[34] #int(input('Encintados manueales con posición: '))
    for i in range(encintado_manual_posicion):
        p4.append('encintado_manual_posicion')
    encintado_automatico = elements[35] #int(input('Encintados automaticos: '))
    for i in range(encintado_automatico):
        p4.append('encintado_automatico')
    encintado_automatico_posicion = elements[36] #int(input('Encintados automaticos con posicion: '))
    for i in range(encintado_automatico_posicion):
        p4.append('encintado_automatico_posicion')
    embalar_cable_caja = elements[37] #int(input('Embalar cable directo a caja: '))
    for i in range(embalar_cable_caja):
        p8.append('embalar_cable_caja')
    embalar_cable_plastico = elements[38] #int(input('Embalar cable a bolsa y luego caja: '))
    for i in range(embalar_cable_plastico):
        p8.append('embalar_cable_plastico-caja')

    # Calculate the time for the electric test and add it if is > 0, const is a constant for the calculation
    const = 4.04
    analizar_el = elements[39]*1.598 + elements[40]*1.815 + elements[41]*2.068 + const + elements[42]

    if analizar_el - const > 0:
        dp7['Test_electrico'] = analizar_el
        p7.append('Test_electrico')

    # Do the same as electric test for tightness
    const2 = 5.423
    analizar_est = elements[43]*2.49 + elements[44]*3.992 + elements[45]*5.653 + elements[46] + elements[47] + elements[48] + const2

    if analizar_est - const2 > 0:
        dp7['Test_estanqueidad'] = analizar_est
        p7.append('Test_estanqueidad')

    #takt_time = 15
    #transformar las p en tiempo

    pendientes = [p1, p2, p3, p4, p5, p6, p7, p8]
    dic_pendientes = [dp1, dp2, dp3, dp4, dp5, dp6, dp7, dp8]
    n = 0
    operarios = {}
    operarios[n] = [[],0]
    for i in range(len(pendientes)):

        while len(pendientes[i]) > 0:
            pt = []
            #iterates over keys in pendientes[i]
            for j in range(len(pendientes[i])):
                #list of times to share out
                pt.append(dic_pendientes[i][pendientes[i][j]])
            #print(pt)
            up_time = takt_time - operarios[n][1]

            #get best combination with takt_time restriction
            b_comb, b_sum = best(pt,up_time)
            b_comblist = list(b_comb)


            #eliminate the combination from p[i] and add to operarios
            for z in b_comb:
                for key in dic_pendientes[i]:
                #for key in dict_mtm:
                    if dic_pendientes[i][key] == z:
                    #if dict_mtm[key] == z:
                        operarios[n][0].append(key)
                        #print(operarios)
                        pendientes[i].remove(key)
                        break
            operarios[n][1] += b_sum
            #print(operarios)

            if (len(pendientes[i]) > 0):
                n += 1
                operarios[n] = [[],0]
    return(operarios)
