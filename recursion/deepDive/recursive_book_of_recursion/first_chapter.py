def a():
    spam = 'Ant'
    print('spam is ' + spam)
    b()
    print('spam is ' + spam)


def b():
    spam = 'Bobcat'
    print('spam is ' + spam)
    c()
    print('spam is ' + spam)


def c():
    spam = 'Coyote'
    print('spam is ' + spam)


a()


def shortestWithBaseCase(makeRecursiveCall):
    print('shortestWithBaseCase(%s) called.' % makeRecursiveCall)
    if not makeRecursiveCall:
    # BASE CASE
        print('Returning from base case.')
        return
    else:
        # RECURSIVE CASE
        shortestWithBaseCase(False)
        print('Returning from recursive case.')
        return
    
print('Calling shortestWithBaseCase(False):')
shortestWithBaseCase(False)
print()
print('Calling shortestWithBaseCase(True):')
shortestWithBaseCase(True)



def countDownAndUp(number):
    print(number)
    if number == 0:
        # BASE CASE
        print('Reached the base case.')
        return
    else:
        # RECURSIVE CASE
        countDownAndUp(number - 1)
        print(number, 'returning')
        # return
countDownAndUp(3)


def fibonacci(nthNumber):
    print('fibonacci(%s) called.' % (nthNumber))
    if nthNumber == 1 or nthNumber == 2:
        # BASE CASE
        print('Call to fibonacci(%s) returning 1.' % (nthNumber))
        return 1
    else:
        # RECURSIVE CASE
        print('Calling fibonacci(%s) and fibonacci(%s).' % (nthNumber - 1, nthNumber - 2))
        result = fibonacci(nthNumber - 1) + fibonacci(nthNumber - 2)
        print('Call to fibonacci(%s) returning %s.' % (nthNumber, result))
        return result
    
print("\n\n")
print(fibonacci(10))



# factorial with iteration, or recursion in iteration 
print("\n\n\nfactorial with stack ")

callStack = [] # The explicit call stack, which holds "frame objects".
callStack.append({'returnAddr': 'start', 'number': 5}) # "Call" the "factorial() function".
returnValue = None
while len(callStack) > 0:
    # The body of the "factorial() function":
    number = callStack[-1]['number'] # Set number parameter.
    returnAddr = callStack[-1]['returnAddr']
    if returnAddr == 'start':
        if number == 1:
            # BASE CASE
            returnValue = 1
            callStack.pop() # "Return" from "function call".
            continue
        else:
            # RECURSIVE CASE
            callStack[-1]['returnAddr'] = 'after recursive call'
            # "Call" the "factorial() function":
            callStack.append({'returnAddr': 'start', 'number': number - 1})
            continue
    elif returnAddr == 'after recursive call':
        returnValue = number * returnValue
        callStack.pop() # "Return from function call".
        continue
print(returnValue)


print('\n\n\nCode in a loop:')
i = 0
while i < 5:
    print(i, 'Hello, world!')
    i = i + 1
print('Code in a function:')
def hello(i=0):
    print(i, 'Hello, world!')
    i = i + 1
    if i < 5:
        hello(i) # RECURSIVE CASE Recursion vs. Iteration 31
    else:
        return # BASE CASE
hello()



print("\n\n\nneedle in haystack")
def findSubstringIterative(needle, haystack):
    i = 0
    while i < len(haystack):
        if haystack[i:i + len(needle)] == needle:
            return i # Needle found.
        i = i + 1
    return -1 # Needle not found.

def findSubstringRecursive(needle, haystack, i=0):
    if i >= len(haystack):
        return -1 # BASE CASE (Needle not found.)
    if haystack[i:i + len(needle)] == needle:
        return i # BASE CASE (Needle found.)
    else:
        # RECURSIVE CASE
        return findSubstringRecursive(needle, haystack, i + 1)
print(findSubstringIterative('cat', 'My cat Zophie'))
print(findSubstringRecursive('cat', 'My cat Zophie'))



