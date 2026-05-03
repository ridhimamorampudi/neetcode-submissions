class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def dfs(newStr):
            if newStr == "":
                return True
            
            if newStr in memo:
                return memo[newStr]
            
            for i in range(len(newStr)):
                if newStr[:i+1] in wordSet:
                    if dfs(newStr[i+1:]):
                        memo[newStr] = True
                        return True
            memo[newStr] = False
            return False
        
        curr = ""
        for i in range(len(s)):
            curr += s[i]
            if curr in wordSet:
                if dfs(s[i+1:]):
                    return True
        
        return False
                    


        

            
            



        