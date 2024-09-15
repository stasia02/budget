import json
from payer import *
from expense import *
class budget:
    payers = {}
    expenses = {}

    def __init__(self, jsonFile):
        with open(jsonFile, "r") as jsonFile:
            budgetJson = json.load(jsonFile)

        for p in budgetJson["payers"]:
            self.addPayer(payer=payer(p["name"], p["paycheck_amt"], p["pay_occurrence"]))

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
    