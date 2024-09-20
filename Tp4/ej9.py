""""

Escribir una función que reciba como parámetro una cadena de caracteres en la que 
las palabras se encuentran separadas por uno o más espacios. Devolver otra 
cadena con las palabras ordenadas según su longitud, dejando un espacio entre 
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la 
longitud de las palabras, pero deberán conservarse en la cadena final.

"""

def ordenar_palabras_por_longitud(cadena):
    partes = []
    palabra = ""
    for caracter in cadena:
        if caracter.isalnum():
            palabra += caracter
        else:
            if palabra:
                partes.append(palabra)
                palabra = ""
            partes.append(caracter)
    if palabra:
        partes.append(palabra)

    palabras = [parte for parte in partes if parte.isalnum()]
    palabras_ordenadas = sorted(palabras, key=len)
    
    resultado = []
    palabra_index = 0
    for parte in partes:
        if parte.isalnum():
            resultado.append(palabras_ordenadas[palabra_index])
            palabra_index += 1
        else:
            resultado.append(parte) 
    return ''.join(resultado)


def main():
    cadena = "viva korn"
    resultado = ordenar_palabras_por_longitud(cadena)
    print(resultado)

main()
