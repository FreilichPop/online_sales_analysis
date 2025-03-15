from product import Product
from product_manager import ProductManager

if __name__ == "__main__":
    manager = ProductManager()

    product1 = Product("Laptop", 1000, 15)
    product2 = Product("Phone", 500, 20)
    product3 = Product("Tablet", 300, 10)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)