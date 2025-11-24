# Pide cuántas veces quieres validar números
# Luego en un bucle, ingresa números y te dice si son positivos, negativos o cero
# datos = int(input("Cuantas veces quiere validar un numero?: "))
# for i in range (datos):
#     num = int(input("\nIngresa tu numero: "))
#     if num > 0:
#         print("Tu numero es positivo")
#     elif num == 0:
#         print("Tu numero es cero")
#     else:
#         print("Tu numero es negativo")

# Imprime "<3 Medellin" junto con los números del 4 al 15
# for i in range (4, 16):
#    print("<3 Medellin", i)

# Crea una lista de frutas y recorre cada una imprimiendo "Me gusta la: [fruta]"
# frutas = ["manzana", "pera", "uva"]
# for fruta in frutas:
#     print("Me gusta la: ", fruta)

# Lista de 10 animales
# Primer for: imprime todos los animales
# Segundo for: usa slicing [6::8] - empieza en índice 6 (leon), salta de 8 en 8
#   Entonces solo imprime "leon" (índice 6) porque el siguiente sería índice 14 (fuera de rango)
# Los prints muestran individualmente animales[6]="leon" y animales[8]="chinche"
# animales = ["perro", "gato", "perico", "loro", "pez", "leon", "hiena", "hormiga", "chinche", "tuteca"]
# for animal in animales:
#     print("Animal: ", animal)
# for elem in animales[6 :: 8]:
#     print(elem)
# print(animales[6])
# print(animales[8])

# Recorre de 0 a 50, saltando de 2 en 2 (solo números pares)
# for num in range(0, 51 ,2):
#     print(num)

# Recorre de -2 a 99, de 2 en 2 (solo números pares por el salto)
# Verifica con módulo si es par o impar
# Nota: Como va de 2 en 2, TODOS serán pares, así que el else nunca se ejecuta
# for num in range(-2, 100, 2):
#     # Muestra los pares y impares de esa lista
#     if num % 2 == 0:
#         print("Es par:", num)
#    else:
#        print("Es impar:", num)

# Recorre de 0 a 99, de 3 en 3 (múltiplos de 3)
# Verifica si cada número es par o impar
# Aquí sí habrá mezcla: 0(par), 3(impar), 6(par), 9(impar), etc.
# for num in range(0, 100, 3):
#     if num % 2 == 0:
#         print("Es par:", num)
#     else:
#         print("Es impar:", num)

# Sistema de menú con While True (bucle infinito hasta que elijas "Salir")
# Opciones:
#   1. Agregar carros a la lista (append)
#   2. Eliminar un carro por nombre (remove)
#   3. Mostrar todos los carros
#   4. Salir del programa (break)
# Es un CRUD básico (Create, Read, Update, Delete) usando listas
# carros = []
# while True:
#     print("\nMenu")
#     print("1. Ingresar carros")
#     print("2. Remover carros")
#     print("3. Listar carros")
#     print("4. Sair")
#     opc=int(input("¿Que desea realizar?: "))
#     if opc == 1:
#         num = int(input("\n¿Cuántos carros desea ingresar?: "))
#         for i in range(num):
#             agg = input("Ingresa una marca de carro: ")
#             carros.append(agg)
#         print("=" * 50)
#     elif opc == 2:
#         rem = input("Elimina una marca de carros: ").lower()
#         carros.remove(rem)
#         print(carros)
#         print("=" * 50)
#     elif opc == 3:
#         print("\nLista de marcas ingresadas:")
#         print(carros)
#         print("=" * 50)
#     elif opc == 4:
#         print("\nBayyy")
#         break
#     else:
#         print("\nOpcion invalida")
#         print("=" * 50)