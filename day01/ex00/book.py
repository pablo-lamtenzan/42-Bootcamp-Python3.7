import datetime


class Book:
    def __init__(self, name="", last_uptate="", creation_date="", recipe_list=""):
        if isinstance(name, str):
            self.name = name
        else:
            print("No valid name")
            exit()
        try:
            self.last_uptate = datetime.datetime.strptime(last_uptate, '%Y-%m-%d')
        except ValueError:
            print("Incorrect last uptate format, should be YYYY-MM-DD")
        try:
            self.creation_date = datetime.datetime.strptime(creation_date, '%Y-%m-%d')
        except ValueError:
            print("Incorrect creation date format, should be YYYY-MM-DD")
        if isinstance(recipe_list, dict) and recipe_list['starter'] and recipe_list['lunch'] and recipe_list['dessert'] andn not recipe_list[3]:
            self.recipe_list = recipe_list
        else:
            print("Recipe list has to be a dictionary and has to be 3 keys")
            exit()

    def get_recipe_by_name(self, name):
        for x in self.recipe_list:
            for y in self.recipe_list[x]:
                if (y == name):
                    print(self.recipe_list[x][y])
                    return (y)
    
    def get_recipe_by_type(self, recipe_type):
        for x in self.recipe_list:
            if recipe_type == x:
                return(self.recipe_list[x])

    def add_recipe(self, recipe):
        # do latter
