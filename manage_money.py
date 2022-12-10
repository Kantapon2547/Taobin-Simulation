class MoneyManagement:
    def __init__(self, money):
        self.money = money
        self.money_count = {'baht': 0}

    def add_baht(self, amount, baht):
        if isinstance(amount, int) and amount >= 0 and isinstance(baht, str):
            self.money_count[baht] += amount
        else:
            print(f"amount of {baht} has to be greater than 0")
            raise ValueError(f"amount of baht has to be greater than 0 !!!")

    @property
    def _money(self):
     return round(self.__money, 2)

    @_money.setter
    def _money(self, amount):
        if isinstance(amount, float) and amount < 0:
            print("money can't be negative")
            raise ValueError("money can't cant be negative !!!")
        else:
            self.__money = amount

    def calculate_bahts(self):
        return sum(self.money.values())

    def reset_bahts_inserted(self):
        self.money_count = {key: 0 for key in self.money_count}

    def take_money(self, price):
        self.money += price

    def insert_bahts(self, message):
        bahts_amount = input(f"How many {message}?:")
        return bahts_amount
