def add(produto, preço, iva):
    return {
        'product': produto,
        'price': preço,
        'tax': iva
    }

def update_final_price(dicionario):
    dicionario["final_price"] = round(dicionario ["price"] * (1+ dicionario["tax"]),2)

def print_products(p):
    print(f"{p["product"]}; Preço: {p["price"]};", sep="\n")
    print(f"Iva: {p["tax"]*100}%, Preço final: {p["final_price"]}")