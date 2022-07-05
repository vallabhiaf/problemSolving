# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        #got to each row add the nodes in queue and until the queue is empty keep adding 1 to the depth
        if not root:
            return 0
        
        depth = 0
        queue=[]
        queue.append(root)
        
        while queue:
            depth +=1
            temp=[]
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
            queue=temp
        return depth