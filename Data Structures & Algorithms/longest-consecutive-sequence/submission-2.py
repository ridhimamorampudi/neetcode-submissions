class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num-1) not in numSet:
                leng = 1
                while (num+leng) in numSet:
                    leng += 1
                longest = max(leng,longest)
        return longest
            
        