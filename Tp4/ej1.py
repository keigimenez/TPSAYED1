""""

Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento.

"""

def capicua(cadena):
    longitud = len(cadena)
    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud - 1 - i]:
            return False
    return True

def main():
    cadena = input("Introduce una cadena de caracteres: ")
    if capicua(cadena):
        print(f"La cadena '{cadena}' es capicúa.")
    else:
        print(f"La cadena '{cadena}' no es capicúa.")

main()