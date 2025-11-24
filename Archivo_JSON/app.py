from funciones import guardar_json

nombre = "info.json"
data = {
    "Curso": "Python",
        "Nivel": "Intermedio",
        "Nombre": "Maryhug",
        "Apellido": "Duran",
        "Edad": "19",
        "Grado": "Universidad"
        }

print(guardar_json(nombre))