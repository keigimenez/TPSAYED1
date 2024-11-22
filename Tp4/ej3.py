""""

Los números de claves de dos cajas fuertes están intercalados dentro de un número 
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa 
para obtener ambas claves, donde la primera se construye con los dígitos ubicados 
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en 
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave 
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89

"""

def claves(clave_maestra):
    c1 = ""  
    c2 = "" 

    for i in range(len(clave_maestra)):
        if (i + 1) % 2 == 1:
            clave1 += clave_maestra[i]
        else:
            clave2 += clave_maestra[i]

    return c1, c2

def main():
    clave_maestra = input("Ingrese la clave maestra: ")
    c1, c2 = claves(clave_maestra)
    print("Clave 1:", c1)
    print("Clave 2:", c2)

main()
