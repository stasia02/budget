import datetime
from copy import deepcopy
from budget_app.occurrences import *
from budget_app.doublyLinkedList import *

class expense:
    shared = True
    payer = None
    cost = 0
    occurrence = None
    description = ""
     
    def __init__(self):
        return

    def getNextBillDate(self, last_occur):
        match self.occurrence.name:
            case "MONTHLY":
                month = datetime.timedelta(days=30)
                last_occur += month
                return last_occur
            case "YEARLY":
                year = datetime.timedelta(days=365)
                last_occur += year
                return last_occur

    def next(self):
        return self.bill_history.curr.next(self.getNextBillDate, self.bill_history.curr)

    def __repr__(self) -> str:
        return "expense()"
    
    def __str__(self) -> str:
        return f"desc: {self.desc}\ncost: {self.cost}\noccurence: {self.occurrence}\nlast occurrence: {self.last_occur}\nshared: {self.shared}"

def jsonToExpense(json: dict, payers: dict):
    e = expense()
    for key, item in json.items():
        match key:
            case "cost":
                e.cost = item
            case "occurrence":
                e.occurrence = occurrences[item.upper()]
            case "desc":
                e.desc = item
            case "last_occur":
                if json["occurrence"] == occurrences.PER_PAYCHECK.name:
                    date = deepcopy(payers[json["payer"]].check_history.head)
                    e.bill_history = date
                else:
                    e.bill_history = dll(datetime.date(item[0], item[1], item[2]))
            case "shared":
                e.shared = item
            case "payer":
                if item:
                    e.payer = item
    return e
