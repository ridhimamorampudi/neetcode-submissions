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

        hashmap = defaultdict(int)
        res = 0
        curr = 0

        for i in range(len(s)):
            while s[i] in hashmap:
                del hashmap[s[curr]]
                curr += 1
            hashmap[s[i]] += 1
            res = max(res,len(hashmap))
                    
        return res



        
        


        