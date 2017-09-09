import unittest
import monopoly


class TestData(unittest.TestCase):

    def test_data(self):
        self.assertEqual(len(monopoly.data['chest']), 2)
        self.assertEqual(len(monopoly.data['chance']), 10)
        self.assertEqual(len(monopoly.data['board']), 40)


if __name__ == '__main__':
    unittest.main()
