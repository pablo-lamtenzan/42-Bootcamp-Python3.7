class Recipe:
    def __init__(self, name="", cooking_1v1="0", cooking_time="0", ingredients="", description="", recipe_type="start"):
        if isinstance(name, str):
            self.name = name
        else:
            print("Bad format in name")
            exit()
        if isinstance(cooking_1v1, int) and cooking_1v1 >= 1 and cooking_1v1 <= 5:
            self.cooking_1v1 = cooking_1v1
        else:
            print("Bad format in cooking 1v1")
            exit()
        if isinstance(cooking_time, int) and cooking_time >= 0:
            self.cooking_time = cooking_time
        else:
            print("Bad format in cooking time")
            exit()
        if isinstance(ingredients, list):
            self.incredients = incredients
        else:
            print("Bad format in incredients")
            exit()
        if isinstance(description, str) or not description:
            self.description = description
        else:
            print("Bad format in description")
            exit()
        if isinstance(recipe_type, str) and (recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert"):
            self.recipe_type = recipe_type
        else:
            print("Bad format in recipe type")
            exit()

    # do i 1 line
    def __str__(self):
        ret = "Name is " + self.name
        ret += "Cooking_1vs1 is " + self.cooking_1v1
        ret += "Cooking time is " + self.cooking_time
        ret += "Incredients are:"
        for i in self.incredients:
            "- " + ret += i
        if not self.description:
            ret += "No description for this recipe"
        else:
            ret += "Description is " + self.description
        ret += "Recipe type" + self.recipe_type
        return ret
