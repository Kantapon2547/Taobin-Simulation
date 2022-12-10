class MenuDrink:
    def __init__(self, name, water=0, milk=0, coffee=0, cocoa=0, tea=0, cost=0):
     self.menu = ['latte', 'espresso', 'cappuccino', 'black coffee', 'black tea',
                  'milk tea', 'dark cocoa', 'cocoa milk']
     self.name = name
     self.water = water
     self.milk = milk
     self.coffee = coffee
     self.cocoa = cocoa
     self.tea = tea
     self.cost = cost

    def coffee_menu(self):
       latte = {'water': 100, 'milk': 100, 'coffee': 24}
       espresso = {'water': 50, 'coffee': 18, 'cost': 25}
       cappuccino = {'water': 150, 'milk': 100, 'coffee': 24, 'cost': 40}
       black_coffee = {'water': 100, 'coffee': 30, 'cost': 30}

    def cocoa_menu(self):
       cocoa_milk = {'milk': 100, 'cocoa': 30, 'cost': 35}
       dark_cocoa = {'water': 100, 'cocoa': 30, 'cost': 35}

    def tea_menu(self):
        black_tea = {'water': 100, 'milk': 100, 'tea': 24, 'cost': 30}
        milk_tea = {'milk': 100, 'tea': 30, 'cost': 35}
