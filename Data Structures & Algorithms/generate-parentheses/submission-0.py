class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []
        def paran(openN, closedN):
            if openN == closedN == n:
                res.append("".join(sub))
                return

            #not include
            if openN < n:
                sub.append("(")
                paran(openN+1,closedN)
                sub.pop()
            if closedN < openN:
                sub.append(")")
                paran(openN,closedN+1)
                sub.pop()
        paran(0,0)
        return res
    
