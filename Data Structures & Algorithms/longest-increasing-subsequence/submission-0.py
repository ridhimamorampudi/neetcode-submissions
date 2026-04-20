class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
    
        def helper(i,j):
            if i == len(nums):
                return 0
            
            LIS = helper(i+1,j) #dont include
            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS,1+helper(i+1,i))
                
            return LIS
        
        return helper(0,-1)
        
        



            
        





