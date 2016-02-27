from ingredient import Ingredient

class Meal:

    def __init__(self, options):
        # print('    Initializing meal...')
        self.ingredients = []
        self.hydrate(options)

    def hydrate(self, options):
        # print('    hydrating meal...')
        self.name = options['name']

        if 'ingredients' in options.keys():
            for ingredient_data in options['ingredients']:
                ingredient = Ingredient(ingredient_data)
                self.ingredients.append(ingredient)

    def show(self):
        print(self.name + ':')
        for ingredient in self.ingredients:
            ingredient.show()
