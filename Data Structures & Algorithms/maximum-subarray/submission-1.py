class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        currSum = 0

        for i in range(len(nums)):
            currSum = max(nums[i],currSum+nums[i])
            largest = max(largest,currSum)
        return largest

