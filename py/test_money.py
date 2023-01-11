import unittest
from typing import Union
from decimal import Decimal
import functools
import operator


class TestMoney(unittest.TestCase):
    def testMultiplicationInDollars(self, ):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        self.assertEqual(tenDollars, fiveDollars.times(2))

    def testMultiplicationInEuros(self, ):
        tenEuros = Money(10, "EUR")
        twentyEuros = tenEuros.times(2)
        self.assertEqual(20, twentyEuros.amount)
        self.assertEqual("EUR", tenEuros.currency)

    def testDivision(self, ):
        originalMoney = Money(4002, "KRW")
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(expectedMoneyAfterDivision.amount, actualMoneyAfterDivision.amount)
        self.assertEqual(expectedMoneyAfterDivision.currency, actualMoneyAfterDivision.currency)

    def testAddition(self, ):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))


class Money:
    def __init__(self, amount: Union[int, float, Decimal], currency: str):
        self.amount = amount
        self.currency = currency
        return

    def times(self, multiplier: Union[int, float]):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor: Union[int, float]):
        return Money(self.amount / divisor, self.currency)

    def __eq__(self, otherInstance: object) -> bool:
        return self.amount == otherInstance.amount and self.currency == otherInstance.currency

class Portfolio:
    def __init__(self, ):
        self.moneys = []
        return

    def add(self, *moneys):
        # self.moneys = [*self.moneys, *moneys]
        self.moneys.extend(moneys)
        return

    def evaluate(self, currency: str):
        total = functools.reduce(operator.add, map(lambda money: money.amount, self.moneys), 0)
        return Money(total, currency)

if __name__ == "__main__":
    unittest.main()
