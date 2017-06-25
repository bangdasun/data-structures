### Stack: based on built-in list
#   stack is LIFO
mystack = [3, 4, 6, 7, 2, 1, 5]
mystack

#   push - use append()
mystack.append(9)
mystack.append(0)
mystack

#   pop - use pop()
mystack.pop()
mystack

### Queue: based on deque() in collections
#   queue is FIFO
from collections import deque
myqueue = deque([3, 4, 5, 6, 7])
myqueue

#   enqueue
myqueue.append(2)
myqueue

#   dequeue
myqueue.popleft()
myqueue
