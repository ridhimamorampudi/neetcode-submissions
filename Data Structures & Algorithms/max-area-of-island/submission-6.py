class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        largest = 0

        def dfs(i,j):
            if i < 0 or j < 0 or i>= m or j >= n or grid[i][j] == 0:
                return 0
            
            dirs = [[1,0],[0,1],[-1,0],[0,-1]]
            grid[i][j] = 0
            area = 1

            for dr,dc in dirs:
                nr,nc = dr+i, dc+j
                area += dfs(nr,nc)
            
            return area
                


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    largest = max(largest,dfs(i,j))
        
        return largest
                
        
        