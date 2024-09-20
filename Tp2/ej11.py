""""

Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que 
ingresa se anuncia en la recepción indicando su número de afiliado (número entero 
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con 
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego 
se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de 
los pacientes atendidos por turno en el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue 
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta 
que se ingrese -1 como número de afiliado.

"""

def registro_paciente(pacientes_urgencia, pacientes_turno):
    while True:
        num_afiliado = int(input("Ingrese número de afiliado (4 dígitos,-1 para salir): "))
        if num_afiliado == -1:
            break
        tipo_atencion = int(input("Ingrese tipo de atención (0 para urgencia,1 para turno): "))
        if tipo_atencion == 0:
            pacientes_urgencia.append(num_afiliado)
        elif tipo_atencion == 1:
            pacientes_turno.append(num_afiliado)
        else:
            print("Tipo de atención no válido.")

def listados(pacientes_urgencia, pacientes_turno):
    print("Pacientes atendidos por urgencia:")
    for afiliado in pacientes_urgencia:
        print(afiliado)
    print("Pacientes atendidos por turno:")
    for afiliado in pacientes_turno:
        print(afiliado)

def buscar_afiliado(pacientes_urgencia, pacientes_turno):
    while True:
        num_afiliado = int(input("Ingrese número de afiliado para buscar (-1 para salir): "))
        if num_afiliado == -1:
            break
        atendido_urgencia = pacientes_urgencia.count(num_afiliado)
        atendido_turno = pacientes_turno.count(num_afiliado)
        print(f"Número de veces atendido por urgencia: {atendido_urgencia}")
        print(f"Número de veces atendido por turno: {atendido_turno}")

def menu():
    pacientes_urgencia = []
    pacientes_turno = []
    while True:
        print("1. Registrar paciente")
        print("2. Mostrar listados")
        print("3. Buscar afiliado")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            registro_paciente(pacientes_urgencia, pacientes_turno)
        elif opcion == 2:
            listados(pacientes_urgencia, pacientes_turno)
        elif opcion == 3:
            buscar_afiliado(pacientes_urgencia, pacientes_turno)
        elif opcion == 4:
            break
        else:
            print("Opción no válida.")

menu()

