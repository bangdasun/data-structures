"""
Written 1
"""

# With iterators
from collections import Iterator
class enhanceIterator(Iterator):
    """
    class enhanceIterator
        
        inheritance from Iterator, hasNext() method is added
    
    https://groups.google.com/forum/#!topic/comp.lang.python/OD3VQLQVuHo
    """
    def __init__(self, lst):
        self.it = iter(lst)
        self.size = len(lst) - 1
    
    def next(self):
        if self.size < 0:
            raise StopIteration
        self.n -= 1
        return next(self.it)
    
    def hasNext(self):
        return self.size >= 0
    
# test
lst1 = range(10)
it1 = enhanceIterator(lst1)
while it1.hasNext():
    print(it1.next())


def printLots(L, P):
    """
    printLosts(L, P) -> L[P]
        
    print the element in L where the index is the element of P 
    """
    Liter = enhanceIterator(L)
    Piter = enhanceIterator(P)
    
    # construct two position in P
    # pf as front, pb as back
    pf = -1
    pb = 0
    while Liter.hasNext() and Piter.hasNext():
        # update the back position as the next element of P
        pb = Piter.next()
        
        # move the iterator of L one position before the index
        for i in range(pf, pb - 1):
            Liter.next()
        # update the front position as the back position at the previous step
        pf = pb
        # print the element of L at the index given by P    
        print(Liter.next())
    
def main():
    # two lists
    L = range(10)
    P = [0, 2, 10]
    
    # print the element of L at index given by P
    printLots(L, P)

"""
Written 2
"""

def findIntersection(lst1, lst2):
    """
    findIntersection(lst1, lst2) -> lst1 and lst2
    
    return the intersection of lst1 and lst2
    where lst1 and lst2 should be sorted already
    """
    it1 = enhanceIterator(lst1)
    it2 = enhanceIterator(lst2)
    
    elmt1 = lst1[0]
    elmt2 = lst2[0]
    
    while it1.hasNext() and it2.hasNext():
        # if elmt1 equals elmt2, then this would be the common
        # otherwise elmt1 < elmt2, move the iterator back; same for elmt1 > emlt2
        if elmt1 == elmt2:
            print(elmt1)
            elmt1 = it1.next()
            elmt2 = it2.next()
        else:
            if elmt1 < elmt2:
                elmt1 = it1.next()
            else:
                elmt2 = it2.next()
                
    # check the last element
    if (elmt1 == elmt2):
        print(elmt1)

def main():
    lst1 = [0, 1, 2, 3, 9, 10]
    lst2 = [1, 2, 6 ,9, 10]
    
    findIntersection(lst1, lst2)

"""
Written 3
"""

class myStack(object):
    """
    myStack
        stack ADT based on list
    """
    def __init__(self):
        self.lst = []
        self.size = 0
        
    def push(self, element):
        self.lst.append(element)
        self.size += 1
    
    def pop(self):
        self.size -= 1
        element = self.lst.pop()
        return element
        
    
    def isEmpty(self):
        return self.size == 0
    
class twoStackQueue(object):
    """
    twoStackQueue
        queue ADT based on two stacks
    """
    def __init__(self):
        self.stack1 = myStack()
        self.stack2 = myStack()
    
    def enqueue(self, element):
        self.stack1.push(element)
        
    def dequeue(self):
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
    
        return self.stack2.pop()
    
    def isEmpty(self):
        return self.stack1.size == 0 and self.stack2.size == 0
    
def main():
    q = twoStackQueue()
    
    q.enqueue('Peter')
    q.enqueue('Paul')
    q.enqueue('Mary')
    print(q.dequeue())
    q.enqueue('Simon')
    q.enqueue('Alvin')
    print(q.dequeue())
    
    while not q.isEmpty():
        print(q.dequeue())
