class Solution:
    def numDecodings(self, s: str) -> int:
        #empty string has only 1 way to decode
        dp = {len(s):1}

        #find # of ways to decode from index i
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            dp[i] = dfs(i + 1)
            #cant do dfs(4) if only 3 letters
            if i+1<len(s) and 10 <= int(s[i:i+2]) <= 26:
                dp[i] += dfs(i+2)
            
            return dp[i]
        
        return dfs(0)
        
