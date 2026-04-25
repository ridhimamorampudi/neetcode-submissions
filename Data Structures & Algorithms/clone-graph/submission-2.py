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
            #pop old curr
            Oldcurr = queue.popleft()
            
            neighbors = Oldcurr.neighbors
            #print([n.val for n in neighbors])
            for n in neighbors:
                
                if n not in visited: #neighbor not already there
                    addN = Node(n.val)
                    queue.append(n)
                    visited[n]=addN
                
                #add to adjacency list of the current node
                
                visited[Oldcurr].neighbors.append(visited[n])
                
                
            #print(currNode.val)
            #print([n.val for n in currNode.neighbors])   

            
        return visited[node]


            
