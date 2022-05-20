import sys

def check(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
	if not isinstance(name, str) or not len(name):
		print("Input error : name")
		quit()
	elif not isinstance(cooking_lvl, int) or cooking_lvl < 1:
		print("Input error : cooking_lvl")
		quit()
	elif not isinstance(cooking_time, int) or cooking_time < 1:
		print("Input error : cooking_time")
		quit()
	elif not isinstance(ingredients, list):
		print("Input error : ingredients has to be a list")
	elif isinstance(ingredients, list):
		if not ingredients:
			print("Input error : ingredients - list type")
			quit()
		for elm in ingredients:
			if not isinstance(elm, str) or not len(elm):
				print("Input error : ingredients - list type")
				quit()
	if not isinstance(recipe_type, str):
		print("Input error : recipe_type")
		quit()
	else:
		if recipe_type not in  ["lunch", "starter", "dessert"] :
			print("Input error : recipe_type not valid")
			quit()

class Recipe:
	"""Class for the recipe info to be stored"""
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		check(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def __str__(self):
		return 'This is the recipe of ' + self.name + '\n- Cooking lvl : ' + str(self.cooking_lvl) + '\n- Time : ' + str(self.cooking_time) + '\n- Ingredients :\n' + str(self.ingredients) + '\n- Description : ' + self.description + '\n- Type of recipe : ' + str(self.recipe_type)
