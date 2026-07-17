class Node:
    def __init__(self,coeff,exp):
        self.coeff=coeff
        self.exp=exp
        self.next=None
class polynomial:

    def __init__(self):
        self.head=None
def insert(self,coeff,exp):
    newnode=Node(coeff,exp)
    if self.head is None:
        self.head = newnode
        return
    current=self.head
    while current:
        if current.exp==exp:
            current.coeff+=coeff
            return
        if current.next is None:
            break
        current=current.next
        current.next=newnode
def delete(self,exp):
    current=self.head
    previous=None
    while current:
        if current.exp==exp:
            if previous is None:
                self.head=current.next
                else:
                    previous.next=current.next
                return
        previous=current
        current=currrent.next
