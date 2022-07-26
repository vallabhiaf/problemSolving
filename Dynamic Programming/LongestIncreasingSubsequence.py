class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        #Bruteforce solution takes 2^n subarray to chevk
        #DP takes on^2
        #Start calculating the subsequence from last number and come down to last and return max of listt
        
        Lis = [1]*len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            for j in range (i+1,len(nums)):
                if nums[j] > nums[i]:
                    Lis[i]=max(Lis[i],1+Lis[j])
                    
        return max(Lis)