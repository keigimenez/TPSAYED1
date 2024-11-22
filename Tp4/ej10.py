""""

 Desarrollar una función para reemplazar todas las apariciones de una palabra por 
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la 
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse 
palabras completas, y no fragmentos de palabras. Escribir también un programa 
para verificar el comportamiento de la función.

"""

def reemplazar(cadena, palabra_a_reemplazar, nueva_palabra):
    palabras = cadena.split()
    contador = 0
    for i in range(len(palabras)):
        if palabras[i] == palabra_a_reemplazar:
            palabras[i] = nueva_palabra
            contador += 1
    nueva_cadena = ' '.join(palabras)
    return nueva_cadena, contador

def main():
    texto = "aguante el metal y el rock de los 80s"
    palabra_original = "metal"
    palabra_nueva = "rock" 
    resultado, cantidad_reemplazos = reemplazar(texto, palabra_original, palabra_nueva)
    print("Cadena original:", texto)
    print("Cadena modificada:", resultado)
    print("Cantidad de reemplazos realizados:", cantidad_reemplazos)

main()
