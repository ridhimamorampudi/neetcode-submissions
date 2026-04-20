class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        for i in range(1,len(nums),1):
            ans[i] = nums[i-1]*ans[i-1]
        
        [1,1,2,8]
        
        val = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            ans[i] *= val
            val *= nums[i] 
        return ans
        
        