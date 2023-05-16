
# En esta variante del juego, se seleccionarán al azar 10 letras de todo el conjunto de
# letras para formar el rosco.

# Ahora que tenemos nuestro diccionario, podremos utilizarlo para obtener una palabra
# candidata de cada letra a adivinar.

# Escribí una función, que reciba como primer parámetro el diccionario y como segundo la
# lista de letras participantes. La función deberá devolver aleatoriamente una palabra que
# empiece con cada letra participante de entre todas las posibles, esto será retornado
# como una lista de palabras ordenadas alfabéticamente.

# Para probar tu función, utiliza un ciclo que la invoque al menos 100 veces, y analiza lo
# que obtienes como palabras a adivinar. Repite el proceso varias veces.
# Además de la función principal de esta etapa, puedes escribir todas las que consideres
# necesarias, teniendo en cuenta los conceptos aprendidos en clase sobre programación
# estructurada y programación modular.
# Lista de letras que deben procesar:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
# 'x', 'y', 'z']

import random

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
    
    return(letras_participantes)

def conseguir_palabra(definiciones:dict, letra_a_procesar:str):
    empiezan_con_letra=[]

    for palabra in definiciones.keys():
            if letra_a_procesar==palabra[0]:
                empiezan_con_letra.append(palabra)
    numero_de_letra=random.randint(0,len(empiezan_con_letra)-1)
    palabra=empiezan_con_letra[numero_de_letra]
    return(palabra)

def crear_rosco (definiciones:dict, letras_participantes:list):
    palabras_rosco=[]

    for letra in letras_participantes:
        palabra=conseguir_palabra(definiciones,letra)
        palabras_rosco.append(palabra)

    rosco_ordenado=sorted(palabras_rosco)
    return (rosco_ordenado)
        
def main():
    prueba={"a":{
            "avion":"cosa que vuela",
            "azul":"color del mar"},
            "boludo":"estudiante de fiuba",
            "barco":"transporte que se usa para navegar",
            "casa":"hogar dulce hogar",
            "cebolla":"vegetal que te hace llorar",
            "diestro":"escribe derecho",
            "eduardo":"yo",
            "excelente":"dicese de una accion realizada de forma sobresaliente",
            "floricienta":"serie vieja",
            "gato":"mascota mas bonita y hermosa",
            "hueco":"agujero pero dicho mas fino",
            "inodoro":"asiento del baño",
            "aguila":"pajaro que vuela y cazador",
            "jirafa":"animal cuello largo",
            "kilo":"unidad de masa",
            "luz":"lo que tira el foquito en el techo",
            "mama":"mi ---- me quiere mucho",
            "naranja":"fruta o color",
            "ñandu":"lo que no es avestruz pero se parece",
            "opera":"galletitas o lugar donde canta la gente",
            "papa":"progenitor que no es mama",
            "queso":"alimento lacteo que se usa para la pizza",
            "raton":"animalito o persona tacaña",
            "sal":"lo que le pones a la comida para que sea salada",
            "teatro":"lugar donde hay actores",
            "uva":"fruta que se obtiene de los viñedos",
            "vaca":"nos da la leche",
            "waterpolo":"deporte acuatico",
            "xenofobo":"persona que odia extranjeros",
            "yogurt":"alimento lacteo que se obtiene por fermentacion",
            "zebra":"importante jugueteria de Buenos Aires"}

    letras_a_procesar=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                        'x', 'y', 'z']
    
    for j in range(10):

        letras_del_juego=seleccionar_letras(letras_a_procesar)
        rosco=crear_rosco(prueba,letras_del_juego)
        print(rosco)
    
main()

    
