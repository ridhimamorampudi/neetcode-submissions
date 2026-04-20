class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        sub = []

        def subset(i,sub):
            if i >= len(nums):
                res.add(tuple(sub))
                return
            
            #include
            sub.append(nums[i])
            subset(i+1,sub)

            #not include
            sub.pop()
            subset(i+1,sub)
        
        nums.sort()
        subset(0,sub)

        return [list(i) for i in res]


        