# Sistema de Gestión de Estudiantes con Materias y Notas

# Inicializar lista vacía para almacenar estudiantes
estudiantes = []


# Función para validar entrada numérica
def solicitar_numero(mensaje, tipo="int", minimo=None, maximo=None):
    """
    Solicita un número al usuario con validaciones
    tipo: 'int' o 'float'
    minimo: valor mínimo permitido
    maximo: valor máximo permitido
    """
    while True:
        try:
            if tipo == "int":
                valor = int(input(mensaje))
            else:
                valor = float(input(mensaje))

            # Validar rango si se especifica
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}")
                continue

            return valor
        except ValueError:
            print(f"Entrada inválida. Debe ingresar un número {'entero' if tipo == 'int' else 'decimal'}.")


# Función para buscar estudiante por nombre
def buscar_estudiante(nombre):
    """Busca un estudiante en la lista por nombre (no sensible a mayúsculas)"""
    for estudiante in estudiantes:
        if estudiante['nombre'].lower() == nombre.lower():
            return estudiante
    return None


# Función para calcular promedio de un estudiante
def calcular_promedio(materias):
    """Calcula el promedio de las notas de todas las materias"""
    if not materias:
        return 0.0

    suma_notas = 0
    for materia in materias:
        suma_notas += materia['nota']

    return suma_notas / len(materias)


# Función para determinar estado del estudiante
def determinar_estado(promedio):
    """Determina si el estudiante aprobó o reprobó según su promedio"""
    if promedio >= 3.0:
        return "APROBADO"
    else:
        return "REPROBADO"


