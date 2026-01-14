def factorial(n, acum):
    if n == 1:
        return acum
    return factorial(n-1, acum * n)

print(factorial(3, 1))


def reverse(theString, acum = ""):
    if len(theString) == 0:
        return acum
    head = theString[0]
    tail = theString[1:]
    return reverse(tail, head + acum)

print(reverse("shir"))


# is Odd or even:
def isOdd(number):
    if number == 0:
        return False 
    return not isOdd(number-1)

print(isOdd(11))

def isOddTailCall(number, acum = False):
    if number == 0:
        return acum
    return isOddTailCall(number-1, not acum)

print(isOddTailCall(10))