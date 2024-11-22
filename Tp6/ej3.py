"""""""""

Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los 
próximos Juegos Panamericanos. Para eso encargó la realización de un programa 
que incluya las siguientes funciones:
GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas 
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una 
línea distinta. Ejemplo:
<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atletas,
leyendo los datos del archivo generado en el paso anterior. La disciplina y el 
promedio deben grabarse en líneas diferentes. Ejemplo:
<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>
< . . . >

MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas 
superan la estatura promedio general. Obtener los datos del segundo archivo.

"""

def RangoAlturas():
    try:
        with open('alturas.txt', 'w') as archivo:
            while True:
                deporte = input("Ingresa el nombre del deporte (o 'fin' para terminar): ")
                if deporte.lower() == 'fin':
                    break
                archivo.write(f"{deporte}\n")
                while True:
                    altura = input(f"Ingresa la altura del atleta para {deporte} (o 'fin' para terminar): ")
                    if altura.lower() == 'fin':
                        break
                    archivo.write(f"{altura}\n")
        print("Alturas grabadas correctamente.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

def GrabarPromedio():
    try:
        with open('alturas.txt', 'r') as archivo_entrada, open('promedios.txt', 'w') as archivo_salida:
            lineas = archivo_entrada.readlines()
            deporte = None
            alturas = []
            for linea in lineas:
                if not linea.strip().isdigit():
                    if deporte and alturas:
                        suma_alturas = sum(map(int, alturas))
                        promedio = suma_alturas // len(alturas)
                        archivo_salida.write(f"{deporte}\n{promedio}\n")
                    deporte = linea.strip()
                    alturas = []
                else:
                    alturas.append(linea.strip())
            if deporte and alturas:
                suma_alturas = sum(map(int, alturas))
                promedio = suma_alturas // len(alturas)
                archivo_salida.write(f"{deporte}\n{promedio}\n")
        print("Promedios grabados correctamente.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

def MostrarMasAltos():
    try:
        with open('promedios.txt', 'r') as archivo:
            lineas = archivo.readlines()
            promedios = []
            for i in range(0, len(lineas), 2):
                deporte = lineas[i].strip()
                promedio = int(lineas[i+1].strip())
                promedios.append((deporte, promedio))
            promedio_general = sum(p[1] for p in promedios) // len(promedios)
            print(f"Promedio general de alturas: {promedio_general}")
            print("Disciplinas con atletas que superan el promedio general:")
            for deporte, promedio in promedios:
                if promedio > promedio_general:
                    print(f"{deporte}: {promedio}")
    except Exception as e:
        print(f"Se produjo un error: {e}")

RangoAlturas()
GrabarPromedio()
MostrarMasAltos()
