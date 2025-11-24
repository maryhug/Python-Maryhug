try:
    numero = int(input("Introduce un numero: "))
    print("El doble del numero es:", numero * 2)
except ValueError:
    print("Error: Debes ingresar un numero valido")
finally:
    print("Finalizando...")