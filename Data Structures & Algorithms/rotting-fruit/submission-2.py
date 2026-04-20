class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        time = 0

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while fresh > 0 and q:
            size = len(q)
            for i in range(size):
                r,c = q.popleft()
                for dir in directions:
                    newR = r+dir[0]
                    newC = c+dir[1]
                    if newR>= 0 and newR < n and newC >= 0 and newC < m and grid[newR][newC] == 1:
                        q.append((newR,newC))
                        fresh -= 1
                        grid[newR][newC] = 2
            time += 1
        print(fresh)
        
        

        return time if fresh == 0 else -1

        