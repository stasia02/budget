class day:
    events = []
    balances = []
    def __init__(self, date) -> None:
        self.date = date

    def getSharedBalance(self):
        return sum(self.balances)

    