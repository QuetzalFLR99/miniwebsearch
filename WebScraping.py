import requests

# Declaracion de matriz
# a = [[],[]]

# Direccion de la pagina web
result = requests.get("https://www.eade.es/blog/186-la-sucesion-de-fibonacci-en-el-diseno")
page = result.text          # Contenido de la pagina

print(len(page))

inicio = page.index("¿Es posible")          # Indice del inicio del texto que queremos recuperar
fin = page.index("Un ejemplo")              # Indice del fin del texto que queremos recuperar
texto = page[inicio:fin]                    # String recuperado



signos = ".,;:¿?!¡"                         # Signos de puntuacion
palabra = ""                                # Variable para guardar cada palabra
lista = []                                  # Lista para TODAS las palabras


# Ciclo para eliminar los signos de puntuacion  del texto
for x in range(len(signos)):
    texto = texto.replace(signos[x],"")


# Ciclo para identificar cada palabra
for x in range(len(texto)):
    if texto[x] != " ":                     # Si cada elemento del texto es diferente de un espacio en blanco
        palabra += texto[x]
    if texto[x] == " ":
        lista.append(palabra)               # Si encuentra un espacio en blanco, quiere decir que es una nueva palabra
        palabra = ""                        # Despues de guardar la palabra, creamos una nueva




listaLimpia = []                 # Lista sin palabras repetidas

for palabra in lista:                       # Este ciclo permite recorrer los elementos de una lista
    if palabra not in listaLimpia:          # Condicion para saber si un elemento está repetido
        listaLimpia.append(palabra)



# Ciclo para mostrar las palabras
for palabra in listaLimpia:
    print(palabra, end="\n")

print("EL numero de palabras del texto es de: ", len(lista) ,"palabras")
print("EL numero de palabras sin repetir es de: ", len(listaLimpia) ,"palabras")