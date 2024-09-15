from occurrences import *
class payer:
    name = ""
    paycheck_amt = 0
    pay_occurrence = None

    def __init__(self, name: str, paycheck_amt: float, pay_occurrence: str):
        """
        Args:
            name - name of payer
            paycheck_amt - pay check amount
            pay_occurrence - how often they get paid
        """
        self.name = name
        self.paycheck_amt = paycheck_amt
        self.pay_occurrence = occurrences[pay_occurrence]

    def __str__(self) -> str:
        return f"name: {self.name}, paycheck_amt: {self.paycheck_amt}, pay_occurrence: {self.pay_occurrence},\nexpenses:\n{self.expenses}"
    
    def __repr__(self) -> str:
        return "payer()"

    # calculate next payday based on occurrence
    def calcNextPay():
        return
    
    
