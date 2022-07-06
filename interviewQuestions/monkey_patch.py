import monkey

def monkey_fil(self):
    print("monkey_fil()")

monkey.ShirClass.f = monkey_fil
obj = monkey.ShirClass()
obj.f()

# The output for the program will be monkey_fil().