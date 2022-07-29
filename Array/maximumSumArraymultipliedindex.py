class Solution:
    def Maximize(self, a, n): 
        a.sort()
        arr_sum=0
        for i in range(0,n):
            arr_sum=arr_sum+(a[i]*i)
        return(arr_sum%(10**9+7))