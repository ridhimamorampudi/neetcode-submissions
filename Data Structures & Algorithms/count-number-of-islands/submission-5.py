class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n

    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                self.size[rootY] += self.size[rootX]
                self.parent[rootX] = rootY
            else:
                self.size[rootX] += self.size[rootY]
                self.parent[rootY] = rootX
        return True

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        uf = UnionFind(rows*cols)
        count = 0

        def index(r, c):
            return r * cols + c

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    for x,y in dirs:
                        nr,nc = x+i, j+y
                        if 0 <= nr < rows and 0<= nc < cols and grid[nr][nc] == "1":
                            if uf.union(index(i,j),index(nr,nc)):
                                count -= 1
                            
        
        return count


        