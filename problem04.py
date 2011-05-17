__author__ = 'tfleischer'

def run():
    products = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            product_string = str(product)
            if product_string == product_string[::-1]:
                products.append(product)
    print max(products)