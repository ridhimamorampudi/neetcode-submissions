# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        #None <- 1 <- 2 -> None

        while curr:
            nextN = curr.next
            curr.next = prev
            prev = curr
            curr = nextN
        
        return prev

            


    # 1 -> 2 -> 3
    # head.next.next = head
    # head.next = dummy