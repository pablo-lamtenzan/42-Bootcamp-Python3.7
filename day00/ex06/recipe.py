cookbook = {'sandwich': {'incredients': {'ham', 'bread', 'cheese', 'tomatoes'}, 'meal': 'lunch', 'prep_time': '10mins'},
            'cake': {'incredients': {'flour', 'sugar', 'eggs'}, 'meal': 'dessert', 'prep_time': '60mins'},
            'salad': {'incredients': {'avocado', 'arugula', 'tomatoes', 'spinash'}, 'meal': 'lunch', 'prep_time': '15mins'}
            }

"""
for x in cookbook:
    #print(x)
    for y in cookbook[x]:
        #print(y)
        for z in cookbook[x][y]:
            if len(str(z)) > 1:
                print(z)
"""


def print_recipe(recipe):
    try:
        cookbook[recipe]['incredients']
    except ValueError:
        print("No avlaible")
    print(cookbook[recipe]['incredients'])


# where are the fcking error ? when i del and then i print ?
def delete_recipe(recipe):
    del cookbook[recipe]['incredients']
# probally not have to del incretients but just its members


def add_recipe(recipe):
    cookbook[recipe] = recipe

delete_recipe('cake')
#print_recipe('cake')
print(cookbook['cake'])