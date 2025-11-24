## Practica en clase
# import csv
#
# def crear_csv(nombre, encabezados):
#     with open(nombre, "w", newline="") as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(encabezados)
#     return (f"Tu archivo creado es: {nombre}\n"
#             f"Lo encabezados son: {encabezados}")

import csv

def crear_csv(nombre_archivo, encabezados):
    with open(nombre_archivo, "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(encabezados)
    return (f"Tu archivo creado es: {nombre_archivo}\n"
            f"Lo encabezados son: {encabezados}")

def leer_tipo(nombre_archivo):
    target_nombre = "Tipo Usuario"
    with open(nombre_archivo, "r", newline="") as archivo:
        reader = csv.reader(archivo)
        try:
            headers = next(reader)
        except ValueError:
            return "Hay error"
        for h in headers:
            if h and h.strip().lower().replace(" ", "") == target_nombre:
                return h.strip()
    return ""


def agregar_linea(nombre_archivo, datos):
    with open(nombre_archivo, "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(datos)
    return "Agregado Correctamente"