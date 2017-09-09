import random


class Dice:

    def __init__(self, dice_sides):
        self.dice_sides = dice_sides

    def roll(self):
        total = 0
        for die_sides in self.dice_sides:
            total += random.randrange(1, die_sides + 1)
        return total
