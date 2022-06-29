import queue as q

custome = q.Queue(maxsize = 5)
print(custome.empty())
# adding
custome.put(1)
custome.put(2)
custome.put(3)
print(custome.qsize())
print(custome.empty())
print(custome.full())
custome.put(4)
custome.put(5)
print(custome.full())
# deleting the first item and returning it
print(custome.get())
print(custome.full())
print(custome.qsize())
