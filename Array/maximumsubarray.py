class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        finalSum=runningSum=nums[0]
        
        for i in nums[1:]:
            runningSum=max(i,runningSum+i)
            finalSum=max(finalSum,runningSum)


         #kadane   
        return finalSum