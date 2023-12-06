# ---------------------------------------------- PASO 1: Lectura del archivo log                                                                      # Paso 1: lectura del archivo log
archivo = open("GithubAcces.log")                                       # Ruta del archivo acces.log

lista = []                                                              # Lista para las palabras que componene el archivo acces.log
palabra = ""                                                            # Variable para cada palabra


# ---------------------------------------------- PASO 2: Filtrar los URLs como "http://"

for fila in archivo:                                                    # Lectura de cada fila del archivo acces.log

    if "http://" in fila:                                               # Si la fila contiene la subcadena "http://"
        for j in range(len(fila)):                                      # Recorrer la fila que contiene "http://"
            if fila[j] != " ":                                          # Si cada elemento del texto es diferente de un espacio en blanco
                palabra += fila[j]
            if fila[j] == " ":                                          # Si encuentra un espacio en blanco, quiere decir que es una nueva palabra


                palabra = palabra.replace('"', "")
                palabra = palabra.replace('(', "")
                palabra = palabra.replace(')', "")
                palabra = palabra.replace("+", "")

                lista.append(palabra)                                   # Guardar la palabra
                palabra = ""                                            # Despues de guardar la palabra, creamos una nueva




# ---------------------------------------------- PASO 3: Eliminar los URLs repetidos

listaLimpia = []                 # Lista sin palabras repetidas

for palabra in lista:                       # Este ciclo permite recorrer los elementos de una lista
    if palabra not in listaLimpia:          # Condicion para saber si un elemento está repetido
        listaLimpia.append(palabra)




# ---------------------------------------------- PASO 4: Escribir el archivo "URLs.txt"
url = open("URLs.txt","w")            # El archivo resultados.tex ya debe estar creado, aunque este vacio


for i in listaLimpia:
    if "http:" in i:                                                    # Si la lista de palabras contiene la subcadena "http:"
        print(i,end="\n")
        url.write(" " + i + "\n")                                       # Guardar el URL en el archivo .tex

