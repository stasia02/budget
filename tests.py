import unittest
import occurrences
import io
import datetime as dt
import expense
from payer import *
from occurrences import *
from budget import *

class BudgetTest(unittest.TestCase):

    def createExpense(self):
        return

    def createTest(self):
        b = budget()
        e = expense(10.50, "MONTHLY", "test expense", (2024, 9, 15), False)
        print(e)
        p = payer("Anastasia", 2995.90, "semi_monthly")
        print(p)
        print(p)
        b.addPayer(p)
        

if __name__ == '__main__':
    unittest.main()