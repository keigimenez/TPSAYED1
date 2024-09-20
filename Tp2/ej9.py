"""""

Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 
que no sean múltiplos de 5. A y B se ingresar desde el teclado.

"""
def multiplo(A, B):
    return[num for num in range(A, B + 1) if num % 7 == 0 and num % 5 != 0]

def main():
    A = int(input("Ingrese un valor para A: "))
    B = int(input("Ingrese un valor para B: "))
    resultados = multiplo(A, B)
    print("Los múltiplos de 7 que no son múltiplos de 5 entre", A, "y", B, "son:", resultados)

main()
