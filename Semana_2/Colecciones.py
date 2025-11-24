# Listas
# Set
# Librerias
#

# def promedio():
#     suma = sum(lista)
#     promedioo = suma/len(lista)
#     return promedioo
#
# lista = []
# for i in range(5):
#     ingresar = int(input("Ingresar numero: "))
#     lista.append(ingresar)
#
# print(promedio())

# lista = []
# def eliminar_repetidos(listaa):
#     resultado = []
#     for elemento in listaa:
#         if elemento not in resultado:
#             resultado.append(elemento)
#     return resultado
#
# while True:
#     entrada = input("Ingresar numero: ").strip()
#     if entrada == "0":
#         break
#     try:
#         num = int(entrada)
#     except ValueError:
#         print("Entrada no válida, ingresa un número o 0 para salir.")
#         continue
#     lista.append(num)
#
# print(eliminar_repetidos(lista))

# def invertida(lista):
#     lista.reverse()
#     return lista
#
# numeros = [1,2,3,4,5,6,7,8,9,10]
# lista = invertida(numeros)
# print(lista)

# nombres = ("Ana", "Juan", "María", "Ana", "Luis", "Ana")
# lista_temporal = list(nombres)
#
# while True:
#     name = input("Ingrese su nombre: ").capitalize()
#     if name == "salir".capitalize():
#         break
#     try:
#         num = str(name)
#     except ValueError:
#         print("Entrada no válida.")
#         continue
#     lista_temporal.append(name)
#
# nombress = tuple(lista_temporal)
# buscar = input("\nNombre a buscar: ").strip().capitalize()
# veces = nombress.count(buscar)
# print(f"El nombre {buscar} aparece {veces} veces en la tupla.")

