class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(newStr):
            if newStr == "":
                print("here")
                return True
            
            for i in range(len(newStr)): 
                if newStr[:i+1] in wordDict:
                    print(newStr[i+1:])
                    return dfs(newStr[i+1:])
                if i == len(newStr):
                    return False
        
        curr = ""
        for i in range(len(s)):
            curr += s[i]
            if curr in wordDict:
                print(dfs(s[i+1:]))
                if dfs(s[i+1:]):
                    print("here2")
                    return True
        
        return False
        

        

            
            



        