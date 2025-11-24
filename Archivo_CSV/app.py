## Practica en clase
# from servicios import *
#
# nombre = "archivo.csv"
#
# print(crear_csv(nombre, ["Nombre", "Edad"]))
from servicios import crear_csv, agregar_linea, leer_tipo

nombre_archivo = "archivo.csv"
encabezados = ["Nombre", "Tipo Usuario"]

print(crear_csv(nombre_archivo, encabezados))
print(agregar_linea(nombre_archivo, ["Andres.David", "Tl"]))
print(leer_tipo(nombre_archivo))
