from book import Book
from recipe import Recipe
import datetime


tajine = Recipe("Tajine", 5, 360, ["tomatoes", "potatoes", "ham"], "A beautiful tajine", "lunch")
burger = Recipe("Burger", 2, 30, ["ham", "cheese", "sauce", "bread"], "A beast", "lunch")


print(str(tajine), end="\n\n")

recipe_list = {
    "starter": {},
      "lunch": {tajine.name: tajine},
      "dessert": {}
    }

book = Book("Aicha", datetime.datetime.now(), datetime.datetime.now(), recipe_list)

print(book.get_recipe_by_name("Tajine"), end = "\n\n")

print(book.get_recipes_by_types("lunch"), end="\n\n")

book.add_recipe("salad")

salad = Recipe("salad", 2, 10, ["tomatoes", "lettuce", "onion", "cucumber"],"","starter")

book.add_recipe(salad)

print(book.get_recipes_by_types("starter"), end="\n\n")