from calendar import c
import re
from linkedlist import LinkedList

def removeDouplicate(ll):
    if ll.head is None:
        return
    current_node = ll.head
    visited = {current_node.value}
    while current_node.next:
        if current_node.next.value in visited:
            current_node.next = current_node.next.next
        else:
            visited.add(current_node.next.value)
            current_node = current_node.next
    return ll



# or
def removeDuplicate01(ll):
    if ll.head is None:
        return
    current_node = ll.head
    while current_node:
        runner = current_node
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current_node = current_node.next
    return ll.head 




custome_link_list = LinkedList()
custome_link_list.generate(20,0,100)
print(custome_link_list)
# removeDouplicate(custome_link_list)
removeDuplicate01(custome_link_list)
print(custome_link_list)



