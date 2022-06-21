
""" Blind 75 
Container with Most water"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
       res=0
       left =0
       length = len(height)
       right = length-1
       
       while left < right:
            res = max((right-left) * min(height[right],height[left]),res)
            if height[right]>= height[left]:
                left +=1
            else:
                right-=1
                
        
       return res