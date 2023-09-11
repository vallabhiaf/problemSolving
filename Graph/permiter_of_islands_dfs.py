class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri= 0
        row = len(grid)
        col = len(grid[0])
        visit=set()

        def dfs (r,c):
            if (r not in range(row) or c not in range(col) or grid[r][c] ==0):
                return 1
            if (r,c) in visit:
                return 0    
            visit.add((r,c))
            return  dfs(r+1,c)  + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    return dfs(r,c)

        

        
