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
        total = functools.reduce(operator.add, map(lambda money: money.amount, self.moneys), 0)
        return Money(total, currency)