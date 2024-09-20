""""

Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y 
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En 
qué cambiaría la función si el rango de valores fuese diferente

"""

def numero_romano(num):
    if not (0 < num < 4000):
        return "Número fuera de rango"
    
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    val_romano = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    romano_num = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            romano_num += val_romano[i]
            num -= val[i]
        i += 1
    return romano_num

def main():
    while True:
        try:
            num = int(input("Ingresa un número entero entre 1 y 3999 (o 0 para salir): "))
            if num == 0:
                print("Saliendo...")
                break
            romano = numero_romano(num)
            print(f"El número romano es: {romano}")
        except ValueError:
            print("Por favor,ingresa un número válido.")

main()