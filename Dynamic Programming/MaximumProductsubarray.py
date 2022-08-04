class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        #3things to take care 
        #ALL POSITIVE 
        #NEGATIVE taken care by min max  
        #AND ZERO adding i in comaprsion
        #Kadane Dyanmic
        res=max(nums)
        minpro=maxpro=1
        
        for i in nums:
            temp = i * maxpro
            maxpro=max(maxpro*i,minpro*i,i)
            minpro=min(temp,minpro*i,i)
            res = max(maxpro,res)
        
        return res
        