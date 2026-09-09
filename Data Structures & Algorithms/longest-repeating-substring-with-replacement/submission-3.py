class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l =0
        cache = defaultdict(int)

        for r in range(len(s)):
            cache[s[r]] += 1

            while (r-l+1) - max(cache.values()) > k:
                cache[s[l]] -= 1
                l += 1
            
            res = max(res,(r-l+1))
            
        return res