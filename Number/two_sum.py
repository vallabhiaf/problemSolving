class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n=len(nums)
        t=0
        dict1={}
        result=[]
        #Save index as per number
        #all numbers are unique
        
        for i in range(n):
            dict1[nums[i]]=i
        
        #Find if complementary is availble
        for i in range(n):
            d=target-nums[i]
            
            if d in dict1:
                index1=dict1[d]
                if index1 != i:
                    return[i,index1]
                
                 
            
        