# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #Mirror function to check 
         
    
         def isMirror( root1,root2):
             if not root1 and not root2:
                return True
        
             if root1 and root2 and root1.val == root2.val:
                 return isMirror(root1.left,root2.right) and isMirror(root2.left,root1.right)
        
             return False
         # the whole tree should be a mirror of itself
         return isMirror(root,root)