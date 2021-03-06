from book import Book
from recipe import Recipe

book = Book("My 42 cooking book")


pasta = Recipe("Pasta", 1, 60, ["tomato", "pasta", "cheese"],
               "the best", "lunch")
salad = Recipe("Salad", 1, 10, ["tomato", "salad", "bread"],
               "", "starter")


print(pasta)
print(salad)

book.add_recipe(pasta)
book.add_recipe(salad)

book.get_recipe_by_name("Pasta")
book.get_recipes_by_types("starter")

print(book)

b = Book("My seductive recipes")
crumble = Recipe("Crumble", 1, 25, ["apples", "flour", "sugar"],
                 "delicious", "dessert")
b.add_recipe(crumble)
b.get_recipes_by_types("asdasd")
print(b.get_recipes_by_types("dessert")[0])
