class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        for brac in s:                
            if stack and brac in hashmap and hashmap[brac] == stack[-1]:
                stack.pop()
                continue
            
            stack.append(brac)
        
        #print(stack)
        
        return False if stack else True
            

                

            

        


        


        