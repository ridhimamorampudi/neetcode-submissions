# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []
        res.append([root.val])

        
        

        while q:
            
            currLevel = []
            for i in range(len(q)):
                
                currNode = q.popleft()
                
                
                if currNode.left:
                    currLevel.append(currNode.left.val)
                    q.append(currNode.left)
                
                if currNode.right:
                    currLevel.append(currNode.right.val)
                    q.append(currNode.right) 
                
            if len(currLevel) > 0:
                res.append(currLevel)


                
        return res

