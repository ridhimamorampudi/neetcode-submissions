"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import defaultdict 
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        nodeMap = defaultdict()
        q = deque()

        newHead = Node(node.val)
        nodeMap[node] = newHead
        q.append(node)

        #nodeMap = [old 1:new1]
        #q = [1,2]

        while q:
            currOldNode = q.popleft()
            #old 1

            for Oldneighbor in currOldNode.neighbors:
                if Oldneighbor in nodeMap:
                    nodeMap[currOldNode].neighbors.append(nodeMap[Oldneighbor])
                else:
                    newNeigh = Node(Oldneighbor.val)
                    nodeMap[Oldneighbor] = newNeigh
                    nodeMap[currOldNode].neighbors.append(nodeMap[Oldneighbor])
                    q.append(Oldneighbor)

        return newHead