# -*- coding: utf-8 -*-
"""
Spyder Editor

Programa de estructuras V1.1.01.22 desarrollado por Tomás Soto
Date 11-25-2021
"""
print('******************************')
print('*** CALCULO DE ESTRUCTURAS ***')
print('******************************')
#___________________________________________________________________
N_Ejes_H = int(input('Numero de ejes horizontales: '))
N_Ejes_V = int(input('Numero de ejes verticales: '))
EjesH = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#___________________________________________________________________
EjesV = []
Dist_EjesH = []
Dist_EjesV = []
Long_tramo_losa = {}
Cargas_losas = {}
Dist_cargas_losas = {}
Area_distribuida = {}
Dist_paredes_punt = {}
Dist_paredes_dist_inicio = {}
Dist_paredes_dist_longitud = {}
Altura_paredes = {}
Tipo_viga = ['Horizontal', 'Vertical']
PesoLosa = {'Maciza 10cm ': 240, 'Nervada 1D':162, 'Nervada 2D':200}
print('\n*** Ejes horizontales ***')
for eje in range(N_Ejes_H):
    print('Eje %s' %EjesH[eje])
print('\n*** Ejes verticales ***')
for eje in range(N_Ejes_V):
    EjesV.append(str(eje+1))
    print('Eje %s' %EjesV[eje])
print('\n*** Distancia entre Ejes horizontales ***')
for dist in range(N_Ejes_H - 1):
    Dist_EjesH.append(float(input('Distancia entre el eje [%s]' %EjesH[dist] +
        ' y el eje [%s]: ' %EjesH[dist+1])))
print('\n*** Distancia entre Ejes verticales ***')
for dist in range(N_Ejes_V - 1):
    Dist_EjesV.append(float(input('Distancia entre el eje [%s]' %EjesV[dist] + 
        ' y el eje [%s]: ' %EjesV[dist+1])))
print()
TipoLosa = {0:'Maciza 10 cm ', 1:'Nervada 1D', 2:'Nervada 2D'}
PesoLosa = {'Maciza 10 cm ': 240, 'Nervada 1D':162, 'Nervada 2D':200}
#___________________________________________________________________
def Calculo_peso_losa():
    def Escoger_losa():
        n=0
        print('TIPO DE LOSA QUE SOPORTA LA VIGA\n')
        for i in TipoLosa:
            print('[%i]' %n,'Tipo: %s' %TipoLosa[i])
            n+=1
    Escoger_losa()   
    Opcion_losa = int(input('Escoja una opcion: '))
    while Opcion_losa < 0 or Opcion_losa > 2:
        print('Opcion equivocada!!\n')
        Escoger_losa()
        Opcion_losa = int(input('Escoja una opcion: '))
    print('\n*** El tipo de losa es %s ***\n' %TipoLosa[Opcion_losa])
    return PesoLosa[TipoLosa[Opcion_losa]]
#___________________________________________________________________
pesolosa = round(Calculo_peso_losa(),2)
print('El peso de la losa es %i Kg/m2' %pesolosa)
PesoViga = {}
b_ant = 0
h_ant = 0
#___________________________________________________________________
def Peso_viga(eje):
    print('\n*** Dimensiones de la sección de la viga %s ***' %eje)
    b = int(input('Base de la viga "b" (cm): '))
    while b<15 or b>50:
        print('Valor inaceptable!')
        b = int(input('Base de la viga "b" (cm): '))
    h = int(input('Altura de la viga "h" (cm): '))
    while h<20 or h>70:
        print('Valor inaceptable!')
        h = int(input('Altura de la viga "h" (cm): '))    
    PesoPropio = b*h*2400/10000
    print('\nEl peso propio de la viga es de %.2f Kg/ml (peso ' %PesoPropio + 
          'específico del concreto de 2400 Kg/m3')
    return PesoPropio, b, h
#___________________________________________________________________
#   CARGA DISTRIBUIDA POR LOSA
Base_viga = {}
Altura_viga = {}
for carga in range(N_Ejes_H):
    print('\n*** Eje [%s] ***' %EjesH[carga])
    Cargas_losas[EjesH[carga]] = []
    Area_distribuida[EjesH[carga]] = []
    Distancia_losa = []
    Dist_cargas_losas[EjesH[carga]] = []
    Numero_tramos_losa = input('Número de tramos de la viga "%s" con distinta área ' 
                               %EjesH[carga] + 'tributaria \n(ENTER para (1) un tramo): ')
    if Numero_tramos_losa != '':
        Numero_tramos_losa = int(Numero_tramos_losa)
    else:
        Numero_tramos_losa = 1
    Long_tramo_losa[EjesH[carga]] = []
    PesoViga[EjesH[carga]], Base_viga[EjesH[carga]], Altura_viga[EjesH[carga]] = Peso_viga(EjesH[carga])
    for tramo in range(Numero_tramos_losa):
        print('\n*** Viga %s' %EjesH[carga], ' Tramo %i ***' %(tramo+1))
        if tramo != 0:
            print('La longitud del tramo anterior es %.2f' 
                  %Dist_cargas_losas[EjesH[carga]][tramo-1][1])
            Distancia_losa.append(Dist_cargas_losas[EjesH[carga]][tramo-1][0] + 
                                  Dist_cargas_losas[EjesH[carga]][tramo-1][1])
            print('El tramo %i' %(tramo+1), 'empieza en %.2f metros' %Distancia_losa[-1])
            Distancia_losa.append(float(input('Longitud de área: ')))
        else:
            Distancia_losa.append(0)
            if Numero_tramos_losa == 1:
                print('El tramo termina en %.2f' %Dist_EjesV[-1])
                Distancia_losa.append(Dist_EjesV[-1])
            else:
                Distancia_losa.append(float(input('Longitud de área: ')))
        Dist_cargas_losas[EjesH[carga]].append(Distancia_losa)
        Distancia_losa = []
        if EjesH[0] == EjesH[carga]:
            Long_tramo = input('Area tributaria de la viga ' + EjesH[carga] + 
                               ' en el tramo %i para la losa\n(ENTER ' %(tramo+1) + 
                           'si es %.2f m): ' %(float(Dist_EjesH[carga]/2)))      
            if Long_tramo != '':
                Long_tramo = float(Long_tramo)
            else:
                Long_tramo = float(Dist_EjesH[carga]/2)
        elif EjesH[N_Ejes_H-1] == EjesH[carga]:
            Long_tramo = input('Area tributaria de la viga ' + EjesH[carga] + 
                               ' en el tramo %i para la losa\n(ENTER ' %(tramo+1) + 
                           'si es %.2f m): ' %(float(Dist_EjesH[carga-1]/2)))
            if Long_tramo != '':
                Long_tramo = float(Long_tramo)
            else:
                Long_tramo = float(Dist_EjesH[carga-1]/2)
        else:
            Long_tramo = input('Area tributaria de la viga ' + EjesH[carga] + 
                               ' en el tramo %i para la losa\n (ENTER para' 
                               %(tramo+1) + ' cálculo automatico): ')
            if Long_tramo == '':
                Long_tramo = float((Dist_EjesH[carga-1]+Dist_EjesH[carga])/2)
            else: 
                Long_tramo = float(Long_tramo)
            print('El área tributaria es %.2f m' %Long_tramo)
        Long_tramo_losa[EjesH[carga]].append(Long_tramo)
        Cargas_losas[EjesH[carga]].append(round(pesolosa*Long_tramo + 
                                                PesoViga[EjesH[carga]], 2))
        Area_distribuida[EjesH[carga]].append(Long_tramo)
        print('La carga por losa incluyendo el peso propio de la viga para el tramo %i es de' 
              %(tramo+1), '%.2f Kg/m' 
              %Cargas_losas[EjesH[carga]][tramo])
