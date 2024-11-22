""""""""""

Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales 
contiene, identificando la cantidad de cada una. Devolver un diccionario con los 
resultados. Luego desarrollar un programa para leer una frase e invocar a la 
función por cada palabra que contenga la misma. Imprimir las palabras y la 
cantidad de vocales hallada.

"""

def contarvocales(palabra):
    vocales = 'aeiouAEIOU'
    conteo = {vocal: 0 for vocal in vocales}
    for letra in palabra:
        if letra in vocales:
            conteo[letra] += 1
    conteo = {vocal: cantidad for vocal, cantidad in conteo.items() if cantidad > 0}
    return conteo

def main():
    frase = input("Ingresa una frase: ")
    palabras = frase.split()
    for palabra in palabras:
        resultado = contarvocales(palabra)
        print(f"Palabra: {palabra}, Vocales: {resultado}")

main()
