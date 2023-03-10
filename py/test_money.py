import unittest
import re
from money import Money
from portfolio import Portfolio
from bank import Bank

class TestMoney(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.bank.addExchangeRate("EUR", "USD", 1.2)
        self.bank.addExchangeRate("USD", "KRW", 1100)
        return super().setUp()

    def testMultiplication(self, ):
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
        self.assertEqual(fifteenDollars, portfolio.evaluate(self.bank, "USD"))

    def testAdditionOfDollarsAndEuros(self, ):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, "USD")
        actualValue = portfolio.evaluate(self.bank, "USD")
        self.assertEqual(expectedValue, actualValue, "%s != %s" %(expectedValue, actualValue))

    def testAdditionOfDollarsAndWons(self, ):
        oneDollar = Money(1, "USD")
        elevenHundredWon = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(oneDollar, elevenHundredWon)
        expectedValue = Money(2200, "KRW")
        actualValue = portfolio.evaluate(self.bank, "KRW")
        self.assertEqual(expectedValue, actualValue, "%s != %s" %(expectedValue, actualValue))

    def testAdditionWithMultipleMissExchangeRates(self, ):
        oneDollar = Money(1, "USD")
        oneEuro = Money(1, "EUR")
        oneWon = Money(1, "KRW")
        portfolio = Portfolio()
        portfolio.add(oneDollar, oneEuro, oneWon)

        scenarios = ["USD", "EUR", "KRW"]
        scenarios = [scenario + "->Kalganid" for scenario in scenarios]
        compile_str = '|'.join(scenarios)
        scenarios_re = re.compile(compile_str)
            
        with self.assertRaisesRegex(
            Exception, 
            scenarios_re
        ): 
            portfolio.evaluate(self.bank, "Kalganid")

    def testConversion(self, ):
        self.bank.addExchangeRate("EUR", "USD", 1.2)
        tenEuros = Money(10, "EUR")
        self.assertEqual(self.bank.convert(tenEuros, "USD"), Money(12, "USD"))

        self.bank.addExchangeRate("EUR", "USD", 1.3)
        tenEuros = Money(10, "EUR")
        self.assertEqual(self.bank.convert(tenEuros, "USD"), Money(13, "USD"))

    def testConversionWithDifferentRatesBetweenTwoCurrencies(self, ):
        bank = Bank()
        tenEuros = Money(10, "EUR")
        with self.assertRaisesRegex(Exception, "EUR->Kalganid"):
            bank.convert(tenEuros, "Kalganid")

    def testAddTwoSameMoneyWithSameCurrency(self, ):
        money1 = Money(10, "USD")
        money2 = Money(11, "USD")
        self.assertEqual(Money(21, "USD"), money1 + money2)


if __name__ == "__main__":
    unittest.main()
