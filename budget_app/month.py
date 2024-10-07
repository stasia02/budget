from budget_app.day import *
from calendar import Calendar
class month:
    def __init__(self, month, year, start_balance) -> None:
        self.month = month
        self.days = [day(year, month, date) for date in Calendar().itermonthdays(year=year, month=month) if date != 0]
        self.start_balance = start_balance

    def getEndBalance(self):
        pass

    