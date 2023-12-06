import requests
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")

pattern1 = [{"LIKE_URL": True}]                     # Patron de busqueda para el URL
matcher = Matcher(nlp.vocab)                        # Objeto matcher
matcher.add("PATTERN1", [pattern1])                 # Agrega el patron al matcher


# ---------------------------------------------- PASO 1: Lectura del archivo log                                                                      # Paso 1: lectura del archivo log
archivo = open("GithubAcces.log")                                       # Ruta del archivo acces.log

cont = 0
lista = []
for fila in archivo:

    if cont == 100:
        break
    cont += 1
    doc = nlp(str(fila))
    for match_id, start, end in matcher(doc):
        if "http:" in str(doc[start:end]):
            print(doc.vocab.strings[match_id], "|| ", doc[start:end].text, end="\n\n")          # el texto del span encontrado
            lista.append(str(doc[start:end].text))

listaLimpia = []                                                        # Lista sin palabras repetidas
for palabra in lista:                                                   # Este ciclo permite recorrer los elementos de una lista
    if palabra not in listaLimpia:                                      # Condicion para saber si un elemento está repetido
        listaLimpia.append(palabra)




listaValida = []
listaNoValida = []

for i in listaLimpia:

    try:
        print("XXX",i)
        result = requests.get(i)
        print(result.reason)
        print(len(result.text))
        if str(result.reason) == "OK":
            listaValida.append(i)
        else:
            print("Chango")
    except:
        listaNoValida.append(i)
        print("URL no valido: ",i)

# --------------------------------------------- PASO 5: Escribir el archivo "URLs.txt"
url = open("URLs.txt","w")                      # El archivo resultados.tex ya debe estar creado, aunque este vacio

for i in listaValida:
    url.write(" " + i + "\n")                   # Guardar el URL en el archivo .tex


# ---------------------------------------------- PASO 5.1: Escribir en el archivo "URLNoValido.txt" los URL que no son validos
url = open("URLNoValido.txt","w")                # El archivo resultados.tex ya debe estar creado, aunque este vacio

for i in listaNoValida:
    url.write(" " + i + "\n")                    # Guardar el URLNoValido en el archivo .tex


print("URLs validos : " , len(listaValida))
print("URLs NO validos : " , len(listaNoValida))

