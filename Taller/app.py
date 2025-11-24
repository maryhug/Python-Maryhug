from CRUD import CRUD

crud = CRUD()
archivo = "datos.json"

crud.crear_archivo(archivo)

while True:
    print("\n--- MENU ---")
    print("1. Crear persona")
    print("2. Listar personas")
    print("3. Modificar persona")
    print("4. Eliminar persona")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        edad = input("Edad: ")

        datos = (nombre, edad)

        id_creado = crud.crear(archivo, datos)
        print(f"Persona creada con ID: {id_creado}")

    elif opcion == "2":
        datos = crud.listar(archivo)
        print("\n--- LISTADO ---")
        if not datos:
            print("No hay registros.")
        else:
            for fila in datos:
                if isinstance(fila, dict):
                    id_ = fila.get("id", "")
                    nombre = fila.get("nombre", "")
                    edad = fila.get("edad", "")
                else:
                    id_ = fila[0] if len(fila) > 0 else ""
                    nombre = fila[1] if len(fila) > 1 else ""
                    edad = fila[2] if len(fila) > 2 else ""
                print(f"ID: {id_} | Nombre: {nombre} | Edad: {edad}")

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción no válida")
