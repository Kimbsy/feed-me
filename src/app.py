from loader import Loader

class App:

    """The main application class.
    """

    def __init__(self):
        print('Initializing...')
        self.loader = Loader()
        self.meals = self.loader.load_meals()
        print('Initialization complete\n')

    def start(self):
        print('What would you like to eat?')
        print('Options:')

        for i, meal in enumerate(self.meals):
            print(str(i + 1) + ') ' + meal.name)

        choice = self.get_choice()

        meal = self.meals[choice]

        print('\nYou chose: ')
        meal.show()

    def get_choice(self):
        choice = input()

        if not self.valid_choice(choice):
            print('Please choose a number from 1 to ' + str(len(self.meals)))
            return self.get_choice()
        else:
            return int(choice) - 1

    def valid_choice(self, choice):
        return choice.isnumeric() and int(choice) > 0 and int(choice) - 1 < len(self.meals)
