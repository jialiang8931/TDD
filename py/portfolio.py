import functools
import operator
from money import Money

class Portfolio:
    def __init__(self, ):
        self.moneys = []
        self._eur_to_usd = 1.2
        return

    def add(self, *moneys):
        # self.moneys = [*self.moneys, *moneys]
        self.moneys.extend(moneys)
        return

    def evaluate(self, currency: str):
        total = functools.reduce(operator.add, map(lambda money: self.__convert(money, currency), self.moneys), 0)
        return Money(total, currency)

    def __convert(self, aMoney, aCurrency):
        exchangeRates = {
            "EUR->USD": 1.2,
            "USD->KRW": 1100
        }
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            key = f"""{ aMoney.currency }->{ aCurrency }"""
            currentExchangeRate = exchangeRates[key]
            return aMoney.amount * currentExchangeRate
