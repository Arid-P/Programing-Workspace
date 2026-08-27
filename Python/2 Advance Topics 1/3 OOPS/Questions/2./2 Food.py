class Restaurant():
    type: None | str = None

    def welcoming_customer(self, name):
        print(f'Thanks {name} for choosing this Restaurant')
        print(f'And Welcome here {name}')

    def print_menu(self):
        print('It has various dishes')


class FastFood(Restaurant):
    _type = "Fast Food"
    total_no_of_orders = 0

    def __init__(self, name):
        self.name = name
        self.no_of_orders = 0
        super().welcoming_customer(self.name)

    def print_menu(self):
        print('We have burger, pizza, tacos, french fries, oreo shake')

    def take_order(self):
        self.dish = input('What would you like? ')
        print(f'Thanks for choosing {self.dish}. Kindly wait a few minutes')

        self.no_of_orders += 1
        self.increase_total_orders()

    @classmethod
    def increase_total_orders(cls):
        cls.total_no_of_orders += 1
        print(cls.total_no_of_orders)

    @classmethod
    def print_total_orders(cls):
        print(f'Total orders in Fast Food is {cls.total_no_of_orders}')


class FineDining(Restaurant):
    _type = "Fine Dining"
    total_no_of_orders = 0

    def __init__(self, name):
        self.name = name
        self.no_of_orders = 0
        super().welcoming_customer(self.name)

    def print_menu(self):
        print('It has pasta, butter chicken, butter paneer, mutton chap')

    def take_order(self):
        self.dish = input('What would you like? ')
        print(f'Thanks for choosing {self.dish}. Kindly wait a few minutes')

        self.no_of_orders += 1
        self.increase_total_orders()

    @classmethod
    def increase_total_orders(cls):
        cls.total_no_of_orders += 1

    @classmethod
    def print_total_orders(cls):
        print(f'Total orders in Fine Dining is {cls.total_no_of_orders}')


def main() -> None:
    rahul = FineDining('Rahul')
    rahul.print_menu()
    rahul.take_order()

    jayesh = FastFood('Jayesh')
    jayesh.print_menu()
    jayesh.take_order()

    rahul.print_total_orders()
    jayesh.print_total_orders()

    return


if __name__ == "__main__":
    main()