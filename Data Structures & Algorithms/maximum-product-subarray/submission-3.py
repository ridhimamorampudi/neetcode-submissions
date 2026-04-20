class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax = nums[0]
        currMin = nums[0]

        for num in nums[1:]:
            if num < 0:
                currMax,currMin = currMin,currMax
            
            currMax = max(currMax*num,num)
            currMin = min(currMin*num,num)
            res = max(res,currMax)
        
        return res