Cargas_puntuales = {}
Cargas_distribuidas = {}
#_____________________________________________________________________________
def Tipo_pared(L_viga, H_pared):
    Peso_Espesor = [180, 210, 240]
    Opciones = ['0', '1', '2']
    Tipo_espesor = input('\n*** Escoja espesor de pared ***\n[0] 10 cm' +
                             '\n[1] 15 Un lado frisado\n[2] 15 cm ambas '+ 
                             'caras frisadas\nEscoja una opción: ')
    while not Tipo_espesor in Opciones:
        print('ENTRADA INVALIDA!!')
        Tipo_espesor = input('\n*** Escoja espesor de pared ***\n[0] 10 cm' +
                                 '\n[1] 15 Un lado frisado\n[2] 15 cm ambas '+ 
                                 'caras frisadas\nEscoja una opción: ')
    Tipo_espesor = int(Tipo_espesor)
    print('Longitud de viga = %.2f' %L_viga)
    print('La altura de la pared es %.2f metros' %H_pared)
    Peso = round(L_viga * H_pared * Peso_Espesor[Tipo_espesor],2)
    return Peso                  
#_____________________________________________________________________________
Par_dist_carga = {}
print('\n----------- La variable carga = %i -----------\n' %carga)
for carga in range(N_Ejes_H):
    Par_dist_carga[EjesH[carga]] = {}
    print('--------------------------------------------------\n')
    print('\n*** Paredes perpendiculares en la viga %s ***' %EjesH[carga])   
    #   ENTRADA DE DATOS DE PAREDES PERPENDICULARES AL EJE DE LA VIGA
    N_paredes_punt = input('Número de paredes perpendiculares a '+'la viga'+
                           ' %s\n(ENTER para ninguna): ' %EjesH[carga])
    if N_paredes_punt != '':
        N_paredes_punt = int(N_paredes_punt)
        Cargas_puntuales[EjesH[carga]] = []
        Dist_paredes_punt[EjesH[carga]] = []
        for pared in range(N_paredes_punt): 
            L = float(input('Longitud de la pared %i perpendicular Viga ' %(pared+1) +
                      '%s: ' %EjesH[carga]))
            h = float(input('Altura de la pared: '))
            Peso = round(Tipo_pared(L, h), 2)
            print('El peso de la pared es de %.2f Kg' %Peso)
            Cargas_puntuales[EjesH[carga]].append(round(1.4*Peso, 2))
            Dist_paredes_punt[EjesH[carga]].append(float(input('Distancia desde' 
                + ' el eje %s hasta la ' %EjesV[0] + 'pared %i' %(pared+1) + 
                ' perpendicular: ')))
            #   VERIFICAR QUE LAS PAREDES NO SE UBICAN EN EL MISMO SITIO
            if N_paredes_punt > 1 and pared != 0:
                print('\n*** Verificación de ubicación de las paredes ***\n')
                while Dist_paredes_punt[EjesH[carga]][-2] == Dist_paredes_punt[EjesH[carga]][-1]:
                    print('Distancia %i = ' %(pared+1),'%.2f es igual a Distancia' 
                          %Dist_paredes_punt[EjesH[carga]][-2], str(pared+1) + 
                          '=%.2f\tDistancia inaceptable!' 
                          %Dist_paredes_punt[EjesH[carga]][-1])
                    Dist_paredes_punt[EjesH[carga]].pop()
                    Dist_paredes_punt[EjesH[carga]].append(float(input('Distancia desde' 
                    + ' el eje %s hasta la ' %EjesV[0] + 'pared %i' %(pared+1) + 
                    ' perpendicular: ')))
            print('La carga puntual en [%s] es de' %EjesH[carga], '%.2f Kg'
                  %Peso, 'ubicada a %.2f metros' 
                  %Dist_paredes_punt[EjesH[carga]][pared])
            Par_dist_carga[EjesH[carga]][Dist_paredes_punt[EjesH[carga]][pared]] = -Cargas_puntuales[EjesH[carga]][-1]
    print('Las cargas puntuales son', Par_dist_carga)
#_____________________________________________________________________________    
    #   ENTRADA DE DATOS DE PAREDES PARALELAS AL EJE DE LA VIGA
    print('\n*** PAREDES PARALELAS A LAS VIGAS ***\n')
    Dist_paredes_dist_inicio[EjesH[carga]] = []
    Dist_paredes_dist_longitud[EjesH[carga]] = []
    Cargas_distribuidas[EjesH[carga]] = []
    Altura_paredes[EjesH[carga]] = []
    pared = 0
    x = 0
    for tramo in range(len(Cargas_losas[EjesH[carga]])):
        print('*** VIGA %s ' %EjesH[carga], 'TRAMO %i ***' %(tramo+1))
        if tramo != 0:
            h_pared = input('Altura de pared en el tramo %i' %(tramo+1) + 
                        ' de la viga %s\n' %EjesH[carga] +  
                        '\n(L = %.2f m)' %Dist_cargas_losas[EjesH[carga]][tramo][1] +
                        ' ENTER para altura' + 
                        ' = %.2f metros: ' %Altura_paredes[EjesH[carga]][-1])
        else:
            h_pared = input('Altura de pared en el tramo %i' %(x+1) + 
                        ' de la viga %s (0 si no hay pared)\n' %EjesH[carga] + 
                        'L = %.2f m: ' %Dist_cargas_losas[EjesH[carga]][tramo][1]) 
        if h_pared == '':
            h_pared = Altura_paredes[EjesH[carga]][-1]
        else:
            h_pared = float(h_pared)
            while h_pared > 4:
                print('La altura debe ser menor a 4 m')
                h_pared = input('Altura de pared en el tramo %i' %(x+1) + 
                            ' de la viga %s (0 si no hay pared)\n' %EjesH[carga] + 
                            'L = %.2f m: ' %Dist_cargas_losas[EjesH[carga]][tramo][1])
                if h_pared == '':
                    h_pared = Altura_paredes[EjesH[carga]][-1]
                else:
                    h_pared = float(h_pared)
        Altura_paredes[EjesH[carga]].append(h_pared)
        Dist_paredes_dist_inicio[EjesH[carga]].append(Dist_cargas_losas[EjesH[carga]][tramo][0])
        Dist_paredes_dist_longitud[EjesH[carga]].append(Dist_cargas_losas[EjesH[carga]][tramo][1])
        if h_pared != 0.0:
            Peso = round(Tipo_pared(1, h_pared),2)
            print('El peso de la pared es de %.2f Kg/m' %Peso)
            print('La carga distribuida por pared paralela en [%s] es de' 
                  %EjesH[carga], '%.2f Kg' %Peso)
        else:
            Peso = 0.0
            print('El peso de la pared es de %.2f Kg/m porque no hay pared' %Peso)
        Cargas_distribuidas[EjesH[carga]].append(Peso) 
        x+=1
