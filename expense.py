import occurrences
import datetime
from payer import *
from typing import Optional
from typing import Type

class expense:
    def __init__(self, cost: float, occurrence: str, desc: str, nxt_occur: list, shared: bool = True, payer: Optional["payer"] = None):
        """
        Args:
            cost - cost of expense
            occurrence - how often expense occurs
            desc - short description of what the expense is
            nxt_occur - the next time this expense will happen; formatted as: (year, month, day) //maybe last_occur instead?
            shared - whether the expense is shared between payers or not, default to True
        Returns:
            initialized object with given values
        """
        self.cost = cost
        if occurrence.islower: occurrence = occurrence.upper()
        self.occurrence = occurrences.occurrence
        self.nxt_occur = datetime.datetime(nxt_occur[0], nxt_occur[1], nxt_occur[2])
        self.desc = desc
        self.shared = shared
        self.payer = payer

    def getNextOccurrence():
        return
    
    def __repr__(self) -> str:
        return "expense()"
    
    def __str__(self) -> str:
        return f"cost: {self.cost}\ndesc: {self.desc}\noccurence: {self.occurrence}\nnext occurrence: {self.nxt_occur}\nshared: {self.shared}"

def jsonToExpense(json: dict):
    e = expense()
    for key, item in json.items():
        match key:
            case "cost":
                e.cost = item
            case "occurrence":
                e.occurrence = item
            case "desc":
                e.desc = item
            case "nxt_occur":
                e.nxt_occur = item
            case "shared":
                e.shared = item
            case "payer":
                e.payer = item
    return e
