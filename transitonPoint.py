def transitionPoint(arr, n):
    #Code here
    
    if arr[0] == 1:
        return 0
    if arr[n-1] == 0:
        return -1
    for i in range(0,n):
        if arr[i] == 1:
            return i

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