# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

    

        

        
        tort = head

        if not tort:
            return False
        
        hare = head.next

        if not hare:
            return False

        while hare and hare.next:
            if hare == tort:
                return True
            
            hare = hare.next.next
            tort=tort.next
        
        return False