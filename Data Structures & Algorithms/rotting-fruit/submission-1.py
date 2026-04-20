class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = deque()
        count = 0
        min = 0
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    count += 1
                else:
                    continue
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        while count > 0 and q:
            leng = len(q)
            for i in range(leng):
                r,c = q.popleft()

                for dr,dc in directions:
                    row = r+dr
                    col = c+dc
                    if (row >= 0 and row < n) and (col >= 0 and col < m) and (grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row,col))
                        count -= 1
            min += 1
        
        return min if count == 0 else -1



