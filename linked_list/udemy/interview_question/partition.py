from linkedlist import LinkedList

# Write code to partiton a linked list around value x,
# such taht all node less than x come before that and greather than x come after x

def partation(ll, x_number):
    current_node = ll.head 
    ll.tail = ll.head 
    
    while current_node:
        next_node = current_node.next 
        current_node.next = None
        if current_node.value < x_number:
            current_node.next = ll.head 
            ll.head = current_node
        else:
            ll.tail.next = current_node
            ll.tail = current_node
        current_node = next_node
    if ll.tail.next is not None:
        ll.tail.next = None
        

custome_link_list = LinkedList()
custome_link_list.generate(10, 0,100)
print(custome_link_list)
partation(custome_link_list, 50)
print(custome_link_list)
