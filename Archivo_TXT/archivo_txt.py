filename = 'notas.txt'

def agregar_notas(notas, cantidad):
    for _ in range(cantidad):
        numero = int(input("Ingrese un número: "))
        notas.append(numero)
    return notas

def crear_archivo_txt(lista):
    with open(filename, 'w') as archivo:
        for n in lista:
            archivo.write(f"{n}\n")
    return f"Notas agregadas en {filename}"

def leer_archivo_txt():
    with open(filename, 'r') as archivo:
        return archivo.read()