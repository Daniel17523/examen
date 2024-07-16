
print("bienvenido al programa de sueldos")

import random
import csv

trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = []

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("sueldos asignados aleatoriamente.")

def clasificar_sueldos():
    menores_800k = [(trabajadores[i], sueldo) for i, sueldo in enumerate(sueldos) if sueldo < 800000]
    entre_800k_2M = [(trabajadores[i], sueldo) for i, sueldo in enumerate(sueldos) if 800000 <= sueldo <= 2000000]
    superiores_2M = [(trabajadores[i], sueldo) for i, sueldo in enumerate(sueldos) if sueldo > 2000000]

    print("sueldos menores a $800.000")
    for emp, sueldo in menores_800k:
        print(f"{emp}: ${sueldo}")

    print("\nsueldos medios entre $800.000 y $2.000.000")
    for emp, sueldo in entre_800k_2M:
        print(f"{emp}: ${sueldo}")

    print("\nsueldos mayores a $2.000.000")
    for emp, sueldo in superiores_2M:
        print(f"{emp}: ${sueldo}")

def ver_estadisticas():
    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    promedio_sueldo = sum(sueldos) / len(sueldos)
    media_geometrica = (max_sueldo * min_sueldo) ** 0.5

    print(f"sueldo más alto: ${max_sueldo}")
    print(f"sueldo más bajo: ${min_sueldo}")
    print(f"promedio de sueldos: ${promedio_sueldo:.2f}")
    print(f"media geométrica: ${media_geometrica:.2f}")

def reporte_sueldos():
    descuentos = [(sueldo * 0.07, sueldo * 0.12) for sueldo in sueldos]
    sueldos_liquidos = [sueldo - d[0] - d[1] for sueldo, d in zip(sueldos, descuentos)]

    with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i, emp in enumerate(trabajadores):
            writer.writerow({
                'Nombre empleado': emp,
                'Sueldo Base': sueldos[i],
                'Descuento Salud': descuentos[i][0],
                'Descuento AFP': descuentos[i][1],
                'Sueldo Líquido': sueldos_liquidos[i]
            })

    print("Reporte de sueldos generado.")

def salir_programa():
    print("finalizando programa…")
    print("desarrollado por DANIEL")
    print("RUT 12.345.678-9")
    exit()

def menu():
    while True:
        print("\nMenu de opciones:")
        print("1.- asignar sueldos aleatorios")
        print("2.- clasificar sueldos")
        print("3.- ver estadísticas")
        print("4.- reporte de sueldos")
        print("5.- salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            asignar_sueldos_aleatorios()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            salir_programa()
        else:
            print("Opción no válida, intente nuevamente.")

menu()
