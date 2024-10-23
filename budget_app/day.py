import datetime as dt
import decimal
class day:
    
    def __init__(self, date: list|tuple, balances: list[str]) -> None:
        self.date = dt.date(date[0], date[1], date[2])
        self.events = []
        self.balances = balances

    def getSharedBalance(self):
        return sum([decimal(x) for x in self.balances])

    