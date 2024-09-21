from more_itertools import nth
from linkedlist import LinkedList

# return the nth number of elements from the last you shold count 
def nthToLast(ll, number):
    pointer1 = ll.head 
    pointer2 = ll.head 
    
    for _ in range(number):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


custom_link_list = LinkedList()
custom_link_list.generate(10,0,100)

print(custom_link_list)
print(nthToLast(custom_link_list,4))
