from linkedlist import LinkedList

def sumList(llA, llB):
    temp_1 = llA.head 
    temp_2 = llB.head
    carry = 0 
    ll = LinkedList()
    
    while temp_1 or temp_2:
        result = carry
        if temp_1:
            result += temp_1.value
            temp_1 = temp_1.next
        if temp_2:
            result += temp_2.value
            temp_2 = temp_2.next
        ll.add(int(result% 10))
        carry = result /10
    return ll

llA  = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)


llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)

print(llA)
print(llB)

print(sumList(llA, llB))
