import unittest

class Doller:
    def __init__(self, amount):
        self.amount = amount
        return

    def times(self, multiplier):
        return Doller(self.amount * multiplier)

class TestMoney(unittest.TestCase):
    def testMultiplication(self, ):
        fiver = Doller(5)
        tenner = fiver.times(2)
        self.assertEqual(10, tenner.amount)

if __name__ == "__main__":
    unittest.main()
    