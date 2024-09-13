import json
from payer import *
from expense import *
class budget:
    payers = []
    expenses = {}

    # Add payer to list of payers. This should also add a section to the expenses dict for the payer's personal expenses
    # If a second person is added create a shared expenses entry. It should then populate the entry by merging each payer's
    # list of shared expenses.
    def addPayer(self, payer):
        self.payers.append(payer)
        self.expenses.update({payer.name: []})
        if len(self.expenses.items()) > 1:
            if "shared" not in self.expenses.keys():
                self.expenses["shared"] = []
            # self.expenses = self.mergeExpenses()
        print(f"Added {payer.name} to payers. Current List: {self.payers}")

    #TODO
    def mergeExpenses():
        return
    
    def build(self, jsonFile):
        budgetJson = json.loads(jsonFile)

        for p in budgetJson["payers"]:
            self.addPayer(payer=payer(p["name"], p["paycheck_amt"], p["pay_occurrence"]))

        for e in budgetJson["expenses"]:
            expense = jsonToExpense(e)
            if expense.shared:
                self.expenses