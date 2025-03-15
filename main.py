from product import Product
from product_manager import ProductManager
from cart import Cart

if __name__ == "__main__":
    manager = ProductManager()

    product1 = Product("Laptop", 1000, 5)
    product2 = Product("Phone", 500, 10)
    product3 = Product("Tablet", 300, 7)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    print("All Products: ")
    manager.display_products()
    print(f"Total Inventory Value: {manager.total_inventory_value()}")

    cart = Cart()
    cart.add_to_cart(product1)
    cart.add_to_cart(product2)
    cart.add_to_cart(product3)

    print("Cart Contents: ")
    cart.display_cart()
    print(f"Total Cart Value: {cart.total_cart_value()}")