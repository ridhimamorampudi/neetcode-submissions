class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = currMin = 1
        total = nums[0]
        
        for i in range(len(nums)):
            temp = currMax*nums[i]
            currMax = max(nums[i],currMax*nums[i],nums[i]*currMin)
            currMin = min(nums[i],currMin*nums[i],temp)
            total = max(total,currMax)
            
            print(f"i: {i}")
            print(f"total: {total}")
            print(f"currMax: {currMax}")
            print(f"currMin: {currMin}")
        
        return total
        

        