class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setnew = set()

        for i in range (0,len(nums)):
            if nums[i] in setnew:
                return True
            setnew.add(nums[i])
        
        return False

        
