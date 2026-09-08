class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = [defaultdict(int) for _ in range(len(nums))]

        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1

        res = 0

        for i in range(1,len(nums)):
            
            for sumV,count in dp[i-1].items():
                
                #positive
                dp[i][sumV+nums[i]] += (count)
                #negative
                dp[i][sumV-nums[i]] += (count)
                if sumV+nums[i] == target:
                    res += dp[i][sumV+nums[i]]
                if sumV-nums[i] == target:
                    res += dp[i][sumV-nums[i]]

        return dp[len(nums)-1][target]




        