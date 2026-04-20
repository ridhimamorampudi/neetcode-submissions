class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        hashmap = {}
        p1 = -1
        res = []

        for i in range(len(s)):

            hashmap[s[i]] = hashmap.get(s[i],counter[s[i]])-1
            if hashmap[s[i]] == 0:
                del hashmap[s[i]]
            if not hashmap:
                res.append(i-p1)
                p1 = i
        return res


        