"""""
   5. Escribir funciones lambda para:
   a. Informar si un número es oblongo. Se dice que un número es oblongo cuando 
   se puede obtener multiplicando dos números naturales consecutivos. Por ejemplo 6 es
   oblongo porque resulta de multiplicar 2 * 3.
   b. Informar si un número es triangular. Un número se define como triangular si 
   puede expresarse como la suma de un grupo de números naturales consecutivos comenzando desde 1. 
   Por ejemplo 10 es un número triangular porque se 
   obtiene sumando 1+2+3+4.
   Ambas funciones lambda reciben como único parámetro el número a evaluar y devuelven True o False.
   No se permite utilizar ayudas externas a las mismas.

"""
oblongo = lambda n: any(i * (i + 1) == n for i in range(1, int(n**0.5) + 1))

triangular = lambda n: any(sum(range(1, i + 1)) == n for i in range(1, n + 1))

def main():
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            if oblongo(num):
                print(f"{num} es un oblongo")
            else:
                print("numero ingresado no corresponde con oblongo")

            if triangular(num):
                print(f"{num} es triangular")
            else:
                print("numero ingresado no corresponde con triangular")
        except ValueError:
            print("Por favor, ingrese un número válido.")
            break

main()
