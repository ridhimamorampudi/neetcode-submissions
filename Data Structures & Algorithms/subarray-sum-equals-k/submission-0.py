class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currVal = 0
        count = 0
        hashmap= defaultdict(int)
        hashmap[0] = 1

        for i in range(len(nums)):
            currVal += nums[i]

            if currVal - k in hashmap:
                count += hashmap[currVal-k]
            hashmap[currVal] += 1
        
        return count