from occurrences import *
import datetime as dt
class payer:
    name = ""
    paycheck_amt = 0
    pay_occurrence = None
    last_check = None

    def __init__(self, name: str, paycheck_amt: float, pay_occurrence: str, last_check: list):
        """
        Args:
            name - name of payer
            paycheck_amt - pay check amount
            pay_occurrence - how often they get paid
        """
        self.name = name
        self.paycheck_amt = paycheck_amt
        self.pay_occurrence = occurrences[pay_occurrence]
        self.last_check = dt.date(last_check[0], last_check[1], last_check[2])

    def __str__(self) -> str:
        return f"name: {self.name}, paycheck_amt: {self.paycheck_amt}, pay_occurrence: {self.pay_occurrence},\nexpenses:\n{self.expenses}"
    
    def __repr__(self) -> str:
        return "payer()"

    # calculate next payday based on occurrence
    def getNextPay(self):
        match self.pay_occurrence:
            case occurrences.SEMI_MONTHLY:
                payday = self.last_check.day
                if payday <= 15:
                    self.last_check = self.last_check.replace(day=30)
                else:
                    self.last_check = self.last_check.replace(day=15, month=self.last_check.month+1)
                day = dt.timedelta(days=1)
                # M=0, T=1, W=2, Th=3, F=4, Sa=5, Su=6
                while self.last_check.weekday() > 4:
                    self.last_check -= day
            case occurrences.BIWEEKLY:
                two_weeks = dt.timedelta(weeks=2)
                self.last_check += two_weeks
        return self.last_check
    
    
