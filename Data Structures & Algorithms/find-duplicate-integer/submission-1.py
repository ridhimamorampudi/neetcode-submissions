class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while (left<right):
            mid = left+(right-left)//2
            target = sum(1 for num in nums if num <= mid)

            if target <= mid:
                left = mid+1
            else:
                right = mid
        return left


        