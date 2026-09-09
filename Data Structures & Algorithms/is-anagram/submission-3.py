class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = [0]*26
        dictt = [0]*26
        
        for i in range(len(s)):
            dicts[ord("a")-ord(s[i])]+= 1


        for i in range(len(t)):
            dictt[ord("a")-ord(t[i])]+= 1

        return True if dicts == dictt else False