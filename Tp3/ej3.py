""""

 Desarrollar un programa para rellenar una matriz de N x N con números enteros al 
azar comprendidos en el intervalo [0,N2),
de tal forma que ningún número se repita. Imprimir la matriz por pantalla.

"""

import random as rn

def generar_matriz(N):
    matriz = [[0] * N for _ in range(N)]
    numeros_usados = set()   
    for i in range(N):
        for j in range(N):
            numero = rn.randint(0, N * N - 1)
            while numero in numeros_usados:
                numero = rn.randint(0, N * N - 1)
            matriz[i][j] = numero
            numeros_usados.add(numero)

    for fila in matriz:
        print(fila)

def main():
    N = int(input("Introduce el tamaño de la matriz (N): "))
    generar_matriz(N)
    return

main()
