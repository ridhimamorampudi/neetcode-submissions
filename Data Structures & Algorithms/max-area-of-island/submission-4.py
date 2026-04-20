class UnionFind():
    def __init__(self,grid):
        self.parent = []
        self.size = []
        self.maxSize = 0

        n = len(grid)
        m = len(grid[0])

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    self.parent.append(r*m+c)
                    self.size.append(1)
                    self.maxSize = 1
                else:
                   self.parent.append(-1)
                   self.size.append(0)
                
    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
            print(self.size[rootY])
            self.maxSize = max(self.maxSize,self.size[rootY])
    
    def maxsize(self):
        return self.maxSize


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        uf = UnionFind(grid)

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    if r-1 >= 0 and grid[r-1][c] == 1:
                        uf.union((r*m+c),((r-1)*m+c))
                    if r+1 < n and grid[r+1][c] == 1:
                        uf.union((r*m+c),((r+1)*m+c))
                    if c-1 >= 0 and grid[r][c-1] == 1:
                        uf.union((r*m+c),(r*m+(c-1)))
                    if c+1 < m and grid[r][c+1] == 1:
                        uf.union((r*m+c),(r*m+(c+1)))
                grid[r][c] == 0
        return uf.maxsize()



        