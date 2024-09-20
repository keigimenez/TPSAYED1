"""""

   Resolver el siguiente problema utilizando funciones:
   Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso 
   para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y 
   cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón 
   caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso 
   de alguna naranja se encuentra fuera del rango indicado se la clasifica para 
   procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas 
   cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para 
   jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente 
   reparto. Simular el peso de cada unidad generando un número entero al azar entre 
   150 y 350.
   Además, se desea saber cuántos camiones se necesitan para transportar la cosecha,
   considerando que la ocupación del camión no debe ser inferior al 80%; en 
   caso contrario el camión no serán despachado por su alto costo.

"""
import random as rn

def peso_naranja():
    return rn.randint(150, 350)

def cuenta_naranjas(cantidad_naranjas):
    cajones_llenos = 0
    naranjas_para_jugo = 0
    naranjas_sobrantes = 0
    peso_total = 0
    
    for _ in range(cantidad_naranjas):
        peso = peso_naranja()
        if 200 <= peso <= 300:
            peso_total += peso
            if peso_total >= 50000:
                cajones_llenos += 1
                peso_total = 0
        else:
            naranjas_para_jugo += 1
    
    naranjas_sobrantes = cantidad_naranjas - (cajones_llenos * 250) - naranjas_para_jugo
    return cajones_llenos, naranjas_para_jugo, naranjas_sobrantes

def calcular_camiones_necesarios(cajones_llenos):
    capacidad_camion = 500
    camiones_necesarios = cajones_llenos // capacidad_camion
    if cajones_llenos % capacidad_camion > 0:
        camiones_necesarios += 1    
    return camiones_necesarios

def main():
    while True:
        try:
            usuario = int(input("Ingrese la cantidad de naranjas cosechadas: "))
            cajones_llenos, naranjas_para_jugo, naranjas_sobrantes = cuenta_naranjas(usuario)
            camiones_necesarios = calcular_camiones_necesarios(cajones_llenos)
            print(f"Cajones llenos: {cajones_llenos}")
            print(f"Naranjas para jugo: {naranjas_para_jugo}")
            print(f"Naranjas sobrantes: {naranjas_sobrantes}")
            print(f"Camiones necesarios: {camiones_necesarios}")
        except ValueError:
            print("Por favor, ingrese un número válido.")
            break

main()

