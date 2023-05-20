import random
import doctest
from datos import obtener_lista_definiciones

#FUNCIONES ETAPA 2
def construction_dictionary_words(list_of_definitions): # NOTE distingue acentos y la letra ñ
    ''' Minimo de 5 letras por palabra de lo contrario no selecciona, se muestra por consola el total de palabras que hay por cada letra, 
    y el total que hay en el diccionario.
    Autor: Matias'''
    dictionary = {} # Para guardar las palabras
    accents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ñ': 'n'}
    ''' El bucle itera y desempaqueta cada elemento de list_of_definitions. 
    En las variables, word ocupara el valor "palabra1" y definition el valor "definicion1"
    Autor: Matias '''
    for word, definition in list_of_definitions: 
        if len(word) >= 5: # NOTE Un minimo de 5 letras, de lo contrario no se agrega a dictionary. Ejemplo: yoga, via
            letter = word[0].lower() # Agarramos el primer caracter de la palabra para convertirlo en mayuscula 
            letter_standard = accents.get(letter, letter)
            if letter_standard not in dictionary: # Comprueba si esa letter no está incluida en el diccionario
                dictionary[letter_standard] = {} # Lista vacia para adjuntar palabras con esa letra
            #dictionary[letter_standard].append((word,definition)) # Incluye word y definition a dictionary segun la letra
            dictionary[letter_standard][word] = definition
    return dictionary # Devuelve el dictionary de palabras generado

def mostrar_diccionario(dictionary_words:dict):
    ''' 
    funcion: mostrar_diccionario
    dictionary_words: diccionario anidado con tres niveles de profundidad
    letter: Toma el valor de la clave principal (a, b, c hasta la z)
    level_2: Entra al segundo diccionario anidado. Tomara el valor que le sigue a Letter, y tomaria clave, valor (palabra, definicion)
    Autor: Matias Gonzalez
    '''
    for letter, level_2 in dictionary_words.items():
        print("Letra:", letter.upper())
        for word_key, definition_value in level_2.items():
            print("Palabra:", word_key)
            print("Definicion:", definition_value)
            print("---")

dictionary_words = {"a":{
            "avion":"cosa que vuela"},
            
            "b":{
            "barco":"transporte que se usa para navegar"},
            
            "c":{
            "cebolla":"vegetal que te hace llorar"},
            
            "d":{
            "diestro":"escribe derecho"},
            
            "e":{
            "estrella":"cuerpo celeste que irradia energia"},
            
            "f":{
            "floricienta":"serie vieja"},
            
            "g":{
            "gato":"mascota mas bonita y hermosa"},
            
            "h":{
            "hueco":"agujero pero dicho mas fino"},
            
            "i":{
            "inodoro":"asiento del baño"},
            
            "j":{
            "jirafa":"animal cuello largo"},
            
            "k":{
            "kilo":"unidad de masa"},
            
            "l":{
            "luz":"lo que tira el foquito en el techo"},
            
            "m":{
            "madera":"proviene del arbol"},
            
            "n":{
            "naranja":"fruta o color"},
            
            "o":{
            "opera":"galletitas o lugar donde canta la gente"},
            
            "p":{
            "papa":"progenitor que no es mama"},
            
            "q":{
            "queso":"alimento lacteo que se usa para la pizza"},
            
            "r":{
            "raton":"animalito o persona tacaña"},
            
            "s":{
            "sal":"lo que le pones a la comida para que sea salada"},
            
            "t":{
            "teatro":"lugar donde hay actores"},
            
            "u":{
            "uva":"fruta que se obtiene de los viñedos"},
            
            "v":{
            "vaca":"nos da la leche"},
            
            "w":{
            "waterpolo":"deporte acuatico"},
            
            "x":{
            "xenofobo":"persona que odia extranjeros"},
            
            "y":{
            "yogurt":"alimento lacteo que se obtiene por fermentacion"},
            
            "z":{
            "zodiacal":"un tipo de horoscopo"}}

