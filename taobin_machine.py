from menu_drink import MenuDrink
from manage_ingredient import IngredientManagement

stock = IngredientManagement()


class TaobinMachine:
    def __init__(self):
        self.menu = [
            MenuDrink(name='latte', water=200, milk=150, coffee=24, cost=35),
            MenuDrink(name='espresso', water=50, coffee=18, cost=25),
            MenuDrink(name='cappuccino', water=250, milk=100, coffee=24, cost=40),
            MenuDrink(name='black coffee', water=200, milk=100, cost=30),
            MenuDrink(name='cocoa milk',  milk=150, cocoa=24, cost=35),
            MenuDrink(name='dark cocoa', water=200, cocoa=30, cost=35),
            MenuDrink(name='black tea', water=200, milk=150, tea=24, cost=35),
            MenuDrink(name='milk tea', milk=100, tea=30, cost=35)
          ]
        self.price = 0
        self.sales = 0
        self.total = []

    def shutting_down_maintenance(self):
        print("Shutting down for maintenance !!!")

    def order_drink(self):
        while True:
            get_drink = input("""============================================\nWhat would you like to drink please?[or quit]: """)
            if get_drink == "quit":
                break

            for menu in self.menu:
             if get_drink == menu.name:
                try:
                 stock._remaining_water_ml -= menu.water
                 stock._remaining_milk_ml -= menu.milk
                 stock._remaining_coffee_g -= menu.coffee
                 stock._remaining_cocoa_g -= menu.cocoa
                 stock._remaining_tea_g -= menu.tea
                 print(f"Your order is {menu.name}. Price of your drink = {menu.cost} ฿")
                 self.price += menu.cost
                 self.sales += 1
                 self.total.append(menu)
                except ValueError:
                    print("--- ingredients stock is not enough !!! ---")
