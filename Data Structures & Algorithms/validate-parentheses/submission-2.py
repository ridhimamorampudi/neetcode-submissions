class Solution:
    def isValid(self, s: str) -> bool:
        paren = {']':'[', 
                '}':'{', 
                ')':'('}

        stack = []
        if s[0] == '}' or s[0] == ']' or s[0] == ')':
            return False
        stack.append(s[0])
        
        for char in s[1:]:
            if char == '{' or char == '[' or char == '(' or not stack:
                stack.append(char)
            else:
                if stack[-1] != paren[char]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True
        


        


        