# Llamada a la función para mostrar el diccionario 
# mostrar_diccionario(dictionary_words)

#FUNCIONES ETAPA 3

def seleccionar_letras(letras_a_procesar:list):
    letras_participantes=[]
    ya_salieron=[]
    cant_letras=10

    for i in range(cant_letras):
        numero_de_letra=random.randint(0,len(letras_a_procesar)-1)
        letra=letras_a_procesar[numero_de_letra]
        while letra in ya_salieron:
            numero_de_letra=random.randint(0,len(letras_a_procesar)-1)
            letra=letras_a_procesar[numero_de_letra]
        letras_participantes.append(letra)
        ya_salieron.append(letra)
    
    letras_participantes_ordenadas=sorted(letras_participantes)
    return(letras_participantes_ordenadas)

def conseguir_palabra(definiciones:dict, letra_a_procesar:str):

    numero=random.randint(0,len(definiciones[letra_a_procesar].keys())-1)
    palabra=(list(definiciones[letra_a_procesar].keys()))[numero]
    return(palabra)

def crear_palabras_del_juego (definiciones:dict, letras_participantes:list):
    palabras_rosco=[]

    for letra in letras_participantes:
        palabra=conseguir_palabra(definiciones,letra)
        palabras_rosco.append(palabra)

    rosco_ordenado=sorted(palabras_rosco)
    return (rosco_ordenado)

#FUNCIONES ETAPA 1
# Sebas
def pregunta_palabra():
    palabra=input("Ingrese palabra: ")
    return palabra

def obtener_longitud_palabra(turno,palabras_del_juego):
    '''
    >>> obtener_longitud_palabra(1,['arco','barco','casco','diarco'])
    5
    >>> obtener_longitud_palabra(3,['arco','barco','casco','diarco'])
    6
    >>> obtener_longitud_palabra(0,['arco','barco','casco','diarco'])
    4
    '''
    longitud= len(palabras_del_juego[turno])
    return longitud
    
# Sebas
def verificador_de_palabra(turno,palabras_del_juego):
    '''
    >>> verificador_de_palabra(5, ['añadir', 'fatal', 'hacinamiento', 'jarabe', 'kevlar', 'mecha', 'sustancia', 'urgir', 'voltear', 'xerografía'])
        False, 'macha'
    >>> verificador_de_palabra(9, ['bilirrubina', 'factible', 'hamaca', 'jurar', 'nebulizar', 'oponer', 'quedar', 'windsurf', 'yarará', 'zambullir'])
        True, 'zambullir'
    >>> verificador_de_palabra(1, ['bilirrubina', 'factible', 'hamaca', 'jurar', 'nebulizar', 'oponer', 'quedar', 'windsurf', 'yarará', 'zambullir'])
        True, 'factible'
    '''
    palabra_a_verificar= pregunta_palabra()
    longitud_de_palabra= obtener_longitud_palabra(turno,palabras_del_juego)
    """la longitud esta medida mediante una funcion que busque la primera palabra
       de la lista y le haga el len"""
    contador_errores=0
    indice=0
    resultado=False
    
    validar_palabra=palabra_a_verificar.lower() 
    if len(validar_palabra) == longitud_de_palabra:
        while indice < len(validar_palabra) and contador_errores==0:
            if not validar_palabra[indice].isalpha():
                contador_errores +=1
            indice +=1
        if contador_errores==0:
            resultado=True
    return resultado,validar_palabra

# Sebas
def listar_palabras_de_usuario(tupla,lista_palabras_ingresadas):
    
    PALABRA_A_VALIDAR=1
    lista_palabras_ingresadas.append(tupla[PALABRA_A_VALIDAR])
    return

