# python
import csv, os
from models.product import Product

FILE = "data/inventory.csv"

def save_csv(products):
    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id","name","quantity","price","description"])
        for p in products:
            w.writerow([p.id, p.name, p.quantity, p.price, p.description])

def load_csv():
    if not os.path.exists(FILE):
        return []
    res = []
    with open(FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i, r in enumerate(reader):
            if i == 0:
                continue
            try:
                res.append(Product(int(r[0]), r[1], int(r[2]), float(r[3]), r[4]))
            except (IndexError, ValueError):
                continue
    return res
