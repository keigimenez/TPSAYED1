""""""""""""""""

Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al 
usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido del conjunto 
luego de cada eliminación. Finalizar el proceso al ingresar -1. 
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos 
inexistentes.

"""

def main():
    numeros = set(range(10))
    print(f"Conjunto inicial: {numeros}")

    while True:
        try:
            valor = int(input("Ingresa un número para eliminar del conjunto (o -1 para terminar): "))
            if valor == -1:
                break
            numeros.remove(valor)
            print(f"Conjunto después de eliminar {valor}: {numeros}")
        except KeyError:
            print(f"El valor {valor} no está en el conjunto.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

    print("Proceso finalizado.")

main()