#_____________________________________________________________________________            
print('\n*** DATOS ***\n')
print('El peso propio de las vigas son: ' ,PesoViga)
print('Las cargas por losa son: ', Cargas_losas)   
print('Las cargas puntuales son: ', Cargas_puntuales)
print('Las cargas distribuidas por paredes son: ', Cargas_distribuidas)
print('Los inicio de las paredes longitudinales son: ', Dist_paredes_dist_inicio)
print('Las longitudes de las paredes longitudinales son: ', Dist_paredes_dist_longitud)
print('Las paredes puntuales se encuentran ubicadas en: ', Dist_paredes_punt)
print('Las distancias de las cargas en la losa son ', Dist_cargas_losas)
print('Las áreas tributarias de las vigas son ', Area_distribuida)
input('(Pausa...)')
#_____________________________________________________________________________
#   CALCULO DE LAS CARGAS ULTIMAS
Carga_ultima = {}
print('______________________________________________________________________')
print('\n\nUso de edificación\n')
Tipo_Uso = {'0':'Residencia', '1':'Oficinas', '2':'Depósito', '3':'Educativo'}
Carga_Uso = {'0':192, '1':240, '2':780, '3':383}
print('\n*** CALCULO DE CARGA ULTIMA ***')
print('\nSelección','\tUso', '\tKg/m2\n-------------------------------')
for dato in Tipo_Uso:
    print('\t%s\t' %dato, '\t%s' %Tipo_Uso[dato], '\t%i' %Carga_Uso[dato])
Op_Carga_Viva = input('Seleccione opción: ')
while (Op_Carga_Viva in Carga_Uso.keys()) == False:
    for dato in Tipo_Uso:
        print('\t%s\t' %dato, '\t%s' %Tipo_Uso[dato], '\t%i' %Carga_Uso[dato])
    Op_Carga_Viva = input('Seleccione opción: ')
print('La carga viva para %s' %Tipo_Uso[Op_Carga_Viva], 'corresponde a %i Kg/m2' 
      %Carga_Uso[Op_Carga_Viva])
print('______________________________________________________________________')
print('\n*** CALCULO DE LAS CARGAS ULTIMAS ***')
Longitud_viga = {}
for eje in range(N_Ejes_H):
    print('\n*** EJE %s ***' %EjesH[eje])
    Carga_ultima[EjesH[eje]] = []
    x = 0
    print('Hay %i tramos' %len(Long_tramo_losa[EjesH[eje]]))
    for tramo in Long_tramo_losa[EjesH[eje]]:
        Carga_ultima[EjesH[eje]].append(round(1.4*(Cargas_losas[EjesH[eje]][x] +
                                             Cargas_distribuidas[EjesH[eje]][x])+
                                        1.7*(tramo*Carga_Uso[Op_Carga_Viva]), 2))
        print('La carga última en el tramo %i es' %(x+1), '%.2f Kg/ml' 
              %Carga_ultima[EjesH[eje]][x])
        print('En el tramo %i' %(x+1), 'la longitud es %.2f m' %Dist_cargas_losas[EjesH[eje]][x][1] )
        if x == 0:
            Longitud_viga[EjesH[eje]] = Dist_cargas_losas[EjesH[eje]][x][1]
        else:
            Longitud_viga[EjesH[eje]] += Dist_cargas_losas[EjesH[eje]][x][1]
        print('La longitud acumulada %.2f metros' %Longitud_viga[EjesH[eje]])
        x+=1
print('______________________________________________________________________\n')
print('*** CALCULO DE REACCIONES ***')
Reacciones = {}; Dist_Apoyo = {}
SumaFuerzasVert = {}
for eje in range(N_Ejes_H):
    Reacciones[EjesH[eje]] = []
    Reacciones[EjesH[eje]].append(0)
    Dist_Apoyo[EjesH[eje]] = []
    SumaFuerzasVert[EjesH[eje]] = 0.0
    print('\n*** Eje %s ***' %EjesH[eje])
    Dist_Apoyo1 = input('Distancia desde el borde izquierdo de la viga hasta el' +  
                        'apoyo izquierdo\n(ENTER para 0 m): ')
    Dist_Apoyo2 = input('Distancia desde el borde izquierdo de la viga hasta el' + 
                        ' apoyo derecho\n(ENTER para apoyo en %s m): ' %Longitud_viga[EjesH[eje]])
    if Dist_Apoyo1 == '':
        Dist_Apoyo[EjesH[eje]].append(0)
    else:
        Dist_Apoyo[EjesH[eje]].append(float(Dist_Apoyo1))
    if Dist_Apoyo2 == '':
        Dist_Apoyo[EjesH[eje]].append(Longitud_viga[EjesH[eje]])
    else:
        Dist_Apoyo[EjesH[eje]].append(float(Dist_Apoyo2))
    print('Las cargas ultimas de la viga %s son' %EjesH[eje], Carga_ultima[EjesH[eje]])
    if EjesH[eje] in Cargas_puntuales:
        print('Las cargas puntuales de la viga %s son' %EjesH[eje], Cargas_puntuales[EjesH[eje]])
    else:
        print('La viga %s no tiene cargas puntuales' %EjesH[eje])
    Momento_cargas = 0.0
    #_________________________________________________________
    print('\n*** CALCULO DE LOS MOMENTOS ACTUANTES ***')
    x = 0
    for carga in Carga_ultima[EjesH[eje]]:
        Momento_cargas += round(carga*Dist_cargas_losas[EjesH[eje]][x][1]*
                                (Dist_cargas_losas[EjesH[eje]][x][1]/2 + 
                                 Dist_cargas_losas[EjesH[eje]][x][0] - 
                                 Dist_Apoyo[EjesH[eje]][0]))
        SumaFuerzasVert[EjesH[eje]] += carga*Dist_cargas_losas[EjesH[eje]][x][1]
        x += 1
    x = 0
    if EjesH[eje] in Cargas_puntuales:
        for carga in Cargas_puntuales[EjesH[eje]]:
            Momento_cargas += round(carga*Dist_paredes_punt[EjesH[eje]][x], 2)
            SumaFuerzasVert[EjesH[eje]] += carga
            x += 1
    Reacciones[EjesH[eje]].append(round(Momento_cargas/(Dist_Apoyo[EjesH[eje]][1]
                                                        - Dist_Apoyo[EjesH[eje]][0]), 2))
    Reacciones[EjesH[eje]][0] = round(SumaFuerzasVert[EjesH[eje]] - Reacciones[EjesH[eje]][1], 2)
    print('La reacción en el apoyo izquierdo es %.2f Kg' %Reacciones[EjesH[eje]][0], 
          'ubicada en %.2f m' %Dist_Apoyo[EjesH[eje]][0])
    print('La reacción en el apoyo derecho es %.2f Kg' %Reacciones[EjesH[eje]][1], 
          'ubicada en %.2f m' %Dist_Apoyo[EjesH[eje]][1])
    Par_dist_carga[EjesH[eje]][Dist_Apoyo[EjesH[eje]][0]] = Reacciones[EjesH[eje]][0]
    Par_dist_carga[EjesH[eje]][Dist_Apoyo[EjesH[eje]][1]] = Reacciones[EjesH[eje]][1]
