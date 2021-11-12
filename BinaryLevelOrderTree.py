# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue=[]
        final=[]
        level=[]
        if not root:
            return queue
        queue.append(root)
        
        while queue:
            temp=[]
            for node in queue:
                level.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            final.append(level)
            level=[]
            queue=temp
            
        return final