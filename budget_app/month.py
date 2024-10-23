from budget_app.day import *
from budget_app.expense import *
from budget_app.payer import *
from calendar import Calendar
class month:
    days: list[day]
    def __init__(self, month: int, year: int, num_payers: int) -> None:
        self.month = month
        self.year = year
        self.days = [day((year, month, date), ['0' for i in range(num_payers)]) for date in Calendar(6).itermonthdays(year=year, month=month) if date != 0]

    def getEndBalance(self):
        # as of right now this will return a list of the payers' balances.
        return self.days[-1].balances

