class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            l = i+1
            r = len(nums)-1

            while l < r:
                sumV = nums[l]+nums[r]

                if sumV > target:
                    r -= 1
                elif sumV < target:
                    l += 1
                else:
                    res.append([-target,nums[l],nums[r]])

                    l += 1
                    r -= 1

                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -=1
        return res



        
