import json

def guardar_json(nombre, data):
    with open(nombre, 'w') as archivo:
        json.dump(data, archivo, indent=5)
    return f"Guardado {nombre, data}"