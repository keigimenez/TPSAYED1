""""
  Desarrollar una función que reciba tres números enteros positivos y devuelva el 
  mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en 
  caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar 
  también un programa para ingresar los tres valores, invocar a la función y mostrar 
  el máximo hallado, o un mensaje informativo si éste no existe.

"""
def mayor_estricto(a, b, c):
    if a > b:
        if a > c:
            mayor = a
        else:
            mayor = c
    else:
        if b > c:
            mayor = b
        else:
            mayor = c
    
    cuenta_max = 0
    if a == mayor:
        cuenta_max += 1
    if b == mayor:
        cuenta_max += 1
    if c == mayor:
        cuenta_max += 1
    if cuenta_max == 1:
        return mayor
    else:
        return -1
    
def main():
    a = int(input("Ingresa su primer número: "))
    b = int(input("Ingresa su segundo número: "))
    c = int(input("Ingresa su tercer número: "))
    
    resultado = mayor_estricto(a, b, c)
    
    if resultado != -1:
        print(f"El mayor valor estricto es: {resultado}")
    else:
        print("No hay un valor mayor en la funcion.")


main()

