#!/usr/bin/python

from ingredient import Ingredient

class Meal:

    """The Meal class contains the name of the meal as well as a list of
    required Ingredients.
    """

    def __init__(self, options):
        self.ingredients = []
        self.hydrate(options)

    def hydrate(self, options):
        self.name = options['name']

        if 'ingredients' in options.keys():
            for ingredient_data in options['ingredients']:
                ingredient = Ingredient(ingredient_data)
                self.ingredients.append(ingredient)

    def show(self, string):
        string = string + self.name + ':' + '\n'
        for ingredient in self.ingredients:
            string = ingredient.show(string)

        return string
