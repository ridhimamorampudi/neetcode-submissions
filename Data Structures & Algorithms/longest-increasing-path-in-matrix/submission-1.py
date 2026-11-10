class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        res = 0
        rows = len(matrix)
        cols = len(matrix[0])
        memo = defaultdict(int)
        


        def dfs(row,col):

            if (row,col) in memo:
                return memo[(row,col)]

            longest = 1

            dirs = [[0,1],[1,0],[0,-1],[-1,0]]

            for d in dirs:
                nr, nc = d[0]+row , d[1]+col

                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] > matrix[row][col]:
                        longest = max(longest,1+dfs(nr,nc))
            memo[(row,col)] = longest
            return longest
        
        for i in range(rows):
            for j in range(cols):
                res = max(res,dfs(i,j))
        return res
                



        