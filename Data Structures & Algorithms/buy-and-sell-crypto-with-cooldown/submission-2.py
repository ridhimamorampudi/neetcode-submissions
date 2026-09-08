class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        hold = [0]*n
        hold[0] = -prices[0]
        rest = [0]*n
        sold = [float("-inf")]*n

        for i in range(1,n):
            hold[i] = max(rest[i-1]-prices[i] , hold[i-1])
            sold[i] = hold[i-1]+prices[i]
            rest[i] = max(rest[i-1], sold[i-1])
        return max(hold[n-1],sold[n-1],rest[n-1])
