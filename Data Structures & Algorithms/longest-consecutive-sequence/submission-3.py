class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        23451020
        nums.sort()
        if len(nums)<= 1:
            return len(nums)
        res = 1
        curr = 1

        print(nums)

        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                curr += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                #print(i)
                #print("here")
                res = max(curr,res)
                curr = 1
            #print(curr)
        
        return max(res,curr)




            
        