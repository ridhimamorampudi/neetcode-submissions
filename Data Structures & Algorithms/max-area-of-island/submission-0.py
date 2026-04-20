class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0

        def dfs(r,c):
            if r>=ROWS or c>=COLS or r< 0 or c<0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return (1
                    + dfs(r + 1, c)
                    + dfs(r - 1, c)
                    + dfs(r, c + 1)
                    + dfs(r, c - 1))
        
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(dfs(r,c),maxArea)
        
        return maxArea