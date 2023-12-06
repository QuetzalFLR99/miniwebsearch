import requests

# ---------------------------------------------- PASO 1: Lectura del archivo log                                                                      # Paso 1: lectura del archivo log
archivo = open("GithubAcces.log")                                       # Ruta del archivo acces.log

lista = []                                                              # Lista para las palabras que componene el archivo acces.log
palabra = ""                                                            # Variable para cada palabra
signos = '()+-";'                                                        # Esta variable es para filtrar correctamente los URLs


# ---------------------------------------------- PASO 2: Filtrar los URLs como "http://"

for fila in archivo:                                                    # Lectura de cada fila del archivo acces.log
    if "http://" in fila:                                               # Si la fila contiene la subcadena "http://"
        for j in range(len(fila)):                                      # Recorrer la fila que contiene "http://"
            if fila[j] != " ":                                          # Si cada elemento del texto es diferente de un espacio en blanco
                palabra += fila[j]
            if fila[j] == " ":                                          # Si encuentra un espacio en blanco, quiere decir que es una nueva palabra
                for x in range(len(signos)):                            # Ciclo para eliminar los signos de puntuacion  de cada palabra
                    palabra = palabra.replace(signos[x], "")            # Eliminar / remplazar los signos

                lista.append(palabra)                                   # Guardar la palabra
                palabra = ""                                            # Despues de guardar la palabra, creamos una nueva


# ---------------------------------------------- PASO 3: Eliminar los URLs repetidos

listaLimpia = []                                                        # Lista sin palabras repetidas

for palabra in lista:                                                   # Este ciclo permite recorrer los elementos de una lista
    if palabra not in listaLimpia:                                      # Condicion para saber si un elemento está repetido
        if "http:" in palabra or "https:" in palabra:                   # Si la lista de palabras contiene la subcadena "http:"
            if "search?" not in palabra:
                listaLimpia.append(palabra)


# ---------------------------------------------- PASO 4: Filtrar los URLs validos y no validos

listaValida = []
listaNoValida = []

for i in listaLimpia:

    try:
        result = requests.get(i)
        if str(result.reason) == "OK":
            listaValida.append(i)
    except:
        listaNoValida.append(i)

# --------------------------------------------- PASO 5: Escribir el archivo "URLs.txt"
url = open("URLValidos.txt","w")                      # El archivo resultados.tex ya debe estar creado, aunque este vacio

for i in listaValida:
    url.write(" " + i + "\n")                   # Guardar el URL en el archivo .tex


# ---------------------------------------------- PASO 5.1: Escribir en el archivo "URLNoValido.txt" los URL que no son validos
url = open("URLNoValido.txt","w")                # El archivo resultados.tex ya debe estar creado, aunque este vacio

for i in listaNoValida:
    url.write(" " + i + "\n")                    # Guardar el URLNoValido en el archivo .tex


print("URLs validos : " , len(listaValida))
print("URLs NO validos : " , len(listaNoValida))



#nltk