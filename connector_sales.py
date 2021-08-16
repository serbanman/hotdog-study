from db_plugins import SellToDB, OperationsToDB
from db_config import nomenclature
from module_ingredients import Ingredient
from db_balance import Balance

class SalesProcessor:
    @staticmethod
    def register_sell(recipe_object):
        if Ingredient.check_sufficiency(recipe_object) is True:
            #  уменьшаем остатки
            def register(name, quantity):
                databases = [k for k in nomenclature]
                for database in databases:
                    SellToDB.register_sell(database, name, quantity)
            for el in recipe_object[0]:
                register(el[0], el[1])

            #  меняем баланс
            price = recipe_object[1]
            current_balance = Balance.read()
            new_balance = int(current_balance) + price
            Balance.write(str(new_balance))

            #заносим в операции
            OperationsToDB.insert('sell', price)

            return True
        else:
            return False
