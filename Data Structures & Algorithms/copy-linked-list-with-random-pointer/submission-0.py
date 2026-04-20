"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        dummy = head
        
        while dummy:
            copyN = Node(dummy.val)
            copyN.next = dummy.next
            dummy.next = copyN
            dummy = copyN.next
        
        newHead = head.next

        p1 = head
        while p1:
            if p1.random:
                p1.next.random = p1.random.next
            p1 = p1.next.next
        
        l1 = head
        while l1:
            l2 = l1.next
            l1.next = l2.next
            if l2.next:
                l2.next = l2.next.next
            l1 = l1.next
            

        return newHead
        



             






        
        
