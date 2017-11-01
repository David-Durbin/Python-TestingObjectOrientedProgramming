class Food:
    def __init__(self):
        self.name = ''
        self.price = 0.0
        self.fat = 0.0
        self.carbs = 0.0
        self.fiber = 0.0
    """
    def __init__(self, n, p):
        self.name = n
        self.price = p
        self.fat = 0.0
        self.carbs = 0.0
        self.fiber = 0.0
    """
    # accessor functions
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_fat(self):
        return self.fat

    def get_carbs(self):
        return self.carbs

    def get_fiber(self):
        return self.fiber

    # mutator functions
    def set_name(self, n):
        self.name = n

    def set_price(self, p):
        self.price = p

    def set_fat(self, ft):
        self.fat = ft

    def set_carbs(self, c):
        self.carbs = c

    def set_fiber(self, fb):
        self.fiber = fb


def main():
    cookie = Food()
    cheeseburger = Food()

    cheeseburger.set_name('cheeseburger')
    cheeseburger.set_price(1.00)


    cookie.set_name('cookie')
    cookie.set_price(0.50)

    print(cheeseburger.get_name(), '  $', format(cheeseburger.get_price(), '.2f'), sep='')
    print(cookie.get_name(), '  $', format(cookie.get_price(), '.2f'), sep='')


main()
