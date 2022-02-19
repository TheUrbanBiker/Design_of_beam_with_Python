#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 23:08:20 2021

@author: Tomas Soto
"""
#________________________________________________________________________________________________________________ 

#   CALCULO DE LAS BARRAS DE ACERO
def calculo_varillas(As, b, d):               # ANCHO MINIMO DE LA BASE a_m_b EN PULGADAS
    print('Los datos son:\nAs = %.2f cm2\nb=' %As,'%i cm\nd='%b, '%i cm' %d)
    a_m_b = {}
    barra = {}

    #   Definición de diámetros nominales de barras de aceromodulo_E
    barra[0] = 4
    barra[1] = 5
    barra[2] = 6
    barra[3] = 7
    barra[4] = 8
    barra[5] = 9
    barra[6] = 10
    barra[7] = 11
    barra[8] = 14
    barra[9] = 18

    #   Ancho mínimo de base de la viga en pulg (Tabla A.5 Pag 651)
    #   Se consideran que los estribos son de 3/8"

    # Para 2 varillas en una capa de refuerzo
    a_m_b[0,0] = 6.8
    a_m_b[1,0] = 6.9
    a_m_b[2,0] = 7.0
    a_m_b[3,0] = 7.2
    a_m_b[4,0] = 7.3
    a_m_b[5,0] = 7.6
    a_m_b[6,0] = 7.8
    a_m_b[7,0] = 8.1
    a_m_b[8,0] = 8.9
    a_m_b[9,0] = 10.6

    # Para 3 varillas en una capa de refuerzo
    a_m_b[0,1] = 8.3
    a_m_b[1,1] = 8.5
    a_m_b[2,1] = 8.8
    a_m_b[3,1] = 9.0
    a_m_b[4,1] = 9.3
    a_m_b[5,1] = 9.8
    a_m_b[6,1] = 10.4
    a_m_b[7,1] = 10.9
    a_m_b[8,1] = 12.3
    a_m_b[9,1] = 15.1

    # Para 4 varillas en una capa de refuerzo
    a_m_b[0,2] = 9.8
    a_m_b[1,2] = 10.2
    a_m_b[2,2] = 10.5
    a_m_b[3,2] = 10.9
    a_m_b[4,2] = 11.3
    a_m_b[5,2] = 12.1
    a_m_b[6,2] = 12.9
    a_m_b[7,2] = 13.8
    a_m_b[8,2] = 15.7
    a_m_b[9,2] = 19.6

    # Para 5 varillas en una capa de refuerzo
    a_m_b[0,3] = 11.3
    a_m_b[1,3] = 11.8
    a_m_b[2,3] = 12.3
    a_m_b[3,3] = 12.8
    a_m_b[4,3] = 13.3
    a_m_b[5,3] = 14.3
    a_m_b[6,3] = 15.5
    a_m_b[7,3] = 16.6
    a_m_b[8,3] = 19.0
    a_m_b[9,3] = 24.1

    # Para 6 varillas en una capa de refuerzo
    a_m_b[0,4] = 12.8
    a_m_b[1,4] = 13.4
    a_m_b[2,4] = 14.0
    a_m_b[3,4] = 14.7
    a_m_b[4,4] = 15.3
    a_m_b[5,4] = 16.6
    a_m_b[6,4] = 18.0
    a_m_b[7,4] = 19.4
    a_m_b[8,4] = 22.4
    a_m_b[9,4] = 28.6
    
    # Para 7 varillas en una capa de refuerzo
    a_m_b[0,5] = 14.3
    a_m_b[1,5] = 15.0
    a_m_b[2,5] = 15.8
    a_m_b[3,5] = 16.5
    a_m_b[4,5] = 17.3
    a_m_b[5,5] = 18.8
    a_m_b[6,5] = 20.5
    a_m_b[7,5] = 22.2
    a_m_b[8,5] = 25.8
    a_m_b[9,5] = 33.1

    # Para 8 varillas en una capa de refuerzo
    a_m_b[0,6] = 15.8
    a_m_b[1,6] = 16.7
    a_m_b[2,6] = 17.5
    a_m_b[3,6] = 18.4
    a_m_b[4,6] = 19.3
    a_m_b[5,6] = 21.1
    a_m_b[6,6] = 23.1
    a_m_b[7,6] = 25.0
    a_m_b[8,6] = 29.2
    a_m_b[9,6] = 37.7

    # Ancho adicional por tipo de barra
    a_m_b[0,7] = 1.5
    a_m_b[1,7] = 1.625
    a_m_b[2,7] = 1.75
    a_m_b[3,7] = 1.875
    a_m_b[4,7] = 2.00
    a_m_b[5,7] = 2.26
    a_m_b[6,7] = 2.54
    a_m_b[7,7] = 2.82
    a_m_b[8,7] = 3.39
    a_m_b[9,7] = 4.51

    opcion = 0
    f = 0
    capa_sup = []
    capa_inf = []
    cantidad_final = {}
    diametro_final = {}
    area_final = {}
    tolerancia = float(input('Tolerancia del área en cm2: '))      
    
    for i in range(7):                          #   Conteo del número de cabillas

        for k in range(10):                     #   Conteo para el tamaño de varilla
            As_barra = (i+2)*3.14159*(barra[k]/16*2.54)**2
            #print('El área de acero es %.2f cm2' %As_barra)
                    
            if  As_barra >= As and (As_barra - As) <= tolerancia:
                opcion +=1
                    
                if (a_m_b[k,i]*2.54) <= b:
                    Doble_capa = False
                    print("\nOpción[%i]" %opcion,"\n%i barras #" %(i+2), barra[k], " Area= %.2f cm2" %As_barra) 
                    capa_inf.append(i)
                    capa_sup.append(2)
                else:
                    
                    while (a_m_b[k,f]*2.54) < b:
                        print('El ancho anterior al doble capa es de %.2f cm' %(a_m_b[k,f]*2.54))
                        f+=1
                        
                    capa_inf.append(f+2)
                    capa_sup.append(i-f)
                    print('Capa inferior: ', capa_inf[-1], '\nCapa superior: ', capa_sup[-1])
                    print('\nOpción [%i]' %opcion,'\n%i barras #' %(i+2), barra[k], 'dividida en dos capas')
                    print('\nEn la capa inferior %i' %capa_inf[opcion-1], 'y en la segunda capa %i' %capa_sup[opcion-1]) 
                    Doble_capa = True
                    print('Area total = %.2f cm2' %As_barra)
                        
                cantidad_final.setdefault(opcion, i+2)
                diametro_final.setdefault(opcion, barra[k])
                area_final.setdefault(opcion, As_barra)
                     
    opcion_final = int(input('Escoja una opcion: '))
    
    while opcion_final <1 or opcion_final> opcion:
         opcion_final = int(input('Escoja una opcion: '))
         
    print('Arriba van %i barras y abajo van ' %capa_sup[opcion_final-1], capa_inf[opcion_final-1], ' barras')
    print('El area final es %.2f' %area_final[opcion_final])
    
    return cantidad_final[opcion_final], diametro_final[opcion_final], Doble_capa, capa_inf[opcion_final-1], capa_sup[opcion_final-1], area_final[opcion_final]
#________________________________________________________________________________________________________________ 

#   BUSCA LOS LIMITES PARA VIGAS DE SECCION RECTANGULAR
def Buscar_limites_viga_rectangular(Valor_comparacion, ruta):
     archivo = open(ruta+'/Coeficientes adimensionales.txt', 'r')
     valores = []
     numero_linea = 0
     no_buscar = False
     valor_max = Valor_comparacion
     
     for linea in archivo:
         linea = linea.strip()
         valores = linea.split()
         valor_min = 0.001
         j_min = 0
         interpolar = True
         
         if numero_linea != 0:
             
             if float(valores[4]) == Valor_comparacion:
                 j_min = float(valores[2])
                 j_max = float(valores[2])
                 valor_min = Valor_comparacion
                 interpolar = False
                 print('El Ks buscado es igual a Ks calculado (%.3f)' %Valor_comparacion)
                 input()
                 break
                 return valor_min, valor_max, j_min, j_max, interpolar
                 
             elif float(valores[4]) < Valor_comparacion:
                 
                 if no_buscar == False:
                     valor_min = float(valores[4])
                     j_min = float(valores[2])
                     no_buscar = True
                     print('El Ks inmediato inferior es %.3f' %valor_min)
                     break
                     return valor_min, valor_max, j_min, j_max, interpolar
                 
             elif Valor_comparacion < float(valores[4]):
                 valor_max = float(valores[4])
                 
                 if no_buscar != True:
                     j_max = float(valores[2])
                 
         else:
             numero_linea = 1
             
     return valor_min, valor_max, j_min, j_max, interpolar
#________________________________________________________________________________________________________________ 

#   CALCULO DE ECUACION CUADRATICA
def Ec_Cua(a,b,c):

    valor = (b**2-4*a*c)
    x = (-b+valor**.5)/(2*a)
    
    if type(x) == complex:
        x = (-b-valor**.5)/(2*a)
    else:
        x = (-b+valor**.5)/(2*a)
        return x
#________________________________________________________________________________________________________________ 

def Interpolacion(x1, x2, y1, y2, x):
    m = abs(y1-y2)/abs(x1-x2)
    if y1 > y2:
        y = y1 - abs(x1-x)*m
    else:
        y = y2 - abs(x1-x)*m
        
    return y
#________________________________________________________________________________________________________________

def Evaluar_entrada(entrada, Presentacion_texto, v_min, v_max):
    
    while entrada < v_min or entrada > v_max:
        print('\aValor incorrecto!\n')
        entrada = int(input(Presentacion_texto))
        
    return entrada
#________________________________________________________________________________________________________________

def Calculo_Momento_Actuante():
    carga = {}
    Salir = ""
    mayor_carga = 0.0
    Letra_carga = 'D','F', 'T', 'L', 'H', 'A', 'S', 'R', 'W', 'E', '0'
    SiNo_peso = input("La carga muerta incluye el peso propio de la viga? [1] Si  [otro] No: ")  
    print('\n*** Introducir las cargas en Ton ***\n')
    Salir = False
    inicio = 0
    mayor_carga = 0.0
    
    L = float(input('Longitud de la viga en metros L= '))

    while Salir != True:
        
        if inicio == 0:       
            op_carga = input("[D] Carga muerta\n[L] Carga viva\n[E] Carga sismica\n[F] Carga fluidos\n[T] Temperatura\n[H] Presion lateral del suelo\n[A] Carga viva de techo\n[S] Carga de Nieve\n[W] Carga eolica\n[R] Carga pluvial\nEscoger opcion: ")
            op_carga = op_carga.upper()
            inicio = 1
        else:
            op_carga = input("[D] Carga muerta\n[L] Carga viva\n[E] Carga sismica\n[F] Carga fluidos\n[T] Temperatura\n[H] Presion lateral del suelo\n[A] Carga viva de techo\n[S] Carga de Nieve\n[W] Carga eolica\n[R] Carga pluvial\n\n[0] SALIR\nEscoger opcion: ")
            op_carga = op_carga.upper()
    
        while (op_carga in Letra_carga) == False:
            op_carga = input("[D] Carga muerta\n[L] Carga viva\n[E] Carga sismica\n[F] Carga fluidos\n[T] Temperatura\n[H] Presion lateral del suelo\n[A] Carga viva de techo\n[S] Carga de Nieve\n[W] Carga eolica\n[R] Carga pluvial\n\n[0] SALIR\nEscoger opcion: ")
            op_carga = op_carga.upper()
    
        if op_carga != '0':
            carga[op_carga] = float(input("Valor de la carga %s: " %op_carga))
        else:
            Salir = True
    
    print("Las cargas son:", carga)
    
    U = []
    h_tent = round(L/10*12,2)

    if h_tent - int(h_tent) > 0:
        h_tent = int(h_tent)+1
    
    b_tent = round(h_tent/2,2)

    if b_tent - int(b_tent) > 0:
        b_tent = int(b_tent)+1
    
    if SiNo_peso != '1':
        peso = round(b_tent * h_tent / 144*150.0,2)
    
        if peso - int(peso)> 0:
            peso = (int(peso)+1)/1000.0
            
    else:
        peso = 0
    
    for i in Letra_carga:
    
        if i in carga.keys():
            continue
        else:
            carga[i] = 0  
    
    #   COMBINACIONES DE CARGAS
    U.append(1.4*((carga['D']+peso)+carga['F']))
    U.append(1.2*((carga['D']+peso)+carga['F']+carga['T'])+1.6*(carga['L']+carga['H'])+0.5*(carga['A']))
    U.append(1.2*((carga['D']+peso)+carga['F']+carga['T'])+1.6*(carga['L']+carga['H'])+0.5*(carga['S']))
    U.append(1.2*(carga['D']+peso+carga['F']+carga['T'])+1.6*(carga['L']+carga['H'])+0.5*(carga['R']))
    U.append(1.2*(carga['D']+peso)+1.6*carga['A']+carga['L'])
    U.append(1.2*(carga['D']+peso)+1.6*carga['S']+carga['L'])
    U.append(1.2*(carga['D']+peso)+1.6*carga['R']+carga['L'])
    U.append(1.2*(carga['D']+peso)+1.6*carga['A']+0.8*carga['W'])
    U.append(1.2*(carga['D']+peso)+1.6*carga['S']+0.8*carga['W'])
    U.append(1.2*(carga['D']+peso)+1.6*carga['R']+0.8*carga['W'])
    U.append(1.2*(carga['D']+peso)+1.6*carga['W']+1.0*carga['L']+0.5*carga['A'])
    U.append(1.2*(carga['D']+peso)+1.6*carga['W']+1.0*carga['L']+0.5*carga['S'])
    U.append(1.2*(carga['D']+peso)+1.6*carga['W']+1.0*carga['L']+0.5*carga['R'])
    U.append(1.2*(carga['D']+peso)+1.0*carga['E']+1.0*carga['L']+0.2*carga['S'])
    U.append(0.9*(carga['D']+peso)+1.6*carga['W']+1.6*carga['H'])
    U.append(0.9*(carga['D']+peso)+1.6*carga['E']+1.6*carga['H'])
    
    for i in U:
        
        if i > 0:
            
            if i > mayor_carga:
                mayor_carga = i
                
    print("\n*** La mayor carga ultima es %.2f Ton/m ***" %(mayor_carga))
    M = round(mayor_carga * L**2 / 8,2)
    return M
#________________________________________________________________________________________________________________

def Factores_fsnfc(ruta, h_dado, Factor_fsp_entre_nfc, Tipo_viga):
    print('\nEl tipo de viga es [%s]' %Tipo_viga)
    td_dado = 0
    if not h_dado:
        nombre_archivo = '/Coeficientes adimensionales.txt'
    else:
        nombre_archivo = '/Coeficientes adimensionales seccion Te.txt'
    
    print('El archivo a utilizar se llama %s y es el actual!!!!' %nombre_archivo)
    archivo_p = open(ruta+nombre_archivo, 'r')
    valores = []; g = []
    K_tabla = 0.0; Ks_tabla = 0.0; Kc_tabla = 0.0; j_tabla = 0.0
    
    for linea in archivo_p:
        valores=linea.strip()
        g=valores.split()
        
        if Tipo_viga == '1':     #  VIGA TIPO TE                      
            td_tabla = round(float(g[0][4:]), 2)
            print('td_tabla = %.3f' %td_tabla)
            input('Hasta aqui todo bien...(linea 370')
                
            if Tipo_viga == '1':
                if td_tabla == td_dado:
                    input('Aqui se pide td_dado!! (linea 371)')
                    
        else:                   #   VIGA TIPO RECTANGULAR

            fsnfc_tabla = float(g[0])
            print(fsnfc_tabla, 'convertido en valor numerico')
            print(Factor_fsp_entre_nfc, ' =  %.2f' %fsnfc_tabla)  
            
            if round(Factor_fsp_entre_nfc, 2) == round(fsnfc_tabla, 2):
                print('\a\n*** Calculo de los limites de fs/nfc ***')
                print('g=', g)
                K_tabla = float(g[1])
                Ks_tabla = float(g[2])
                Kc_tabla = float(g[3])
                j_tabla = float(g[4])
                print('K=%.3f' %K_tabla)
                print('Ks=%.3f' %Ks_tabla)
                print('Kc=%.3f' %Kc_tabla)
                print('j=%.3f' %j_tabla)
                input('Hasta aqui todo bien...(linea 408)')
                return K_tabla, Ks_tabla, Kc_tabla, j_tabla
                break
            #else:
                """
                if abs(Factor_fsp_entre_nfc - fsnfc_tabla) < 0.1:
                    #print('\a\n*** Calculo de los limites de fs/nfc ***')
                    K_tabla = float(g[1])
                    Ks_tabla = float(g[2])
                    Kc_tabla = float(g[3])
                    j_tabla = float(g[4])
                    return K_tabla, Ks_tabla, Kc_tabla, j_tabla"""
                
    archivo_p.close()
    #return K_tabla, Ks_tabla, Kc_tabla, j_tabla
#________________________________________________________________________________________________________________    

def Extraer_factores_Te(ruta):
    archivo_p = open(ruta +'/Coeficientes adimensionales seccion Te.txt', 'r')
    Factor_fsp_entre_nfc = float(input('Factor fsp/nfc: '))
    valores = []
    g = []
    Rango = False
    td_min = 0.52
    td_max = 0.10
    td_tabla = 0.0
    td = 0
    for linea in archivo_p:
        valores=linea.strip()
        g = valores.split()      
        
        if len(g) == 1:
            td_tabla = float(g[0][-4:])
            input('Aqui se pide td_dado!! (linea 406)')
            
            if td_tabla < td:
                td_min = td_tabla    
            else:
                
                if td_tabla == (td+.02) or td_tabla == (td+0.01):
                    td_max = td_tabla
            
            if td == float(g[0][-4:]):
                Rango = True
                print('\nLinea = %s' %g, 'y t/d = %s' %str(round(td, 2)))
            else:
                Rango = False
                        
        if Rango and len(g)>1:
            
            if abs(float(g[0]) - Factor_fsp_entre_nfc) < 0.05:
                print(g[0],'es aproximadamente %.2f' %Factor_fsp_entre_nfc)
                print('Interpolar')
                Rango = False
                
    archivo_p.close()    
    return td_min, td_max
#________________________________________________________________________________________________________________

def Extraer_factores(ruta, Factor_fsp_entre_nfc):
    
    archivo_p = open(ruta +'/Coeficientes adimensionales.txt', 'r')
    valores = []; g = []
    nlinea = 0; K = 0; j=0; Kc = 0

    for linea in archivo_p:
    
        if nlinea != 0:
            valores=linea.strip()
            g = valores.split()
        
            if float(g[0]) == Factor_fsp_entre_nfc: 
                K, j, Kc = float(g[1]), float(g[2]), float(g[3])
                
        nlinea+=1
        
    archivo_p.close()
    return K, j, Kc
#________________________________________________________________________________________________________________

def Interpolacion(x1, x2, y1, y2, x):
    m = abs(y1-y2)/abs(x1-x2)
    if y1 > y2:
        y = y1 - abs(x1-x)*m
    else:
        y = y2 - abs(x1-x)*m
        
    return y
#________________________________________________________________________________________________________________

def Evaluar_entrada_2_datos(Presentacion_texto, Datos):
    print(Presentacion_texto)
    
    for i in range(len(Datos)):
        print('[%i] =' %(i+1), Datos[i+1])
        
    entrada = int(input(Presentacion_texto))
        
    while entrada < 1 or entrada > len(Datos):
        print('Opción incorrecta.')
        entrada = int(input(Presentacion_texto))
        
    return Datos[entrada]
#_______________________________________________________________________
def Dibujar_solicitaciones(Magnitud, Tipo, Distancia, Longitud_tramo, Viga, Altura_viga):   
#Created on Thu Jan 13 08:09:45 2022
#***     DIBUJO DE SOLICITACIONES    ***
#author: Tomas Soto
    Dist_Apoyo = []
    MayorCargaDist = 0
    Cargas_dist = [] 
    Dist_Apli_Cargas_Dist = []
    Long_Cargas_Dist = []
    print('\n********************************************')
    print('*** DIBUJO DE SOLICITACIONES EN VIGA "%s" ***' %Viga)
    print('********************************************\n')
    #n_cargas = int(input('Número total de solicitaciones (cargas y reacciones): '))
    n_cargas = len(Magnitud)
    datos_carga = {}
    Dato_texto = ['Magnitud', 'Tipo', 'Distancia aplicación', 'Longitud']
    
    long_carga = {}
    dist_aplicacion = {}
    #h_viga = float(input('Altura de la viga: '))
    h_viga = float(Altura_viga/100)
    for carga in range(n_cargas):
        print('\n*** Carga %i ***' %(carga+1))
        datos_carga[carga] = []
        for i in range(4):
        #    datos_carga[carga][i].append()
            if i == 3:
                '''if datos_carga[carga][1] == 1:
                    datos_carga[carga].append(0)
                    print('La carga es puntual. No tiene longitud.')
                else:
                    datos_carga[carga].append(float(input('%s: ' %Dato_texto[i])))'''
                datos_carga[carga].append(Longitud_tramo[carga])
            '''else:
                datos_carga[carga].append(float(input('%s: ' %Dato_texto[i])))'''   
            if i == 1:
                if Tipo[carga] == 2:
                    #Cargas_dist.append(datos_carga[carga][0])
                    Cargas_dist.append(Magnitud[carga])
            elif i == 2:
                #Dist_Apli_Cargas_Dist.append(datos_carga[carga][2])
                Dist_Apli_Cargas_Dist.append(Distancia[carga])
                if Magnitud[carga] > 0:
                    #Dist_Apoyo.append(datos_carga[carga][2])
                    Dist_Apoyo.append(Distancia[carga])
            elif i == 3:    
                #Long_Cargas_Dist.append(datos_carga[carga][3])
                Long_Cargas_Dist.append(Longitud_tramo[carga])
    Y_cargas_dist = []
    Dist_apoyo = []
    #Longitud = datos_carga[carga][2]+datos_carga[carga][3]
    Longitud = Distancia[carga]+Longitud_tramo[carga]
    a = 0
    for carga in Cargas_dist:
        if abs(carga) > MayorCargaDist:
            MayorCargaDist = abs(carga)
    for carga_dist in Cargas_dist:
        Y_cargas_dist.append(round(abs(carga_dist)*3/MayorCargaDist,1))
    Y_punt = max(Y_cargas_dist)  
    print('Los datos son:', datos_carga)
    print('\n*** PLOTEO DEL CUERPO LIBRE ***\n')
    from matplotlib import pyplot as plt
    plt.title('CUERPO LIBRE DE LA VIGA "%s"' %Viga)
    plt.xlim(-1, Longitud+2)
    plt.ylim(-3, 5)
    VigaX = [0, 0 , Longitud, Longitud, 0]; VigaY = [0, h_viga, h_viga, 0, 0]
    plt.plot(VigaX, VigaY, 'red')
    plt.plot([0, Longitud], [-.6, -.6], 'green')
    plt.plot([0, Longitud], [-1.2, -1.2], 'green')
    for carga in datos_carga:
        if a < len(Cargas_dist):
            Y_dist = Y_cargas_dist[a]
        if Tipo[carga] == 1:  #   CARGA PUNTUAL
            if Magnitud[carga] > 0:
                y_flecha1 = -1.7; y_flecha2 = y_flecha1 - .3; inicio_vert = -1.7; final_vert = -2.5
                ApoyoX = [Distancia[carga], Distancia[carga]+.15, Distancia[carga]-.15, Distancia[carga]]
                ApoyoY = [0, -.3, -.3, 0]
                plt.plot(ApoyoX, ApoyoY, 'red')
            else:
                y_flecha1 = Y_punt; y_flecha2 = Y_punt + .3; inicio_vert = Y_punt; final_vert = 4
            plt.plot([Distancia[carga], Distancia[carga]-.15, Distancia[carga]
                      +.15, Distancia[carga]], [y_flecha1, y_flecha2, y_flecha2, y_flecha1], 'black' )
            plt.plot([Distancia[carga], Distancia[carga]], [inicio_vert, final_vert], 'black')
            plt.text(Distancia[carga], final_vert, Magnitud[carga])
        else:   #   CARGA DISTRIBUIDA
            plt.plot([Distancia[carga], Distancia[carga], Distancia[carga]
                      +Longitud_tramo[carga], Distancia[carga]+Longitud_tramo[carga], 
                      Distancia[carga]], [h_viga+.05, Y_cargas_dist[a], Y_cargas_dist[a], h_viga+.05, h_viga+.05], 'blue')
            plt.text(Distancia[carga], Y_cargas_dist[a]+.1, Magnitud[carga])
            a +=1
        plt.plot([Distancia[carga], Distancia[carga]], [-.8, -.4], 'green')
        if carga == n_cargas-1:
            plt.plot([Distancia[carga]+Longitud_tramo[carga], Distancia[carga]+Longitud_tramo[carga]], [-.8, -.4], 'green')
        plt.plot([0, 0], [-1.4, -1], 'green')
        plt.plot([Longitud, Longitud], [-1.4, -1], 'green')
        if Tipo[carga] == 2:
            plt.text(round((Distancia[carga]+Longitud_tramo[carga]/2-.1), 2), -.55, Longitud_tramo[carga])
        for flecha in range(int(Longitud+1)):
            plt.plot([flecha-.15, flecha, flecha + .15], [h_viga+.3, h_viga+.05, h_viga+.3], 'blue')
    plt.text(round(Longitud/2-.1,2), -1.1, Longitud) 
    plt.show()