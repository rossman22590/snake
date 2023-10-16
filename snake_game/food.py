import random

class Food:
    def __init__(self):
        self.x = 0
        self.y = 0

    def generate(self):
        self.x = random.randint(0, 9)
        self.y = random.randint(0, 9)
        return self.x, self.y