# Dario
def confirmar_palabra(palabra_a_confirmar,lista_palabras_ingresadas,palabras_del_juego:list):
    '''
    >>> confirmar_palabra('arco',['arco'],['arco','barco','casco','diarco'])
    True

    >>> confirmar_palabra('barco',['arco', 'biblioteca', 'barco'],['arco','barco','casco','diarco'])
    False

    >>> confirmar_palabra('casa',['arco', 'barco', 'casa'],['arco','barco','casco','diarco'])
    False

    '''
    posicion= lista_palabras_ingresadas.index(palabra_a_confirmar)
    if palabra_a_confirmar in palabras_del_juego and palabra_a_confirmar == palabras_del_juego[posicion]:
        resultado = True
    else:
        resultado = False
    return resultado

# Sebas
def verificador_aciertos_errores(tupla_de_veripalabra, cant_aciertos, cant_errores,lista_palabras_ingresadas,palabras_del_juego):
    '''
    >>> verificador_aciertos_errores((True, 'arroz'), 0, 0, ['arroz'],['arroz','barco', 'camion'])
    (1, 0)

    >>> verificador_aciertos_errores((False, 'arco'), 1, 0, ['arroz', 'arco'],['arroz','barco', 'camion'])
    (1, 1)

    >>> verificador_aciertos_errores((True, 'arroz'), 5, 4, ['arroz'],['arroz','barco', 'camion'])
    (6, 4)

    '''
    validez,palabra=(tupla_de_veripalabra)
    if validez:
        cant_errores+=1
    else:
        if confirmar_palabra(palabra,lista_palabras_ingresadas,palabras_del_juego):
            cant_aciertos+=1
        else:
            cant_errores+=1
    return cant_aciertos,cant_errores

# Dario
def mostrar_rosco_letras(letras_participantes):
    '''
    >>> mostrar_rosco_letras(['A','B','C'])
    '[A][B][C]'
    >>> mostrar_rosco_letras(['D','E','F'])
    '[D][E][F]'

    '''
    letras=''
    
    for letra in letras_participantes:
        letras += '['+letra+']'
    return letras

# Dario
def resultado_palabra(lista_palabras_ingresadas,letras_participantes:list,palabras_del_juego:list):
    resultado=''
    if lista_palabras_ingresadas == []:
        for letra in letras_participantes:
            resultado += '[ ]'
    else:
        for ingresada in lista_palabras_ingresadas:
            if confirmar_palabra(ingresada,lista_palabras_ingresadas,palabras_del_juego) :
                resultado += '[a]'
            elif not(confirmar_palabra(ingresada,lista_palabras_ingresadas,palabras_del_juego)):
                resultado += '[e]'
        espacios_vacios = len(letras_participantes) - len(lista_palabras_ingresadas)
        for vacio in range(0, espacios_vacios):
            resultado += '[ ]'
    return resultado

# Etapa 5
def calcular_puntaje_ronda(cant_aciertos:int,cant_errores:int):
    """Calcula y devuelve el puntaje de una ronda determinada dados los aciertos y errores cometidos.
        Autor:Eduardo
    """
    PUNTOS_ACIERTO=10
    PUNTOS_ERROR=-3
    puntaje=0
    puntaje+= PUNTOS_ACIERTO*cant_aciertos+PUNTOS_ERROR*cant_errores
    return(puntaje)

def mostrar_puntajes(puntaje_anterior,cant_aciertos,cant_errores):
    """Muestra el puntaje de ronda y el total acumulado dados los aciertos y erores cometidos en la ronda
    actual.
        Autor:Eduardo
    """
    puntos_ronda=calcular_puntaje_ronda(cant_aciertos,cant_errores)
    print("Puntaje Final de esta ronda:",puntos_ronda)
    print("El puntaje total acumulado es:")
    print(puntaje_anterior+puntos_ronda)

#####
def turnos(letra, turno,lista_palabras_ordenadas):
    return 'Turno letra '+ letra + ' - Palabra de ' + str(len(lista_palabras_ordenadas[turno])) + ' letras'

