class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # zxyzxyz
        # start = 0
        # end keep traversing
        # set = (z,x,y)
        # set.remove(s[i])
        # set = (x,y)
        # keep moving start until you are after the removed value
        # start += 1
        # end += 1

        start = 0
        res = 0
        cache = set()

        for end in range(len(s)):
            while s[end] in cache:
                cache.remove(s[start])
                start += 1
            cache.add(s[end])
            res = max(res, end-start+1)
        return res



        
        


        