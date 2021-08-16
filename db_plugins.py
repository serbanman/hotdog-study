from db_connector import Connector
from module_ingredients import Ingredient
from datetime import datetime

class InstantiateDB:
    @staticmethod
    def create_instances(db, cls=None):
        con = Connector()

        con.cursor.execute(f'SELECT "name", "cost", "price", "remain" FROM "{db}"')
        rows = con.cursor.fetchall()
        for el in rows:
            Ingredient(name=el[0], cost=el[1], price=el[2], remain=el[3])
            # print(Ingredient._varieties)


class SellToDB:
    @staticmethod
    def register_sell(db: str, name: str, quantity: int):
        con = Connector()
        try:
            con.cursor.execute(f'SELECT "remain" FROM "{db}" WHERE name = "{name}"')
            current_remains = con.cursor.fetchone()
            current_remains = current_remains[0]
            # print(f'Current remains in db = {current_remains}')
            if current_remains >= quantity:
                con.cursor.execute(f'UPDATE "{db}" '
                                   f'SET "remain" = {current_remains - quantity} '
                                   f'WHERE "name" = "{name}"')
                con.connector.commit()

                Ingredient.reduce_remains(name, quantity)
            else:
                print(f'Insufficient remains of {name} in database')
            # con.connector.close()
        except:
            pass


class BuyToDB:
    @staticmethod
    def register(db: str, name: str, quantity: int):
        con = Connector()

        try:
            con.cursor.execute(f'SELECT "remain" FROM "{db}" WHERE name = "{name}"')
            current_remains = con.cursor.fetchone()
            current_remains = current_remains[0]
            # print(f'Current remains in db = {current_remains}')
            con.cursor.execute(f'UPDATE "{db}" '
                               f'SET "remain" = {current_remains + quantity} '
                               f'WHERE "name" = "{name}"')
            con.connector.commit()
            # print(f'New remain - {current_remains + quantity}')
            Ingredient.reduce_remains(name, -quantity)

            # con.connector.close()
        except:
            pass


class OperationsToDB:
    @staticmethod
    def insert(type, price):
        time = datetime.now().strftime('%H:%M %d.%m.%Y')

        con = Connector()

        con.cursor.execute(f'INSERT INTO "operations"'
                           f'("datetime","type","price")'
                           f'VALUES('
                           f'"{time}",'
                           f'"{type}",'
                           f'{price})')
        con.connector.commit()
    @staticmethod
    def get():
        con = Connector()

        con.cursor.execute('SELECT * FROM "operations"')
        values = con.cursor.fetchall()

        return values



