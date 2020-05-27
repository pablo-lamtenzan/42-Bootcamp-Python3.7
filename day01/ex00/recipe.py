class Recipe:
    def __init__(self, name=None, cooking_1v1=None, cooking_time=None,
                 incredients=[], description=None, recipe_type=None):
        if isinstance(name, str):
            self.name = name
        else:
            print("Bad format in name")
            exit()
        if isinstance(cooking_1v1, int) and cooking_1v1 >= 1 and \
           cooking_1v1 <= 5:
            self.cooking_1v1 = cooking_1v1
        else:
            print("Bad format in cooking 1v1")
            exit()
        if isinstance(cooking_time, int) and cooking_time >= 0:
            self.cooking_time = cooking_time
        else:
            print("Bad format in cooking time")
            exit()
        if isinstance(incredients, list):
            self.incredients = incredients
        else:
            print("Bad format in incredients")
            exit()
        if isinstance(description, str) or not description:
            self.description = description
        else:
            print("Bad format in description")
            exit()
        if isinstance(recipe_type, str) and (recipe_type == "starter" or
           recipe_type == "lunch" or recipe_type == "dessert"):
            self.recipe_type = recipe_type
        else:
            print("Bad format in recipe type")
            exit()

    def __str__(self):
        txt = "Name is " + self.name + '\n' + "Cooking_1vs1 is " + \
         str(self.cooking_1v1) + '\n' + "Cooking time is " + \
         str(self.cooking_time) + '\n' + "Incredients are:\n"
        for i in self.incredients:
            txt += i + '\n'
        if not self.description:
            txt += "No description for this recipe" + '\n'
        else:
            txt += "Description is " + self.description + '\n'
        txt += "Recipe type is " + self.recipe_type
        return txt
