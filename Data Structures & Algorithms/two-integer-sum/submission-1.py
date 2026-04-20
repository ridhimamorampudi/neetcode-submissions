class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}

        for i in range(len(nums)):
            sumMap[nums[i]] = i
        
        for i in range(len(nums)):
            if (target-nums[i]) in sumMap:
                if i != sumMap[target-nums[i]]:
                    return [i,sumMap[target-nums[i]]]
        
        return []

        