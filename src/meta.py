from collections import deque as stack

s = stack()
s.append(1)
s.append(2)
# print(s.pop())
# print(s.pop())

from heapq import *

q = [2, 6, 4, 3, 5]
heapify(q)
print(q)
heappush(q,1)
heappush(q,10)
print(q)
print(heappop(q))
