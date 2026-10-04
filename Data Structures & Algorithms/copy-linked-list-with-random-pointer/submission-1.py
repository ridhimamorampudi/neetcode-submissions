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
        hashmap = defaultdict(lambda:Node(0))
        hashmap[None] = None
       
        #map old node to new node
        currNode = head

        while currNode:
            hashmap[currNode].val = currNode.val
            hashmap[currNode].next = hashmap[currNode.next]
            hashmap[currNode].random = hashmap[currNode.random]
            currNode = currNode.next
        
        return hashmap[head]
        


            
                


        
