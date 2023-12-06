from bs4 import BeautifulSoup
import requests
import spacy
import re


diccionario = {}

# ---------------------------------------------- PASO 1: Lectura del archivo log                                                                      # Paso 1: lectura del archivo log
archivo = open("URLValidos.txt")  # Ruta del archivo acces.log

for url in archivo:

    nlp = spacy.load("es_core_news_sm")
    stopwords = nlp.Defaults.stop_words
    try:

        # Direccion de la pagina web
        result = requests.get(url)
        page = result.text  # Contenido de la pagina
        page = page.replace("\n","")
        soup = BeautifulSoup(page,'lxml')

        html = soup.text
        html = html.lower()

        cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        cleanr = re.compile("["
                            u"\U0001F600-\U0001F64F"
                            u"\U0001F300-\U0001F5FF"
                            u"\U0001F680-\U0001F6FF"
                            u"\U0001F1E0-\U0001F1FF"
                            u"\U00002500-\U00002BEF"
                            u"\U00002702-\U000027B0"
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            u"\U0001f926-\U0001f937"
                            u"\U00010000-\U0010ffff"
                            u"\u2640-\u2642"
                            u"\u2600-\u2B55"
                            u"\u200d"
                            u"\u23cf"
                            u"\u23e9"
                            u"\u231a"
                            u"\ufe0f"
                            u"\u3030"
                            "]+", re.UNICODE)
        clean_html = re.sub(cleanr, '', html)

        doc = nlp(html)

        lista = [token.lemma_ for token in doc if token.is_stop == False]
        palabrasUnicas = set(lista)
        contar = [lista.count(palabra) for palabra in lista]

        tupla = []
        for i in palabrasUnicas:
            x = lista.count(i)
            tupla.append([i,x])

        diccionario.update({url:tupla})

    except:
        print("\nURL no valido:", url, "\n")



# ---------------------------------------------- PASO 5.1: Escribir en el archivo "URLNoValido.txt" los URL que no son validos
url = open("Diccionario.txt", "w", encoding="utf8")  # El archivo resultados.tex ya debe estar creado, aunque este vacio
url.write(str(diccionario))  # Guardar el URLNoValido en el archivo .tex

print(diccionario.values())
