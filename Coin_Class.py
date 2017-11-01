"""
Creating a coin class for a simple coin flip program.

THIS IS ONLY THE CLASS! NOT A FUNCTIONAL PROGRAM!
"""

import random

class Coin:

    # __init__ function will initialize the created object (self) with the 'side_up' attribute 'heads'
    def __init__(self):
        self.side_up = 'Heads'

    # Toss function generates a random number between 0 and 1 (which is to say, either 0 or 1)
    # If the toss equals 0 then the side is 'Heads' if the toss is 1 then the side is 'Tails'
    def toss(self):
        if random.randint(0, 1) == 0:
            self.side_up = 'Heads'
        else:
            self.side_up = 'Tails'

    # get_side_up function returns the value referenced by side_up
    def get_side_up(self):
        return self.side_up


