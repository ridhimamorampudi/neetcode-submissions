class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(i,j):
            dirs = [[1,0],[0,1],[-1,0],[0,-1]]
            grid[i][j] = "*"

            for dr,dc in dirs:
                nr,nc = i+dr,j+dc
                if nr >= 0 and nc >= 0 and nr < m and nc < n and grid[nr][nc] == "1":
                    #print("here")
                    grid[nr][nc] = "*" 
                    dfs(nr,nc)
                           
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    print(grid)
                    count += 1
        return count