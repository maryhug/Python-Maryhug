datos = []

for i in range(5):
    nombre = input("Ingrese nombre: ")
    datos.append(nombre)

with open("nombre.txt","w") as archivo:
    for nombre in datos:
        archivo.write(nombre + "\n")

with open("nombre.txt","r") as archivo:
    contenido = archivo.read()
    print(contenido)

## Leer linea a linea
with open ("nombre.txt","r") as archivo:
    for linea in archivo:
        print(f"Linea: " + linea.strip())