'''
ExchangeRates.py
Sinem Firat

FINE 3300 Assignment #1 - Part 1
ExchangeRates class that reads the Bank of Canada annual exchange rate file
and converts an amount from CAD to USD or from USD to CAD using the latest
USD/CAD exchange rate (the last row of the file).
'''

import csv

class ExchangeRates:
    def __init__(self, file_name="BankOfCanadaExchangeRate.2026.csv"):
        self.__file_name = file_name
        self.__date = ""
        self.__usd_cad = 0.0
        self.__read_file()

    def __read_file(self):
        # Read every row of the file into a list
        with open(self.__file_name, newline="") as file:
            rows = list(csv.reader(file))

        # First row holds the column names, last row holds the latest rates
        header = rows[0]
        latest = rows[-1]

        # FXAUSDCAD is the number of Canadian dollars for 1 US dollar
        usd_cad_column = header.index("FXAUSDCAD")

        self.__date = latest[0]
        self.__usd_cad = float(latest[usd_cad_column])

    def get_date(self):
        return self.__date

    def get_rate(self):
        return self.__usd_cad

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == to_currency:
            return amount
        elif from_currency == "USD" and to_currency == "CAD":
            return amount * self.__usd_cad
        else:
            # CAD to USD
            return amount / self.__usd_cad


if __name__ == "__main__":
    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Convert from (USD or CAD): ").upper()
    to_currency = input("Convert to (USD or CAD): ").upper()

    converted = rates.convert(amount, from_currency, to_currency)

    print("Bank of Canada exchange rate ({}): 1 USD = {:.4f} CAD".format(rates.get_date(), rates.get_rate()))
    print("${:,.2f} {} = ${:,.2f} {}".format(amount, from_currency, converted, to_currency))
