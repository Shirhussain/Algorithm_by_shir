from multiprocessing import Queue

custome = Queue(maxsize=3)
custome.put(10)
print(custome.get())
print(custome.qsize())