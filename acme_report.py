from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []

    for i in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        products.append(Product(name=name, price=price, weight=weight, flammability=flammability))

    return products

def inventory_report(products):
    print('ACME CORP OFFICIAL INVENTORY REPORT')

    total_price = 0
    total_weight = 0
    total_flamm = 0

    for product in products:
        total_price = total_price + product.price
        total_weight = total_weight + product.weight
        total_flamm = total_flamm + product.flammability

    print('Unique product names:',len(products))
    print('Average price:',total_price/len(products))
    print ('Average weight:',total_weight/len(products))
    print ('Average flammability:',total_flamm/len(products))

    pass

if __name__ == '__main__':
    inventory_report(generate_products(19))