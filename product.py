class Product:

    def __init__(self, exDate, Quant):
        self.exDate = exDate
        self.Quant = Quant

class Food(Product):
    pass

class Dish(Food):
    pass

class Pizza(Dish):
    pass

class Cheese(Pizza):
    pass

class Peperoni(Pizza):
    pass

class Pineapple(Pizza):
    pass

class Calzone(Pizza):
    pass

class Side(Food):
    pass

class GarlicBread(Side):
    pass

class Salad(Side):
    pass

class House(Salad):
    pass

class Caesar(salad):
    pass

import datetime
class Product:

    def __init__(self, exDate, Quant):
        self.exDate = exDate
        self.Quant = Quant

class Drink(Product):
    def __init__(self, exDate, Quant):
        super().__init__(exDate,Quant)
        self.type = "Drink"

x = Drink(str(datetime.datetime.today()), 1987)
print(x.exDate)
