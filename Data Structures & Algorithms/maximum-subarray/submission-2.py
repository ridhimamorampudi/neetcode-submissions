class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = nums[0]
        total = nums[0]
        for i in range(1,len(nums)):
            total = max(nums[i],total+nums[i])
            currMax = max(total,currMax)

            print(f"total: {total}, currMax: {currMax}")
        
        return currMax
        
        
        #[2,-3,4,-2,2,1,-1,4]