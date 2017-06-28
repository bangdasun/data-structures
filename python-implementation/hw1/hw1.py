"""
Programming 1
"""

class Rectangle(object):
    """class Rectangle(object)"""
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.perimeter = 2 * (self.width+self.length)
    
    def getLength(self):
        return self.length
    
    def getWidth(self):
        return self.width
    
    def compareTo(self, object):
        if self.perimeter < object.perimeter:
            return -1
        elif self.perimeter > object.perimeter:
            return 1
        else:
            return 0

rectSmall = Rectangle(1.2, 3.2)
rectSmall.getLength()
rectSmall.getWidth()

rectLarge = Rectangle(2.4, 6.4)

def findMax(lst):
    """
    findMax(...)
        finMax(lst[ Rectangle]) -> Rectangle
        
        return the rectangle with largest perimeter
    """
    maxIdx = 0
    for i in range(1, len(lst)):
        if lst[i].compareTo(lst[maxIdx]) > 0:
            maxIdx = i
    return lst[maxIdx]

# create a list of rectangles
lst = []
lst.append(Rectangle(1, 2))
lst.append(Rectangle(4, 3))
lst.append(Rectangle(5, 1))
lst.append(Rectangle(3, 3))
lst.append(Rectangle(3, 1))
lst

findMax(lst)
