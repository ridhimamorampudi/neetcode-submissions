class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        while(l<=r):
            mid = l+(r-l)//2
            total = 0
            for pile in piles:
                total += math.ceil(float(pile)/mid)
            if total > h:
                l = mid+1
            else:
                res = mid
                r=mid-1
        return res

        #if totalHours is greater 7hr instead of 5hrs:
           # - increase the number of bananas per cycle

        