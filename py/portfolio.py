import functools
import operator
from money import Money

class Portfolio:
    def __init__(self, ):
        self.moneys = []
        return

    def add(self, *moneys):
        # self.moneys = [*self.moneys, *moneys]
        self.moneys.extend(moneys)
        return

    def evaluate(self, currency: str):
        total = functools.reduce(operator.add, map(lambda money: self.__convert(money, currency), self.moneys), 0)
        return Money(total, currency)

    def __convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            return aMoney.amount * self._eur_to_usd