import unittest
from monopoly import Dice


class TestDice(unittest.TestCase):

    def test_one_sided_dice(self):
        self.assertEqual(sum(Dice([1]).roll()), 1)
        self.assertEqual(sum(Dice([1, 1]).roll()), 2)
        self.assertEqual(sum(Dice([1, 1, 1]).roll()), 3)

    def test_roll(self):

        ROLLS = 10**5

        test_cases = [
            [1, 2, 3],
            [2, 2, 2],
            [3, 4, 5]
        ]

        for dice_sides in test_cases:
            rolls = set()
            roll_range = range(len(dice_sides), sum(dice_sides) + 1)
            dice = Dice(dice_sides)

            for i in range(ROLLS):
                rolls.add(sum(dice.roll()))

            self.assertEqual(
                rolls,
                set(list(roll_range))
            )


if __name__ == '__main__':
    unittest.main()
