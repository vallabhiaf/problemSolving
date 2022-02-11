
#MArking method 
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer=[]
        
        for n in nums:  
            n= abs(n)
            if nums[n-1]<0:
                answer.append(n)
            else:
                nums[n-1] = -nums[n-1]
                
        return answer
            