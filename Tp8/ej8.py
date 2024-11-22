"""""""""""

Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.

"""

def generar_diccionario():
    diccionario = {i: i**2 for i in range(1, 21)}
    return diccionario
def main():
    diccionario = generar_diccionario()
    print("Diccionario generado:")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")

main()
