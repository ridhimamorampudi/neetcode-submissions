class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(amount+1):
            
            for coin in coins:
                if i == coin:
                    dp[i]= 1
                if coin < i:
                    dp[i] = min(dp[i-coin]+1,dp[i])
        
                    
        if dp[amount] == float('inf'): return -1 
        return dp[amount]