""""

Desarrollar una función que devuelva una subcadena con los últimos N caracteres 
de una cadena dada. La cadena y el valor de N se pasan como parámetros

"""

def ultimos_caracteres(cadena, n):
    if n > len(cadena):
        return "El valor de N es mayor que la longitud de la cadena."
    return cadena[-n:]

def main():
    cadena = input("Ingresa la cadena: ")
    n = int(input("Ingresa el valor de N: "))
    resultado = ultimos_caracteres(cadena, n)
    print("Los últimos N caracteres son:", resultado)

main()
