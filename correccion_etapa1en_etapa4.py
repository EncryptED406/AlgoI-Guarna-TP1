# lista_palabras_ordenadas= ['arroz', 'boludo','careta','pañal']
# letras_participantes=['a','b','c','p']

import random
from datos import obtener_lista_definiciones

#FUNCIONES ETAPA 2
def construction_dictionary_words(list_of_definitions): # NOTE distingue acentos y la letra ñ
    ''' Minimo de 5 letras por palabra de lo contrario no selecciona, se muestra por consola el total de palabras que hay por cada letra, 
    y el total que hay en el diccionario.'''
    dictionary = {} # Para guardar las palabras
    accents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ñ': 'n'}
    ''' El bucle itera y desempaqueta cada elemento de list_of_definitions. 
    En las variables, word ocupara el valor "palabra1" y definition el valor "definicion1" '''
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
    for letter in sorted(dictionary_words.keys()): # Itera sobre las letters del dictionary ordenadas alfabeticamente 
        words = sorted([w['word'] for w in dictionary_words[letter]])    
        print(f'Letter {letter.upper()}: {len(words)} words') # En consola, ejemplo: Letter E: 1 words. letter y la cantidad de words que empiezan con la misma 
    total_words = sum([len(dictionary_words[letter]) for letter in dictionary_words])
    print(f'Total words in the dictionary: {total_words}') # Muestra el total de words en dictionary sumando la cantidad de words por letter

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
    longitud= len(palabras_del_juego[turno])
    return longitud
    
# Sebas
def verificador_de_palabra(turno,palabras_del_juego):
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
    resultado, palabra= tupla
    lista_palabras_ingresadas.append(palabra)
    return

# Dario
def confirmar_palabra(palabra_a_confirmar,lista_palabras_ingresadas,palabras_del_juego:list):
    posicion= lista_palabras_ingresadas.index(palabra_a_confirmar)
    if palabra_a_confirmar in palabras_del_juego and palabra_a_confirmar == palabras_del_juego[posicion]:
        resultado = True
    else:
        resultado = False
    return resultado

# Sebas
def verificador_aciertos_errores(tupla_de_veripalabra, cant_aciertos, cant_errores,lista_palabras_ingresadas,palabras_del_juego):
    validez,palabra=(tupla_de_veripalabra)
    if validez == False:
        cant_errores+=1
    elif validez == True:
        if confirmar_palabra(palabra,lista_palabras_ingresadas,palabras_del_juego):
            cant_aciertos+=1
        else:
            cant_errores+=1
    return cant_aciertos,cant_errores

# Dario
def devolver_palabra_de_letra(lista_palabras_ordenadas, letra):
    respuesta = ''
    contador = 0
    i = 0
    while i < len(lista_palabras_ordenadas) and contador == 0:
        if lista_palabras_ordenadas[i][0] == letra:
            respuesta = lista_palabras_ordenadas[i]
            contador += 1
        else:
            i += 1
    return respuesta

# Dario
def mostrar_rosco_letras(letras_participantes):
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

def turnos(letra, turno,lista_palabras_ordenadas):
    return 'Turno letra '+ letra + ' - Palabra de ' + str(len(lista_palabras_ordenadas[turno])) + ' letras'

def jugar(letras_participantes,palabras_del_juego:list,definiciones:dict,lista_palabras_ingresadas):
    turno=0
    cant_aciertos= 0
    cant_errores=0
    quiere_jugar=True

    while turno <= len(palabras_del_juego):
        print(mostrar_rosco_letras(letras_participantes))
        print(resultado_palabra(lista_palabras_ingresadas,letras_participantes,palabras_del_juego))
        print('Aciertos: '+ str(cant_aciertos))
        print('Errores: '+ str(cant_errores))
        if turno >= len(palabras_del_juego):
            print("funcion que rrecorra todo lo que escribiste y lo que deberia ser")
            print("puntaje final:" )
        else:
            print(turnos(letras_participantes[turno],turno,palabras_del_juego))
            print('definicion de palabra')
            #if turno != len(lista_palabras_ordenadas):
            x=verificador_de_palabra(turno,palabras_del_juego) #Cambiar variable X
            listar_palabras_de_usuario(x,lista_palabras_ingresadas)
            verificador_aciertos_errores(x, cant_aciertos, cant_errores,lista_palabras_ingresadas,palabras_del_juego)

        #listar_palabras_ingresadas()
        #print(x)
        turno += 1
        aciertos, errores = verificador_aciertos_errores(x, cant_aciertos, cant_errores,lista_palabras_ingresadas,palabras_del_juego)
        cant_aciertos = aciertos
        cant_errores = errores
    
        #mostrar_resultado_partida(letras_del_juego,palabras_del_juego)
        #mostrar_puntaje(cant_aciertos,cant_errores):
        
def main():
    
    definiciones={}
    letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                        'x', 'y', 'z']
    lista_palabras_ingresadas = []
    ####################################################
    lista_definiciones= obtener_lista_definiciones()
    definiciones=construction_dictionary_words(lista_definiciones)  #ITEM1 Etapa2
    #mostrar_diccionario(definiciones) 
    ##################################################
    letras_del_juego=seleccionar_letras(letras) #ITEM 2 ETAPA_4
    print(letras_del_juego)
    #################################################
    palabras_del_juego=crear_palabras_del_juego(definiciones,letras_del_juego)#ITEM 3 ETAPA_4
    print(palabras_del_juego)
    #################################################  HASTA ACA, CORRE JOYITA.
    jugar(letras_del_juego,palabras_del_juego,definiciones,lista_palabras_ingresadas)  #ITEM4 ETAPA 4

### Sebas y Mati: su mision aca es eliminar las 2 variables globales restantes.
### O sea: cambiar las funciones de la ETAPA1 para q en lugar de usar las
### listas de las lineas 1 y 2 (globales) usen las listas "letras_del_juego" y 
### "palabras_del_juego" recibidas por parametro. La funcion jugar ya esta recibiendo ambas
### desde el main, asique solo restaria que las distribuyan donde haga falta.
### Nota: una vez modificada cada funcion, no olviden modificar el llamado desde la funcion "jugar"

main()


        