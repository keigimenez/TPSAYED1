""""""""""

 Escribir un programa que permita ingresar un número entero N y genere un 
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la 
tabla de multiplicar con el formato apropiado.

"""
def generar_tabla_multiplicar(N):
    tabla_multiplicar = {i: N * i for i in range(1, 13)}
    return tabla_multiplicar

def mostrar_tabla(tabla):
    for clave, valor in tabla.items():
        print(f"{clave} x {N} = {valor}")

def main():
    N = int(input("Ingresa un número entero: "))
    tabla = generar_tabla_multiplicar(N)
    print(f"Tabla de multiplicar del {N}:")
    mostrar_tabla(tabla)

main()
