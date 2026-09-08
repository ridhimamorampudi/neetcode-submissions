class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0 for i in range(2)] for i in range(n)]

        #do not own a stock
        dp[0][0] = 0

        #i do own a stock
        dp[0][1] = -prices[0]

        dp[1][0] = max(
            dp[0][0],
            dp[0][1] + prices[1]
        )

        dp[1][1] = max(
            dp[0][1],
            -prices[1]
        )

        for i in range(2,n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i])
        return dp[n-1][0]
