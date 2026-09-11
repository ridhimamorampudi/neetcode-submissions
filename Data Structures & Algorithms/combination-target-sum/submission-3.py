class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final = []

        def dfs(i,path,sumV):
            nonlocal final

            #base case:
            if sumV == target:
                final.append(path.copy())
                return
            
            if i >= len(nums) or sumV > target:
                return 
            
            path.append(nums[i])
            dfs(i,path,sumV+nums[i])
            path.pop()
            dfs(i+1,path,sumV)
        
        dfs(0,[],0)

        return final
                    