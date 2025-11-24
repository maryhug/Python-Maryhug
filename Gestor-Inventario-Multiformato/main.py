from services.product_crud import *
from services.load_save_json import *
from services.load_save_txt import *
from services.load_save_csv import *

def load_any():
    for f in (load_json, load_csv, load_txt):
        data = f()
        if data: return data
    return []

def main_print():
    print("\nMenu de opciones --")
    print("1. Listar productos")
    print("2. Crear producto")
    print("3. Editar producto")
    print("4. Eliminar producto")
    print("5. Guardar producto "
          "\n   en los 3 tipos de formato")
    print("0. Salir")

def main():
    products = load_any()
    while True:
        main_print()
        op = input("Opción: ")
        print()
        if op=="1":
            list_products(products)
        elif op=="2":
            create_product(products)
        elif op=="3":
            edit_product(products)
        elif op=="4":
            delete_product(products)
        elif op=="5":
            save_json(products);
            save_csv(products);
            save_txt(products)
        elif op=="0": break


if __name__=="__main__":
    main()