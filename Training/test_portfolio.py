import unittest
# from Training.demo import Portfolio
# from Training.demo import Portfolio
from demo import Portfolio
from Library.config import Config


class Test_Portfolio(unittest.TestCase):

    def test_empty_portfolio(self):
        p = Portfolio()
        self.assertEqual(p.cost(), 0.00)

    def test_buy_one_stock(self):
        p = Portfolio()
        p.buy('IBM', 10, 10)
        self.assertEqual(p.cost(), 100.00)

    def test_buy_two_stocks(self):
        p = Portfolio()
        p.buy('IBM', 10, 10)
        p.buy('HP', 10, 10)
        self.assertEqual(p.cost(), 200.00)

    def test_sell_stocks(self):
        p = Portfolio()
        p.buy('IBM', 10, 10)
        p.buy('HP', 10, 10)
        p.sell('HP', 5)
        self.assertEqual(p.cost(), 150.00)

    def test_sell_not_owned(self):
        p = Portfolio()
        p.buy('IBM', 10, 10)
        p.buy('HP', 10, 10)
        with self.assertRaises(ValueError):
            p.sell('AAPL', 10)

    def test_not_enough_stocks(self):
        p = Portfolio()
        p.buy('IBM', 10, 10)
        p.buy('HP', 10, 10)
        with self.assertRaises(ValueError):
            p.sell('HP', 11)