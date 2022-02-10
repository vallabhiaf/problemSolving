def transitionPoint(arr, n):
    #Code here
     #Code here
    
    if arr[0] == 1:
        return 0
    if arr[n-1] == 0:
        return -1
    low=0
    high=n-1
    ans=-1
    while high >= low:
        mid = (low+high)//2
        if arr[mid] == 1:
            ans = mid
            high=mid-1
        else:
            low = mid +1
            
    return ans

#{ 
#  Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends