import json
from calendar import monthrange
from budget_app.payer import *
from budget_app.expense import *

class budget:
    payers = []
    expenses = []

    def __init__(self, jsonFile):
        with open(jsonFile, "r") as jsonFile:
            budgetJson = json.load(jsonFile)
        idx = 0
        for p in budgetJson["payers"]:
            self.payers.append(payer(p["name"], p["paycheck_amt"], p["pay_occurrence"], p["last_check"], p["curr_checking"]))
            self.payers[idx].idx = idx
            idx += 1

        for e in budgetJson["expenses"]:
            expense = jsonToExpense(e, self.payers)
            self.expenses.append(expense)