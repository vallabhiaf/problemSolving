class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mix= False
        
        for i in range (len(matrix)):
            if matrix[i][0] == 0:
                mix = True
            for  d in range (1,len(matrix[0])):
                if matrix[i][d]==0:
                        matrix[i][0]=0
                        matrix[0][d]=0
        
        
        for i in range (len(matrix)-1,-1,-1):
            for d in range(len(matrix[0])-1,0,-1):
                if matrix[i][0] == 0  or matrix[0][d] == 0:
                    matrix[i][d] = 0
                    
            if mix == True:
                matrix[i][0] = 0
                
            