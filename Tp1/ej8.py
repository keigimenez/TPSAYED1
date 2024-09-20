"""""
  siguiente función permite averiguar el día de la semana para una fecha determinada. La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para 
  imprimir por pantalla el calendario de un mes completo, correspondiente a un mes 
  y año cualquiera basándose en la función suministrada. Considerar que la semana 
  comienza en domingo.
              def diadelasemana(dia,mes,año):
                  if mes < 3:
                    mes = mes + 10
                    año = año – 1
                 else:
                   mes = mes – 2
                  siglo = año // 100
                   año2 = año % 100
                 diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
                   if diasem < 0:
                     diasem = diasem + 7
                 return diasem

"""
def diadelasemana(dia, mes, anio):
    if mes < 3:
        mes += 10
        anio -= 1
    else:
        mes -= 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if diasem < 0:
        diasem += 7
    return diasem

def dias_del_mes(mes, anio):
    if mes == 2: 
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return 29
        else:
            return 28
    elif mes in [4, 6, 9, 11]: 
        return 30
    else:  
        return 31

def imprimir_calendario(mes, anio):
    print(f"Calendario de {mes}/{anio}")
    print("Do Lu Ma Mi Ju Vi Sá")


    primer_dia = diadelasemana(1, mes, anio)
    dias_mes = dias_del_mes(mes, anio)
    
    for _ in range(primer_dia):
        print("   ", end="") 
    
    for dia in range(1, dias_mes + 1):
        print(f"{dia:2}", end=" ")  
        primer_dia += 1
        if primer_dia == 7:
            primer_dia = 0
            print() 

    if primer_dia != 0:
        print()


def main():
    while True:
        try:
            mes = int(input("\nIngrese un número de mes (1-12) o 0 para salir: "))
            if mes == 0:
                print("Saliendo del programa.")
                break
            if mes < 1 or mes > 12:
                print("Por favor, ingrese un número de mes válido entre 1 y 12.")
                continue
            anio = int(input("Ingrese un año: "))
            imprimir_calendario(mes, anio)
        except ValueError:
            print("Por favor, ingrese un número válido.")
            break

main()