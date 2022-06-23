class Solution:
    def climbStairs(self, n: int) -> int:
        
        #Dynamic Programming
        #Approach is final stair it takes 1 step to reach there
        # from n-1 steps it also takes 1 step
        #now from n-2 steps you have two options 
        #either to take one step which will take you to n-1 step
        #or take two steps which will take you to nth step
        #valuesfor both you know you add it
        
        #we solve it by visualizing a descion tree first
        #complexity o(n)
        
        one=two=1
        for i in range(n-1):
            temp=one
            one = one +two
            two= temp
            
        return one 