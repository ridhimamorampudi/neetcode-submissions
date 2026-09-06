class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Pacific = [0,*] or [*,0]
        #Atlantic = [len(heights[0]), *], [len(heights),*]
        

        self.heights = heights

        res = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (self.helperP(i,j,set())) and (self.helperA(i,j,set())):
                    res.append([i,j])
        
        return res



    def helperP(self, i, j, visited):
        if i == 0 or j == 0:
            return True

        if (i, j) in visited:
            return False

        visited.add((i, j))

        if i+1 < len(self.heights) and self.heights[i+1][j] <= self.heights[i][j]:
            if self.helperP(i+1, j, visited):
                return True

        if i-1 >= 0 and self.heights[i-1][j] <= self.heights[i][j]:
            if self.helperP(i-1, j, visited):
                return True

        if j+1 < len(self.heights[0]) and self.heights[i][j+1] <= self.heights[i][j]:
            if self.helperP(i, j+1, visited):
                return True

        if j-1 >= 0 and self.heights[i][j-1] <= self.heights[i][j]:
            if self.helperP(i, j-1, visited):
                return True

        return False

    def helperA(self, i, j, visited):
        if i == len(self.heights)-1 or j == len(self.heights[0])-1:
            return True

        if (i, j) in visited:
            return False

        visited.add((i, j))

        if i+1 < len(self.heights) and self.heights[i+1][j] <= self.heights[i][j]:
            if self.helperA(i+1, j, visited):
                return True

        if i-1 >= 0 and self.heights[i-1][j] <= self.heights[i][j]:
            if self.helperA(i-1, j, visited):
                return True

        if j+1 < len(self.heights[0]) and self.heights[i][j+1] <= self.heights[i][j]:
            if self.helperA(i, j+1, visited):
                return True

        if j-1 >= 0 and self.heights[i][j-1] <= self.heights[i][j]:
            if self.helperA(i, j-1, visited):
                return True

        return False

    