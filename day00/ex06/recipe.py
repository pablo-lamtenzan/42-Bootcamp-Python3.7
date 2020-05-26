cookbook = {'sandwich': {'incredients': ['ham', 'bread', 'cheese', 'tomatoes'],
            'meal': 'lunch', 'prep_time': '10'},
            'cake': {'incredients': ['flour', 'sugar', 'eggs'],
            'meal': 'dessert', 'prep_time': '60'},
            'salad': {'incredients': ['avocado', 'arugula', 'tomatoes',
            'spinash'],
            'meal': 'lunch', 'prep_time': '15'}
            }


def print_recipe(recipe):
    if recipe not in cookbook:
        print("Recipe not founded")
        return
    try:
        print("Recipe for %s:" % name)
        print("Ingredients list: %s" % cookbook[name]['incredients'])
        print("To be eaten for %s." % cookbook[name]['meal'])
        print("Take %s mininutes of cooking.\n" % cookbook[name]['prep_time'])
    except ValueError:
        print("Unespected Error while printing")
    return
    

def delete_recipe(recipe):
    if recipe not in cookbook:
        print("Recipe not founded")
        return
    try:
        cookbook.pop(recipe)
        print("Recipe deleted with succes!\n")
    except ValueError:
        print("Unespected Error while printing")
    return
        

def add_recipe(name, incredients, meal, prep_time):
    if name not in cookbook:
        cookbook[name] = {'incredients': incredients,
            'meal': meal, 'prep_time': prep_time}
        print("Recipe %s added with succes!\n" % name)
    else:
        print("Recipe is alreaddy in the cookbook")


def print_all_recipes_names():
    print("Cookbook's recipes names:")
    for i in cookbook:
        print("- %s" % i)
    print("")
    return


def parse():
    val = input(">> ")
    try:
        val = int(val)
    except ValueError:
        return -1
    if val > 5 or val < 1:
        return -1
    return val


def print_menu():
    print("Please select an option by typing the corresponding number: ")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


print_menu()
n = parse()
while n == -1:
    print("This option does not exist, please type the corresponding number.")
    n = parse()
while n != 5:
    if n == 1:
        print("\nPlease insert recipe parameters:")
        name = input("Name of new recipe: ")
        incredients = []
        while True:
            incredient = input("Incredinets of new recipe: ")
            if not incredient:
                break
            incredients.append(incredient)
        meal = input("Meal of new recipe: ")
        prep_time = input("Prep time of the new recipe: ")
        add_recipe(name, incredients, meal, prep_time)
    elif n == 2:
        print("\nPlease insert name of the recipe and say goodbye:")
        name = input("Name for delete: ")
        delete_recipe(name)
    elif n == 3:
        print("\nPlease enter the recipe's name to get its details:")
        name = input(">> ")
        print_recipe(name)
    elif n == 4:
        print_all_recipes_names()
    elif n == -1:
        print("\nThis option does not exist, please type the corresponding number.")
    print_menu()
    n = parse()

# careful with format {} in incredients
# can t add stuff