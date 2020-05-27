from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name=None, last_uptate=None, creation_date=None,
                 recipe_list=None):
        if isinstance(name, str):
            self.name = name
        else:
            print("No valid name")
            exit()
        try:
            self.last_uptate = datetime.strptime(last_uptate, '%Y-%m-%d')
        except ValueError:
            print("Incorrect last uptate format, should be YYYY-MM-DD")
        try:
            self.creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
        except ValueError:
            print("Incorrect creation date format, should be YYYY-MM-DD")
        if isinstance(recipe_list, dict) and recipe_list['starter'] and \
           recipe_list['lunch'] and recipe_list['dessert']:
            self.recipe_list = recipe_list
        else:
            print("Recipe list has to be a dictionary and has to be 3 keys")
            exit()

    def get_recipe_by_name(self, name):
        for x in self.recipe_list:
            for y in self.recipe_list[x]:
                for z in y:
                    if (z == name):
                        print(y)
                        return (z)
        print("No recipe with name %s founded" % name)
    
    def get_recipe_by_type(self, recipe_type):
        ret = self.recipe_list[recipe_type]
        return ret

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            print("Argument is not a Recipe")
            exit()
        if recipe.name not in self.recipe_list[recipe.recipe_type]:
            self.recipe_list[recipe.recipe_type] += {recipe.name: {
                'incredients': recipe.incredients, 'meal': recipe.recipe_type,
                'prep_time': recipe.cooking_time}}
            print("New recipe %s added with succes!" % recipe.name)
        else:
            print("Recipe %s is aldrerry in the book." % recipe.name)
        self.last_uptate = datetime.now()
