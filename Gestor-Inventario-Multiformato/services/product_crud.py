from services.utils import *
from models.product import Product

def list_products(products):
    for p in products:
        print(vars(p))

def create_product(products):
    name = input("Nombre: ")
    qty = input_int("Cantidad: ", 0)
    price = input_float("Precio: ", 0.0)
    desc = input("Descripción: ")
    pid = generate_id(products)
    products.append(Product(pid, name, qty, price, desc))

def edit_product(products):
    pid = input_int("ID a editar: ")
    p = next((x for x in products if x.id == pid), None)
    if not p:
        return
    name = input(f"Nombre [{p.name}]: ") or p.name
    p.name = name

def delete_product(products):
    pid = input_int("ID a eliminar: ")
    products[:] = [p for p in products if p.id != pid]
