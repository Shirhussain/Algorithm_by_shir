class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        

def merge(list1, list2):
    merge_list = Node()
    current = merge_list
    
    while list1 and list2:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    current.next = list1 or list2
    return merge_list.next


def arr_to_linked_list(array):
    if array is None:
        return array
    head = Node(array[0])
    current = head 
    
    for i in range(1, len(array)):
        current.next = Node(array[i])
        current = current.next
    return head 


# lst1 = Node(1)
# lst1.next = Node(3)
# lst1.next.next = Node(5)
# lst1.next.next.next = Node(7)
# lst1.next.next.next.next = Node(9)



# lst2 =Node(0)
# lst2.next = Node(2)
# lst2.next.next = Node(4)
# lst2.next.next.next = Node(6)
# lst2.next.next.next  = Node(8)


# Define the arrays
array1 = [0,2, 4, 6, 8, 10]
array2 = [1, 3, 5, 7, 9]

lst1 = arr_to_linked_list(array1)
lst2 = arr_to_linked_list(array2)


result = merge(lst1, lst2)

while result:
    print( result.value, end = " ")
    result = result.next 
    
    