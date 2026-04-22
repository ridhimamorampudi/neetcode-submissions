class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        grid = [[False] * n for _ in range(n)]
        index = 0
        length = float('-inf')

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j-i<=2 or grid[i+1][j-1]):
                    grid[i][j] = True
                    if j-i+1 > length:
                        length = j-i+1
                        index = i
        return s[index:index+length]
                
         
        




        

                