print('Los pares distancia/cargas son', Par_dist_carga)
N_cargas = {}
#_________________________________________________________________
print('\n*** CALCULO DE NUMERO DE CARGAS TOTALES ***')
Dist_final_cargas = {}
for eje in range(N_Ejes_H):
    x = 0
    Dist_final_cargas[EjesH[eje]] = []
    print('\n*** VIGA %s ***\n' %EjesH[eje])
    N_cargas[EjesH[eje]] = len(Reacciones[EjesH[eje]]) + len(Carga_ultima[EjesH[eje]])
    if EjesH[eje] in Dist_paredes_punt:        
        N_cargas[EjesH[eje]] += len(Dist_paredes_punt[EjesH[eje]])
        for tramo in range(len(Dist_paredes_punt[EjesH[eje]])):
            if not Dist_paredes_punt[EjesH[eje]][tramo] in Dist_cargas_losas[EjesH[eje]][0]:
                N_cargas[EjesH[eje]] += 1
    else:
        print('No hay cargas puntuales en la viga %s' %EjesH[eje])
    for x in range(len(Dist_cargas_losas[EjesH[eje]])):
        Dist_final_cargas[EjesH[eje]].append(Dist_cargas_losas[EjesH[eje]][x][0] 
                + Dist_cargas_losas[EjesH[eje]][x][1])
        x += 1
    print('En la viga %s hay' %EjesH[eje], '%i cargas' %N_cargas[EjesH[eje]])
print('\nLas cargas son: ', N_cargas)
#_________________________________________________________________
print('\n*** ORDENACION DE LAS SOLICITACIONES ***')
Pos_cargas = {}
Tramo_carga = {}
Tipo_carga = {}
Distancia_tipocarga = {}
#_________________________________________________________________
for eje in range(N_Ejes_H):
    print('\n*** ALMACENAMIENTO DE LOS TRAMOS DE LAS SOLICITACIONES ***')
    print('*** VIGA %s ***\n' %EjesH[eje])
    Tipo_carga[EjesH[eje]] = []
    Pos_cargas[EjesH[eje]] = []
    Aplicacion = {}
    x = 0; y = 0
    for tramo in Dist_cargas_losas[EjesH[eje]]:
        for dist_puntual in Dist_Apoyo[EjesH[eje]]:
            if dist_puntual == tramo[0] or dist_puntual == (tramo[0]+tramo[1]):
                print('La distancia del apoyo es %.2f m' %dist_puntual)
                print('El tramo es', tramo)
                Tipo_carga[EjesH[eje]].append(1) 
                Pos_cargas[EjesH[eje]].append(dist_puntual)
                print('*** Aqui se almacena la variable Pos_carga =', Pos_cargas, 
                      ' ***')
                x += 1
            elif dist_puntual > tramo[0] and dist_puntual < (tramo[0]+tramo[1]):
                Tipo_carga[EjesH[eje]].append(1) 
                Pos_cargas[EjesH[eje]].append(dist_puntual)
                x += 1
        if EjesH[eje] in Dist_paredes_punt:
            for dist_puntual in Dist_paredes_punt[EjesH[eje]]:
                if dist_puntual == tramo[0] or dist_puntual == (tramo[0]+ tramo[1]):
                    Tipo_carga[EjesH[eje]].append(-1) 
                    Pos_cargas[EjesH[eje]].append(dist_puntual)
                    y += 1
                elif dist_puntual > tramo[0] and dist_puntual < (tramo[0]+tramo[1]):
                    Tipo_carga[EjesH[eje]].append(-1) 
                    Pos_cargas[EjesH[eje]].append(dist_puntual)
                    y += 1
        Pos_cargas[EjesH[eje]].sort()
    print('La posición de las cargas son ', Pos_cargas[EjesH[eje]])  
    #_____________________________________________
    x = 0   #   Contador de tramos absolutos
    print('\n*** ALMACENAMIENTO DE LOS EXTREMOS PARA LOS TRAMOS ***\n')
    print('*** Viga %s ***\n' %EjesH[eje])
    Tramo_carga[EjesH[eje]] = []
    for tramo in Dist_cargas_losas[EjesH[eje]]:
        Tramo_carga[EjesH[eje]].append(tramo[0])
        Tramo_carga[EjesH[eje]].append(tramo[0]+tramo[1])
        y = 0   #   Contador de tramos parciales
        z = 0   #   Contador de cargas puntuales
        for punt in Pos_cargas[EjesH[eje]]:
            if punt > tramo[0] and punt < (tramo[0]+tramo[1]):
                if not punt in Tramo_carga[EjesH[eje]]:
                    Tramo_carga[EjesH[eje]].append(punt)
    for tramo in Tramo_carga[EjesH[eje]]:
        while Tramo_carga[EjesH[eje]].count(tramo) > 1:
            Tramo_carga[EjesH[eje]].remove(tramo)
    Tramo_carga[EjesH[eje]].sort()
    for carga in Pos_cargas[EjesH[eje]]:
        if EjesH[eje] in Dist_paredes_punt:
            for punt in Dist_paredes_punt[EjesH[eje]]:
                if punt == carga:
                    Aplicacion[carga] = -1
        for punt in Dist_Apoyo[EjesH[eje]]:
            if punt == carga:
                Aplicacion[carga] = 1
    Distancia_tipocarga[EjesH[eje]] = Aplicacion
