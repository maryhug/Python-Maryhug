def ejercicio1():
    """Validador de números positivos/negativos"""
    print("\n=== EJERCICIO 1: Validador de números ===")
    datos = int(input("¿Cuántas veces quiere validar un número?: "))

    for i in range(datos):
        num = int(input(f"\nIngresa tu número {i + 1}: "))
        if num > 0:
            print("Tu número es positivo")
        elif num == 0:
            print("Tu número es cero")
        else:
            print("Tu número es negativo")

def ejercicio2():
    """Imprimir <3 Medellín con números"""
    print("\n=== EJERCICIO 2: <3 Medellín ===")
    for i in range(4, 16):
        print("<3 Medellín", i)

def ejercicio3():
    """Recorrer lista de frutas"""
    print("\n=== EJERCICIO 3: Lista de frutas ===")
    frutas = ["manzana", "pera", "uva"]
    for fruta in frutas:
        print("Me gusta la:", fruta)

def ejercicio4():
    """Trabajar con lista de animales"""
    print("\n=== EJERCICIO 4: Lista de animales ===")
    animales = ["perro", "gato", "perico", "loro", "pez", "leon", "hiena", "hormiga", "chinche", "tuteca"]

    print("\nTodos los animales:")
    for animal in animales:
        print("Animal:", animal)

    print("\nAnimales con slicing [6::8]:")
    for elem in animales[6::8]:
        print(elem)

    print(f"\nAnimal en índice 6: {animales[6]}")
    print(f"Animal en índice 8: {animales[8]}")

def ejercicio5():
    """Números pares de 0 a 50"""
    print("\n=== EJERCICIO 5: Números pares de 0 a 50 ===")
    for num in range(0, 51, 2):
        print(num, end=" ")
    print()  # Salto de línea al final

def ejercicio6():
    """Pares e impares de -2 a 99 (de 2 en 2)"""
    print("\n=== EJERCICIO 6: Pares e impares de -2 a 99 ===")
    for num in range(-2, 100, 2):
        if num % 2 == 0:
            print("Es par:", num)
        else:
            print("Es impar:", num)

def ejercicio7():
    """Múltiplos de 3 entre 0 y 99"""
    print("\n=== EJERCICIO 7: Múltiplos de 3 (pares e impares) ===")
    for num in range(0, 100, 3):
        if num % 2 == 0:
            print("Es par:", num)
        else:
            print("Es impar:", num)

def ejercicio8():
    """Menú CRUD de carros"""
    print("\n=== EJERCICIO 8: Gestión de carros ===")
    carros = []

    while True:
        print("\n--- Menú de Carros ---")
        print("1. Ingresar carros")
        print("2. Remover carros")
        print("3. Listar carros")
        print("4. Salir")

        try:
            opc = int(input("¿Qué desea realizar?: "))

            if opc == 1:
                num = int(input("\n¿Cuántos carros desea ingresar?: "))
                for i in range(num):
                    agg = input(f"Ingresa marca de carro {i + 1}: ")
                    carros.append(agg)
                print("=" * 50)

            elif opc == 2:
                if not carros:
                    print("No hay carros para eliminar")
                else:
                    print(f"Carros disponibles: {carros}")
                    rem = input("Elimina una marca de carros: ").lower()
                    if rem in carros:
                        carros.remove(rem)
                        print(f"Carros restantes: {carros}")
                    else:
                        print("Esa marca no existe en la lista")
                print("=" * 50)

            elif opc == 3:
                print("\nLista de marcas ingresadas:")
                if carros:
                    print(carros)
                else:
                    print("No hay carros ingresados")
                print("=" * 50)

            elif opc == 4:
                print("\nSaliendo del menú de carros...")
                break

            else:
                print("\nOpción inválida")
                print("=" * 50)

        except ValueError:
            print("\nPor favor ingresa un número válido")
            print("=" * 50)


def menu_principal():
    """Menú principal con todos los ejercicios"""
    while True:
        print("\n" + "=" * 50)
        print("        MENÚ PRINCIPAL DE EJERCICIOS")
        print("=" * 50)
        print("1. Validador de números (positivo/negativo/cero)")
        print("2. Imprimir <3 Medellín (números 4-15)")
        print("3. Lista de frutas")
        print("4. Lista de animales con slicing")
        print("5. Números pares de 0 a 50")
        print("6. Pares e impares de -2 a 99")
        print("7. Múltiplos de 3 (clasificar par/impar)")
        print("8. Gestión de carros (CRUD)")
        print("9. Salir del programa")
        print("=" * 50)

        try:
            opcion = int(input("Selecciona un ejercicio (1-9): "))

            if opcion == 1:
                ejercicio1()
            elif opcion == 2:
                ejercicio2()
            elif opcion == 3:
                ejercicio3()
            elif opcion == 4:
                ejercicio4()
            elif opcion == 5:
                ejercicio5()
            elif opcion == 6:
                ejercicio6()
            elif opcion == 7:
                ejercicio7()
            elif opcion == 8:
                ejercicio8()
            elif opcion == 9:
                print("\n¡Hasta luego! 👋")
                break
            else:
                print("\n❌ Opción inválida. Por favor selecciona entre 1 y 9.")

        except ValueError:
            print("\n❌ Por favor ingresa un número válido.")

        input("\nPresiona Enter para continuar...")


# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()