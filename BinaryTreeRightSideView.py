# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
            stack=[]
            value=[]
            if root:
                stack.append(root)
            else :
                 return []
            
            while stack:
                newStack=[]
                value.append(stack[-1].val)
                
                for n in stack:
                    if n.left:
                        newStack.append(n.left)
                     
                    if n.right:
                        newStack.append(n.right)
                stack=newStack
                
            return value    