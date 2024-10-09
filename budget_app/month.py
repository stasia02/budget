from budget_app.day import *
from budget_app.expense import *
from budget_app.payer import *
from calendar import Calendar
class month:
    def __init__(self, month: int, year: int, start_balances: dict[str, float]) -> None:
        self.month = month
        self.days = [day(year, month, date) for date in Calendar().itermonthdays(year=year, month=month) if date != 0]
        self.start_balances = start_balances

    def calculate(self):
        shared_balance = self.start_balances["shared"]
        payer_balances = [balance for name, balance in self.start_balances.items() if name != "shared"]
        for day in self.days:
            for event in day.events:
                if isinstance(event, expense):
                    pass
                elif isinstance(event, payer):
                    pass

    def getEndBalance(self):
        # as of right now this will return a list of the payers' balances.
        return self.days[-1].balances

