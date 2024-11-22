""""

Escribir una función que reciba una lista de números enteros como parámetro y la 
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones 
relativas que cada elemento tiene en la lista original. Desarrollar también 
un programa que permita verificar el comportamiento de la función. Por ejemplo, 
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].

"""

def normalizar(lista):
    suma_total = sum(lista)
    return [x / suma_total for x in lista]

def main():
    lista = [1, 1, 2]
    lista_normalizada = normalizar(lista)
    print(f"Lista original: {lista}")
    print(f"Lista normalizada: {lista_normalizada}")
    print(f"Suma de elementos normalizados: {sum(lista_normalizada)}")
    
main()