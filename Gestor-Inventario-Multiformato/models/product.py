class Product:
    def __init__(self, pid, name, quantity, price, desc):
        self.id = pid
        self.name = name
        self.quantity = quantity
        self.price = price
        self.description = desc

    def to_dict(self):
        return vars(self)