from db_init import Init
from db_plugins import InstantiateDB
from connector_visuals import UID
from db_config import nomenclature

def start():
    #  создаем базу данных
    Init.create_database()
    #  создаем экземпляры классов для каждого ингредиента из бд
    for database in nomenclature:
        InstantiateDB.create_instances(database)

    UID()


if __name__ == '__main__':
    start()


