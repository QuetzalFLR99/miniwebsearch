import requests

archivo = open("C:\\xampp\\apache\\logs\\error.log")

lista = []
palabra = ""
for fila in archivo:

    if "http:" in fila:

        # Ciclo para identificar cada palabra
        for j in range(len(fila)):
            if fila[j] != " ":  # Si cada elemento del texto es diferente de un espacio en blanco
                if fila[j] != "[":
                    palabra += fila[j]
            if fila[j] == " ":
                lista.append(palabra)  # Si encuentra un espacio en blanco, quiere decir que es una nueva palabra
                palabra = ""  # Despues de guardar la palabra, creamos una nueva

        for i in lista:

            if "http:" in i:
                print(i,end="\n")

print(lista)