class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        profit = 0

        for p2 in range(len(prices)):
            if prices[p2] < prices[p1]:
                p1 = p2
            
            else:
                profit = max(profit,prices[p2] - prices[p1])
                
        return profit


        
        