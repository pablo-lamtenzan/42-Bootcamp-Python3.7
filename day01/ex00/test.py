from book import Book
from recipe import Recipe

tourte = Recipe("tourte", 1, 40, ['aaa', 'nnnn', 'cccc'], "bci3bv", "starter")
to_print = str(tourte)
print(to_print)

cookbook = {'starter': [{'salad': {
               'incredients': ['avocado', 'arugula', 'tomatoes', 'spinash'],
               'meal': 'lunch',
               'prep_time': '15'}}],
            'lunch': [{'sandwich': {
               'incredients': ['ham', 'bread', 'cheese', 'tomatoes'],
               'meal': 'lunch',
               'prep_time': '10'}}],
            'dessert': [{'cake': {
               'incredients': ['flour', 'sugar', 'eggs'],
               'meal': 'dessert',
               'prep_time': '60'}}]}


book = Book("AA", "2020-05-26", "2020-09-09", cookbook)
print("")
print(book.get_recipe_by_type("starter"))
print("")

book.add_recipe(tourte)
print(book.recipe_list)
# print(book.get_recipe_by_type("starter"))
book.get_recipe_by_name("tourte")
# mmm 
