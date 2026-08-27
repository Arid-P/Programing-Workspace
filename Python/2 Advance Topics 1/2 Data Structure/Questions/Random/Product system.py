from collections import namedtuple
# gpt 
def get_discounted_products(products: list, discount_percentage: int) -> dict:
    """
    Filters products with prices greater than 100 and applies a discount.
    Returns a dictionary with product names as keys and their discounted prices as values.
    """
    # Filter products with price greater than 100
    products_more_than_100 = filter(lambda product: product.price > 100, products)
    
    # Apply the discount percentage on the price
    discounted_product = {
        product.name: round(product.price * (1 - discount_percentage / 100), 2)
        for product in products_more_than_100
    }
    
    return discounted_product

def main() -> None:
    """
    Main function to define products and calculate discounted prices.
    """
    # Define the namedtuple
    Product = namedtuple('Product', ['name', 'category', 'price', 'quantity'])
    
    # Create a list of products
    products: list[Product] = [
        Product(name="Laptop", category="Electronics", price=1200, quantity=10),
        Product(name="Shampoo", category="Personal Care", price=5, quantity=50),
        Product(name="Smartphone", category="Electronics", price=800, quantity=20),
        Product(name="Socks", category="Clothing", price=10, quantity=100),
        Product(name="Washing Machine", category="Appliances", price=500, quantity=15),
        Product(name="Headphones", category="Electronics", price=200, quantity=30),
        Product(name="T-shirt", category="Clothing", price=15, quantity=200),
        Product(name="Refrigerator", category="Appliances", price=700, quantity=25)
    ]
    
    # Discount percentage
    discount_percentage: int = 10
    
    # Get discounted products and print the result
    discounted_products = get_discounted_products(products, discount_percentage)
    print("Discounted Products:")
    for name, price in discounted_products.items():
        print(f"{name}: ${price}")

if __name__ == "__main__":
    main()

"""
Mine 

def get_discounted_products(products: list, discount_percentage: int) -> dict:
    
    Filters products with prices greater than 100 and prints them.
    
    # Filter products with price greater than 100
    products_more_than_100 = list(filter(lambda product: product.price > 100, products))
    
    #Applys the discount_percentage on the price
    discounted_product = {}
    for product in products_more_than_100:
        dis_price = product.price - (discount_percentage / 100 * product.price)
        discounted_product[product.name] = dis_price
    
    return discounted_product



def main() -> None:
    # Define the namedtuple
    Product = namedtuple('Product', ['name', 'category', 'price', 'quantity'])
    
    # Create a list of products
    products: list[Product] = [
        Product(name="Laptop", category="Electronics", price=1200, quantity=10),
        Product(name="Shampoo", category="Personal Care", price=5, quantity=50),
        Product(name="Smartphone", category="Electronics", price=800, quantity=20),
        Product(name="Socks", category="Clothing", price=10, quantity=100),
        Product(name="Washing Machine", category="Appliances", price=500, quantity=15),
        Product(name="Headphones", category="Electronics", price=200, quantity=30),
        Product(name="T-shirt", category="Clothing", price=15, quantity=200),
        Product(name="Refrigerator", category="Appliances", price=700, quantity=25)
    ]
    
    # Discount percentage
    discount_percentage: int = 10
    print(get_discounted_products(products, discount_percentage))

if __name__ == "__main__":
    main()

"""