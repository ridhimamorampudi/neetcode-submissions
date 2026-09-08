class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = [defaultdict(int) for _ in range(len(nums))]

        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1

        res = 0

        for i in range(1,len(nums)):
            #positive
            for sumV,count in dp[i-1].items():
                
                dp[i][sumV+nums[i]] += (count)
                if sumV+nums[i] == target:
                    res += 1

            #negative
            
            for sumV,count in dp[i-1].items():
                
                dp[i][sumV-nums[i]] += (count)
            if sumV-nums[i] == target:
                    res += 1
        
        #print(dp)
        return dp[len(nums)-1][target]




        