print('Los cargas en las vigas están en ', Pos_cargas) 
print('Los tramos de carga son', Tramo_carga) 
print('Las distancias y el tipo de cargas son', Distancia_tipocarga)
input('Pausa...') 
#________________________________________________       
print('\n*** CALCULO DE LOS TRAMOS PARA LAS CARGAS DISTRIBUIDAS ***')
Tramo_carga_dist = {}
Vector_final_solicitaciones = {}
Long_tramo = {}
Dist_aplicacion_cargas = {}
for eje in range(N_Ejes_H):
    print('\n*** Viga %s ***\n' %EjesH[eje])
    Tramo_carga_dist[EjesH[eje]] = []
    for tramo in Tramo_carga[EjesH[eje]]:
        x = 0
        for carga_dist in Dist_cargas_losas[EjesH[eje]]:
            if tramo > 0:
                if tramo <= (carga_dist[0] + carga_dist[1]) and tramo > carga_dist[0]:                
                    Tramo_carga_dist[EjesH[eje]].append(-Carga_ultima[EjesH[eje]][x])
            x += 1
#________________________________________________
#   Unificación de cargas puntuales con cargas distribuidas       
    Vector_final_solicitaciones[EjesH[eje]] = []
    Dist_aplicacion_cargas[EjesH[eje]] = []
    Tipo_carga[EjesH[eje]] = []
    Long_tramo[EjesH[eje]] = []
    a = 0
    for dist in Tramo_carga[EjesH[eje]]:
        if dist in Par_dist_carga[EjesH[eje]]:
            Vector_final_solicitaciones[EjesH[eje]].append(Par_dist_carga[EjesH[eje]][dist])
            Tipo_carga[EjesH[eje]].append(1)
        if dist != Tramo_carga[EjesH[eje]][-1]:
            Vector_final_solicitaciones[EjesH[eje]].append(Tramo_carga_dist[EjesH[eje]][a])
            Tipo_carga[EjesH[eje]].append(2)
            a += 1
            Long_tramo[EjesH[eje]].append(Tramo_carga[EjesH[eje]][a]-dist)
    a = 0; b = 0
    for dist_aplicacion in Tipo_carga[EjesH[eje]]:
        if dist_aplicacion == 1:
            Dist_aplicacion_cargas[EjesH[eje]].append(Pos_cargas[EjesH[eje]][a])
            a += 1
        else:
            Dist_aplicacion_cargas[EjesH[eje]].append(Tramo_carga[EjesH[eje]][b])
            b += 1
print('Las cargas ordenadas son', Vector_final_solicitaciones, '\nLos tipos de cargas son', Tipo_carga)

print('Los tipos de carga son', Tipo_carga)
print('Las longitudes de los tramos son', Long_tramo)
print('Las distancias de aplicacion de las cargas son', Dist_aplicacion_cargas)
Long_tramo_totales = {}
for eje in range(N_Ejes_H):
    Long_tramo_totales[EjesH[eje]] = []
    a = 0
    for tipo in Tipo_carga[EjesH[eje]]:
        if tipo == 1:
            Long_tramo_totales[EjesH[eje]].append(0)
        else:
            Long_tramo_totales[EjesH[eje]].append(Long_tramo[EjesH[eje]][a])
            a += 1
print('Las longitudes totales son', Long_tramo_totales)
input('Pausa...')
#   PLOTEO DE LAS SOLICITACIONES
from Funciones import Dibujar_solicitaciones as Dib
for eje in range(N_Ejes_H):
    Dib(Vector_final_solicitaciones[EjesH[eje]], Tipo_carga[EjesH[eje]], 
                Dist_aplicacion_cargas[EjesH[eje]], Long_tramo_totales[EjesH[eje]], 
                EjesH[eje], Altura_viga[EjesH[eje]])
