class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map = {}
        ans = []
        for stri in strs:
            temp = tuple(sorted(stri))
            if temp not in Map:
                Map[temp]= [stri]
            else:
                Map[temp].append(stri)
            
        return list(Map.values()) 






        