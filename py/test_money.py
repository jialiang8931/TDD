import unittest
from typing import Union
from decimal import Decimal


class TestMoney(unittest.TestCase):
    def testMultiplication(self, ):
        fiver = Dollar(5)
        tenner = fiver.times(2)
        self.assertEqual(10, tenner.amount)

    def testMultiplicationInEuros(self, ):
        tenEuros = Money(10, "EUR")
        twentyEuros = tenEuros.times(2)
        self.assertEqual(20, twentyEuros.amount)
        self.assertEqual("EUR", tenEuros.currency)

class Dollar:
    def __init__(self, amount):
        self.amount = amount
        return

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

class Money:
    def __init__(self, amount: Union[int, float, Decimal], currency: str):
        self.amount = amount
        self.currency = currency
        return

    def times(self, multiplier: Union[int, float]):
        return Money(self.amount * multiplier, self.currency)


if __name__ == "__main__":
    unittest.main()
