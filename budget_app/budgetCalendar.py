import datetime as dt
import calendar as cal
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec as gs
from decimal import Decimal
from budget_app.month import *
from budget_app.budget import *

w_days = 'Sun Mon Tue Wed Thu Fri Sat'.split()
month_names = '''
January February March April
May June July August
September October November December'''.split()

class budgetCalendar():
    storage = {int:{int:month}}
    
    def __init__(self, budget: budget) -> None:
        self.budget = budget

    def __call__(self, target_year:int=dt.date.today().year, target_month:int=dt.date.today().month) -> None:
        if target_year not in self.storage.keys():
            self.storage[target_year] = {}
        if target_month-1 not in self.storage[target_year].keys():
            entry = month(year=target_year, month=target_month, num_payers=len(self.budget.payers))
            # add events
            for expense in self.budget.expenses:
                if expense.occurrence == occurrences.PER_PAYCHECK:
                    pass
                else:
                    # grab the last due date before first of target_month
                    curr = expense.bill_history[(dt.date(target_year, target_month, 1), expense)]
                    # iterate through every due date for the month
                    while curr.value <= dt.date(target_year, target_month, cal.monthrange(target_year, target_month)[1]):
                        # add date as an event
                        entry.days[curr.value.day-1].events.append(expense)
                        curr = curr.next if curr.next is not None else expense.next()
    
            for payer in self.budget.payers:
                curr = payer.check_history[(dt.date(target_year, target_month, 1), payer)]
                while curr.value <= dt.date(target_year, target_month, cal.monthrange(target_year, target_month)[1]):
                    entry.days[curr.value.day-1].events.append(payer)
                    for expense in self.budget.expenses:
                        if expense.occurrence == occurrences.PER_PAYCHECK and expense.payer == payer.idx:
                            entry.days[curr.value.day-1].events.append(expense)
                    curr = curr.next if curr.next is not None else payer.next()
            self.display(entry)
            self.getBudget(entry)
            self.storage[target_year][target_month] = entry
        self.display(self.storage[target_year][target_month])

    # TODO add balances to display
    def display(self, month: month):
        tot_num_days = sum(1 for _ in cal.Calendar(6).itermonthdays(month.year, month.month))
        # display month with events and daily balances
        fig = plt.figure()
        grid = gs(tot_num_days//7, 7)

        for idx, day_n in enumerate(cal.Calendar(6).itermonthdays(month.year, month.month)):
            r, c = self.getRowCol(idx)
            ax = fig.add_subplot(grid[r,c])
            ax.set_xticks([])
            ax.set_yticks([])
            if day_n != 0:
                date = month.days[day_n-1]
                ax.text(.02, .98, str(date.date.day),
                        verticalalignment='top',
                        horizontalalignment='left')
                contents = "\n".join([f"{event.name}'s Payday" if isinstance(event, payer) else f"{event.desc} bill is due" for event in date.events])
                
                ax.text(.03, .85, contents,
                        verticalalignment='top',
                        horizontalalignment='left',
                        wrap=True,
                        fontsize=5)
        for n, day in enumerate(w_days):
            fig.axes[n].set_title(day)
        fig.subplots_adjust(hspace=0,wspace=0)
        fig.suptitle(f"{month_names[month.month-1]} {month.year}", fontsize=20, fontweight='bold')
        plt.show()

    def getRowCol(self, n: int, width: int = 7):
        return n//width, n%width
    
    def getBudget(self, month:month):
        for day in month.days:
            for event in day.events:
                if isinstance(event, expense):
                    if event.shared:
                        for payee in self.budget.payers:
                            payee.payBill(amt=str(event.cost*Decimal(event.split_rate[payee.idx])))
                    else:
                        self.budget.payers[event.payer].payBill(amt=event.cost)
                elif isinstance(event, payer):
                    event.getPaid()

            for payee in self.budget.payers:
                day.balances[payee.idx] = payee.curr_checking
            
    def graph(self, month:month):
        # generate graphs showing inflow/outflow of money
        pass

    