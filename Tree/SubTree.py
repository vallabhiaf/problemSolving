# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root,subRoot):
            return True
        else:
            return (self.isSubtree(root.left,subRoot) or 
                     self.isSubtree(root.right,subRoot))
        
    def sameTree(self,root,subroot):
            if not root and not subroot:
                return True
            if root and subroot and root.val == subroot.val:
                return self.sameTree(root.right,subroot.right) and self.sameTree(root.left,subroot.left)
    