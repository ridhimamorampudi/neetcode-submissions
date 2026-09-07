class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for i in range(m)]
        grid[0] = [1]*n
        

        for i in range(1,m):
            for j in range(n):
                if j == 0:
                    grid[i][j] = 1
                    continue
                print(f"i: {i}, j: {j}")
                print(f"{grid[i][j]}")
                if 0<=i-1<m:
                    grid[i][j] += grid[i-1][j]
                if 0<= j-1<n:
                    grid[i][j] += grid[i][j-1]

                    
        print(grid)
                
        return grid[m-1][n-1]
                 

        