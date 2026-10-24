class Product () :
    total_no_of_products = 0
    
    def __init__ (self, detail: list) :
        self.name = detail[0]
        self.price = detail[1]
        self.category = detail[2]
        
        self.increase_no_products()
    
    
    @classmethod 
    def increase_no_products (cls) :
        cls.total_no_of_products += 1
    
    
    def apply_discount (self, dis_rate) :
        self.price = self.price * (1 - dis_rate/100)
    
    def __str__ (self) :
        print(f"name = {self.name}")
        print(f"price = {self.price}")
        print(f"category = {self.category}")
        
        return "\n"


def main () -> None :
    #raise ValueError('main not implemented')
    products: list[Product] = [
        Product(['washing powder', 200, 'laundry']),
        Product(['charger', 100, 'electronics']),
        Product(['samasung S10 tab', 110000, 'electronics']),
        Product(['air jordons', 20000, 'shoes']),
        ]
    
    dis_rate = int(input('Enter the discount rate: '))
    for product in products :
        product.apply_discount(dis_rate)
    
    print("\nPrinting products... \n")
    for product in products :
        print(product)

    return

if __name__ == "__main__" :
    main()