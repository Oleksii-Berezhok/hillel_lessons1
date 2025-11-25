class Item:

    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f'{self.name}, price: {self.price}'

class User:

    def __init__(self, name, surname, phone_number, date_of_birth):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f'{self.name} {self.surname}'

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        if item.name in self.products:
            old_cnt = self.products[item.name]
            self.total -= old_cnt * item.price
        self.products[item.name] = cnt
        self.total += cnt*item.price

    def __str__(self):
        return (f'"""' '\n'
                f'User: {self.user.name} {self.user.surname}' '\n'
                f'Items:' '\n'
                f'{'\n'.join(f"{k}: {v}" for k, v in self.products.items())}\n'
                f'"""')

    def get_total(self):
        return self.total

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
banana = Item('banana', 3, "yellow", "middle", )
cucumber = Item('cucumber', 1, "green", "middle", )
watermelon = Item('watermelon', 5, "green", "big", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162",1987)
buyer_2 = User("Piter", "Parker", "167775458",1960)
buyer_3 = User("Santa", "Claus", "13795773",1830)
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40