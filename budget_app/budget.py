import json
from calendar import monthrange
from budget_app.payer import *
from budget_app.expense import *

class budget:
    payers = []
    """
    {
        "name": [expense(), expense() ...],
        "name": [expense(), expense() ...],
        "shared": [expense(), expense() ...]
    }
    """
    expenses = {}
    """
    {
        "name": float
    }
    """
    rates = {}

    def __init__(self, jsonFile):
        with open(jsonFile, "r") as jsonFile:
            budgetJson = json.load(jsonFile)

        for p in budgetJson["payers"]:
            self.addPayer(payer=payer(p["name"], p["paycheck_amt"], p["pay_occurrence"], p["last_check"], p["curr_checking"]))
            self.rates[p["name"]] = p["rate"]

        for e in budgetJson["expenses"]:
            expense = jsonToExpense(e, self.payers)
            if expense.shared:
                self.expenses["shared"].append(expense)
            else:
                self.expenses[self.payers[e["payer"]].name].append(expense)

    def addPayer(self, payer):
        """
        Args:
            payer - the payer that needs to be added
        Effect:
            Adds payer to payers, creates an entry for the payers expenses.
            If the payer is the second payer to be added, create a shared
            entry in expenses.
        """
        self.payers.append(payer)
        self.expenses.update({payer.name: []})
        if len(self.expenses.items()) > 1:
            if "shared" not in self.expenses.keys():
                self.expenses["shared"] = []
        print(f"Added {payer.name} to payers. Current List: {self.payers}")

    def getBudget(self, today: dt.date, month: int):
        """
        Args:
            today - starting date for budget
        Return:

        """
        """
        Setting up a bank dictionary to keep track of account balances.
        The keys will be the names of payers and then shared to track a
        combined total.
        """
        bank = {}
        for payer in self.payers:
            bank[payer.name] = payer.check_history.head.value

        assert bank["Anastasia"] == 4213.64, "Anastasia should have 4213.64 in the bank"
        assert bank["Adam"] == 3234.32, "Adam should have 3234.32 in the bank"

        bank["shared"] = round(sum([i for i in bank.values()]), 2)
        assert bank["shared"] == 7447.96, f"shared amt should be 7447.96, not: {bank['shared']}"
        # get days left in month
        _, days_left = monthrange(today.year, today.month)
        days_left -= today.day

        payday = False
        while today.month <= month:
            for day in range(days_left+1):
                date = today.replace(day=today.day+day)
                for payer in self.payers:
                    if date == payer.check_history:
                        bank[payer.name] = payer.getPaid()
                        payday = True
                    
                    def handleExpense(expense, balance):
                        if expense.occur == occurrences.PER_PAYCHECK and payday:
                            balance -= expense.cost
                        elif expense.occur == occurrences.MONTHLY:
                            if expense.bill_history.month < date.month:
                                expense.getNextBillDate()
                            if expense.bill_history == date:
                                balance -= expense.cost
                        elif expense.occur == occurrences.WEEKLY:
                            pass
                        elif expense.occur == occurrences.BIMONTHLY:
                            pass
                        elif expense.occur == occurrences.YEARLY:
                            pass
                        return balance

                    # TODO handling for when calculating budgets rolls into the next year
                    for expense in self.expenses[payer.name]:
                        handleExpense(expense, payer.curr_checking)
                bank["shared"] = sum([payer.curr_checking for payer in self.payers])
                for expense in self.expenses["shared"]:
                    #handleExpense(exp)
                    pass
        return bank
            


    def clear(self):
        self.payers = {}
        self.expenses = {}
        self.rates = {}

    