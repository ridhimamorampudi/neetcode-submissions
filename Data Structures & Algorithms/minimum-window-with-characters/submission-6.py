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
                    print(visited)
                    if s[temp] in visited:
                        print(f"removing {s[temp]}")
                        visited.remove(s[temp])
                    temp += 1
                print(visited)
                if len(visited) == 0:
                    print(f"temp: {temp} and i:{i}")
                    if temp-i < shortj-shorti:
                        
                        shorti = i
                        shortj = temp
                        print(f"{shortj} and {shorti}")
  
            i+=1

        #print(f"final val: {s[shorti:shortj]}")
        if shortj-shorti == float('inf'): return ""
        return s[shorti:shortj]



        

        

        