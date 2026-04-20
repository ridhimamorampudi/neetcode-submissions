class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxWater = 0

        while(l<r):          
            w = r-l
            h = min(heights[r],heights[l])
            maxWater = max(maxWater,w*h)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxWater
        