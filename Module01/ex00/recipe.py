class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if name=='' or type(name)!=str:
            print("The name should be a string.")
            raise ValueError
        self.name = name
        if type(cooking_lvl)!=int or  cooking_lvl > 5 or cooking_lvl < 1:
            print("The cooking level should be an integer between 1 and 5.")
            raise ValueError
        self.cooking_lvl = cooking_lvl
        if type(cooking_time)!=int or cooking_time < 0:
            print("The cooking time should be a positive integer.")
            raise ValueError
        self.cooking_time = cooking_time
        if type(ingredients) != list:
            print("The ingredients should be a list of strings.")
            raise ValueError
        self.ingredients = ingredients
        if type(description) != str:
            print("The description should be a string.")
            raise ValueError
        self.description = description
        if type(recipe_type) != str or recipe_type.lower() != "starter" and recipe_type.lower() !="lunch" and recipe_type.lower() !="dessert":
            print("The recipe type should either be 'starter' or 'lunch' or 'dessert")
            raise ValueError
        self.recipe_type = recipe_type
    
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt="The {recipe} recipe is of level {lvl}, needs {time} min, uses the following ingredients {ing},{desc} it is taken as {typ}".format(recipe=self.name,lvl=self.cooking_lvl,time=self.cooking_time,ing=self.ingredients,desc=self.description,typ=self.recipe_type)
        return txt
        