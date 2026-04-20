class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self,a,b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            if self.size[rootA] < self.size[rootB]:
                rootA, rootB=rootB,rootA
            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]
            return True
        else:
            return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges)+1)
        for x,y in edges:
            if not uf.union(x,y):
                return [x,y]
