class Solution:
    def uniquePaths(m,n):
        #LAST ROW INITAIZED WITH 1
        row=[1] *n
        #GRID STARTS FROM 0,0
        #ALL ROWS ABOVE LAST ROW
        for i in range (m-1): 
            newRow=[1]*n
            for j in range(n-2,-1,-1):
                newRow[j]=newRow[j+1]+row[j]
            row=newRow
        return row[0]
    
    result=uniquePaths(3,7)
    print(result)