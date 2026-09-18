# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self,node):
        self.node = node
    def __lt__(self,other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        res = ListNode(0)
        cur = res

        for lst in lists:
            if lst:
                heapq.heappush(heap,NodeWrapper(lst))

        while heap:
            top = heapq.heappop(heap)
            cur.next = top.node
            cur = cur.next

            if top.node.next:
                heapq.heappush(heap,NodeWrapper(top.node.next))
             
        return res.next
        

        
