import random

class Dice:
    def roll(self):
        first = random.randint(1, 4)
        second = random.randint(2, 6)
        return first, second


dice = Dice()
print(dice.roll())