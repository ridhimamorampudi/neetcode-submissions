# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        dummy = ListNode(0)
        cur = dummy
        
        heap = []
        for i,lst in enumerate(lists):
            #append val,index of list,node
            if lst:
                heapq.heappush(heap,(lst.val,i,lst))
        
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = ListNode(node.val,node.next)
            cur = cur.next

            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))
        
        return dummy.next

            
        
        