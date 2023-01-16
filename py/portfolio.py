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

    def evaluate(self, bank, currency: str):
        total = 0
        failures = []
        for m in self.moneys:
            try:
                total += bank.convert(m, currency).amount
            except KeyError as ke:
                failures.append(ke)

        if len(failures) == 0:
            return Money(total, currency=currency)
        
        failureMessage = ", ".join(f.args[0] for f in failures)
        raise Exception(f"Missing exchange rate(s):[{ failureMessage }]")

