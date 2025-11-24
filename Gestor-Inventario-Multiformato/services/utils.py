def input_int(msg, default=None):
    val = input(msg).strip()
    return int(val) if val else default

def input_float(msg, default=None):
    val = input(msg).strip()
    return float(val) if val else default

def generate_id(products):
    ids = [p.id for p in products]
    return max(ids)+1 if ids else 1