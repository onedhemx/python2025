products = [("Хлеб", 40), ("Молоко", 60), ("Яблоки", 100)]
for product in products:
    nazvan, tsena = product
    print(f"Товар: {nazvan}, Цена: {tsena}")
    
def vivesti_products(products):
    for product in products:
        if product[1] < 80:
            print(product[0])

vivesti_products(products)