#_____________________________________________________________________________
def Calculo_corte(Vector_final_solicitaciones, Dist_aplicacion_cargas, Tipo_carga, Long_tramo, viga):
    """
    Created on Sun Aug 16 10:33:26 2020
    
    @author: Tomas Soto
    """
    print('**************************************************')
    print('********** CALCULO DE CORTE EN VIGA "%s" **********' %EjesH[eje])
    print('**************************************************')
    a = 0; b = 0
    n_cargas = len(Vector_final_solicitaciones)
    print('Hay %i solicitaciones' %n_cargas)
    carga = 1
    CA = 0
    MA = 0
    X = []; Y = []; Z = []
    f = {}
    f[1]=1
    tipo_carga = {}
    dist_apli = {}; dist_apli2 = {}
    corte_inicial = {}; corte_final = {}
    corte_inicial[carga]=CA
    mag1 = dict(); mag2 = dict()
    e = {}
    dist1 = {}; dist2 = {}
    while carga <= n_cargas:
        mag1[carga] = 0
        mag2[carga] = 0
        dist1[carga] = 0
        dist2[carga] = 0
        if carga == 1:
            dist_apli[carga] = 0.0
        tipo_carga[carga] = Tipo_carga[a]
        mag1[carga] = Vector_final_solicitaciones[a]
        if tipo_carga[carga] == 1:
            e[carga] = 0
            mag2[carga] = mag1[carga]
            mag1[carga] = 0
            dist_apli[carga] = Dist_aplicacion_cargas[a]
            dist_apli2[carga] = dist_apli[carga]
            xf = 0
            dist2[carga] = 1
            dist1[carga] = 0
            f[carga] = 1
        else:
            e[carga] = 1
            mag2[carga] = mag1[carga]
            dist_apli[carga] = Dist_aplicacion_cargas[a]
            dist2[carga] = Long_tramo[b]
            dist_apli2[carga] = dist_apli[carga]+dist2[carga]
            xf = dist2[carga]
            b += 1
            if mag2[carga] == mag1[carga]:
                dist2[carga] = 1
                dist1[carga] = 0
                mag1[carga] = 0
                f[carga] = 1     
            else:
                e[carga] += 1
                f[carga] = e[carga]
        a += 1    
        fc=CA+((mag2[carga]-mag1[carga])*xf**e[carga])/((dist2[carga] - 
                                                         dist1[carga])*f[carga])
        corte_final[carga] = fc        
        CA = fc
        carga +=1
        if carga <= n_cargas:
            corte_inicial[carga]= CA
    #_________________________________________________________________________       
    #   Creacion de los vectores X y Y para ploteo
    print('\n***** PLOTEO DEL DIAGRAMA *****\n')
    mom_max = 0
    seguir = True
    DistanciaMomento = 0
    for carga in range(1,n_cargas):
            
        if dist_apli[carga]==dist_apli[carga+1] and corte_inicial[carga+1]==corte_final[carga] and carga != 1:
            continue
        else:
            if e[carga] <2:
                X.append(dist_apli[carga])
                X.append(dist_apli2[carga])
                Y.append(corte_inicial[carga])
                Y.append(corte_final[carga])
                Z.append((corte_inicial[carga]*xf))
                Z.append((corte_final[carga]*xf))
                if xf in dist1 or xf in dist2:
                        CA = Y[-1]
                        MA = Z[-1]
            else:
                xf = dist_apli[carga]
                if carga != 1:
                    CA = corte_final[carga-1]
                    MA = corte_final[carga-1]*xf
                else:
                    CA = 0.0
                    MA = 0.0
                while xf<= dist_apli2[carga]:
                    X.append(xf)
                    Y.append(CA+((mag2[carga]-mag1[carga])*xf**e[carga])/
                             ((dist2[carga]-dist1[carga])*f[carga]))
                    Z.append(MA+CA*xf+(mag2[carga]-mag1[carga])*xf**(e[carga]+1)/
                             ((dist2[carga]-dist1[carga])*(f[carga]+1)))
                    if carga > 1:
                        if xf in dist1.values() or xf in dist2.values():
                            CA = corte_final[carga-1]
                    xf += .1
        #   CALCULO DE MOMENTO MAXIMO POR AREAS DEL DIAGRAMA DE CORTE
        if seguir == True:
            if dist_apli[carga] != dist_apli2[carga]:
                if corte_inicial[carga] > 0 and corte_final[carga] > 0:
                    mom_max += (dist_apli2[carga]-dist_apli[carga])*(corte_inicial[carga]+corte_final[carga])/2
                    DistanciaMomento += dist_apli2[carga] - dist_apli[carga]
                else:
                    mom_max += corte_inicial[carga]*abs(corte_inicial[carga]/mag2[carga])/2
                    DistanciaMomento += abs(corte_inicial[carga]/mag2[carga])
                    seguir = False
    mom_max = round(mom_max, 2)
    print('--- El momento máximo es %##.2f Kg.m' %mom_max, 'a una distancia de %.2f metros ---' 
          %DistanciaMomento) 
    carga += 1
    X.append(dist_apli[carga])
    X.append(dist_apli2[carga])
    Y.append(corte_inicial[carga])
    Y.append(corte_final[carga]) 
    Z.append(corte_inicial[carga]*dist1[carga])  
    Z.append(corte_final[carga]*dist2[carga])     
    from matplotlib import pyplot as plt
    #   ********** IDENTIFICACION DE VALORES **********
    plt.title('DIAGRAMA DE CORTE VIGA "%s"' %viga)
    plt.xlabel('Longitud de la viga (m)')
    plt.ylabel('Esfuerzo de Corte (Kg)')
    plt.grid()
    k=0
    for i in X:
        if (i in dist_apli.values() or i in dist_apli2.values()):
            plt.text(X[k],Y[k],format(Y[k],".2f"), fontsize = 8)
        k+=1
    plt.text(DistanciaMomento, Y[1]/6, "M max = %.2f Kg.m" %mom_max)
    xx = [0, DistanciaMomento]
    yx = [Y[-2]/5, Y[-2]/6]
    plt.text(DistanciaMomento/3, yx[1], "X = %.2f m" %DistanciaMomento)
    # ********** GRAFICACION DE LOS CORTES **********
    x0 = [0,X[-1]]
    y0 = [0,0]
    plt.ion()   
    plt.plot(X,Y,'blue') 
    plt.plot(x0,y0,'red')
    plt.plot(xx, [yx[0],yx[0]], 'green')
    plt.plot([0,0], [yx[0]-yx[0]*5/20, yx[0]+yx[0]*5/20], 'green')
    plt.plot([DistanciaMomento,DistanciaMomento], [yx[0]-yx[0]*5/20, yx[0]+yx[0]*5/20], 'green')
    plt.plot()
    plt.show()
    return mom_max, DistanciaMomento
#_____________________________________________________________________________
Momento_maximo = {}
Distancia_Momento = {}
for eje in range(N_Ejes_H):
    print('\n*** Viga %s ***\n' %EjesH[eje])
    Momento_maximo[EjesH[eje]], Distancia_Momento[EjesH[eje]] = Calculo_corte(Vector_final_solicitaciones[EjesH[eje]], Dist_aplicacion_cargas[EjesH[eje]], 
                  Tipo_carga[EjesH[eje]], Long_tramo[EjesH[eje]], EjesH[eje])
#_____________________________________________________________________________       
from sys import exit
import os
ruta = os.getcwd()
import Funciones as Func

