class Solution:
    def findKthLargest(nums, k):
        
        #Qucik select algo o(n)on average 
        ## easy way is just sort and find len - k
        k = len(nums) - k
        
        def quickselect(l,r):
            pivot=nums[r]
            p=l
            for i in range (l,r):
                if nums[i] <= pivot: 
                    #Easy swapping
                    nums[p],nums[i]=nums[i],nums[p]
                    p +=1
            nums[p],nums[r]=nums[r],nums[p]
                
            if p>k: return quickselect(l,p-1)
            elif p<k : return quickselect(p+1,r)
            else: return nums[p]



        ans=quickselect(0,len(nums)-1)
        print(ans)


    nums=[3,2,3,1,2,4,5,5,6]
    k=4
    findKthLargest(nums,k)