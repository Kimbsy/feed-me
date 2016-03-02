from loader import Loader
import random

class App:

    """The main application class.
    """

    def __init__(self):
        print('Initializing...')
        self.loader = Loader()
        self.available_meals = self.loader.load_meals()
        self.meals = self.available_meals
        print('Initialization complete\n')

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
        while True:
            self.loop()

    def loop(self):
        print('What would you like to do?')
        print('1) Load this week\'s meals')
        print('2) Generate new meals')
        print('3) Hold specific meals')

        choice = input()

        if int(choice) == 1:
            print('loading')
            self.meals = []
            self.print_meals()
        elif int(choice) == 2:
            print('generating')
            self.meals = self.get_random_meals([])
            self.print_meals()
        elif int(choice) == 3:
            print('make selections:')
            choices = self.get_choices()
            self.meals = self.get_random_meals(choices)
            self.print_meals()


    def print_meals(self):
        for i, meal in enumerate(self.meals):
            day_spaces = self.max_day_len() - len(self.days[i])
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
        available_idxs = list(range(0, len(self.available_meals)))
        print(available_idxs)
        # Remove the held choices.
        if choices:
            for c in choices:
                print(c)
                available_idxs.remove(c)
        meal_idxs = available_idxs

        print(meal_idxs)

        for i in range(1, 8):
            if choices and i in choices:
                meals.append(self.meals[i - 1])
            else:
                rand = random.choice(meal_idxs)
                print(rand)
                meals.append(self.available_meals[rand])
                available_idxs.remove(rand)

        print(meals)


        # for idx in meal_idxs[:7]:
        #     meals.append(self.available_meals[idx])

        return meals

    def get_choices(self):
        # Get choices.
        choices = input().split(' ')
        # Remove blank strings from list.
        choices = [int(c) for c in choices if c]

        if not self.valid_choices(choices):
            print('Please enter a list of choices:')
            return self.get_choices()
        else:
            return choices

    def valid_choices(self, choices):
        valid = True

        for choice in choices:
            if choice < 1:
                print('choices must be greater than 0')
                valid = False
                break
            if choice - 1 >= len(self.meals):
                print('choices must be less than ' + str(len(self.meals) + 2))
                valid = False
                break

        return valid
