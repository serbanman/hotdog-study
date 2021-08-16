from db_config import recipes

class Hotdog:

    @staticmethod
    def get_data(country):
        if country in ('Dutch', 'French', 'Mexican'):
            raw_recipe = recipes[country]
            price = raw_recipe[1]
            quantity_of_each = 1
            recipe_info = (tuple((k, quantity_of_each) for k in raw_recipe[0]), price)
            return recipe_info
        else:
            print('Unknown country')


# print(Hotdog.get_data('French')[1])


