class IngredientManagement:
    def __init__(self, _remaining_water_ml=300, _remaining_milk_ml=200, _remaining_coffee_g=100,
                 _remaining_cocoa_g=100, _remaining_tea_g=100):
     self._remaining_water_ml = _remaining_water_ml
     self._remaining_milk_ml = _remaining_milk_ml
     self._remaining_coffee_g = _remaining_coffee_g
     self._remaining_cocoa_g = _remaining_cocoa_g
     self._remaining_tea_g = _remaining_tea_g

    @property
    def _remaining_water_ml(self):
        return self.__remaining_water_ml

    @_remaining_water_ml.setter
    def _remaining_water_ml(self, _remaining_water_ml):
        if isinstance(_remaining_water_ml, int) and _remaining_water_ml < 0:
            print("--- water must be a positive value in ml ---")
            raise ValueError("water can't be negative !!!")
        else:
            self.__remaining_water_ml = _remaining_water_ml
    @property
    def _remaining_milk_ml(self):
        return self.__remaining_milk_ml

    @_remaining_milk_ml.setter
    def _remaining_milk_ml(self, _remaining_milk_ml):
        if isinstance(_remaining_milk_ml, int) and _remaining_milk_ml < 0:
            print("--- milk must be a positive value in ml ---")
            raise ValueError("milk can't be negative !!!")
        else:
            self.__remaining_milk_ml = _remaining_milk_ml

    @property
    def _remaining_coffee_g(self):
        return self.__remaining_coffee_g

    @_remaining_coffee_g.setter
    def _remaining_coffee_g(self, _remaining_coffee_g):
        if isinstance(_remaining_coffee_g, int) and _remaining_coffee_g < 0:
            print("coffee must be a positive value in g")
            raise ValueError("coffee can't be negative !!!")
        else:
            self.__remaining_coffee_g = _remaining_coffee_g

    @property
    def _remaining_cocoa_g(self):
        return self.__remaining_cocoa_g

    @_remaining_cocoa_g.setter
    def _remaining_cocoa_g(self, _remaining_cocoa_g):
        if isinstance(_remaining_cocoa_g, int) and _remaining_cocoa_g < 0:
            print("cocoa must be a positive value in g")
            raise ValueError("cocoa can't be negative !!!")
        else:
            self.__remaining_cocoa_g = _remaining_cocoa_g

    @property
    def _remaining_tea_g(self):
        return self.__remaining_tea_g

    @_remaining_tea_g.setter
    def _remaining_tea_g(self, _remaining_tea_g):
        if isinstance(_remaining_tea_g, int) and _remaining_tea_g < 0:
            print("tea must be a positive value in g")
            raise ValueError("tea can't be negative !!!")
        else:
            self.__remaining_tea_g = _remaining_tea_g

    def check_ingredient(self, water_needed, milk_needed, coffee_needed, cocoa_needed, tea_needed):
        if water_needed:
            if water_needed > self._remaining_water_ml:
                print(f"Not enough water! Taobinmachine: {self._remaining_water_ml}ml < needed: {water_needed} ml")
                return False

        if milk_needed:
            if milk_needed > self._remaining_milk_ml:
             print(f"There is not enough milk! TaobinMachine: {self._remaining_milk_ml}ml < needed: {milk_needed} ml")
            return False

        if coffee_needed:
            if coffee_needed > self._remaining_coffee_g:
             print(f"there is not enough coffee! TaobinMachine: {self._remaining_coffee_g}g < needed: {coffee_needed} g")
            return False

        if cocoa_needed:
            if cocoa_needed > self._remaining_cocoa_g:
             print(f"there is not enough cocoa! TaobinMachine: {self._remaining_coffee_g}g < needed: {coffee_needed} g")
            return False

        if tea_needed:
            if tea_needed > self._remaining_tea_g:
             print(f"there is not enough tea! TaobinMachine: {self._remaining_tea_g}g < needed: {tea_needed} g")
            return False

        return True

    def deduct_ingredient(self, water_needed, milk_needed, coffee_needed, cocoa_needed, tea_needed):

        if self.check_ingredient(water_needed, milk_needed, coffee_needed, cocoa_needed, tea_needed):
            self._remaining_water_ml -= water_needed
            self._remaining_milk_ml -= milk_needed
            self._remaining_coffee_g -= coffee_needed
            self._remaining_cocoa_g -= cocoa_needed
            self._remaining_tea_g -= tea_needed
            return True
        else:
            return False

