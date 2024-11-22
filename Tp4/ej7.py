""""

Escribir una función para eliminar una subcadena de una cadena de caracteres, a 
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. 
Escribir también un programa para verificar el comportamiento de la misma. 
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas

"""

def eliminar_rebanadas(cadena, posicion, cantidad):
    return cadena[:posicion] + cadena[posicion + cantidad:]

def eliminar_sin_rebanadas(cadena, posicion, cantidad):
    resultado = ""
    for i in range(len(cadena)):
        if i < posicion or i >= posicion + cantidad:
            resultado += cadena[i]
    return resultado

def main():
    cadena_original = "bienvenido, este es un ejemplo."
    posicion = 7
    cantidad = 4
    resultado_rebanadas = eliminar_rebanadas(cadena_original, posicion, cantidad)
    print("Cadena original:", cadena_original)
    print("Cadena resultante (rebanadas):", resultado_rebanadas)
    resultado_sin_rebanadas = eliminar_sin_rebanadas(cadena_original, posicion, cantidad)
    print("Cadena resultante (sin rebanadas):", resultado_sin_rebanadas)

main()