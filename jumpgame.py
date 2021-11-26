class Solution:
    def canJump(nums):

       #greedy trchniqe
       goal = len(nums)-1

       for i in range (len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal=i

       return True if goal == 0 else False

    
    result=canJump([3,2,2,0,4])
    print (result)