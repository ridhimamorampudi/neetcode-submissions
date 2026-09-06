class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()
        res = []

        for i in range(rows):
            self.dfs(i,0,pacific)
            self.dfs(i,cols-1,atlantic)
        
        for j in range(cols):
            self.dfs(0,j,pacific)
            self.dfs(rows-1,j,atlantic)
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j]) 
        
        return res
                   


    def dfs(self,i,j,visited):
        if (i,j) in visited:
            return
        
        visited.add((i,j))
        
        if i+1 < len(self.heights) and self.heights[i+1][j] >= self.heights[i][j]:
            self.dfs(i+1,j,visited)
        if i-1 >= 0 and self.heights[i-1][j] >= self.heights[i][j]:
            self.dfs(i-1,j,visited)
        if j+1 < len(self.heights[0]) and self.heights[i][j+1] >= self.heights[i][j]:
            self.dfs(i,j+1,visited)
        if j-1 >= 0 and self.heights[i][j-1] >= self.heights[i][j]:
            self.dfs(i,j-1,visited)




