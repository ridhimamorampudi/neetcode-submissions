# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkSameTree(root,subroot):
            if not root and not subroot:
                return True
            if root and subroot and root.val == subroot.val:
                return checkSameTree(root.left,subroot.left) and checkSameTree(root.right,subroot.right)
            else:
                return False
        
        if not root and subRoot:
            return False
        if root and subRoot and root.val == subRoot.val:
            if checkSameTree(root.left,subRoot.left) and checkSameTree(root.right,subRoot.right):
                return True
            
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        


        
        
    





