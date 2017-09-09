import unittest
from monopoly import rank_squares


class TestOdds(unittest.TestCase):

    def test_rank_squares(self):
        rankings = rank_squares(dice_sides=(6, 6))
        self.assertEqual(
            [x[0] for x in rankings[:3]],
            [10, 24, 0]
        )


if __name__ == '__main__':
    unittest.main()
