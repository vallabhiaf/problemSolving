class Solution:

    #another solution is sum of natural numbers
    def missingNumber(self, nums: List[int]) -> int:
        len1=len(nums)
        nums.sort()
        i=0
        result=0
        while i < len1:
            if i==nums[i]:
                i +=1
            else:
                result=i
                return result
        if i == len1:
            return i
                
        