def Dibujar_seccion(base, altura, Momento):   
    Momento = round(Momento/1000, 2)    # Convertimos el momento en Ton.m
    print('\n************************************************')
    print('****** Diseño de Viga por Teoría Clásica  ******')
    print('************************************************')
    print('\nLos datos son:\nBase = %i m\nAltura = ' %base, '%i m\nMomento = ' %altura,
          '%.2f Kg.m')
    t = 0.0; td = 0.0; td_min = 5; td_max = 0; r_sup = 0
    op_secc_viga = '2'
    while op_secc_viga != '1' and op_secc_viga != '2':
        print('Seleccione una opción válida!\a')
        op_secc_viga = input('Sección de viga:\n[1] Te\n[2] Rectangular\nSeleccione una opción: ')
    if op_secc_viga == '1':
        print('*** VIGA DE SECCION TIPO TE ***')
        b = float(input('Ancho del nervio la viga b\' (cm): '))
        t = float(input('Espesor del ala "t" (cm): '))
        ba = float(input('Ancho del ala de la viga b: '))    
    else:
        print('*** VIGA DE SECCION TIPO RECTANGULAR ***\n')
        b = base
    modulo_E = {170:177940, 210:219239, 240:234535, 280:253909, 350:283481, 420:310503}
    h = altura
    M = Momento
    #_________________________________________________________________________
    def evaluar_dicc(dicc, texto, unidades):
        for opciones in dicc:
            print('[%i]:' %opciones, '%i' %dicc[opciones], unidades)
        valor = int(input('Escoja una opción: '))
        while not valor in dicc:
            print('Opción incorrecta!')
            valor = int(input('Escoja una opción: '))
        return dicc[valor]
    #_________________________________________________________________________
    fc_op = {1:210, 2:250, 3:280, 4:320, 5:350, 6:400} 
    print('\n*** Maximo esfuerzo a compresion del concreto ***')
    fpc = evaluar_dicc(fc_op, 'f\'c = ', 'Kg/cm2')
    print("Concreto de f\'c= %i Kg/cm2" %fpc)
    print('\n*** Máximo Esfuerzo de fluencia del acero ***')
    fy_op = {1:2800, 2:3500, 3:4200, 4:5200}
    fy = evaluar_dicc(fy_op, 'Fy = ', 'Kg/cm2')
    fs = 0.50*fy
    print('\nLos valores a utilizar son:')
    print('El esfuerzo permisible del acero "fs" es %.2f Kg/cm2' %fs)               
    fc = 0.45*fpc  
    print('El esfuerzo en el concreto "fc" es %.2f Kg/cm2' %fc)               
    n = input('Coeficiente de equivalencia "n": ')
    menor_diferencia_fc = 500
    valores_fc = modulo_E.keys()
    if not n:
        for f in valores_fc:
            if abs(fpc-f) < menor_diferencia_fc:
                menor_diferencia_fc = abs(fpc-f)
                fc = f
            n = int(2100000/modulo_E[fc])
    else:
        n = int(n)     
    print('El coeficiente de equivalencia \'n\' a usar es %i' %n) 
    Factor_fsp_entre_nfc = round(fs/(n*fc),2)
    print("El factor fs/(nfc) = %.2f" %Factor_fsp_entre_nfc)
    r = float(input('Recubrimiento "r" (cm): '))
    while r < 3 or r > 10:
        print('Valores entre 3 - 10 cm')
        r = float(input('Recubrimiento "r" (cm): '))
    if h:
        d = h - r
        if op_secc_viga == '1' and t:
            td = round(t/d,2)
    else:
        x1, x2, y1, y2, x = 0, 0, 0, 0, 0
        K, Ks, Kc, j = Func.Factores_fsnfc(ruta, h, Factor_fsp_entre_nfc, op_secc_viga)
        print('K = %.3f\nKs = ' %K, '%.3f\nKc = ' %Ks, Kc,'\nj = %.3f' %j)
        if op_secc_viga == '1':
            td_min, td_max = Func.Extraer_factores_Te(ruta)
            print('td minimo = %.3f' %td_min, 'y td maximo = %.3f' %td_max)
            Func.Interpolacion(x1, x2, y1, y2, x)
        d = (M*1000*100/(Kc*fc*b))**.5
        print('El valor de [d] es %.2f cm' %d)
        input('Pausa...')
    Factor_fsp_entre_nfc = round(fs/(n*fc), 2)
    if op_secc_viga == '1':
        nf_min = 0.30
        nf_max = 5.00
        paso = 0.10
        td = round(t/d, 2)
        print('\n*** t/d = %.2f ***' %td)
    else:
        nf_min = 0.50
        nf_max = 10.00
        paso = 0.01
    print('\n*** El factor fsp/(n*fc) es %.2f ***\n' %Factor_fsp_entre_nfc)
    K = 0; j=0; Kc = 0
    td_evaluar = []
    minimos = []
    maximos = []
    if op_secc_viga == '1':
        td_min, td_max = Func.Extraer_factores_Te()
        td_evaluar = [td_min, td_max]
        print('t/d a evaluar =', td_evaluar)
        for t_rango in td_evaluar: 
            K_tabla, Ks_tabla, Kc_tabla, j_tabla = Func.Factores_fsnfc(t_rango)
            if t_rango == td_min: 
                K_min, Ks_min, Kc_min, j_min = Func.Factores_fsnfc(t_rango)
                print('K min = %.3f' %K_min, '\nKs min = %.3f' %Ks_min, '\nKc min = %.3f' %Kc_min, '\nj min = %.3f' %j_min)
                minimos = [K_min, Ks_min, Kc_min, j_min]
            else: 
                K_max, Ks_max, Kc_max, j_max = Func.Factores_fsnfc(t_rango)
                print('K max = %.3f' %K_max, '\nKs max = %.3f' %Ks_max, '\nKc max = %.3f' %Kc_max, '\nj max = %.3f' %j_max)
                maximos = [K_max, Ks_max, Kc_max, j_max]
    else:
        K, j, Kc = Func.Extraer_factores(ruta, Factor_fsp_entre_nfc)
        print('*** Factores adimensionales para viga rectangular ***')
        print('K=%s' %K, '\nj=%s' %j, '\nKc=%s' %Kc)
        input('Pausa...')
    if not h:
        d = (M*10**5/(Kc*fc*b))**.5
        h_dado = False
    else:
        d = float(h)-r
        h_dado = True
    if op_secc_viga == '1':
        td = round(t/d, 2) 
        if td<.10 or td>.52:
            print('**** \n\aDimensiones de la viga inaceptables! ****')
            exit()
        if int(td*100)%2 != 0:
            td = round(td + .01, 2)
        else:
            td=round(t/d,2)
    if op_secc_viga == '1':
        td=round(t/d,2)
        if K*d > t:
            Func.Extraer_factores_Te(ruta)
    h = d + r
    if h % 5 != 0:
        if h-int(h) > 0.5:
            h = int(h/10)*10+10
        else:
            h = int(h/10)*10+5
    d = round(h-r, 2)    
    print('h= %.2f cm' %h)  
    print('d nuevo = %.2f cm' %d) 
    cantidad = 1
    Valores_adimensionales_Nombre = ['K', 'Ks', 'Kc', 'j']
    Factores_adimensionales = {}
    if op_secc_viga == '1': 
        for rango in minimos[1:]:
            Factores_adimensionales[Valores_adimensionales_Nombre[cantidad]] = Func.Interpolacion(td_min, td_max, minimos[cantidad], maximos[cantidad], td)
            cantidad +=1
        Ks = Factores_adimensionales['Ks']
        Kc = Factores_adimensionales['Kc']
        j = Factores_adimensionales['j']
        print('\nLos coeficientes adimensionales para t/d=%.2f son:' %td, '\nKs = %.3f' %Ks, '\nKc = %.3f' %Kc, '\nj = %.3f' %j)
    Rc = Kc * fc
    print('Rc= %.2f\n' %Rc)
    Mo = round((Rc * b * d**2)/10**5,2)
    print('El momento óptimo de la sección es "Mo" = %.2f Ton.m\n' %Mo)    
    print('\nCálculo del acero "fs"\n')
    if Mo > M:
        print(Mo, 'Ton.m > %.2f Ton.m' %M, '\n*** Sección simplemente armada ***\n')
        Ks = round(M*10**5*n/(fs*b*d**2),3)
        print('Ks calculado es %.3f' %Ks)
        valor_min, valor_max, j_min, j_max, interpolar = Func.Buscar_limites_viga_rectangular(Ks, ruta)   
        if Ks == valor_min:
            j = j_min
            print('El brazo mecanico especifico a usar es %.3f' %j)
        else:
            x1 = valor_min
            x2 = valor_max
            x = Ks
            y1 = j_min
            y2 = j_max
            j = Func.Interpolacion(x1, x2, y1, y2, x)
        print('j interpolado es %.3f' %j)
        print('Ks = %.4f' %Ks,'\n(Ver tablas Pag 30 y siguientes)')
        As = round(M*10**5/(fs*j*d),2)
        As_min = round(14*b*d/fy,2)
    else:
        print('Momento óptimo Mo = %.2f Ton.m' %Mo, ' < Momento actuante M = %.2f Ton.m' %M, '\n*** Sección doblemente armada ***\n')
        r_sup = float(input('Recubrimiento superior r: '))
        As1 = round(Mo*10**5/(fs*j*d),2)
        print('As1 =  %.2f cm2' %As1)
        As2 = round((M-Mo)*10**5/(d-r_sup)/fs,2)
        print('As2 =  %.2f cm2' %As2)
        fps_As2 = round(2*fs*(K-r_sup/d)/(1-K),2)
        print('El f\'s = %.2f kg/cm2' %fps_As2)
        As = As1 + As2
        if fps_As2 > fs:
            As_min = As2
        else:
            As_min = round(fs/fps_As2*As2,2)
        if As_min > 14*b*d/fy:
            As = As1 + As2
        else: 
            As_min = round(14*b*d/fy,2)
    print('El área de acero As es %.2f cm2' %As, ' y el acero mínimo A\'s es %.2f cm2\n\n' %As_min)  
    print('****************************************')
    print('*** Cálculo de las varillas de acero ***')
    print('****************************************')
    num_barras = 0
    Doble_capa = False
    capa_inf = 0
    capa_sup = 0
    area = []
    print('d = %.2f cm' %d)
    print('\n********** Acero a tracción (Armadura inferior) **********')
    num_barras, diam_acero, Doble_capa, capa_inf, capa_sup, valor_area = Func.calculo_varillas(As, b, d)
    print('El area traccionada es %.2f' %valor_area)
    area.append(valor_area)
    print('\n********** Acero en compresión (Armadura superior) **********')
    capa1=0
    capa2 = 0
    Doble = 0
    num_barras_comp, diam_acero_comp, Doble, capa1, capa2, area_final = Func.calculo_varillas(As_min, b, d)
    area.append(area_final)
    h = d + r
    print('Doble capa de cabillas =', Doble_capa)
    if Doble_capa:
        print('En la capa inferior van %i varillas y en la capa superior irán ' %capa_inf, capa_sup, ' varillas')
    # ******************************************
    # ********** Ploteo de la sección **********
    # ******************************************
    X = []
    Y = []
    if op_secc_viga != '1':  
        X= [0,0,b,b,0]
        Y = [0, h , h, 0, 0]
    else:
        X = [0, ba, ba, ba-(ba-b)/2, ba-(ba-b)/2, ba-(ba-b)/2 - b, ba-(ba-b)/2 - b, 0, 0]
        Y = [h, h, h-t, h-t, 0, 0, h-t, h-t, h]
    from matplotlib import pyplot as plt
    #   ********** IDENTIFICACION DE VALORES **********
    plt.title('SECCION DE VIGA %s' %EjesH[eje])
    inicio = 0
    alinear_texto = 0
    if op_secc_viga != '1': 
        plt.xticks(range(0, int(b)+1, 5))
        plt.yticks(range(0, int(h)+1, 5))
        plt.xlim(-1, 3*b)
        plt.ylim(-1, h+2)
    else:
        relacion = ba/h
        alinear_texto = ba/3+r
        plt.xticks(range(0, int(ba)+1, 20))
        plt.yticks(range(0, int(h)+1, 20))
        plt.xlim(-5, ba+10)
        plt.ylim(-5, relacion*h*3/4+10)
        inicio = (ba-b)/2
    plt.ylabel('Altura de la viga (cm)')
    plt.xlabel('Base de la viga (cm)')  
    x = []; y = []              #   Vector para separacion de aceros a traccion (Armadura inferior)
    xs = []; ys = []
    xc = []; yc = []            #   Vector para separacion de aceros a compresion (Armadura superior)
    t = num_barras
    t_comp = num_barras_comp
    if Doble_capa:
        if capa_sup != 1:
            d2 = (b-2*r)/(capa_sup-1)
        else:
            d2 = (b-2*r)/(capa_sup)
        r2 = 2*r-2
        denom = (capa_inf-1)
        if denom == 0:
            denom = 1
        d = (b-2*r)/denom
    else:
        d = (b-2*r)/(t-1)
    d_comp = (b-2*r)/(t_comp-1)
    for j in range(capa_inf):
        x.append(j*d+r+inicio)
        y.append(r)
    for j in range(capa_sup):
        if capa_sup > 1:
            xs.append(j*d2+r+inicio)
        else:
            xs.append(b/2+inicio)
        ys.append(r2)
    if not r_sup:
        r_sup = r
    for j in range(t_comp):
        xc.append(j*d_comp+r+inicio)
        yc.append(h-r_sup)    
    #k=0
    plt.annotate('Acero tracc. %i barras #' %t + str(diam_acero), xy=(b+r+alinear_texto, r))
    plt.annotate('Area= %.2f cm2 #' %area[-2], xy=(b+r+alinear_texto, r-4))
    plt.annotate('Acero comp. %i barras #'%t_comp + str(diam_acero_comp), xy=(b+r+alinear_texto, h-r))
    plt.annotate('Area= %.2f cm2 #' %area[-1], xy=(b+r+alinear_texto, h-r-4))
    plt.annotate('Base = %i x ' %b + ' Altura = %i' %h, xy=(b+r+alinear_texto, h/2))
    plt.plot(X, Y,'blue') 
    plt.plot(x, y, 'ro')
    plt.plot(xc, yc, 'go')
    if Doble_capa:
        plt.plot(xs, ys, 'ro')  
    plt.show()
#____________________________________________________________________________
print('\n*** PLOTEO DE LA SECCION DE VIGA ***')
for eje in range(N_Ejes_H):
    print('\n*** Viga %s ***\n' %EjesH[eje])
    Dibujar_seccion(Base_viga[EjesH[eje]], Altura_viga[EjesH[eje]], Momento_maximo[EjesH[eje]])