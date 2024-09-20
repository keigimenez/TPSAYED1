""""
  Desarrollar una función que reciba tres números enteros positivos correspondientes 
  al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe 
  tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos. 
  Devolver True o False según la fecha sea correcta o no. Realizar también un 
  programa para verificar el comportamiento de la función.

"""""

def bisiestos(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def fecha_valida(anio, mes , dia):
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False  
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    if mes == 2:
        if bisiestos(anio) and dia > 29:
            return False
        elif not bisiestos(anio) and dia > 28:
            return False
    return True

def main():
    while True:
        try:
            dia = int(input("Ingrese un dia: "))
            mes = int(input("Ingrese un mes: "))
            anio = int(input("Ingrese un anio: "))
            if fecha_valida(dia, mes, anio):
                print(f"La fecha {dia}/{mes}/{anio} es válida")
            else:
                print("La fecha ingresada es incorrecta")
        except ValueError:
            print("Por favor, ingrese valores enteros.")

main()