class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        self.dirs = [[0,1],[1,0],[0,-1],[-1,0]]

        res = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    self.dfs(i,j)
                    res += 1

        return res



    def dfs(self,i,j):
        if self.grid[i][j] == "0":
            return
        
        self.grid[i][j] = "0"
        
        for x,y in self.dirs:
            nr, nc = x+i, y+j
        
            if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]) and self.grid[nr][nc] == "1":
                self.dfs(nr,nc)

        