def mostrar_resultado_partida(lista_palabras_ingresadas,letras_participantes, lista_palabras_ordenadas):
    indice = 0
    for palabra in lista_palabras_ingresadas:
        if palabra == lista_palabras_ordenadas[indice]:
            print('Turno letra '+ str(letras_participantes[indice]) + ' - Palabra de ' + str(len(lista_palabras_ordenadas[indice])) + ' letras - ' + palabra + ' - acierto')
        else:
            print('Turno letra '+ str(letras_participantes[indice]) + ' - Palabra de ' + str(len(lista_palabras_ordenadas[indice])) + ' letras - ' + palabra + ' - error - Palabra Correcta: ' + str(lista_palabras_ordenadas[indice]))
        indice += 1

def jugar(letras_participantes,palabras_del_juego:list,definiciones:dict,lista_palabras_ingresadas, puntaje):
    turno=0
    cant_aciertos= 0
    cant_errores=0
    lista_palabras_ingresadas = []
    while turno <= len(palabras_del_juego):
        print(mostrar_rosco_letras(letras_participantes))
        print(resultado_palabra(lista_palabras_ingresadas,letras_participantes,palabras_del_juego))
        print('Aciertos: '+ str(cant_aciertos))
        print('Errores: '+ str(cant_errores))
        if turno != len(palabras_del_juego):
            print(turnos(letras_participantes[turno],turno,palabras_del_juego))
            print('Definición: '+ definiciones[letras_participantes[turno]][palabras_del_juego[turno]])
            #if turno != len(lista_palabras_ordenadas):
            x=verificador_de_palabra(turno,palabras_del_juego) #Cambiar variable X
            listar_palabras_de_usuario(x,lista_palabras_ingresadas)
            aciertos, errores=verificador_aciertos_errores(x, cant_aciertos, cant_errores,lista_palabras_ingresadas,palabras_del_juego)

        #listar_palabras_ingresadas()
        #print(x)
        turno += 1
        #aciertos, errores = verificador_aciertos_errores(x, cant_aciertos, cant_errores,lista_palabras_ingresadas,palabras_del_juego)
        cant_aciertos = aciertos
        cant_errores = errores
    mostrar_resultado_partida(lista_palabras_ingresadas,letras_participantes, palabras_del_juego)
    mostrar_puntajes(puntaje,cant_aciertos,cant_errores)
    puntaje+=calcular_puntaje_ronda(cant_aciertos,cant_errores)
    palabras_del_juego = []
    letras_participantes = []
    turno=0
    cant_aciertos= 0
    cant_errores=0
    
    return puntaje
    
    #mostrar_resultado_partida(letras_del_juego,palabras_del_juego)
    #mostrar_puntaje(cant_aciertos,cant_errores):
        
def main():
    
    definiciones={}
    letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                        'x', 'y', 'z']
    lista_palabras_ingresadas = []
    sigue_jugando=True
    puntaje = 0
    ####################################################
    lista_definiciones= obtener_lista_definiciones()
    definiciones=construction_dictionary_words(lista_definiciones)  #ITEM1 Etapa2
    mostrar_diccionario(dictionary_words) 
    ##################################################
    while sigue_jugando:
        letras_del_juego=seleccionar_letras(letras) #ITEM 2 ETAPA_4
    #################################################
        palabras_del_juego=crear_palabras_del_juego(definiciones,letras_del_juego)#ITEM 3 ETAPA_4
        print(palabras_del_juego)
    #################################################  HASTA ACA, CORRE JOYITA.
        puntaje = jugar(letras_del_juego,palabras_del_juego,definiciones,lista_palabras_ingresadas, puntaje)  #ITEM4 ETAPA 4   
        continua=input("Desea jugar otra partida? Presione la tecla ""S"", cualquier otra para salir:")
        if continua.lower()=="s":
            sigue_jugando=True
        else:
            sigue_jugando=False
    print(doctest.testmod())
main()


        