# Ciclo principal del programa
while True:
    # Mostrar menú principal
    print("\n" + "=" * 50)
    print("     SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("=" * 50)
    print("1. Registrar nuevo estudiante")
    print("2. Agregar materias y notas a un estudiante")
    print("3. Ver información de un estudiante")
    print("4. Ver listado completo de estudiantes")
    print("5. Ver estadísticas generales")
    print("6. Modificar nota de una materia")
    print("7. Eliminar estudiante")
    print("8. Salir")
    print("=" * 50)

    # Solicitar opción del menú con validación
    opcion = solicitar_numero("Seleccione una opción (1-8): ", "int", 1, 8)

    # OPCIÓN 1: Registrar nuevo estudiante
    if opcion == 1:
        print("\n--- REGISTRAR NUEVO ESTUDIANTE ---")

        # Solicitar nombre del estudiante
        nombre = input("Ingrese el nombre completo del estudiante: ").strip()

        # Validar que el nombre no esté vacío
        while not nombre:
            print("El nombre no puede estar vacío.")
            nombre = input("Ingrese el nombre completo del estudiante: ").strip()

        # Verificar si el estudiante ya existe
        if buscar_estudiante(nombre):
            print(f"\n⚠️  El estudiante '{nombre}' ya está registrado.")
            continue

        # Solicitar edad con validación
        edad = solicitar_numero("Ingrese la edad del estudiante: ", "int", 5, 100)

        # Solicitar ID/código del estudiante
        codigo = input("Ingrese el código o ID del estudiante: ").strip()
        while not codigo:
            print("El código no puede estar vacío.")
            codigo = input("Ingrese el código o ID del estudiante: ").strip()

        # Crear diccionario del estudiante con lista vacía de materias
        nuevo_estudiante = {
            "nombre": nombre,
            "edad": edad,
            "codigo": codigo,
            "materias": []  # Lista vacía para almacenar materias
        }

        # Agregar estudiante a la lista
        estudiantes.append(nuevo_estudiante)
        print(f"\n✅ Estudiante '{nombre}' registrado exitosamente!")

    # OPCIÓN 2: Agregar materias y notas
    elif opcion == 2:
        # Verificar que haya estudiantes registrados
        if not estudiantes:
            print("\n⚠️  No hay estudiantes registrados. Registre uno primero.")
            continue

        print("\n--- AGREGAR MATERIAS Y NOTAS ---")

        # Solicitar nombre del estudiante
        nombre_buscar = input("Ingrese el nombre del estudiante: ").strip()

        # Buscar estudiante
        estudiante_encontrado = buscar_estudiante(nombre_buscar)

        if not estudiante_encontrado:
            print(f"\n❌ El estudiante '{nombre_buscar}' no existe.")
            continue

        # Solicitar cantidad de materias a agregar
        num_materias = solicitar_numero("¿Cuántas materias desea agregar? ", "int", 1, 20)

        # Ciclo para ingresar cada materia
        for i in range(num_materias):
            print(f"\n--- Materia #{i + 1} ---")

            # Solicitar nombre de la materia
            nombre_materia = input("Nombre de la materia: ").strip()
            while not nombre_materia:
                print("El nombre de la materia no puede estar vacío.")
                nombre_materia = input("Nombre de la materia: ").strip()

            # Solicitar nota (0.0 a 5.0)
            nota = solicitar_numero("Ingrese la nota (0.0 - 5.0): ", "float", 0.0, 5.0)

            # Solicitar créditos de la materia
            creditos = solicitar_numero("Ingrese los créditos de la materia: ", "int", 1, 10)

            # Crear diccionario de la materia
            materia = {
                "nombre": nombre_materia,
                "nota": nota,
                "creditos": creditos
            }

            # Agregar materia a la lista de materias del estudiante
            estudiante_encontrado['materias'].append(materia)

        print(f"\n✅ {num_materias} materia(s) agregada(s) exitosamente a '{estudiante_encontrado['nombre']}'!")

    # OPCIÓN 3: Ver información de un estudiante
    elif opcion == 3:
        # Verificar que haya estudiantes registrados
        if not estudiantes:
            print("\n⚠️  No hay estudiantes registrados.")
            continue

        print("\n--- INFORMACIÓN DEL ESTUDIANTE ---")

        # Solicitar nombre del estudiante
        nombre_buscar = input("Ingrese el nombre del estudiante: ").strip()

        # Buscar estudiante
        estudiante_encontrado = buscar_estudiante(nombre_buscar)

        if not estudiante_encontrado:
            print(f"\n❌ El estudiante '{nombre_buscar}' no existe.")
            continue

        # Mostrar información del estudiante
        print(f"\n{'=' * 50}")
        print(f"Nombre: {estudiante_encontrado['nombre']}")
        print(f"Edad: {estudiante_encontrado['edad']} años")
        print(f"Código: {estudiante_encontrado['codigo']}")
        print(f"{'=' * 50}")

        # Verificar si tiene materias registradas
        if not estudiante_encontrado['materias']:
            print("⚠️  Este estudiante no tiene materias registradas.")
        else:
            print(f"\nMaterias registradas ({len(estudiante_encontrado['materias'])}):")
            print("-" * 50)

            # Recorrer y mostrar cada materia
            for idx, materia in enumerate(estudiante_encontrado['materias'], 1):
                print(f"{idx}. {materia['nombre']}")
                print(f"   Nota: {materia['nota']:.2f}")
                print(f"   Créditos: {materia['creditos']}")
                print("-" * 50)

            # Calcular y mostrar promedio
            promedio = calcular_promedio(estudiante_encontrado['materias'])
            estado = determinar_estado(promedio)

            print(f"\n📊 PROMEDIO GENERAL: {promedio:.2f}")
            print(f"📋 ESTADO: {estado}")

    # OPCIÓN 4: Ver listado completo
    elif opcion == 4:
        # Verificar que haya estudiantes registrados
        if not estudiantes:
            print("\n⚠️  No hay estudiantes registrados.")
            continue

        print("\n" + "=" * 50)
        print(f"     LISTADO COMPLETO ({len(estudiantes)} estudiante(s))")
        print("=" * 50)

        # Recorrer todos los estudiantes
        for idx, estudiante in enumerate(estudiantes, 1):
            print(f"\n{idx}. {estudiante['nombre']} (Código: {estudiante['codigo']})")
            print(f"   Edad: {estudiante['edad']} años")
            print(f"   Materias registradas: {len(estudiante['materias'])}")

            # Si tiene materias, calcular promedio
            if estudiante['materias']:
                promedio = calcular_promedio(estudiante['materias'])
                estado = determinar_estado(promedio)
                print(f"   Promedio: {promedio:.2f} - {estado}")
            else:
                print(f"   Promedio: Sin materias")
            print("-" * 50)

    # OPCIÓN 5: Ver estadísticas generales
    elif opcion == 5:
        # Verificar que haya estudiantes registrados
        if not estudiantes:
            print("\n⚠️  No hay estudiantes registrados.")
            continue

        print("\n" + "=" * 50)
        print("     ESTADÍSTICAS GENERALES")
        print("=" * 50)

        # Contadores
        total_estudiantes = len(estudiantes)
        estudiantes_con_materias = 0
        estudiantes_aprobados = 0
        estudiantes_reprobados = 0
        suma_promedios = 0

        # Recorrer estudiantes para calcular estadísticas
        for estudiante in estudiantes:
            if estudiante['materias']:
                estudiantes_con_materias += 1
                promedio = calcular_promedio(estudiante['materias'])
                suma_promedios += promedio

                if promedio >= 3.0:
                    estudiantes_aprobados += 1
                else:
                    estudiantes_reprobados += 1

        # Mostrar estadísticas
        print(f"Total de estudiantes registrados: {total_estudiantes}")
        print(f"Estudiantes con materias: {estudiantes_con_materias}")
        print(f"Estudiantes sin materias: {total_estudiantes - estudiantes_con_materias}")

        if estudiantes_con_materias > 0:
            promedio_general = suma_promedios / estudiantes_con_materias
            print(f"\nPromedio general del curso: {promedio_general:.2f}")
            print(f"Estudiantes aprobados: {estudiantes_aprobados}")
            print(f"Estudiantes reprobados: {estudiantes_reprobados}")

            # Calcular porcentajes
            porcentaje_aprobados = (estudiantes_aprobados / estudiantes_con_materias) * 100
            porcentaje_reprobados = (estudiantes_reprobados / estudiantes_con_materias) * 100

            print(f"\nTasa de aprobación: {porcentaje_aprobados:.1f}%")
            print(f"Tasa de reprobación: {porcentaje_reprobados:.1f}%")

        print("=" * 50)

    # OPCIÓN 6: Modificar nota de una materia
    elif opcion == 6:
        # Verificar que haya estudiantes registrados
        if not estudiantes:
            print("\n⚠️  No hay estudiantes registrados.")
            continue

        print("\n--- MODIFICAR NOTA ---")

        # Solicitar nombre del estudiante
        nombre_buscar = input("Ingrese el nombre del estudiante: ").strip()

        # Buscar estudiante
        estudiante_encontrado = buscar_estudiante(nombre_buscar)

        if not estudiante_encontrado:
            print(f"\n❌ El estudiante '{nombre_buscar}' no existe.")
            continue

        # Verificar si tiene materias
        if not estudiante_encontrado['materias']:
            print("\n⚠️  Este estudiante no tiene materias registradas.")
            continue

        # Mostrar materias disponibles
        print("\nMaterias disponibles:")
        for idx, materia in enumerate(estudiante_encontrado['materias'], 1):
            print(f"{idx}. {materia['nombre']} - Nota actual: {materia['nota']:.2f}")

        # Solicitar número de materia a modificar
        num_materia = solicitar_numero(f"Seleccione la materia (1-{len(estudiante_encontrado['materias'])}): ",
                                       "int", 1, len(estudiante_encontrado['materias']))

        # Solicitar nueva nota
        nueva_nota = solicitar_numero("Ingrese la nueva nota (0.0 - 5.0): ", "float", 0.0, 5.0)

        # Modificar la nota
        materia_modificar = estudiante_encontrado['materias'][num_materia - 1]
        nota_anterior = materia_modificar['nota']
        materia_modificar['nota'] = nueva_nota

        print(f"\n✅ Nota modificada exitosamente!")
        print(f"   Materia: {materia_modificar['nombre']}")
        print(f"   Nota anterior: {nota_anterior:.2f}")
        print(f"   Nota nueva: {nueva_nota:.2f}")

    # OPCIÓN 7: Eliminar estudiante
    elif opcion == 7:
        # Verificar que haya estudiantes registrados
        if not estudiantes:
            print("\n⚠️  No hay estudiantes registrados.")
            continue

        print("\n--- ELIMINAR ESTUDIANTE ---")

        # Solicitar nombre del estudiante
        nombre_buscar = input("Ingrese el nombre del estudiante a eliminar: ").strip()

        # Buscar estudiante
        estudiante_encontrado = buscar_estudiante(nombre_buscar)

        if not estudiante_encontrado:
            print(f"\n❌ El estudiante '{nombre_buscar}' no existe.")
            continue

        # Confirmar eliminación
        confirmacion = input(f"¿Está seguro de eliminar a '{estudiante_encontrado['nombre']}'? (S/N): ").strip().lower()

        if confirmacion == 's':
            # Eliminar estudiante de la lista
            estudiantes.remove(estudiante_encontrado)
            print(f"\n✅ Estudiante '{nombre_buscar}' eliminado exitosamente.")
        else:
            print("\n❌ Eliminación cancelada.")

    # OPCIÓN 8: Salir
    elif opcion == 8:
        print("\n" + "=" * 50)
        print("     Gracias por usar el sistema")
        print("     ¡Hasta luego!")
        print("=" * 50)
        break