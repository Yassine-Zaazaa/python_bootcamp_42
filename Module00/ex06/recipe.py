cookbook = {
        "sandwich": {"ingredients": ["ham", "bred", "cheese", "tomatoes"], "meal": "lunch", "prep_time": 10,},
        "cake": {"ingredients": ["flour", "sugar", "eggs"], "meal": "dessert", "prep_time": 60,},
        "salad": {"ingredients": ["avocado", "arugula", "tomatoes", "spinach"], "meal": "lunch", "prep_time": 15,},
    }

def print_recipe(recipe_name):
    if(recipe_name in cookbook):
        print(recipe_name,":")
        print("Ingredient lists:", end=" ")
        length = len(cookbook[recipe_name]["ingredients"])
        for i in range(length - 1):
            print(cookbook[recipe_name]["ingredients"][i],end=", ")
        print(cookbook[recipe_name]["ingredients"][length - 1], end=".\n")
        print("To be eaten for", cookbook[recipe_name]["meal"],end=".\n")
        print("Takes", cookbook[recipe_name]["prep_time"], "minutes of cooking.\n")
    else:
        print("This recipe isn't in the cookbook.\n")


def  delete_recipe(recipe_name):
    if(recipe_name in cookbook):
        del cookbook[recipe_name]


def add_recipe(recipe_name, ingredients, meal_type, prep_time):
    cookbook[recipe_name] = {"ingredients": ingredients, "meal": meal_type, "prep_time": prep_time}
    

def print_recipe_names(cookbook):
    RECIPE_NAMES = list(cookbook.keys())
    print("Here are all of the recipes: ")
    for recipe in RECIPE_NAMES:
        print(recipe+".", end="\n")

var = True
while var == True:
    print("Please select an option by typing the corresponding number: ")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    scan = int(input(">> "))
    if scan == 1:
        print("Enter the recipe name, the ingredients, the meal type and the preparation time please.")
        recipe_name = input("Enter recipe name: ")
        ingredients = []
        scan2 = ""
        print("Enter the ingredients (Or enter q to stop): ")
        while scan2 != "q":
            scan2 = input(">> ")
            if scan2 != "q":
                ingredients.append(scan2)
        meal_type = input("Enter the meal type: ")
        prep_time = int(input("Enter the preparation time: "))
        add_recipe(recipe_name, ingredients, meal_type, prep_time)
        var = False
    if scan == 2:
        print("Enter the name of the recipe you want ot delete: ")
        recipe_name = input(">> ")
        delete_recipe(recipe_name)
        var = False
    if scan == 3:
        print("Please enter the recipe's name to get its details: ")
        recipe_name = input(">> ")
        print_recipe(recipe_name) 
        var = False
    if scan == 4:
        print("Here is the cookbook: \n")
        for recipe in cookbook:
            print_recipe(recipe)
        var = False
    if scan == 5:
        print("Cookbook closed.")
        var = False
    
