import os

dir = os.getcwd()
filename = 'database.db'
database_root = os.path.abspath(os.path.join(dir, filename))
# if os.getcwd().endswith('db'):
#     database_root = os.path.join(dir, filename)
# elif os.getcwd().endswith('hotdog'):
#     dir += '/db/'
#     database_root = os.path.join(dir, filename)
# else:
#     dir = os.path.split(dir)[0] + '/db/'
#     database_root = os.path.join(dir, filename)

database_config = {
    'ingredients': (
        '"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
        '"name" varchar(20),'
        '"cost" INTEGER,'
        '"price" INTEGER,'
        '"remain" INTEGER'
    ),
    'toppings': (
        '"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
        '"name" varchar(20),'
        '"cost" INTEGER,'
        '"price" INTEGER,'
        '"remain" INTEGER'
    ),
    'sauces': (
        '"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
        '"name" varchar(20),'
        '"cost" INTEGER,'
        '"price" INTEGER,'
        '"remain" INTEGER'
    ),
    'operations': (
        '"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
        '"datetime" varchar(20),'
        '"type" varchar(20),'
        '"price" INTEGER'
    )
}
#   [name. purchase price, retail price, base remain]
nomenclature = {
    'ingredients': (
        ('bread', 1, 3, 10),
        ('sausage', 5, 10, 10),
    ),
    'toppings': (
        ('fried onion', 1, 3, 10),
        ('pickle', 1, 2, 10),
        ('hot pepper', 2, 4, 10)
    ),
    'sauces': (
        ('ketchup', 1, 0, 10),
        ('mayo', 1, 0, 10),
        ('mustard', 1, 0, 10),
        ('hot sauce', 1, 3, 10)
    )
}

recipes = {
    'Dutch': (('bread', 'sausage', 'fried onion', 'pickle'), 20),
    'French': (('bread', 'sausage'), 15),
    'Mexican': (('bread', 'sausage', 'hot pepper'), 17)
}