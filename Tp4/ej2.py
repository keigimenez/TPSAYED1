"""

Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la 
misma tiene 80 columnas.

"""

def centrado(texto):
    ancho_pantalla = 80
    espacio_izquierda = (ancho_pantalla - len(texto)) // 2
    print(' ' * espacio_izquierda + texto)

def main():
    cadena = input("Introduce una cadena de caracteres: ")
    centrado(cadena)

main()
