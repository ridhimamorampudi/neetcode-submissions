class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target = (n*(n+1))/2

        sum = 0
        for num in nums:
            sum += num
        
        if sum == target:
            return 0
        else:
            return int(target-sum)

        