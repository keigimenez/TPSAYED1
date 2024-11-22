""""

Desarrollar una función que extraiga una subcadena de una cadena de caracteres, 
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena 
como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma. 
Ejemplo, dada la cadena "El número de teléfono es 4356-
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres, 
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas

"""

def extraer_rebanadas(cadena, posicion, cantidad):
    return cadena[posicion:posicion + cantidad]

def extraer_sin_rebanadas(cadena, posicion, cantidad):
    subcadena = ""
    for i in range(posicion, posicion + cantidad):
        subcadena += cadena[i]
    return subcadena

def main():
    cadena = "número de teléfono 4356-7890"
    posicion = 25
    cantidad = 9    
    resultado_rebanadas = extraer_rebanadas(cadena, posicion, cantidad)
    print(f"Subcadena extraída (usando rebanadas): '{resultado_rebanadas}'")    
    resultado_sin_rebanadas = extraer_sin_rebanadas(cadena, posicion, cantidad)
    print(f"Subcadena extraída (sin usar rebanadas): '{resultado_sin_rebanadas}'")

main()