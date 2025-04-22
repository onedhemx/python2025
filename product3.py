products = [("Хлеб", 40, 20), ("Молоко", 60, 15), ("Яблоки", 100, 50)]
for product in products:
    nazvan, tsena = product
    print(f"Товар: {nazvan}, Цена: {tsena}")
    
def vivesti_products(products):
    for product in products:
        if product[1] < 80:
            print(product[0])

vivesti_products(products)
