from unittest import TestCase

from utils import minimum_coin_bottom_up


class VendingMachine(TestCase):

    def test_change_coin_values(self):
        total = 12
        coins = [1, 2, 5]
        best_possible_change = [5, 5, 2]

        change = minimum_coin_bottom_up(total, coins)
        self.assertEqual(best_possible_change, change)
