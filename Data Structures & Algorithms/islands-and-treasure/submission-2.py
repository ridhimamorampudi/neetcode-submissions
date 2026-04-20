class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m=len(grid)
        n = len(grid[0])
        INF = 2**31-1

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append([i,j])
                
        dirs = [(0,-1),(0,1),(1,0),(-1,0)]

        while queue:
            r,c=queue.popleft()
            for dr,dc in dirs:
                nr,nc = dr+r,dc+c
                if (0 <= nr < m) and (0<=nc<n) and (grid[nr][nc] == INF):
                    grid[nr][nc] = 1+grid[r][c]
                    queue.append([nr,nc])


                

                    



            

        