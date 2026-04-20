class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        counts = defaultdict(int)
        maxCount = 0
        result = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            maxCount = max(maxCount,counts[s[right]])

            while (right - left + 1) - maxCount > k:
                counts[s[left]] -= 1
                left += 1
        
        result = max(result, right - left + 1)
        return result

        