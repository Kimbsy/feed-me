from loader import Loader
import random
import os

class App:

    """The main application class takes user input and manages the applicatino loop.
    """

    def __init__(self):
        os.system('clear')
        print('Initializing...')
        self.loader          = Loader()
        self.available_meals = self.loader.load_meals()
        self.size            = os.popen('stty size', 'r').read().split()
        self.active          = True
        print('Initialization complete')

        self.days = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday',
        ]

    def start(self):
        while self.active:
            self.loop()

    def loop(self):
        print('\nWhat would you like to do?')
        print('1) Load this week\'s meals')
        print('2) Generate new meals')
        print('3) Hold specific meals')
        print('4) Save current meals')

        choice = input()

        if int(choice) == 1:
            # @TODO: load saved meals
            os.system('clear')
            print('loading current meals...')
            self.meals = []
            self.print_meals()
        elif int(choice) == 2:
            os.system('clear')
            print('generating meals...\n')
            self.meals = self.get_random_meals([])
            self.print_meals()
        elif int(choice) == 3:
            print('make selections:')
            choices = self.get_choices()
            self.meals = self.get_random_meals(choices)
            os.system('clear')
            print('generating meals...\n')
            self.print_meals()
        elif int(choice) == 4:
            # @TODO: save meals and email shopping list


    def print_meals(self):
        for i, meal in enumerate(self.meals):
            day_spaces  = self.max_day_len() - len(self.days[i])
            meal_spaces = self.max_meal_len() - len(meal.name)

            print(self.days[i] + ': ' + (' ' * day_spaces) + meal.name + (' ' * meal_spaces) + ' (' + str(i + 1) + ')')

    def max_day_len(self):
        return max([len(day) for day in self.days])

    def max_meal_len(self):
        return max([len(meal.name) for meal in self.meals])

    def get_random_meals(self, choices):
        meals = []

        # Make sure the choices are in order.
        choices.sort()

        # Get list of available meals.
        available_meals = list(self.available_meals)

        # Remove the held choices.
        if choices:
            for c in choices:
                available_meals.remove(self.meals[c])

        # Loop to fill up meals list.
        for i in range(0, 7):
            # If we're at the index of a choice, add in that choice.
            if choices and i in choices:
                choice = self.meals[i]
                meals.append(choice)
            else:
                # Otherwise, make a random choice from what's available and
                # remove it from available.
                rand = random.choice(available_meals)
                meals.append(rand)
                available_meals.remove(rand)

        meals = meals[:7]

        return meals

    def get_choices(self):
        # Get choices.
        choices = input().split(' ')
        # Remove blank strings from list and decrement index.
        choices = [int(c) - 1 for c in choices if c]

        # Validate choices, if invalid, request new choices.
        if not self.valid_choices(choices):
            print('Please enter a list of choices:')
            return self.get_choices()
        else:
            return choices

    def valid_choices(self, choices):
        valid = True

        for choice in choices:
            if choice < 0:
                print('choices must be greater than 0')
                valid = False
                break
            if choice >= len(self.meals):
                print('choices must be less than ' + str(len(self.meals) + 1))
                valid = False
                break

        return valid
