class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        maxarea = 0
        visit = set()

        def dfs(r,c):
            if r not in range(row) or c not in range (col) or (r,c) in visit or grid[r][c] ==0:
                return 0

            visit.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c)+ dfs(r,c+1)+ dfs(r,c-1)

        for r in range(row):
            for c in range(col):
                maxarea = max(maxarea, dfs(r, c))
        return maxarea


        
