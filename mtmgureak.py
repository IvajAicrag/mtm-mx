import math
import itertools
import copy

from helpers import best

def shareOut(elements, takt_time):

    dict_mtm = {'poner conector grande': 2.59, 'extraer conector grande':1.26, 'poner conector mediano': 3.18, 'extraer conector mediano': 1.35, 'poner conector pequeño': 3.62, 'extraer conector pequeño': 1.73, 'poner interconexión': 4.24, 'extraer interconexión': 1.7301, 'junta redonda': 4.73, 'junta plana': 9.15, 'Encliquetado diámetro>1 (<100mm)': 2.70, 'Encliquetado diámetro>1 (100-300mm)':3.20, 'Encliquetado diámetro>1 (300-500mm)': 3.85, 'Encliquetado diámetro>1 (500-750mm)':4.71, 'Encliquetado diámetro>1 (750-1000mm)': 5.47, 'Encliquetado diámetro=0,5-1 (<100mm)': 3.20, 'Encliquetado diámetro=0,5-1 (100-300mm)': 3.70, 'Encliquetado diámetro=0,5-1 (300-500mm)': 4.35, 'Encliquetado diámetro=0,5-1 (500-750mm)': 5.21, 'Encliquetado diámetro=0,5-1 (750-1000mm)': 5.97, 'Encliquetado diámetro<0,5 (<100mm)': 4.47, 'Encliquetado diámetro<0,5 (100-300mm)': 4.96, 'Encliquetado diámetro<0,5 (300-500mm)': 5.61, 'Encliquetado diámetro<0,5 (500-750mm)': 6.47, 'Encliquetado diámetro<0,5 (750-1000mm)': 7.24, 'Encliquetado interconexión<100mm': 5.52, 'Encliquetado interconexión=100-300mm': 5.92, 'Encliquetado interconexión>300mm': 6.24, 'poner brida simple': 5.43, 'cortar brida simple': 4.14, 'poner brida compleja': 6.79, 'orientar y cortar brida': 5.18, 'colocar lámpara giratoria':6.49, 'colocar lámpara lengueta': 6.05, 'colocar retenedor': 3.20, 'cierre seguridad': 4.50, 'cerrar tapa automática':5.66, 'cerrar tapa libro':3.15, 'cerrar integrado':1.73, 'cerrar independiente': 4.15, 'encintado manual': 9.42, 'encintado manual con posición': 10.81, 'encintado automático': 6.02, 'encintado automático con posición': 7.32, 'embalar cable directo a caja': 2.04, 'embalar cable de plástico a caja':10.36}

    dp1 = {'poner conector grande': 2.59, 'poner conector mediano': 3.18, 'poner conector pequeño': 3.62,'poner interconexión': 4.24}
    dp2 = {'junta redonda': 4.73, 'junta plana': 9.15,}
    dp3 = {'Encliquetado diámetro>1 (<100mm)': 2.70, 'Encliquetado diámetro>1 (100-300mm)':3.20, 'Encliquetado diámetro>1 (300-500mm)': 3.85, 'Encliquetado diámetro>1 (500-750mm)':4.71, 'Encliquetado diámetro>1 (750-1000mm)': 5.47, 'Encliquetado diámetro=0,5-1 (<100mm)': 3.2001, 'Encliquetado diámetro=0,5-1 (100-300mm)': 3.70, 'Encliquetado diámetro=0,5-1 (300-500mm)': 4.35,'Encliquetado diámetro=0,5-1 (500-750mm)': 5.21, 'Encliquetado diámetro=0,5-1 (750-1000mm)': 5.97, 'Encliquetado diámetro<0,5 (<100mm)': 4.47, 'Encliquetado diámetro<0,5 (100-300mm)': 4.96, 'Encliquetado diámetro<0,5 (300-500mm)': 5.61, 'Encliquetado diámetro<0,5 (500-750mm)': 6.47, 'Encliquetado diámetro<0,5 (750-1000mm)': 7.24, 'Encliquetado interconexión<100mm': 5.52, 'Encliquetado interconexión=100-300mm': 5.92, 'Encliquetado interconexión>300mm': 6.24}
    dp4 = {'poner brida simple': 5.43, 'poner brida compleja': 6.79, 'colocar lámpara giratoria':6.49, 'colocar lámpara lengueta': 6.05, 'colocar retenedor': 3.20, 'cierre seguridad': 4.50, 'cerrar tapa automática':5.66, 'cerrar tapa libro':3.15, 'cerrar integrado':1.73, 'cerrar independiente': 4.15, 'encintado manual': 9.42, 'encintado manual con posición': 10.81, 'encintado automático': 6.02, 'encintado automático con posición': 7.32}
    dp5 = {'cortar brida simple': 4.14, 'orientar y cortar brida': 5.18}
    dp6 = { 'extraer conector grande': 1.26, 'extraer conector mediano': 1.35, 'extraer conector pequeño': 1.73, 'extraer interconexión': 1.7301 }
    dp7 = {}
    dp8 = {'embalar cable directo a caja': 2.04, 'embalar cable de plástico a caja':10.36}
    dp9 = {}

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

    p9 = []


    #def por_ahora():
    #takt_time = float(input("takt time: "))
    cg = elements[0] #int(input("conectores grandes: "))
    for i in range(cg):
        p1.append('poner conector grande')
        p6.append('extraer conector grande')

    cm = elements[1] #int(input("conectores medianos: "))
    for i in range(cm):
        p1.append('poner conector mediano')
        p6.append('extraer conector mediano')
    ch = elements[2] #int(input("conectores pequeños: "))
    for i in range(ch):
        p1.append('poner conector pequeño')
        p6.append('extraer conector pequeño')

    inter = elements[3] #int(input("conectores pequeños: "))
    for i in range(ch):
        p1.append('poner interconexión')
        p6.append('extraer interconexión')

    jun = elements[4] #int(input('junta_redonda: '))
    for i in range(jun):
        p2.append('junta redonda')

    jun_p = elements[5] #int(input('junta_plana: '))
    for i in range(jun_p):
        p2.append('junta plana')

    en1 = elements[6] #int(input("en_d>1_<100: "))
    for i in range(en1):
        p3.append('Encliquetado diámetro>1 (<100mm)')

    en2 = elements[7] #int(input('en_d>1_100-300: '))
    for i in range(en2):
        p3.append('Encliquetado diámetro>1 (100-300mm)')
    en3 = elements[8] #int(input('en_d>1_300-500: '))
    for i in range(en3):
        p3.append('Encliquetado diámetro>1 (300-500mm)')
    en4 = elements[9] #int(input('en_d>1_500-750: '))
    for i in range(en4):
        p3.append('Encliquetado diámetro>1 (500-750mm)')
    en5 = elements[10] #int(input('en_d>1_750-1000: '))
    for i in range(en5):
        p3.append('Encliquetado diámetro>1 (750-1000mm)')
    en6 = elements[11] #int(input('en_d=0,5-1_<100: '))
    for i in range(en6):
        p3.append('Encliquetado diámetro=0,5-1 (<100mm)')
    en7 = elements[12] #int(input('en_d=0,5-1_100-300: '))
    for i in range(en7):
        p3.append('Encliquetado diámetro=0,5-1 (100-300mm)')
    en8 = elements[13] #int(input('en_d=0,5-1_300-500: '))
    for i in range(en8):
        p3.append('Encliquetado diámetro=0,5-1 (300-500mm)')
    en9 = elements[14] #int(input('en_d=0,5-1_500-750: '))
    for i in range(en9):
        p3.append('Encliquetado diámetro=0,5-1 (500-750mm)')
    en10 = elements[15] #int(input('en_d=0,5-1_750-1000: '))
    for i in range(en10):
        p3.append('Encliquetado diámetro=0,5-1 (750-1000mm)')
    en11 = elements[16] #int(input('en_d<0,5_<100: '))
    for i in range(en11):
        p3.append('Encliquetado diámetro<0,5 (<100mm)')
    en12 = elements[17] #int(input('en_d<0,5_100-300: '))
    for i in range(en12):
        p3.append('Encliquetado diámetro<0,5 (100-300mm)')
    en13 = elements[18] #int(input('en_d<0,5_300-500: '))
    for i in range(en13):
        p3.append('Encliquetado diámetro<0,5 (300-500mm)')
    en14 = elements[19] #int(input('en_d<0,5_500-750: '))
    for i in range(en14):
        p3.append('Encliquetado diámetro<0,5 (500-750mm)')
    en15 = elements[20] #int(input('en_d<0,5_750-1000: '))
    for i in range(en15):
        p3.append('Encliquetado diámetro<0,5 (750-1000mm)')
    en16 = elements[21] #int(input('en_inter_<100: '))
    for i in range(en16):
        p3.append('Encliquetado interconexión<100mm')
    en17 = elements[22] #int(input('en_inter_100-300: '))
    for i in range(en17):
        p3.append('Encliquetado interconexión=100-300mm')
    en18 = elements[23] #int(input('en_inter_>300: '))
    for i in range(en18):
        p3.append('Encliquetado interconexión>300mm')
    brs = elements[24] #int(input('bridas simples: '))
    for i in range(brs):
        p4.append('poner brida simple')
        p5.append('cortar brida simple')
    brc = elements[25] #int(input('bridas complejas: '))
    for i in range(brc):
        p4.append('poner brida compleja')
        p5.append('orientar y cortar brida')
    lamp_gr = elements[26] #int(input('lamparas giratorias: '))
    for i in range(lamp_gr):
        p4.append('colocar lámpara giratoria')
    lamp_len = elements[27] #int(input('lamparas de lengueta: '))
    for i in range(lamp_len):
        p4.append('colocar lámpara lengueta')
    el_s1 = elements[28] #int(input('Retenedores: '))
    for i in range(el_s1):
        p4.append('colocar retenedor')
    el_s2 = elements[29] #int(input('cierre_seguridad: '))
    for i in range(el_s2):
        p4.append('cierre seguridad')
    el_s3 = elements[30] #int(input('Tapas automaticas: '))
    for i in range(el_s3):
        p4.append('cerrar tapa automática')
    el_s4 = elements[31] #int(input('Tapas de libro: '))
    for i in range(el_s4):
        p4.append('cerrar tapa libro')
    el_s5 = elements[32] #int(input('integrados: '))
    for i in range(el_s5):
        p4.append('cerrar integrado')
    el_s6 = elements[33] #int(input('Independientes: '))
    for i in range(el_s6):
        p4.append('cerrar independiente')
    encintado_manual = elements[34] #int(input('Encintados manuales: '))
    for i in range(encintado_manual):
        p4.append('encintado manual')
    encintado_manual_posicion = elements[35] #int(input('Encintados manueales con posición: '))
    for i in range(encintado_manual_posicion):
        p4.append('encintado manual con posición')
    encintado_automatico = elements[36] #int(input('Encintados automaticos: '))
    for i in range(encintado_automatico):
        p4.append('encintado automático')
    encintado_automatico_posicion = elements[37] #int(input('Encintados automaticos con posicion: '))
    for i in range(encintado_automatico_posicion):
        p4.append('encintado automático con posición')
    embalar_cable_caja = elements[38] #int(input('Embalar cable directo a caja: '))
    for i in range(embalar_cable_caja):
        p8.append('embalar cable directo a caja')
    embalar_cable_plastico = elements[39] #int(input('Embalar cable a bolsa y luego caja: '))
    for i in range(embalar_cable_plastico):
        p8.append('embalar cable de plástico a caja')

    # Calculate the time for the electric test and add it if is > 0, const is a constant for the calculation
    const = 4.04
    analizar_el = elements[40]*1.598 + elements[41]*1.815 + elements[42]*2.068 + const + elements[43]

    if analizar_el - const > 0:
        dp7['Test eléctrico'] = analizar_el
        p7.append('Test eléctrico')

    # Do the same as electric test for tightness
    const2 = 5.423
    analizar_est = elements[44]*2.49 + elements[45]*3.992 + elements[46]*5.653 + elements[47] + elements[48] + elements[49] + const2

    if analizar_est - const2 > 0:
        dp7['Test estanqueidad'] = analizar_est
        p7.append('Test estanqueidad')

    #takt_time = 15
    #transformar las p en tiempo

    #In case of more thant 15 Encliquetados we will split the first 15 for optimization
    if len(p3) > 20:
        p9 = copy.deepcopy(p8)
        dp9 = copy.deepcopy(dp8)
        p8 = copy.deepcopy(p7)
        dp8.clear()
        dp8 = copy.deepcopy(dp7)
        p7 = copy.deepcopy(p6)
        dp7.clear()
        dp7 = copy.deepcopy(dp6)
        p6 = copy.deepcopy(p5)
        dp6.clear()
        dp6 = copy.deepcopy(dp5)
        p5 = copy.deepcopy(p4)
        dp5.clear()
        dp5 = copy.deepcopy(dp4)

        #store in p4 and dp4 to make faster the operation of share in Encliquetados
        dp4.clear()
        dp4 = copy.deepcopy(dp3)
        #divide p3 into two
        lenght = len(p3)
        middle_index = lenght//2

        first = p3[:middle_index]

        second = p3[middle_index:]

        p4 = copy.deepcopy(second)
        p3 = copy.deepcopy(first)


    pendientes = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    dic_pendientes = [dp1, dp2, dp3, dp4, dp5, dp6, dp7, dp8, dp9]
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
