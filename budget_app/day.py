import datetime as dt
class day:
    events = []
    balances = []
    def __init__(self, date) -> None:
        self.date = dt.date(date[0], date[1], date[2])

    def getSharedBalance(self):
        return sum(self.balances)

    