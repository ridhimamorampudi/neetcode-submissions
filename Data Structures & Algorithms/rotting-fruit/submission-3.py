class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        min = 0
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        while fresh > 0 and q:
            length = len(q)

            for i in range(length):
                r,c = q.popleft()
                for dr,dc in dirs:
                    x,y = dr+r, dc+c
                    if 0 <= x < rows and 0<= y <cols and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        q.append((x,y))
            min += 1
        
        if fresh == 0:
            return min 
        else:
            return -1

