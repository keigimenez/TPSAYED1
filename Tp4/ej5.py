""""

Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase
y un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original. 
Escribir también un programa para 
verificar el comportamiento de la misma. Hacer tres versiones de la función, para 
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter

"""

def filtrar_palabras(frase, N):
    palabras = frase.split()
    resultado = []
    for palabra in palabras:
        if len(palabra) >= N:
            resultado.append(palabra)
    return(resultado)

def palabras_comprension(frase, N):
    return ' '.join([palabra for palabra in frase.split() if len(palabra) >= N])

def palabras_filter(frase, N):
    return ' '.join(filter(lambda palabra: len(palabra) >= N, frase.split()))

def main():
    while True:
        frase = input("Ingresa una frase: ")
        N = int(input("Ingresa un valor entero N: "))
        print("Con ciclos normales:", filtrar_palabras(frase, N))
        print("Con comprensión de listas:", palabras_comprension(frase, N))
        print("Con filter:", palabras_filter(frase, N))

main()