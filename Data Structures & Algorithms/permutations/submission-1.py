class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(curr,pick):

            if len(curr) >= len(nums):
                ans.append(curr.copy())
                return
            
            
            for i in range(len(nums)): 
                if not pick[i]:
                    #include it
                    curr.append(nums[i])
                    pick[i] = True
                    backtrack(curr,pick)
                    #dont include
                    curr.pop()
                    pick[i] = False
            
        ans = []
        pick = [False] *len(nums)
        backtrack([],pick)
        return ans
        

            
            

        