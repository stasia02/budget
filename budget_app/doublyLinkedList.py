class node:
    def __init__(self, pre=None, value=None) -> None:
        # self.next = next
        self.pre = pre
        self.value = value
        self.next = None

    def __repr__(self):
        return f"node({self.val})"

    def __eq__(self, other: object):
        if isinstance(other, node):
            if self.pre == other.pre and self.value == other.value and self.next == other.next:
                return True
        return False
        
class dll:
    length = 0
    def __init__(self, date):
        self.head = self.curr = node(value=date)
        self.length += 1

    def __repr__(self) -> str:
        return f"dll({self.head})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, dll):
            if self.length != other.length:
                return False
            elif self.length == 0 and other.length == 0:
                return True
            
            self_ptr = self.head
            other_ptr = other.head
            while self_ptr:
                if self_ptr.value != other_ptr.value:
                    return False
                self_ptr=self_ptr.next
                other_ptr=other_ptr.next
            return True
        return False

    def pre(self):
        # check for prev node
        if self.curr.pre:
            # set curr node of dll to prev node
            self.curr = self.curr.pre
        # return curr node of dll
        return self.curr
    
    def next(self, func, args):
        # check for next node
        if self.curr.next:
            # set curr node of dll to next node
            self.curr = self.curr.next
            # return curr node of dll
            return self.curr
        else:
            # create and set next node using getNextPay or getNextBill func
            self.curr.next = node(pre=self.curr, value=func(*args))
            # set curr node of dll to next node
            self.curr = self.curr.next
            self.length += 1
            # return curr node of dll
            return self.curr