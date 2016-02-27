class Ingredient:

    """The Ingredient class contains the name of an ingredient as well as the
    required quantity.
    """

    def __init__(self, options):
        self.hydrate(options)

    def hydrate(self, options):
        self.name = options['name']
        self.quantity = options['quantity']

    def show(self):
        print('  ' + self.quantity + ' ' + self.name)
