import datetime
from decimal import Decimal
from copy import deepcopy
from budget_app.occurrences import *
from budget_app.doublyLinkedList import *

class expense:
    shared: bool
    payer: int
    cost: Decimal
    occurrence: occurrences
    bill_history: dll
    desc: str
    split_rate: list
     
    def __init__(self):
        return

    def getNextBillDate(self, last_occur):
        if isinstance(last_occur, node):
            last_occur = last_occur.value
        match self.occurrence.name:
            case "MONTHLY":
                mth = last_occur.month+1
                if mth > 12:
                    mth = mth - 12
                nxt_occur = last_occur.replace(month=mth)
                return nxt_occur
            case "YEARLY":
                nxt_occur = last_occur.replace(year=(last_occur.year+1))
                return nxt_occur
            case "BIMONTHLY":
                mth = last_occur.month+2
                if mth > 12:
                    mth = mth - 12
                nxt_occur = last_occur.replace(month=mth)
                return nxt_occur

    def next(self):
        return self.bill_history.next(self.getNextBillDate, self.bill_history.curr)

    def __repr__(self) -> str:
        return "expense()"
    
    def __str__(self) -> str:
        return f"desc: {self.desc}\ncost: {self.cost}\noccurence: {self.occurrence}\nlast occurrence: {self.last_occur}\nshared: {self.shared}"

def jsonToExpense(json: dict, payers: list):
    e = expense()
    for key, item in json.items():
        match key:
            case "cost":
                e.cost = Decimal(item)
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
                if item is not None:
                    e.payer = item
            case "split":
                e.split_rate = item
    return e
