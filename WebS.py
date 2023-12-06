import requests



# Declaracion de matriz
# a = [[],[]]

diccionario = {
                   0: {'puntuacion': {",":1, ".":2, ":":3, ";":4, "¿":5, "?":6, "¡":7, "!":8} },
                   1: {'pronombres': {  'singular': {"yo":1, "tú":2, "usted":3, "ella":4, "él":5},
                                        'plural': {"nosotros":1, "nosotras":2, "ustedes":3, "ellas":4, "ellos":5},
                                     } # Fin de pronombres
                      }, # Fin de 1
                   2: {'sustantivos': {  'singular': {"el":1, "la":2},
                                        'plural': {"los":1, "las":2},
                                      } # Fin de sustantivos
                      } # Fin de 2
} # Fin del diccionario




diccionarioC = {
                   0: {'puntuacion': {",":1, ".":2, ":":3, ";":4, "¿":5, "?":6, "¡":7, "!":8} },
                   1: {'pronombres': {  'singular': {"yo":1, "tú":2, "usted":3, "ella":4, "él":5},
                                        'plural': {"nosotros":1, "nosotras":2, "ustedes":3, "ellas":4, "ellos":5}

                                        } # Fin de pronombres
                      }, # Fin de 1
                   2: {'sustantivos': {  'singular': {"el":1, "la":2},
                                        'plural': {"los":1, "las":2},
                                      } # Fin de sustantivos
                      } # Fin de 2
} # Fin del diccionario



# Direccion de la pagina web
result = requests.get('https://www.eade.es/blog/186-la-sucesion-de-fibonacci-en-el-diseno')
page = result.text          # Contenido de la pagina


inicio = page.index("¿Es posible")          # Indice del inicio del texto que queremos recuperar
fin = page.index("Un ejemplo")              # Indice del fin del texto que queremos recuperar
texto = page[inicio:fin]                    # String recuperado


# Ciclo para quitar los signos de puntuacion
for clave in diccionario[0]['puntuacion'].keys():
    texto = texto.replace(clave,"")



lista = []
listaLimpia = [[],[]]

palabra = ""

# Ciclo para separar las palabras de todo el texto
for x in range(len(texto)):
    if texto[x] != " ":                     # Si cada elemento del texto es diferente de un espacio en blanco
        palabra += texto[x]
    if texto[x] == " ":
        lista.append(palabra.lower())               # Si encuentra un espacio en blanco, quiere decir que es una nueva palabra
        palabra = ""                                               # Despues de guardar la palabra, creamos una nueva



for i in range(len(listaLimpia)):

    for palabra in lista:

        if palabra not in listaLimpia:
            listaLimpia[i].append([palabra])
            listaLimpia[i].append([lista.count(palabra)])


for palabra in listaLimpia:
    print(palabra,end=" \n")

#print(listaLimpia[5][0])

print(type(listaLimpia))

#puntuacion = {",":1, ".":2, ":":3, ";":4, "¿":5, "?":6, "¡":7, "!":8}

#for clave in puntuacion.keys():
#    texto = texto.replace(clave,"")



#print(diccionario[0]['puntuacion'].keys())

texto = texto.lower()

# Ciclo para quitar los signos de puntuacion
for clave in diccionario[0]['puntuacion'].keys():
    texto = texto.replace(clave,"")



# Ciclo para quitar los pronombres
for clave in diccionario[1]['pronombres']['plural'].keys():
    texto = texto.replace(clave,"")


# Ciclo para quitar los sustantivos singulares
for clave in diccionario[2]['sustantivos']['singular'].keys():
    texto = texto.replace(clave,"")

# Ciclo para quitar los sustantivos plurales
for clave in diccionario[2]['sustantivos']['plural'].keys():
    texto = texto.replace(clave,"")




