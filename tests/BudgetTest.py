import unittest
import io
import datetime as dt
from budget_app.occurrences import *
from budget_app.doublyLinkedList import *
from budget_app.expense import *
from budget_app.payer import *
from budget_app.budget import *

# TODO check that making deep copy of node actually works and doesn't end up causing probs
class BudgetTest(unittest.TestCase):
    def setUp(self) -> None:
        self.p = payer("Anastasia", 1, "MONTHLY", [2024, 5, 1], 1234.31)
        self.b = budget("budget_app/testBudget.json")
        self.e = expense()
        return super().setUp()

    def test_createPayer(self):
        self.assertEqual("Anastasia", self.p.name, f"Name mismatch: {self.p.name}")
        self.assertEqual(1, self.p.paycheck_amt, f"paycheck_amt mismatch: {self.p.paycheck_amt}")
        self.assertEqual(occurrences.MONTHLY, self.p.pay_occurrence, f"pay_occurrence mismatch: {self.p.pay_occurrence}")
        self.assertEqual(dt.date(2024, 5, 1), self.p.check_history.head.value)
        self.assertEqual(1234.31, self.p.curr_checking)

    def test_createBudget(self):
        for p in self.b.payers:
            print(p)
        for key, expenseDict in self.b.expenses.items():
            print(key, " expenses:")
            for expense in expenseDict:
                print(expense)
                print("\n")

    def test_getNextPay(self):
        self.assertEqual(dt.date(2024, 9, 30), self.p.next())

        self.p.check_history = dll(dt.date(2024, 8, 30))
        self.assertEqual(dt.date(2024, 9, 13), self.p.next())

        self.p.pay_occurrence=occurrences.BIWEEKLY
        self.p.check_history = dll(dt.date(2024, 8, 13))
        self.assertEqual(dt.date(2024, 8, 27), self.p.next())


    def test_getNextBill(self):
        self.e.payer = self.p

        self.e.bill_history.head = dt.date(2024, 5, 1)
        self.e.occurrence = occurrences.YEARLY
        self.assertEqual(self.e.bill_history.next(), dt.date(2025, 5, 1))
        
        self.e.bill_history.head = dt.date(2024, 7, 8)
        self.e.occurrence = occurrences.MONTHLY
        self.assertEqual(self.e.bill_history.next(), dt.date(2024, 8, 7))

        self.e.bill_history.head = dt.date(2024, 9, 13)
        self.e.occurrence = occurrences.PER_PAYCHECK
        self.assertEqual(self.e.bill_history.next(), dt.date(2024, 9, 30))
    
    def test_getMonth(self):
        bank = self.b.getMonth(dt.date.today())
        self.assertEqual({"Anastasia": 4213.64, "Adam": 3234.32, "shared": 4213.64+3234.32}, bank)


if __name__ == '__main__':
    unittest.main()