print("\n\n power")
def exponentByIteration(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result
print(exponentByIteration(3, 6))
print(exponentByIteration(10, 3))
print(exponentByIteration(17, 10))


def exponentByRecursion2(a,n):
    result = 1
    
    def helper(i):
        nonlocal result
        if i == n:
            return 
        result *= a 
        helper(i+1)
    helper(0)
    return result

print(exponentByRecursion2(3,6))


def exponentByRecursion(a, n):
    if n == 1:
        # BASE CASE
        return a
    elif n % 2 == 0:
        # RECURSIVE CASE (When n is even.)
        result = exponentByRecursion(a, n // 2)
        return result * result
    elif n % 2 == 1:
        # RECURSIVE CASE (When n is odd.)
        result = exponentByRecursion(a, n // 2)
        return result * result * a
print(exponentByRecursion(3, 6))
print(exponentByRecursion(10, 3))
print(exponentByRecursion(17, 10))


def exponentWithPowerRule(a, n):
    # Step 1: Determine the operations to be performed.
    opStack = []
    while n > 1:
        if n % 2 == 0:
            # n is even.
            opStack.append('square')
            n = n // 2
        elif n % 2 == 1:
            # n is odd.
            n -= 1
            opStack.append('multiply')
            # Step 2: Perform the operations in reverse order.
            result = a # Start result at `a`.
    while opStack:
        op = opStack.pop()
        if op == 'multiply':
            result *= a
        elif op == 'square':
            result *= result
        return result
print(exponentWithPowerRule(3, 6))
print(exponentWithPowerRule(10, 3))
print(exponentWithPowerRule(17, 10))



print("\n\n sum array recursively")
def sum(numbers):
    if len(numbers) == 0: # BASE CASE
        return 0
    else: # RECURSIVE CASE
        head = numbers[0]
        tail = numbers[1:]
        return head + sum(tail)
nums = [1, 2, 3, 4, 5]
print('The sum of', nums, 'is', sum(nums))
nums = [5, 2, 4, 8]

print('The sum of', nums, 'is', sum(nums))
nums = [1, 10, 100, 1000]
print('The sum of', nums, 'is', sum(nums))



print("\n\n reverse string")
def rev(theString):
    if len(theString) == 0 or len(theString) == 1:
    # BASE CASE
        return theString
    else:
        # RECURSIVE CASE
        head = theString[0]
        tail = theString[1:]
        return rev(tail) + head
print(rev('abcdef'))
print(rev('Hello, world!'))
print(rev(''))
print(rev('X'))


def isPalindrome(theString):
    if len(theString) == 0 or len(theString) == 1:
        # BASE CASE
        return True
    else:
        # RECURSIVE CASE
        head = theString[0]
        middle = theString[1:-1]
        last = theString[-1]
        return head == last and isPalindrome(middle)
text = 'racecar'
print(text + ' is a palindrome: ' + str(isPalindrome(text)))
text = 'amanaplanacanalpanama'
print(text + ' is a palindrome: ' + str(isPalindrome(text)))
text = 'tacocat'
print(text + ' is a palindrome: ' + str(isPalindrome(text)))
text = 'zophie'
print(text + ' is a palindrome: ' + str(isPalindrome(text)))


print("\n\n\n ackermann function")
def ackermann(m, n, indentation=None):
    if indentation is None:
        indentation = 0
    print('%sackermann(%s, %s)' % (' ' * indentation, m, n))
    
    if m == 0:
        # BASE CASE
        return n + 1
    elif m > 0 and n == 0:
        # RECURSIVE CASE
        return ackermann(m - 1, 1, indentation + 1)
    elif m > 0 and n > 0:
    # RECURSIVE CASE
        return ackermann(m - 1, ackermann(m, n - 1, indentation + 1), indentation + 1)
print('Starting with m = 1, n = 1:')
print(ackermann(1, 1))
print('Starting with m = 2, n = 3:')
print(ackermann(2, 3))



print("\n\n Tree traversal")
root = {'name': 'Alice', 'children': [{'name': 'Bob', 'children':
[{'name': 'Darya', 'children': []}]}, {'name': 'Caroline',
'children': [{'name': 'Eve', 'children': [{'name': 'Gonzalo',
'children': []}, {'name': 'Hadassah', 'children': []}]}, {'name': 'Fred',
'children': []}]}]}
def find8LetterName(node):
    print(' Visiting node ' + node['name'] + '...')
    # Preorder depth-first search:
    print('Checking if ' + node['name'] + ' is 8 letters...')
    if len(node['name']) == 8: return node['name'] # BASE CASE
    if len(node['children']) > 0:
        # RECURSIVE CASE
        for child in node['children']:
            returnValue = find8LetterName(child)
            if returnValue != None:
                return returnValue

    # Postorder depth-first search:
    # print('Checking if ' + node['name'] + ' is 8 letters...')
    # if len(node['name']) == 8: return node['name'] # BASE CASE
    
    #Value was not found or there are no children.
    return None # BASE CASE
print('Found an 8-letter name: ' + str(find8LetterName(root)))


print("\n\n tree max depth")
root = {'data': 'A', 'children': [{'data': 'B', 'children':
[{'data': 'D', 'children': []}]}, {'data': 'C', 'children':
[{'data': 'E', 'children': [{'data': 'G', 'children': []},
{'data': 'H', 'children': []}]}, {'data': 'F', 'children': []}]}]}
def getDepth(node):
    if len(node['children']) == 0:
        # BASE CASE
        return 0
    else:
        # RECURSIVE CASE
        maxChildDepth = 0
        for child in node['children']:
            # Find the depth of each child node:
            childDepth = getDepth(child)
            if childDepth > maxChildDepth:
                # This child is deepest child node found so far:
                maxChildDepth = childDepth
    return maxChildDepth + 1
print('Depth of tree is ' + str(getDepth(root)))