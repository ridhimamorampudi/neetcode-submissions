from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        counter1 = Counter(s1)

        for i in range(0,m-n+1,1):
            curr = Counter(s2[i:i+n])
            print(curr)
            if curr == counter1:
                return True
        
        return False
