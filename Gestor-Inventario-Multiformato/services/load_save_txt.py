from models.product import Product
import os

FILE = "data/inventory.txt"

def save_txt(products):
    with open(FILE, "w", encoding="utf-8") as f:
        for p in products:
            f.write(f"{p.id}|{p.name}|{p.quantity}|{p.price}|{p.description}\n")

def load_txt():
    if not os.path.exists(FILE):
        return []
    res = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            d=line.strip().split("|")
            res.append(Product(int(d[0]),d[1],int(d[2]),float(d[3]),d[4]))
    return res