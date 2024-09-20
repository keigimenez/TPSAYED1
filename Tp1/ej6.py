"""""

    Desarrollar una función que reciba como parámetros dos números enteros positivos 
    y devuelva como valor de retorno el número que resulte de concatenar ambos 
    parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567.
    No se permite utilizar facilidades de Python no vistas en clase.

"""

def concatenar_numeros(num1, num2):
    resultado = num1
    
    num2_temp = num2
    num2_digitos = 0
    while num2_temp > 0:
        num2_temp //= 10
        num2_digitos += 1

    resultado *= 10 ** num2_digitos

    resultado += num2
    
    return resultado
def main():
    while True:
        try:
            num1 = int(input("ingrese un valor: "))
            num2 = int(input("ingrese otro valor: "))
            resultado = concatenar_numeros(num1, num2)
            print(f"El resultado de concatenar {num1} y {num2} es: {resultado}")
        except ValueError:
            print("Por favor, ingrese un número válido.")
            break

main()