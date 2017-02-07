class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

# find cycle in linked list, run two pointers (references) down the list, one slow one fast. if they are equal at any point then there is a cycle
temp = Node(93)
print temp.data
print temp.next

def find_cycles(head):
    slow = head
    fast = head.next
    while slow.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False