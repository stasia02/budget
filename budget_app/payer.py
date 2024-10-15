from budget_app.occurrences import *
from budget_app.doublyLinkedList import *
import datetime as dt
class payer:
    name: str
    paycheck_amt: float
    pay_occurrence: occurrences
    curr_checking: float
    check_history: dll
    idx: int

    def __init__(self, name: str, paycheck_amt: float, pay_occurrence: str, last_check: list, curr_checking: float):
        self.name = name
        self.paycheck_amt = paycheck_amt
        self.pay_occurrence = occurrences[pay_occurrence]
        self.check_history = dll(dt.date(last_check[0], last_check[1], last_check[2]))
        self.curr_checking = curr_checking

    def __str__(self) -> str:
        return f"name: {self.name}, paycheck_amt: {self.paycheck_amt}, pay_occurrence: {self.pay_occurrence}"
    
    def __repr__(self) -> str:
        return "payer()"

    # calculate next payday based on occurrence & last payday
    def getNextPay(self, last_check):
        if isinstance(last_check, node):
            last_check = last_check.value
        match self.pay_occurrence:
            case occurrences.SEMI_MONTHLY:
                payday = last_check.day
                if payday <= 15:
                    last_check = last_check.replace(day=30)
                else:
                    last_check = last_check.replace(day=15, month=last_check.month+1)
                day = dt.timedelta(days=1)
                # M=0, T=1, W=2, Th=3, F=4, Sa=5, Su=6
                while last_check.weekday() > 4:
                    last_check -= day
            case occurrences.BIWEEKLY:
                two_weeks = dt.timedelta(weeks=2)
                last_check += two_weeks
        return last_check
    
    def next(self):
        return self.check_history.next(self.getNextPay, self.check_history.curr)

    def getPaid(self):
        self.curr_checking += self.paycheck_amt
        return self.curr_checking

    def payBill(self, amt: float):
        self.curr_checking -= amt
        return self.curr_checking
    
