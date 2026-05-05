class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return t
        
        if len(t) > len(s) or s == "" or t == "":
            return ""
        
        shorti = 0
        shortj= float('inf')
        i = 0
  
        while i < len(s)-len(t)+1:
            #all hits
            if s[i:i+len(t)] == t:
                return s[i:i+len(t)]
            
            visited = list(t)
            
            if s[i] in visited:
                print(s[i])
                visited.remove(s[i])
                temp = i+1

                while temp < len(s) and visited:
                    if s[temp] in visited:
                        visited.remove(s[temp])
                    temp += 1
                if len(visited) == 0:
                    if temp-i < shortj-shorti:
                        shorti = i
                        shortj = temp
  
            i+=1

        if shortj-shorti == float('inf'): return ""
        return s[shorti:shortj]



        

        

        