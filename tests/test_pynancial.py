from collections import namedtuple

Bracket = namedtuple('Bracket', ['rate', 'floor', 'ceiling'])


class MarriedFilingJointly(object):

    def __init__(self):
        self.brackets = [
            Bracket(rate=0.10, floor=0, ceiling=19750),
            Bracket(rate=0.12, floor=19751, ceiling=80250),
            Bracket(rate=0.22, floor=80251, ceiling=171050),
            Bracket(rate=0.24, floor=171051, ceiling=326600),
            Bracket(rate=0.32, floor=326601, ceiling=414700),
            Bracket(rate=0.35, floor=414701, ceiling=622050),
            Bracket(rate=0.37, floor=622051, ceiling=None),
        ]

    def marginal_tax_rate(self, taxable_income):
        for bracket in self.brackets:
            if taxable_income < bracket.ceiling:
                return bracket.rate

    def taxes_owed(self, taxable_income):
        taxes = 0
        for bracket in self.brackets:
            if taxable_income > bracket.ceiling:
                taxes += bracket.ceiling * bracket.rate
            else:
                taxes += (taxable_income - bracket.floor) * bracket.rate
                return round(taxes, 2)

    def effective_tax_rate(self, taxable_income):
        return round(self.taxes_owed(taxable_income) / taxable_income, 2)


if __name__ == '__main__':
    income = 145000
    filing_status = MarriedFilingJointly()

    print("Income: {income}".format(income=income))
    print("Marginal tax rate: {rate}".format(rate=filing_status.marginal_tax_rate(income)))
    print("Effective tax rate: {rate}".format(rate=filing_status.effective_tax_rate(income)))
    print("Taxes owed: {rate}".format(rate=filing_status.taxes_owed(income)))
