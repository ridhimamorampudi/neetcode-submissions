class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text2)
        cols = len(text1)
        dp = [[0 for i in range(cols+1)] for j in range(rows+1)]

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if text1[j] == text2[i]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:        
                    dp[i][j] = max(dp[i][j],dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]

