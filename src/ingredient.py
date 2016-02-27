class Ingredient:

    def __init__(self, options):
        self.hydrate(options)

    def hydrate(self, options):
        self.name = options['name']
        self.quantity = options['quantity']
        # print('      hydrating ingredient...')
        # print('      ' + self.show())

    def show(self):
        print('  ' + self.quantity + ' ' + self.name)
