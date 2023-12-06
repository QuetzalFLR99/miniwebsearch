import requests
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")

pattern1 = [{"LIKE_URL": True}]  # Patron de busqueda para el URL
matcher = Matcher(nlp.vocab)  # Objeto matcher
matcher.add("PATTERN1", [pattern1])  # Agrega el patron al matcher

# ---------------------------------------------- PASO 1: Lectura del archivo log                                                                      # Paso 1: lectura del archivo log
archivo = open("GithubAcces.log")  # Ruta del archivo acces.log
lista = []


for fila in archivo:

    doc = nlp(str(fila))
    for match_id, start, end in matcher(doc):
        if "http:" in str(doc[start:end]) and ".log" not in str(doc[start:end].text):
            if str(doc[start:end].text) not in lista:  # Condicion para saber si un elemento está repetido
                lista.append(str(doc[start:end]))
                print(str(doc[start:end].text), end="\n")  # el texto del span encontrado



listaValida = []
listaNoValida = []

for i in lista:

    try:

        result = requests.get(i, timeout=3)
        #print("URL: ", result.reason, i)

        if str(result.reason) == "OK":
            print("URL: ", result.reason, i)
            listaValida.append(i)
        if  str(result.reason) == "Not Found":
            listaNoValida.append(i)

    except:
        listaNoValida.append(i)
        print("\nURL no valido:", i, "\n")



# --------------------------------------------- PASO 5: Escribir el archivo "URLs.txt"
url = open("URLValidos.txt", "w")  # El archivo resultados.tex ya debe estar creado, aunque este vacio
for i in listaValida:
    url.write(" " + i + "\n")  # Guardar el URL en el archivo .tex


# ---------------------------------------------- PASO 5.1: Escribir en el archivo "URLNoValido.txt" los URL que no son validos
url = open("URLNoValido.txt", "w")  # El archivo resultados.tex ya debe estar creado, aunque este vacio
for i in listaNoValida:
    url.write(" " + i + "\n")  # Guardar el URLNoValido en el archivo .tex



print("URLs validos : ", len(listaValida))
print("URLs NO validos : ", len(listaNoValida))
