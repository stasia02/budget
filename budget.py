import json
from payer import *
from expense import *

class budget:
    payers = {}
    expenses = {}
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
                self.expenses[e["payer"]].append(expense)

    # Add payer to list of payers. This should also add a section to the expenses dict for the payer's personal expenses
    # If a second person is added create a shared expenses entry. 
    def addPayer(self, payer):
        self.payers.update({payer.name: payer})
        self.expenses.update({payer.name: []})
        if len(self.expenses.items()) > 1:
            if "shared" not in self.expenses.keys():
                self.expenses["shared"] = []
        print(f"Added {payer.name} to payers. Current List: {self.payers}")

    def getMonth(self):
        pay_dates = []
        bill_dates = []
        bank = { key : 0 for key in self.expenses.keys() }
        for account, amt in bank.items():
            if account == "shared":
                bank.update({})
            bank.update({account: self.payers[account].curr_checking})
        # get days left in month
        # calculate important dates + store: paydays, bill days
        """
        for day in days_left:
        """  
        return bank


    