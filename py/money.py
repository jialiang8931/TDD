from typing import Union
from decimal import Decimal

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

    def __str__(self) -> str:
        return f"""{ self.currency }: { self.amount }"""

    def __add__(self, other):
        if not isinstance(other, Money):
            return None

        if (other is not None) and (self.currency == other.currency):
            return Money(self.amount + other.amount, self.currency)
        else:
            return None 
