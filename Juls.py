## Algoritmo para la extracción y escritura de enlases URL desde un archivo .log
## Autor: Julian Pérez Dolores
## Fecha: 27/Septiembre/2022
## Archivo access.log:
## Archivo urls.txt:
## ---------------------------------------------------------------------------------------------------------------- ##

## "re" es la libreria para expresiones regulares.
#   Estas expresiones son patrones de coincidencia de texto descritos con una
#   sintaxis formal. Los patrones se interpretan como un conjunto de instrucciones,
#   que luego se ejecutan con una cadena como entrada para producir un subconjunto
#   de coincidencia o una versión modificada del original
import re


## ---------------------------------------------------------------------------------------------------------------- ##

## "with" es una de las mejores formas de asegurarnos de que el fichero se cierra
#   correctamente, pase lo que pase sin tener que utilizar el metodo close()
#   Por lo tanto leemos los valores del primer archivo "access.log", para luego
#   escribir los valores obtenidos en le segundo archivo "urls.txt"

def isValidURL(url):
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    urlValida = re.compile(regex)

    if (url == None):
        return False

    if (re.search(urlValida, url)):
        return True
    else:
        return False


with open("GithubAcces.log", "r") as archivo, open("urls.txt", "w") as urls:
    lista = []  # Lista para almacenar valores del archivo de lectura
    patron = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:&[0-9a-fA-F][0-9a-fA-F]))+'  # Patron para buscar URLs
    caracteres = '(),'  # Caracteres especiales dontro de cada URLs

    ## --------------------------------- Obtenemos los URLs el archivo "access.log" ---------------------------------- ##

    for fila in archivo:  # Recorremos todas las fila dentro del archivo de lectura
        for j in range(len(caracteres)):  # Recorremos la cantidad total de caracteres de la cadena
            fila = fila.replace(caracteres[j], '')  # Remplazamos los caracteres por un espacio en blanco
            enlace = re.findall(patron, fila)  # Buscamos los URLs que cumpla con el "patron" en cada fila
        if len(enlace) != 0:  # Condicion para eliminar valores que sean igual a 0
            lista.append(enlace)  # Agreamos los elementos "URLs" dentro de la lista

    ## --------------------------------- Eliminamos los URLs que esten repetidos ------------------------------------- ##

    listaLimpia = []  # Lista limpia para almacenar valores no repetidos

    for valor in lista:  # Recorremos todas los valores dentro de la "lista" creada
        if valor not in listaLimpia:  # Conocer si "valor" no se encuentra en la "listaLimpia"
            listaLimpia.append(valor)  # Agregamos "valor" a "listaLimpia" hasta que se repita

    ## -------------------------------- Escribimos los URLs en el archivo "urls.txt" --------------------------------- ##

    for url in listaLimpia:
        if (isValidURL(str(url)) == True):
            print("".join(url), end='\n')  # Con " ".join() convertimos toda la lista a cadena e imprimimos
            urls.write("".join(map(str, url)) + '\n')  # Con .write() se escriben las URLs en el archivo de escritura
            # map() aplica "str" a cada elemento de "listaLimpia"
            # Despues del mapping en "listaLimpia", se escribe en "urls.txt"


