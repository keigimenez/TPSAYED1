""""

Muchas aplicaciones financieras requieren que los números sean expresados también en letras. 
Por ejemplo, el número 2153 puede escribirse como "dos mil ciento 
cincuenta y tres". Escribir un programa que utilice una función para convertir un 
número entero entre 0 y 1 billón (1.000.000.000.000) a letras. ¿En qué cambiaría 
la función si también aceptara números negativos? ¿Y números con decimales?

"""

def convertir_a_letras(n):
    if n < 0:
        return "menos " + convertir_a_letras(-n)

    if n == 0:
        return "cero"

    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    partes = []

    if n >= 100:
        partes.append(centenas[n // 100])
        n %= 100

    if n >= 20:
        partes.append(decenas[n // 10])
        n %= 10

    if n > 0:
        partes.append(unidades[n])

    return " ".join(partes).strip()

def convertir_a_letras_decimal(n):
    parte_entera = int(n)
    parte_decimal = str(n).split('.')[1]
    letras_decimal = " ".join(convertir_a_letras(int(d)) for d in parte_decimal)
    return convertir_a_letras(parte_entera) + " punto " + letras_decimal

def main():
    numero = int(input("Introduce un número (puede ser negativo o decimal): "))
    if '.' in str(numero):
        resultado = convertir_a_letras_decimal(numero)
    else:
        resultado = convertir_a_letras(int(numero))
    
    print(f"El número {numero} se escribe como: {resultado}")

main()