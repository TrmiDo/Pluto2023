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

class Food(Product):
    
        def __init__(self, exDate, Quant):
        super().__init__(exDate,Quant)
        self.type = "Food"

x = Food(str(datetime.datetime.today()), 2023)
print(x.exDate)

class Dish(Food):
      
        def __init__(self, exDate, Quant):
        super().__init__(exDate,Quant)
        self.type = "Dish"

x = Dish(str(datetime.datetime.today()), 2023)
print(x.exDate)

class Pizza(Dish):
          
        def __init__(self, exDate, Quant):
        super().__init__(exDate,Quant)
        self.type = "Pizza"

x = Pizza(str(datetime.datetime.today()), 2023)
print(x.exDate)

class Cheese(Pizza):
        
    def __init__(self, exDate, Quant):
        super().__init__(exDate,Quant)
        self.type = "Cheese"

x = Cheese(str(datetime.datetime.today()), 1987)
print(x.exDate)

class Pepperoni(Pizza):
        
    def __init__(self, exDate, Quant):
        super().__init__(exDate,Quant)
        self.type = "Pepperoni"

x = Pepperoni(str(datetime.datetime.today()), 1987)
print(x.exDate)

class Pineapple(Pizza):
        
    def __init__(self, exDate, Quant):
        super().__init__(exDate,Quant)
        self.type = "Pineapple"

x = Pineapple(str(datetime.datetime.today()), 1987)
print(x.exDate)

class Calzone(Pizza):
        
    def __init__(self, exDate, Quant):
        super().__init__(exDate,Quant)
        self.type = "Calzone"

x = Calzone(str(datetime.datetime.today()), 1987)
print(x.exDate)

class Side(Food):
        
    def __init__(self, exDate, Quant):
        super().__init__(exDate,Quant)
        self.type = "Side"

x = Side(str(datetime.datetime.today()), 1987)
print(x.exDate)

class GarlicBread(Side):
        
    def __init__(self, exDate, Quant):
        super().__init__(exDate,Quant)
        self.type = "GarlicBread"

x = GarlicBread(str(datetime.datetime.today()), 1987)
print(x.exDate)

class Salad(Side):
        
    def __init__(self, exDate, Quant):
        super().__init__(exDate,Quant)
        self.type = "Salad"

x = Salad(str(datetime.datetime.today()), 1987)
print(x.exDate)

class House(Salad):
        
    def __init__(self, exDate, Quant):
        super().__init__(exDate,Quant)
        self.type = "House"

x = House(str(datetime.datetime.today()), 1987)
print(x.exDate)

class Caesar(salad):
        
    def __init__(self, exDate, Quant):
        super().__init__(exDate,Quant)
        self.type = "Caesar"

x = Caesar(str(datetime.datetime.today()), 1987)
print(x.exDate)


