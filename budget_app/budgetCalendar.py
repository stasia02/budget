import datetime as dt
import calendar as cal
from typing import Any
from budget_app.month import *
from budget_app.budget import *

class budgetCalendar():
    storage = {}
    
    def __init__(self, budget: budget) -> None:
        self.budget = budget

    def __call__(self, target_year=dt.date.today().year, target_month=dt.date.today().month) -> Any:
        if target_month-1 in self.storage.keys():
            strt_bal = self.storage[target_month-1].getEndBalance()
        else:
            strt_bal = sum([p.curr_checking for p in self.budget.payers])
        entry = month(target_year, target_month, strt_bal)

        for expense in self.budget.expenses:
            # grab the last due date before first of target_month
            curr = expense.bill_history[dt.date(target_year, target_month, 1)]
            curr = curr.next if curr.next is not None else curr = expense.bill_history.next()
            # iterate through every due date for the month
            while curr.value <= dt.date(target_year, target_month, cal.monthrange(target_year, target_month)[1]):
                # add date as an event
                entry.days[curr.value.day-1].events.append(expense)
                curr = curr.next if curr.next is not None else curr = expense.bill_history.next()
        
        for payer in self.budget.payers:
            curr = payer.check_history[dt.date(target_year, target_month, 1)]
            curr = curr.next if curr.next is not None else curr = payer.check_history.next()
            while curr.value <= dt.date(target_year, target_month, cal.monthrange(target_year, target_month)):
                entry.days[curr.value.day-1].events.append(payer)
                curr = curr.next if curr.next is not None else curr = payer.check_history.next()
        
    def display(self):
        # display month with events and daily balances
        pass

    def getMonth(self, year, month):
        pass

    def genGraphs(self):
        # generate graphs showing inflow/outflow of money
        pass

    