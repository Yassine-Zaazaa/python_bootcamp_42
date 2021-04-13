import datetime
from recipe import Recipe

class Book:
    def __init__(self, name, last_update, creation_date, recipe_list):
        if type(name) != str or name == '':
            print("The name should be a string")
            raise ValueError
        self.name = name
        self.creation_date = creation_date
        self.last_update = last_update
        if type(recipe_list ) != dict or "starter" not in recipe_list.keys() or "lunch" not in recipe_list.keys() or "dessert" not in recipe_list.keys():
            print("The recipe list should be a dictionary with 3 keys: 'starter', 'lunch', 'dessert'.")
        self.recipe_list = recipe_list
    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        starter = list(self.recipe_list["starter"])
        lunch = list(self.recipe_list["lunch"])
        dessert = list(self.recipe_list["dessert"])
        if name in starter:
            return self.recipe_list["starter"][name]
        elif name in lunch:
            return self.recipe_list["lunch"][name]
        elif name in dessert:
            return self.recipe_list["dessert"][name]
        else:
            return f"{name} is not in the recipe list"  

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type.lower() == "starter":
            return list(self.recipe_list["starter"])
        elif recipe_type.lower() == "lunch":
            return list(self.recipe_list["lunch"])
        elif recipe_type.lower() == "dessert":
            return list(self.recipe_list["dessert"])
        else:
            return "The recipe type given is not valid"
        
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if type(recipe) != Recipe:
            print("Please create the recipe then add it.")
            return
        self.recipe_list[recipe.recipe_type][recipe.name]=recipe
        self.last_update=datetime.datetime.now()
        return
            
            
        