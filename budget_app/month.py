from budget_app.day import *
from budget_app.expense import *
from budget_app.payer import *
from calendar import Calendar
class month:
    def __init__(self, month: int, year: int) -> None:
        self.month = month
        self.days = [day(year, month, date) for date in Calendar().itermonthdays(year=year, month=month) if date != 0]

    def getEndBalance(self):
        # as of right now this will return a list of the payers' balances.
        return self.days[-1].balances

