import math
import itertools
import copy

from helpers import best, chunker_list

def shareOut(elements, takt_time, factor):

    dict_mtm = {'poner conector grande': 2.59, 'extraer conector grande':1.26, 'poner conector mediano': 3.18, 'extraer conector mediano': 1.35, 'poner conector pequeño': 3.62, 'extraer conector pequeño': 1.73, 'poner interconexión': 4.24, 'extraer interconexión': 1.73, 'junta redonda': 4.73, 'junta plana': 9.15, 'Encliquetado diámetro>1 (<100mm)': 2.70, 'Encliquetado diámetro>1 (100-300mm)':3.20, 'Encliquetado diámetro>1 (300-500mm)': 3.85, 'Encliquetado diámetro>1 (500-750mm)':4.71, 'Encliquetado diámetro>1 (750-1000mm)': 5.47, 'Encliquetado diámetro=0,5-1 (<100mm)': 3.2001, 'Encliquetado diámetro=0,5-1 (100-300mm)': 3.70, 'Encliquetado diámetro=0,5-1 (300-500mm)': 4.35, 'Encliquetado diámetro=0,5-1 (500-750mm)': 5.21, 'Encliquetado diámetro=0,5-1 (750-1000mm)': 5.97, 'Encliquetado diámetro<0,5 (<100mm)': 4.47, 'Encliquetado diámetro<0,5 (100-300mm)': 4.96, 'Encliquetado diámetro<0,5 (300-500mm)': 5.61, 'Encliquetado diámetro<0,5 (500-750mm)': 6.47, 'Encliquetado diámetro<0,5 (750-1000mm)': 7.24, 'Encliquetado interconexión<100mm': 5.52, 'Encliquetado interconexión=100-300mm': 5.92, 'Encliquetado interconexión>300mm': 6.24, 'poner brida simple': 5.43, 'cortar brida simple': 4.14, 'poner brida compleja': 6.79, 'orientar y cortar brida': 5.18, 'colocar lámpara giratoria':6.49, 'colocar lámpara lengueta': 6.05, 'colocar retenedor': 3.20, 'cierre seguridad': 4.50, 'cerrar tapa automática':5.66, 'cerrar tapa libro':3.15, 'cerrar integrado':1.73, 'cerrar independiente': 4.15, 'encintado manual': 9.42, 'encintado manual con posición': 10.81, 'encintado automático': 6.02, 'encintado automático con posición': 7.32, 'embalar cable directo a caja': 2.04, 'embalar cable de plástico a caja':10.36}

    #dp1 = {'poner conector grande': 2.59, 'poner conector mediano': 3.18, 'poner conector pequeño': 3.62,'poner interconexión': 4.24}
    dp1 = {}
    #dp2 = {'junta redonda': 4.73, 'junta plana': 9.15,}
    dp2 = {}
    #dp3 = {'Encliquetado diámetro>1 (<100mm)': 2.70, 'Encliquetado diámetro>1 (100-300mm)':3.20, 'Encliquetado diámetro>1 (300-500mm)': 3.85, 'Encliquetado diámetro>1 (500-750mm)':4.71, 'Encliquetado diámetro>1 (750-1000mm)': 5.47, 'Encliquetado diámetro=0,5-1 (<100mm)': 3.2001, 'Encliquetado diámetro=0,5-1 (100-300mm)': 3.70, 'Encliquetado diámetro=0,5-1 (300-500mm)': 4.35,'Encliquetado diámetro=0,5-1 (500-750mm)': 5.21, 'Encliquetado diámetro=0,5-1 (750-1000mm)': 5.97, 'Encliquetado diámetro<0,5 (<100mm)': 4.47, 'Encliquetado diámetro<0,5 (100-300mm)': 4.96, 'Encliquetado diámetro<0,5 (300-500mm)': 5.61, 'Encliquetado diámetro<0,5 (500-750mm)': 6.47, 'Encliquetado diámetro<0,5 (750-1000mm)': 7.24, 'Encliquetado interconexión<100mm': 5.52, 'Encliquetado interconexión=100-300mm': 5.92, 'Encliquetado interconexión>300mm': 6.24}
    dp3 = {}
    #dp4 = {'poner brida simple': 5.43, 'poner brida compleja': 6.79, 'colocar lámpara giratoria':6.49, 'colocar lámpara lengueta': 6.05, 'colocar retenedor': 3.20, 'cierre seguridad': 4.50, 'cerrar tapa automática':5.66, 'cerrar tapa libro':3.15, 'cerrar integrado':1.73, 'cerrar independiente': 4.15, 'encintado manual': 9.42, 'encintado manual con posición': 10.81, 'encintado automático': 6.02, 'encintado automático con posición': 7.32}
    dp4 = {}
    #dp5 = {'cortar brida simple': 4.14, 'orientar y cortar brida': 5.18}
    dp5 = {}
    #dp6 = { 'extraer conector grande': 1.26, 'extraer conector mediano': 1.35, 'extraer conector pequeño': 1.73, 'extraer interconexión': 1.7301 }
    dp6 = {'extraer cable': 0}
    dp7 = {}
    #dp8 = {'embalar cable directo a caja': 2.04, 'embalar cable de plástico a caja':10.36}
    dp8 = {}
    dp9 = {}
    dp10 = {}
    dp11 = {}
    dp12 = {}

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
    p10 = []
    p11 = []
    p12 = []

    #def por_ahora():
    #takt_time = float(input("takt time: "))
    cg = elements[0] #int(input("conectores grandes: "))
    for i in range(cg):
        task = 'poner conector grande'
        task2 = 'extraer conector grande'
        extraer = 'extraer cable'
        p1.append(task)
        dp1[task] = (dict_mtm[task]) / factor
        if len(p6) == 0:
            p6.append(extraer)
        dp6[extraer] += dict_mtm[task2] / factor

    cm = elements[1] #int(input("conectores medianos: "))
    for i in range(cm):
        task = 'poner conector mediano'
        task2 = 'extraer conector mediano'
        extraer = 'extraer cable'
        p1.append(task)
        dp1[task] = (dict_mtm[task]) / factor
        if len(p6) == 0:
            p6.append(extraer)
        dp6[extraer] += dict_mtm[task2] / factor

    ch = elements[2] #int(input("conectores pequeños: "))
    for i in range(ch):
        task = 'poner conector pequeño'
        task2 = 'extraer conector pequeño'
        extraer = 'extraer cable'
        p1.append(task)
        dp1[task] = (dict_mtm[task]) / factor
        if len(p6) == 0:
            p6.append(extraer)
        dp6[extraer] += dict_mtm[task2] / factor

    inter = elements[3] #int(input("conectores pequeños: "))
    for i in range(inter):
        task = 'poner interconexión'
        task2 = 'extraer interconexión'
        extraer = 'extraer cable'
        p1.append(task)
        dp1[task] = (dict_mtm[task]) / factor
        if len(p6) == 0:
            p6.append(extraer)
        dp6[extraer] += dict_mtm[task2] / factor

    jun = elements[4] #int(input('junta_redonda: '))
    for i in range(jun):
        task = 'junta redonda'
        p2.append(task)
        dp2[task] = dict_mtm[task] / factor

    jun_p = elements[5] #int(input('junta_plana: '))
    for i in range(jun_p):
        task = 'junta plana'
        p2.append(task)
        dp2[task] = dict_mtm[task] / factor

    en1 = elements[6] #int(input("en_d>1_<100: "))
    for i in range(en1):
        task = 'Encliquetado diámetro>1 (<100mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en2 = elements[7] #int(input('en_d>1_100-300: '))
    for i in range(en2):
        task = 'Encliquetado diámetro>1 (100-300mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en3 = elements[8] #int(input('en_d>1_300-500: '))
    for i in range(en3):
        task = 'Encliquetado diámetro>1 (300-500mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en4 = elements[9] #int(input('en_d>1_500-750: '))
    for i in range(en4):
        task = 'Encliquetado diámetro>1 (500-750mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en5 = elements[10] #int(input('en_d>1_750-1000: '))
    for i in range(en5):
        task = 'Encliquetado diámetro>1 (750-1000mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en6 = elements[11] #int(input('en_d=0,5-1_<100: '))
    for i in range(en6):
        task = 'Encliquetado diámetro=0,5-1 (<100mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en7 = elements[12] #int(input('en_d=0,5-1_100-300: '))
    for i in range(en7):
        task = 'Encliquetado diámetro=0,5-1 (100-300mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en8 = elements[13] #int(input('en_d=0,5-1_300-500: '))
    for i in range(en8):
        task = 'Encliquetado diámetro=0,5-1 (300-500mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en9 = elements[14] #int(input('en_d=0,5-1_500-750: '))
    for i in range(en9):
        task = 'Encliquetado diámetro=0,5-1 (500-750mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en10 = elements[15] #int(input('en_d=0,5-1_750-1000: '))
    for i in range(en10):
        task = 'Encliquetado diámetro=0,5-1 (750-1000mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en11 = elements[16] #int(input('en_d<0,5_<100: '))
    for i in range(en11):
        task = 'Encliquetado diámetro<0,5 (<100mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en12 = elements[17] #int(input('en_d<0,5_100-300: '))
    for i in range(en12):
        task = 'Encliquetado diámetro<0,5 (100-300mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en13 = elements[18] #int(input('en_d<0,5_300-500: '))
    for i in range(en13):
        task = 'Encliquetado diámetro<0,5 (300-500mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en14 = elements[19] #int(input('en_d<0,5_500-750: '))
    for i in range(en14):
        task = 'Encliquetado diámetro<0,5 (500-750mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en15 = elements[20] #int(input('en_d<0,5_750-1000: '))
    for i in range(en15):
        task = 'Encliquetado diámetro<0,5 (750-1000mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en16 = elements[21] #int(input('en_inter_<100: '))
    for i in range(en16):
        task = 'Encliquetado interconexión<100mm'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en17 = elements[22] #int(input('en_inter_100-300: '))
    for i in range(en17):
        task = 'Encliquetado interconexión=100-300mm'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    en18 = elements[23] #int(input('en_inter_>300: '))
    for i in range(en18):
        task = 'Encliquetado interconexión>300mm'
        p3.append(task)
        dp3[task] = dict_mtm[task] / factor

    brs = elements[24] #int(input('bridas simples: '))
    for i in range(brs):
        task = 'poner brida simple'
        task2 = 'cortar brida simple'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor
        p5.append(task2)
        dp5[task2] = dict_mtm[task2] / factor

    brc = elements[25] #int(input('bridas complejas: '))
    for i in range(brc):
        task = 'poner brida compleja'
        task2 = 'orientar y cortar brida'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor
        p5.append(task2)
        dp5[task2] = dict_mtm[task2] / factor

    lamp_gr = elements[26] #int(input('lamparas giratorias: '))
    for i in range(lamp_gr):
        task = 'colocar lámpara giratoria'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor

    lamp_len = elements[27] #int(input('lamparas de lengueta: '))
    for i in range(lamp_len):
        task = 'colocar lámpara lengueta'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor

    el_s1 = elements[28] #int(input('Retenedores: '))
    for i in range(el_s1):
        task = 'colocar retenedor'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor

    el_s2 = elements[29] #int(input('cierre_seguridad: '))
    for i in range(el_s2):
        task = 'cierre seguridad'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor

    el_s3 = elements[30] #int(input('Tapas automaticas: '))
    for i in range(el_s3):
        task = 'cerrar tapa automática'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor

    el_s4 = elements[31] #int(input('Tapas de libro: '))
    for i in range(el_s4):
        task = 'cerrar tapa libro'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor

    el_s5 = elements[32] #int(input('integrados: '))
    for i in range(el_s5):
        task = 'cerrar integrado'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor

    el_s6 = elements[33] #int(input('Independientes: '))
    for i in range(el_s6):
        task = 'cerrar independiente'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor

    encintado_manual = elements[34] #int(input('Encintados manuales: '))
    for i in range(encintado_manual):
        task = 'encintado manual'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor

    encintado_manual_posicion = elements[35] #int(input('Encintados manueales con posición: '))
    for i in range(encintado_manual_posicion):
        task = 'encintado manual con posición'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor

    encintado_automatico = elements[36] #int(input('Encintados automaticos: '))
    for i in range(encintado_automatico):
        task = 'encintado automático'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor

    encintado_automatico_posicion = elements[37] #int(input('Encintados automaticos con posicion: '))
    for i in range(encintado_automatico_posicion):
        task = 'encintado automático con posición'
        p4.append(task)
        dp4[task] = dict_mtm[task] / factor

    embalar_cable_caja = elements[38] #int(input('Embalar cable directo a caja: '))
    for i in range(embalar_cable_caja):
        task = 'embalar cable directo a caja'
        p8.append(task)
        dp8[task] = dict_mtm[task] / factor

    embalar_cable_plastico = elements[39] #int(input('Embalar cable a bolsa y luego caja: '))
    for i in range(embalar_cable_plastico):
        task = 'embalar cable de plástico a caja'
        p8.append(task)
        dp8[task] = dict_mtm[task] / factor

    # Calculate the time for the electric test and add it if is > 0, const is a constant for the calculation
    const = 4.04
    analizar_el = (elements[40]*1.598 + elements[41]*1.815 + elements[42]*2.068 + const + elements[43]) / factor

    if analizar_el - (const / factor) > 0:
        dp7['Test eléctrico'] = analizar_el
        p7.append('Test eléctrico')

    # Do the same as electric test for tightness
    const2 = 5.423
    analizar_est = (elements[44]*2.49 + elements[45]*3.992 + elements[46]*5.653 + elements[47] + elements[48] + elements[49] + const2) / factor

    if analizar_est - (const2 / factor) > 0:
        dp7['Test estanqueidad'] = analizar_est
        p7.append('Test estanqueidad')

    #takt_time = 15
    #transformar las p en tiempo

    #set a variable to know if we have optimizate the priorities in the Encliquetados in case that we want to do the same for priorities 4 (p4)
    optimization = 0
    #Get know if we have to optimizate p4 too
    if len(p4) > 20:
        opti_p4 = True
    else:
        opti_p4 = False

    #In case of more thant 20 Encliquetados we will split the first 15 for optimization
    if len(p3) > 20 and len(p3) < 40:
        optimization = 1
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

    elif len(p3)>= 40 and len(p3) < 60:

        optimization = 2
        p10 = copy.deepcopy(p8)
        dp10 = copy.deepcopy(dp8)
        p9 = copy.deepcopy(p7)
        dp9.clear()
        dp9 = copy.deepcopy(dp7)
        p8 = copy.deepcopy(p6)
        dp8 = copy.deepcopy(dp6)
        p7 = copy.deepcopy(p5)
        dp7.clear()
        dp7 = copy.deepcopy(dp5)
        p6 = copy.deepcopy(p4)
        dp6.clear()
        dp6 = copy.deepcopy(dp4)


        #store the dicts to make faster the operation of share in Encliquetados
        dp5 = copy.deepcopy(dp3)
        dp4.clear()
        dp4 = copy.deepcopy(dp3)
        #divide p3 into three
        division = list(chunker_list(p3, 3))

        p5 = division[2]
        p4 = division[1]
        p3 = division[0]

    elif len(p3)>= 60:

        optimization = 3
        p11 = copy.deepcopy(p8)
        dp11 = copy.deepcopy(dp8)
        p10 = copy.deepcopy(p7)
        dp10.clear()
        dp10 = copy.deepcopy(dp7)
        p9 = copy.deepcopy(p6)
        dp9 = copy.deepcopy(dp6)
        p8 = copy.deepcopy(p5)
        dp8.clear()
        dp8 = copy.deepcopy(dp5)
        p7 = copy.deepcopy(p4)
        dp7.clear()
        dp7 = copy.deepcopy(dp4)

        #store the dicts to make faster the operation of share in Encliquetados
        dp6 = copy.deepcopy(dp3)
        dp5 = copy.deepcopy(dp3)
        dp4.clear()
        dp4 = copy.deepcopy(dp3)

        #divide p3 into 4
        division = list(chunker_list(p3, 4))

        p6 = division[3]
        p5 = division[2]
        p4 = division[1]
        p3 = division[0]

        if opti_p4 == True:
            if optimization == 0:
                p9 = copy.deepcopy(p8)
                dp9 = copy.deepcopy(dp8)
                p8 = copy.deepcopy(p7)
                dp8 = copy.deepcopy(dp7)
                p7 = copy.deepcopy(p6)
                dp7 = copy.deepcopy(dp6)
                p6 = copy.deepcopy(p5)
                dp6 = copy.deepcopy(dp5)

                #store the dicts to make faster the operation
                dp5 = copy.deepcopy(dp4)

                #divide p4 in two
                division = list(chunker_list(p4,2))

                p5 = division[1]
                p4 = division[0]

            elif optimization == 1:
                p10 = copy.deepcopy(p9)
                dp10 = copy.deepcopy(dp9)
                p9 = copy.deepcopy(p8)
                dp9.clear()
                dp9 = copy.deepcopy(dp8)
                p8 = copy.deepcopy(p7)
                dp8 = copy.deepcopy(dp7)
                p7 = copy.deepcopy(p6)
                dp7.clear()
                dp7 = copy.deepcopy(dp6)

                #store the dicts to make the operation faster
                dp6 = copy.deepcopy(dp5)

                #divide p5 in two
                division = list(chunker_list(p5,2))

                p6 = division[1]
                p5 = division[0]

            elif optimization == 2:
                p11 = copy.deepcopy(p10)
                dp11 = copy.deepcopy(dp10)
                p10 = copy.deepcopy(p9)
                dp10.clear()
                dp10 = copy.deepcopy(dp9)
                p9 = copy.deepcopy(p8)
                dp9 = copy.deepcopy(dp8)
                p8 = copy.deepcopy(p7)
                dp8.clear()
                dp8 = copy.deepcopy(dp7)

                #store dics
                dp7 = copy.deepcopy(dp6)

                #divide p6
                division = list(chunker_list(p6,2))

                p7 = division[1]
                p6 = division[0]

            elif optimization == 3:
                p12 = copy.deepcopy(p11)
                dp12 = copy.deepcopy(dp11)
                p11 = copy.deepcopy(p10)
                dp11.clear()
                dp11 = copy.deepcopy(dp10)
                p10 = copy.deepcopy(p9)
                dp10 = copy.deepcopy(dp9)
                p9 = copy.deepcopy(p8)
                dp9.clear()
                dp9 = copy.deepcopy(dp8)

                #store dics
                dp8 = copy.deepcopy(dp7)

                #divide p7
                division = list(chunker_list(p7,2))

                p8 = division[1]
                p7 = division[0]



    pendientes = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11,p12]
    dic_pendientes = [dp1, dp2, dp3, dp4, dp5, dp6, dp7, dp8, dp9, dp10, dp11, dp12]

    n = 0
    operarios = {}
    operarios[n] = [[],0]
    for i in range(len(pendientes)):

        if (('Test eléctrico' in dic_pendientes[i]) or ('Test estanqueidad' in dic_pendientes[i])):

            new_dic = copy.deepcopy(dic_pendientes[i])

            for key in new_dic:
                if ((operarios[n][0] == ['extraer cable']) and (operarios[n][1] + dic_pendientes[i][key] <= takt_time)):

                    operarios[n][0].append(key)
                    operarios[n][1] += round(dic_pendientes[i][key],2)
                    operarios[n][1] = round(operarios[n][1],2)
                    pendientes[i].remove(key)
                    dic_pendientes[i].pop(key, None)
                else:
                    n += 1
                    operarios[n] = [[],0]
                    operarios[n][0].append(key)
                    operarios[n][1] = round(dic_pendientes[i][key],2)
                    pendientes[i].remove(key)

                    dic_pendientes[i].pop(key, None)


        while len(pendientes[i]) > 0:
            pt = []
            #iterates over keys in pendientes[i]
            for j in range(len(pendientes[i])):
                #list of times to share out
                pt.append(dic_pendientes[i][pendientes[i][j]])
            #print(pt)
            up_time = takt_time - operarios[n][1]

            #get best combination with takt_time restriction
            # b_comb, b_sum = best(pt,up_time)
            # b_comblist = list(b_comb)

            indexes , b_sum = best(pt,up_time)
            indexes = list(indexes)
            b_sum = round(b_sum,2)
            for index in indexes:

                operarios[n][0].append(pendientes[i][index])
            #Eliminate assigned activities from pendientes
            pendientes[i]= [val for ind, val in enumerate(pendientes[i]) if ind not in indexes]


            #Delete this is there is not bugs
            # #eliminate the combination from p[i] and add to operarios
            # for z in b_comb:
            #     for key in dic_pendientes[i]:
            #     #for key in dict_mtm:
            #         if dic_pendientes[i][key] == z:
            #         #if dict_mtm[key] == z:
            #             operarios[n][0].append(key)
            #             #print(operarios)
            #             pendientes[i].remove(key)
            #             break

            operarios[n][1] += b_sum
            operarios[n][1] = round(operarios[n][1],2)

            if (len(pendientes[i]) > 0):
                n += 1
                operarios[n] = [[],0]
    return(operarios)

