import datetime as dt
import calendar as cal
import matplotlib.pyplot as plt
from typing import Any
from budget_app.month import *
from budget_app.budget import *

class budgetCalendar():
    storage = {int:[month]}
    
    def __init__(self, budget: budget) -> None:
        self.budget = budget

    def __call__(self, target_year=dt.date.today().year, target_month=dt.date.today().month) -> Any:
        entry = month(target_year, target_month)
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
        
    def display(self, month):
        # display month with events and daily balances
        f, axs = plt.subplots(len())

    def getBudget(self, year, month):
        month = self.storage[year][month]
        for day in month.days:
            for event in day.events:
                if isinstance(event, expense):
                    if event.shared:
                        for payee in self.budget.payers:
                            payee.payBill(amt=event.cost*event.split_rate[payee.idx])
                    else:
                        self.budget.payers[event.payer].payBill(amt=event.cost)
                elif isinstance(event, payer):
                    event.getPaid()
            for payee in self.budget.payers:
                day.balances[payee.idx] = payee.curr_checking
            

    def genGraphs(self):
        # generate graphs showing inflow/outflow of money
        pass

    