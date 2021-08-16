
class Ingredient:
    _varieties = []

    def __init__(self, name: str, cost: int, price: int, remain: int):
        def check_existance():
            for el in Ingredient._varieties:
                if el.name == name:
                    return True
            return False

        if check_existance() is False:
            self.__name = name
            self.__cost = cost
            self.__price = price
            self.__remain = remain
            Ingredient._varieties.append(self)
        else:
            print(f'Trying to create another instance of {name}')

    def __repr__(self):
        return self.__name

    @classmethod
    def reduce_remains(cls, name, quantity):
        for el in cls._varieties:
            if el.name == name:
                if el.remain >= quantity:
                    el.__remain -= quantity
                else:
                    print(f'Insufficient remains of {name} in class')

    @classmethod
    def check_sufficiency(cls, recipe_obj):
        remains = []
        for el in recipe_obj[0]:
            for el2 in cls._varieties:
                if el[0] == el2.name:
                    remains.append(el2.remain)

        if min(remains) > 0:
            return True
        else:
            return False

    @property
    def name(self):
        return self.__name

    @property
    def cost(self):
        return self.__cost

    @property
    def price(self):
        return self.__price

    @property
    def remain(self):
        return self.__remain

    @property
    def to_load(self):
        return self.name, self.price, self.remain
