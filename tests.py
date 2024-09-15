import unittest
import occurrences
import io
import datetime as dt
import expense
from payer import *
from occurrences import *
from budget import *

class BudgetTest(unittest.TestCase):

    def test_createBudget(self):
        b = budget("testBudget.json")
        for p in b.payers:
            print(p)
        for key, expenseDict in b.expenses.items():
            print(key, " expenses:")
            for expense in expenseDict:
                print(expense)       

if __name__ == '__main__':
    unittest.main()