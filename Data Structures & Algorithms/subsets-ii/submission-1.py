class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

        def subset(i,sub):
            if i >= len(nums):
                if sub not in res:
                    res.append(sub.copy())
                return
            
            #include
            sub.append(nums[i])
            subset(i+1,sub)

            #not include
            sub.pop()
            subset(i+1,sub)
        
        nums.sort()
        subset(0,sub)

        return res


        