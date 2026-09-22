class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        res = 0
        left = 0
        maxFreq = 0
        
        for r in range(len(s)):
            hashmap[s[r]] += 1
            maxFreq = max(maxFreq,hashmap[s[r]])

            while (r-left+1) - maxFreq > k:
                hashmap[s[left]] -= 1
                left += 1
            res = max(res,r-left+1)
        return res

