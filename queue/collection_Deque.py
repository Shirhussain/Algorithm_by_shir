from calendar import c
from collections import deque

# deque works like cercular queue, with max capacity
custome = deque(maxlen=4)
custome.append(1)
custome.append(2)
custome.append(3)
custome.append(4)
custome.append(5)


custome.popleft()
# custome.clear()
