import random
import doctest
from datos import obtener_lista_definiciones

#FUNCIONES ETAPA 2
def construction_dictionary_words(list_of_definitions): 
    ''' Minimo de 5 letras por palabra de lo contrario no selecciona, se muestra por consola el total de palabras que hay por cada letra, 
    y el total que hay en el diccionario.
    Autor: Matias Gonzalez'''
    dictionary = {} 
    accents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ñ': 'n'}
    ''' El bucle itera y desempaqueta cada elemento de list_of_definitions. 
    En las variables, word ocupara el valor "palabra1" y definition el valor "definicion1"
    Autor: Matias '''
    for word, definition in list_of_definitions: 
        if len(word) >= 5:
            letter = word[0].lower() 
            letter_standard = accents.get(letter, letter)
            if letter_standard not in dictionary: 
                dictionary[letter_standard] = {} 
            dictionary[letter_standard][word] = definition
    return dictionary 

def mostrar_diccionario(dictionary_words:dict):
    ''' 
    funcion: mostrar_diccionario
    dictionary_words: diccionario anidado con tres niveles de profundidad
    letter: Toma el valor de la clave principal (a, b, c hasta la z)
    Autor: Matias Gonzalez
    '''
    total_words = 0
    for letra in sorted (dictionary_words.keys()):
        print("La letra", letra, "tiene: ", len(dictionary_words[letra].keys()))
        total_words += len(dictionary_words[letra].keys())
        
    print("Palabras del diccionario: ", total_words)

#FUNCIONES ETAPA 3

def seleccionar_letras(letras_a_procesar:list):
    """
    Obj: Recibe una lista y selecciona X elementos al azar únicos de la misma. La long de la lista debe
    ser mayor que los X elementos deseados.
    Autores: Luz y Eduardo 
    """
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
    """
    Obj: Recibe el diccionario y una letra, retorna una palabra al azar del 
    diccionario que empieza con tal letra.
    Autores:Eduardo y Luz
    """
    numero=random.randint(0,len(definiciones[letra_a_procesar].keys())-1)
    palabra=(list(definiciones[letra_a_procesar].keys()))[numero]
    return(palabra)

def crear_palabras_del_juego (definiciones:dict, letras_participantes:list):
    """
    Obj: Recibe el diccionario y una lista de letras participantes, selecciona una palabra al azar
    por cada una de tales letras y las retorna ordenadas alfabeticamente.  
    Autores:Eduardo y Luz
    """
    palabras_rosco=[]

    for letra in letras_participantes:
        palabra=conseguir_palabra(definiciones,letra)
        palabras_rosco.append(palabra)

    rosco_ordenado=sorted(palabras_rosco)
    return (rosco_ordenado)

#FUNCIONES ETAPA 1

def pregunta_palabra():
    '''
    La función pregunta_palabra le pide al usuario que ingrese una palabra
    y devuelve la palabra para luego utilizarla.
    AUTOR: Sebastián 
    '''
    palabra=input("Ingrese palabra: ")
    return palabra

def obtener_longitud_palabra(turno,palabras_del_juego):
    '''
    La funcion obtener_longitud_palabra recibe el turno y palabras_del_juego,nos devuelve la longitud
    de la palabra en la lista de palabras_del_juego en la posicion que se esta jugando(turno)
    AUTOR: Dario.

    >>> obtener_longitud_palabra(1,['arco','barco','casco','diarco'])
    5

    >>> obtener_longitud_palabra(3,['arco','barco','casco','diarco'])
    6

    >>> obtener_longitud_palabra(0,['arco','barco','casco','diarco'])
    4

    '''
    longitud= len(palabras_del_juego[turno])
    return longitud
    

def verificador_de_palabra(turno,palabras_del_juego):
    '''
    La funcion verificador_de_palabra recibe el turno y las palabras_del_juego, va a llamar a las funciones
    pregunta_palabra y obtener_longitud_palabra para luego verificar que la palabra ingresada cumpla con las
    condiciones necesarias para usarse ,en caso contrario volvera a preguntar hasta devolver la palabra pedida.
    AUTOR: Sebastián.
    
    >>> verificador_de_palabra(5, ['añadir', 'fatal', 'hacinamiento', 'jarabe', 'kevlar', 'mecha', 'sustancia', 'urgir', 'voltear', 'xerografía'])
    'macha'
    >>> verificador_de_palabra(9, ['bilirrubina', 'factible', 'hamaca', 'jurar', 'nebulizar', 'oponer', 'quedar', 'windsurf', 'yarará', 'zambullir'])
    'zambullir'
    >>> verificador_de_palabra(1, ['bilirrubina', 'factible', 'hamaca', 'jurar', 'nebulizar', 'oponer', 'quedar', 'windsurf', 'yarará', 'zambullir'])
    'factible'
    
    '''
    palabra= pregunta_palabra().lower()
    longitud_de_palabra= obtener_longitud_palabra(turno,palabras_del_juego)
    palabra_valida=False
    while not palabra_valida:
        if len(palabra) == longitud_de_palabra and palabra.isalpha():
            palabra_valida=True
        else:
            print("Revise la palabra que escribio,la misma no debe contener espacios, caracteres especiales, numeros, y debe tener",longitud_de_palabra,"caracteres")
            palabra=pregunta_palabra().lower()
    return palabra

def listar_palabras_de_usuario(palabra_ingresada,lista_palabras_ingresadas):
    """
    La funcion listar_palabras_de_usuario recibe una palabra_ingresada que ha sido escrita por el usuario y la
    guarda en lista_palabras_ingresadas.
    AUTOR:Sebastián
    """
    lista_palabras_ingresadas.append(palabra_ingresada)
    return

