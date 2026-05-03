class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = currMin = 1
        total = nums[0]
        
        for i in range(len(nums)):
            oldMax = currMax
            currMax = max(nums[i],currMax*nums[i],nums[i]*currMin)
            currMin = min(nums[i],currMin*nums[i],oldMax*nums[i])
            total = max(total,currMax)

        
        return total
        

        