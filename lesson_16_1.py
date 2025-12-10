class Goods:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Goods [name = {self.name}, price = {self.price}]"

class BasketIterator:
    """ Клас ітератор, який знає як обробляти наповнення Кошика,
    щоб віддавати по одному елементу при кожному запиті
    """

    def __init__(self, goods_list):
        """При ініціалізації отримує список товарів
        і встановлює значення індексу 0"""
        self.goods_list = goods_list
        self.index = 0

    def __next__(self):
        """ Якщо значення індексу не виходить за межі розміру
        списку, надаємо елемент Кошика.
        В іншому випадку - викликаємо виняток"""
        if self.index < len(self.goods_list):
            res = self.goods_list[self.index]
            self.index = self.index + 1
            return res
        else:
            raise StopIteration

    def __iter__(self):
        return self


class Basket:
    def __init__(self, user):
        self.user = user
        self.goods_list = list()

    def add_good(self, good):
        self.goods_list.append(good)

    def __str__(self):
        result = f"User: {self.user}\n"
        for good in self.goods_list:
            result += str(good) + "\n"
        return result

    def __iter__(self):
        """Повертаємо екземпляр класу Ітератора"""
        return BasketIterator(self.goods_list)


basket = Basket("Alexander_Ts")

a = Goods("Apple", 35)
b = Goods("Milk", 50)

basket.add_good(a)
basket.add_good(b)

# Пройдемося циклом по елементах кошика
for good in basket:
    print(good)
# Додамо ще одну позицію товару до кошику
c = Goods("Oil", 100)
basket.add_good(c)

# І знову пройдемося циклом по елементах кошика
for good in basket:
    print(good)