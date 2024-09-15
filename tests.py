import unittest
import occurrences
import io
import datetime as dt
import expense
from payer import *
from occurrences import *
from budget import *

class BudgetTest(unittest.TestCase):

    """def test_createBudget(self):
        b = budget("testBudget.json")
        for p in b.payers:
            print(p)
        for key, expenseDict in b.expenses.items():
            print(key, " expenses:")
            for expense in expenseDict:
                print(expense)"""

    """def test_calcNextPay(self):
        p = payer("Anastasia", 200, "SEMI_MONTHLY", [2024, 9, 13])
        self.assertEqual(dt.date(2024, 9, 30), p.calcNextPay())
        p.last_check = dt.date(2024, 8, 30)
        self.assertEqual(dt.date(2024, 9, 13), p.calcNextPay())"""



    def test_getNextBill(self):
        e = expense()
        p = payer("Anastasia", 200, "SEMI_MONTHLY", [2024, 9, 13])
        e.payer = p

        e.last_occur = dt.date(2024, 5, 1)
        e.occurrence = occurrences.YEARLY
        self.assertEqual(e.getNextBillDate(), dt.date(2025, 5, 1))
        
        e.last_occur = dt.date(2024, 7, 8)
        e.occurrence = occurrences.MONTHLY
        self.assertEqual(e.getNextBillDate(), dt.date(2024, 8, 7))

        e.last_occur = dt.date(2024, 9, 13)
        e.occurrence = occurrences.PER_PAYCHECK
        self.assertEqual(e.getNextBillDate(), dt.date(2024, 9, 30))


if __name__ == '__main__':
    unittest.main()