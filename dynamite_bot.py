import random

class DynamiteBot:
    def __init__(self):
        self.dynamite = 100

    def make_move(self, gamestate):
        if self.dynamite > 0:
            self.dynamite -= 1
            return 'D'

        options = ['R', 'P', 'S']

        return random.choice(options)
