# def mostrar_bienvenida_nombre(nombre: str):
#     print(f"Hola {nombre}, bienvenida")
#
# def mostrar_edad(edad: int):
#     print(f"Tu edad es: {edad}")
#
# # Llamar las funciones directamente
# nombre = input("Introduce tu nombre: ")
# mostrar_bienvenida_nombre(nombre)
#
# edad = int(input("Cual es tu edad?: "))
# mostrar_edad(edad)

# def mostrar_bienvenida_nombre(nombre: str):
#     return f"Hola {nombre}, bienvenida. "
#
# def mostrar_edad(edad: int):
#     return f"Tu edad es: {edad}"
#
# # Ahora sí puedes usar print con ambas funciones
# nombre = input("Introduce tu nombre: ")
# edad = int(input("Cual es tu edad?: "))
#
# print(mostrar_bienvenida_nombre(nombre))
# print(mostrar_edad(edad))
#
# # O en un solo print:
# print(mostrar_bienvenida_nombre(nombre), mostrar_edad(edad))

# def suma(a,b):
#     c = a + b
#     return c
# total = suma(5,5)
# print(f"La suma es: {total}")

# def multiplicacion(a,b):
#     c = a * b
#     return c
# total_multiplicacion = multiplicacion(5,5)
# print(f"\nEl resultado de la multiplicación es: {total_multiplicacion}")

# num1 = int(input("\nIntroduce un numero: "))
# num2 = int(input("Introduce otro numero: "))
# def resta(numero1:int,numero2:int):
#     total_resta = numero1 - numero2
#     return total_resta
# print(f"El resultado de la resta: ", resta(num1,num2))

# while True:
#     numero = int(input("\nIntroduce un numero: "))
#     def par(numero1:int):
#         if numero % 2 == 0:
#             print(f"Es par el numero: {numero1}")
#     par(numero)
#
#     def impar(numero1:int):
#         if numero % 2 == 1:
#             print(f"Es impar el numero: {numero1}")
#     impar(numero)

# while True:
#     numero1 = int(input("\nIngrese un numero: "))
#     numero2 = int(input("Ingrese otro numero: "))
#
#     def sumar(numero_1, numero_2):
#         resultado_sum = numero_1 + numero_2
#         return resultado_sum
#     resultado_suma = sumar(numero1, numero2)
# #    print(sumar(numero1, numero2))
#
#     def modulo (resultado):
#         if resultado % 2 == 0:
#             return f"El resultado de la operación es par: {resultado}"
#         else:
#             return f"El resultado es impar: {resultado}"
#     print(modulo(resultado_suma))

# list_num = []
# for i in range(4):
#     numero = int(input(f"\nIngrese un numero {i+1}: "))
#     list_num.append(numero)
# def promedio_list(lista):
#     promedio = sum(lista) / len(lista)
#     return f"Tu promedio es: {promedio}"
# print(promedio_list(list_num))

# lista = []
# nombre = ""
# while nombre != "Andres".lower:
#     nombre = input("Ingresa un nombre: ")
#     lista.append(nombre)
