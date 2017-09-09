import unittest
from monopoly import Deck
import random


class TestDice(unittest.TestCase):

    def testRoll(self):
        cards = [random.randint(0, 100) for i in range(50)]
        deck = Deck(cards)

        self.assertEqual(
            [deck.draw() for i in range(24)],
            cards[:24]
        )
        self.assertEqual(
            [deck.draw() for i in range(29)],
            cards[24:] + cards[:3]
        )


if __name__ == '__main__':
    unittest.main()
