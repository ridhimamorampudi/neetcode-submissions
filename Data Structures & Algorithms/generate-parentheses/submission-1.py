class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []

        def dfs(openN,closedN):
            if openN==closedN==n:
                res.append("".join(sub))
                return
            
            if openN < n:
                sub.append("(")
                dfs(openN+1,closedN)
                sub.pop()
            if closedN < openN:
                sub.append(")")
                dfs(openN,closedN+1)
                sub.pop()
        
        dfs(0,0)
        return res
