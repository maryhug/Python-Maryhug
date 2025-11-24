import json
import os

class CRUD:

    def crear_archivo(self, archivo):
        if not os.path.exists(archivo):
            with open(archivo, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=2)
            return "Archivo creado"
        return "El archivo ya estaba creado"

    def obtener_nuevo_id(self, archivo):
        if not os.path.exists(archivo):
            return 1
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return 1

        if not isinstance(data, list) or not data:
            return 1

        ids = []
        for item in data:
            if isinstance(item, dict) and "id" in item:
                try:
                    ids.append(int(item["id"]))
                except (TypeError, ValueError):
                    pass
        return (max(ids) + 1) if ids else 1

    def crear(self, archivo, datos):
        id_nuevo = self.obtener_nuevo_id(archivo)

        # Normalizar entrada a nombre / edad
        if isinstance(datos, dict):
            nombre = datos.get("nombre", "") or datos.get("name", "")
            edad = datos.get("edad", "") or datos.get("age", "")
        elif isinstance(datos, (list, tuple)):
            nombre = datos[0] if len(datos) > 0 else ""
            edad = datos[1] if len(datos) > 1 else ""
        else:
            nombre = str(datos)
            edad = ""

        nuevo_registro = {"id": id_nuevo, "nombre": nombre, "edad": edad}

        # Leer lista existente
        data = []
        if os.path.exists(archivo):
            try:
                with open(archivo, "r", encoding="utf-8") as f:
                    loaded = json.load(f)
                    if isinstance(loaded, list):
                        data = loaded
            except (json.JSONDecodeError, FileNotFoundError):
                data = []

        # Añadir y guardar
        data.append(nuevo_registro)
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return id_nuevo

    def listar(self, archivo):
        if not os.path.exists(archivo):
            return []
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
        return data if isinstance(data, list) else []

def eliminar(self, archivo, id_):
    if not os.path.exists(archivo):
        return False
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return False

    if not isinstance(data, list):
        return False

    try:
        buscado = int(id_)
    except (TypeError, ValueError):
        return False

    for i, item in enumerate(data):
        if isinstance(item, dict):
            try:
                if int(item.get("id")) == buscado:
                    data.pop(i)
                    with open(archivo, "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    return True
            except (TypeError, ValueError):
                continue
    return False

def modificar(self, archivo, id_, nuevos_datos):
    if not os.path.exists(archivo):
        return False
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return False

    if not isinstance(data, list):
        return False

    try:
        buscado = int(id_)
    except (TypeError, ValueError):
        return False

    # Normalizar nuevos_datos a nombre/edad
    if isinstance(nuevos_datos, dict):
        nombre_nuevo = nuevos_datos.get("nombre", None) or nuevos_datos.get("name", None)
        edad_nueva = nuevos_datos.get("edad", None) or nuevos_datos.get("age", None)
    elif isinstance(nuevos_datos, (list, tuple)):
        nombre_nuevo = nuevos_datos[0] if len(nuevos_datos) > 0 else None
        edad_nueva = nuevos_datos[1] if len(nuevos_datos) > 1 else None
    else:
        nombre_nuevo = str(nuevos_datos)
        edad_nueva = None

    for i, item in enumerate(data):
        if isinstance(item, dict):
            try:
                if int(item.get("id")) == buscado:
                    # Actualizar solo si se proporcionó un valor no vacío
                    if nombre_nuevo is not None and nombre_nuevo != "":
                        item["nombre"] = nombre_nuevo
                    if edad_nueva is not None and edad_nueva != "":
                        item["edad"] = edad_nueva
                    data[i] = item
                    with open(archivo, "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    return True
            except (TypeError, ValueError):
                continue
    return False
