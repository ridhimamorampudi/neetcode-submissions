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
        end = 0
        res = 0
        cache = set()
        n = len(s)

        if s is None or s == " ":
            return len(s)

        while end < n:
            #print(cache)
            #print(res)
            
            if s[end] not in cache:
                cache.add(s[end])
                res = max(res,len(cache))

            else:
                res = max(res,len(cache))
                while s[end] in cache:
                    #print("taking off letters!")
                    #print(cache)
                    if s[start] in cache:
                        cache.remove(s[start])
                    start += 1
                cache.add(s[end])

            end += 1
        
        
        
        return res





        
        


        