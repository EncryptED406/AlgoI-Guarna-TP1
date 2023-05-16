lista_palabras_ingresadas= []
lista_palabras_ordenadas= ['arroz', 'boludo','careta','pañal']
letras_participantes=['a','b','c','p']

# Sebas
def pregunta_palabra():
    palabra=input("Ingrese palabra: ")
    return palabra

def obtener_longitud_palabra(turno):
    longitud= len(lista_palabras_ordenadas[turno])
    return longitud
    

# Sebas
def verificador_de_palabra(turno):
    palabra_a_verificar= pregunta_palabra()
    longitud_de_palabra= obtener_longitud_palabra(turno)
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
def listar_palabras_ingresadas(tupla):
    resultado, palabra= tupla
    lista_palabras_ingresadas.append(palabra)
    return

# Dario
def confirmar_palabra(palabra_confirmar):
    posicion= lista_palabras_ingresadas.index(palabra_confirmar)
    if palabra_confirmar in lista_palabras_ordenadas and palabra_confirmar == lista_palabras_ordenadas[posicion]:
        resultado = True
    else:
        resultado = False
    return resultado

# Sebas
def verificador_aciertos_errores(tupla_de_veripalabra, cant_aciertos, cant_errores):
    validez,palabra=(tupla_de_veripalabra)
    if validez == False:
        cant_errores+=1
    elif validez == True:
        if confirmar_palabra(palabra):
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
def resultado_palabra():
    resultado=''
    if lista_palabras_ingresadas == []:
        for letra in letras_participantes:
            resultado += '[ ]'
    else:
        for ingresada in lista_palabras_ingresadas:
            if confirmar_palabra(ingresada) :
                resultado += '[a]'
            elif not(confirmar_palabra(ingresada)):
                resultado += '[e]'
        espacios_vacios = len(letras_participantes) - len(lista_palabras_ingresadas)
        for vacio in range(0, espacios_vacios):
            resultado += '[ ]'
    return resultado



def turnos(letra, turno):
    return 'Turno letra '+ letra + ' - Palabra de ' + str(len(lista_palabras_ordenadas[turno])) + ' letras'

def jugar():
    turno=0
    cant_aciertos= 0
    cant_errores=0
    while turno <= len(lista_palabras_ordenadas):
        print(mostrar_rosco_letras(letras_participantes))
        print(resultado_palabra())
        print('Aciertos: '+ str(cant_aciertos))
        print('Errores: '+ str(cant_errores))
        if turno >= len(lista_palabras_ordenadas):
            print("funcion que rrecorra todo lo que escribiste y lo que deberia ser")
            print("puntaje final:" )
        else:
            print(turnos(letras_participantes[turno],turno))
            print('definicion de palabra')
            #if turno != len(lista_palabras_ordenadas):
            x=verificador_de_palabra(turno)
            listar_palabras_ingresadas(x)
            verificador_aciertos_errores(x, cant_aciertos, cant_errores)

        #listar_palabras_ingresadas()
        #print(x)
        turno += 1
        aciertos, errores = verificador_aciertos_errores(x, cant_aciertos, cant_errores)
        cant_aciertos = aciertos
        cant_errores = errores
    
jugar()
        
