"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        visited = {}
        
        dummy = Node();
        queue = deque()
        queue.append(node)
        visited[node] = Node(node.val)
        i = 0;


        while queue:
            Oldcurr = queue.popleft() 
            neighbors = Oldcurr.neighbors
            for n in neighbors:
                if n not in visited: #neighbor not already there
                    addN = Node(n.val)
                    queue.append(n)
                    visited[n]=addN                
                visited[Oldcurr].neighbors.append(visited[n])


            
        return visited[node]


            
