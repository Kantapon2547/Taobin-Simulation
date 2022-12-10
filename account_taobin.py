import json


class Account:
    def __init__(self, name):
        self.name = name

    def username(self, user_account):
        new_data = {
            self.name: {
                "name": user_account.name,
                "menu": [],
                "cost": 0
            }
        }
        try:
            with open("accounts.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("accounts.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("accounts.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    def menu(self, name, menu):
        try:
            with open("accounts.json", "r") as data_file:
                data = json.load(data_file)
                data[name]["menu"].append(menu.name)
                data[name]["cost"] += menu.cost
        except KeyError:
            pass

        with open("accounts.json", "w") as data_file:
            json.dump(data, data_file, indent=4)


