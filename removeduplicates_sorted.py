#This solution does not take extra space
class Solution:
    def removeDuplicates(nums):
        if nums: 
            length=len(nums)
            k=1
            largest=nums[-1]
            for i in range(length-1):
                runner1=i+1
                if nums[i]== largest:
                    break
                
                while runner1 > 0:

                    if runner1 <length: 
                    
                        if nums[runner1] > nums[i]:
                            nums[i+1]=nums[runner1]
                            k=k+1
                            runner1=0
                        

                        else:
                            runner1= runner1+1
                    else:
                        runner1=0
                    
            print(nums) 
                    
                    
            return k    
        else:
            return 0
   