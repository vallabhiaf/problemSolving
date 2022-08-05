class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #differntform of partion
        l,r=0,len(nums)-1
        i=0
        
        def swap(i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            
        while i <= r:
            if nums[i]==0:
                swap(i,l)
                l += 1
            if nums[i]==2:
                swap(i,r)
                r -=1
                i -=1
            
            i +=1
            