class Link:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        

def has_cycle(head):
    fast, slow = head, head 
    while fast and fast.next:
        fast = fast.next.next 
        slow = slow.next
        if slow == fast:
            return True
    return False


tail = Link(10)
tail.next =Link(3)
tail.next.next = Link(-4)
tail.next.next.next = tail.next


cycle = has_cycle(tail)
print(cycle)
        
    