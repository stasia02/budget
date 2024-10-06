from tests.BudgetTest import *

def getNextDay(today):
    day = datetime.timedelta(1)
    return today+day

b = BudgetTest()
"""today = datetime.date.today()
d1 = dll(today)
d2 = dll(today)
print(d1==d2)

d2.next(getNextDay, [today])
print(d1==d2)
d1.next(getNextDay, [today])
print(d1==d2)
try: 
    assert(d1 == d2)
except Exception as e:
    print(e)"""

b.setUp()
b.test_createPayer()