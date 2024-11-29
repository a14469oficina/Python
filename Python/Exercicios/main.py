import produtos.products as p
products = []

products.append(p.add("ak-47",270,0.10))
products.append(p.add("ak-47",270,0.10))
products.append(p.add("ak-47",270,0.10))


for product in products:
    p.update_final_price(product)
    p.print_products(product)

print(*products,sep="\n")


    
