from meal import Meal
import os
import json

class Loader:

    """The Loader class gets the data from the meal json files ad constructs
    Meal objects with it.
    """

    def __init__(self):
        print('Loader initialized')
        working_dir = os.path.dirname(__file__)
        self.data_dir = working_dir + '/../data/'
        self.meal_files = os.listdir(self.data_dir)

    def load_meals(self):
        print('loading meals...')
        meals = []

        for filename in self.meal_files:
            # print('loading meal:')
            # print('  ' + filename)
            meals.append(self.load(filename))

        return meals

    def load(self, filename):
        full_path = self.data_dir + filename
        # print('  File: ' + full_path)
        
        with open(full_path) as f:
            data = json.load(f)
            meal = Meal(data)
        # print('  Name: ' + meal.name)

        return meal
