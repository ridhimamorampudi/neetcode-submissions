class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = [0]*n
        hold[0] = -prices[0]
        sell = [0]*n
        
        for i in range(1,n):
            hold[i] = max(hold[i-1],-prices[i])
            sell[i] = max(hold[i-1]+prices[i], sell[i-1])
            
        
        ans =  max(hold[n-1], sell[n-1]) 
        return ans if ans>0 else 0
