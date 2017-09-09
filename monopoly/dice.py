import random


class Dice:

    def __init__(self, dice_sides):
        self.dice_sides = dice_sides

    def roll(self):
        return [random.randint(1, die_sides) for die_sides in self.dice_sides]