def confirmar_palabra(palabra_a_confirmar,lista_palabras_ingresadas,palabras_del_juego:list):
    '''
    Esta funcion devuelve True o False dependiendo de si la palabra ingresada por el usuario 
    este en la lista de palabras del juego y a su vez que su posicion sea la correcta.
    AUTOR: Dario.

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

def verificador_aciertos_errores(palabra_ingresada, cant_aciertos, cant_errores,lista_palabras_ingresadas,palabras_del_juego):
    '''    
    La funcion verificador_aciertos_errores recibe palabra_ingresada,cant_aciertos, cant_errores,
    lista_palabras_ingresadas,palabras_del_juego va a llamar a la funcion confirmar_palabra,
    contara los aciertos y los errores y los devolvera.
    Autor:Sebastián
    
    >>> verificador_aciertos_errores('arroz', 0, 0, ['arroz'],['arroz','barco', 'camion'])
    (1, 0)

    >>> verificador_aciertos_errores('arco', 1, 0, ['arroz', 'arco'],['arroz','barco', 'camion'])
    (1, 1)

    >>> verificador_aciertos_errores('arroz', 5, 4, ['arroz'],['arroz','barco', 'camion'])
    (6, 4)

    '''
    if confirmar_palabra(palabra_ingresada,lista_palabras_ingresadas,palabras_del_juego):
        cant_aciertos+=1
    else:
        cant_errores+=1
    return cant_aciertos,cant_errores

def mostrar_rosco_letras(letras_participantes):
    '''
    Muestra por pantalla el rosco de las letras participantes
    AUTOR: Dario
    >>> mostrar_rosco_letras(['A','B','C'])
    '[A][B][C]'
    >>> mostrar_rosco_letras(['D','E','F'])
    '[D][E][F]'
    '''
    letras=''
    
    for letra in letras_participantes:
        letras += '['+letra.upper()+']'
    return letras

def resultado_palabra(lista_palabras_ingresadas,letras_participantes:list,palabras_del_juego:list):
    '''
    Muestra por pantalla [ ] vacios si todavia no se ingreso una palabra, una [e] si la palabra 
    ingresada es un error o una [a] si es un acierto.
    AUTOR: Dario.
    '''
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

# Funciones Etapa 5

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
    """Muestra el puntaje de ronda y el total acumulado dados los aciertos y errores cometidos en la ronda
    actual.
        Autor:Eduardo
    """
    puntos_ronda=calcular_puntaje_ronda(cant_aciertos,cant_errores)
    print("Puntaje Final de esta ronda:",puntos_ronda)
    print("El puntaje total acumulado es:")
    print(puntaje_anterior+puntos_ronda)

def turnos(letra, turno,lista_palabras_ordenadas):
    """
    La funcion turnos recibe letra, turno,lista_palabras_ordenadas para luego imprimir
    el turno de la letra y cuantas letras tiene la palabra que estamos jugando.
    Autor:Sebastián
    """
    return 'Turno letra '+ letra + ' - Palabra de ' + str(len(lista_palabras_ordenadas[turno])) + ' letras'

def mostrar_resultado_partida(lista_palabras_ingresadas,letras_participantes, lista_palabras_ordenadas):
    """
    La funcion imprime por pantalla el resultado turno por turno de la ronda que acaba de concluir. 
    Autores: Luz y Dario
    """
    indice = 0
    for palabra in lista_palabras_ingresadas:
        if palabra == lista_palabras_ordenadas[indice]:
            print('Turno letra '+ str(letras_participantes[indice]) + ' - Palabra de ' + str(len(lista_palabras_ordenadas[indice])) + ' letras - ' + palabra + ' - acierto')
        else:
            print('Turno letra '+ str(letras_participantes[indice]) + ' - Palabra de ' + str(len(lista_palabras_ordenadas[indice])) + ' letras - ' + palabra + ' - error - Palabra Correcta: ' + str(lista_palabras_ordenadas[indice]))
        indice += 1

def jugar(letras_participantes,palabras_del_juego:list,definiciones:dict,lista_palabras_ingresadas, puntaje):
    """
    La funcion jugar es el encargado de mostrar por pantalla el tablero,tambien se encarga de manejar el juego
    interactuando con el usuario y mostrando como avanza la partida
    Autores:Sebastián y Dario
    """
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
            palabra_ingresada=verificador_de_palabra(turno,palabras_del_juego) 
            listar_palabras_de_usuario(palabra_ingresada,lista_palabras_ingresadas)
            aciertos, errores=verificador_aciertos_errores(palabra_ingresada, cant_aciertos, cant_errores,lista_palabras_ingresadas,palabras_del_juego)
        turno += 1
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
        
def main():
    
    #DEFINICIONES
    definiciones={}
    letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                        'x', 'y', 'z']
    lista_palabras_ingresadas = []
    sigue_jugando=True
    puntaje = 0

    #PREARMADO DEL JUEGO
    lista_definiciones= obtener_lista_definiciones() 
    definiciones=construction_dictionary_words(lista_definiciones)
    mostrar_diccionario(definiciones) 
    #JUEGO 
    while sigue_jugando:
        letras_del_juego=seleccionar_letras(letras) 
        palabras_del_juego=crear_palabras_del_juego(definiciones,letras_del_juego)
        print(palabras_del_juego)
    #POST Ronda(PUNTUACION+nueva partida)
        puntaje = jugar(letras_del_juego,palabras_del_juego,definiciones,lista_palabras_ingresadas, puntaje)   
        continua=input("Desea jugar otra partida? Presione la tecla ""S"", cualquier otra para salir:")
        acepta_continuar="s"
        if continua.lower()==acepta_continuar:
            sigue_jugando=True
        else:
            sigue_jugando=False
    print(doctest.testmod())

main()
