class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        final = []
        def dfs(path):
            nonlocal final
            
            if len(path) == len(nums):
                final.append(path.copy())
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs(path)
                    path.pop()
        
        dfs([])
        return final