def shareOut_multiple(elements, takt_time, factores):
    dict_mtm = {'poner conector grande': 2.59, 'extraer conector grande':1.26, 'poner conector mediano': 3.18, 'extraer conector mediano': 1.35, 'poner conector pequeño': 3.62, 'extraer conector pequeño': 1.73, 'poner interconexión': 4.24, 'extraer interconexión': 1.73, 'junta redonda': 4.73, 'junta plana': 9.15, 'Encliquetado diámetro>1 (<100mm)': 2.70, 'Encliquetado diámetro>1 (100-300mm)':3.20, 'Encliquetado diámetro>1 (300-500mm)': 3.85, 'Encliquetado diámetro>1 (500-750mm)':4.71, 'Encliquetado diámetro>1 (750-1000mm)': 5.47, 'Encliquetado diámetro=0,5-1 (<100mm)': 3.2001, 'Encliquetado diámetro=0,5-1 (100-300mm)': 3.70, 'Encliquetado diámetro=0,5-1 (300-500mm)': 4.35, 'Encliquetado diámetro=0,5-1 (500-750mm)': 5.21, 'Encliquetado diámetro=0,5-1 (750-1000mm)': 5.97, 'Encliquetado diámetro<0,5 (<100mm)': 4.47, 'Encliquetado diámetro<0,5 (100-300mm)': 4.96, 'Encliquetado diámetro<0,5 (300-500mm)': 5.61, 'Encliquetado diámetro<0,5 (500-750mm)': 6.47, 'Encliquetado diámetro<0,5 (750-1000mm)': 7.24, 'Encliquetado interconexión<100mm': 5.52, 'Encliquetado interconexión=100-300mm': 5.92, 'Encliquetado interconexión>300mm': 6.24, 'poner brida simple': 5.43, 'cortar brida simple': 4.14, 'poner brida compleja': 6.79, 'orientar y cortar brida': 5.18, 'colocar lámpara giratoria':6.49, 'colocar lámpara lengueta': 6.05, 'colocar retenedor': 3.20, 'cierre seguridad': 4.50, 'cerrar tapa automática':5.66, 'cerrar tapa libro':3.15, 'cerrar integrado':1.73, 'cerrar independiente': 4.15, 'encintado manual': 9.42, 'encintado manual con posición': 10.81, 'encintado automático': 6.02, 'encintado automático con posición': 7.32, 'embalar cable directo a caja': 2.04, 'embalar cable de plástico a caja':10.36}

    #dp1 = {'poner conector grande': 2.59, 'poner conector mediano': 3.18, 'poner conector pequeño': 3.62,'poner interconexión': 4.24}
    dp1 = {}
    #dp2 = {'junta redonda': 4.73, 'junta plana': 9.15,}
    dp2 = {}
    #dp3 = {'Encliquetado diámetro>1 (<100mm)': 2.70, 'Encliquetado diámetro>1 (100-300mm)':3.20, 'Encliquetado diámetro>1 (300-500mm)': 3.85, 'Encliquetado diámetro>1 (500-750mm)':4.71, 'Encliquetado diámetro>1 (750-1000mm)': 5.47, 'Encliquetado diámetro=0,5-1 (<100mm)': 3.2001, 'Encliquetado diámetro=0,5-1 (100-300mm)': 3.70, 'Encliquetado diámetro=0,5-1 (300-500mm)': 4.35,'Encliquetado diámetro=0,5-1 (500-750mm)': 5.21, 'Encliquetado diámetro=0,5-1 (750-1000mm)': 5.97, 'Encliquetado diámetro<0,5 (<100mm)': 4.47, 'Encliquetado diámetro<0,5 (100-300mm)': 4.96, 'Encliquetado diámetro<0,5 (300-500mm)': 5.61, 'Encliquetado diámetro<0,5 (500-750mm)': 6.47, 'Encliquetado diámetro<0,5 (750-1000mm)': 7.24, 'Encliquetado interconexión<100mm': 5.52, 'Encliquetado interconexión=100-300mm': 5.92, 'Encliquetado interconexión>300mm': 6.24}
    dp3 = {}
    #dp4 = {'poner brida simple': 5.43, 'poner brida compleja': 6.79, 'colocar lámpara giratoria':6.49, 'colocar lámpara lengueta': 6.05, 'colocar retenedor': 3.20, 'cierre seguridad': 4.50, 'cerrar tapa automática':5.66, 'cerrar tapa libro':3.15, 'cerrar integrado':1.73, 'cerrar independiente': 4.15, 'encintado manual': 9.42, 'encintado manual con posición': 10.81, 'encintado automático': 6.02, 'encintado automático con posición': 7.32}
    dp4 = {}
    #dp5 = {'cortar brida simple': 4.14, 'orientar y cortar brida': 5.18}
    dp5 = {}
    #dp6 = { 'extraer conector grande': 1.26, 'extraer conector mediano': 1.35, 'extraer conector pequeño': 1.73, 'extraer interconexión': 1.7301 }
    dp6 = {'extraer cable': 0}
    dp7 = {}
    #dp8 = {'embalar cable directo a caja': 2.04, 'embalar cable de plástico a caja':10.36}
    dp8 = {}
    dp9 = {}
    dp10 = {}
    dp11 = {}
    dp12 = {}

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
    p10 = []
    p11 = []
    p12 = []

    #convert factores into a list of factors
    factors = []
    #factor A
    factors.extend([1]*factores[0])
    #factor B
    factors.extend([0.91]*factores[1])
    #factor c1.1
    factors.extend([0.83]*factores[2])
    #factor c
    factors.extend([0.77]*factores[3])

    #Reverse to start with the lowest factores
    factors.reverse()

    cg = elements[0] #int(input("conectores grandes: "))
    for i in range(cg):
        task = 'poner conector grande'
        task2 = 'extraer conector grande'
        extraer = 'extraer cable'
        p1.append(task)
        dp1[task] = (dict_mtm[task])
        if len(p6) == 0:
            p6.append(extraer)
        dp6[extraer] += dict_mtm[task2]

    cm = elements[1] #int(input("conectores medianos: "))
    for i in range(cm):
        task = 'poner conector mediano'
        task2 = 'extraer conector mediano'
        extraer = 'extraer cable'
        p1.append(task)
        dp1[task] = (dict_mtm[task])
        if len(p6) == 0:
            p6.append(extraer)
        dp6[extraer] += dict_mtm[task2]

    ch = elements[2] #int(input("conectores pequeños: "))
    for i in range(ch):
        task = 'poner conector pequeño'
        task2 = 'extraer conector pequeño'
        extraer = 'extraer cable'
        p1.append(task)
        dp1[task] = (dict_mtm[task])
        if len(p6) == 0:
            p6.append(extraer)
        dp6[extraer] += dict_mtm[task2]

    inter = elements[3] #int(input("conectores pequeños: "))
    for i in range(inter):
        task = 'poner interconexión'
        task2 = 'extraer interconexión'
        extraer = 'extraer cable'
        p1.append(task)
        dp1[task] = (dict_mtm[task])
        if len(p6) == 0:
            p6.append(extraer)
        dp6[extraer] += dict_mtm[task2]

    jun = elements[4] #int(input('junta_redonda: '))
    for i in range(jun):
        task = 'junta redonda'
        p2.append(task)
        dp2[task] = dict_mtm[task]

    jun_p = elements[5] #int(input('junta_plana: '))
    for i in range(jun_p):
        task = 'junta plana'
        p2.append(task)
        dp2[task] = dict_mtm[task]

    en1 = elements[6] #int(input("en_d>1_<100: "))
    for i in range(en1):
        task = 'Encliquetado diámetro>1 (<100mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en2 = elements[7] #int(input('en_d>1_100-300: '))
    for i in range(en2):
        task = 'Encliquetado diámetro>1 (100-300mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en3 = elements[8] #int(input('en_d>1_300-500: '))
    for i in range(en3):
        task = 'Encliquetado diámetro>1 (300-500mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en4 = elements[9] #int(input('en_d>1_500-750: '))
    for i in range(en4):
        task = 'Encliquetado diámetro>1 (500-750mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en5 = elements[10] #int(input('en_d>1_750-1000: '))
    for i in range(en5):
        task = 'Encliquetado diámetro>1 (750-1000mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en6 = elements[11] #int(input('en_d=0,5-1_<100: '))
    for i in range(en6):
        task = 'Encliquetado diámetro=0,5-1 (<100mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en7 = elements[12] #int(input('en_d=0,5-1_100-300: '))
    for i in range(en7):
        task = 'Encliquetado diámetro=0,5-1 (100-300mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en8 = elements[13] #int(input('en_d=0,5-1_300-500: '))
    for i in range(en8):
        task = 'Encliquetado diámetro=0,5-1 (300-500mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en9 = elements[14] #int(input('en_d=0,5-1_500-750: '))
    for i in range(en9):
        task = 'Encliquetado diámetro=0,5-1 (500-750mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en10 = elements[15] #int(input('en_d=0,5-1_750-1000: '))
    for i in range(en10):
        task = 'Encliquetado diámetro=0,5-1 (750-1000mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en11 = elements[16] #int(input('en_d<0,5_<100: '))
    for i in range(en11):
        task = 'Encliquetado diámetro<0,5 (<100mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en12 = elements[17] #int(input('en_d<0,5_100-300: '))
    for i in range(en12):
        task = 'Encliquetado diámetro<0,5 (100-300mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en13 = elements[18] #int(input('en_d<0,5_300-500: '))
    for i in range(en13):
        task = 'Encliquetado diámetro<0,5 (300-500mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en14 = elements[19] #int(input('en_d<0,5_500-750: '))
    for i in range(en14):
        task = 'Encliquetado diámetro<0,5 (500-750mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en15 = elements[20] #int(input('en_d<0,5_750-1000: '))
    for i in range(en15):
        task = 'Encliquetado diámetro<0,5 (750-1000mm)'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en16 = elements[21] #int(input('en_inter_<100: '))
    for i in range(en16):
        task = 'Encliquetado interconexión<100mm'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en17 = elements[22] #int(input('en_inter_100-300: '))
    for i in range(en17):
        task = 'Encliquetado interconexión=100-300mm'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    en18 = elements[23] #int(input('en_inter_>300: '))
    for i in range(en18):
        task = 'Encliquetado interconexión>300mm'
        p3.append(task)
        dp3[task] = dict_mtm[task]

    brs = elements[24] #int(input('bridas simples: '))
    for i in range(brs):
        task = 'poner brida simple'
        task2 = 'cortar brida simple'
        p4.append(task)
        dp4[task] = dict_mtm[task]
        p5.append(task2)
        dp5[task2] = dict_mtm[task2]

    brc = elements[25] #int(input('bridas complejas: '))
    for i in range(brc):
        task = 'poner brida compleja'
        task2 = 'orientar y cortar brida'
        p4.append(task)
        dp4[task] = dict_mtm[task]
        p5.append(task2)
        dp5[task2] = dict_mtm[task2]

    lamp_gr = elements[26] #int(input('lamparas giratorias: '))
    for i in range(lamp_gr):
        task = 'colocar lámpara giratoria'
        p4.append(task)
        dp4[task] = dict_mtm[task]

    lamp_len = elements[27] #int(input('lamparas de lengueta: '))
    for i in range(lamp_len):
        task = 'colocar lámpara lengueta'
        p4.append(task)
        dp4[task] = dict_mtm[task]

    el_s1 = elements[28] #int(input('Retenedores: '))
    for i in range(el_s1):
        task = 'colocar retenedor'
        p4.append(task)
        dp4[task] = dict_mtm[task]

    el_s2 = elements[29] #int(input('cierre_seguridad: '))
    for i in range(el_s2):
        task = 'cierre seguridad'
        p4.append(task)
        dp4[task] = dict_mtm[task]

    el_s3 = elements[30] #int(input('Tapas automaticas: '))
    for i in range(el_s3):
        task = 'cerrar tapa automática'
        p4.append(task)
        dp4[task] = dict_mtm[task]

    el_s4 = elements[31] #int(input('Tapas de libro: '))
    for i in range(el_s4):
        task = 'cerrar tapa libro'
        p4.append(task)
        dp4[task] = dict_mtm[task]

    el_s5 = elements[32] #int(input('integrados: '))
    for i in range(el_s5):
        task = 'cerrar integrado'
        p4.append(task)
        dp4[task] = dict_mtm[task]

    el_s6 = elements[33] #int(input('Independientes: '))
    for i in range(el_s6):
        task = 'cerrar independiente'
        p4.append(task)
        dp4[task] = dict_mtm[task]

    encintado_manual = elements[34] #int(input('Encintados manuales: '))
    for i in range(encintado_manual):
        task = 'encintado manual'
        p4.append(task)
        dp4[task] = dict_mtm[task]

    encintado_manual_posicion = elements[35] #int(input('Encintados manueales con posición: '))
    for i in range(encintado_manual_posicion):
        task = 'encintado manual con posición'
        p4.append(task)
        dp4[task] = dict_mtm[task]

    encintado_automatico = elements[36] #int(input('Encintados automaticos: '))
    for i in range(encintado_automatico):
        task = 'encintado automático'
        p4.append(task)
        dp4[task] = dict_mtm[task]

    encintado_automatico_posicion = elements[37] #int(input('Encintados automaticos con posicion: '))
    for i in range(encintado_automatico_posicion):
        task = 'encintado automático con posición'
        p4.append(task)
        dp4[task] = dict_mtm[task]

    embalar_cable_caja = elements[38] #int(input('Embalar cable directo a caja: '))
    for i in range(embalar_cable_caja):
        task = 'embalar cable directo a caja'
        p8.append(task)
        dp8[task] = dict_mtm[task]

    embalar_cable_plastico = elements[39] #int(input('Embalar cable a bolsa y luego caja: '))
    for i in range(embalar_cable_plastico):
        task = 'embalar cable de plástico a caja'
        p8.append(task)
        dp8[task] = dict_mtm[task]

    # Calculate the time for the electric test and add it if is > 0, const is a constant for the calculation
    const = 4.04
    analizar_el = (elements[40]*1.598 + elements[41]*1.815 + elements[42]*2.068 + const + elements[43])

    if analizar_el - (const) > 0:
        dp7['Test eléctrico'] = analizar_el
        p7.append('Test eléctrico')

    # Do the same as electric test for tightness
    const2 = 5.423
    analizar_est = (elements[44]*2.49 + elements[45]*3.992 + elements[46]*5.653 + elements[47] + elements[48] + elements[49] + const2)

    if analizar_est - (const2) > 0:
        dp7['Test estanqueidad'] = analizar_est
        p7.append('Test estanqueidad')

    #takt_time = 15
    #transformar las p en tiempo

    #set a variable to know if we have optimizate the priorities in the Encliquetados in case that we want to do the same for priorities 4 (p4)
    optimization = 0
    #Get know if we have to optimizate p4 too
    if len(p4) > 20:
        opti_p4 = True
    else:
        opti_p4 = False
    #In case of more thant 20 Encliquetados we will split the first 15 for optimization
    if len(p3) > 20 and len(p3) < 40:

        optimization = 1
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

    elif len(p3)>= 40 and len(p3) < 60:

        optimization = 2
        p10 = copy.deepcopy(p8)
        dp10 = copy.deepcopy(dp8)
        p9 = copy.deepcopy(p7)
        dp9.clear()
        dp9 = copy.deepcopy(dp7)
        p8 = copy.deepcopy(p6)
        dp8 = copy.deepcopy(dp6)
        p7 = copy.deepcopy(p5)
        dp7.clear()
        dp7 = copy.deepcopy(dp5)
        p6 = copy.deepcopy(p4)
        dp6.clear()
        dp6 = copy.deepcopy(dp4)


        #store the dicts to make faster the operation of share in Encliquetados
        dp5 = copy.deepcopy(dp3)
        dp4.clear()
        dp4 = copy.deepcopy(dp3)
        #divide p3 into three
        division = list(chunker_list(p3, 3))

        p5 = division[2]
        p4 = division[1]
        p3 = division[0]

    elif len(p3)>= 60:

        optimization = 3
        p11 = copy.deepcopy(p8)
        dp11 = copy.deepcopy(dp8)
        p10 = copy.deepcopy(p7)
        dp10.clear()
        dp10 = copy.deepcopy(dp7)
        p9 = copy.deepcopy(p6)
        dp9 = copy.deepcopy(dp6)
        p8 = copy.deepcopy(p5)
        dp8.clear()
        dp8 = copy.deepcopy(dp5)
        p7 = copy.deepcopy(p4)
        dp7.clear()
        dp7 = copy.deepcopy(dp4)

        #store the dicts to make faster the operation of share in Encliquetados
        dp6 = copy.deepcopy(dp3)
        dp5 = copy.deepcopy(dp3)
        dp4.clear()
        dp4 = copy.deepcopy(dp3)

        #divide p3 into 4
        division = list(chunker_list(p3, 4))

        p6 = division[3]
        p5 = division[2]
        p4 = division[1]
        p3 = division[0]

    if opti_p4 == True:
        if optimization == 0:
            p9 = copy.deepcopy(p8)
            dp9 = copy.deepcopy(dp8)
            p8 = copy.deepcopy(p7)
            dp8 = copy.deepcopy(dp7)
            p7 = copy.deepcopy(p6)
            dp7 = copy.deepcopy(dp6)
            p6 = copy.deepcopy(p5)
            dp6 = copy.deepcopy(dp5)

            #store the dicts to make faster the operation
            dp5 = copy.deepcopy(dp4)

            #divide p4 in two
            division = list(chunker_list(p4,2))

            p5 = division[1]
            p4 = division[0]

        elif optimization == 1:
            p10 = copy.deepcopy(p9)
            dp10 = copy.deepcopy(dp9)
            p9 = copy.deepcopy(p8)
            dp9.clear()
            dp9 = copy.deepcopy(dp8)
            p8 = copy.deepcopy(p7)
            dp8 = copy.deepcopy(dp7)
            p7 = copy.deepcopy(p6)
            dp7.clear()
            dp7 = copy.deepcopy(dp6)

            #store the dicts to make the operation faster
            dp6 = copy.deepcopy(dp5)

            #divide p5 in two
            division = list(chunker_list(p5,2))

            p6 = division[1]
            p5 = division[0]

        elif optimization == 2:
            p11 = copy.deepcopy(p10)
            dp11 = copy.deepcopy(dp10)
            p10 = copy.deepcopy(p9)
            dp10.clear()
            dp10 = copy.deepcopy(dp9)
            p9 = copy.deepcopy(p8)
            dp9 = copy.deepcopy(dp8)
            p8 = copy.deepcopy(p7)
            dp8.clear()
            dp8 = copy.deepcopy(dp7)

            #store dics
            dp7 = copy.deepcopy(dp6)

            #divide p6
            division = list(chunker_list(p6,2))

            p7 = division[1]
            p6 = division[0]

        elif optimization == 3:
            p12 = copy.deepcopy(p11)
            dp12 = copy.deepcopy(dp11)
            p11 = copy.deepcopy(p10)
            dp11.clear()
            dp11 = copy.deepcopy(dp10)
            p10 = copy.deepcopy(p9)
            dp10 = copy.deepcopy(dp9)
            p9 = copy.deepcopy(p8)
            dp9.clear()
            dp9 = copy.deepcopy(dp8)

            #store dics
            dp8 = copy.deepcopy(dp7)

            #divide p7
            division = list(chunker_list(p7,2))

            p8 = division[1]
            p7 = division[0]




    pendientes = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
    dic_pendientes = [dp1, dp2, dp3, dp4, dp5, dp6, dp7, dp8, dp9, dp10, dp11, dp12]

    n = 0
    operarios = {}
    #add factores to operarios
    operarios[n] = [[],0,factors[n]]
    for i in range(len(pendientes)):

        if (('Test eléctrico' in dic_pendientes[i]) or ('Test estanqueidad' in dic_pendientes[i])):

            new_dic = copy.deepcopy(dic_pendientes[i])

            for key in new_dic:
                if ((operarios[n][0] == ['extraer cable']) and (operarios[n][1] + (dic_pendientes[i][key] / operarios[n][2]) <= takt_time)):

                    operarios[n][0].append(key)
                    operarios[n][1] += round(dic_pendientes[i][key],2)
                    pendientes[i].remove(key)

                    dic_pendientes[i].pop(key, None)
                else:
                    n += 1
                    try:
                        operarios[n] = [[],0,factors[n]]
                    except IndexError:
                        operarios[n] = [[],0,1]
                    operarios[n][0].append(key)
                    operarios[n][1] = round(dic_pendientes[i][key],2)
                    operarios[n][1] = round(operarios[n][1],2)
                    pendientes[i].remove(key)

                    dic_pendientes[i].pop(key, None)


        while len(pendientes[i]) > 0:
            pt = []
            #iterates over keys in pendientes[i]
            for j in range(len(pendientes[i])):
                #list of times to share out
                pt.append((dic_pendientes[i][pendientes[i][j]]) / operarios[n][2])
            #print(pt)
            up_time = takt_time - operarios[n][1]

            #get best combination with takt_time restriction
            indexes , b_sum = best(pt,up_time)
            indexes = list(indexes)
            b_sum = round(b_sum,2)
            for index in indexes:

                operarios[n][0].append(pendientes[i][index])
            #Eliminate assigned activities from pendientes
            pendientes[i]= [val for ind, val in enumerate(pendientes[i]) if ind not in indexes]

            operarios[n][1] += b_sum
            operarios[n][1] = round(operarios[n][1],2)
            if (len(pendientes[i]) > 0):
                n += 1
                try:
                    operarios[n] = [[],0,factors[n]]
                except IndexError:
                    operarios[n] = [[],0,1]
    return(operarios)
