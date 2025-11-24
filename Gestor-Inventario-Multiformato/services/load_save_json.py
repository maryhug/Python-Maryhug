# python
import json, os
from models.product import Product

FILE = "data/inventory.json"

def save_json(products):
    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump([p.__dict__ for p in products], f, ensure_ascii=False, indent=2)

def load_json():
    if not os.path.exists(FILE):
        return []
    res = []
    with open(FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []
        for item in data:
            # renombrar clave 'id' a 'pid' si viene desde CSV/JSON externo
            if "id" in item and "pid" not in item:
                item["pid"] = item.pop("id")
            try:
                res.append(Product(**item))
            except (TypeError, ValueError):
                # omitir entradas inválidas
                continue
    return res
