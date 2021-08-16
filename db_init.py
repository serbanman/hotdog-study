from db_config import database_config, nomenclature
from db_connector import Connector
from db_balance import Balance

class Init:
    @staticmethod
    def check_existance():
        con = Connector()
        try:
            for key in nomenclature:
                for el in nomenclature[key]:
                    con.cursor.execute(f'SELECT * FROM {key} WHERE name = "{el[0]}"')
            result = con.cursor.fetchall()
            # print(result)
            # con.connector.close()
            if len(result) > 0:
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def create_database():
        con = Connector()

        for key in database_config:
            con.cursor.execute(f'CREATE TABLE IF NOT EXISTS {key}({database_config[key]})')

        con.connector.commit()
        if Init.check_existance() is False:
            for key in nomenclature:
                for el in nomenclature[key]:
                    con.cursor.execute(f'INSERT INTO {key}("name","cost", "price","remain")'
                                       f'VALUES(?,?,?,?)', el)
            Balance.write('10')

        # con.cursor.execute(f'SELECT * FROM sauces WHERE name = "mayo"')
        # results = con.cursor.fetchall()
        # print(results)
        con.connector.commit()
        con.connector.close()


# Init.create_database()