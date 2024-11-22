""""""""""

 Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas 
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True 
o False. Escribir también un programa para verificar su comportamiento. Considerar 
el uso de conjuntos para resolver este ejercicio.

"""

def encajan(ficha1, ficha2):
    conjunto1 = set(ficha1)
    conjunto2 = set(ficha2)
    return len(conjunto1.intersection(conjunto2)) > 0

def main():
    ficha1 = (3, 4)
    ficha2 = (5, 4)
    resultado = encajan(ficha1, ficha2)
    if resultado:
        print(f"Las fichas {ficha1} y {ficha2} encajan")
    else:
        print(f"Las fichas {ficha1} y {ficha2} no encajan")

    ficha3 = (1, 2)
    ficha4 = (3, 5)
    resultado = encajan(ficha3, ficha4)
    if resultado:
        print(f"Las fichas {ficha3} y {ficha4} encajan")
    else:
        print(f"Las fichas {ficha3} y {ficha4} no encajan")

main()

