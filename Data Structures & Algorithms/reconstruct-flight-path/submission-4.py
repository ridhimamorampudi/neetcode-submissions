class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)

        #sort the tickers
        tickets.sort()
        #build adjacency list
        for src,dst in tickets:
            adj_list[src].append(dst)
        
        res = ["JFK"]
        #do dfs + backtrack
        def dfs(src):
            #final len has to be tix +1
            if len(res) == len(tickets)+1:
                return True
            
            
            #if it leads no where
            if src not in adj_list:
                return False
            
            #otherwise iterate through temp list
            temp = list(adj_list[src])
            for i,v in enumerate(temp):
                adj_list[src].pop(i)
                res.append(v)

                if dfs(v): return True
                adj_list[src].insert(i,v)
                res.pop()
            return False

        dfs("JFK")
        return res
            


        



        


        