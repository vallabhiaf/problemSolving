class Solution:
    def climbStairs(self, n: int) -> int:
        #this one and two zre ways from the a back to reach the top
        #this is a bottom up apprach
        one=two=1
        for i in range(n-1):
            temp=one
            one = one +two
            two =temp
            
        return one