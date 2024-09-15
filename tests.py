import unittest
import occurrences
import io
import datetime as dt
import expense
from payer import *
from occurrences import *
from budget import *

class BudgetTest(unittest.TestCase):
    def test_createPayer(self):
        p = payer("Anastasia", 1, "MONTHLY", [2024, 5, 1], 1234.31)
        self.assertEqual("Anastasia", p.name, f"Name mismatch: {p.name}")
        self.assertEqual(1, p.paycheck_amt, f"paycheck_amt mismatch: {p.paycheck_amt}")
        self.assertEqual(occurrences.MONTHLY, p.pay_occurrence, f"pay_occurrence mismatch: {p.pay_occurrence}")
        self.assertEqual(dt.date(2024, 5, 1), p.last_check)
        self.assertEqual(1234.31, p.curr_checking)


    def test_createBudget(self):
        b = budget("testBudget.json")
        for p in b.payers:
            print(p)
        for key, expenseDict in b.expenses.items():
            print(key, " expenses:")
            for expense in expenseDict:
                print(expense)

    def test_getNextPay(self):
        p = payer("Anastasia", 200, "SEMI_MONTHLY", [2024, 9, 13])
        self.assertEqual(dt.date(2024, 9, 30), p.getNextPay())
        p.last_check = dt.date(2024, 8, 30)
        self.assertEqual(dt.date(2024, 9, 13), p.getNextPay())



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
    
    def test_getMonth(self):
        b = budget("testBudget.json")
        bank = b.getMonth()
        self.assertEqual({"Anastasia": 4213.64, "Adam": 3234.32}, bank)


if __name__ == '__main__':
    unittest.main()