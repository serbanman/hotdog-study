from db_plugins import BuyToDB, OperationsToDB
from db_config import nomenclature
from db_balance import Balance

class Buy:
    @classmethod
    def register(cls, name, quantity=1):
        #сначала меняем остатки
        databases = [k for k in nomenclature]
        for database in databases:
            BuyToDB.register(database, name, quantity)

        #меняем баланс
        price = 0
        for key in nomenclature:
            for el in nomenclature[key]:
                if el[0] == name:
                    price = el[1]

        current_balance = Balance.read()
        new_balance = int(current_balance) - price
        Balance.write(new_balance)
        # print(Balance.read())

        #заносим в операции
        OperationsToDB.insert('buy', price)