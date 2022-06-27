# given two linked list, we need to determine if the two list intersect with each other
# return the intersecting node 

from audioop import add
from linkedlist import LinkedList, Node 

def intersect(llA, llB):
    if llA.tail is not llB.tail:
        return False
    lenA = len(llA)
    lenB = len(llB)
    
    shorter = llA if lenA < lenB else llB
    longer  = llB if lenA < lenB else llA
    
    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head 
    
    for _ in range(diff):
        longerNode = longerNode.next
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next 
        
    return longerNode


def addSameNode(llA, llB, value):
    temp_node = Node(value)
    llA.tail.next = temp_node
    llA.tail = temp_node
    llB.tail.next = temp_node
    llB.tail = temp_node
    

lla = LinkedList()
lla.generate(3,0,100)

llb = LinkedList()
llb.generate(4,0,100)

addSameNode(lla, llb, 300)
addSameNode(lla, llb, 500)

print(lla)
print(llb)


print(intersect(lla, llb))