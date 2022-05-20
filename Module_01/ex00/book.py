import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        if not isinstance(name, str):
            print("Input error : name")
            quit()
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.recipe_list = {'starter': [], 'lunch': [], 'dessert': []}

    def get_recipe_by_name(self, name):
        for elm, type in self.recipe_list.items():
            for key in type:
                if key.name == name:
                    print(key)
                    return self.recipe_list[elm]
        print("The recipe is not in the book or is misspelled")

    def get_recipes_by_types(self, recipe_type):
        if recipe_type not in self.recipe_list:
            print("The type is not recognised")
            return
        print("For the the " + recipe_type + ", you have :")
        for elm in self.recipe_list[recipe_type]:
            print('* ' + elm.name)
        return self.recipe_list[recipe_type]

    def add_recipe(self, recipe):
        self.last_update = datetime.datetime.now()
        if isinstance(recipe, Recipe):
            self.recipe_list[recipe.recipe_type].append(recipe)
        else:
            print("Input error : the recipe is not valid")

    def __str__(self):
        return 'This book is named "' + self.name + \
            '" and has been created the ' \
            + str(self.creation_date) + ' \
            (last update : ' + str(self.last_update) + ')'
