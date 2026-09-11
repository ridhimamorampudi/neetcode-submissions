class Solution:
    def partition(self, s: str) -> List[List[str]]:
        final = []
        
        def dfs(start,path):
            nonlocal final
            # print(start)
            # print(path)
            if start == len(s):
                final.append(path.copy())
                return
            
            for i in range(start+1,len(s)+1):
                if s[start:i] == s[start:i][::-1]:
                    # print("here")
                    path.append(s[start:i])
                    dfs(i,path)
                    path.pop()
        
        dfs(0,[])
        return final
