from typing import Union
from money import Money

class Bank:
    def __init__(self, ):
        self.exchangeRates = {}
        return

    def addExchangeRate(self, currentFrom: str, currentTo: str, rate: Union[int, float]):
        key = f"""{ currentFrom }->{ currentTo }"""
        self.exchangeRates[key] = rate

    def convert(self, aMoney, aCurrency: str):
        if aMoney.currency == aCurrency:
            return Money(aMoney.amount, aCurrency)
        
        key = f"""{ aMoney.currency }->{ aCurrency }"""
        if key in self.exchangeRates.keys():
            targetAmount = aMoney.amount * self.exchangeRates[key]
            return Money(targetAmount, aCurrency)
        raise Exception(key)
