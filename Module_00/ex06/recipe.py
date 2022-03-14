cookbook = { 'sandwich' : {'ingredients': ['ham', 'bread', 'tomatoes'], 'meal': 'lunch', 'prep_time': '10'},
        'cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': '60'},
        'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': '15'}}

def print_keys():
    for key, info in cookbook.items(): #info permet de stoker le reste des valeurs
        print("Recipe for : ", key)
    print()
# recipes for :  sandwich
# recipes for :  cake
# recipes for :  salad

def print_values():
    for key, info in cookbook.items(): #info permet de stoker le reste des valeurs
        # print("recipes for : ", key)
        for value in info:
            print(value)

def print_all():
    for key, info in cookbook.items(): #info permet de stoker le reste des valeurs
        print("Recipe for : ", key)
        for value in info:
            print(value + ':', info[value])


def print_recipe(recipe):
    if recipe in cookbook:
        print("\nRecipe for", recipe, end=':\n')
        print("Ingredients list:", cookbook[recipe]['ingredients'])
        print("To be eaten for", cookbook[recipe]['meal'], end='.\n')
        print("Takes", cookbook[recipe]['prep_time'], "minutes of cooking.\n")
    else: 
        print("\nRecipe not found")

def del_recipe(recipe):
    if recipe in cookbook:
        del cookbook[recipe]
    else:
        print("Recipe not found")

def add_recipe(recipe, ingredients, meal, prep_time):
    if recipe in cookbook:
        print("Already in there")
    else:
        cookbook[recipe] = {'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time}

# print_keys()
# print("{0:->30}".format(''))
# print_values()
# print("{0:->30}".format(''))
# print_all()
# print("{0:->30}".format(''))
# print_recipe('cake')
# print("{0:->30}".format(''))
# del_recipe('salad')
# print_all()
# print("{0:->30}".format(''))
# add_recipe('pasta', ['pasta', 'cheese', 'cream'], 'lunch', '10')
# print_all()

while True:
    inp = input('Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>> ')
    if inp.isdigit():
        if inp == '1':
            print()
            name = input('Name of the recipe :\n>> ')
            igts = input('Ingredients :\n>> ')
            ingredients = igts.split()
            meal = input('Type of meal :\n>> ')
            time = input('Time to prepare it :\n>> ')
            print()
            add_recipe(name, ingredients, meal, time)
        elif inp == '2':
            name = input('Name of the recipe to delete:\n>> ')
            print()
            del_recipe(name)
        elif inp == '3':
            name = input('Name of the recipe to print:\n>> ')
            print_recipe(name)
        elif inp == '4':
            print()
            print_keys()
        elif inp == '5':
            print("\nCookbook closed.")
            break
        else:
            print("\nThis option does not exist, please type the corresponding number.\nTo exit, enter 5.\n")
    else :
        print("\nThis option does not exist, please type the corresponding number.\nTo exit, enter 5.\n")
